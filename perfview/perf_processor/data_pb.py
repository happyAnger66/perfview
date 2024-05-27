# Copyright (C) @2024 Cargo Team. All rights reserved.
# Author: zhangxiaoan
# Contact: zhangxiaoan@didiglobal.com
import os.path
import re
import time
import queue
import re
from threading import Thread

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from cargo_monitor_protos.system_info_pb2 import SystemInfo
from .parser.do_msg import TripMsg
from .db.do_db import DataBase
from .db.table_create import trip_info_table_create_sql, \
    node_info_table_create_sql, \
    node_info_table_insert_batch_sql, \
    trip_info_table_insert_batch_sql, \
    cpu_core_info_table_insert_batch_sql, \
    cpu_core_info_table_create_sql, \
    system_total_info_table_create_sql, \
    system_total_info_table_insert_batch_sql, \
    gpu_info_table_create_sql, \
    gpu_info_table_insert_batch_sql, \
    node_info_table_index_sql, \
    cpu_core_info_table_index_sql, \
    system_total_info_table_index_sql, \
    gpu_info_table_index_sql, \
    node_thread_info_table_create_sql, \
    node_thread_info_table_index_sql, \
    node_thread_info_table_insert_batch_sql, \
    node_pub_info_table_create_sql, \
    node_pub_info_table_insert_batch_sql, \
    node_pub_info_table_index_sql, \
    node_sub_info_table_create_sql, \
    node_sub_info_table_index_sql, \
    node_sub_info_table_insert_batch_sql, \
    node_sub_ipc_info_table_create_sql, \
    node_sub_ipc_info_table_insert_batch_sql, \
    node_sub_ipc_info_table_index_sql, \
    disk_info_table_create_sql, \
    disk_info_table_insert_batch_sql, \
    disk_info_table_index_sql, \
    connections_info_table_create_sql, \
    connections_info_table_insert_batch_sql, \
    connections_info_table_index_sql, \
    connections_info_table_index1_sql, \
    connections_info_table_index2_sql, \
    connections_info_table_index3_sql, \
    mem_info_table_create_sql, \
    mem_info_table_insert_batch_sql, \
    mem_info_table_index_sql, \
    table_create_sqls, \
    table_index_sqls, \
    softirqs_info_table_insert_batch_sql, \
    nets_info_table_insert_batch_sql, \
    snmp_udp_info_table_insert_batch_sql, \
    cpu_irq_table_insert_batch_sql


from minio import Minio

TRIPS_ROOT_PATH="/datas"
DB_FILE_PATH="/tmp/db.sqlite3"
RE_PB_FILE = re.compile(r'system_monitor_(.*)_protobuf_(.*)')
RE_FRONT_PB_FILE = re.compile(r'system_monitor_protobuf_(.*)')
WORK_NUMS = 4
queues = []
msgs = []

def get_data_len(data_len):
    num, base = 0, 16
    i = 0
    for item in data_len:
        if i == 0:
            num += int(item)
        else:
            num += int(item) * base
        base *= base
        i += 1
    return num

import logging
def log_init(logfile, is_stdout=False):
    fmt = '[%(asctime)s] %(filename)s:%(lineno)d %(threadName)s %(message)s'
    stream = None
    if is_stdout:
        stream = sys.stdout
        logging.basicConfig(
            level=logging.INFO,
            format=fmt,
            stream=stream)
    else:
        logging.basicConfig(
            filename=logfile,
            level=logging.INFO,
            format=fmt)
    logging.StreamHandler(stream=stream)


def is_my_work(cur_task, task_id, total_task):
    if task_id == total_task and cur_task%task_id == 0:
        return True

    if cur_task % total_task != task_id:
        return False

    return True

def thread_work(task_id, total_task, trip_id, hostname):
    logging.info('thread_work task:%d total_task:%d trip:%s host:%s' %(task_id, total_task, trip_id, hostname))

    do_tasks = 0
    cur_num = 0
    my_msgs = []
    all_nodes_info, cpu_core_infos, st_infos, gpu_infos = [], [], [], []
    node_threads_info, node_pubs_info, node_subs_info = [], [], []
    node_sub_ipc_infos = []
    disk_infos, connection_infos = [], []
    mem_infos, softirq_infos, net_infos, snmp_udp_infos = [], [], [], []
    cpu_irqs = []
    msg_parse = TripMsg(trip_id)
    q = queues[task_id % total_task]
    total_num = q.qsize()
    print('thread_work task:%d total_task:%d trip:%s host:%s num:%d' %(task_id, total_task, trip_id, hostname, total_num))
    while True:
        try:
            data = q.get(timeout=1)
            cur_num+=1
#            if not is_my_work(cur_num, task_id, total_task):
#                continue

            msg = SystemInfo()
            try:
                msg.ParseFromString(data)
            except Exception as e:
                logging.error('parse msg error:%s' % e)
            do_tasks+=1

            try:
                nodes_info = msg_parse.get_nodes_info(hostname, msg.header.timestamp_ns, msg)
                all_nodes_info.extend(nodes_info)
            except Exception as e:
                logging.error('db msg msg error:%s' % e)

            try:
                cpu_core_info = msg_parse.get_cpu_core_info(hostname, msg.header.timestamp_ns, msg)
                cpu_core_infos.extend(cpu_core_info)
            except Exception as e:
                logging.error('db msg cpu_core_info error:%s' % e)

            try:
                st_info = msg_parse.get_system_total_info(hostname, msg.header.timestamp_ns, msg)
                st_infos.extend(st_info)
            except Exception as e:
                logging.error('db msg system total error:%s' % e)

            try:
                gpu_info = msg_parse.get_gpu_info(hostname, msg.header.timestamp_ns, msg)
                gpu_infos.extend(gpu_info)
            except Exception as e:
                logging.error('db msg gpu_info error:%s' % e)

            try:
                node_thread_info = msg_parse.get_node_thread_info(hostname, msg.header.timestamp_ns, msg)
                node_threads_info.extend(node_thread_info)
            except Exception as e:
                logging.error('db msg node_thread_info error:%s' % e)

            try:
                node_pub_info = msg_parse.get_node_pub_infos(hostname, msg.header.timestamp_ns, msg)
                node_pubs_info.extend(node_pub_info)
            except Exception as e:
                logging.error('db msg node_pub_info error:%s' % e)

            try:
                node_sub_info = msg_parse.get_node_sub_infos(hostname, msg.header.timestamp_ns, msg)
                node_subs_info.extend(node_sub_info)
            except Exception as e:
                logging.error('db msg node_sub_info error:%s' % e)

            try:
                node_sub_ipc_info = msg_parse.get_node_sub_ipc_infos(hostname, msg.header.timestamp_ns, msg)
                node_sub_ipc_infos.extend(node_sub_ipc_info)
            except Exception as e:
                logging.error('db msg node_sub_ipc_info error:%s' % e)

            try:
                disk_info = msg_parse.get_disk_infos(hostname, msg.header.timestamp_ns, msg)
                disk_infos.extend(disk_info)
            except Exception as e:
                logging.error('db msg disk_info error:%s' % e)

            try:
                connction_info = msg_parse.get_connection_infos(hostname, msg.header.timestamp_ns, msg)
                connection_infos.extend(connction_info)
            except Exception as e:
                logging.error('db msg connction_info error:%s' % e)

            try:
                mem_info = msg_parse.get_mem_infos(hostname, msg.header.timestamp_ns, msg)
                mem_infos.extend(mem_info)
            except Exception as e:
                logging.error('db msg mem_infos error:%s' % e)

            try:
                softirq_info = msg_parse.get_softirq_infos(hostname, msg.header.timestamp_ns, msg)
                softirq_infos.extend(softirq_info)
            except Exception as e:
                logging.error('db msg softirq_infos error:%s' % e)

            try:
                net_info = msg_parse.get_net_infos(hostname, msg.header.timestamp_ns, msg)
                net_infos.extend(net_info)
            except Exception as e:
                logging.error('db msg net_infos error:%s' % e)

            try:
                snmp_udp_info = msg_parse.get_snmp_udp_infos(hostname, msg.header.timestamp_ns, msg)
                snmp_udp_infos.extend(snmp_udp_info)
            except Exception as e:
                logging.error('db msg snmp_udp_info error:%s' % e)

            try:
                cpu_irq = msg_parse.get_cpu_irq(hostname, msg.header.timestamp_ns, msg)
                cpu_irqs.extend(cpu_irq)
            except Exception as e:
                logging.error('db msg cpu_irq error:%s' % e)

            print("\r", end="")
            progress = cur_num/total_num
#            print('progress:%f' % progress)
            if cur_num%20 == 0:
                print("progress: %d%% " % max(int(progress * 100)-8, 0), end="")
#            my_msgs.append(msg)
#            print('task:%d num:%d seq:%d' % (task_id, cur_num, msg.header.sequence_num))
        except Exception as e:
            logging.info('q empty end. %s' % e)
            break

    with DataBase(DB_FILE_PATH) as db:
        db.execute_many(node_info_table_insert_batch_sql, all_nodes_info)
        db.close()
    print("\rprogress: 93%% ", end="")

    with DataBase(DB_FILE_PATH) as db:
        db.execute_many(cpu_core_info_table_insert_batch_sql, cpu_core_infos)
        db.close()
    print("\rprogress: 94%% ", end="")

    with DataBase(DB_FILE_PATH) as db:
        db.execute_many(system_total_info_table_insert_batch_sql, st_infos)
        db.close()
    print("\rprogress: 95%% ", end="")

    with DataBase(DB_FILE_PATH) as db:
        db.execute_many(gpu_info_table_insert_batch_sql, gpu_infos)
        db.close()
    print("\rprogress: 96%% ", end="")

    with DataBase(DB_FILE_PATH) as db:
        db.execute_many(node_thread_info_table_insert_batch_sql, node_threads_info)
        db.close()

    with DataBase(DB_FILE_PATH) as db:
        db.execute_many(softirqs_info_table_insert_batch_sql, softirq_infos)
        db.close()
    print("\rprogress: 97%% ", end="")

    with DataBase(DB_FILE_PATH) as db:
        db.execute_many(node_pub_info_table_insert_batch_sql, node_pubs_info)
        db.close()

    with DataBase(DB_FILE_PATH) as db:
        db.execute_many(mem_info_table_insert_batch_sql, mem_infos)
        db.close()

    with DataBase(DB_FILE_PATH) as db:
        db.execute_many(snmp_udp_info_table_insert_batch_sql, snmp_udp_infos)
        db.close()

    with DataBase(DB_FILE_PATH) as db:
        db.execute_many(cpu_irq_table_insert_batch_sql, cpu_irqs)
        db.close()
    print("\rprogress: 98%% ", end="")

    with DataBase(DB_FILE_PATH) as db:
        db.execute_many(node_sub_info_table_insert_batch_sql, node_subs_info)
        db.close()

    with DataBase(DB_FILE_PATH) as db:
        db.execute_many(disk_info_table_insert_batch_sql, disk_infos)
        db.close()

    with DataBase(DB_FILE_PATH) as db:
        db.execute_many(connections_info_table_insert_batch_sql, connection_infos)
        db.close()

    with DataBase(DB_FILE_PATH) as db:
        db.execute_many(nets_info_table_insert_batch_sql, net_infos)
        db.close()
    print("\rprogress: 99%% ", end="")

    with DataBase(DB_FILE_PATH) as db:
        db.execute_many(node_sub_ipc_info_table_insert_batch_sql, node_sub_ipc_infos)
        db.close()
    print("\rprogress: 100%% ", end="")
    print("\r\n")
    logging.info('thread_work task:%d total_task:%d do_tasks:%d items:%d' %(task_id, total_task, do_tasks, len(all_nodes_info)))


def get_trip_from_trip_path(trip_path):
    if trip_path.endswith('/'):
        trip_path = trip_path[:-1]
    filename = os.path.basename(trip_path)
    ps = filename.split('_')
    return ps[1] + '_' + ps[2], ps[2]

def get_all_files_in_trip_path(trip_path):
    return [os.path.join(trip_path, file) for file in os.listdir(trip_path)]

def get_trip_from_file(filepath):
    filename = os.path.basename(filepath)
    filename = filename.split('.')[0]
    if not RE_PB_FILE.match(filename) and not RE_FRONT_PB_FILE.match(filename):
        raise Exception('unsupported filetype:%s' % filename)

#    return filename
    re_groups = RE_PB_FILE.match(filename)
    if re_groups is not None and len(re_groups.groups()) == 2:
        return re_groups.groups()[0], re_groups.groups()[1]

    re_groups = RE_FRONT_PB_FILE.match(filename)
    if re_groups is not None and len(re_groups.groups()) == 1:
        return "master", re_groups.groups()[0]

    raise Exception('unsupported filetype:%s' % filename)



def table_init(db):
    db.execute(trip_info_table_create_sql)
    db.execute(node_info_table_create_sql)
    db.execute(cpu_core_info_table_create_sql)
    db.execute(system_total_info_table_create_sql)
    db.execute(gpu_info_table_create_sql)
    db.execute(node_thread_info_table_create_sql)
    db.execute(node_pub_info_table_create_sql)
    db.execute(node_sub_info_table_create_sql)
    db.execute(node_sub_ipc_info_table_create_sql)
    db.execute(disk_info_table_create_sql)
    db.execute(connections_info_table_create_sql)
    db.execute(mem_info_table_create_sql)
    for sql in table_create_sqls:
        db.execute(sql)

    db.execute(node_info_table_index_sql)
    db.execute(cpu_core_info_table_index_sql)
    db.execute(system_total_info_table_index_sql)
    db.execute(gpu_info_table_index_sql)
    db.execute(node_thread_info_table_index_sql)
    db.execute(node_pub_info_table_index_sql)
    db.execute(node_sub_info_table_index_sql)
    db.execute(node_sub_ipc_info_table_index_sql)
    db.execute(disk_info_table_index_sql)
    db.execute(connections_info_table_index_sql)
    db.execute(connections_info_table_index1_sql)
    db.execute(connections_info_table_index2_sql)
    db.execute(connections_info_table_index3_sql)
    db.execute(mem_info_table_index_sql)
    for sql in table_index_sqls:
        db.execute(sql)

def _do_pb_file(filepath, debug=False):
    for i in range(WORK_NUMS):
        queues.append(queue.Queue())

    trip_id, car_no = get_trip_from_trip_path(filepath)
    logging.info("trip_id:%s" % trip_id)

    with DataBase(DB_FILE_PATH) as db:
        table_init(db)
        db.execute_many(trip_info_table_insert_batch_sql,[[trip_id]])

    all_begin_time = time.time()

    for file in get_all_files_in_trip_path(filepath):
        try:
            hostname, filename = get_trip_from_file(file)
        except Exception as e:
            continue

        print("\r\n\r\n")
        print("!!! do file : [ %s ] hostname :%s !!!" % (file, hostname))
        logging.info("!!! do file : [ %s ] hostname :%s !!!" % (file, hostname))

        queues.clear()
        for i in range(WORK_NUMS):
            queues.append(queue.Queue())

        with open(file, 'rb') as f:
            #        content = mmap.mmap(f.fileno(), 0)
            total_items = 0
            data_len = get_data_len(f.read(4))
            begin_time = time.time()
            while data_len > 0:
                data = f.read(data_len)
                total_items += 1
                index = total_items % WORK_NUMS
                queues[index].put(data)
                if debug:
                    print(SystemInfo)
                    msg = SystemInfo()
                    try:
                        msg.ParseFromString(data)
                    except Exception as e:
                        logging.error('parse msg error:%s' % e)
                    print(msg.vehicle_mode.timestamp_ns, msg.vehicle_mode.vehicle_event, msg.vehicle_mode.takeover_ns)
                data_len = get_data_len(f.read(4))
    #            print('items:%d' % total_items)

        if debug:
            return

        task_i = 1
        tasks = []
        with ProcessPoolExecutor(WORK_NUMS) as pool:
            for i in range(WORK_NUMS):
                logging.info('begin worker :%d' % task_i)
                task = pool.submit(thread_work, task_i, WORK_NUMS, trip_id, hostname)
                tasks.append(task)
                task_i += 1

        print('file: [ %s ] total_items:%d cost:%ds' %
              (file, total_items, time.time() - begin_time))
        logging.info('file: [ %s ] total_items:%d cost:%ds' %
              (file, total_items, time.time() - begin_time))

    all_end_time = time.time()
    print('trip: [ %s ] times:%ds' %
      (trip_id, all_end_time - all_begin_time))
    logging.info('trip: [ %s ] times:%ds' %
          (trip_id, all_end_time - all_begin_time))

downloading = False

def check_file_downloaded(filepath, total_size):
    try:
        cur_size = os.stat(filepath).st_size
    except Exception as e:
        return False

    if cur_size == total_size:
        return True

    print("party file found:%s remove and redownload !!!" % filepath)
    os.remove(filepath)
    return False

def download_progress(filepath, total_size):
    time.sleep(3) # wait fetch begin
#    print('download progress:%s %d\r\n' %(filepath, total_size))
    dir_path = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    download_tmp_filename = None
    for file in os.listdir(dir_path):
        if file.startswith(filename):
            download_tmp_filename = os.path.join(dir_path, file)
            break

    if download_tmp_filename is None:
        raise  RuntimeError('can not download file:%s' % filepath)

    delta_size, last_size = 0, 0
    while downloading:
        try:
            cur_size = os.stat(download_tmp_filename).st_size
        except Exception as e:
            break
        progress = cur_size / total_size
        if last_size == 0:
            speed = 0
        else:
            speed = (cur_size - last_size) / MB / 0.5
        print("\rprogress: %d%% speed:%dMB/s" % (max(int(progress * 100), 0), speed), end="")
        time.sleep(0.5)
        last_size = cur_size

MB=1024*1024
def download_trip_data(trip_id, pattern=None):
    trip_download_dir = os.path.join(TRIPS_ROOT_PATH, trip_id)
    try:
        os.system("mkdir -p %s" % trip_download_dir)
    except FileExistsError as e:
        pass

    minio_client = Minio('s3-cargo-inter.didistatic.com',
                         access_key='AKDD00000000000PYBDSF7ZSDL9KID',
                         secret_key='ASDDrsIQBrqftvRhTARPrBQPsRPhwkXqpZWSaSEc',
                         secure=True)
    try:
        if not minio_client.bucket_exists("none_existing_bucket"):
            print("Object storage connected")
    except Exception as e:
        print("Object storage not reachable! You can try download by yourself")
        exit()

    file_nums = 0
    download_threads = []
    for item in minio_client.list_objects('cargo-data', f"{trip_id}/logs/", recursive=False):
#        print(item.object_name)
        name = item.object_name
        filename = os.path.basename(name)
        filesize = item.size
        #print(filename, item.size)
        #, convert_size(item.size))
        if RE_PB_FILE.match(filename) or RE_FRONT_PB_FILE.match(filename):
           if pattern is not None:
               file_re = re.compile(pattern)
               if not file_re.match(filename):
                   print('%s not mattch pattern:%s' % (filename, pattern))
                   continue

           file_download_dir = os.path.join(trip_download_dir, filename)

           if check_file_downloaded(file_download_dir, item.size):
               print('file:%s already exist!' % file_download_dir)
               file_nums+=1
               continue

           print('\r\n downloading %s to %s... size:[%d]MB\r\n' % (filename, file_download_dir, filesize/MB))
           global downloading
           downloading = True
           progress_thread = Thread(target=download_progress, args=(file_download_dir, filesize))
           progress_thread.start()
           minio_client.fget_object('cargo-data', item.object_name, file_download_dir)
           downloading = False
           progress_thread.join()
           file_nums+=1

    if file_nums == 0:
        print('trip: [ %s ] seems has not be uploaded, please check!!!' % trip_id)
        exit()
    return file_nums > 0


import argparse
def main():
    log_init("/var/log/data_db.log")

    parser = argparse.ArgumentParser()
    parser.add_argument("--trip_path", type=str, help="local trip path.")
    parser.add_argument("--trip_id", type=str, help="specify trip_id and auto download.")
    parser.add_argument("--debug", type=bool, default=False, help="debug mode only.")
    parser.add_argument("--filter", type=str, help="filter parse file.")
    args = parser.parse_args()

    if args.trip_id:
        trip_id = args.trip_id
        if not args.trip_id.startswith("BAG"):
            trip_id = "BAG_" + trip_id
        download_trip_data(trip_id, pattern=args.filter)
        _do_pb_file(os.path.join(TRIPS_ROOT_PATH, trip_id))
    elif args.trip_path:
        _do_pb_file(args.trip_path, args.debug)
    else:
        print("you must specify either trip_id or trip_path !!!")


if __name__ == "__main__":
    main()

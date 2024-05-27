# Copyright (C) @2024 Cargo Team. All rights reserved.
# Author: zhangxiaoan
# Contact: zhangxiaoan@didiglobal.com

from collections import namedtuple

NodeInfo = namedtuple('NodeInfo', ['trip_id', 'timestamp', 'node_name', 'hostname', 'pid', 'threads', 'status',
                                   'cpu_used_percent', 'mem_used_percent', 'cpu_user',
                                   'cpu_sys', 'cpu_wait', 'processor', 'read_kb_speed', 'write_kb_speed', 'read_mb', 'write_mb',
                                   'io_delay', 'shm_mem_mb', 'vm_swap_mb', 'schedule_policy', 'priority', 'non_voluntary_cs',
                                   'voluntary_cs', 'minor_fault', 'major_fault', 'sched_run_time',
                                   'sched_wait_time', 'sched_run_speed', 'car_no'])


class TripMsg:
    def __init__(self, trip_id):
        self._trip_id = trip_id
#        self._car_no = int(trip_id.split('_')[-1])

    def get_nodes_info(self, hostname, ts, msg):
        node_tables = []
        for node in msg.node_info:
            status = 'null'
            if node.status:
                status = node.status

#            node_table = NodeInfo(self._trip_id, ts, node.name, hostname, node.pid, node.threads, status,
#                                  node.cpu_used_percent, node.mem_used_percent, node.cpu_user_percent,
#                                  node.cpu_sys_percent, node.cpu_wait_percent, node.processor, node.read_kb_speed,
#                                  node.write_kb_speed, node.read_mbytes, node.write_mbytes,
#                                  node.io_delay, node.rss_shmem, node.vm_swap, node.sched_policy, node.sched_prio,
#                                  node.nonvoluntary_ctxt_switches,
#                                  node.voluntary_ctxt_switches, node.minflt, node.majflt, node.sched_run_time,
#                                  node.sched_wait_time, node.sched_run_cnts,
#                                  self._car_no)
            node_tables.append((self._trip_id, ts, hostname, node.name,
                                node.pid,
                                node.mem_used_percent,
                                node.cpu_used_percent, node.cpu_user_percent, node.cpu_sys_percent, node.cpu_wait_percent,
                                node.write_kb_speed, node.read_kb_speed,
                                node.minflt, node.majflt))
        return node_tables

    def get_cpu_core_info(self, hostname, ts, msg):
        cpu_core_infos = []
        for cpu_info in msg.cpu_info:
            cpu_core_infos.append((self._trip_id, ts, hostname, cpu_info.cpu_name, cpu_info.cpu_percent,
                                   cpu_info.cpu_user_percent, cpu_info.cpu_sys_percent, cpu_info.cpu_wa_percent,
                                   cpu_info.cpu_idle_percent, cpu_info.cpu_si_percent, cpu_info.cpu_hi_percent,
                                   cpu_info.cpu_ni_percent))
        return cpu_core_infos

    def get_system_total_info(self, hostname, ts, msg):
        st_infos = []
        st_infos.append((self._trip_id, ts, hostname, msg.cpu_used_percent, msg.cpu_user_percent,
        msg.cpu_sys_percent, msg.cpu_wa_percent, msg.cpu_si_percent, msg.cpu_hi_percent,
        msg.mem_used_percent, msg.mem_free_size))
        return st_infos

    def get_gpu_info(self, hostname, ts, msg):
        gpu_infos = []
        for gpu in msg.gpu_info:
            gpu_infos.append((self._trip_id, ts, hostname, gpu.name, gpu.temperature, gpu.pwr_usage,
                               gpu.mem_used_percent, gpu.gpu_usage, gpu.gpu_freq_mhz, gpu.gpu_load))

        return gpu_infos

    def get_node_thread_info(self, hostname, ts, msg):
        node_threads_info = []
        for node in msg.node_thread_info:
            status = 'null'
            if node.status:
                status = node.status

            thread_info = (self._trip_id, ts, hostname, node.name, node.pid, node.tid, node.type, status, node.cpu_used_percent, node.cpu_user_percent,
            node.cpu_sys_percent, node.cpu_wait_percent, node.processor, node.read_kb_speed, node.write_kb_speed, node.read_mbytes, node.write_mbytes,
            node.io_delay, node.sched_policy, node.sched_prio, node.nonvoluntary_ctxt_switches,
            node.voluntary_ctxt_switches, node.minflt, node.majflt, node.sched_run_time, node.sched_wait_time, node.sched_run_cnts)
            node_threads_info.append(thread_info)

        return node_threads_info

    def get_node_pub_infos(self, hostname, ts, msg):
        node_pub_infos = []
        for pub_info in msg.node_pub_info:
            node_pub_info = (self._trip_id, ts, hostname, pub_info.node, pub_info.topic, pub_info.hz,
                                        pub_info.max_delta, pub_info.avg_delta, pub_info.max_proc_delta, pub_info.avg_proc_delta)
            node_pub_infos.append(node_pub_info)
        return node_pub_infos

    def get_node_sub_infos(self, hostname, ts, msg):
        node_sub_infos = []
        for sub_info in msg.node_sub_info:
            node_sub_info = (self._trip_id, ts, hostname, sub_info.node, sub_info.topic, sub_info.hz,
                                        sub_info.max_delta, sub_info.avg_delta, sub_info.max_proc_delta, sub_info.avg_proc_delta,
                                        sub_info.max_sched_delta, sub_info.avg_sched_delta)
            node_sub_infos.append(node_sub_info)
        return node_sub_infos

    def get_node_sub_ipc_infos(self, hostname, ts, msg):
        node_sub_ipc_infos = []
        for sub_info in msg.node_sub_info:
            node_sub_ipc_info = (self._trip_id, ts, hostname, sub_info.node, sub_info.topic,
                                               sub_info.avg_ipc, sub_info.min_ipc, sub_info.max_ipc)
            node_sub_ipc_infos.append(node_sub_ipc_info)
        return node_sub_ipc_infos

    def get_disk_infos(self, hostname, ts, msg):
        disk_infos = []
        for disk_info in msg.filesystem_info:
            disk_table_info = (self._trip_id, ts, hostname, disk_info.type, disk_info.total,
                               disk_info.used, disk_info.free, disk_info.used_percent, disk_info.mount_point,
                               disk_info.read_req_speed, disk_info.write_req_speed, disk_info.read_kb_speed,
                               disk_info.write_kb_speed, disk_info.read_wait, disk_info.write_wait, disk_info.aqu_sz,
                               disk_info.util)
            disk_infos.append(disk_table_info)
        return disk_infos

    def get_connection_infos(self, hostname, ts, msg):
        connection_infos = []
        for conn_info in msg.conn_info:
            connection_info = (self._trip_id, ts, hostname, conn_info.nodename, conn_info.topic, conn_info.local_addr,
                                             conn_info.peer_addr, conn_info.direction, conn_info.snd_buf, conn_info.rcv_buf, conn_info.rmem,
                                             conn_info.wmem, conn_info.snd_speed, conn_info.rcv_speed, conn_info.retrans_speed,
                                             conn_info.retrans_rate, conn_info.cwnd, conn_info.un_acked,
                                             conn_info.retrans_segs_speed, conn_info.retrans_segs_total_speed, conn_info.drops)
            connection_infos.append(connection_info)
        return connection_infos

    def get_mem_infos(self, hostname, ts, msg):
        mem_info = msg.mem_detail
        mem_infos = []
        mem_table_info = (self._trip_id, ts, hostname, msg.mem_free_size, msg.mem_used_percent,
                                 msg.mem_avail_size, msg.mem_buffers_size, msg.mem_cached_size, mem_info.active,
                                 mem_info.inactive, mem_info.active_file, mem_info.inactive_file,
                                 mem_info.active_anon, mem_info.inactive_anon, mem_info.dirty, mem_info.writeback,
                                 mem_info.anon_Pages) #, mem_info.mapped,
#                                 mem_info.kreclaimable, mem_info.sreclaimable, mem_info.sunreclaim,
#                                 0, 0, 0, 0, 0, 0,
#                                 0, 0)
        #                                 mem_info.pgin, mem_info.pgout, mem_info.pgfree, mem_info.pswpin, mem_info.pswpout, mem_info.pgscan_kswapd,
        # mem_info.pgscan_direct, mem_info.vmscan_immediate_reclaim)
        mem_infos.append(mem_table_info)
        return mem_infos

    def get_softirq_infos(self, hostname, ts, msg):
        softirqs = []
        for softirq in msg.softirqs:
            soft_irq_info = (self._trip_id, ts, hostname, softirq.cpu, softirq.hi, softirq.timer,
                                    softirq.net_tx, softirq.net_rx, softirq.block, softirq.irq_poll,
                                    softirq.tasklet, softirq.sched, softirq.hrtimer, softirq.rcu)
            softirqs.append(soft_irq_info)
        return softirqs

    def get_net_infos(self, hostname, ts, msg):
        net_infos = []
        for net in msg.net_info:
            net_info = (self._trip_id, ts, hostname, net.name, net.status, net.mtu,
                               net.send_rate, net.rcv_rate, net.send_pkts_rate, net.rcv_pkts_rate,
                        net.drop_in_rate, net.drop_out_rate, net.fifo_in_rate, net.fifo_out_rate,
                        net.err_in_rate, net.err_out_rate)
            net_infos.append(net_info)
        return net_infos

    def get_snmp_udp_infos(self, hostname, ts, msg):
        snmp_udp = msg.snmp_udp
        snmp_udp_info = (self._trip_id, ts, hostname,
                         snmp_udp.in_speed, snmp_udp.out_speed,
                         snmp_udp.in_errs,
                         snmp_udp.rcvbuf_errs, snmp_udp.sndbuf_errs)
        return [snmp_udp_info]

    def get_cpu_irq(self, hostname, ts, msg):
        cpu_irqs = []
        for cpu_irq in msg.cpu_irq:
            cpu_irq_info = (self._trip_id, ts, hostname,
                                  cpu_irq.cpu,
                                  cpu_irq.irq,
                                  cpu_irq.speed)
            cpu_irqs.append(cpu_irq_info)
        return cpu_irqs

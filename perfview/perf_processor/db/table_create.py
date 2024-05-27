# Copyright (C) @2024 Cargo Team. All rights reserved.
# Author: zhangxiaoan
# Contact: zhangxiaoan@didiglobal.com

trip_info_table_create_sql = """
CREATE TABLE trip_info (
    trip_id TEXT, PRIMARY KEY(trip_id)
);
"""

trip_info_table_insert_batch_sql="""
insert into trip_info (trip_id) values (?);
"""

node_info_table_create_sql = """
CREATE TABLE node_info (
    trip_id TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    hostname TEXT NOT NULL,
    name TEXT NOT NULL,
    pid BIGINT NOT NULL,
    mem_total FLOAT,
    cpu_total FLOAT,
    cpu_user FLOAT,
    cpu_sys FLOAT,
    cpu_wait FLOAT,
    write_kb_speed FLOAT,
    read_kb_speed FLOAT,
    minor_fault BIGINT,
    major_fault BIGINT,
    PRIMARY KEY(trip_id, timestamp, hostname, name, pid)
);
"""

node_info_table_index_sql="""
CREATE INDEX nii on node_info (trip_id, hostname);
"""

node_info_table_index_sql1="""
CREATE INDEX nii1 on node_info (name);
"""

node_info_table_insert_batch_sql="""
insert into node_info (trip_id, timestamp, hostname, name,\
pid, \
mem_total, \
cpu_total, cpu_user, cpu_sys, cpu_wait, \
write_kb_speed, read_kb_speed, \
minor_fault, major_fault) \
values (?,?,?,?, \
?, \
?, \
?,?,?,?, \
?,?, \
?,?);
"""

cpu_core_info_table_create_sql = """
CREATE TABLE cpu_core_info (
    trip_id TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    hostname TEXT NOT NULL,
    core TEXT NOT NULL,
    cpu_total FLOAT,
    cpu_user FLOAT,
    cpu_sys FLOAT,
    cpu_wait FLOAT,
    cpu_idle FLOAT,
    cpu_si FLOAT,
    cpu_hi FLOAT,
    cpu_ni FLOAT,
    PRIMARY KEY(trip_id, timestamp, hostname, core)
);
"""

cpu_core_info_table_index_sql="""
CREATE INDEX cci on cpu_core_info (trip_id, hostname);
"""

cpu_core_info_table_insert_batch_sql="""
insert into cpu_core_info (trip_id, timestamp, hostname, core,\
cpu_total, cpu_user, cpu_sys, cpu_wait, \
cpu_idle, cpu_si, \
cpu_hi, cpu_ni) \
values (?,?,?,?, \
?, ?, ?, ?,\
?, ?, ?, ?);
"""


system_total_info_table_create_sql="""
CREATE TABLE system_total_info (
    trip_id TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    hostname TEXT NOT NULL,
    cpu_used_percent FLOAT,
    cpu_user_percent FLOAT,
    cpu_sys_percent FLOAT,
    cpu_wa_percent FLOAT,
    cpu_si_percent FLOAT,
    cpu_hi_percent FLOAT,
    mem_used_percent FLOAT,
    mem_free_size FLOAT,
    PRIMARY KEY(trip_id, timestamp, hostname)
);
"""

system_total_info_table_index_sql="""
CREATE INDEX sti on system_total_info (trip_id, hostname);
"""

system_total_info_table_insert_batch_sql="""
insert into system_total_info (trip_id, timestamp, hostname, \
cpu_used_percent, cpu_user_percent, cpu_sys_percent, \
cpu_wa_percent, cpu_si_percent, \
cpu_hi_percent, mem_used_percent, mem_free_size) \
values (?,?,?, \
?, ?, ?, \
?, ?, \
?,?,?);
"""

gpu_info_table_create_sql="""
CREATE TABLE gpu_info(
    trip_id TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    hostname TEXT NOT NULL,
    name TEXT NOT NULL,
    temp FLOAT,
    pwr_usage FLOAT,
    mem_used_percent FLOAT,
    gpu_usage FLOAT,
    gpu_freq_mhz FLOAT,
    gpu_load FLOAT,
    PRIMARY KEY(trip_id, timestamp, hostname, name)
);
"""

gpu_info_table_insert_batch_sql="""
insert into gpu_info (trip_id, timestamp, hostname, \
name, temp, \
pwr_usage, mem_used_percent, \
gpu_usage, gpu_freq_mhz, gpu_load) \
values (?,?,?, \
?, ?, \
?, ?, \
?,?,?);
"""

gpu_info_table_index_sql="""
CREATE INDEX gii on gpu_info (trip_id, hostname);
"""

node_thread_info_table_create_sql="""
CREATE TABLE node_thread_info (
trip_id TEXT NOT NULL, 
timestamp TEXT NOT NULL, 
hostname TEXT NOT NULL, 
name TEXT, 
pid bigint, 
tid bigint, 
type int, 
status TEXT, 
cpu_used_percent float, 
cpu_user float, 
cpu_sys float, 
cpu_wait float,
processor int, 
read_kb_speed float, 
write_kb_speed float,
read_mb float, 
write_mb float,
io_delay float, 
schedule_policy TEXT, 
priority int, 
non_voluntary_cs bigint, 
voluntary_cs bigint, 
minor_fault bigint, 
major_fault bigint,
sched_run_time bigint, 
sched_wait_time bigint,
sched_run_speed bigint,
PRIMARY KEY(trip_id, timestamp, hostname, name, pid, tid, type));
"""

node_thread_info_table_insert_batch_sql="""
insert into node_thread_info (trip_id, timestamp, hostname, \
name, pid, tid, type, \
status, \
cpu_used_percent, cpu_user, cpu_sys, cpu_wait, \
processor, read_kb_speed, write_kb_speed, \
read_mb, write_mb, io_delay, \
schedule_policy, priority, \
non_voluntary_cs, voluntary_cs, \
minor_fault, major_fault, \
sched_run_time, sched_wait_time, sched_run_speed) \
values (?,?,?, \
?, ?, ?, ?,\
?, \
?, ?, ?, ?, \
?, ?, ?, \
?, ?, ?, \
?, ?, \
?, ?, \
?, ?, \
?,?,?);
"""

node_thread_info_table_index_sql = """
CREATE INDEX ntii on node_thread_info (trip_id, name, hostname);
"""

node_pub_info_table_create_sql="""
CREATE TABLE node_pub_info (
trip_id TEXT NOT NULL, 
timestamp TEXT NOT NULL, 
hostname TEXT NOT NULL, 
name TEXT, 
topic TEXT, 
hz float, 
max_delta float, 
avg_delta float, 
max_proc float, 
avg_proc float, 
PRIMARY KEY(trip_id, timestamp, hostname, name, topic));
"""

node_pub_info_table_insert_batch_sql="""
insert into node_pub_info (trip_id, timestamp, hostname, \
name, topic,
hz, \
max_delta, avg_delta, \
max_proc, avg_proc) \
values (?,?,?, \
?, ?, \
?, \
?, ?, \
?, ?);
"""

node_pub_info_table_index_sql = """
CREATE INDEX npii on node_pub_info (trip_id, name, topic);
"""

node_pub_info_table_index_sql1 = """
CREATE INDEX npii1 on node_pub_info (name);
"""

node_pub_info_table_index_sql2 = """
CREATE INDEX npii2 on node_pub_info (topic);
"""

node_sub_info_table_create_sql="""
CREATE TABLE node_sub_info (
trip_id TEXT NOT NULL, 
timestamp TEXT NOT NULL, 
hostname TEXT NOT NULL, 
name TEXT, 
topic TEXT, 
hz float, 
max_delta float, 
avg_delta float, 
max_proc float, 
avg_proc float, 
max_sched float, 
avg_sched float, 
PRIMARY KEY(trip_id, timestamp, hostname, name, topic));
"""

node_sub_info_table_insert_batch_sql="""
insert into node_sub_info (trip_id, timestamp, hostname, \
name, topic,
hz, \
max_delta, avg_delta, \
max_proc, avg_proc, \
max_sched, avg_sched) \
values (?,?,?, \
?, ?, \
?, \
?, ?, \
?, ?, \
?, ?);
"""

node_sub_info_table_index_sql = """
CREATE INDEX nsii on node_sub_info (trip_id, name, topic);
"""

node_sub_ipc_info_table_create_sql="""
CREATE TABLE node_sub_ipc_info (
trip_id TEXT NOT NULL, 
timestamp TEXT NOT NULL, 
hostname TEXT NOT NULL, 
name TEXT, 
topic TEXT, 
avg_ipc float, 
min_ipc float, 
max_ipc float, 
PRIMARY KEY(trip_id, timestamp, hostname, name, topic));
"""

node_sub_ipc_info_table_insert_batch_sql="""
insert into node_sub_ipc_info (trip_id, timestamp, hostname, \
name, topic,
avg_ipc, min_ipc, \
max_ipc) \
values (?,?,?, \
?, ?, \
?, ?, \
?);
"""

node_sub_ipc_info_table_index_sql = """
CREATE INDEX nsiit on node_sub_ipc_info (trip_id, name, topic);
"""

node_sub_ipc_info_table_index_sql1 = """
CREATE INDEX nsiit1 on node_sub_ipc_info (name);
"""

node_sub_ipc_info_table_index_sql2 = """
CREATE INDEX nsiit2 on node_sub_ipc_info (topic);
"""

disk_info_table_create_sql="""
CREATE TABLE disk_info (
trip_id TEXT NOT NULL, 
timestamp TEXT NOT NULL, 
hostname TEXT NOT NULL, 
name TEXT, 
total float, 
used float, 
free float, 
used_percent float, 
mount_point TEXT,
read_req_speed float,
write_req_speed float,
read_kb_speed float,
write_kb_speed float,
read_wait float,
write_wait float,
aqu_sz float,
util float,
PRIMARY KEY(trip_id, timestamp, hostname, name, mount_point));
"""

disk_info_table_insert_batch_sql="""
insert into disk_info (trip_id, timestamp, hostname, \
name,
total, used, free, used_percent, \
mount_point, \
read_req_speed, write_req_speed, read_kb_speed, write_kb_speed, \
read_wait, write_wait, \
aqu_sz, util) \
values (?,?,?, \
?, 
?, ?, ?, ?, \
?,
?, ?, ?, ?, \
?, ?, \
?, ?);
"""

disk_info_table_index_sql = """
CREATE INDEX dii on disk_info (trip_id, hostname);
"""

connections_info_table_create_sql="""
CREATE TABLE connections_info (
trip_id TEXT NOT NULL, 
timestamp TEXT NOT NULL, 
hostname TEXT NOT NULL, 
name TEXT, 
topic TEXT, 
direction TEXT, 
local_addr TEXT, 
peer_addr TEXT, 
snd_buf bigint,
rcv_buf bigint,
rmem bigint,
wmem bigint,
snd_speed float,
rcv_speed float,
retrans_speed float,
retrans_rate float,
cwnd int,
un_acked bigint,
retrans_segs_speed float,
retrans_segs_total_speed float,
drops bigint,
PRIMARY KEY(trip_id, timestamp, hostname, name, topic, local_addr, peer_addr));
"""

connections_info_table_insert_batch_sql="""
insert into connections_info (trip_id, timestamp, hostname, \
name, topic, \
local_addr, peer_addr, direction, \
snd_buf,  rcv_buf, \
rmem, wmem, snd_speed, rcv_speed, \
retrans_speed, retrans_rate, \
cwnd, un_acked, \
retrans_segs_speed, retrans_segs_total_speed, \
drops) \
values (?,?,?, \
?, ?, \
?, ?, ?, \
?, ?, \
?, ?, ?, ?, \
?, ?, \
?, ?, \
?, ?,\
?);
"""

connections_info_table_index_sql = """
CREATE INDEX cii on connections_info (trip_id, hostname);
"""

connections_info_table_index1_sql = """
CREATE INDEX cii1 on connections_info (trip_id, hostname, name, topic);
"""

connections_info_table_index2_sql = """
CREATE INDEX cii2 on connections_info (trip_id, hostname, name);
"""

connections_info_table_index3_sql = """
CREATE INDEX cii3 on connections_info (trip_id, hostname, topic);
"""

connections_info_table_index4_sql = """
CREATE INDEX cii4 on connections_info (trip_id);
"""

mem_info_table_create_sql="""
CREATE TABLE mem_info (
trip_id TEXT NOT NULL, 
timestamp TEXT NOT NULL, 
hostname TEXT NOT NULL, 
free float, 
used_percent float, 
avail float, 
buffers float, 
cached float, 
active float,
inactive float,
active_file float,
inactive_file float,
active_anon float,
inactive_anon float,
dirty float,
writeback float,
anon_pages float,
PRIMARY KEY(trip_id, timestamp, hostname));
"""

mem_info_table_insert_batch_sql="""
insert into mem_info (trip_id, timestamp, hostname, \
free, used_percent, \
avail, buffers, cached, \
active, inactive, \
active_file, inactive_file, \
active_anon, inactive_anon, \
dirty, writeback, \
anon_pages) \
values (?,?,?, \
?, ?, \
?, ?, ?, \
?, ?, \
?, ?, \
?, ?, \
?, ?, \
?);
"""

mem_info_table_index_sql = """
CREATE INDEX mii on mem_info (trip_id, hostname);
"""

softirqs_info_table_create_sql="""
CREATE TABLE softirqs_info (
trip_id TEXT NOT NULL, 
timestamp TEXT NOT NULL, 
hostname TEXT NOT NULL, 
name TEXT NOT NULL, 
hi float, 
timer float, 
net_tx float, 
net_rx float, 
block float, 
irq_poll float,
tasklet float,
sched float,
hrtimer float,
rcu float,
PRIMARY KEY(trip_id, timestamp, hostname, name));
"""

softirqs_info_table_insert_batch_sql="""
insert into softirqs_info (trip_id, timestamp, hostname, \
name, \
hi, timer, \
net_tx, net_rx, \
block, irq_poll, \
tasklet, sched, \
hrtimer, rcu) \
values (?,?,?, \
?, \
?, ?, \
?, ?, \
?, ?, \
?, ?, \
?, ?); 
"""

softirqs_info_table_index_sql = """
CREATE INDEX sqi on softirqs_info (trip_id, hostname);
"""

nets_info_table_create_sql="""
CREATE TABLE nets_info (
trip_id TEXT NOT NULL, 
timestamp TEXT NOT NULL, 
hostname TEXT NOT NULL, 
name TEXT NOT NULL, 
status TEXT, 
mtu bigint,
send_speed float, 
rcv_speed float, 
send_pkts_speed float, 
rcv_pkts_speed float, 
drop_in_rate float, 
drop_out_rate float, 
fifo_in_rate float, 
fifo_out_rate float, 
err_in_rate float, 
err_out_rate float, 
PRIMARY KEY(trip_id, timestamp, hostname, name));
"""

nets_info_table_insert_batch_sql="""
insert into nets_info (trip_id, timestamp, hostname, \
name, \
status, \
mtu, \
send_speed, rcv_speed, \
send_pkts_speed, rcv_pkts_speed, \
drop_in_rate, drop_out_rate, \
fifo_in_rate, fifo_out_rate, \
err_in_rate, err_out_rate \
) \
values (?,?,?, \
?, \
?, \
?, \
?, ?, \
?, ?, \
?, ?, \
?, ?, \
?, ?); 
"""

nets_info_table_index_sql = """
CREATE INDEX nsi on nets_info (trip_id, hostname);
"""

snmp_udp_info_table_create_sql="""
CREATE TABLE snmp_udp_info (
trip_id TEXT NOT NULL, 
timestamp TEXT NOT NULL, 
hostname TEXT NOT NULL, 
in_speed float, 
out_speed float, 
in_errs bigint, 
rcvbuf_errs float, 
sndbuf_errs float, 
PRIMARY KEY(trip_id, timestamp, hostname));
"""

snmp_udp_info_table_insert_batch_sql="""
insert into snmp_udp_info (trip_id, timestamp, hostname, \
in_speed, out_speed, \
in_errs, \
rcvbuf_errs, sndbuf_errs \
) \
values (?,?,?, \
?, ?, \
?, \
?, ?); 
"""

snmp_udp_info_table_index_sql = """
CREATE INDEX suii on snmp_udp_info (trip_id, hostname);
"""

cpu_irq_table_create_sql="""
CREATE TABLE cpu_irq (
trip_id TEXT NOT NULL, 
timestamp TEXT NOT NULL, 
hostname TEXT NOT NULL, 
cpu text, 
irq text, 
speed float, 
PRIMARY KEY(trip_id, timestamp, hostname, cpu, irq));
"""

cpu_irq_table_insert_batch_sql="""
insert into cpu_irq (trip_id, timestamp, hostname, \
cpu, irq, \
speed \
) \
values (?,?,?,\
?,?,\
?);
"""

cpu_irq_table_index_sql = """
CREATE INDEX cii on cpu_irq (trip_id, hostname, cpu);
"""

cpu_irq_table_index_sql1 = """
CREATE INDEX cii1 on cpu_irq (trip_id, hostname);
"""

table_create_sqls = [softirqs_info_table_create_sql,
                     nets_info_table_create_sql,
                     snmp_udp_info_table_create_sql,
                     cpu_irq_table_create_sql]
table_index_sqls = [softirqs_info_table_index_sql,
                    nets_info_table_index_sql,
                    snmp_udp_info_table_index_sql,
                    cpu_irq_table_index_sql, cpu_irq_table_index_sql1,
                    node_pub_info_table_index_sql1, node_pub_info_table_index_sql2,
                    node_info_table_index_sql1,
                    node_sub_ipc_info_table_index_sql1, node_sub_ipc_info_table_index_sql2,
                    connections_info_table_index_sql, connections_info_table_index1_sql, connections_info_table_index2_sql,
                    connections_info_table_index3_sql, connections_info_table_index4_sql]

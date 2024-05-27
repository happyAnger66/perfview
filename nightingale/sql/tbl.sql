--
-- PostgreSQL database dump
--

-- Dumped from database version 11.7
-- Dumped by pg_dump version 11.7

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: timescaledb; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS timescaledb WITH SCHEMA public;


--
-- Name: EXTENSION timescaledb; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION timescaledb IS 'Enables scalable inserts and complex queries for time-series data';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: cpu_core_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cpu_core_info (
    "timestamp" timestamp without time zone NOT NULL,
    hostname text NOT NULL,
    car_no integer NOT NULL,
    trip_id text NOT NULL,
    core text NOT NULL,
    cpu_total numeric,
    cpu_user numeric,
    cpu_sys numeric,
    cpu_idle numeric,
    cpu_wait numeric,
    cpu_si numeric,
    cpu_hi numeric,
    cpu_ni numeric
);


ALTER TABLE public.cpu_core_info OWNER TO postgres;

--
-- Name: cpu_load_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cpu_load_info (
    "timestamp" timestamp without time zone NOT NULL,
    car_no integer NOT NULL,
    trip_id text NOT NULL,
    hostname text NOT NULL,
    core smallint NOT NULL,
    load_avg_1 numeric,
    load_avg_5 numeric,
    load_avg_15 numeric,
    cs bigint,
    procs bigint
);


ALTER TABLE public.cpu_load_info OWNER TO postgres;

--
-- Name: disk_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.disk_info (
    "timestamp" timestamp without time zone NOT NULL,
    hostname text NOT NULL,
    car_no integer NOT NULL,
    trip_id text NOT NULL,
    name text NOT NULL,
    total numeric,
    used numeric,
    free numeric,
    used_percent numeric,
    mount_point text NOT NULL,
    read_req_speed numeric,
    write_req_speed numeric,
    read_kb_speed numeric,
    write_kb_speed numeric,
    read_wait numeric,
    write_wait numeric,
    aqu_sz numeric,
    util numeric
);


ALTER TABLE public.disk_info OWNER TO postgres;

--
-- Name: do_trip_bag; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.do_trip_bag (
    trip_id text NOT NULL,
    bag_file text NOT NULL,
    result smallint
);


ALTER TABLE public.do_trip_bag OWNER TO postgres;

--
-- Name: mem_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mem_info (
    "timestamp" timestamp without time zone NOT NULL,
    hostname text NOT NULL,
    car_no integer NOT NULL,
    trip_id text NOT NULL,
    free numeric,
    used_percent numeric,
    avail numeric,
    buffers numeric,
    cached numeric,
    active numeric,
    inactive numeric,
    active_file numeric,
    inactive_file numeric,
    active_anon numeric,
    inactive_anon numeric,
    dirty numeric,
    writeback numeric,
    anon_pages numeric,
    mapped numeric,
    kreclaimable numeric,
    sreclaimable numeric,
    sunreclaim numeric,
    pgin bigint,
    pgout bigint,
    pgscan_kswapd bigint,
    pgscan_direct bigint
);


ALTER TABLE public.mem_info OWNER TO postgres;

--
-- Name: driver_event; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.driver_event_info (
    "timestamp" timestamp without time zone NOT NULL,
    hostname text NOT NULL,
    trip_id text NOT NULL,
    driver_event smallint NOT NULL,
    takeover_ts timestamp without time zone
);


ALTER TABLE public.driver_event_info OWNER TO postgres;


--
-- Name: nets_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.nets_info (
    "timestamp" timestamp without time zone NOT NULL,
    hostname text NOT NULL,
    trip_id text NOT NULL,
    name text NOT NULL,
    status text NOT NULL,
    mtu bigint,
    send_speed numeric,
    rcv_speed numeric,
    send_pkts_speed numeric,
    rcv_pkts_speed numeric
);


ALTER TABLE public.nets_info OWNER TO postgres;

--
-- Name: node_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.node_info (
    "timestamp" timestamp without time zone NOT NULL,
    car_no integer NOT NULL,
    trip_id text NOT NULL,
    node_name text NOT NULL,
    hostname text NOT NULL,
    pid bigint NOT NULL,
    threads bigint,
    status text,
    cpu_used_percent numeric,
    mem_used_percent numeric,
    cpu_user numeric,
    cpu_sys numeric,
    cpu_wait numeric,
    processor smallint,
    read_kb_speed numeric,
    write_kb_speed numeric,
    read_mb numeric,
    write_mb numeric,
    io_delay numeric,
    shm_mem_mb numeric,
    vm_swap_mb numeric,
    schedule_policy text,
    priority smallint,
    non_voluntary_cs bigint,
    voluntary_cs bigint,
    minor_fault bigint,
    major_fault bigint,
    sched_run_time numeric,
    sched_wait_time numeric,
    sched_run_speed numeric
);


ALTER TABLE public.node_info OWNER TO postgres;

--
-- Name: node_pub_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.node_pub_info (
    "timestamp" timestamp without time zone NOT NULL,
    trip_id text NOT NULL,
    name text NOT NULL,
    topic text NOT NULL,
    hostname text NOT NULL,
    hz numeric,
    max_delta numeric,
    avg_delta numeric,
    max_proc numeric,
    avg_proc numeric
);


ALTER TABLE public.node_pub_info OWNER TO postgres;

--
-- Name: node_sub_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.node_sub_info (
    "timestamp" timestamp without time zone NOT NULL,
    trip_id text NOT NULL,
    name text NOT NULL,
    topic text NOT NULL,
    hostname text NOT NULL,
    hz numeric,
    max_delta numeric,
    avg_delta numeric,
    max_proc numeric,
    avg_proc numeric,
    max_sched numeric,
    avg_sched numeric
);


ALTER TABLE public.node_sub_info OWNER TO postgres;

--
-- Name: node_thread_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.node_thread_info (
    "timestamp" timestamp without time zone NOT NULL,
    car_no integer NOT NULL,
    trip_id text NOT NULL,
    name text NOT NULL,
    hostname text NOT NULL,
    pid bigint NOT NULL,
    tid bigint NOT NULL,
    type smallint NOT NULL,
    status text,
    cpu_used_percent numeric,
    cpu_user numeric,
    cpu_sys numeric,
    cpu_wait numeric,
    processor smallint,
    read_kb_speed numeric,
    write_kb_speed numeric,
    read_mb numeric,
    write_mb numeric,
    io_delay numeric,
    schedule_policy text,
    priority smallint,
    non_voluntary_cs bigint,
    voluntary_cs bigint,
    minor_fault bigint,
    major_fault bigint,
    sched_run_time bigint,
    sched_wait_time bigint,
    sched_run_speed bigint
);


ALTER TABLE public.node_thread_info OWNER TO postgres;

--
-- Name: perf_auto_drive_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.perf_auto_drive_info (
    trip_id text NOT NULL,
    "timestamp" timestamp without time zone NOT NULL,
    drive_mode smallint
);


ALTER TABLE public.perf_auto_drive_info OWNER TO postgres;

--
-- Name: perf_e2e; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.perf_e2e (
    "timestamp" timestamp without time zone NOT NULL,
    trip_id text NOT NULL,
    total_latency smallint,
    topdown_detections_ipc smallint,
    topdown_detections_sched smallint,
    topdown_detections_proc smallint,
    mot_tracks_ipc smallint,
    mot_tracks_sched smallint,
    mot_tracks_proc smallint,
    pred_obstacles_ipc smallint,
    pred_obstacles_sched smallint,
    pred_obstacles_proc smallint,
    planner_traj_ipc smallint,
    planner_traj_sched smallint,
    planner_traj_proc smallint,
    control_ipc smallint,
    control_sched smallint,
    control_proc smallint,
    auto_driver_mode smallint,
    car_no integer NOT NULL
);


ALTER TABLE public.perf_e2e OWNER TO postgres;

--
-- Name: perf_trip_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.perf_trip_info (
    trip_id text NOT NULL,
    bag_name text,
    git_info text,
    result smallint
);


ALTER TABLE public.perf_trip_info OWNER TO postgres;

--
-- Name: perf_trip_item_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.perf_trip_item_info (
    trip_id text NOT NULL,
    item text NOT NULL,
    result text NOT NULL,
    items bigint
);


ALTER TABLE public.perf_trip_item_info OWNER TO postgres;

--
-- Name: softirqs_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.softirqs_info (
    "timestamp" timestamp without time zone NOT NULL,
    hostname text NOT NULL,
    trip_id text NOT NULL,
    name text NOT NULL,
    hi numeric,
    timer numeric,
    net_tx numeric,
    net_rx numeric,
    block numeric,
    irq_poll numeric,
    tasklet numeric,
    sched numeric,
    hrtimer numeric,
    rcu numeric
);


ALTER TABLE public.softirqs_info OWNER TO postgres;

--
-- Name: trip_detail; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.trip_detail (
    trip_id text NOT NULL,
    git_commit text,
    git_branch text,
    task integer,
    uuid text,
    start_ts bigint,
    end_ts bigint,
    driving_status text,
    vehicle_type smallint
);


ALTER TABLE public.trip_detail OWNER TO postgres;

--
-- Name: trip_events; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.trip_events (
    trip_id text NOT NULL,
    event text NOT NULL,
    "timestamp" timestamp without time zone NOT NULL,
    distance numeric,
    gps_lat numeric,
    gps_long numeric,
    val integer
);


ALTER TABLE public.trip_events OWNER TO postgres;

--
-- Name: cpu_core_info cpu_core_info_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cpu_core_info
    ADD CONSTRAINT cpu_core_info_pkey PRIMARY KEY ("timestamp", trip_id, car_no, hostname, core);


--
-- Name: cpu_load_info cpu_load_info_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cpu_load_info
    ADD CONSTRAINT cpu_load_info_pkey PRIMARY KEY ("timestamp", trip_id, car_no, hostname, core);


--
-- Name: disk_info disk_info_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.disk_info
    ADD CONSTRAINT disk_info_pkey PRIMARY KEY ("timestamp", trip_id, hostname, name, mount_point);


--
-- Name: do_trip_bag do_trip_bag_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.do_trip_bag
    ADD CONSTRAINT do_trip_bag_pkey PRIMARY KEY (trip_id, bag_file);


--
-- Name: mem_info mem_info_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mem_info
    ADD CONSTRAINT mem_info_pkey PRIMARY KEY ("timestamp", trip_id, hostname);


--
-- Name: driver_event_info driver_event_info_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.driver_event_info
    ADD CONSTRAINT driver_event_info_pkey PRIMARY KEY ("timestamp", trip_id, hostname, driver_event);


--
-- Name: nets_info nets_info_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.nets_info
    ADD CONSTRAINT nets_info_pkey PRIMARY KEY ("timestamp", trip_id, hostname, name);


--
-- Name: node_info node_info_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.node_info
    ADD CONSTRAINT node_info_pkey PRIMARY KEY ("timestamp", trip_id, node_name, hostname, pid);


--
-- Name: node_pub_info node_pub_info_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.node_pub_info
    ADD CONSTRAINT node_pub_info_pkey PRIMARY KEY ("timestamp", trip_id, hostname, name, topic);


--
-- Name: node_sub_info node_sub_info_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.node_sub_info
    ADD CONSTRAINT node_sub_info_pkey PRIMARY KEY ("timestamp", trip_id, hostname, name, topic);


--
-- Name: node_thread_info node_thread_info_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.node_thread_info
    ADD CONSTRAINT node_thread_info_pkey PRIMARY KEY ("timestamp", trip_id, name, hostname, pid, tid, type);


--
-- Name: perf_auto_drive_info perf_auto_drive_info_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perf_auto_drive_info
    ADD CONSTRAINT perf_auto_drive_info_pkey PRIMARY KEY (trip_id, "timestamp");


--
-- Name: perf_e2e perf_e2e_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perf_e2e
    ADD CONSTRAINT perf_e2e_pkey PRIMARY KEY (trip_id, "timestamp");


--
-- Name: perf_trip_info perf_trip_info_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perf_trip_info
    ADD CONSTRAINT perf_trip_info_pkey PRIMARY KEY (trip_id);


--
-- Name: perf_trip_item_info perf_trip_item_info_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perf_trip_item_info
    ADD CONSTRAINT perf_trip_item_info_pkey PRIMARY KEY (trip_id, item);


--
-- Name: softirqs_info softirqs_info_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.softirqs_info
    ADD CONSTRAINT softirqs_info_pkey PRIMARY KEY ("timestamp", trip_id, hostname, name);


--
-- Name: trip_detail trip_detail_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trip_detail
    ADD CONSTRAINT trip_detail_pkey PRIMARY KEY (trip_id);


--
-- Name: trip_events trip_events_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trip_events
    ADD CONSTRAINT trip_events_pkey PRIMARY KEY (trip_id, "timestamp", event);


--
-- Name: npi_trip_index; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX npi_trip_index ON public.node_pub_info USING btree (trip_id);


--
-- Name: npi_trip_name_index; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX npi_trip_name_index ON public.node_pub_info USING btree (trip_id, name);


--
-- Name: nti_trip_index; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX nti_trip_index ON public.node_thread_info USING btree (trip_id);


--
-- Name: nti_trip_name_index; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX nti_trip_name_index ON public.node_thread_info USING btree (trip_id, name);


--
-- Name: trip_index; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX trip_index ON public.node_pub_info USING btree (trip_id);


--
-- PostgreSQL database dump complete
--


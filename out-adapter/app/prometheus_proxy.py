import logging

import requests
import json
import copy

from flask import (
    Blueprint, current_app, request, jsonify
)

from .prom_proxy.metrics import METRICS
from .prom_proxy.pysql import DBOper
from .prom_proxy.result import Result, Metric
from .prom_proxy.db_utils import get_table_from_sql

bp = Blueprint('prometheus_proxy', __name__, url_prefix='/api/v1')

PROMETHEUS_TIME_OFFSET = 3600 * 8
logger = logging.getLogger('proxy')

@bp.route('/label/auto_drive_mode/values', methods=['GET'])
def get_ad_values():
    data = {
        'status': 'success',
        'data': ['all',
                 'auto'
            ]
    }
    return jsonify(data)

@bp.route('/label/filter_text/values', methods=['GET'])
def get_filter_text_values():
    data = {
        'status': 'success',
        'data': ['pose',
                 'lidar_localization',
            ]
    }
    return jsonify(data)

@bp.route('/label/cpu/values', methods=['GET'])
def get_cpu_values():
    data = {
        'status': 'success',
        'data': ['CPU0',
                 'CPU1',
                 'CPU2',
                 'CPU3',
                 'CPU4',
                 'CPU5',
                 'CPU7',
                 'CPU8',
                 'CPU9',
                 'CPU10',
                 'CPU11',
                 'CPU12',
                 ]
    }
    return jsonify(data)

@bp.route('/label/timerange_flag/values', methods=['GET'])
def get_timerange_flag_values():
    data = {
        'status': 'success',
        'data': ['all', 'timerange']
    }
    return jsonify(data)

@bp.route('/label/peer_addr/values', methods=['GET'])
def get_peer_addr_values():
    data = {
        'status': 'success',
        'data': ['192.168.5.11',
                 '192.168.5.16',
                 '192.168.5.32',
                 '192.168.5.48',
                 '192.168.5.64']
    }
    return jsonify(data)


@bp.route('/label/slice_modules/values', methods=['GET'])
def get_slice_modules_values():
    data = {
        'status': 'success',
        'data': ['planner',
                 'prediction',
                 'lidar_pipeline_static_map',
                 'lidar_pipeline_rv_detector',
                 'lidar_pipeline_td_detector',
                 'fusion_object_detection_node',
                 'camera_object_detection_node',
                 'camera_object_detection_node_cam5689',
                 'camera_object_detection_node_fisheye',
                 'CViz']
    }
    return jsonify(data)


@bp.route('/label/im_branch/values', methods=['GET'])
def get_im_branch_values():
    cfg = current_app.config
    db_str = cfg["POSTGRESQL_CONNECTION"]
    with DBOper(db_str) as db:
        branchs = db.query_datas(
            "trip_detail",
            ["git_branch"],
            conditions="git_branch like 'development%' or git_branch like 'release2%'",
            distinct=True)
    data = {
        'status': 'success',
        'data': branchs['git_branch']
    }
    return jsonify(data)


@bp.route('/label/sensor_reason/values', methods=['GET'])
def get_sensor_reason_values():
    cfg = current_app.config
    db_str = cfg["POSTGRESQL_CONNECTION"]
    with DBOper(db_str) as db:
        sensors = db.query_datas(
            "sensor_status_info",
            ["reason"],
            order_by="order by reason desc",
            distinct=True)
    data = {
        'status': 'success',
        'data': sensors['reason']
    }
    return jsonify(data)


@bp.route('/label/sensor_name/values', methods=['GET'])
def get_sensor_name_values():
    cfg = current_app.config
    db_str = cfg["POSTGRESQL_CONNECTION"]
    with DBOper(db_str) as db:
        sensors = db.query_datas(
            "sensor_status_info",
            ["sensor_name"],
            order_by="order by sensor_name desc",
            distinct=True)
    data = {
        'status': 'success',
        'data': sensors['sensor_name']
    }
    return jsonify(data)


@bp.route('/label/ad_v/values', methods=['GET'])
def get_ad_v_values():
    modes = [1, 0]
    data = {
        'status': 'success',
        'data': modes
    }
    return jsonify(data)


@bp.route('/label/auto_drive_mode/values', methods=['GET'])
def get_auto_drive_mode_values():
    modes = ['enable', 'disable']
    data = {
        'status': 'success',
        'data': modes
    }
    return jsonify(data)


@bp.route('/label/car_type/values', methods=['GET'])
def get_car_type_values():
    car_types = ['x86', 'orin', 'all']
    data = {
        'status': 'success',
        'data': car_types
    }
    return jsonify(data)


@bp.route('/label/branchs/values', methods=['GET'])
def get_branchs_values():
    #cfg = current_app.config
    #db_str = cfg["POSTGRESQL_CONNECTION"]
    # with DBOper(db_str) as db:
    #    datas = db.query_datas(
    #        "node_thread_info",
    #        ["name"],
    #        distinct=True)
    branchs = ['development', 'release20230228']
    data = {
        'status': 'success',
        'data': branchs
    }

    return jsonify(data)


@bp.route('/label/thread_names/values', methods=['GET'])
def get_thread_names_values():
    #cfg = current_app.config
    #db_str = cfg["POSTGRESQL_CONNECTION"]
    # with DBOper(db_str) as db:
    #    datas = db.query_datas(
    #        "node_thread_info",
    #        ["name"],
    #        distinct=True)
    threads = ['(at128_lidar_nod)', '(lidar_to_lidar_)', '(fusion_localiza)', '(cargo_monitor_n)',
               '(livox_ros_drive)', '(perception_lida)', '(light_monitor_m)',
               '(air_bridge)', '(detect_followin)', '(gap_distance_fu)',
               '(planner_main)', '(recorder_node)', '(hulk_diagnostic)',
               '(lead_control)', '(lidar_localizat)', '(perception_came)',
               '(hulk_statistics)', '(safety_surrogat)', '(prediction_node)',
               '(monitor_cmd)', '(voice_play)', '(gnss_driver_nod)', '(v2x_remote_cmd)',
               '(bywire_chassis)', '(dynamic_lidar_t)', '(platoon_manager)', '(monitor)',
               '(v2x)', '(v2x_lose_rate)', '(imu_to_vehicle_)', '(trailer_pose)', '(chassis_fusion)',
               '(hulk_estimation)', '(roslaunch)', '(multi_object_tr)',
               '(grpcpp_sync_ser)', '(hulk_control)', '(leimou_f30_node)',
               '(tracker)',
               '(front_agent_tra)', '(sensor_check)',
               '(backup_planner)',
               ]
    data = {
        'status': 'success',
        'data': threads
    }
    # data = {
    #    'status': 'success',
    #    'data': ["at128_lidar_nod", "air_bridge", "bywire_chassis",
    #             "cargo_monitor_n", "categraf",
    #             "chassis_fusion", "detect_followin", "front_agent_tra",
    #             "gap_distance_fu", "gnss_driver_nod", "hulk_diagnostic",
    #             "hulk_estimation", "hulk_control",
    #             "irq", "kworker",
    #             "voice_play", "launchpad", "/tracker",
    #             "lead_control", "monitor",
    #             "monitor_cmd", "/safety_surrogate/safety_surrogate", "/alpas/localization/lidar_localization",
    #             "/alpas/platoon_manager/platoon_manager", "/alpas/drivers/v2x/v2x",
    #             ]
    # }

    return jsonify(data)


@bp.route('/label/ident/values', methods=['GET'])
def get_ident_values():
    data = {
        'status': 'success',
        'data': ["10001", "10002", "10003",
                 "10004", "10005", "10006",
                 "10007", "10008", "10009",
                 "10010", "10011", "10012",
                 "10013", "10014", "10015",
                 "10016", "10017", "10018",
                 "10019", "10020", "10021",
                 "10022", "10023", "10024",
                 "10025", "10026", "10027",
                 "10028", "10029", "10030",
                 "10031", "10032", "10033",
                 "10034", "10035", "10036",
                 "10037", "10038", "10039",
                 "10040", "10041", "10042",
                 "10043", "10044", "10045",
                 "10046", "10047", "10048",
                 ]
    }

    return jsonify(data)

@bp.route('/label/dst_addr/values', methods=['GET'])
def get_dst_addr_values():
    data = {
        'status': 'success',
        'data': ["192.168.5.16", "192.168.5.32", "192.168.5.48",
                 "192.168.5.64", "192.168.5.11"
                 ]
    }

    return jsonify(data)

@bp.route('/label/hostname/values', methods=['GET'])
def get_hostname_values():
    data = {
        'status': 'success',
        'data': ["master", "slave", "orin_0",
                 "orin_1", "orin_2", "orin_3",
                 ]
    }

    return jsonify(data)

@bp.route('/label/trip_item/values', methods=['GET'])
def get_perf_e2e_trips():
    cfg = current_app.config
    db_str = cfg["POSTGRESQL_CONNECTION"]
    with DBOper(db_str) as db:
        datas = db.query_datas(
            "trip_info",
            ["trip_id"],
            order_by="order by trip_id desc")
    data = {
        'status': 'success',
        'data': datas["trip_id"]
    }
    return jsonify(data)

@bp.route('/label/git_branch/values', methods=['GET'])
def get_git_branchs():
    cfg = current_app.config
    db_str = cfg["POSTGRESQL_CONNECTION"]
    with DBOper(db_str) as db:
        datas = db.query_datas("trip_detail;", ["git_branch"], distinct=True)

#    branchs = [branch for branch in datas['git_branch'] if branch.startswith(
#        'release') or branch.find('development') != -1]
    data = {
        'status': 'success',
        'data': datas['git_branch']
    }

#    print(branchs)
    return jsonify(data)


@bp.route('/label/sub_node/values', methods=['GET'])
def get_sub_node():
    # cfg = current_app.config
    # db_str = cfg["POSTGRESQL_CONNECTION"]
    # with DBOper(db_str) as db:
    #    datas = db.query_datas("node_sub_info", ["name"], distinct=True)

    nodes = ['/alpas/control/hulk_control/hulk_control', '/cviz', '/alpas/v2x_remote_cmd/v2x_remote_cmd',
             'default', '/alpas/monitor/monitor', '/chassis_fusion',
             '/alpas/localization/trailer_pose/trailer_pose',
             'core', '/alpas/control/hulk_diagnostic/hulk_diagnostic',
             '/alpas/control/hulk_estimation/hulk_estimation',
             '/lead_control', '/cargo/control/hulk_statistics/hulk_statistics',
             '/v2x_remote_cmd', '/cargo/calibration/imu_to_vehicle_check',
             '/alpas/chassis/bywire/bywire_chassis',
             '/alpas/localization/gap_distance_fusion/gap_distance_fusion', 'lidar',
             '/detect_following', '/alpas/drivers/v2x/v2x_lose_rate',
             '/alpas/drivers/voice_play/voice_play', '/leimou_f30_node',
             '/alpas/hmi/air_bridge/air_bridge',
             '/tracker', '/alpas/remote_control/lead_control/lead_control', '/front_agent_tracker',
             '/camera_object_detection_node', '/v2x',
             '/fusion_localization', '/planner_main', '/bywire_chassis',
             '/lidar_pipeline', '/safety_surrogate/safety_surrogate',
             '/lidar_localization',
             '/alpas/platoon_manager/platoon_manager', '/prediction',
             '/alpas/drivers/v2x/v2x', '/monitor_summary', 'camera', '/platoon_manager',
             '/monitor_summary_orin_0',
             '/monitor_summary_orin_1',
             '/monitor_summary_orin_2',
             '/monitor_summary_orin_3',
             '/fusion_object_detection_node',
             '/front_car_lane_process',
             '/lane_localization',
             '/sensor_check',
             '/backup_planner',
             'cmw_bench_sub',
             'cmw_bench_pub',
             '/cmw_bench_sub',
             '/cmw_bench_pub',
            '/lidar_pipeline_static_map',
            'lidar_pipeline_static_map'
             ]
    data = {
        'status': 'success',
        'data': nodes
    }

    return jsonify(data)

@ bp.route('/label/topics/values', methods=['GET'])
def get_topics_values():
    cfg = current_app.config
    db_str = cfg["POSTGRESQL_CONNECTION"]
    with DBOper(db_str) as db:
        datas = db.query_datas("node_pub_info", ["topic"], distinct=True)

    data = {
        'status': 'success',
        'data': datas['topic']
    }

    return jsonify(data)


@ bp.route('/label/pub_node/values', methods=['GET'])
def get_pub_node():
    cfg = current_app.config
    db_str = cfg["POSTGRESQL_CONNECTION"]

    with DBOper(db_str) as db:
        datas = db.query_datas("node_thread_info", ["name"], distinct=True)

    data = {
        'status': 'success',
        'data': datas['name']
    }

    return jsonify(data)

@bp.route('/label/connection_node/values', methods=['GET'])
def get_connections_node():
    cfg = current_app.config
    db_str = cfg["POSTGRESQL_CONNECTION"]

    with DBOper(db_str) as db:
        datas = db.query_datas("connections_info", ["name"], distinct=True)

    data = {
        'status': 'success',
        'data': datas['name']
    }

    return jsonify(data)

@bp.route('/label/topic_nodes/values', methods=['GET'])
def get_topic_nodes_names():
    cfg = current_app.config
    db_str = cfg["POSTGRESQL_CONNECTION"]

    with DBOper(db_str) as db:
        datas = db.query_datas("node_pub_info", ["name"], distinct=True)

    data = {
        'status': 'success',
        'data': datas['name']
    }

    return jsonify(data)

@bp.route('/label/topic_sub_nodes/values', methods=['GET'])
def get_topic_sub_nodes_names():
    cfg = current_app.config
    db_str = cfg["POSTGRESQL_CONNECTION"]

    with DBOper(db_str) as db:
        datas = db.query_datas("node_sub_info", ["name"], distinct=True)

    data = {
        'status': 'success',
        'data': datas['name']
    }

    return jsonify(data)

@bp.route('/label/node_names/values', methods=['GET'])
def get_node_names():
    cfg = current_app.config
    db_str = cfg["POSTGRESQL_CONNECTION"]

    with DBOper(db_str) as db:
        datas = db.query_datas("node_info", ["name"], distinct=True)

    data = {
        'status': 'success',
        'data': datas['name']
    }

    return jsonify(data)


@bp.route('/label/sub_topic/values', methods=['GET'])
def get_sub_topic():
    #cfg = current_app.config
    #db_str = cfg["POSTGRESQL_CONNECTION"]
    # with DBOper(db_str) as db:
    #    datas = db.query_datas("node_sub_info", ["topic"], distinct=True)

    topics = ['/alpas/driverless/heartbeat_to_mcu', '/traffic_light_sensor_objects_camera_10',
              '/alpas/monitor/system_status', '/alpas/monitor/control_status',
              '/alpas/camera_front_right_1/image_raw/pb_image', '/alpas/platoon_manager/flags_event',
              '/alpas/monitor/system_info', '/alpas/hmi/air_bridge/statistics', '/perception/topdown_detections',
              '/perception/camera_7_segmentation', '/alpas/planning/decider/decider_result',
              '/perception/camera_10_lane_detect', '/alpas/v2x/v2x_cmd/platoon_cmd',
              '/alpas/platoon_manager/mileage_statistics', '/perception/camera_10_object_list',
              '/alpas/planning_trajectory_gap_distance_topic_fusion_debug',
              '/alpas/camera_front_left_1/image_raw/pb_image', '/perception/camera_11_segmentation', '/scan',
              '/alpas/remote_control/lead_control/to_hmi_L2_rsp', '/autonomy/hulk_control/ori_reference_path_info',
              '/alpas/v2x/v2x_cmd/platoon_cmd_resp', '/alpas/planning/trajectory_planner/gap_distance',
              '/alpas/monitor/system_error_info', '/perception/camera_17_object_list', '/traffic_light_detect',
              '/alpas/hmi/air_bridge/weight_setting', '/cargo/autolabel/sceneinfo', '/alpas/monitor/runtimer/control_mainfunction_warning',
              '/alpas/monitor/topic_monitor_summary_warning', '/perception/camera_7_lane_detect',
              '/alpas/monitor/prediction_status', '/alpas/monitor/sensor_monitor/state', '/cargo/planning/debug',
              '/cargo/perception/front_agent_tracker_status', '/perception/camera_6_lane_detect', '/gps_imu_data',
              '/alpas/v2x/v2x_monitor/monitor_l_r_cycle_tx',
              '/alpas/v2x/v2x_monitor/monitor_m_cycle_tx',
              '/alpas/platoon_manager/external_vehicle',
              '/alpas/planning/trajectory_planner/path_history',
              '/alpas/camera_fisheye_right/image_raw/pb_image', '/perception/toll_gate_result',
              '/alpas/v2x/v2x_app/v2x_others_tx', '/perception/camera_8_object_list', '/perception/lidar_pipeline_status',
              '/autonomy/hulk_control/reference_path_info', '/alpas/chassis/chassis_info_timeout',
              '/tf', '/alpas/monitor/lidar_rm_status', '/perception/camera_8_lane_detect', '/alpas/monitor/bywire_chassis_status',
              '/alpas/localization/trailer_angle', '/raw_gps_data', '/perception/lidar_lane', '/pose_chassis',
              '/perception/camera_12_segmentation', '/traffic_light_detect/status', '/alpas/monitor/lidar_lr_status',
              '/perception/camera_5_object_list', '/alpas/hmi/air_bridge/platoon_cmd', '/perception/camera_13_segmentation',
              '/alpas/remote_control/lead_control/from_hmi_req', '/pose_base', '/alpas/planning/scene/scene_info',
              '/cargo/lidar/left/front', '/cargo/safety_surrogate/timetocollision', '/alpas/v2x/v2x_app/v2x_others_tx_base',
              '/perception/camera_13_object_list', '/alpas/planning/decider/decider_debug', '/alpas/drivers/lidar/livox0',
              '/traffic_light_sensor_objects_camera_7', '/perception/camera_6_object_list', '/alpas/control/diagnostic_info',
              '/alpas/camera_front_right/image_raw/pb_image', '/alpas/platoon_manager/vehicle_status',
              '/alpas/hmi/air_bridge/platoon_cmd_resp', '/alpas/monitor/lidar_rr_status',
              '/alpas/planning_trajectory_gap_distance_topic_fusion_gnss', '/alpas/monitor/others_error_info',
              '/perception/camera_14_segmentation', '/perception/camera_9_object_list', '/perception/camera_5_lane_detect',
              '/cargo/lidar/right/front', '/cargo/control/control_info', '/perception/lidar_clusters', '/alpas/planning/decider/decider_info',
              '/alpas/control/control_status', '/cargo/localization/lidar_localization_error', '/perception/camera_8_segmentation',
              '/system_info', '/perception/camera_9_lane_detect', '/perception/lidar_camera_fusion_detections',
              '/alpas/v2x/v2x_cmd/rx_info', '/alpas/camera_fisheye_front/image_raw/pb_image',
              '/alpas/control/control_notice', '/f30_scan', '/prediction/prediction_obstacles',
              '/perception/camera_5_segmentation', '/alpas/planner/platoon_debug_info', '/perception/mot_tracks',
              '/alpas/platoon_manager/platoon_status', '/alpas/planning/planner/status_info',
              '/perception/camera_4_segmentation', '/cargo/localization/toll_gate_center_line',
              '/alpas/camera_front/image_raw/pb_image', '/cargo/lidar/right/rear', '/perception/lidar_rangeview_detections',
              '/alpas/camera_front_left/image_raw/pb_image', '/alpas/v2x/v2x_cmd/tx_info',
              '/alpas/remote_control/vehicle_status_to_remote', '/perception/camera_11_object_list',
              '/alpas/platoon_manager/front_vehicle', '/cargo/localization/pose', '/alpas/camera_fisheye_left/image_raw/pb_image',
              '/alpas/camera_front_1/image_raw/pb_image', '/alpas/monitor/lidar_lf_status',
              '/prediction/prediction_obstacles_debug', '/alpas/camera_front_left_2/image_raw/pb_image',
              '/alpas/v2x/v2x_monitor/monitor_info', '/perception/camera_4_object_list',
              '/prediction/prediction_debug_information', '/pose', '/cargo/control/control_statistics',
              '/alpas/monitor/runtimer/waypoint_process', '/alpas/v2x/v2x_lose_rate', 'f30_scan',
              '/alpas/planning_trajectory_gap_distance_topic_fusion', '/alpas/v2x/v2x_interface/v2x_l_tx',
              '/alpas/camera_front_right_2/image_raw/pb_image', '/alpas/platoon_manager/external_platoon', '/perception/camera_12_object_list',
              '/traffic_light_sensor_objects_camera_4', '/perception/camera_6_segmentation',
              '/cargo/lidar/status', '/alpas/monitor/lidar_rf_status',
              '/perception/static_grid', '/alpas/drivers/voice_play/play', '/perception/camera_10_segmentation',
              '/alpas/monitor/runtimer/mpc_calc_time', '/alpas/v2x/v2x_monitor/monitor_l_r_tx',
              '/alpas/control/vehicle_states_estimation', '/perception/camera_14_object_list', '/alpas/monitor/system_info_cmd',
              '/perception/camera_18_object_list', '/cargo/localization/detect_following_info', '/perception/camera_9_segmentation',
              '/alpas/monitor/recorder_node_0_status', '/autonomy/hulk_control/predict_path_info', '/autonomy/hulk_control/debug_info',
              '/cargo/perception/front_agent_track_info', '/alpas/v2x/v2x_app/v2x_ego_tx', '/alpas/remote_control/lead_control/to_sys_req',
              '/alpas/v2x/v2x_interface/v2x_rx', '/alpas/chassis/chassis_info_rx', '/alpas/planning/planner/trajectory_info',
              '/alpas/driverless/heartbeat_to_ipc', '/alpas/v2x/v2x_interface/v2x_r_tx', '/perception/tracker_status',
              '/alpas/monitor/runtimer/control_mainfunction', '/perception/camera_4_lane_detect',
              '/alpas/remote_control/lead_control/to_hmi_rsp', '/cargo/lidar/left/rear',
              '/perception/camera_7_object_list', '/cargo/prediction/status', '/alpas/monitor/topic_monitor_summary',
              '/alpas/v2x/v2x_monitor/monitor_m_tx', '/alpas/drivers/voice_play/status', '/cargo/lidar/front/middle',
              '/alpas/monitor/lidar_fm_status',
              '/perception/camera_14_lane_detect', '/perception/camera_11_lane_detect',
              '/v2x_lane_info', '/cargo/localization/lane_debug_info', '/cargo/localization/pose_lane',
              '/perception/camera_14_lane_detect',
              '/perception/camera_15_lane_detect',
              '/cargo/sensors_info',
              '/system_info_orin_0',
              '/system_info_orin_1',
              '/system_info_orin_2',
              '/system_info_orin_3',
              '/bench_size_128',
              '/bench_size_256',
              '/bench_size_512',
              '/bench_size_1K',
              '/bench_size_2K',
              '/bench_size_4K',
              '/bench_size_8K',
              '/bench_size_16K',
              '/bench_size_32K',
              '/bench_size_64K',
              '/bench_size_128K',
              '/bench_size_256K',
              '/bench_size_512K',
              '/bench_size_1M',
              '/bench_size_2M',
              '/bench_size_3M',
              '/bench_size_4M',
              '/bench_size_7M',
              '/bench_size_8M',
              '/bench_size_15M',
              '/bench_size_16M',
              '/bench_size_31M',
              '/bench_size_32M',
              '/bench_size_63M',
              '/bench_size_64M',
              '/cargo/autolabel/platooninginfo',
              ]
    data = {
        'status': 'success',
        'data': topics
    }

    return jsonify(data)


@bp.route('/label/pub_topic/values', methods=['GET'])
def get_pub_topic():
    # cfg = current_app.config
    # db_str = cfg["POSTGRESQL_CONNECTION"]
    # with DBOper(db_str) as db:
    #    datas = db.query_datas("node_pub_info", ["topic"], distinct=True)

    topics = ['/perception/camera_10_depth_estimation', '/alpas/driverless/heartbeat_to_mcu',
              '/alpas/monitor/control_status', '/alpas/monitor/system_status', '/alpas/camera_front_right_1/image_raw/pb_image',
              '/cargo/localization/pose_hz', '/alpas/platoon_manager/flags_event', '/alpas/monitor/system_info',
              '/alpas/hmi/air_bridge/statistics', '/perception/camera_7_segmentation',
              '/alpas/planning/decider/decider_result', '/alpas/v2x/v2x_cmd/platoon_cmd',
              '/perception/camera_10_lane_detect', '/alpas/platoon_manager/mileage_statistics',
              '/perception/camera_10_object_list', '/alpas/monitor/runtimer/planner_status_mainfunction',
              '/perception/camera_4_depth_estimation', '/recurring_task/frame', '/alpas/camera_front_left_1/image_raw/pb_image',
              '/perception/camera_9_depth_estimation', '/alpas/remote_control/lead_control/to_hmi_L2_rsp',
              '/alpas/v2x/v2x_cmd/platoon_cmd_resp', '/perception/camera_4_object_status', '/alpas/planning/trajectory_planner/gap_distance',
              '/perception/camera_17_object_list', '/alpas/hmi/air_bridge/weight_setting', '/traffic_light_detect',
              '/cargo/autolabel/sceneinfo', '/alpas/monitor/runtimer/path_update_mainfunction', '/perception/camera_7_lane_detect',
              '/alpas/driverless/l2_debug_info_to_ipc', '/alpas/monitor/prediction_status', '/alpas/camera_front_left_2/image_raw/pb_image_hz',
              '/alpas/monitor/sensor_monitor/state', '/cargo/planning/debug', '/cargo/perception/front_agent_tracker_status',
              '/prediction/prediction_obstacles_hz', '/perception/camera_6_lane_detect', '/perception/camera_8_object_status',
              '/gps_imu_data', '/alpas/platoon_manager/external_vehicle', '/alpas/planning/trajectory_planner/path_history',
              '/alpas/camera_fisheye_right/image_raw/pb_image', '/perception/toll_gate_result', '/alpas/v2x/v2x_app/v2x_others_tx',
              '/perception/camera_8_object_list', '/perception/lidar_pipeline_status', '/alpas/chassis/chassis_info_timeout',
              '/alpas/monitor/lidar_rm_status', '/perception/camera_8_lane_detect', '/alpas/monitor/bywire_chassis_status',
              '/raw_gps_data', '/alpas/localization/trailer_angle', '/pose_chassis', '/perception/lidar_lane',
              '/alpas/drivers/voice_play/status_hz', '/perception/camera_17_segmentation', '/alpas/hmi/air_bridge/platoon_cmd',
              '/alpas/remote_control/lead_control/from_hmi_req', '/pose_base', '/alpas/planning/scene/scene_info',
              '/alpas/camera_fisheye_left/image_raw/pb_image_hz', '/perception/camera_6_object_status', '/alpas/v2x/v2x_app/v2x_others_tx_base',
              '/cargo/safety_surrogate/timetocollision', '/alpas/planning/decider/decider_debug', '/perception/camera_6_object_list',
              '/alpas/control/diagnostic_info', '/alpas/control/diagnostic_debug_info', '/alpas/camera_front_right/image_raw/pb_image',
              '/alpas/platoon_manager/vehicle_status', '/alpas/hmi/air_bridge/platoon_cmd_resp',
              '/alpas/camera_front_left_1/image_raw/pb_image_hz', '/alpas/camera_front_left/image_raw/pb_image_hz',
              '/alpas/camera_front_right_1/image_raw/pb_image_hz', '/alpas/monitor/others_error_info',
              '/alpas/planning_trajectory_gap_distance_topic_fusion_gnss', '/perception/camera_5_object_status',
              '/alpas/drivers/lidar/livox0_hz', '/alpas/monitor/runtimer/chassis_rx', '/perception/camera_5_lane_detect',
              '/cargo/control/control_info', '/perception/lidar_clusters', '/alpas/camera_front_right_2/image_raw/pb_image_hz',
              '/alpas/planning/decider/decider_info', '/alpas/camera_fisheye_right/image_raw/pb_image_hz',
              '/alpas/control/control_status', '/perception/camera_8_segmentation', '/system_info',
              '/perception/camera_9_lane_detect', '/perception/lidar_camera_fusion_detections',
              '/alpas/v2x/v2x_cmd/rx_info', '/alpas/planning/scene/scene_info_hz',
              '/alpas/camera_fisheye_front/image_raw/pb_image', '/alpas/control/control_notice',
              '/f30_scan', '/perception/camera_5_depth_estimation', '/alpas/planner/platoon_debug_info', '/prediction/prediction_obstacles',
              '/cargo/control/control_info_hz', '/perception/mot_tracks', '/alpas/platoon_manager/platoon_status',
              '/perception/camera_9_object_status', '/perception/camera_7_depth_estimation',
              '/alpas/planning/planner/status_info', '/perception/camera_4_segmentation',
              '/alpas/driverless/heartbeat_to_mcu_details', '/alpas/camera_front/image_raw/pb_image',
              '/alpas/camera_front_left/image_raw/pb_image', '/alpas/platoon_manager/platoon_status_hz',
              '/alpas/v2x/v2x_cmd/tx_info', '/perception/lidar_rangeview_detections', '/alpas/remote_control/vehicle_status_to_remote',
              '/alpas/platoon_manager/front_vehicle', '/cargo/localization/pose', '/alpas/camera_fisheye_left/image_raw/pb_image',
              '/alpas/camera_front_1/image_raw/pb_image', '/alpas/monitor/runtimer/scene_recvpcptracksv2_mainfunction',
              '/prediction/prediction_obstacles_debug', '/alpas/camera_front_left_2/image_raw/pb_image',
              '/alpas/v2x/v2x_monitor/monitor_info', '/perception/camera_4_object_list',
              '/alpas/chassis/chassis_info_rx_hz', '/prediction/prediction_debug_information',
              '/pose', '/cargo/control/control_statistics', '/perception/camera_7_object_status',
              '/alpas/v2x/v2x_lose_rate', '/perception/camera_17_object_status',
              '/perception/camera_10_object_status', '/alpas/camera_front_right_2/image_raw/pb_image',
              '/alpas/platoon_manager/external_platoon', '/cargo/localization/detect_following_debug_info',
              '/perception/camera_6_segmentation', '/cargo/lidar/status', '/alpas/camera_fisheye_front/image_raw/pb_image_hz',
              '/perception/static_grid', '/alpas/drivers/voice_play/play', '/alpas/monitor/runtimer/chassis_tx',
              '/perception/camera_10_segmentation', '/alpas/v2x/v2x_monitor/monitor_l_r_tx', '/alpas/control/vehicle_states_estimation',
              '/alpas/monitor/system_info_cmd', '/cargo/localization/detect_following_info', '/health/camera_object_detection_node',
              '/perception/camera_9_segmentation', '/alpas/monitor/recorder_node_0_status', '/autonomy/hulk_control/debug_info', '/perception/camera_6_depth_estimation',
              '/cargo/perception/front_agent_track_info', '/alpas/v2x/v2x_app/v2x_ego_tx', '/alpas/remote_control/lead_control/to_sys_req',
              '/alpas/v2x/v2x_interface/v2x_rx', '/alpas/camera_front_right/image_raw/pb_image_hz', '/alpas/chassis/chassis_info_rx',
              '/alpas/monitor/runtimer/control_anchor_9', '/alpas/camera_front_1/image_raw/pb_image_hz',
              '/alpas/camera_front/image_raw/pb_image_hz', '/alpas/planning/planner/trajectory_info',
              '/alpas/driverless/heartbeat_to_ipc', '/alpas/v2x/v2x_interface/v2x_r_tx', '/perception/tracker_status',
              '/perception/camera_4_lane_detect', '/alpas/remote_control/lead_control/to_hmi_rsp', '/perception/camera_7_object_list',
              '/cargo/prediction/status', '/alpas/monitor/topic_monitor_summary', '/alpas/drivers/voice_play/status',
              '/cargo/lidar/front/middle', '/alpas/monitor/lidar_fm_status', '/health/gnss_driver_node', '/perception/camera_8_depth_estimation',
              '/alpas/v2x/v2x_monitor/monitor_l_r_cycle_tx',
              '/alpas/v2x/v2x_monitor/monitor_m_cycle_tx',
              '/v2x_lane_info', '/cargo/localization/lane_debug_info', '/cargo/localization/pose_lane',
              '/perception/camera_14_lane_detect',
              '/perception/camera_15_lane_detect',
              '/cargo/sensors_info'
              '/system_info_orin_0',
              '/system_info_orin_1',
              '/system_info_orin_2',
              '/system_info_orin_3',
              '/bench_size_128',
              '/bench_size_256',
              '/bench_size_512',
              '/bench_size_1K',
              '/bench_size_2K',
              '/bench_size_4K',
              '/bench_size_8K',
              '/bench_size_16K',
              '/bench_size_32K',
              '/bench_size_64K',
              '/bench_size_128K',
              '/bench_size_256K',
              '/bench_size_512K',
              '/bench_size_1M',
              '/bench_size_4M',
              '/cargo/autolabel/platooninginfo',
              ]
    data = {
        'status': 'success',
        'data': topics
    }

    return jsonify(data)


@bp.route('/label/e2e_trip/values', methods=['GET'])
def get_e2e_trips():
    cfg = current_app.config
    db_str = cfg["POSTGRESQL_CONNECTION"]
    with DBOper(db_str) as db:
        datas = db.query_datas(
            "perf_trip_item_info",
            ["trip_id"],
            conditions="item='e2e_latency' and items>1000",
            order_by="order by trip_id desc")
    data = {
        'status': 'success',
        'data': datas["trip_id"]
    }
    return jsonify(data)


@bp.route('/label/perfetto_events_slice_trips/values', methods=['GET'])
def get_perfetto_events_slice_trips():
    cfg = current_app.config
    db_str = cfg["POSTGRESQL_CONNECTION"]
    with DBOper(db_str) as db:
        datas = db.query_datas(
            "perf_trip_item_info",
            ["trip_id"],
            conditions="item='perfetto_events_slcie'",
            order_by="order by trip_id desc")
    data = {
        'status': 'success',
        'data': datas["trip_id"]
    }
    return jsonify(data)

@bp.route('/label/trip/values', methods=['GET'])
def get_trips():
    cfg = current_app.config
    db_str = cfg["POSTGRESQL_CONNECTION"]
    with DBOper(db_str) as db:
        datas = db.query_datas(
            "trip_info",
            ["trip_id"],
            order_by="order by trip_id desc")
    #all_trips = list(set(datas["trip_id"] + datas_pb["trip_id"]))
    data = {
        'status': 'success',
        'data': datas["trip_id"]
    }
    return jsonify(data)


@bp.route('/series', methods=['GET'])
def get_series():
    data = {}
    return jsonify(data)


@bp.route('/label/__name__/values', methods=['GET'])
def get_label_values():
    data = {
        'status': 'success',
        'data': METRICS
    }

    return jsonify(data)


@bp.route('/metadata', methods=['GET'])
def get_metadata():
    data = {
        'status': 'success',
        'data': {
            "e2e_lidar_ipc": [{"type": "summary", "help": "A summary of the lidar ipc duration", "unit": "ms"}],
            "e2e_lidar_sched": [{"type": "summary", "help": "A summary of the lidar sched duration", "unit": "ms"}],
            "e2e_lidar_proc": [{"type": "summary", "help": "A summary of the lidar proc duration", "unit": "ms"}],
            "e2e_topdown_ipc": [{"type": "summary", "help": "A summary of the topdown ipc duration", "unit": "ms"}],
            "e2e_topdown_sched": [{"type": "summary", "help": "A summary of the topdown sched duration", "unit": "ms"}],
            "e2e_topdown_proc": [{"type": "summary", "help": "A summary of the topdown proc duration", "unit": "ms"}],
            "perf_e2e": [{"type": "Counter", "help": "A summary of the e2e latency duration", "unit": "ms"}]
        }
    }

    return jsonify(data)


def get_values(values):
    v = []
    for pair in values:
        _, value = pair
        v.append(float(value))
    s_v = sorted(v)
    l = len(s_v)
    avg = sum(s_v) / l
    p50 = s_v[int(l * 0.5) - 1]
    p99 = s_v[int(l * 0.99) - 1]
    return avg, p50, p99, s_v[0], s_v[-1]


@bp.route('/query', methods=['GET'])
def get_query():
    cfg = current_app.config
    db_str = cfg["POSTGRESQL_CONNECTION"]

    timestamp = request.args.get('time')
    sql = request.args.get('query')
    # sql = "select timestamp, topdown_detections_ipc, mot_tracks_ipc, mot_tracks_proc from perf_e2e"
    data = {}
    data["resultType"] = "vector"
    result = {"status": "success", "data": data}
    metrics = []
    if sql:
        with DBOper(db_str) as db:
            datas = db.query_p(sql)
            for name, values in datas.items():
                items = {}
                metric = {}
                metric["metric"] = items
                metric["value"] = [timestamp, 1]
                items["__name__"] = name
                avg, p50, p99, min_v, max_v = get_values(values)
                items["p50"] = p50
                items["p99"] = p99
                items["avg"] = avg
                items["min"] = min_v
                items["max"] = max_v
                metrics.append(metric)
            data["result"] = metrics
    # data = {"status": "success", "data":
    #        {"resultType": "vector", "result":
    #         [
    #             {"metric": {"__name__": "e2e_lidar_ipc",
    #                         "instance": "localhost:5000",
    #                         "job": "prometheus", "quantile": "0"},
    #              "value": [1671626583.003, "12"]},
    #             {"metric": {"__name__": "e2e_lidar_sched",
    #                         "instance": "localhost:5000",
    #                         "job": "prometheus", "quantile": "0"},
    #              "value": [1671626583.003, "2"]}
    #         ]
    #         }
    #        }

    return jsonify(result)


def sql_add_timerange(sql, start, end):
    add_sql = ""
    if "where" in sql:
        add_sql = " and timestamp between to_timestamp(%f) and to_timestamp(%f)" % (
            start + PROMETHEUS_TIME_OFFSET, end + PROMETHEUS_TIME_OFFSET)
    else:
        add_sql = " where timestamp between to_timestamp(%f) and to_timestamp(%f)" % (
            start + PROMETHEUS_TIME_OFFSET, end + PROMETHEUS_TIME_OFFSET)

    return sql + add_sql


@bp.route('/query_range', methods=['GET', 'POST'])
def get_range():
    cfg = current_app.config
    db_str = cfg["POSTGRESQL_CONNECTION"]
    time_offset = cfg["PROMETHEUS_TIME_OFFSET"]

    if request.method == "POST":
        query_form = request.form
        start, end, sql, step = query_form['start'], query_form['end'], query_form['query'], query_form['step']
    else:
        start, end, sql, step = request.args.get('start'), request.args.get(
            'end'), request.args.get('query'), request.args.get('step')

    # sql = sql_add_timerange(sql, int(start), int(end))
    logger.info('query_range sql %s' % sql)
    # sql = "select timestamp, topdown_detections_ipc, mot_tracks_ipc, mot_tracks_proc from perf_e2e"
    result = Result()
    if sql:
        with DBOper(db_str) as db:
            metric_name = get_table_from_sql(sql)
            datas = db.query(
                sql,
                time_offset=time_offset,
                start=int(start),
                end=int(end))
            for name, values in datas.items():
                m = Metric(metric_name, {"ident": name})
                m.set_values(values)
                result.add_metric(m)

    # print('data', data)
    #data = {"status": "success", "data":
    #        {"resultType": "matrix", "result":
    #         [
    #             {"metric": {"__name__": "e2e", "ident": "1"},
    #              "values": [[1671622723, "13"], [1671625243, "14"], [1671627763, "13.6"], [1671628800, "15"],
    #                         [1671630000, "19"]]},
    #             {"metric": {"__name__": "e2e", "ident": "2"},
    #              "values": [[1671622723, "13"], [1671625243, "14"], [1671627763, "13.6"], [1671628800, "15"],
    #                         [1671630000, "19"]]},
    #         ]
    #         }}
#    print('result', result.data())
    return jsonify(result.data())


'''
    data = {"status": "success", "data":
            {"resultType": "matrix", "result":
             [{"metric": {"__name__": "e2e_lidar_ipc",
                          "instance": "localhost:5000",
                          "job": "prometheus", "quantile": "0"},
              "values": [[1671626583.003, "12"], [1671622723, "13"], [1671625243, "14"], [1671627763, "13.6"]]},
              {"metric": {"__name__": "e2e_lidar_sched",
                          "instance": "localhost:5000",
                          "job": "prometheus", "quantile": "0"},
              "values": [[1671626583.003, "1"], [1671622723, "3"], [1671625243, "4"], [1671627763, "3.6"]]}]
             }
            }
'''

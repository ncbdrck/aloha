### Task parameters

DATA_DIR = '/home/sri-tus/Projects/aloha_data'
TASK_CONFIGS = {
    'aloha_wear_shoe':{
        'dataset_dir': DATA_DIR + '/aloha_wear_shoe',
        'num_episodes': 50,
        'episode_len': 1000,
        'camera_names': ['cam_high', 'cam_low', 'cam_left_wrist', 'cam_right_wrist']
    },

    'aloha_stationary_dummy':{
        'dataset_dir': DATA_DIR + '/aloha_stationary_dummy',
        'episode_len': 800,
        'camera_names': ['cam_high', 'cam_left_wrist', 'cam_right_wrist']
    },

    'aloha_stationary_test':{
            'dataset_dir': DATA_DIR + '/aloha_stationary_test',
            'episode_len': 500,
            'camera_names': ['cam_high', 'cam_low', 'cam_right_wrist', 'cam_left_wrist']
        },

    'aloha_stationary_pnp_one_arm':{
            'dataset_dir': DATA_DIR + '/aloha_stationary_pnp_one_arm',
            'episode_len': 500,
            'camera_names': ['cam_high', 'cam_low', 'cam_right_wrist', 'cam_left_wrist']
        },

    'aloha_stationary_pnp_both_arms':{
            'dataset_dir': DATA_DIR + '/aloha_stationary_pnp_both_arms',
            'episode_len': 1000,
            'camera_names': ['cam_high', 'cam_low', 'cam_right_wrist', 'cam_left_wrist']
        },

    'aloha_stationary_cube_sorting':{
            'dataset_dir': DATA_DIR + '/cube_sort/aloha_stationary_cube_sorting',
            'episode_len': 1250,
            'camera_names': ['cam_high', 'cam_low', 'cam_right_wrist', 'cam_left_wrist']
        },

    'aloha_stationary_rgb_cube_sorting':{
            'dataset_dir': DATA_DIR + '/cube_sort/aloha_stationary_rgb_cube_sorting',
            'episode_len': 1250,
            'camera_names': ['cam_high', 'cam_low', 'cam_right_wrist', 'cam_left_wrist']
        },

    'aloha_stationary_rgb_cube_sorting_v1':{
            'dataset_dir': DATA_DIR + '/cube_sort/aloha_stationary_rgb_cube_sorting_v1',
            'episode_len': 1250,
            'camera_names': ['cam_high', 'cam_low', 'cam_right_wrist', 'cam_left_wrist']
        },

    'aloha_stationary_rgb_cube_sorting_co_train_v1':{
            'dataset_dir': DATA_DIR + '/cube_sort/aloha_stationary_rgb_cube_sorting_co_train_v1',
            'episode_len': 1250,
            'camera_names': ['cam_high', 'cam_low', 'cam_right_wrist', 'cam_left_wrist']
        },
}

### ALOHA fixed constants
DT = 0.02
JOINT_NAMES = ["waist", "shoulder", "elbow", "forearm_roll", "wrist_angle", "wrist_rotate"]
START_ARM_POSE = [0, -0.96, 1.16, 0, -0.3, 0, 0.02239, -0.02239,  0, -0.96, 1.16, 0, -0.3, 0, 0.02239, -0.02239]

# Left finger position limits (qpos[7]), right_finger = -1 * left_finger
MASTER_GRIPPER_POSITION_OPEN = 0.0323
MASTER_GRIPPER_POSITION_CLOSE = 0.0185
PUPPET_GRIPPER_POSITION_OPEN = 0.0579
PUPPET_GRIPPER_POSITION_CLOSE = 0.0440

# Gripper joint limits (qpos[6])
MASTER_GRIPPER_JOINT_OPEN = 0.8298
MASTER_GRIPPER_JOINT_CLOSE = -0.0552
PUPPET_GRIPPER_JOINT_OPEN = 1.6214
PUPPET_GRIPPER_JOINT_CLOSE = 0.6197

############################ Helper functions ############################

MASTER_GRIPPER_POSITION_NORMALIZE_FN = lambda x: (x - MASTER_GRIPPER_POSITION_CLOSE) / (MASTER_GRIPPER_POSITION_OPEN - MASTER_GRIPPER_POSITION_CLOSE)
PUPPET_GRIPPER_POSITION_NORMALIZE_FN = lambda x: (x - PUPPET_GRIPPER_POSITION_CLOSE) / (PUPPET_GRIPPER_POSITION_OPEN - PUPPET_GRIPPER_POSITION_CLOSE)
MASTER_GRIPPER_POSITION_UNNORMALIZE_FN = lambda x: x * (MASTER_GRIPPER_POSITION_OPEN - MASTER_GRIPPER_POSITION_CLOSE) + MASTER_GRIPPER_POSITION_CLOSE
PUPPET_GRIPPER_POSITION_UNNORMALIZE_FN = lambda x: x * (PUPPET_GRIPPER_POSITION_OPEN - PUPPET_GRIPPER_POSITION_CLOSE) + PUPPET_GRIPPER_POSITION_CLOSE
MASTER2PUPPET_POSITION_FN = lambda x: PUPPET_GRIPPER_POSITION_UNNORMALIZE_FN(MASTER_GRIPPER_POSITION_NORMALIZE_FN(x))

MASTER_GRIPPER_JOINT_NORMALIZE_FN = lambda x: (x - MASTER_GRIPPER_JOINT_CLOSE) / (MASTER_GRIPPER_JOINT_OPEN - MASTER_GRIPPER_JOINT_CLOSE)
PUPPET_GRIPPER_JOINT_NORMALIZE_FN = lambda x: (x - PUPPET_GRIPPER_JOINT_CLOSE) / (PUPPET_GRIPPER_JOINT_OPEN - PUPPET_GRIPPER_JOINT_CLOSE)
MASTER_GRIPPER_JOINT_UNNORMALIZE_FN = lambda x: x * (MASTER_GRIPPER_JOINT_OPEN - MASTER_GRIPPER_JOINT_CLOSE) + MASTER_GRIPPER_JOINT_CLOSE
PUPPET_GRIPPER_JOINT_UNNORMALIZE_FN = lambda x: x * (PUPPET_GRIPPER_JOINT_OPEN - PUPPET_GRIPPER_JOINT_CLOSE) + PUPPET_GRIPPER_JOINT_CLOSE
MASTER2PUPPET_JOINT_FN = lambda x: PUPPET_GRIPPER_JOINT_UNNORMALIZE_FN(MASTER_GRIPPER_JOINT_NORMALIZE_FN(x))

MASTER_GRIPPER_VELOCITY_NORMALIZE_FN = lambda x: x / (MASTER_GRIPPER_POSITION_OPEN - MASTER_GRIPPER_POSITION_CLOSE)
PUPPET_GRIPPER_VELOCITY_NORMALIZE_FN = lambda x: x / (PUPPET_GRIPPER_POSITION_OPEN - PUPPET_GRIPPER_POSITION_CLOSE)

MASTER_POS2JOINT = lambda x: MASTER_GRIPPER_POSITION_NORMALIZE_FN(x) * (MASTER_GRIPPER_JOINT_OPEN - MASTER_GRIPPER_JOINT_CLOSE) + MASTER_GRIPPER_JOINT_CLOSE
MASTER_JOINT2POS = lambda x: MASTER_GRIPPER_POSITION_UNNORMALIZE_FN((x - MASTER_GRIPPER_JOINT_CLOSE) / (MASTER_GRIPPER_JOINT_OPEN - MASTER_GRIPPER_JOINT_CLOSE))
PUPPET_POS2JOINT = lambda x: PUPPET_GRIPPER_POSITION_NORMALIZE_FN(x) * (PUPPET_GRIPPER_JOINT_OPEN - PUPPET_GRIPPER_JOINT_CLOSE) + PUPPET_GRIPPER_JOINT_CLOSE
PUPPET_JOINT2POS = lambda x: PUPPET_GRIPPER_POSITION_UNNORMALIZE_FN((x - PUPPET_GRIPPER_JOINT_CLOSE) / (PUPPET_GRIPPER_JOINT_OPEN - PUPPET_GRIPPER_JOINT_CLOSE))

MASTER_GRIPPER_JOINT_MID = (MASTER_GRIPPER_JOINT_OPEN + MASTER_GRIPPER_JOINT_CLOSE)/2

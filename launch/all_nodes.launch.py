import launch
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share = get_package_share_directory('sea_rabbit')
    return LaunchDescription([
        Node(
            package='bno055',
            executable='bno055',
            name='imu_driver',
            parameters=["~/seals_ws/src/bno055/bno055/params/bno055_params.yaml"]
        ),
        Node(
            package='sea_rabbit',
            executable='odom_to_baselink',
            name='odom_to_baselink'
        ),
        IncludeLaunchDescription (
            PythonLaunchDescriptionSource (
                pkg_share + '/launch/display.launch.py'
            )
        ),
        IncludeLaunchDescription (
            PythonLaunchDescriptionSource (
                get_package_share_directory('velodyne') + '/launch/velodyne-all-nodes-VLP16-composed-launch.py'
            )
        ),
        IncludeLaunchDescription (
            PythonLaunchDescriptionSource (
                get_package_share_directory('slam_toolbox') + '/launch/online_async_launch.py'
            )
        )
    ])

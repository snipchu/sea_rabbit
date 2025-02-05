import launch
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='bno055',
            executable='bno055',
            name='imu_driver',
            parameters=["~/seals_ws/src/bno055/bno055/params/bno055_params.yaml"]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2'
        ),
        launch.actions.IncludeLaunchDescription (
            launch.launch_description_sources.PythonLaunchDescriptionSource (
                get_package_share_directory('velodyne') + '/launch/velodyne-all-nodes-VLP16-composed-launch.py'
            )
        )
    ])

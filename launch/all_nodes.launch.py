import launch
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share = FindPackageShare(package='sea_rabbit').find('sea_rabbit')
    urdf_path = os.path.join(pkg_share, 'src', 'description', 'tuppyurdf.urdf')
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
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2'
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': Command(['xacro ', LaunchConfiguration('model')])}]
        ),
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            parameters=[{'robot_description': Command(['xacro ', urdf_path])}]
        ),
        launch.actions.IncludeLaunchDescription (
            launch.launch_description_sources.PythonLaunchDescriptionSource (
                get_package_share_directory('velodyne') + '/launch/velodyne-all-nodes-VLP16-composed-launch.py'
            )
        ),
        launch.actions.IncludeLaunchDescription (
            launch.launch_description_sources.PythonLaunchDescriptionSource (
                get_package_share_directory('slam_toolbox') + '/launch/online_async_launch.py'
            )
        )
    ])

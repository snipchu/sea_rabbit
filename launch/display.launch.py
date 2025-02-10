import launch
import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    pkg_share = get_package_share_directory('sea_rabbit')
    urdf_path = os.path.join(pkg_share, 'tuppy.urdf.xml')
    urdf = open(urdf_path).read()
    return LaunchDescription([
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2'
        ),
        Node(
            name='robot_state_publisher',
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{
                'use_sim_time': LaunchConfiguration('use_sim_time', default='false'),
                'robot_description': urdf
            }],
            arguments=[urdf_path],
        )
    ])

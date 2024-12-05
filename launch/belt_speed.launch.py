from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='belt_speed_publisher',
            executable='belt_speed_publisher',
            name='belt_speed_publisher',
            output='screen'
        )
    ])

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='hamano_dyn_commander',
            namespace='',
            executable='server_multicommander_m3',
            name='module3_hamano_commander'
        ),
        Node(
            package='hamano_dyn_commander',
            namespace='',
            executable='client_multicommander',
            name='hamano_joy_client'
        )
    ])
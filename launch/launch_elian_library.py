import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
   dynamixel_hotplug_ros2_python = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('motor_controller'), 'launch'),
         '/multi_port_launch.py'])
      )


   return LaunchDescription([
      dynamixel_hotplug_ros2_python
   ])

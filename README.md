# Simple commander for the Hamano connector dynamixel-based gripper

## Prerequisites

- ROS 2 (Humble)
- Elian's dynamixel_hotplug_ros2_python library

## Install
### Install Odrive can
```sh
git clone https://github.com/Space-Robotics-Laboratory/hamano_dyn_commander.git
cd ros2_ws/
colcon build --packages-select hamano_dyn_commander
source ./install/setup.bash
```

## How to use

### 1. Open the gripper

```sh
ros2 service call /control_gripper std_srvs/srv/SetBool "{data: True}"
```

### 2. Close the gripper

```sh
ros2 service call /control_gripper std_srvs/srv/SetBool "{data: False}"
```

### 3. Joystick control [todo]

```sh
```
  
## Safety Precautions
Do not disconnect the motor power cables while the robot is powered on.
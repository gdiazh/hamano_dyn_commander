import sys
import rclpy

from rclpy.node import Node
from std_srvs.srv import SetBool
from sensor_msgs.msg import Joy

# Axis index
ANALOG_LEFT_LR = 0
ANALOG_LEFT_UD = 1
L2_AXIS = 2
ANALOG_RIGHT_LR = 3
ANALOG_RIGHT_UD = 4
R2_AXIS = 5
BUTTON_LR = 6
BUTTON_UD = 7

# Buttons index
X = 0
CIRCLE = 1
TRIANGLE = 2
SQUARE = 3
L1 = 4
R1 = 5
L2_BUTTON = 6
R2_BUTTON = 7
SHARE_BUTTON = 8
OPTIONS_BUTTON = 9
PS_BUTTON = 10
ANALOG_LEFT_BUTTON = 11
ANALOG_RIGHT_BUTTON = 1

class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('hamano_joy_client')
        
        self.cli_1_1_ = self.create_client(SetBool,'/module1/control_gripper_1') # not currently in use
        self.cli_2_1_ = self.create_client(SetBool,'/module2/control_gripper_1') 
        self.cli_2_2_ = self.create_client(SetBool,'/module2/control_gripper_2') # not currently in use
        self.cli_3_1_ = self.create_client(SetBool,'/module3/control_gripper_1')

        self.subscription = self.create_subscription(Joy, '/joy', self.joy_listener_callback, 10)

        self.req = SetBool.Request()

    def joy_listener_callback(self, msg):
        #Control module 3 connector one
        if msg.buttons[L2_BUTTON]:
            if msg.axes[BUTTON_LR] == 1:
                self.req.data = bool(True)
                self.cli_3_1_.call_async(self.req)
            elif msg.axes[BUTTON_LR] == -1:
                self.req.data = bool(False)
                self.cli_3_1_.call_async(self.req)
        #Control module 2 connector one
        if msg.buttons[R2_BUTTON]:
            if msg.buttons[CIRCLE]:
                self.req.data = bool(True)
                self.cli_2_1_.call_async(self.req)
            if msg.buttons[SQUARE]:
                self.req.data = bool(False)
                self.cli_2_1_.call_async(self.req)

def main():
    rclpy.init()
    minimal_client = MinimalClientAsync()
    rclpy.spin(minimal_client)
    minimal_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

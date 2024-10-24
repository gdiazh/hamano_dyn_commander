import sys

import rclpy
from rclpy.node import Node

from std_srvs.srv import SetBool

from sensor_msgs.msg import Joy

CIRCLE_ = 1
SQUARE_ = 3

R1_ = 4
L1_ = 5
R2_ = 6
L2_ = 7


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('multicommander_client_async')
        
        self.cli_1_ = self.create_client(SetBool,'/module1/control_gripper_1') 
        self.cli_2_ = self.create_client(SetBool,'/module1/control_gripper_2') 
        self.cli_3_ = self.create_client(SetBool,'/module2/control_gripper_1') 
        self.cli_4_ = self.create_client(SetBool,'/module2/control_gripper_2') 

        self.subscription = self.create_subscription(Joy, '/joy', self.joy_listener_callback, 10)
        # I think this part is wrong -Nette
        #-----
        self.cli = self.create_client(Joy, '/joy')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        #-----
        self.req = SetBool.Request()

    def joy_listener_callback(self, msg):
        #Control module 1 motor one
        if msg.buttons[R1_]:
            if msg.buttons[CIRCLE_]:
                self.req.data = bool(True)
            if msg.buttons[SQUARE_]:
                self.req.data = bool(False) 
            return self.cli_1_.call_async(self.req)
        #Control module 1 motor two
        if msg.buttons[L1_]:
            if msg.buttons[CIRCLE_]:
                self.req.data = bool(True)
            if msg.buttons[SQUARE_]:
                self.req.data = bool(False)
            return self.cli_2_.call_async(self.req)
        if msg.buttons[R2_]:
            if msg.buttons[CIRCLE_]:
                self.req.data = bool(True)
            if msg.buttons[SQUARE_]:
                self.req.data = bool(False) 
            return self.cli_3_.call_async(self.req)
        #Control module 1 motor two
        if msg.buttons[L2_]:
            if msg.buttons[CIRCLE_]:
                self.req.data = bool(True)
            if msg.buttons[SQUARE_]:
                self.req.data = bool(False)
            return self.cli_4_.call_async(self.req)



def main():
    rclpy.init()

    minimal_client = MinimalClientAsync()
    #future = minimal_client.send_request(bool(sys.argv[1]))
    #rclpy.spin_until_future_complete(minimal_client, future)
    
    #response = future.result()
    #minimal_client.get_logger().info()

    rclpy.spin(minimal_client)
    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

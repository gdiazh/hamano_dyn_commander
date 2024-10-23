import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64
from std_srvs.srv import SetBool

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('module2_hamano_commander')
        
        self.topic_1_ = 'ang_joint2_1_set'
        self.topic_2_ = 'ang_joint1_1_set'

        #Publisher for 2 motors
        self.publisher_1_ = self.create_publisher(Float64, self.topic_1_ ,10)
        self.publisher_2_ = self.create_publisher(Float64, self.topic_2_, 10)

        self.srv_1_ = self.create_service(SetBool, '/module3/control_gripper_1', self.handle_control_gripper_1)
        self.srv_2_ = self.create_service(SetBool, '/module3/control_gripper_2', self.handle_control_gripper_2)
        self.CLOSE_VALUE = 0.46
        self.OPEN_VALUE = 2.46

    def handle_control_gripper_1(self, req, resp):
        """
        Callback function for the "control_gripper" service.
        """
        topic_ = self.topic_1_

        #Default values for now
        gain = 1
        offset = 0
        untransform_msg = lambda x:x

        try:
            mode_value = 0.2 
            if req.data:
                mode_value = self.OPEN_VALUE 
                msg_info = 'Opening'
            else:
                mode_value = self.CLOSE_VALUE
                msg_info = 'Closing'
                
            new_msg = Float64()
            # If the received value is True (1), perform action for gripping
                
            new_msg.data = untransform_msg(mode_value / gain - offset) 
            self.publisher_1_.publish(new_msg)
            self.get_logger().info('Publishing for topic %s: "%s"' % (topic_, new_msg.data))
            self.get_logger().info(msg_info) 

            # Respond to the service request
            resp.success = True
            resp.message = "Gripper control completed"
            return resp
            # return SetBool(success=True, message="Gripper control completed")
        except Exception as e:
            # Handle any exceptions that might occur during gripping actions
            resp.success = False
            resp.message = 'Error during gripping action: "%s"' % str(e)
            return resp
            # self.get_logger().error('Error during gripping action: "%s"' % str(e))
            # return SetBool(success=False, message=f"Error during gripping action: {str(e)}")

    def handle_control_gripper_2(self, req, resp):
        """
        Callback function for the "control_gripper" service.
        """
        topic_ = self.topic_2_

        #Default values for now
        gain = 1
        offset = 0
        untransform_msg = lambda x:x

        try:
            mode_value = 0.2 
            if req.data:
                mode_value = self.OPEN_VALUE 
                msg_info = 'Opening'
            else:
                mode_value = self.CLOSE_VALUE
                msg_info = 'Closing'
                
            new_msg = Float64()
            # If the received value is True (1), perform action for gripping
                
            new_msg.data = untransform_msg(mode_value / gain - offset) 
            self.publisher_2_.publish(new_msg)
            self.get_logger().info('Publishing for topic %s: "%s"' % (topic_, new_msg.data))
            self.get_logger().info(msg_info) 

            # Respond to the service request
            resp.success = True
            resp.message = "Gripper control completed"
            return resp
            # return SetBool(success=True, message="Gripper control completed")
        except Exception as e:
            # Handle any exceptions that might occur during gripping actions
            resp.success = False
            resp.message = 'Error during gripping action: "%s"' % str(e)
            return resp
            # self.get_logger().error('Error during gripping action: "%s"' % str(e))
            # return SetBool(success=False, message=f"Error during gripping action: {str(e)}")

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

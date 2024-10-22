import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64, String
import sys
sys.path.append('/home/moonshot/dynamixel_hotplug_ros2_python/src/motor_controller/motor_controller/python_package_include/')
from topic_remapping import *
from std_srvs.srv import SetBool

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('motor_subscriber')
        
        #Data formatting
        
        self.subscription = self.create_subscription(
            Float64,
            'hm_connector_cmd',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.publisher_ = self.create_publisher(Float64, 'ang_joint2_1_set', 10)

        self.srv = self.create_service(SetBool, 'control_gripper', self.handle_control_gripper)

        self.transform_msg = input_shaping_map['ang_joint2_1_set']
        self.untransform_msg = output_shaping_map['ang_joint2_1_set']

        self.offset = offset_map['ang_joint2_1_set']
        self.gain = gain_map['ang_joint2_1_set']

        self.CLOSE_VALUE = 0.2
        self.OPEN_VALUE = 1.0

    def listener_callback(self, msg):
        new_msg = Float64()
        
        new_msg.data = self.untransform_msg(msg.data / self.gain - self.offset)
        self.publisher_.publish(new_msg)
        self.get_logger().info('Publishing: "%s"' % new_msg.data)

    def handle_control_gripper(self, req, resp):
        """
        Callback function for the "control_gripper" service.
        """

        try:
            if req.data:
                new_msg = Float64()
                # If the received value is True (1), perform action for gripping
                new_msg.data = self.untransform_msg(self.CLOSE_VALUE / self.gain - self.offset)
                self.publisher_.publish(new_msg)
                self.get_logger().info('Publishing: "%s"' % new_msg.data)
                self.get_logger().info('Opening')
            else:
                new_msg = Float64()
                # If the received value is True (1), perform action for gripping
                new_msg.data = self.untransform_msg(self.OPEN_VALUE / self.gain - self.offset)
                self.publisher_.publish(new_msg)
                self.get_logger().info('Publishing: "%s"' % new_msg.data)
                self.get_logger().info('Closing')

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
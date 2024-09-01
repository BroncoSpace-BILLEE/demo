import rclpy
from rclpy.node import Node

import std_msgs.msg

class Publisher(Node): 
    
    def __init__(self):
        super().__init__('subscriber')

        self.create_subscription(
            msg_type = std_msgs.msg.String,
            topic = 'my_topic',
            qos_profile = 10,
            callback = self.sub_callback,
        )

    def sub_callback(self, msg):
        self.get_logger().info(msg.data)
            

def main(args=None):
    rclpy.init(args=args)

    node = Publisher()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
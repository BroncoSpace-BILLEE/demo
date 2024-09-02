import rclpy
from rclpy.node import Node
# here's why i do the weird import statements https://answers.ros.org/question/405527/is-rclpy-and-rclpynode-different/

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
        # can't use regular print() statement in ros
        self.get_logger().info(msg.data)
            

def main(args=None):
    rclpy.init(args=args)

    node = Publisher()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

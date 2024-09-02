import rclpy
from rclpy.node import Node
# here's why i do the weird import statements https://answers.ros.org/question/405527/is-rclpy-and-rclpynode-different/

import std_msgs.msg

class Publisher(Node): 
    
    def __init__(self):
        super().__init__('publisher')

        self.count = 0

        self.publisher = self.create_publisher(
            msg_type = std_msgs.msg.String,
            topic = '/my_topic',
            qos_profile = 10,
        )

        self.timer = self.create_timer(
            timer_period_sec = 1,
            callback = self.timer_callback,
        )

    def timer_callback(self): 
        msg = std_msgs.msg.String()
        msg.data = f'{self.count} hello world'

        self.count += 1

        self.publisher.publish(msg)
            

def main(args=None):
    rclpy.init(args=args)

    node = Publisher()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

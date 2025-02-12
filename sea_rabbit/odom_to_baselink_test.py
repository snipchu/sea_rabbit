import rclpy
from rclpy.node import Node
import numpy as np
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import Vector3, TransformStamped
from sensor_msgs.msg import Imu

class broadcaster(Node):
    def __init__(self):
        super().__init__('odom_to_baselink')
        
        self.imu_sub = self.create_subscription(Imu, '/bno055/imu', self.imu_cb, 10)
        self.broadcaster = TransformBroadcaster(self)
    
    def imu_cb(self, msg):
        if (msg is not None):
            tf = TransformStamped()

            tf.header.stamp = self.get_clock().now().to_msg()
            tf.header.frame_id = "odom"
            tf.child_frame_id = "base_link"

            tf.transform.translation.x = 0.0
            tf.transform.translation.y = 0.0
            tf.transform.translation.z = 0.0
            tf.transform.rotation = msg.orientation
            
            self.broadcaster.sendTransform(tf)
        else:
            self.get_logger().info("IMU data not received, stopped publishing")

def main(args=None):
    rclpy.init(args=args)
    node = broadcaster()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

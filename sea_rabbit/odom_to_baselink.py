import rclpy
import numpy as np
from rclpy.node import Node
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import Vector3, TransformStamped
from sensor_msgs.msg import Imu

class broadcaster(Node):
    def __init__(self):
        super().__init__('odom_to_baselink')
        self.cb_time = self.get_clock.now()
        self.cb_cut = 0;
        self.imu_sub = self.create_subscription(Imu, '/bno055/imu', self.imu_cb, 10)
        self.broadcaster = TransformBroadcaster(self)
    
    def imu_cb(self, msg):
        if (msg is not None):
            self.cb_cut = self.get_clock.now()-self.cb_time
            self.cb_time = self.get_clock.now()
            self.get_logger().info(self.cb_time)
            
            tf = TransformStamped()

            tf.header.stamp = self.get_clock().now().to_msg()
            tf.header.frame_id = "odom"
            tf.child_frame_id = "base_link"

            tf.transform.translation.x = self.grav.x
            tf.transform.translation.y = self.grav.y
            tf.transform.translation.z = self.grav.z
            tf.transform.rotation.x = msg.orientation.x
            tf.transform.rotation.y = msg.orientation.y
            tf.transform.rotation.z = msg.orientation.z
            tf.transform.rotation.w = msg.orientation.w
            
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

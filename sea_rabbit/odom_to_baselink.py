import rclpy
from rclpy.node import Node
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import Vector3, TransformStamped
from sensor_msgs.msg import Imu

class broadcaster(Node):
    def __init__(self):
        super().__init__('odom_to_baselink')
        
        self.grav = None
        self.imu = None

        self.grav_sub = self.create_subscription(Vector3, '/bno055/grav', self.grav_cb, 10)
        self.imu_sub = self.create_subscription(Imu, '/bno055/imu', self.imu_cb, 10)
        self.broadcaster = TransformBroadcaster(self)
    
    def grav_cb(self, msg):
        self.grav = msg
        self.broadcast()
    
    def imu_cb(self, msg):
        self.imu = msg
        self.broadcast()

    def broadcast(self):
        if (self.grav is not None and self.imu is not None):
            tf = TransformStamped()

            tf.header.stamp = self.get_clock().now().to_msg()
            tf.header.frame_id = "odom"
            tf.child_frame_id = "base_link"

            tf.transform.translation.x = self.grav.x
            tf.transform.translation.y = self.grav.y
            tf.transform.translation.z = self.grav.z
            tf.transform.rotation.x = self.imu.orientation.x
            tf.transform.rotation.y = self.imu.orientation.y
            tf.transform.rotation.z = self.imu.orientation.z
            tf.transform.rotation.w = self.imu.orientation.w
            
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

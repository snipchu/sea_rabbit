import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion, Twist, Vector3
from sensor_msgs.msg import Imu

class odompub(Node):
    def __init__(self):
        super().__init__('odom_publisher')
        
        self.grav = None
        self.imu = None

        self.grav_sub = self.create_subscription(Vector3, '/bno055/grav', self.grav_cb, 10)
        self.imu_sub = self.create_subscription(Imu, '/bno055/imu', self.imu_cb, 10)
        self.pub_ = self.create_publisher(Odometry, '/bno055/odom', 10)
    
    def grav_cb(self, msg):
        self.grav = msg
        publish()
    
    def imu_cb(self, msg):
        self.grav = msg
        publish()

    def publish(self):
        msg = Odometry()
        # header
        msg.header.frame_id = 'odom'
        msg.header.stamp = self.get_clock().now().to_msg()
        # pose
            # pose
                # position
                # orientation
            # covariance

        msg.pose.pose.position.x = self.grav.x
        msg.pose.pose.orientation.x = self.imu.orientation.x
        # twist
            # twist
                # linear
                # angular
            # covariance
        msg.twist.twist.linear.x = self.imu.orientation.x
        
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = odompub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

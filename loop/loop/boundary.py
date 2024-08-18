import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class self_correction_turtle(Node):
    def __init__(self):
        super().__init__("pose_checking_robo")
        self.get_logger().info("pose_chekking_robo has been initiated")
        self.pub = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.sub = self.create_subscription(Pose,"/turtle1/pose",self.callback,10)
    def callback(self,msg:Pose):
        vel = Twist()
        if 3.0<msg.x<9.0 and 3.0<msg.y<9.0 :
            vel.linear.x = 5.0
            vel.angular.z = 0.0
        else:
            vel.linear.x = 1.0
            vel.angular.z = 0.9
        self.pub.publish(vel)
def main(args= None):
    rclpy.init(args=args)
    node = self_correction_turtle()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__" :
    main()
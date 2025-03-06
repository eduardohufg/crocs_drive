import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

class ProcVelocity(Node):
    def __init__(self):
        super().__init__('proc_velocity')
        self.publisher1 = self.create_publisher(Float32, 'motor_input_1', 10)
        self.publisher2 = self.create_publisher(Float32, 'motor_input_2', 10)
        self.subscription = self.create_subscription(Twist, 'cmd_vel', self.callback, 10)
        self.subscription

        self.vel_motor1 = Float32()
        self.vel_motor2 = Float32()
        #self.timer = self.create_timer(0.05, self.control)
        self.vel_x = 0.0
        self.vel_y = 0.0
        self.vel_z = 0.0
        self.angular = 0.0

    def callback(self, msg):
        self.vel_x = msg.linear.x
        self.vel_y = msg.linear.y
        self.vel_z = msg.linear.z
        self.angular = msg.angular.z

        right = self.vel_x + self.angular
        left = self.vel_x - self.angular

        
        left_target_vel = left * 2
        right_target_vel = right * 2

        self.vel_motor1.data = left_target_vel
        self.vel_motor2.data = right_target_vel

        self.publisher1.publish(self.vel_motor1)
        self.publisher2.publish(self.vel_motor2)


    def control(self):
        
        right = self.vel_x + self.angular
        left = self.vel_x - self.angular

        
        left_target_vel = left * 2
        right_target_vel = right * 2

        self.vel_motor1.data = left_target_vel
        self.vel_motor2.data = right_target_vel

        self.publisher1.publish(self.vel_motor1)
        self.publisher2.publish(self.vel_motor2)

def main(args=None):
    rclpy.init(args=args)
    proc_velocity = ProcVelocity()
    rclpy.spin(proc_velocity)
    proc_velocity.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

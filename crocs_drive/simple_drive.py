import rclpy 
import math 
from std_msgs.msg import * 
from geometry_msgs.msg import Twist 
from sensor_msgs.msg import Joy 
from numpy import* 
from rclpy.node import Node
import numpy as np

class Simple_Drive(Node):
    def __init__(self):
        super().__init__('simple_drive_teleop')
        self.publisher_vel = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscriber_joy = self.create_subscription(Joy,"joy", self.callbackjoy,10)
        self.subscriber_joy
        self.subscriber_webInt = self.create_subscription(Bool,"SD_WI", self.callbackwi,10)
        self.subscriber_webInt
        self.angle_srw = Float64()
        self.active = False
        self.buttons, self.axes = [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]
        self.velocity=3 
        self.twist=Twist()
        self.timer = self.create_timer(0.05, self.control)
        self.anglesRad = 0.0
        self.flag=0

    def callbackjoy(self,data):
        self.buttons = list(data.buttons [:])
        self.axes = list(data.axes [:])

    def callbackwi(self,data):
        self.active = bool(data.data)
        print(self.active)

    def control(self):
        if self.buttons[3]:
            self.velocity=1
        elif self.buttons[2] or self.buttons[1]:
            self.velocity=2
        elif self.buttons[0]:
            self.velocity=3

        left_speed= self.axes[4]/self.velocity
        right_speed= self.axes[1]/self.velocity
        
        linear_vel  = (left_speed + right_speed)/2 
        angular_vel  = (left_speed - right_speed)/2 
        
        self.twist.linear.x=linear_vel
        self.twist.angular.z=angular_vel
        self.publisher_vel.publish(self.twist)
            
            

def main(args=None):
    rclpy.init(args=args)
    listener=Simple_Drive()
    rclpy.spin(listener)
    listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
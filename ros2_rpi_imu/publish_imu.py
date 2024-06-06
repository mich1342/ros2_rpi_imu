import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from rclpy.clock import Clock

from .i2clibraries.i2c_itg3205 import *
from .i2clibraries.i2c_adxl345 import *
DEG_TO_RAD = 0.017453292519943295769236907684886

class ImuPublisher(Node):
  def __init__(self):
    super().__init__('imu_publisher')
    self.publisher_ = self.create_publisher(Imu, 'imu_data', 10)
    timer_period = 0.033 # seconds
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.itg3205_ = i2c_itg3205(1)
    self.adxl345_ = i2c_adxl345(1)
    self.msg_ = Imu()
    self.msg_.header.frame_id = "imu_link"
  
  def timer_callback(self):
    ts = Clock().now()
    self.msg_.header.stamp = ts.to_msg() 
    (itgready, dataready) = self.itg3205_.getInterruptStatus()
    if itgready and dataready:
      (x, y, z) = self.itg3205_.getDegPerSecAxes()
      self.msg_.angular_velocity.x = x * DEG_TO_RAD
      self.msg_.angular_velocity.y = y * DEG_TO_RAD
      self.msg_.angular_velocity.z = z * DEG_TO_RAD

    dataready = self.adxl345_.getInterruptStatus()
    if dataready:
      (x, y, z) = self.adxl345_.getAxes()
      self.msg_.linear_acceleration.x = x
      self.msg_.linear_acceleration.y = y
      self.msg_.linear_acceleration.z = z
    

    
    self.publisher_.publish(self.msg_)

def main(args=None):
  rclpy.init(args=args)

  imu_publisher = ImuPublisher()

  rclpy.spin(imu_publisher)

  imu_publisher.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()

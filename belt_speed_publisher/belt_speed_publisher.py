import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import serial

class BeltSpeedPublisher(Node):
    def __init__(self):
        super().__init__('belt_speed_publisher')
        self.publisher_ = self.create_publisher(Float32, 'belt_speed', 10)
        self.serial_port = serial.Serial('/dev/ttyACM0', 115200, timeout=1)  # Change to your Arduino's serial port
        self.timer = self.create_timer(0.1, self.publish_belt_speed)  # Publish speed every 100 ms

    def publish_belt_speed(self):
        if self.serial_port.in_waiting > 0:
            line = self.serial_port.readline().decode('utf-8').strip()
            if line.startswith("BeltSpeed:"):
                try:
                    speed = float(line.split(":")[1].strip())
                    msg = Float32()
                    msg.data = speed
                    self.publisher_.publish(msg)
                    self.get_logger().info(f'Published Belt Speed: {speed:.2f} mm/s')
                except ValueError:
                    self.get_logger().warn(f"Failed to parse speed from: {line}")

def main(args=None):
    rclpy.init(args=args)
    belt_speed_publisher = BeltSpeedPublisher()
    rclpy.spin(belt_speed_publisher)
    belt_speed_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

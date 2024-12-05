Fhis is the ros2 node for belt_speed_publisher for yumo encoder e6a2-cw3c.

First upload https://github.com/nilupul-tsukarm/belt_speed_publisher_ros2_arduino to arduino.

check Arduino's serial port using .
            $ cd /dev/
            /dev$ ls
change belt_speed_publisher/belt_speed_publisher.py line 10.
    self.serial_port = serial.Serial('/dev/ttyACM0', 115200, timeout=1)  # Change to your Arduino's serial port.

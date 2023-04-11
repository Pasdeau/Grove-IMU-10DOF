import time
import math
from grove.i2c import Bus
from grove.imu import IMU

# Initialise I2C et IMU
bus = Bus()
imu = IMU(bus)

# Reads IMU data and calculates rotation angles
while True:
    accel_data = imu.acceleration()
    gyro_data = imu.gyroscope()
    mag_data = imu.magnetic_field()

    roll, pitch, yaw = imu.acceleration_and_rotation(accel_data, gyro_data, mag_data)

    # Conversion de radian en angle
    roll_deg = roll * 180 / math.pi
    pitch_deg = pitch * 180 / math.pi
    yaw_deg = yaw * 180 / math.pi

    # output
    print("Roll: %.2f, Pitch: %.2f, Yaw: %.2f" % (roll_deg, pitch_deg, yaw_deg))

    # delay
    time.sleep(0.1)

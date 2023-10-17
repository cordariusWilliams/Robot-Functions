# Write your code here :-)
import time   #imports time library that are needed to run this code
import board  #imports board library that are needed to run this code
import digitalio #imports digitalio library that are needed to run this code
import pwmio #imports pwmio library that are needed to run this code

from adafruit_motor import motor #imports a small section of the adafruit_motor library

left_motor_forward = board.GP12 # Initializes the variable left_motor_forward and attaches it to GP12
left_motor_backward = board.GP13 # Initializes the variable left_motor_backward and attaches it to GP13
right_motor_forward = board.GP14 # Initializes the variable right_motor_forward and attaches it to GP14
right_motor_backward = board.GP15 # Initializes the variable right_motor_backward and attaches it to GP15


pwm_La = pwmio.PWMOut(left_motor_forward, frequency=10000) #Tells the pico that this component is an Output (and some other configuration)
pwm_Lb = pwmio.PWMOut(left_motor_backward, frequency=10000) #Tells the pico that this component is an Output (and some other configuration)
pwm_Ra = pwmio.PWMOut(right_motor_forward, frequency=10000) #Tells the pico that this component is an Output (and some other configuration)
pwm_Rb = pwmio.PWMOut(right_motor_backward, frequency=10000) #Tells the pico that this component is an Output (and some other configuration)


Left_Motor = motor.DCMotor(pwm_La, pwm_Lb) #Initializes Left_Motor and Configuration line and it is required
Left_Motor_speed = 0 #Initializes the variable Left_Motor_speed to 0

Right_Motor = motor.DCMotor(pwm_Ra, pwm_Rb) #Initializes Right_Motor and Configuration line and it is required
Right_Motor_speed = 0 ##Initializes the variable Right_Motor_speed to 0


    # Makes robot go forward

def Robot_Forward():
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1
    Right_Motor.throttle = Right_Motor_speed

    # Makes robot turn left

def Robot_Left():
    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1
    Right_Motor.throttle = Right_Motor_speed

    # Makes robot turn right

def Robot_right():
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1
    Right_Motor.throttle = Right_Motor_speed

    # Makes robot go backwards

def Robot_Backwards():
    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1
    Right_Motor.throttle = Right_Motor_speed

    # Makes robot stop

def Robot_Stop():
    Left_Motor_speed = 0
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 0
    Right_Motor.throttle = Right_Motor_speed



while True:

Robot_Forward()
Robot_Left()
Robot_right()
Robot_Backwards()
Robot_Stop()

# Write your code here :-)

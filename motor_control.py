from gpiozero import Motor

left_motor = Motor(forward=17, backward=18) # left motor
right_motor = Motor(forward=22, backward=23)

def drive(forward_speed=0.5, turn_correction=0.0):
    left_speed = max(min(forward_speed - turn_correction, 1.0), 0.0)
    right_speed = max(min(forward_speed + turn_correction, 1.0), 0.0)
    left_motor.forward(left_speed)
    right_motor.forward(right_speed)

def stop(): #stops both motors
    left_motor.stop()
    right_motor.stop()

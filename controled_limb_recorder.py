#import argparse
import rospy
import baxter_interface
import time
import sys

from baxter_interface import CHECK_VERSION
from baxter_interface import DigitalIO
from baxter_interface import Limb


#right arm joints are written first, then left arm joints. see recording function
right_arm_names = []
left_arm_names = []

start_time = 0

def main():
    if len(sys.argv) < 2:
	print("please enter a filepath for where to record the joint positions")
	exit(1)
    print("Press the circular button on Baxter's right gripper to record the position of his joints")
    print("Hit the pill-shapped button to end recording")
    #TODO! handle file exceptions here
    dst_file = open(sys.argv[1], 'w')


    rospy.init_node("rsdk_joint_recorder")
    rs = baxter_interface.RobotEnable(CHECK_VERSION)
    rs.enable()

    button = DigitalIO('right_lower_button')
    exit_bttn = DigitalIO('right_upper_button')
    right_arm = Limb('right')
    left_arm = Limb('left')

    initialize_file(dst_file, right_arm, left_arm)

    bttn_was_pressed = False 

    global start_time 
    start_time = time.time()

    while True :

	if bool(exit_bttn.state) : #if the exit button is pressed
	    print("finished recording\n")
	    exit(0)


	bttn_is_pressed = bool(button.state)

	#Triggers when the button is first pressed, but doesn't repeat the whole time the button is held
	if bttn_is_pressed and bttn_was_pressed == False: 
	    record_limbs(dst_file, right_arm, left_arm)
	bttn_was_pressed = bttn_is_pressed
    	time.sleep(0.005)



def initialize_file(dst_file, right_arm, left_arm):
    global right_arm_names
    global left_arm_names
    global start_time

    right_arm_names = right_arm.joint_names()
    left_arm_names = left_arm.joint_names()
    joint_names = right_arm_names + left_arm_names

    dst_file.write("time,")   

    for name in joint_names:
	dst_file.write(name)
	dst_file.write(",")
    dst_file.write("\n")
    dst_file.flush()
    
	

def record_limbs(dst_file, right_arm, left_arm):
    global right_arm_names
    global left_arm_names

    current_time = time.time()
    seconds_elapsed = current_time - start_time
    dst_file.write(str(seconds_elapsed) + ',')

    r_d = right_arm.joint_angles()
    l_d = left_arm.joint_angles()

    for name in right_arm_names :
	angle = r_d.get(name)
	dst_file.write(str(angle))
	dst_file.write(',')
    for name in left_arm_names :
	angle = l_d.get(name)
	dst_file.write(str(angle))
	dst_file.write(',')
    dst_file.write('\n')
    dst_file.flush()
    print("point recorded")


if __name__ == '__main__':
    main()	
	



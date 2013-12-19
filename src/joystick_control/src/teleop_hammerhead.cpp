#include <ros/ros.h>
#include <sensor_msgs/Joy.h>
#include <stdio.h>
#include <joystick.h>


void joyCallback(const sensor_msgs::Joy::ConstPtr& joy)
{
  //Define Subscibed Controller Data
  //Yaw
  yawjoy_ = joy->axes[PS3_AXIS_STICK_LEFT_LEFTWARDS];
  //Surge
  surgejoy_ = joy->axes[PS3_AXIS_STICK_LEFT_UPWARDS];
  //Heave
  heavejoy_ = joy->axes[PS3_AXIS_STICK_RIGHT_UPWARDS];
  //Test
  circlebutton = joy->buttons[PS3_BUTTON_ACTION_CIRCLE];
}

int main(int argc, char** argv)
{
  ros::init(argc, argv, "teleop_hammerhead");
 
  ros::NodeHandle n;
  //Declaring Subscriber
  ros::Subscriber joy_sub_;

  joy_sub_ = n.subscribe<sensor_msgs::Joy>("joy", 50, joyCallback);

  while(n.ok()){
  //Printing Controller Values
  printf("%f\t\t%f\n", yawjoy_, surgejoy_);

  //Left Joystick
  if(heavejoy_==0){
  //Turning Left
    if(yawjoy_>0.25 && surgejoy_<0.75 && surgejoy_>-0.75){
    printf("Turning Left!\n");
    }

  //Turning Right
    if(yawjoy_<-0.25 && surgejoy_<0.75 && surgejoy_>-0.75){
    printf("Turning Right!\n");
    }

  //Moving Forward
    if(surgejoy_>0.25 && yawjoy_<0.75 && yawjoy_>-0.75){
    printf("Moving Forward!\n");
    }

  //Moving Backward
    if(surgejoy_<-0.25 && yawjoy_<0.75 && yawjoy_>-0.75){
    printf("Moving Backward!\n");
    }
  }
  //Right Joystick
  if(surgejoy_==0 || yawjoy_==0){
    if(heavejoy_ >0.25){
    printf("Decreasing Depth!\n");
    }
    if(heavejoy_ <-0.25){
    printf("Increasing Depth!\n");
    }
  }
  ros::spinOnce();
  }
}
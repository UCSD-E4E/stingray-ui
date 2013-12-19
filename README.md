stingray-ui
===========

High-level Stingray operation. Separates UI controls from the internal Stingray controls. Modularizes Stingray system into high-level UI controls (this repository), vision system, and controls system. 

Provides the following packages:
  * stingray_start
  * mission_controller
  * joystick_control
  * demo

Also contains a directory called "demos" that contains various demo packages.


## Package Details


### stingray_start
Provides launch and configuration options for starting up the Stingray. Start files and configuration options are left to the <system>_start package for each subsystem (vision, controls, etc.). This package provides subsystem-independent configuration and launch files, as well as launch files for each individual subsystem. Also starts up the mission controller UI.

#### Subsystems
  * vision
  * controls


### mission_controller
Provides the main UI for the entire Stingray system. Uses rqt_gui and available plugins to define UI window, rviz, etc. Also provides custom plugins for mission-control GUI widget, navigation GUI, and others TBD.

#### UI Controls provided for:
  * vision subsystem
  * controls subsystem (PID tuning, etc.)
  * Navigation and waypoints
  * Path Planning options


### joystick_control
Provides ability to control Stingray in ROV mode, with full access to sensor suite but no autonomy.

### demo
TODO: Demo package with TBD functionality

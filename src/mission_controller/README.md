mission_controller
=====================

This package provides a user interface for operating the Stingray. It is built on rqt_gui and uses existing rqt plugins such as Rviz and image-viewer to build the UI. It also defines custom plugins for Stingray mission control, pose estimation, and other mission-specific options, which integrate into the UI.

See the documentation website for screenshots explaining mission controller operation. 

## Mission Controller UI Components

### Mission Options

#### Basic Operation Components
  * Start/Stop buttons: Starts/stops defined mission
  * Emergency stop (E-stop) button: Exact functionality TBD but likely will make the Stingray surface as quickly as possible.
  * Surface button: tells Stingray to surface where it is and hold
  * Descend button: tells Stingray to descend to a user-specified depth and hold
  * Battery indicator: displays remaining battery life and warns when battery is getting low

#### Mission Types
  * Lawnmower: allows user to input a survey area, choose path options, and specify waypoints
  * 3D Mapping: Exact functionality TBD, but will involve selecting survey volume, waypoints, and path options
  * ROV Mode: Navigation/path planning controlled by human operator, but gives options for which sensors should remain active and whether robot should still use vSLAM to build a map

##### Survey Options: based on specified mission type
  * Lawnmower
    * Allows user to specify survey area (width and length) and survey depth
    * Includes option for changing "inspection plane," i.e. if Stingray is surveying a coral reef it will be moving in the XY plane, but if it's inspecting the side of a ship (for example) it will be moving in XZ or YZ: TBD what this will be called
  * 3D Mapping: TBD
  * ROV Mode
    * Allows user to select which sensors should record to a bag file
    * Allows user to select whether Stingray should still perform SLAM

### RVIZ
Rviz displays the results of SLAM as the robot navigates in the environment. It displays the 3D map being built by the Stingray, as well as the Stingray's estimated pose in the map.


### Navigation 
TBD

### Image View
Provides left and right stereo images, updated at a much lower frequency than recorded at (say, every 5 seconds? we'll see)

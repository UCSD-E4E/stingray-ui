#!/usr/bin/env python
import roslib; roslib.load_manifest('controls_demo')
import ropsy
from std_msgs.msg import Float32
import sys

###
### Author: Antonella Wilby
### Email: awilby@ucsd.edu
###
### Gets distance from target from target tracker node and keeps Stingray
### at stable distance from target.
###

### TODO
### Implement me!

class DemoController:
    def __init__(self):
        """Initializes DemoController."""
        
        # Subscribe to distance from target topic
        rospy.Subscriber('/distance_from_target', Float32, self.distance_handler)
        
    def distance_handler(self):
        """..."""
        pass
    
    


def main(args):
    """..."""
    
    # Initialize demo controller node
    rospy.init_node('controls_demo')
    
    # Initialize DemoController
    demo = DemoController()
    
    # Run until program is quit
    rospy.spin()


# Calls main and passes system arguments if run standalone
if __name__ == "__main__":
    main(sys.argv)
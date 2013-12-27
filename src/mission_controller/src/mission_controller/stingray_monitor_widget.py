#!/usr/bin/env python
import rospy
import rospkg
import os
import time
from python_qt_binding import loadUi
from python_qt_binding.QtCore import Qt
from python_qt_binding.QtGui import QFileDialog, QGraphicsView, QIcon, QWidget, QGroupBox
import python_qt_binding.QtGui as QtGUI
from qt_gui.plugin import Plugin
from argparse import ArgumentParser


class StingrayMonitorView(QGraphicsView):
    """..."""

    def __init__(self, parent=None):
        super(StingrayMonitorView, self).__init__()



class StingrayMonitorWidget(QWidget):
    """..."""

    def __init__(self, context):
        """ Initializes widget and UI.
            Parameters: context - plugin context hook to enable adding widgets as ROS_GUI pane, 'PluginContext'.
        """
        
        # Get parent class
        super(StingrayMonitorWidget, self).__init__()

        # Get UI file from resources folder
        rp = rospkg.RosPack()
        ui_file = os.path.join(rp.get_path('mission_controller'), 'resource', 'StingrayMonitor.ui')
        loadUi(ui_file, self, {'StingrayMonitorView': StingrayMonitorView})

        self.setObjectName('StingrayMonitorWidget') # Name QObject

        #self.init_interface()

           
        #self.show()


    
    def init_interface(self):
        self.start = QtGUI.QPushButton("Start")
        
        





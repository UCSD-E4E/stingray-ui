#!/usr/bin/env python

import rospy
import rospkg
import os
import time
from python_qt_binding import loadUi
from python_qt_binding.QtCore import Qt
from python_qt_binding.QtGui import QFileDialog, QGraphicsView, QIcon, QWidget
from qt_gui.plugin import Plugin
from argparse import ArgumentParser


class MissionControllerView(QGraphicsView):
    """..."""

    def __init__(self, parent=None):
        super(MissionControllerView, self).__init__()



class MissionControllerWidget(QWidget):
    """..."""

    def __init__(self, context):
        """ Initializes widget and UI.
            Parameters: context - plugin context hook to enable adding widgets as ROS_GUI pane, 'PluginContext'.
        """
        
        # Get parent class
        super(MissionControllerWidget, self).__init__()

        # Get UI file from resources folder
        rp = rospkg.RosPack()
        ui_file = os.path.join(rp.get_path('mission_controller'), 'resource', 'MissionController.ui')
        loadUi(ui_file, self, {'MissionControllerView': MissionControllerView})

        self.setObjectName('MissionControllerWidget') # Name QObject



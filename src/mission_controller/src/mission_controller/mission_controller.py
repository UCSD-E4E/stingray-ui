#!/usr/bin/env python

from argparse import ArgumentParser
from qt_gui.plugin import Plugin
from .mission_controller_widget import MissionControllerWidget


class MissionController(Plugin):
    """ Subclass of Plugin that provides mission control options.
    """

    def __init__(self, context):
        """ Initializes widget and UI.
                :param context: plugin context hook to enable adding widgets as a ROS Gui pane, 'PluginContext'
        """

        # Get parent class
        super(MissionController, self).__init__(context)

        self.setObjectName('MissionController')

        self._widget = MissionControllerWidget(context)

        # For case when there are more than 1 of the widget in the rqt window
        if context.serial_number > 1:
            self._widget.setWindowTitle(self._widget.windowTitle() + (' (%d)' % context.serial_number()))
        
        # Add widgets to user interface
        context.add_widget(self._widget)

        # Parse command line arguments
        args = self.parse_args(context.argv())


    def parse_args(self, argv):
        """ Parses command line arguments. """

        parser = ArgumentParser(prog="mission_controller", add_help=False)
        MissionController.add_arguments(parser)
        return parser.parse_args(argv)


    @staticmethod
    def add_arguments(parser):
        """..."""

        group = parser.add_argument_group('Options for mission_controller plugin')
        #group.add_argument()


    def shutdown_plugin(self):
        """Unregisters all publishers from this widget."""

        pass


    def save_settings(self, plugin_settings, instance_settings):
        """Saves intrinsic plugin configuration."""

        pass


    def restore_settings(self, plugin_settings, instance_settings):
        """Restores intrinsic plugin configuration."""

        pass


    def trigger_configuration(self):
        """Opens settings dialog for plugin."""

        pass

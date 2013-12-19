#include "mission_controller.h"
#include <pluginlib/class_list_macros.h>
#include <QStringList>

namespace mission_controller {


// Constructor: called before initPlugin function
MissionController::MissionController() : rqt_gui_cpp::Plugin(), widget_(0) {

    // Initialize QObject
    setObjectName("MissionController");

}

// 
void MissionController::initPlugin(qt_gui_cpp::PluginContext& context) {

    // Access standalone command line arguments
    QStringList argv context.argv();

    // Create QWidget
    widget_ = new QWidget();

    // Extend widget with all attributes and children from UI file
    ui_.setupUi(widget_);

    // Add widget to User Interface
    context.addWidget(widget_);

}

// Shuts down UI Plugin and unregisters all publishers
void MissionController::shutdownPlugin() {



}

// Save configuration
void MissionController::saveSettings(qt_gui_cpp::Settings& plugin_settings,
                                     const qt_gui_cpp::Settings& instance_settings) const {

// instance_settings.setValue(k,v)

} 

// Restore configuration
void MissionController::restoreSettings(const qt_gui_cpp::Settings& plugin_settings,
                                        const qt_gui_cpp::Settings& instance_settings) {

    // v = instance_settings.value(k)

} 

/*bool hasConfiguration() const {
  return true;
}

void triggerConfiguration() {
  // Usually used to open a dialog to offer the user a set of configurations
}*/

} // end namespace mission_controller

PLUGINLIB_DECLARE_CLASS(mission_controller, MissionController, 
                        mission_controller::MissionController, rqt_gui_cpp::MissionController)

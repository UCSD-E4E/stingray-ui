#ifndef mission_controller__mission_controller_H
#define mission_controller__mission_controller_H

#include <rqt_gui_cpp/plugin.h>
#include <mission_controller/ui_mission_controller.h>
#include <QWidget>

namespace mission_controller {

    class MissionController : public rqt_gui_cpp::Plugin {

        Q_OBJECT

        public:
            MissionController();
            virtual void initPlugin(qt_gui_cpp::PluginContext& context);
            virtual void shutdownPlugin();
            virtual void saveSettings(qt_gui_cpp::Settings& plugin_settings,
                                      qt_gui_cpp::Settings& instance_settings) const;
            virtual void restoreSettings(const qt_gui_cpp::Settings& plugin_settings,
                                         const qt_gui_cpp::Settings& instance_settings);


        private:
            Ui::MissionControllerWidget ui_;
            QWidget* widget_;
        

    }; // end MissionController class

} // end namespace
#endif

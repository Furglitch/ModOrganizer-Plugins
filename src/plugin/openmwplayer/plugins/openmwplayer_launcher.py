import mobase, threading
from ..core.openmwplayer_plugin import OpenMWPlayerPlugin
from ..modules.openmwplayer_menu import OpenMWPlayerMenu
from ....base.base_dialog import BaseDialog
from ....common.common_qt import *
from ....common.common_icons import *

class OpenMWPlayerLauncher(OpenMWPlayerPlugin, mobase.IPlugin):
    def __init__(self):
        super().__init__()

    def init(self, organiser:mobase.IOrganizer):
        res = super().init(organiser)
        self._organiser.onAboutToRun(lambda appName: self.onApplicationLaunch(appName))
        self._organiser.onFinishedRun(lambda appName, exitCode: self.onApplicationClose(appName))
        self._organiser.onUserInterfaceInitialized(lambda window: self.onModListChange())
        self._organiser.onProfileChanged(lambda old, new: self.onModListChange())

        modList:mobase.IModList = self._organiser.modList()
        modList.onModInstalled(lambda mod: self.onModListChange())
        modList.onModStateChanged(lambda mods: self.onModListChange())
        modList.onModMoved(lambda mod, old, new: self.onModListChange())
        modList.onModRemoved(lambda name: self.onModListChange())

        pluginList:mobase.IPluginList = self._organiser.pluginList()
        pluginList.onPluginMoved(lambda name, old, new: self.onModListChange())
        pluginList.onPluginStateChanged(lambda map: self.onModListChange())
        return res

    def __tr(self, trstr):
        return QCoreApplication.translate(self._pluginName, trstr)

    def icon(self):
        return OPENMW_ICON

    def master(self):
        return self.baseName()

    def name(self):
        return self.baseName() + " Launcher"

    def displayName(self):
        return self.baseDisplayName() + " Launcher"

    def description(self):
        return self.__tr("Handles background running of OpenMW Player jobs.")

    def settings(self):
        return []

    def onModListChange(self):
        t = [
            threading.Thread(target=self._openmwPlayer._files.refreshOpenmwCfg),
            threading.Thread(target=self._openmwPlayer.setupDummyEsps)
        ]
        for nt in t:
            nt.start()

    def onApplicationLaunch(self, appName):
        return self._openmwPlayer.runApplication(appName)

    def onApplicationClose(self, appName):
        self._openmwPlayer._deploy.restoreCfg()

import mobase 
from ..shared.shared_plugin import SharedPlugin
from .profilesync import ProfileSync

class ProfileSyncPlugin(SharedPlugin):

    def __init__(self):
        super().__init__("ProfileSync", "Profile Sync", mobase.VersionInfo(1,1,1, mobase.ReleaseType.ALPHA))

    def init(self, organiser=mobase.IOrganizer):
        self.profilesync = ProfileSync(organiser)
        return super().init(organiser)
    
        
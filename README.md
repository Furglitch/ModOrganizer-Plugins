# ModOrganizer-Plugins
Shared repository for [Mod Organizer](https://github.com/ModOrganizer2/modorganizer) plugins.

## Plugins

### [Root Builder](https://kezyma.github.io/?p=rootbuilder)
Root Builder is a Mod Organizer 2 plugin that allows you to manage files in the base game folder through Mod Organizer, leaving your game folder in pristine, vanilla condition!

### [Reinstaller](https://kezyma.github.io/?p=reinstaller)
Reinstaller is a Mod Organizer 2 plugin that allows you to backup downloaded mods and run their installers on demand. Useful for large fomod patch installers with loads of options that you have to re-run frequently. Don't let those files keep your downloads tab cluttered anymore!

### [Shortcutter](https://kezyma.github.io/?p=shortcutter)
Shortcutter is a Mod Organizer 2 plugin that gives you the option of quickly creating instance and profile specific desktop shortcuts, allowing you to quickly launch your game using different profiles without having to manually switch inside Mod Organizer.

### [Plugin Finder](https://kezyma.github.io/?p=pluginfinder)
Plugin Finder is a Mod Organizer 2 plugin that allows you to browse and install other plugins for Mod Organizer, as well as uninstall them.

### [Curation Club](https://kezyma.github.io/?p=curationclub)
Curation Club is a plugin for Mod Organizer 2, allowing users to import Creation Club content into Mod Organizer as separate mods.

### [Profile Sync](https://kezyma.github.io/?p=profilesync)
Profile Sync is a plugin for Mod Organizer 2, it allows you to maintain the same mod order (while keeping the enabled/disabled state) across multiple profiles.

### [OpenMW Player](https://kezyma.github.io/?p=openmwplayer)
A plugin for Mod Organizer 2 that automatically exports your mod list, enabled plugins, and grass mods to OpenMW whenever you run the game through Mod Organizer. 

## Usage

### Installing Mods
To install a plugin from this repository, download a plugin from above and extract the folder inside into your `Mod Organizer\plugins` folder.

### This Repo
- `src` contains the plugin code and a shared code folder. Each plugin has its own folder and a `plugin_init.py` file.
- `release` contains the plugins packaged for individual release. each folder is an individual plugin.
- `readme` contains the readme files (and any other documentation) in individual plugin folders.
- `tools` contains various batch files.

### Tools
the `tools` folder contains a few batch files.

#### cleanup.bat
When called, the `release` folder will be deleted, as will any log files in the `tools` folder.

#### release.bat
Calling release.bat with parameters of different plugin names will; (eg. `release.bat rootbuilder reinstaller` would build rootbuilder and reinstaller)
- Copy the plugin and shared folders from `src` to `release\plugin`
- Copy the `plugin_init.py` file to `release\plugin` and rename it to `__init__.py`
- Copy the readme content from `readme\plugin` to `release\plugin`
- Zip the plugin for release and place it in `release\zip`

#### release_all.bat
Calls release.bat with parameters for every plugin.

#### deploy.bat
Calling deploy.bat with parameters of different plugin names will copy the relevant plugin folder from `release` to all the folders listed in `deploy_targets.txt`
(eg. `deploy.bat rootbuilder reinstaller` would deploy rootbuilder and reinstaller)

#### deploy_all.bat
Calls deploy.bat with parameters for every plugin.

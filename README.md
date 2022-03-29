# bhlegacylinuxlauncher
Linux launcher for the legacy brick-hill client


# Requirements
* Linux (duhh)
* Wine
* Python3


# Installation guide
* Install brick-hill using wine
* Open a new terminal window
* run "cd ~/.local/share/applications"
* run "git clone https://github.com/Modnark/bhlegacylinuxlauncher.git"
* run "mv bhlegacylinuxlauncher/launcher.py ./"
* run "mv bhlegacylinuxlauncher/brick-hill.desktop ./"
* run "rm -rf bhlegacylinuxlauncher", this will remove any remaining files that we don't need


If everything went well you should now be able to play any game on the legacy client!

# Known issues
Unfortunately, there are some issues that I have no solution to. Maybe it's only me who has these problems, but I'll put them here so you know what to expect.

* When closing the client your screen will briefly go all black.
* Playing the game in maximized mode leads to crashing 99% of the time
* There is performance loss compared to running this natively on windows (playability depends on your hardware)

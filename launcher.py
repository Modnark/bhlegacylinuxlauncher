#!/usr/bin/python3
import sys
import os

# shows values of variables for debugging
debugging = False

try:
    # get environment variables
    homeDir = os.getenv("HOME")
    username = homeDir.split("/")[2]

    # brick-hill client location
    clientPath = f"{homeDir}/.wine/drive_c/users/{username}/AppData/Roaming/Brick Hill/Player.exe"

    # get the passed args from the website
    launchArgs = sys.argv[1]

    # string to remove from launch args
    launcherStrip = "brickhill.legacy://client/"

    # formatted args
    clientArgs = launchArgs.replace(launcherStrip, "")

    # command to run        
    sysCmd = f"wine \"{clientPath}\" {clientArgs}"

    if debugging:
        print(f"[DEBUG] clientArgs: {clientArgs}")
        print(f"[DEBUG] clientPath: {clientPath}")
        print(f"[DEBUG] sysCmd: {sysCmd}")

    # launch brick-hill client w/ args
    os.system(sysCmd)
except Exception as e:
    print(e)
    open("./brick-hill-launcher-errors.log", "a+").write(f"{e}\n")
    input("Press enter to quit.")

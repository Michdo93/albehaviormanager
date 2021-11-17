#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use ALBehaviorManager Module"""

import qi
import argparse
import sys
import time


def main(session, behavior_name, function, localPath):
    """
    Use ALBehaviorManager Module.
    """
    # Get the service ALBehaviorManager.

    behavior_mng_service = session.service("ALBehaviorManager")

    if(behavior_name == ""):
        if(function == "getBehaviorNames"):
            getBehaviorNames(behavior_mng_service)
        elif(function == "getInstalledBeviors"):
            getInstalledBeviors(behavior_mng_service)
        elif(function == "getDefaultBehaviors"):
            getDefaultBehaviors(behavior_mng_service)
        elif(function == "getLoadedBehaviors"):
            getLoadedBehaviors(behavior_mng_service)
        elif(function == "getRunningBehaviors"):
            getRunningBehaviors(behavior_mng_service)
        elif(function == "getSystemBehaviorNames"):
            getSystemBehaviorNames(behavior_mng_service)
        elif(function == "getUserBehaviorNames"):
            getUserBehaviorNames(behavior_mng_service)
        elif(function == "stopAllBehaviors"):
            stopAllBehaviors(behavior_mng_service)
    elif(localPath):
        if(function == "installBehavior"):
            installBehavior(behavior_mng_service, localPath)
        elif(function == "installBehavior2"):
            installBehavior2(behavior_mng_service, localPath, True)
    else:
        if(function == "isBehaviorLoaded"):
            isBehaviorLoaded(behavior_mng_service, behavior_name)
        elif(function == "isBehaviorPresent"):
            isBehaviorPresent(behavior_mng_service, behavior_name)
        elif(function == "isBehaviorRunning"):
            isBehaviorRunning(behavior_mng_service, behavior_name)
        elif(function == "getDefaultBehavior"):
            setDefaultBehavior(behavior_mng_service, behavior_name)
        elif(function == "removeDefaultBehavior"):
            setDefaultBehavior(behavior_mng_service, behavior_name)
        elif(function == "preloadBehavior"):
            preloadBehavior(behavior_mng_service, behavior_name)
        elif(function == "runBehavior"):
            runBehavior(behavior_mng_service, behavior_name)
        elif(function == "startBehavior"):
            startBehavior(behavior_mng_service, behavior_name)
        elif(function == "stopBehavior"):
            stopBehavior(behavior_mng_service, behavior_name)

def getBehaviorNames(behavior_mng_service):
    names = behavior_mng_service.getBehaviorNames()
    print "All Behaviors:"
    print names

def getBehaviorNature(behavior_mng_service, behavior):
    nature = behavior_mng_service.getBehaviorNature(behavior)
    print "The behavior nature of " + behavior + ":"
    print nature

def getBehaviorTags(behavior_mng_service, behavior):
    tags = behavior_mng_service.getBehaviorTags(behavior)
    print "The behavior tags of " + behavior + ":"
    print tags

def getInstalledBeviors(behavior_mng_service):
    names = behavior_mng_service.getInstalledBehaviors()
    print "Behaviors on the robot:"
    print names

def getDefaultBehaviors(behavior_mng_service):
    names = behavior_mng_service.getDefaultBehaviors()
    print "Default behaviors:"
    print names

def setDefaultBehavior(behavior_mng_service, behavior_name):
    behavior_mng_service.addDefaultBehavior(behavior_name)
    getDefaultBehaviors(behavior_mng_service)

def removeDefaultBehavior(behavior_mng_service, behavior_name):
    behavior_mng_service.removeDefaultBehavior(behavior_name)
    getDefaultBehaviors(behavior_mng_service)

def getLoadedBehaviors(behavior_mng_service):
    names = behavior_mng_service.getLoadedBehaviors()
    print "Loaded behaviors:"
    print names

def getRunningBehaviors(behavior_mng_service):
    names = behavior_mng_service.getRunningBehaviors()
    print "Running behaviors:"
    print names

def getSystemBehaviorNames(behavior_mng_service):
    names = behavior_mng_service.getSystemBehaviorNames()
    print "System behaviors:"
    print names

def getTagList(behavior_mng_service):
    tags = behavior_mng_service.getTagList()
    print "All tags of the robot:"
    print tags

def getUserBehaviorNames(behavior_mng_service):
    names = behavior_mng_service.getUserBehaviorNames()
    print "User behaviors:"
    print names

def installBehavior(behavior_mng_service, localPath):
    path = behavior_mng_service.installBehavior(localPath)
    print "Install " + localPath + ":"
    print path

def installBehavior2(behavior_mng_service, absolutePath, localPath, overwrite):
    path = behavior_mng_service.installBehavior(absolutePath, localPath, overwrite)
    print "Install absolute " + absolutePath + " local " + localPath + ":"
    print path

def isBehaviorInstalled(behavior_mng_service, name):
    installed = behavior_mng_service.isBehaviorInstalled(name)
    print "The Behavior " + name + " is installed: "
    print installed

def isBehaviorLoaded(behavior_mng_service, behavior):
    loaded = behavior_mng_service.isBehaviorLoaded(behavior)
    print "The Behavior " + behavior + " is loaded: "
    print loaded

def isBehaviorPresent(behavior_mng_service, prefixedBehavior):
    present = behavior_mng_service.isBehaviorPresent(prefixedBehavior)
    print "The Behavior " + prefixedBehavior + " is present: "
    print present

def isBehaviorRunning(behavior_mng_service, behavior):
    running = behavior_mng_service.isBehaviorRunning(behavior)
    print "The Behavior " + behavior + " is running: "
    print running

def preloadBehavior(behavior_mng_service, behavior):
    preload = behavior_mng_service.preloadBehavior(behavior)
    print "Preload the Behavior " + behavior + ": "
    print preload

def runBehavior(behavior_mng_service, behavior):
    run = behavior_mng_service.runBehavior(behavior)
    print "Run the Behavior " + behavior + ": "
    print run

def startBehavior(behavior_mng_service, behavior):
    start = behavior_mng_service.startBehavior(behavior)
    print "Start the Behavior " + behavior + ": "
    print start

def stopBehavior(behavior_mng_service, behavior):
    stop = behavior_mng_service.stopBehavior(behavior)
    print "Stop the Behavior " + behavior + ": "
    print stop

def stopAllBehaviors(behavior_mng_service):
    stop = behavior_mng_service.stopAllBehaviors()
    print "Stopped all behaviors!"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")
    parser.add_argument("--behavior_name", type=str, default="", required=False,
                        help="Name of the behavior")
    parser.add_argument("--function", type=str, required=True,
                        help="Name of called function")
    parser.add_argument("--localPath", type=str, default="",
                        help="local path of behavior install")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session, args.behavior_name, args.function, args.localPath)

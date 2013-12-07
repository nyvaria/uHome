#!/usr/bin/env python

import sys
import yaml
import os
import time
from os import path

SERVER    = <SET-YOUR-SERVER-DIR-HERE>
pluginDir = path.join(SERVER, 'plugins')

if not path.exists(pluginDir):
  print "Path %s doesn't exist" % (pluginDir)
  sys.exit()

essentialsDir = path.join(pluginDir,'Essentials')

if not path.exists(essentialsDir):
    print "Essentials path %s doesn't exist" % essentialsDir
    sys.exit()

userDataDir = path.join(essentialsDir,'userdata')

if not path.exists(userDataDir):
    print "Can't find essentials userdata directory"
    print userDataDir
    sys.exit()

userFiles = os.listdir(userDataDir)

for userFile in userFiles:
    user = os.path.splitext(userFile)[0]

    #print "Parsing Homes: " + userFile

    userData = open(path.join(userDataDir, userFile))
    userYaml = yaml.load(userData)

    if not userYaml:
        continue

    try:
        userHomes = userYaml['homes']

    except KeyError:
        continue

    #print "YAML = \n" + str(userHomes)
    for home in userHomes:
        #print "     Found Home: " + home
        print "INSERT INTO uhomeTable (id, owner, name, world, x, y, z, yaw, pitch, atime, unlocked) " \
            + "VALUES (NULL, '%s', '%s', '%s', '%s', %s, %s, %s, %s, -1, 0);" % \
            ( user \
            , home \
            , userHomes[home]['world'] \
            , userHomes[home]['x'] \
            , userHomes[home]['y'] \
            , userHomes[home]['z'] \
            , userHomes[home]['yaw'] \
            , userHomes[home]['pitch'] )

    userData.close()

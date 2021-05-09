import os
import glob
import sys
import functools
import jsonpickle
from collections import OrderedDict
from Orange.widgets import widget, gui, settings
import Orange.data
from Orange.data.io import FileFormat
from DockerClient import DockerClient
from BwBase import OWBwBWidget, ConnectionDict, BwbGuiElements, getIconName, getJsonName
from PyQt5 import QtWidgets, QtGui

class OWguppySetup(OWBwBWidget):
    name = "guppySetup"
    description = "Downloads files from URL"
    priority = 2
    icon = getIconName(__file__,"guppy_build..png")
    want_main_area = False
    docker_image_name = "biodepot/guppy-setup"
    docker_image_tag = "ubuntu_20.04__cuda_11.3__9f4d152a"
    inputs = [("gpu_url",str,"handleInputsgpu_url"),("trigger",str,"handleInputstrigger")]
    outputs = [("gpu_url",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    gpu_url=pset(None)
    overwrite=pset(False)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"guppySetup")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputsgpu_url(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("gpu_url", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputstrigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("trigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue="/data"
        if hasattr(self,"gpu_url"):
            outputValue=getattr(self,"gpu_url")
        self.send("gpu_url", outputValue)

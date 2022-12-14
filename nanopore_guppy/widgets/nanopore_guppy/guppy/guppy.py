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

class OWguppy(OWBwBWidget):
    name = "guppy"
    description = "Guppy Basecaller"
    priority = 3
    icon = getIconName(__file__,"guppy1.png")
    want_main_area = False
    docker_image_name = "biodepot/guppy"
    docker_image_tag = "latest"
    inputs = [("InputDir",str,"handleInputsInputDir"),("trigger",str,"handleInputstrigger"),("fastqdir",str,"handleInputsfastqdir"),("trigger2",str,"handleInputstrigger2")]
    outputs = [("OutputDir",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    InputDir=pset({})
    OutputDir=pset(None)
    modelFile=pset("ont-guppy/data/template_r9.4.1_450bps_hac.jsn")
    configfile=pset(None)
    device=pset(None)
    flowcell=pset(None)
    kitname=pset(None)
    compressfastq=pset(True)
    chunksPerRunner=pset(1000)
    numCallers=pset(None)
    gpuRunnersPerDevice=pset(None)
    fastqdir=pset(None)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"guppy")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputsInputDir(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("InputDir", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputstrigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("trigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsfastqdir(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("fastqdir", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputstrigger2(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("trigger2", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"OutputDir"):
            outputValue=getattr(self,"OutputDir")
        self.send("OutputDir", outputValue)

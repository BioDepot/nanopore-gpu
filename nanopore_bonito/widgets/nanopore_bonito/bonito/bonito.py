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

class OWbonito(OWBwBWidget):
    name = "bonito"
    description = "Bonito basecaller"
    priority = 20
    icon = getIconName(__file__,"bonito.png")
    want_main_area = False
    docker_image_name = "biodepot/bonito"
    docker_image_tag = "0.3.8__ubuntu_18.04__cuda_10.2-cudnn7"
    inputs = [("InputDir",str,"handleInputsInputDir"),("OutputDir",str,"handleInputsOutputDir"),("Trigger",str,"handleInputsTrigger")]
    outputs = [("OutputDir",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    OutputDir=pset(None)
    InputDir=pset({})
    ModelName=pset(None)
    ChunkSize=pset(4000)
    BatchSize=pset(32)
    fastq=pset(False)
    device=pset("cuda")
    mincoverage=pset(0.9)
    minaccuracy=pset(0.9)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"bonito")) as f:
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
    def handleInputsOutputDir(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("OutputDir", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsTrigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("Trigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"OutputDir"):
            outputValue=getattr(self,"OutputDir")
        self.send("OutputDir", outputValue)

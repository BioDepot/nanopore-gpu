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

class OWminimap2_samtools(OWBwBWidget):
    name = "minimap2_samtools"
    description = "Minimap2 Samtools Alignment"
    priority = 5
    icon = getIconName(__file__,"minimap2.png")
    want_main_area = False
    docker_image_name = "biodepot/minimap2_samtools"
    docker_image_tag = "2.15-r905__1.9__3733bb34"
    inputs = [("outputdir",str,"handleInputsoutputdir"),("indexfile",str,"handleInputsindexfile"),("inputFiles",str,"handleInputsinputFiles"),("trigger",str,"handleInputstrigger")]
    outputs = [("outputfile",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    outputdir=pset(None)
    indexfile=pset(None)
    InputFiles=pset({})
    optionalflags=pset(None)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"minimap2_samtools")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputsoutputdir(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("outputdir", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsindexfile(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("indexfile", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsinputFiles(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("inputFiles", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputstrigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("trigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"outputfile"):
            outputValue=getattr(self,"outputfile")
        self.send("outputfile", outputValue)

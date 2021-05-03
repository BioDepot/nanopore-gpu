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

class OWminimap2_index(OWBwBWidget):
    name = "minimap2_index"
    description = "Minimap2 index genome"
    priority = 4
    icon = getIconName(__file__,"minimap2.png")
    want_main_area = False
    docker_image_name = "biodepot/minimap2-index"
    docker_image_tag = "2.15-r905__d5c53a99"
    inputs = [("indexfile",str,"handleInputsindexfile"),("RefGenome",str,"handleInputsRefGenome"),("trigger",str,"handleInputstrigger")]
    outputs = [("indexfile",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    indexfile=pset(None)
    RefGenome=pset(None)
    kmersize=pset(15)
    windowsize=pset(None)
    hpcminimizer=pset(False)
    maxload=pset(None)
    idxnoseq=pset(False)
    altcontigs=pset(None)
    altdrop=pset(0.15)
    overwrite=pset(False)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"minimap2_index")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputsindexfile(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("indexfile", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsRefGenome(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("RefGenome", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputstrigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("trigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"indexfile"):
            outputValue=getattr(self,"indexfile")
        self.send("indexfile", outputValue)

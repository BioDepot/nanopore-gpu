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
    priority = 8
    icon = getIconName(__file__,"bonito.png")
    want_main_area = False
    docker_image_name = "bonito-cpu"
    docker_image_tag = "latest"
    inputs = [("modelName",str,"handleInputsmodelName"),("readsDirectory",str,"handleInputsreadsDirectory")]
    outputs = [("OutputFile",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    OutputFile=pset(None)
    InputDir=pset(None)
    ModelName=pset(None)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"bonito")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputsmodelName(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("modelName", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsreadsDirectory(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("readsDirectory", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"OutputFile"):
            outputValue=getattr(self,"OutputFile")
        self.send("OutputFile", outputValue)

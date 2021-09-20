from .strg import strg
from .gen8 import gen8
from .bgnd import bgnd
from .optn import optn
from .path import path
from .audo import audo
from .code import code
from .lang import lang
from .sprt import sprt
from .sond import sond
from .tpag import tpag
from .objt import objt
from .txtr import txtr
from .room import room
from .extn import extn
import traceback
import sys
class form:
    def __init__(self, data = None):
        self.strg = None
        if data:
            self.load(data)
    
    def load(self, data):
        if not data.canRead(8):
            raise ValueError("Cannot possibly be FORM data!")
        
        magic = data.readUInt32()
        if magic != 0x4D524F46: #FORM
            raise ValueError("Not a FORM file!")
        
        size = data.readUInt32()
        if not data.canRead(size):
            raise ValueError("FORM data is invalid!")
        
        while data.offset < len(data):
            magic = data.readString(4)
            size = data.readUInt32()
            dataend = data.offset + size
            try:
                if magic == "GEN8" or magic == "GEN7": #Generator, GEN7 is forward compatible with GEN8
                    self.gen8 = gen8(form, data)
                elif magic == "STRG": #Strings
                    self.strg = strg(form, data)
                elif magic == "OPTN": #Options
                    self.optn = optn(form, data)
                elif magic == "PATH": #Paths
                    self.path = path(form, data)
                elif magic == "AUDO": #Audio
                    self.audo = audo(form, data)
                elif magic == "SOND": #Sound
                    self.sond = sond(form, data)
                elif magic == "CODE": #Bytecode
                    self.code = code(form, data)
                elif magic == "BGND": #Background info
                    self.bgnd = bgnd(form, data)
                elif magic == "LANG": #Language info probably
                    self.lang = lang(form, data)
                elif magic == "SPRT": #Sprite data
                    self.sprt = sprt(form, data)
                elif magic == "TPAG": #Texture page
                    self.tpag = tpag(form, data)
                elif magic == "OBJT": #Object
                    self.objt = objt(form, data)
                elif magic == "TXTR": #Texture
                    self.txtr = txtr(form, data)
                elif magic == "ROOM": #Room
                    self.room = room(form, data)
                elif magic == "EXTN": #Room
                    self.extn = extn(form, data)
                else:
                    print("Unknown chunk [{}]".format(magic))
            except Exception as e:
                print("Failed to read chunk [{}]:".format(magic))
                traceback.print_exc(file=sys.stdout)
                data.pop(0)
            data.seek(dataend)

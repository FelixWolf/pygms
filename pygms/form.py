from .strg import strg
from .gen8 import gen8

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
            if magic == "STRG": #Strings
                self.strg = strg(data)
            if magic == "GEN8": #Generator
                self.gen8 = gen8(data)
            else:
                print("Unknown chunk [{}]".format(magic))
            data.seek(dataend)

from .kvp import kvp

class bgnd:
    def __init__(self, form, data = None):
        self.form = form
        self.values = []
        if data:
            self.load(data)
    
    def load(self, data):
        entries = data.readUInt32()
        for i in range(entries):
            entry = kvp()
            #bgnd
            data.push(data.readUInt32())
            
            #name
            entry.name = data.readGMSString()
            
            entry.transparent = data.readUInt32() == 1
            entry.smooth = data.readUInt32() == 1
            entry.preload = data.readUInt32() == 1
            entry.texture = data.readUInt32()
            #/bgnd
            data.pop()
    
    def __getitem__(self, index):
        return self.values[index]
    

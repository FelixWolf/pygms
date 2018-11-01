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
            data.push(data.readUInt32()-4)
            length = data.readUInt32()
            kvp.name = data.readString(length)
            data.pop()
            
            kvp.transparent = data.readUInt32() == 1
            kvp.smooth = data.readUInt32() == 1
            kvp.preload = data.readUInt32() == 1
            kvp.texture = data.readUInt32()
            #/bgnd
            data.pop()
    
    def __getitem__(self, index):
        return self.values[index]
    

from .kvp import kvp

class sond:
    def __init__(self, form, data = None):
        self.form = form
        self.values = {}
        if data:
            self.load(data)
    
    def load(self, data):
        for i in range(data.readUInt32()):
            entry = kvp()
            data.push(data.readUInt32())
            
            data.push(data.readUInt32()-4)
            length = data.readUInt32()
            name = data.readString(length)
            data.pop()
            
            entry.kind = data.readUInt32()
            
            data.push(data.readUInt32()-4)
            length = data.readUInt32()
            entry.extension = data.readString(length)
            data.pop()
            
            data.push(data.readUInt32()-4)
            length = data.readUInt32()
            entry.filename = data.readString(length)
            data.pop()
            
            entry.effects = data.readUInt32()
            
            entry.volume = data.readFloat()
            entry.pan = data.readFloat()
            
            if entry.kind == 0:
                entry.preload = data.readUInt32() == 1
                entry.groupPointer = None
            else:
                entry.preload = False
                entry.groupPointer = data.readUInt32()
                
            entry.groupCount = data.readUInt32()
            
            self.values[name] = entry
            data.pop()
    
    def __contains__(self, key):
        return key in self.values
    
    def __getitem__(self, index):
        return self.values[index]
    

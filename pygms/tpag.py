from .kvp import kvp

class tpag:
    def __init__(self, form, data = None):
        self.form = form
        self.values = []
        self.addresses = []
        if data:
            self.load(data)
    
    def load(self, data):
        for i in range(data.readUInt32()):
            entry = kvp()
            #tpag
            offset = data.readUInt32()
            self.addresses.append(offset)
            data.push(offset)
            entry.x = data.readUInt16()
            entry.y = data.readUInt16()
            entry.width = data.readUInt16()
            entry.height = data.readUInt16()
            entry.xOffset = data.readUInt16()
            entry.yOffset = data.readUInt16()
            entry.cropWidth = data.readUInt16()
            entry.cropHeight = data.readUInt16()
            entry.OW = data.readUInt16()
            entry.OH = data.readUInt16()
            entry.TexturePage = data.readUInt16()
            self.values.append(entry)
            #/tpag
            data.pop()
        
    def from_address(self, addr):
        if addr in self.addresses:
            return self.values[self.addresses.index(addr)]
        return None
    
    def __dir__(self):
        return self.values.keys()
    
    def __getitem__(self, index):
        return self.values[index]
    

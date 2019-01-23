from .kvp import kvp

class txtr:
    def __init__(self, form, data = None):
        self.form = form
        self.values = []
        if data:
            self.load(data)
    
    def load(self, data):
        data.seek(-4, data.SEEK_CUR)
        dataSize = data.readUInt32()
        textures = []
        for i in range(data.readUInt32()):
            offset = data.readUInt32()
            data.push(offset)
            
            unk = data.readUInt32()
            unk = data.readUInt32()
            txtrLoc = data.readUInt32()
            textures.append((unk, unk, txtrLoc))
            
            data.pop()
        
        for i in range(len(textures)):
            entry = kvp()
            end = 0
            if i == len(textures)-1:
                end = textures[i][2]+dataSize
            else:
                end = textures[i+1][2]
            data.push(textures[i][2])
            entry.unk0 = textures[i][0]
            entry.unk1 = textures[i][1]
            entry.data = data.readBytes(end-textures[i][2])
            self.values.append(entry)
            data.pop()
        
    def __dir__(self):
        return self.values.keys()
    
    def __getitem__(self, index):
        return self.values[index]
    

from .kvp import kvp

class sprt:
    def __init__(self, form, data = None):
        self.form = form
        self.values = {}
        if data:
            self.load(data)
    
    def load(self, data):
        for i in range(data.readUInt32()):
            entry = kvp()
            #sprt
            data.push(data.readUInt32())
            
            data.push(data.readUInt32()-4)
            length = data.readUInt32()
            name = data.readString(length)
            data.pop()
            
            entry.width = data.readUInt32()
            entry.height = data.readUInt32()
            entry.bbox = (
                data.readUInt32(), data.readUInt32(),
                data.readUInt32(), data.readUInt32()
            )
            
            entry.transparent = data.readUInt32() == 1
            entry.smooth = data.readUInt32() == 1
            entry.preload = data.readUInt32() == 1
            
            entry.bboxMode = data.readUInt32()
            
            entry.colCheck = data.readUInt32() == 1
            
            entry.origin = (
                data.readUInt32(),
                data.readUInt32()
            )
            
            spriteCount = data.readInt32()
            if spriteCount >= 0:
                #Old sprite format
                spriteCount = data.readUInt32()
                entry.texturePages = []
                for i in range(spriteCount):
                    offset = data.readUInt32()
                    if offset != 0:
                        entry.texturePages.append(offset)
                
                maskCount = data.readUInt32()
                entry.textureMasks = []
                for i in range(maskCount):
                    entry.textureMasks.append(data.readBytes(entry.width*entry.height))
                
                pass
            else:
                dummy = data.readUInt32() # Should always be 1
                entry.spriteType = data.readUInt32()
                entry.playbackSpeed = data.readFloat()
                entry.playbackType = data.readUInt32()
                
                if entry.spriteType == 0:
                    #Basic sprite format
                    spriteCount = data.readUInt32()
                    entry.texturePages = []
                    for i in range(spriteCount):
                        offset = data.readUInt32()
                        if offset != 0:
                            entry.texturePages.append(offset)
                    
                    maskCount = data.readUInt32()
                    entry.textureMasks = []
                    for i in range(maskCount):
                        entry.textureMasks.append(data.readBytes(entry.width*entry.height))
                    
                elif entry.spriteType == 1:
                    #SWF sprite
                    dummy = data.readUInt32() # Should always be 8
                    spriteCount = data.readUInt32()
                    entry.texturePages = []
                    for i in range(spriteCount):
                        entry.texturePages.append(data.readUInt32())
                        
                    dummy = data.readUInt32() #Should always be 4
                    entry.swfData = data.readBytes(data.readUInt32())
                
                elif entry.spriteType == 2:
                    #Spine data
                    entry.spineData = data.readBytes(data.readUInt32())
            
            self.values[name] = entry
            #/sprt
            data.pop()
        
    def __dir__(self):
        return self.values.keys()
    
    def __getitem__(self, index):
        return self.values[index]
    

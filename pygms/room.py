from .kvp import kvp

class room:
    def __init__(self, form, data = None):
        self.form = form
        self.values = {}
        if data:
            self.load(data)
    
    FLAG_ENABLE_VIEWS = 1
    FLAG_VIEW_CLEAR_SCREEN = 2
    FLAG_CLEAR_DISPLAY_BUFFER = 4
    FLAG_HAS_LAYERS = 131072
    
    def load(self, data):
        for i in range(data.readUInt32()):
            entry = kvp()
            #tpag
            
            data.push(data.readUInt32())
            
            name = data.readGMSString()
            
            entry.caption = data.readGMSString()
            
            entry.width = data.readUInt32()
            entry.height = data.readUInt32()
            
            entry.speed = data.readUInt32()
            entry.persistent = data.readUInt32() == 1
            entry.colour = data.readInt32()
            entry.showColour = data.readUInt32() == 1
            
            entry.code = data.readInt32()
            
            entry.flags = data.readUInt32()
            
            #Background (This is probably incorrect)
            data.push(data.readUInt32())
            entry.backgrounds = []
            for i in range(data.readUInt32()):
                data.push(data.readUInt32())
                bgEntry = kvp()
                bgEntry.visible = data.readUInt32() == 1
                bgEntry.foreground = data.readUInt32() == 1
                bgEntry.index = data.readInt32()
                bgEntry.position = (
                    data.readInt32(),
                    data.readInt32(),
                )
                bgEntry.hTiled = data.readUInt32() == 1
                bgEntry.vTiled = data.readUInt32() == 1
                bgEntry.speed = (
                    data.readInt32(),
                    data.readInt32(),
                )
                bgEntry.stretch = data.readUInt32() == 1
                entry.backgrounds.append(bgEntry)
                data.pop()
            data.pop()
            
            #Views
            data.push(data.readUInt32())
            entry.views = []
            for i in range(data.readUInt32()):
                data.push(data.readUInt32())
                view = kvp()
                view.visible = data.readUInt32() == 1
                view.position = (
                    data.readInt32(),
                    data.readInt32(),
                )
                view.size = (
                    data.readInt32(),
                    data.readInt32(),
                )
                view.portPosition = (
                    data.readInt32(),
                    data.readInt32(),
                )
                view.portSize = (
                    data.readInt32(),
                    data.readInt32(),
                )
                view.border = (
                    data.readInt32(),
                    data.readInt32(),
                )
                view.speed = (
                    data.readInt32(),
                    data.readInt32(),
                )
                view.index = data.readInt32()
                entry.views.append(view)
                data.pop()
            data.pop()
            
            #Instances
            data.push(data.readUInt32())
            entry.instances = []
            for i in range(data.readUInt32()):
                data.push(data.readUInt32())
                instance = kvp()
                instance.position = (
                    data.readInt32(),
                    data.readInt32(),
                )
                instance.index = data.readInt32()
                instance.id = data.readInt32()
                instance.code = data.readInt32()
                instance.scale = (
                    data.readFloat(),
                    data.readFloat(),
                )
                instance.colour = data.readInt32()
                instance.rotation = data.readFloat()
                instance.preCreateCode = data.readInt32()
                entry.instances.append(instance)
                data.pop()
            data.pop()
            
            #Tiles
            data.push(data.readUInt32())
            entry.tiles = []
            for i in range(data.readUInt32()):
                data.push(data.readUInt32())
                tile = kvp()
                tile.position = (
                    data.readInt32(),
                    data.readInt32(),
                )
                tile.index = readInt32()
                tile.position_origin = (
                    data.readInt32(),
                    data.readInt32(),
                )
                tile.size = (
                    data.readInt32(),
                    data.readInt32(),
                )
                tile.depth = data.readInt32()
                tile.id = data.readInt32()
                tile.scale = (
                    data.readFloat(),
                    data.readFloat(),
                )
                tile.blending = data.readUInt32()
                tile.blending = (
                    tile.blending&0xFFFFFF, #Unknown
                    tile.blending>>24 #Alpha
                )
                
                entry.tiles.append(tile)
                data.pop()
            data.pop()
            
            entry.physicsWorld = data.readUInt32() == 1
            entry.physicsBBox = (
                data.readUInt32(), #Top
                data.readUInt32(), #Left
                data.readUInt32(), #Right
                data.readUInt32(), #Bottom
            )
            entry.physicsGravity = (
                data.readFloat(), #X
                data.readFloat(), #y
            )
            entry.physicsMeterSize = data.readFloat()
            
            if entry.flags & self.FLAG_HAS_LAYERS == self.FLAG_HAS_LAYERS:
                data.push(data.readUInt32())
                
                entry.layers = {}
                for i in range(data.readUInt32()):
                    data.push(data.readUInt32())
                    layer = kvp()
                    lName = data.readGMSString()
                    
                    layer.id = data.readInt32()
                    layer.type = data.readInt32()
                    layer.depth = data.readInt32()
                    layer.offset = (
                        data.readFloat(),
                        data.readFloat(),
                    )
                    layer.speed = (
                        data.readFloat(),
                        data.readFloat(),
                    )
                    layer.visible = data.readUInt32() == 1
                    
                    if layer.type == 1:
                        lData = kvp()
                        lData.visible = data.readUInt32() == 1
                        lData.foreground = data.readUInt32() == 1
                        lData.index = data.readInt32()
                        lData.hTiled = data.readUInt32() == 1
                        lData.vTiled = data.readUInt32() == 1
                        lData.stretch = data.readUInt32() == 1
                    
                        lData.blending = data.readUInt32()
                        lData.blending = (
                            lData.blending&0xFFFFFF, #Unknown
                            lData.blending>>24 #Alpha
                        )
                        lData.firstFrame = data.readFloat()
                        lData.animationFPS = data.readFloat()
                        lData.animationSpeedType = data.readUInt32()
                        layer.data = lData
                        
                    elif layer.type == 2:
                        lData = []
                        for i in range(data.readUInt32()):
                            lData.append(data.readUInt32())
                            
                    elif layer.type == 3:
                        lData = kvp()
                        lData.tiles = []
                        data.push(data.readUInt32())
                        for i in range(data.readUInt32()):
                            lData.tiles.append(data.readUInt32())
                        data.pop()
                        
                        lData.sprites = []
                        data.push(data.readUInt32())
                        for i in range(data.readUInt32()):
                            lData.sprites.append(data.readUInt32())
                        data.pop()
                        
                    elif layer.type == 4:
                        lData = kvp()
                        lData.index = data.readInt32()
                        lData.mapSize = (
                            data.readInt32(),
                            data.readInt32(),
                        )
                        lData.tiles = []
                        #How do we do this? What is the data type used here?
                        for i in range(0):
                            lData.tiles.append(data.readUInt32())
                    
                    else:
                        print("Unknown layer type [{}]!".format(layer.type))
                    entry.layers[lName] = layer
                    data.pop()
                #Layers
                data.pop()
            
            #print(entry.__values__)
            #exit()
            self.values[name] = entry
            #/tpag
            data.pop()

    def __dir__(self):
        return self.values.keys()
    
    def __contains__(self, key):
        return key in self.values
    
    def __getitem__(self, index):
        return self.values[index]

from .kvp import kvp

class objt:
    def __init__(self, form, data = None):
        self.form = form
        self.values = {}
        if data:
            self.load(data)
    
    def load(self, data):
        for i in range(data.readUInt32()):
            entry = kvp()
            #objt
            data.push(data.readUInt32())
            
            name = data.readGMSString()
            
            entry.sprite = data.readInt32()
            if entry.sprite == -1:
                entry.sprite = None
            
            entry.visible = data.readUInt32() == 1
            entry.solid = data.readUInt32() == 1
            entry.depth = data.readUInt32()
            entry.persistant = data.readUInt32() == 1
            entry.parent = data.readUInt32()
            entry.mask = data.readUInt32()
            
            hasPhysics = data.readUInt32() == 1
            entry.physics = {}
            entry.physics["Sensor"] = data.readUInt32() == 1
            entry.physics["Shape"] = data.readUInt32()
            entry.physics["Density"] = data.readFloat()
            entry.physics["Restitution"] = data.readFloat()
            entry.physics["Group"] = data.readUInt32()
            entry.physics["LinearDamping"] = data.readFloat()
            entry.physics["AngularDamping"] = data.readFloat()
            vertexCount = data.readUInt32()
            entry.physics["Friction"] = data.readFloat()
            entry.physics["Awake"] = data.readUInt32() == 1
            entry.physics["Kinematic"] = data.readUInt32() == 1
            entry.physics["Vertices"] = []
            for i in range(vertexCount):
                entry.physics["Vertices"].append((data.readFloat(), data.readFloat()))
            self.values[name] = entry
            #/objt
            data.pop()
    
    def __dir__(self):
        return self.values.keys()
    
    def __contains__(self, key):
        return key in self.values
    
    def __getitem__(self, index):
        return self.values[index]
    

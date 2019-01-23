class code:
    def __init__(self, form, data = None):
        self.form = form
        self.values = {}
        if data:
            self.load(data)
    
    def load(self, data):
        for i in range(data.readUInt32()):
            #code
            data.push(data.readUInt32())
            
            #name
            data.push(data.readUInt32()-4)
            length = data.readUInt32()
            name = data.readString(length)
            data.pop()
            #/name
            
            #value
            length = data.readUInt32()
            value = data.readBytes(length)
            #/value
            self.values[name] = value
            
            data.pop()
            #/code
    
    def __dir__(self):
        return self.values.keys()
    
    def __contains__(self, key):
        return key in self.values
    
    def __getitem__(self, index):
        return self.values[index]
    

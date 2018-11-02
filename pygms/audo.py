class audo:
    def __init__(self, form, data = None):
        self.form = form
        self.values = []
        if data:
            self.load(data)
    
    def load(self, data):
        for i in range(data.readUInt32()):
            while (data.offset & 3) != 0:
                data.offset += 1
            data.push(data.readUInt32())
            self.values.append(data.readBytes(data.readUInt32()))
            data.pop()
    
    def __getitem__(self, index):
        return self.values[index]
    

class strg:
    def __init__(self, data = None):
        self.values = []
        if data:
            self.load(data)
    
    def load(self, data):
        entries = data.readUInt32()
        addresses = []
        for i in range(entries):
            addresses.append(data.readUInt32())
        
        for i in range(entries):
            data.seek(addresses[i])
            length = data.readUInt32()
            self.values.append(data.readString(length))
    
    def __getitem__(self, index):
        return self.values[index]
    

class strg:
    def __init__(self, form, data = None):
        self.form = form
        self.values = []
        self.addresses = []
        if data:
            self.load(data)
    
    def load(self, data):
        entries = data.readUInt32()
        self.addresses = []
        for i in range(entries):
            self.addresses.append(data.readUInt32())
        
        for i in range(entries):
            data.seek(self.addresses[i])
            length = data.readUInt32()
            self.values.append(data.readString(length))
    
    def from_address(self, addr):
        if addr in self.addresses:
            return self.values[self.addresses.index(addr)]
        return None
    
    def __getitem__(self, index):
        return self.values[index]
    

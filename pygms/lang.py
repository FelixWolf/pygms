class lang:
    def __init__(self, form, data = None):
        self.form = form
        self.values = {}
        if data:
            self.load(data)
    
    def load(self, data):
        if data.readUInt32() == 1:
            languageCount = data.readUInt32()
            languageEntryCount = data.readUInt32()
            if languageCount > 0:
                for i in range(languageEntryCount):
                    data.push(data.readUInt32()-4)
                    length = data.readUInt32()
                    languageID = data.readString(length)
                    data.pop()
                
                for i in range(languageCount):
                    data.push(data.readUInt32()-4)
                    length = data.readUInt32()
                    language = data.readString(length)
                    data.pop()
                    
                    data.push(data.readUInt32()-4)
                    length = data.readUInt32()
                    region = data.readString(length)
                    data.pop()
                    
                    for ii in range(languageEntryCount):
                        data.push(data.readUInt32()-4)
                        length = data.readUInt32()
                        languageString = data.readString(length)
                        data.pop()
        
        else:
            raise ValueError("Expected 1, got not 1!")
        
    def __dir__(self):
        return self.values.keys()
    
    def __getitem__(self, index):
        return self.values[index]
    

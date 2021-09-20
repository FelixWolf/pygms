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
                    languageID = data.readGMSString()
                
                for i in range(languageCount):
                    language = data.readGMSString()
                    
                    region = data.readGMSString()
                    
                    for ii in range(languageEntryCount):
                        languageString = data.readGMSString()
        
        else:
            raise ValueError("Expected 1, got not 1!")
        
    def __dir__(self):
        return self.values.keys()
    
    def __getitem__(self, index):
        return self.values[index]
    

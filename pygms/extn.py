from .kvp import kvp

class extn:
    def __init__(self, form, data = None):
        self.form = form
        self.values = []
        if data:
            self.load(data)
    
    def load(self, data):
        entries = data.readUInt32()
        for i in range(entries):
            entry = kvp()
            #extn
            data.push(data.readUInt32())
            
            #name
            entry.empty = data.readGMSString()
            
            #name
            entry.name = data.readGMSString()
            
            #classname
            entry.classname = data.readGMSString()
            
            #extensions
            entry.files = []
            files = data.readUInt32()
            for ii in range(files):
                #extension
                data.push(data.readUInt32()-4)
                file = kvp()
                entry.files.push(file)
                
                #name
                file.name = data.readGMSString()
                
                #destructor
                file.destructor = data.readGMSString()
                
                #constructor
                file.constructor = data.readGMSString()
                file.type = data.readUInt32()
                
                
                functions = data.readUInt32()
                for iii in range(functions):
                    #function
                    data.push(data.readUInt32()-4)
                    function = kvp()
                    
                    #name
                    function.name = data.readGMSString()
                    
                    function.id = data.readUInt32()
                    function.type = data.readUInt32()
                    function.returntype = data.readUInt32()
                    
                    #extname
                    function.extname = data.readGMSString()
                    
                    function.arguments = []
                    for iiii in range(data.readUInt32()):
                        function.arguments.push(data.readUInt32())
                    
                    #/function
                    data.pop()
                data.pop()
                #/extension
            self.values.push(entry)
            #/extn
            data.pop()
    
    def __getitem__(self, index):
        return self.values[index]
    

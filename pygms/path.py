class path:
    def __init__(self, form, data = None):
        self.form = form
        self.values = []
        if data:
            self.load(data)
    
    def load(self, data):
        pass
        #Unknown, no games that use this
        #for i in range(data.readUInt32()):
            #Format should be:
            #UInt32 Dummy (Unknown, probably unused
            #UInt32 Kind
            #UInt32(Bool) Closed
            #UInt32 Precision
            #UInt32 Points
            #for i in points:
            # float x
            # float y
            # float speed
    
    def __getitem__(self, index):
        return self.values[index]
    

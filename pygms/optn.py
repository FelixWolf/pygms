class optn:
    def __init__(self, form, data = None):
        self.form = form
        self.values = {}
        if data:
            self.load(data)
    
    #Whole bunch of things. :(            values
    OPTION_FULL_SCREEN                  = 0x00000001
    OPTION_INTEROPLATE_PIXELS           = 0x00000002
    OPTION_USE_NEW_AUDIO                = 0x00000004
    OPTION_NO_BORDER                    = 0x00000008
    OPTION_SHOW_CURSOR                  = 0x00000010
    OPTION_SIZEABLE                     = 0x00000020
    OPTION_STAY_ON_TOP                  = 0x00000040
    OPTION_CHANGE_RESOLUTION            = 0x00000080
    OPTION_NO_BUTTON                    = 0x00000100
    OPTION_SCREEN_KEY                   = 0x00000200
    OPTION_HELP_KEY                     = 0x00000400
    OPTION_QUIT_KEY                     = 0x00000800
    OPTION_SAVE_KEY                     = 0x00001000
    OPTION_SCREEN_SHOT_KEY              = 0x00002000
    OPTION_CLOSE_SEC                    = 0x00004000
    OPTION_FREEZE                       = 0x00008000
    OPTION_SHOW_PROGRESS                = 0x00010000
    OPTION_LOAD_TRANSPARENT             = 0x00020000
    OPTION_SCALE_PROGRESS               = 0x00040000
    OPTION_DISPLAY_ERRORS               = 0x00080000
    OPTION_WRITE_ERRORS                 = 0x00100000
    OPTION_ABORT_ERRORS                 = 0x00200000
    OPTION_VARIABLE_ERRORS              = 0x00400000
    OPTION_CREATION_EVENT_ORDER         = 0x00800000
    OPTION_USE_FRONT_TOUCH              = 0x01000000
    OPTION_USE_REAR_TOUCH               = 0x02000000
    OPTION_USE_FAST_COLLISION           = 0x04000000
    OPTION_FAST_COLLISION_COMPATIBILITY = 0x08000000
    
    def load(self, data):
        dummy = data.readUInt32()
        if data.readUInt32() == 2:
            self.values["Flags"] = data.readUInt64()
            self.values["Scale"] = data.readUInt32()
            self.values["WindowColour"] = data.readUInt32()
            self.values["ColourDepth"] = data.readUInt32()
            self.values["Resolution"] = data.readUInt32()
            self.values["Frequency"] = data.readUInt32()
            self.values["Sync_Vertex"] = data.readUInt32()
            self.values["Priority"] = data.readUInt32()
            
            self.values["BackImage"] = data.readUInt32()
            self.values["FrontImage"] = data.readUInt32()
            self.values["LoadImage"] = data.readUInt32()
            self.values["LoadAlpha"] = data.readUInt32()
            
            for i in range(data.readUInt32()):
                data.push(data.readUInt32()-4)
                length = data.readUInt32()
                key = data.readString(length)
                data.pop()
                
                data.push(data.readUInt32()-4)
                length = data.readUInt32()
                value = data.readString(length)
                data.pop()
                if key!="" and value!="":
                    self.values[key] = value

        else:
            raise ValueError("Expected 2, got not 2!")
    
    def __dir__(self):
        return self.values.keys()
    
    def __getitem__(self, index):
        return self.values[index]
    

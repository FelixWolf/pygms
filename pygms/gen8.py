import datetime
import uuid

class gen8:
    def __init__(self, data = None):
        self.values = {}
        if data:
            self.load(data)
        
        #print(self.values)
    
    OPTION_FULLSCREEN = 1
    OPTION_INTERPOLATE_PIXELS = 8
    OPTION_SCALE = 16
    OPTION_SHOW_CURSOR = 32
    OPTION_SIZABLE = 64
    OPTION_SCREEN_KEY = 128
    OPTION_STUDIO_EDITION_TRIAL = 512 #Unconfirmed
    OPTION_STUDIO_EDITION_CREATOR = 1024 #Unconfirmed
    OPTION_STUDIO_EDITION_DEVELOPER = 2048 #Unconfirmed
    OPTION_STUDIO_EDITION_CONSOLE = 1536 #Unconfirmed
    OPTION_STEAM_PROJECT = 4096
    OPTION_YOYOPLAYER = 4096
    OPTION_SAVE_LOCATION = 8192
    OPTION_BORDERLESS = 16384
    OPTION_UNKNOWN_CODE_TYPE = 32768
    OPTION_OVERRIDE_HOBBY_SPLASH = 65536
    
    def load(self, data):
        self.values["Debug"] = data.readUInt32() & 1
        
        data.push(data.readUInt32()-4)
        length = data.readUInt32()
        self.values["FileName"] = data.readString(length)
        data.pop()
        
        data.push(data.readUInt32()-4)
        length = data.readUInt32()
        self.values["Config"] = data.readString(length)
        data.pop()
        
        self.values["RoomMaxId"] = data.readUInt32()
        
        self.values["RoomMaxTileId"] = data.readUInt32()
        
        self.values["GameID"] = data.readUInt32()
        
        dummy = data.readUInt32()
        dummy = data.readUInt32()
        dummy = data.readUInt32()
        dummy = data.readUInt32()
        
        data.push(data.readUInt32()-4)
        length = data.readUInt32()
        self.values["GameName"] = data.readString(length)
        data.pop()
        
        self.values["MajorVersion"] = data.readUInt32()
        self.values["MinorVersion"] = data.readUInt32()
        self.values["ReleaseVersion"] = data.readUInt32()
        self.values["BuildVersion"] = data.readUInt32()
        self.values["version"] = (self.values["MajorVersion"], self.values["MinorVersion"], self.values["ReleaseVersion"], self.values["BuildVersion"])
        
        self.values["Width"] = data.readUInt32()
        self.values["Height"] = data.readUInt32()
        self.values["WindowSize"] = (self.values["Width"], self.values["Height"])
        
        self.values["Options"] = data.readUInt32()
        
        self.values["Option"] = {
            "FullScreen": self.values["Options"]&gen8.OPTION_FULLSCREEN == gen8.OPTION_FULLSCREEN,
            #"Sync_Vertex & 0x01": ???,
            #"Sync_Vertex & 0x80000000": ???,
            "InterpolatePixels": self.values["Options"]&gen8.OPTION_INTERPOLATE_PIXELS == gen8.OPTION_INTERPOLATE_PIXELS,
            "Scale": self.values["Options"]&gen8.OPTION_SCALE == gen8.OPTION_SCALE,
            "ShowCursor": self.values["Options"]&gen8.OPTION_SHOW_CURSOR == gen8.OPTION_SHOW_CURSOR,
            "Sizeable": self.values["Options"]&gen8.OPTION_SIZABLE == gen8.OPTION_SIZABLE,
            "ScreenKey": self.values["Options"]&gen8.OPTION_SCREEN_KEY == gen8.OPTION_SCREEN_KEY,
            #"Sync_Vertex & 0x40000000": ???,
            "SaveLocation": self.values["Options"]&gen8.OPTION_SAVE_LOCATION == gen8.OPTION_SAVE_LOCATION,
            "Borderless": self.values["Options"]&gen8.OPTION_BORDERLESS == gen8.OPTION_BORDERLESS,
            "OverrideHobbySplash": self.values["Options"]&gen8.OPTION_OVERRIDE_HOBBY_SPLASH == gen8.OPTION_OVERRIDE_HOBBY_SPLASH,
            "Unknown_CodeType": self.values["Options"]&gen8.OPTION_UNKNOWN_CODE_TYPE == gen8.OPTION_UNKNOWN_CODE_TYPE,
        }
        
        self.values["LicenseCRC"] = data.readUInt32()
        
        self.values["LicenceMD5"] = "".join(["{:0>2x}".format(i) for i in data.readBytes(16)])
        
        self.values["BuildTime"] = datetime.datetime.utcfromtimestamp(data.readUInt64())
        
        data.push(data.readUInt32()-4)
        length = data.readUInt32()
        self.values["DisplayName"] = data.readString(length)
        data.pop()
        
        self.values["ActiveTargets"] = ((data.readUInt32() << 32) | data.readUInt32())
        
        self.values["FunctionClassifications"] = ((data.readUInt32() << 32) | data.readUInt32())
        
        self.values["SteamAppId"] = data.readUInt32()
        
        self.values["DebuggerPort"] = data.readUInt32()
        
        self.values["RoomOrder"] = []
        for i in range(data.readUInt32()):
            self.values["RoomOrder"].append(data.readUInt32())
        
        if self.values["MajorVersion"] >= 2:
            #Signature stuff, probably unimportant, might implement later
            #Double RandSeed
            #Double[4] Game Signature (???)
            data.seek(40, data.SEEK_CUR)
            
            #Return to normal activities. This still requires MajorVersion >= 2
            self.values["GameSpeed"] = data.readFloat() #In FPS
            self.values["AllowStatistics"] = data.readUInt32() == True
            
            self.values["GameGUID"] = uuid.UUID(bytes=data.readBytes(16))
            
        
    def __dir__(self):
        return dir(self.values)
    
    def __getitem__(self, index):
        return self.values[index]
    

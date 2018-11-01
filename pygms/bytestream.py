#!/usr/bin/env python3
import struct

class bytestream:
    def __init__(self, data, byteorder = "big"):
        self.data = data
        self.offset = 0
        if byteorder == "big" or byteorder == ">":
            self.byteorder = ">"
        elif byteorder == "little" or byteorder == "<":
            self.byteorder = "<"
        else:
            raise ValueError("byteorder must be either 'big' or 'little'")
    
    SEEK_SET = 0
    SEEK_CUR = 1
    SEEK_END = 2
    def seek(self, offset, direction = SEEK_SET):
        if direction == bytestream.SEEK_SET:
            self.offset = offset
        elif direction == bytestream.SEEK_CUR:
            self.offset += offset
        elif direction == bytestream.SEEK_END:
            self.offset = len(self.data) + offset
        else:
            raise ValueError("Unsupported seek operation!")
    
    def __len__(self):
        return len(self.data)
    
    def __repr__(self):
        return "<bytestream {} @ {}>".format(len(self), self.offset)
    
    def __bytes__(self):
        return self.data
    
    def canRead(self, length, raiser=False):
        if raiser:
            if self.offset+length > len(self.data):
                raise ValueError("offset({})+length({}) is greater than data length({})".format(self.offset, length, len(self.data)))
        else:
            return self.offset+length <= len(self.data)
    
    def unpack(self, fmt):
        return struct.unpack_from(fmt, self.data, self.offset)
    
    def readInt8(self):
        self.canRead(1, True)
        
        result = struct.unpack_from(self.byteorder+"b", self.data, self.offset)[0]
        self.offset += 1
        return result
    
    def readUInt8(self):
        self.canRead(1, True)
        
        result = struct.unpack_from(self.byteorder+"B", self.data, self.offset)[0]
        self.offset += 1
        return result
    
    def readInt16(self):
        self.canRead(2, True)
        
        result = struct.unpack_from(self.byteorder+"h", self.data, self.offset)[0]
        self.offset += 2
        return result
    
    def readUInt16(self):
        self.canRead(2, True)
        
        result = struct.unpack_from(self.byteorder+"H", self.data, self.offset)[0]
        self.offset += 2
        return result
    
    def readInt32(self):
        self.canRead(4, True)
        
        result = struct.unpack_from(self.byteorder+"i", self.data, self.offset)[0]
        self.offset += 4
        return result
    
    def readUInt32(self):
        self.canRead(4, True)
        
        result = struct.unpack_from(self.byteorder+"I", self.data, self.offset)[0]
        self.offset += 4
        return result
    
    def readInt64(self):
        self.canRead(8, True)
        
        result = struct.unpack_from(self.byteorder+"q", self.data, self.offset)[0]
        self.offset += 8
        return result
    
    def readUInt64(self):
        self.canRead(8, True)
        
        result = struct.unpack_from(self.byteorder+"Q", self.data, self.offset)[0]
        self.offset += 8
        return result
    
    def readFloat(self):
        self.canRead(4, True)
        
        result = struct.unpack_from(self.byteorder+"f", self.data, self.offset)[0]
        self.offset += 4
        return result
    
    def readDouble(self):
        self.canRead(8, True)
        
        result = struct.unpack_from(self.byteorder+"d", self.data, self.offset)[0]
        self.offset += 8
        return result
    
    def readBytes(self, size):
        self.canRead(size, True)
        
        result = self.data[self.offset:self.offset+size]
        self.offset += size
        return result
    
    def readString(self, size):
        return self.readBytes(size).decode()
    
    def readStream(self, size, byteorder = None):
        self.canRead(size, True)
        
        result = bytestream(self.data[self.offset:self.offset+size], byteorder = byteorder or self.byteorder)
        self.offset += size
        return result
    

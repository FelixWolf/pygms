from .form import form
from .strg import strg
from .bytestream import ByteStream

class GMSByteStream(ByteStream):
    def readGMSString(self):
        offset = self.readUInt32()
        if offset == 0:
            return ""
        self.push(offset-4)
        length = self.readUInt32()
        result = self.readBytes(length).decode()
        self.pop()
        return result
        

def load(file):
    with open(file, "rb") as f:
        data = GMSByteStream(f.read(), "<")
        return form(data)

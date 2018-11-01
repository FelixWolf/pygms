from .form import form
from .strg import strg
from .bytestream import bytestream

def load(file):
    with open(file, "rb") as f:
        data = bytestream(f.read(), "<")
        return form(data)

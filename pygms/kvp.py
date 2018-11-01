class kvp:
    def __init__(self):
        super(kvp, self).__setattr__("__values__", {})
    
    def __getitem__(self, key):
        if key not in self.__values__:
            raise IndexError("[{}] is not in [{}]".format(key, self))
        return self.__values__[key]
    
    def __getattr__(self, key):
        return self.__values__[key]
    
    def __setitem__(self, key, value):
        self.__values__[key] = value
    
    def __setattr__(self, key, value):
        self.__values__[key] = value
    
    def __delitem__(self, key, value):
        del self.__values__[key]
    
    def __delattr__(self, key):
        del self.__values__[key]
    
    def __dir__(self):
        yield dir(self.__values__)
        
    def __contains__(self, item):
        return item in self.__values__
    
    def __len__(self):
        return len(self.__values__.keys())
    
    def __repr__(self):
        return "<KeyValue Pair ({}) at 0x{:x}>".format(len(self), id(self))

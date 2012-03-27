
class Proxy:
    def __init__(self, subject):
        self.__subject = subject
        
    def __getattr__( self, name ):
        return getattr( self.__subject, name )

class Struct:
    def __init__(self, **entries): 
        self.__dict__.update(entries)
class Person:
    """
    Construct Family Tree Layout
    
    """
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

class Male(Person):
    """
    Construct male role in the tree
    """
    def __init__(self,name):
        Person.__init__(self,name,"Male")
        self.husbandOf=None
        self.sonOf=None             
        
class Female(Person):
    """
    Construct Female role in the tree
    """
    def __init__(self,name):
        Person.__init__(self,name,"Female")
        self.wifeOf=None
        self.daughterOf=None        
        self.children=list()        




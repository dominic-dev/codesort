from sortable import Sortable

class Attribute(Sortable):
    def __init__(self, name, dataType, modifier=None, final=False):
        self.name = name
        self.dataType = dataType
        self.modifier = modifier
        self.final = final


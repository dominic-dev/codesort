from sortable import Sortable
class Method(Sortable):
    def __init__(self, name, dataType, line_start, modifier=None, final=False):
        self.name = name
        self.dataType = dataType
        self.modifier = modifier
        self.final = final
        self.line_start = line_start
        self.line_end self.get_line_end()
        self.docstring = self.get_docstring()

    """
    Return the docstring if it is found for this method
    return None otherwise
    """
    def get_docstring(self):
        return None

    """
    Return the last line of the method
    """
    def get_line_end(self):
        return None

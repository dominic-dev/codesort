import vim
import re
from collections import OrderedDict

def main():
    # Get buffer
    (start_line, start_col) = vim.current.buffer.mark('<')
    (end_line, end_col) = vim.current.buffer.mark('>')
    lines = vim.eval('getline({}, {})'.format(start_line, end_line))
    lines[0] = lines[0][start_col:]
    lines[-1] = lines[-1][:end_col]


    # Read attributes
    #attributes = Attribute.read(lines)

    # Replace original text
    i = start_line - 1
    del vim.current.buffer[i:end_line]

    Attribute.sort(lines, i)

class Sortable():
    def __init__(self, name, data_type, text, modifier=None):
        self.name = name
        self.dataType = data_type
        self.text = text;
        self.modifier = modifier

    def __cmp__(self, other):
        return cmp(self.name, other.name)

    def __lt__(self, other):
         return self.name < other.name


class Attribute(Sortable):
    def __init__(self, name, data_type, text, modifier=None, final=False):
        super().__init__(name, data_type, text, modifier)
        self.final = final

    """
    Take an array of lines, return a dictionary with attributes
    """
    @staticmethod
    def _read(lines):
        attributes = {}
        pattern = re.compile(r"(public|private|protected)\s?(static)?(final)?\s?([A-Za-z0-9]+)\s([A-Za-z0-9]+)")
        for l in lines:
            match = pattern.search(l)
            if match:
                (modifier, static, final, data_type, name) = match.groups()
                attributes.setdefault(modifier, []).append(Attribute(name, data_type,\
                                                                    l, modifier, final ))
            else:
                attributes.setdefault('no_attr', []).append(l)
        return attributes

    """
    Take an array of lines, and a starting line number
    And replace the lines, sorted by attribute modifier and name
    """
    @staticmethod
    def sort(lines, start):
        attributes = Attribute._read(lines)
        if attributes.get('no_attr'):
            no_attr = attributes.pop('no_attr')
            vim.current.buffer.append(no_attr, start)
            start += len(no_attr)

        for key, values in attributes.items():
            #values.sort(key=lambda x: x.name)
            values.sort()
            vim.current.buffer.append([v.text for v in values], start)


class Method(Sortable):
    """
    Take an array of lines, return a dictionary with attributes
    """
    @staticmethod
    def _read(lines):
        attributes = {}
        pattern =
        re.compile(r"(public|private|protected)\s?(static)?\s?([A-Za-z0-9]+)\s([A-Za-z0-9]+).*{")
        i = 0
        for l in lines:
            match = pattern.search(l)
            if match:
                text = []
                (modifier, static, data_type, name) = match.groups()
                attributes.setdefault(modifier, []).append(Attribute(name, data_type,\
                                                                    l, modifier, final ))
                l2 = lines[i:]
                number_of_lines = 1
                while (not l2.contains('}')):
                    number_of_lines += 1

            else:
                attributes.setdefault('no_attr', []).append(l)
            i += 1
        return attributes

    """
    Take an array of lines, and a starting line number
    And replace the lines, sorted by attribute modifier and name
    """
    @staticmethod
    def sort(lines, start):
        attributes = Attribute._read(lines)
        if attributes.get('no_attr'):
            no_attr = attributes.pop('no_attr')
            vim.current.buffer.append(no_attr, start)
            start += len(no_attr)

        for key, values in attributes.items():
            #values.sort(key=lambda x: x.name)
            values.sort()
            vim.current.buffer.append([v.text for v in values], start)


main()

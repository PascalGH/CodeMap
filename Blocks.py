# This is the main file to experiment code analysis

# Import of external files and modules
import Keywords_Map # Own module where keywords are associated with fonctions to perform
import re # Regular expressions

myblock = Keywords_Map.block_indicators
myblockkeys = myblock.keys()
mycomment = Keywords_Map.comment_indicator
myeol = Keywords_Map.eol_indicator
myindent = Keywords_Map.indent_length


class block:
    def __init__(self, name, indent, content):
        self.name = name
        self.indent = indent
        self.content = content
        self.blocks = []
        self.comments = []

    def addblock(self, name, indent, content):
        self.newblock = block(name, indent, content)
        self.blocks.append(self.newblock)

    def analyse(self):
        indent = 0
        for line in self.content:
            print(line)
            sub_line = line.split(mycomment)
            if sub_line[0] != '':
                term = sub_line[0].split()[0].lower()
                for i in myblockkeys:
                    if re.search(i,term):
                        left = list((re.findall(r'\s+', line)))
                        nb_chars = len(left[0])
                        if nb_chars == 1:
                            indent = 0
                        else:
                            indent = int(nb_chars / myindent)
                            # Here we create a new block below
                            self.content = self.content.pop(0)
                            self.addblock('block', indent, self.content)
                            self.blocks[len(self.blocks) - 1].analyse()
                        break
                if len(sub_line) > 1:
                    # print(f'Comment: ',sub_line[1])
                    self.comments.append(sub_line[1])
            else:
                if len(sub_line) > 1:
                    # print(f'Comment: ',sub_line[1])
                    self.comments.append(sub_line[1])
        self.content = self.content.pop(0)
        print(self.content)
        return self.content

f = open("Analyser.py","r")
content = f.read().split(myeol)
f.close()
main_block = block(name = 'Main', indent = 0, content = content)
content = main_block.analyse()
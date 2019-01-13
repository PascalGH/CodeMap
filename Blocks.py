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
        self.code = []
        # print(f'new block: ', name, ',', indent)

    def display(self):
        print(f' ' * self.indent * myindent, self.name)
        for i in self.comments:
            print(f'  ' * self.indent * myindent, mycomment, ' ',i)
        for i in self.code:
            print(f'  ' * self.indent * myindent, ' ',i)
        for i in self.blocks:
            i.display()

    def save(self,file):
        cursor = ' ' * self.indent * myindent
        file.write('--------- Block\n')
        file.write(cursor + self.name + '\n')
        file.write('-------------------\n')
        file.write('--------- Comments\n')
        for i in self.comments:
            file.write(cursor + '# ' + i + '\n')
        file.write('-------------------\n')
        file.write('--------- Code\n')
        for i in self.code:
            file.write(cursor + i + '\n')
        file.write('-------------------\n')
        for i in self.blocks:
            i.save(file)


    def decode(self):
        indent = 0
        while len(self.content) != 0:
            line = self.content.pop(0)
            self.code.append(line)
            sub_line = line.split(mycomment)
            if sub_line[0] != '':
                term = sub_line[0].split()[0].lower()
                for i in myblockkeys:
                    if re.search(i,term):
                        left = list((re.findall(r'\s+', line)))
                        nb_chars = len(left[0])
                        if nb_chars == 1:
                            nb_chars = 0
                        indent = int(nb_chars / myindent)
                        # Here we create a new block below
                        newblock = block(term, indent + 1, self.content)
                        self.blocks.append(newblock)
                        newblock.decode()
                if len(sub_line) > 1:
                    self.comments.append(sub_line[1])
            else:
                if len(sub_line) > 1:
                    self.comments.append(sub_line[1])
        return self.content

f = open("Analyser.py","r")
content = f.read().split(myeol)
f.close()
main_block = block(name = 'Main', indent = 0, content = content)
content = main_block.decode()
#main_block.display()
f = open("Analyser.txt","w")
main_block.save(f)
f.close()
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
        # Need to add a field to store pure instructions

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
            #self.code.append(line)
            """ Splitting the line to determine if there is a comment (using the character defined as comment indicator)
                4 options are possible:
                    Option 1 - We have an empty line, we will ignore it.
                    Option 2 - We have a comment only in the line and no instruction.
                    Option 3 - We have an instruction only in the line is no comment.
                    Option 4 - We have a comment in the second part of the line. """
            sub_line = line.split(mycomment)
            if sub_line[0] != '':      # Option 3 or option 4
                term = sub_line[0].split()[0].lower() # Extracting the first word of the line
                for i in myblockkeys:
                    if re.search(i,term): # Match found, we will create a new block
                        left = list((re.findall(r'\s+', line)))  # Looking for the initial spaces
                        nb_chars = len(left[0]) # Number of spaces
                        if nb_chars == 1:
                            nb_chars = 0
                        indent = int(nb_chars / myindent) # ICalculation of indentation based on the size of an indent
                        newblock = block(term, indent + 1, self.content) # We create a new block, indentation increased
                        self.blocks.append(newblock) # Add the block to the lists of inner ones
                        newblock.code.append(line) # Adding the line that triggers the block creation
                        if len(sub_line) > 1:  # Option 2
                            newblock.comments.append(sub_line[1])
                        self.content = newblock.decode()
                        return self.content
                self.code.append(line)
                if len(sub_line) > 1:  # Option 2 (option 1 is just ignored)
                    self.comments.append(sub_line[1]) # We add the line to the comments of the current block
            else:                      # Option 1 or 2
                if len(sub_line) > 1:  # Option 2 (option 1 is just ignored)
                    self.comments.append(sub_line[1]) # We add the line to the comments of the current block
                    self.code.append(line) # We add the line to the code of the current block
        return self.content # Return the remainder of the content to potentially be analysed in block(s) above

f = open("Analyser.py","r")
content = f.read().split(myeol)
f.close()
main_block = block(name = 'Main', indent = 0, content = content)
content = main_block.decode()
#main_block.display()
f = open("Analyser.txt","w")
main_block.save(f)
f.close()
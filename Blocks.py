# This is the main file to experiment code analysis

# Import of external files and modules
import Keywords_Map # Own module where keywords are associated with fonctions to perform
import re # Regular expressions

myblock = Keywords_Map.block_indicators
myblockkeys = myblock.keys()
mycomment = Keywords_Map.comment_indicator
myeol = Keywords_Map.eol_indicator
myindent = Keywords_Map.indent_length


def get_indent(chain):
    if len(chain) == 0:
        return 0
    left = list((re.findall(r'\s+', chain)))  # Looking for the initial spaces
    if len(left) == 0:
        return 0
    nb_chars = len(left[0])  # Number of spaces
    if nb_chars == 1:
        nb_chars = 0
    return int(nb_chars / myindent)  # Calculation of indentation based on the size of an indent


class Block:
    def __init__(self, name, indent, content, line):
        self.name = name
        self.indent = indent
        self.content = content
        self.blocks = []
        self.comments = []
        self.code = []
        self.instructions = []

        sub_line = line.split(mycomment)
        self.code.append(line)
        self.instructions.append(sub_line[0])
        if len(sub_line) > 1:
            self.comments.append(sub_line[1])


    def display(self):
        print(' ' * self.indent * myindent + self.name)
        for i in self.comments:
            print('  ' * self.indent * myindent + mycomment + ' ' +i)
        for i in self.code:
            print('  ' * self.indent * myindent + ' ' +i)
        for i in self.blocks:
            i.display()

    def save(self,file):
        cursor = ' ' * self.indent * myindent
        if self.name == 'Line':
            file.write(cursor + self.code[0] + '\n')
        else:
            file.write(cursor + self.name + '\n')
        """for i in self.comments:
            file.write(cursor + '# ' + i + '\n')
        if len(self.comments) > 0:
            file.write('\n' * 2)
        for i in self.instructions:
            file.write('I: ' + cursor + i + '\n')
        if len(self.instructions) > 0:
            file.write('\n' * 2)
        
        for i in self.code:
            # file.write('C: ' + cursor + i + '\n')
            file.write(cursor + i + '\n')
        if len(self.code) > 0:
            file.write('\n' * 2)
        """
        for i in self.blocks:
            i.save(file)

    def blockify(self):
        while len(self.content) != 0:
            line = self.content[0]
            """ Splitting the line to determine if there is a comment (using the character defined as comment indicator)
                4 options are possible:
                    Option 1 - We have an empty line, we will just add it.
                    Option 2 - We have a comment only in the line and no instruction.
                    Option 3 - We have an instruction only in the line is no comment.
                    Option 4 - We have an instruction and a comment in the second part of the line.
            """
            match_block = 0
            sub_line = line.split(mycomment)
            if len(re.findall(r'\S+', sub_line[0])) != 0:      # Option 3 or option 4
                indent = get_indent(line)
                if indent < self.indent:
                    return self.content
                line = self.content.pop(0)
                term = sub_line[0].split()[0].lower() # Extracting the first word of the line
                for i in myblockkeys: # Looking for match in the block definition terms
                    if re.search(i,term): # Match found, we will create a new block
                        new_block = Block('Line', self.indent, line, line)
                        self.blocks.append(new_block)
                        new_block = Block(term, self.indent + 1, self.content, line) # We create a new block, indentation increased
                        self.blocks.append(new_block) # Add the block to the lists of inner ones
                        self.content = new_block.blockify()
                        break
                # Need to find a way to no create the block after when exiting from blockify method
                new_block = Block('Line', self.indent, line, line)  # We create a new block, same indentation
                self.blocks.append(new_block)  # Add the block to the lists of inner ones
            else: # Option 1 or 2, we create a new line block
                line = self.content.pop(0)
                new_block = Block('Line', self.indent, line, line)  # We create a new block, indentation increased
                self.blocks.append(new_block)  # Add the block to the lists of inner ones
        return self.content # Return the remainder of the content to potentially be analysed in block(s) above

file_in = open("Test.py","r")
content = file_in.read().split(myeol)
file_in.close()
main_block = Block(name = 'Main', indent = 0, content = content, line = '')
content = main_block.blockify()
file_out = open("Test.txt","w")
main_block.save(file_out)
file_out.close()
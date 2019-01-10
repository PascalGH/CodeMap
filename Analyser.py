# This is the main file to experiment code analysis

# Import of external files and modules
import Keywords_Map # Own module where keywords are associated with fonctions to perform
import re # Regular expressions

mymap = Keywords_Map.keywords_map
mykeys = (Keywords_Map.keywords)
mycomment = Keywords_Map.comment_indicator
myeol = Keywords_Map.eol_indicator


f = open("Analyser.py","r")
content = f.read().split(myeol)

for line in content: #First loop
    sub_line = line.split(mycomment)
    if sub_line[0] != '':  #             First if
        term = sub_line[0].split()[0].lower()
        for i in mykeys:
            if re.search(i,term): # Here we can count the number of spaces or tabs upfront to determine the indentation for Python
                mymap[i]()
                break
        if len(sub_line) > 1:
            print(f'Comment: ',sub_line[1])
    else:
        if len(sub_line) > 1:
            print(f'Comment: ',sub_line[1])
f.close()

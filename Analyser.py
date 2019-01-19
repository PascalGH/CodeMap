# First full line comment of the file

# Second comment of the file
import re # First instruction in block main

print('fgb') # First instruction in main block
print('fghfgh') # Second instruction in the main block
print('dfgdfg') # Now going to the for block, indent 1

for line in content: # First for loop, indent 1

    print('xxxxx') # First instruction in for block, indent 1

    if sub_line[0] != '':  #             First if, indent 2
        term = sub_line[0].split()[0].lower()
        # Now going for the for, indent 3
        for i in mykeys:
            # Going for the for the if block, indent 4
            if re.search(i,term): # Here we can count the number of spaces or tabs upfront to determine the indentation for Python
                left = list((re.findall(r'\s+', line)))
                nbchars = len(left[0])
                mymap[i](nbchars)
                break
            # End of  the if block indent 4
            # Back to block for, indent 3
            print('gototot')
            print('tutu')
        # End of block for, indent 3
        # Back to block if, indent 2
        print('titi')
        # New block if, indent 3
        if len(sub_line) > 1:
            print(f'Comment: ',sub_line[1])
            # End of block if, indent 3
        print('tata')
        # End of block if, indent 2
    # New block else, indent 2
    else:
    # New block if, indent 3
        if len(sub_line) > 1:
            print(f'Comment: ',sub_line[1])
            # End of block if, indent 3
        print('ok')
        # End of block block else, indent 2
    # Back to block for, indent 1
    print('dududud')
    # Back to block main
f.close()
print('ttitit')
print('dsfgdsg')
# End of block main

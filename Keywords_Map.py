comment_indicator = '#'
eol_indicator = '\n'
indent_length = 4
block_indicators = {'for': 'block', 'if': 'block', 'while': 'block', 'else':'block', 'def':'function'}
key_blocks = block_indicators.keys()


def for_fn(nbchars):
    if nbchars == 1:
        indent = 0
    else:
        indent = int(nbchars / indent_length)
    print('for block at indent: ',indent)


def if_fn(nbchars):
    if nbchars == 1:
        indent = 0
    else:
        indent = int(nbchars / indent_length)
    print('if block at indent: ',indent)


def while_fn(nbchars):
    if nbchars == 1:
        indent = 0
    else:
        indent = int(nbchars / indent_length)
    print('while block at indent: ',indent)

# keywords_map = {'for':for_fn,'if':if_fn,'while':while_fn}

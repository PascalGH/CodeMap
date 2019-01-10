comment_indicator = '#'
eol_indicator = '\n'

def for_fn():
    print('for block')

def if_fn():
    print('if block')

def while_fn():
    print('while block')

keywords_map = {'for':for_fn,'if':if_fn,'while':while_fn}
keywords = keywords_map.keys()
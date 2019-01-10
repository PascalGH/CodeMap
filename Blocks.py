class block:
    def __init__(self, name):
        self.name = name
        self.blocks = []

    def addblock(self,newblock):
        self.blocks.append(newblock)

toto = block(name = 'Toto')
titi = block(name = 'titi')

toto.addblock(titi)
print(toto.blocks[0].name)
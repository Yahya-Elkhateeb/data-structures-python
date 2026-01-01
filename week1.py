class plane:
    def __init__(self, id, position):
        self.position=position
        self.id=id

    def begin_fly(self, position):
        self.position = position

    def end_fly(self, position):
        self.position = position
    def go_forward(self,position):
        self.position=position
    def show(self):
        print('plane {}, coordinates on {} now'.format(self.id, self.position))
ucak1=plane('u1',(0,0,0))
siha=plane('s1',(0,0,0))
iha=plane('iha1',(0,0,0))

class filo:
    def __init__(self):
        self.planes = []

    def show(self):
        for i in self.planes:
            print('our filo include {}'.format(i.id))

    def add_filo(self, plane):
        self.planes.append(plane)


filo2 = filo()
filo2.add_filo(iha)
filo2.show()


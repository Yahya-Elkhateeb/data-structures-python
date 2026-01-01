class plane:
    def __init__(self, id, position):
        self.position = position
        self.id = id

    def begin_fly(self, position):
        self.position = position

    def end_fly(self, position):
        self.position = position

    def go_forward(self, position):
        self.position = position

    def show(self):
        print(f'plane {self.id}, coordinates on {self.position} now')


class filo:
    def __init__(self):
        self.planes = []

    def add_filo(self, plane):
        self.planes.append(plane)

    def show(self):
        for p in self.planes:
            print(f'our filo include {p.id}')


ucak1 = plane('u1', (0, 0, 0))
siha = plane('s1', (0, 0, 0))
iha = plane('iha1', (0, 0, 0))

filo2 = filo()
filo2.add_filo(iha)
filo2.show()

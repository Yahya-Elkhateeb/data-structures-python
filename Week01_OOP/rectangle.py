class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        print(2 * (self.length + self.width))

    def calculate_area(self):
        print('rectangle area={}'.format(self.length * self.width))

my_rectangle = rectangle(4, 6)
my_rectangle.calculate_perimeter()
my_rectangle.calculate_area()

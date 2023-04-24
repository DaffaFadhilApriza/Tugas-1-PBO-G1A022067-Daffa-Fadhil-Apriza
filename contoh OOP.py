# membuat kelas
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# membuat objek
rect = Rectangle(3, 4)

# memanggil metode pada objek
print(rect.area())

# Bridge design pattern

# Implementer Interface
class DrawingDevice:
    def draw_circle(self, radius):
        pass

    def draw_square(self, side):
        pass


# Concrete Implementer - Pen
class Pen(DrawingDevice):
    def draw_circle(self, radius):
        print(f'Drawing circle with a pen of radius {radius}')

    def draw_square(self, side):
        print(f'Drawing square with a pen of side {side}')

# Concrete Implementer - Brush
class Brush(DrawingDevice):
    def draw_circle(self, radius):
        print(f'Drawing circle with a brush of radius {radius}')

    def draw_square(self, side):
        print(f'Drawing square with a brush of side {side}')


# Abstraction
class Shape:
    def __init__(self, drawing_device: DrawingDevice):
        self.drawing_device = drawing_device

    def draw(self):
        pass


# Refined Abstraction
class Circle(Shape):
    def __init__(self, drawing_device: DrawingDevice, radius: int):
    # def __init__(self, drawing_device, radius: int):
        super().__init__(drawing_device)
        self.radius = radius

    def draw(self):
        self.drawing_device.draw_circle(self.radius)


# Refined Abstraction
class Square(Shape):
    def __init__(self, drawing_device: DrawingDevice, side: int):
    # def __init__(self, drawing_device, side: int):
        super().__init__(drawing_device)
        self.side = side

    def draw(self):
        self.drawing_device.draw_square(self.side)


# Client
pen = Pen()
brush = Brush()

circle = Circle(pen, 5)
square = Square(brush, 10)

circle.draw()
square.draw()

circle.drawing_device = brush
circle.radius = 12
circle.draw()

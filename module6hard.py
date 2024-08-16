import math
print('\033[30m\033[47mДополнительное практическое задание по модулю*\033[0m')
print('\033[30m\033[47mЗадание "Они все так похожи":\033[0m')
print('\033[30m\033[47mСтудент Крылов Эдуард Васильевич\033[0m')
thanks = '\033[30m\033[47mБлагодарю за внимание :-)\033[0m'
print()


class Figure:
    sides_count = 0

    def __init__(self, color: tuple, *sides: int, filled: bool = True) -> None:
        if len(sides) != self.sides_count:
            self.__sides = [1*self.sides_count]
        else:
            self.__sides = [i for i in sides]
        self.__color = color
        self.filled = filled

    def get_color(self):
        return [i for i in self.__color]

    def __is_valid_color(self, r, g, b):
        color_list = [r, g, b]
        color_list.sort()
        if color_list[0] < 0 or color_list[-1] > 255:
            return False
        else:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, sides):
        sides_list = []
        for i in sides:
            if i > 0:
                sides_list.append(i)
        if len(sides_list) > 0 and len(sides) == len(self.__sides):
            return True
        else:
            return False

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = sides

    def get_sides(self):
        return [*self.__sides]

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1
    __radius = None

    def set_radius(self):
        self.__radius = self.__len__() / (2 * math.pi)
        return self.__radius

    def get_square(self):
        self.set_radius()
        return (self.__radius ** 2) * math.pi


class Triangle(Figure):
    sides_count = 3
    __height = None

    def get_square(self):
        return (self.side ** 2) * (3 ** 0.5) / 4

    def set_height(self):
        self.__height = self.side * (3 ** 0.5) / 2
        return self.__height


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides: int, filled: bool = True):
        super().__init__(color, *sides, filled)
        if len(sides) == 1:
            self.__sides = self.sides_count * [i for i in sides]
        else:
            self.__sides = [1 * self.sides_count]

    def get_sides(self):
        return [*self.__sides]

    def get_volume(self):
        return self.__sides[1] ** 3


# Код для проверки:
# (Цвет, стороны)
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
# Изменится
circle1.set_color(55, 66, 77)
print(f'Проверка на изменение цветов: Изменится - {circle1.get_color()}')
# Не изменится
cube1.set_color(300, 70, 15)
print(f'Проверка на изменение цветов: Не изменится - {cube1.get_color()}')

# Проверка на изменение сторон:
# Не изменится
cube1.set_sides(5, 3, 12, 4, 5)
print(f'Проверка на изменение сторон: Не изменится - {cube1.get_sides()}')
# Изменится
circle1.set_sides(15)
print(f'Проверка на изменение сторон: Изменится - {circle1.get_sides()}')

# Проверка периметра (круга), это и есть длина:
print(f'Проверка периметра (круга), это и есть длина: {len(circle1)}')

# Проверка объёма (куба):
print(f'Проверка объёма (куба): {cube1.get_volume()}')
print()
print(thanks)

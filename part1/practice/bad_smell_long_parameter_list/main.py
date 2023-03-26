# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:

    def __init__(self, state, speed=1):
        self.state = state
        self.speed = speed
        self.new_y = 0
        self.new_x = 0

    def determine_speed(self):
        if self.state == 'fly':
            self.speed *= 1.2
        elif self.state == 'crawl':
            self.speed *= 0.5
        else:
            raise ValueError('нельзя летать и ползать')
        return self.speed

    def move(self, x_coord, y_coord, direction):

        if direction == 'UP':
            self.new_y = y_coord + self.speed
            self.new_x = x_coord
        elif direction == 'DOWN':
            self.new_y = y_coord - self.speed
            self.new_x = x_coord
        elif direction == 'LEFT':
            self.new_y = y_coord
            self.new_x = x_coord - self.speed
        elif direction == 'RIGTH':
            self.new_y = y_coord
            self.new_x = x_coord + self.speed


    def set_field(self, field):
        field.set_unit(x=self.new_x, y=self.new_y, unit=self)

#     ...

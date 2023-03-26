# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов


class Person:
    def __init__(self, room_num, city_popultaion):
        self.room_num = room_num
        self.city_popultaion = city_popultaion

    def get_person_room(self):
        return self.room_num

    def get_city_population(self):
        return self.city_popultaion



person = Person(23, 1102503)

print(person.get_person_room())
print(person.get_city_population())
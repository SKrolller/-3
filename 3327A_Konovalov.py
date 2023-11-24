#1
class Soda:
    def __init__(self, additive=None):
        self.additive = additive

    def show_my_drink(self):
        if self.additive:
            print(f'Газировка и {self.additive}')
        else:
            print('Обычная газировка')
napitok1 = Soda("Ваниль")
napitok1.show_my_drink()
 #Газировка с Ванилью
napitok2 = Soda("")
napitok2.show_my_drink()
 #Обычная газировка

#3
class Nikola:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        if self.name == 'Николай':
            return f'Меня зовут {self.name} и мне {self.age} лет'
        else:
            return f'я не {self.name}. Я Николай'

chell = Nikola('Николай', 66)
print(chell)
#2
class TriangleChecker:
    def __init__(self, a, s, d):
        self.a = a
        self.s = s
        self.d = d

    def is_Triangle(self):
        if not isinstance(self.a, int) or not isinstance(self.s, int) or not isinstance(self.d, int):
            return f'Нужно вводить только числа'
        if self.a <= 0 or self.s <= 0 or self.d <= 0:
            return f'С отрицательными числами ничего не выйдет'

        if self.a + self.s > self.d or self.s + self.d > self.a or self.a + self.d > self.s:
            return f'Ура, можно построить треугольник'
        else:
            return f'Жаль, но из этого треугольник не сделать'

checker1 = TriangleChecker(3, 4, 5)
print(checker1.is_Triangle())
checker2 = TriangleChecker(1, 7, 5, )
print(checker2.is_Triangle())
checker3 = TriangleChecker(-3, 4, 7)
print(checker3.is_Triangle())

#4

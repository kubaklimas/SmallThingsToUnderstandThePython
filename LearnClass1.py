class Emp:

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.pay = pay
        self.email = name + '.' + surname + '@gmail.com'

    def showit(self):
        return '{} {}'.format(self.name, self.surname)

    def giveraise(self):
        self.pay = int(self.pay*1.14)


Employee1 = Emp('Doran', 'Still', 4000)
Employee2 = Emp('Anakin', 'Ergar', 5000)

print(Employee1.pay)
Employee1.giveraise()
print(Employee1.pay)
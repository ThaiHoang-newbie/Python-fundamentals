from datetime import date

class Person():

    def __init__(self, name, year):
        self.name = name
        self.year =  year
    
    def getName(self):
        return self.name

    def calAge(self):
        return date.today().year - self.year
    
    @staticmethod
    def validateYear(year) -> bool:
        return 1000 <= year <= date.today().year

def main():
    name = input("Enter your name: ")
    year = int(input("Enter your year of birth: "))

    while not Person.validateYear(year):
        year = int(input("Are you sure? It's impossible dude. Please enter again: "))

    person = Person(name, year)
    age = person.calAge()
    print(f"{name}: {age} {"year old" if age <= 1 else "years old"}")

if __name__ == "__main__":
    main()
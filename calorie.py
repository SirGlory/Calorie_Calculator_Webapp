from temperature import Temperature

class Calorie:

    def __init__(self, age, weight, height, temperature):
        self.age = age
        self.height = height
        self.weight = weight
        self.temperature = temperature

    def calculate(self):
        result = 10*self.weight + 6.5*self.height + 5 - self.temperature*18
        return result

if __name__ == "__main__":
    temperature = Temperature(country="Italy", city="Rome").get()
    calorie = Calorie(weight=80, height=185, age=25, temperature=temperature)
    print(f"{calorie.calculate()} kcal")




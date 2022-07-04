# Crie uma classe de sua preferência com, no mínimo, uma variável, um método e um incremento. Depois, desenvolva três ou
# mais objetos para testar o código.

class Person:
    def __init__(self, name, yo, gender):
        self.name = name
        self.yo = yo
        self.gender = gender

    def do(self, verb):
        print(f"{self.name} est� a fazer {verb}.")

    def eat(self, food):
        print(f"{self.name} est� comendo {food}.")

    def speak(self, topic):
        print(f"{self.name} est� falando sobre {topic}")

    def specifications(self):
        print(f"{self.name} possui {self.yo} e � {self.gender}.")


pessoa1 = Person("Heitor Danilo Silva Barros", "18", "homem")
pessoa1.speak("programaç�o")

print("")

pessoa2 = Person("Eduarda Fortaleza", "19", "mulher")
pessoa2.eat("lasanha")

print("")

pessoa3 = Person("Kelvin Santos", "17", "homem")
pessoa3.speak("biologia")

print("")

pessoa1.specifications()
pessoa2.specifications()
pessoa3.specifications()

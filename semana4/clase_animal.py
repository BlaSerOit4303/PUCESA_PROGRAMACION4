class Animal:
    def hablar(self):
        return "El animal hace un sonido"

class Perro(Animal):
    def hablar(self):
        return "El perro ladra"
    
class Gato(Animal):
    def hablar(self):
        return "El gato maulla"
    
animales = [Perro(), Gato(), Animal()]
for animal in animales:
    print(animal.hablar())
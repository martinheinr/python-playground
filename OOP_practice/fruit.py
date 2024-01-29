class Apple:
    def __init__(self):
        self.color = "yellow"
        self.flavor = "sweet"

honeycrisp = Apple()
honeycrisp.color = "Green"
pink_lady = Apple()
pink_lady.color = "Red"
print("Apple color is " + honeycrisp.color)
print("Apple color is " + pink_lady.color)


class Peach:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    
    def __str__(self) -> str:
        return "Peach which is {} and {}".format(self.color, self.flavor)

honeycrisp = Peach("red", "sweet")
fuji = Peach("yellow", "tart")

print(honeycrisp.flavor)
print(fuji.flavor)

print(honeycrisp)
print(fuji)
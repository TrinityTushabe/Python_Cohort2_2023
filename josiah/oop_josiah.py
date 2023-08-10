# creating a phone class where the brand name, model storage and price will be displayed
class Phones:
    brand = "Apple"
    model = "iPhone 12"
    storage = "256GB"
    price = "4,000,000 UGX"

print(f"Phone 1: {Phones.brand} {Phones.model} - Storage: {Phones.storage}, Price: {Phones.price}")

phone2 = Phones()
phone2.brand = "Samsung"
phone2.model = "Galaxy S21"
phone2.storage = "128GB"
phone2.price = "3,500,000 UGX"

print(f"Phone 2: {phone2.brand} {phone2.model} - Storage: {phone2.storage}, Price: {phone2.price}")

phone3 = Phones()
phone3.brand = "Google"
phone3.model = "Pixel 5"
phone3.storage = "128GB"
phone3.price = "2,500,000 UGX"

print(f"Phone 3: {phone3.brand} {phone3.model} - Storage: {phone3.storage}, Price: {phone3.price}")

phone4 = Phones()
phone4.brand = "OnePlus"
phone4.model = "9 Pro"
phone4.storage = "256GB"
phone4.price = "3,500,000 UGX"

print(f"Phone 4: {phone4.brand} {phone4.model} - Storage: {phone4.storage}, Price: {phone4.price}")

phone5 = Phones()
phone5.brand = "Xiaomi"
phone5.model = "Mi 11"
phone5.storage = "128GB"
phone5.price = "2,900,000 UGX"

print(f"Phone 5: {phone5.brand} {phone5.model} - Storage: {phone5.storage}, Price: {phone5.price}")

# a class for ugandan shopping mall
class ShoppingMall:
    name = "Acacia Mall"
    location = "Kampala"

print(f"I love shopping at {ShoppingMall.name} in {ShoppingMall.location}.")

mall2 = ShoppingMall()
mall2.name = "Garden City Mall"
mall2.location = "Kampala"

print(f"I love shopping at {mall2.name} in {mall2.location}.")

mall3 = ShoppingMall()
mall3.name = "Oasis Mall"
mall3.location = "Kampala"

print(f"I love shopping at {mall3.name} in {mall3.location}.")

mall4 = ShoppingMall()
mall4.name = "Victoria Mall"
mall4.location = "Entebbe"

print(f"I love shopping at {mall4.name} in {mall4.location}.")

mall5 = ShoppingMall()
mall5.name = "Forest Mall"
mall5.location = "Kampala"

print(f"I love shopping at {mall5.name} in {mall5.location}.")




# printing out  a patriotic message
class Africa:
    name = "Nigeria"

country1 = Africa()
print(f"I love my homeland {country1.name}.")


country2 = Africa()
country2.name = "Kenya"
print(f"I love my homeland {country2.name}.")

country3 = Africa()
country3.name = "South Africa"
print(f"I love my homeland {country3.name}.")

country4 = Africa()
country4.name = "Egypt"
print(f"I love my homeland {country4.name}.")

country5 = Africa()
country5.name = "Ghana"
print(f"I love my homeland {country5.name}.")

# creating a class for wild animals and national game parks in Ug
class Wildlife:
    pass

animal1 = Wildlife()
animal1.name = "Lion"
animal1.game_park = "Queen Elizabeth National Park"
print(f"I love seeing {animal1.name}s in {animal1.game_park}.")

animal2 = Wildlife()
animal2.name = "Giraffe"
animal2.game_park = "Murchison Falls National Park"
print(f"I love seeing {animal2.name}s in {animal2.game_park}.")

animal3 = Wildlife()
animal3.name = "Elephant"
animal3.game_park = "Kidepo Valley National Park"
print(f"I love seeing {animal3.name}s in {animal3.game_park}.")

animal4 = Wildlife()
animal4.name = "Zebra"
animal4.game_park = "Lake Mburo National Park"
print(f"I love seeing {animal4.name}s in {animal4.game_park}.")

animal5 = Wildlife()
animal5.name = "Rhino"
animal5.game_park = "Ziwa Rhino Sanctuary"
print(f"I love seeing {animal5.name}s in {animal5.game_park}.")


# laptop brands here
class laptop:
    brand = "Apple"
    model = "Macbook pro"
    display = "15 inch"
    storage = 256
print(f"I use only {laptop.name} branded laptop a {laptop.model} with a {laptop.storage} capacity")

laptop2 = laptop()
laptop2.brand = "Dell"
laptop2.model = "XPS 13"
laptop2.display = "13 inch"
laptop2.storage = 512

print(f"I use only {laptop2.brand} branded laptop, a {laptop2.model} with a {laptop2.storage}GB storage capacity.")

laptop3 = laptop()
laptop3.brand = "HP"
laptop3.model = "ENVY x360"
laptop3.display = "15.6 inch"
laptop3.storage = 1

print(f"I use only {laptop3.brand} branded laptop, a {laptop3.model} with a {laptop3.storage}TB storage capacity.")

laptop4 = laptop()
laptop4.brand = "Lenovo"
laptop4.model = "ThinkPad X1 Carbon"
laptop4.display = "14 inch"
laptop4.storage = 512

print(f"I use only {laptop4.brand} branded laptop, a {laptop4.model} with a {laptop4.storage}GB storage capacity.")

laptop5 = laptop()
laptop5.brand = "Asus"
laptop5.model = "ZenBook 14"
laptop5.display = "14 inch"
laptop5.storage = 256

print(f"I use only {laptop5.brand} branded laptop, a {laptop5.model} with a {laptop5.storage}GB storage capacity.")

# earbuds sales in uganda
class EarBuds:
    pass

# Creating instances of the EarBuds class
earbuds1 = EarBuds()
earbuds1.brand = "Apple"
earbuds1.model = "AirPods Pro"
earbuds1.price = 249000

earbuds2 = EarBuds()
earbuds2.brand = "Sony"
earbuds2.model = "WF-1000XM4"
earbuds2.price = 279000

earbuds3 = EarBuds()
earbuds3.brand = "Jabra"
earbuds3.model = "Elite 75t"
earbuds3.price = 179000

earbuds4 = EarBuds()
earbuds4.brand = "Samsung"
earbuds4.model = "Galaxy Buds Pro"
earbuds4.price = 199000

earbuds5 = EarBuds()
earbuds5.brand = "Bose"
earbuds5.model = "QuietComfort Earbuds"
earbuds5.price = 279000

# Printing information about each pair of earbuds
print(f"Earbuds 1: {earbuds1.brand} {earbuds1.model} - Price: UGX{earbuds1.price}")
print(f"Earbuds 2: {earbuds2.brand} {earbuds2.model} - Price: UGX{earbuds2.price}")
print(f"Earbuds 3: {earbuds3.brand} {earbuds3.model} - Price: UGX{earbuds3.price}")
print(f"Earbuds 4: {earbuds4.brand} {earbuds4.model} - Price: UGX{earbuds4.price}")
print(f"Earbuds 5: {earbuds5.brand} {earbuds5.model} - Price: UGX{earbuds5.price}")

# screen types in uganda
class ScreenTypes:
    pass

# Creating instances of the ScreenTypes class
screen1 = ScreenTypes()
screen1.type = "LCD"
screen1.size = "27 inches"
screen1.resolution = "1920x1080"

screen2 = ScreenTypes()
screen2.type = "LED"
screen2.size = "32 inches"
screen2.resolution = "3840x2160"

screen3 = ScreenTypes()
screen3.type = "OLED"
screen3.size = "55 inches"
screen3.resolution = "3840x2160"

screen4 = ScreenTypes()
screen4.type = "QLED"
screen4.size = "65 inches"
screen4.resolution = "3840x2160"

screen5 = ScreenTypes()
screen5.type = "IPS"
screen5.size = "24 inches"
screen5.resolution = "2560x1440"


# creating an object for cars
class Cars:
    name = "Toyota Corolla"
    model = "Sedan"
    color = "Silver"

print(f"I would love to drive the {Cars.name} in the future.")

car2 = Cars()
car2.name = "Honda CR-V"
car2.model = "SUV"
car2.color = "Blue"
print(f"I would love to drive the {car2.name} in the future.")

car3 = Cars()
car3.name = "Volkswagen Golf"
car3.model = "Hatchback"
car3.color = "Red"
print(f"I would love to drive the {car3.name} in the future.")

car4 = Cars()
car4.name = "Subaru Forester"
car4.model = "SUV"
car4.color = "Black"
print(f"I would love to drive the {car4.name} in the future.")

car5 = Cars()
car5.name = "Mercedes-Benz C-Class"
car5.model = "Sedan"
car5.color = "White"
print(f"I would love to drive the {car5.name} in the future.")



# Printing information about each screen type
print(f"Screen 1: Type - {screen1.type}, Size - {screen1.size}, Resolution - {screen1.resolution}")
print(f"Screen 2: Type - {screen2.type}, Size - {screen2.size}, Resolution - {screen2.resolution}")
print(f"Screen 3: Type - {screen3.type}, Size - {screen3.size}, Resolution - {screen3.resolution}")
print(f"Screen 4: Type - {screen4.type}, Size - {screen4.size}, Resolution - {screen4.resolution}")
print(f"Screen 5: Type - {screen5.type}, Size - {screen5.size}, Resolution - {screen5.resolution}")

# creating a objects for programing languages

class Languages:
    pass

language1 = Languages()
language1.name = "Python"
print(f"I am studying {language1.name} right now. Hello, World!")

language2 = Languages()
language2.name = "JavaScript"
print(f"I am studying {language2.name} right now. Hello, World!")

language3 = Languages()
language3.name = "Java"
print(f"I am studying {language3.name} right now. Hello, World!")

language4 = Languages()
language4.name = "C++"
print(f"I am studying {language4.name} right now. Hello, World!")

language5 = Languages()
language5.name = "Ruby"
print(f"I am studying {language5.name} right now. Hello, World!")

'''
10 classes and 5 objects
'''
class Book:
    name = "picfare"
    cover = "smooth"
    size = "small"
    color = "white"
    pages = "194"
    weight = "1kg"
print(Book.name)
print(f"{Book.name}) is (Book.color) is (Book.size) is nice")

book2 = Book()
name = "graph"
cover = "light"
size = "medium"
pages = "94"
weight = "ahalfkg"
use = "writing"
print(book2.name)
print(f"{book2.name}) is (book2.size) is (book2.weight) is nice for drawing")

book3 = Book()
name = "note_book"
color = "white"
size = "small"
weight = "0.1kg"
cover = "soft"
use = "drawing"
print(book3.name)
print(f"{book3.name}) is (book3.color) is (book.size) it is nice")

book4 = Book()
name = "text_book"
color ="white"
size = "large"
weight = "3kg"
cover = "hard"
use = "keeping_notes"
print(book4.name)
print(f"{book4.name}) is (book4.use) is (book4.cover) it stores notes safely")

book5 = Book()
name = "magazine"
color = "yellow"
size = "medium"
cover = "soft"
use = "advertisement"
weight = "light"
print(book5.name)
print(f"{book5.name}) is (book.color) is(book.size) it gives detailed information")

class Shoe:
    name = "snickers"
    size = "30cm"
    color = "black"
    quality = "new bland"
    durability = "1 year"
    price = "20000"
print(Shoe.name)
print(f"{Shoe.name}) is (Shoe.size) is (Shoe.price) in quality")

shoe2 = Shoe()
name = "sandles"
color = "green"
quality = "second_hand"
price = "5000sh"
durability = "2week"
size = "5"
print(shoe2.name)
print(f"{shoe2.name}) is (shoe2.quality) is (shoe2.price) is easy to put on")

shoe3 = Shoe()
name = "leather"
color = "black"
price = "20000"
durability = "5years"
size = "8cm"
print(shoe3.name)
print(f"{shoe3.name}) is (shoe3.color) is (shoe3.durability) is (shoe3.size) it is good for students")

shoe4 = Shoe()
name = "push_in"
color = "blue"
price = "80000sh"
durability = "month"
size = "29cm"
type = "plastic"
print(shoe4.name)
print(f"{shoe4.name}) is (shoe.color) is (shoe.type) it suits every where")


shoe5 = Shoe()
name = "gum_boot"
color = "black"
durability = "10yrs"
size = "8cm"
type = "silk"
price = "15000sh"
print(shoe5.name)
print(f"{shoe5.name}) is (shoe5.type) is (shoe5.durability) is better in dry season")


class Phone:
    name = "Aitel"
    color = "black"
    size = "medium"
    price = "2000sh"
    battery_size = "large"
    data_storage = "2gb"
print(Phone.name)
print(f"{Phone.name}) is (phone.color) is (phone.size) lasts longer")

phone2 = Phone()
name = "tecno"
color = "black"
price = "500000"
battery_size = "extra large"
data_storage = "5gb"
size = "large"
print(phone2.name)
print(f"{phone2.name}) is (phone2.name) is (phone2.price) is affordable")


phone3 = Phone()
name = "oppo"
price = "200000sh"
battery_size = "5gb"
size = "medium"
data_storage = "large"
color = "dark_white"
weight = "light"
print(phone3.name)
print(f"{phone3.name}) is (phone3.price) is (phone3.weight) it is cheap")

phone4 = Phone()
name =  "fire_phone"
price = "500000sh"
weight = "heavy"
size = "large"
color = "black"
battery_size= "large"
print(phone4.name)
print(f"{phone4.name}) is (phone4.price) is (phne4.weight) stores full data")

phone5 = Phone()
name =  "infinix"
price = "900000sh"
weight = "heavy"
size = "large"
color = "black"
battery_size= "large"
print(phone5.name)
print(f"{phone5.name}) is (phone5.price) is (phne5.weight) consumes much power")


phone5 = Phone()
name = "sumsang"
price = "6000000"
color = "pale blue"
battery_size= "medium"
size = "large"
data_storage = "10gb"
print(phone5.name)
print(f"{phone5.name}) is (phone5.price) is (phone5.data_storage) it keeps power for so long")



class Fruit:
    name = "mango"
    size = "large"
    color = "yellow"
    growth_period = "3"
    price = 1000
    harveting_stage = "old"
print(Fruit.name)
print(f"{Fruit.name}) is (Fruit.color) is (Fruit.size)it is a sweat fruit")

fruit2 = Fruit()
name = "orange"
size = "small"
color = "green"
growth_period = "a month"
harvesting_stage = "flowering"
print(fruit2.name)
print(f"{fruit2.name}) is (fruit2.color) is (fruit2.harvesting_period) it makes good juice")

fruit3 = Fruit()
name = "passipon_fruit"
size = "medium"
color = "green"
growth_period = "5 months"
harvesting_stage = "rippening"
print(fruit3.name)
print(f"{fruit3.name}) is (fruit3.color) is (fruit3.harvesting_period) it makes people health")


fruit4 = Fruit()
name = "jack_fruit"
size = "large"
color = "green"
growth_period = "10 years"
harvesting_stage = "rippening"
print(fruit4.name)
print(f"{fruit4.name}) is (fruit4.color) is (fruit4.harvesting_period) is sweat")

fruit5 = Fruit()
name = "banana"
size = "madium"
color = "yellow"
growth_period = "1year"
harvesting_stage = "rippening"
print(fruit5.name)
print(f"{fruit5.name}) is (fruit4.color) is (fruit4.harvesting_period) it has noseeds")

class Utensil:
        name = "plate"
        size = "small"
        color = "red"
        type = "brokable"
        weight = "2kgs"
        price = "100000"
        shape = "oval"
print(Utensil.name)
print(f"{Utensil.name}) is (Utensil.price) is (Utensil.size) it is cheap")

utensil2 = Utensil()
name = "cup"
size = "large"
shape = "v_shaped"
color = "green"
type = "glass"
weight = "2kg"
print(utensil2.name)
print(f"{utensil2.name}) is (utensil2.type) is (utensil2.size) it is transparent")

utensil3 = Utensil()
name = "spoon"
shape  = "spade_shaped"
color = "dark"
type = "metallic"
weight = "heavy"
size = "thin"
print(utensil3.name)
print(f"{utensil3.name}) is (utensil.shape) is (utensil.type) is used for eating")


utensil4 = Utensil()
name = "knife"
color = "black"
shape = "panga_shaped"
type = "metallic"
weight = "light"
size = "thin"
print(utensil4.name)
print(f"{utensil4.name}) is (utensil.shape) is (utensil.size) is sharp")

utensil5 = Utensil()
name = "sauce_pan"
shape = "oval_shaped"
weight = "heavy"
type = "metallic"
size = "large"
color = "dark"
print(utensil5.name)
print(f"{utensil5.name})  is (utensil5.shape)is (utensil5.color) is used for cooking")

class Bag:
     name = "laptop"
     size = "large"
     color = "black"
     storage_size = "extra_large"
     quality = "durable"
     weight = "light"
print(Bag.name)
print(f"{Bag.name}) is (Bag2.size) is (Bag2.color) it is nice for school children")

bag2 = Bag()
name = "hand bag"
size ="very_small"
storage_size = "small"
quality = "durable"
weight = "lighter"
print(bag2.name)
print(f"{bag2.name}) is (bag2.size) is (bag2.weight) it is flexible")

bag3 = Bag()
name = "suit_case"
size = "large"
weight = "heavy"
quality = "shot_lasting"
type = "woolen"
price = "300000"
print (bag3.name)
print(f"{bag3.name}) is (bag3.type) is (bag.quality) best for highier students")


bag4 = Bag()
name = "metallic_cases"
size = "large"
weight = "heavy"
type = "metallic"
price = "600000sh"
quality = "long_lasting"
print (bag4.name)
print(f"{bag4.name}) is (bag4.size) is (bag.quality)is for primary students")



class Priest:
     name = "John"
     gender = "male"
     status = "married"
     age = "70"
     size = "small"
     height = "tall"
print(Priest.name)
print(f"{Priest.name}) is (Priest.gender) is (Priest.size) he is humble")

Priest2 =Priest()
name = "Anthony"
gender = "male"
status = "single"
size = "fat"
age = "23"
height = "short"
print(Priest2.name)
print(f"{Priest2.name}) is (Priest2.gender)is (Priest2.status) he is proud")


priest3 = Priest()
gender = "female"
status = "single"
size = "thin"
age = "45"
height = "medium"
color = "brown"
print(priest3.name)
print(f"{priest3.name}) is (priest3.size) is (priest3.age) is co_operative")


priest4 = Priest()
gender = "male"
age = "46"
status = "married"
size = "fat"
height = "tall"
color  = "black"
print(priest4.name)
print(f"{priest4.name}) (priest4.gender) is ( priest4.height)  is kind")

priest5 = Priest()
gender = "male"
age = "60"
status = "married"
size = "fat"
height = "short"
color  = "black"
print(priest4.name)
print(f"{priest5.name}) (priest5.gender) is ( priest5.height)  is respectful")



class Cloth:
     name = "sweater"
     price = "3000sh"
     color = "white"
     type = "woolen"
     size = "large"
     quality = "washable"
print(Cloth.name)
print(f"{Cloth.name}) is (Cloth.type) is (Cloth.color) is shinny")

cloth2 =Cloth() 
name = "gomess"
price = "5000sh"
color = "white"
type = "woolen"
size = "large"
quality = "washable"
print(cloth2.name)
print(f"{cloth2.name}) is (cloth.type) is (cloth.color) is warm")

cloth3 =Cloth() 
name = "skirt"
price = "1000sh"
color = "white"
type = "wooven"
size = "small"
quality = "hard"
print(cloth3.name)
print(f"{cloth3.name}) is (cloth3.type) is (cloth3.color) is tight")


cloth4 =Cloth() 
name = "t_shirt"
price = "4000sh"
color = "white"
type = "skinny"
size = "medium"
quality = "soft"
print(cloth4.name)
print(f"{cloth4.name}) is (cloth4.type) is (cloth.color) is good for workers")


cloth5 =Cloth() 
name = "trouser"
price = "3000000sh"
color = "blue"
type = "silket"
size = "extra_large"
quality = "soft"
print(cloth5.name)
print(f"{cloth5.name}) is (cloth5.type) is (cloth5.color) is good for fat men")


class District:
     name = "kisoro"
     location = "south_western"
     country = "uganda"
     language = "kifumbira"
     tribe = "Bafumbira"
     town = "kisoro"
print(District.name)
print(f"{District.name}) is (District.location) is in (country.name) at the boarder")


district2 = District()
name = "wakiso"
location = "central"
country = "uganda"
language = "luganda"
tribe = "basoga"
town = "wakiso"
print(district2.name)
print(f"{district2.name}) is (district2.location) is in (district2.name) is city")

district3 = District()
name = "amuru"
location ="northern"
country = "uganda"
language = "langi"
tribe = "langi"
town = "lira"
print(district3.name)
print(f"{district3.name}) is (district3.location) is in (district3.name) has good climate")



district4 = District()
name = "kasese"
location ="western"
country = "uganda"
language = "lukonjo"
tribe = "bakonjo"
town = "kasese"
print(district4.name)
print(f"{district4.name}) is (district4.location) is in (district4.name) affected by wars")

district5 = District()
name = "jinja"
location ="central"
country = "uganda"
language = "lusoga"
tribe = "basoga"
town = "jinja"
print(district5.name)
print(f"{district5.name}) is (district5.location) is in (district5.name) is undeveloped")

class School:
     name = "muko high school"
     status = "single"
     fee_structure = "7000000sh"
     level_of_edu = "a'level"
     num_of_teacher = 2
     location = "kampala"
print(School.name)
print(f"{School.name}) is (School.status) is (School.location) it is a city school")

School2 = School()
name = "ntinda"
status = "mixt"
fee_structure = "2000sh"
level_of_edu = "primary"
num_of_teacher = "12"
location = "kanungu"
print(School2.name)
print(f"{School2.name}) is (School2.name) is (School2.level_of_edu) is a day and boarding primary school")

school3 = School()
name = "lwengo "
status = "single"
fee_structure = "6000sh"
level_of_edu = "primary"
num_of_teacher = "10"
location = "lwengo district"
print(school3.name)
print(f"{school3.name}) is (School3.name) is (School3.level_of_edu) is for only girls under 12years")
     


school4 = School()
name = "butobere "
status = "single"
fee_structure = "34000sh"
level_of_edu = "secondary"
num_of_teacher = "45"
location = "kabale"
print(school4.name)
print(f"{school4.name}) is (School4.name) is (School4.level_of_edu) is for boys")


school5 = School()
name = "mengo junor"
status = "mixt"
fee_structure = "66668000sh"
level_of_edu = "secondary"
num_of_teacher = "67"
location = "central"
print(school5.name)
print(f"{school5.name}) is (School5.name) is (School5.level_of_edu) is catholic founded")
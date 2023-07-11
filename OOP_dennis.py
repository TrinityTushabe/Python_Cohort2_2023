'''
Assignment on OOP
'''


class Console:
    playstation = 'PS5'
    realized = 2021
    games = 'God Of War'
    version = 'Diskless'
print(Console.games)


class Watch:
    brand = 'Patek Phillipe'
    price = 700000
    make = 'America'
    
watch2 = Watch() 
watch2.brand = 'Hublot'
watch2.price = 650000
watch2.make = 'America'

watch3 = Watch()
watch3.brand = 'Reymond Wil' 
watch3.price = 30000
watch3.make = 'Britian'
print(f"{watch3.brand} is made in {watch3.make}")


class Perfume:
    manufactuer = "Tom Ford"
    amount = 500000
    scent = 'woody'
    halflife = '6 hours'    
print(Perfume.manufactuer)


class Phone: 
    model = 'Google pixel 7'
    price = 750000
    year = 2022
    software = 'android'
print(Phone.model)


class Footballer:
    name = 'halaand'
    club = 'Manchester City'
    goals = 50
    trophys = 3
    country = 'Norway'
    
footballer2 = Footballer()
footballer2.name = 'CR7'
footballer2.club = 'Manchester United'
footballer2.country = 'Portugal'
footballer2.trophys = 50
footballer2.goals = 750 
print(f"{footballer2.name} has scored {footballer2.goals} ")


class Restuarant:
    name = 'The Aleph'
    location = 'Kamwokya'
    dish = 'Burger'
    price = 30000
    drink = 'water'
print(Restuarant.dish)


class Musician:
    artist = 'Kanye West'
    song = 'Through the wire'
    accolades = 3
    year = 2004
    album = 'My twisted Dark Fantasy'

musician2 = Musician() 
musician2.artist = 'Kendrick'
musician2.song = 'DNA'
musician2.accolades = 20
musician2.year = 2016
musician2.album = 'DAMN'
print(f"{musician2.artist} has {musician2.accolades} accolades ")


class Hotel:
    name = 'Serena'
    location = 'Kampala'
    price = 800
    pool = 'Yes'
print(Hotel.name)


class Formula1:
    name = 'Lewis Hamilton'
    team = 'Mercedes'
    races = 800
    championships = 7
    poles = 350
    
racer2 = Formula1()
racer2.name = 'Max Versterppen'
racer2.team = 'Red bull'
racer2.races = 400
racer2.championships = 2
racer2.poles = 50
print (f"{Formula1.name} has won {Formula1.championships} champions")
    
    
class Shoe:
    brand = 'Jordans'
    maker = 'Nike'
    color = 'black'
    price = 500
    size  = 12
print(Shoe.brand)


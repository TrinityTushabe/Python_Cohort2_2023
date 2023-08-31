#class 1
# create class
class Pictures:
    # define an attribute
    subject = "Family"
    location = ''
    name = ''
    time_taken = ''
    place_taken = ''
#accessing attributes via class
print(Pictures.subject)
    
picture1 = Pictures()           # creating object
picture1.name = "Sorce"         # assigning values to attribute
picture2 = Pictures()
picture2.location = "sitting room"
picture3 = Pictures()
picture3.place_taken = "ftown"
picture4 = Pictures()
picture4.name = "TnT 4"
picture5 = Pictures()
picture5.subject = "The  Smiling Angel"
print(f"The {picture1.name} then the {picture4.name}")  #accessing attributes using two objects

#class 2
# create class
class HouseRepair:
    # define an attribute
    where = ''
    duration = 'Two months'
    repair_buddy = ''
    food = ''
    week = ''
# creating objects
repair_job1 = HouseRepair()
repair_job2 = HouseRepair()
repair_job3 = HouseRepair()
repair_job4 = HouseRepair()
repair_job5 = HouseRepair()
# assigning values to attributes
repair_job1.where = 'kitchen'
repair_job2.repair_buddy = 'john'
repair_job3.food = 'posho and greens'
repair_job4.week = 'week two'
repair_job5.repair_buddy = 'james'
#accessing attributes
print(HouseRepair.duration)
print(repair_job4.week)

#class 3
# create class
class WorkOutMix:
    # define an attribute
    mix_name = ''
    duration = float
    artist = ''
    play_count = int
    genre = ''
    gym_bangers = 'BoomBoom'

# creating objects
mix1 = WorkOutMix()
mix2 = WorkOutMix()
mix3 = WorkOutMix()
mix4 = WorkOutMix()
mix5 = WorkOutMix()

# assigning values to attributes
mix1.artist = 'Black Coffe'
mix2.mix_name = 'Amapiano Balcony Jozi 2022'
mix3.artist = 'Lofi'
mix4.duration = '45:34'
mix5.play_count = 16
#accessing attributes
print(WorkOutMix.gym_bangers)
print(mix4.duration)

#class 4
# create class
class CoinCollection:
    # define an attribute
    country = ''
    date_of_minting = ''
    weight = ''
    composition = ''
    diameter = ''
# creating objects
coin1 = CoinCollection()
coin2 = CoinCollection()
coin3 = CoinCollection()
coin4 = CoinCollection()
coin5 = CoinCollection()
# assigning values to attributes
coin1.country = 'South Africa'
coin2.weight = '11g'
coin3.date_of_minting = '01/03/67'
coin4.composition = 'nickle + tin'
coin5.diameter = '2.1mm'
#accessing attribute
print(coin4.composition)

#class 5
# create class
class Podcasts:
    # define an attribute
    name = ''
    duration = ''
    subject_matter = ''
    subs = ''
    location = ''
    platform = ''
# creating objects
podcast1 = Podcasts()
podcast2 = Podcasts()
podcast3 = Podcasts()
podcast4 = Podcasts()
podcast5 = Podcasts()

# assigning values to attributes
podcast1.subject_matter = 'sports'
podcast2.subs = '1.2 million'
podcast3.location = 'kampala,uganda'
podcast4.name = 'Joe Rogan Experience'
podcast5.platform = 'Spotify'

#accessing attribute
print(podcast3.location)

#class 6
# create class
class MyPets:
    # define an attribute
    habitat = 'Anywhere outside the House in the Compound'
    animal = ''
    years = ''
    feed = ''
    
# creating objects
pet1 = MyPets()
pet2 = MyPets()
pet3 = MyPets()
pet4 = MyPets()
pet5 = MyPets()

# assigning values to attributes
pet1.animal = 'dog'
pet2.feed   = 'chicken feed'
pet3.years  = '4 years'
pet4.animal = 'cat'
pet5.years = '2.5 years'

#accessing attributes
print(MyPets.habitat)
print(pet2.feed)
print(f"{pet4.animal} is less than {pet3.years}.")

#class 7
# create class
class Pens:
    # define an attribute
    type = ''
    colour = ''
    construction = ''
    
# creating objects
pen1 = Pens()
pen2 = Pens()
pen3 = Pens()
pen4 = Pens()
pen5 = Pens()

# assigning values to attributes
pen1.type = 'Ball point'
pen2.colour = 'black'
pen3.type = 'Dip Pen'
pen4.construction = 'plastic'
pen5.colour = 'blue'
#accessing attributes
print(f"The {pen2.colour} and {pen5.colour} {pen1.type} are better than the {pen3.type}.")

#class 8
# create class
class Breaks:
    # define an attribute
    start_time = ''
    end_time = ''
    work_before = ''
    work_after = ''
    work_duration_before = ''
    work_duration_after = ''
# creating objects
break1 = Breaks()
break2 = Breaks()
break3 = Breaks()
break4 = Breaks()
break5 = Breaks()

# assigning values to attributes
break1.start_time = '10:30'
break1.end_time = '11:00'
break1.work_before = 'Debugging'
break1.work_duration_before = '2 hours'
#accessing attributes
print(f"break starts at {break1.start_time} after {break1.work_before}")


#class 9
# create class
class Bulbs:
    # define an attribute
    type = ''
    wattage = ''
    connection = ''
    lumens = ''
    colour = ''
# creating objects
bulb1 = Bulbs()
bulb2 = Bulbs()
bulb3 = Bulbs()
bulb4 = Bulbs()
bulb5 = Bulbs()

# assigning values to attributes
bulb1.lumens = '400+'
bulb2.colour = 'white'
bulb3.type = 'LED'
bulb4.wattage = '28W'
bulb5.connection = 'screw on'

#accessing attributes
print(f"is {bulb4.wattage} better than {bulb1.lumens} ?" )


#class 10
# create class
class FriedChips:
    # define an attribute
    type = ''
    flavor = ''
    quantity = ''
    brand = ''
    
# creating objects
chips1 = FriedChips()
chips2 = FriedChips()
chips3 = FriedChips()
chips4 = FriedChips()
chips5 = FriedChips()

# assigning values to attributes
chips1.type = 'banana'
chips2.quantity = '250g'
chips3.flavor = 'salt and vinegar'
chips4.brand = 'Simba'
chips5.type = 'potato'
#accessing attributes
print(f"{chips4.brand} {chips3.flavor}")



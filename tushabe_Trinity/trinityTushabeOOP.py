#1movie
class Movie:
    title = "The Shawshank Redemption"
    director = "Frank Darabont"
    genre = "Drama"
    release_year = 1994
    duration = 142

movie1 = Movie()
movie1.title = "The Godfather"
movie1.director = "Francis Ford Coppola"
movie1.genre = "Crime"
movie1.release_year = 1972
movie1.duration = 175

movie2 = Movie()
movie2.title = "Pulp Fiction"
movie2.director = "Quentin Tarantino"
movie2.genre = "Crime"
movie2.release_year = 1994
movie2.duration = 154

movie3 = Movie()
movie3.title = "Inception"
movie3.director = "Christopher Nolan"
movie3.genre = "Sci-Fi"
movie3.release_year = 2010
movie3.duration = 148

movie4 = Movie()
movie4.title = "The Dark Knight"
movie4.director = "Christopher Nolan"
movie4.genre = "Action"
movie4.release_year = 2008
movie4.duration = 152

movie5 = Movie()
movie5.title = "The Matrix"
movie5.director = "The Wachowski Brothers"
movie5.genre = "Sci-Fi"
movie5.release_year = 1999
movie5.duration = 136

movie6 = Movie()
movie6.title = "Forrest Gump"
movie6.director = "Robert Zemeckis"
movie6.genre = "Drama"
movie6.release_year = 1994
movie6.duration = 142


# Printing one object using a formatted string
print(f"Title: {movie1.title}\nDirector: {movie1.director}\nGenre: {movie1.genre}")
print("--------------------------------------------------------------------------------------------------------------------")

class Furniture:
    name = "Sofa"
    material = "Leather"
    color = "Black"
    price = 799.99

furniture1 = Furniture()
furniture2 = Furniture()
furniture2.name = "Bed"
furniture2.material = "Wood"
furniture2.color = "Brown"
furniture2.price = 1299.99

furniture3 = Furniture()
furniture3.name = "Desk"
furniture3.material = "Metal"
furniture3.color = "Silver"
furniture3.price = 299.99

furniture4 = Furniture()
furniture4.name = "Dining Table"
furniture4.material = "Glass"
furniture4.color = "Clear"
furniture4.price = 599.99

furniture5 = Furniture()
furniture5.name = "Bookshelf"
furniture5.material = "Wood"
furniture5.color = "White"
furniture5.price = 249.99

# Printing objects using formatted strings
print(f"Furniture 1: {furniture1.name}, Material: {furniture1.material}, Color: {furniture1.color}, Price: {furniture1.price}")
print("--------------------------------------------------------------------------------------------------------------------")


#2song
class Song:
    title = "Bohemian Rhapsody"
    artist = "Queen"
    genre = "Rock"
    release_year = 1975
    duration = 355

song1 = Song()
song1.title = "Hotel California"
song1.artist = "Eagles"
song1.genre = "Rock"
song1.release_year = 1976
song1.duration = 390

song2 = Song()
song2.title = "Thriller"
song2.artist = "Michael Jackson"
song2.genre = "Pop"
song2.release_year = 1982
song2.duration = 357

song3 = Song()
song3.title = "Hey Jude"
song3.artist = "The Beatles"
song3.genre = "Rock"
song3.release_year = 1968
song3.duration = 431

song4 = Song()
song4.title = "Shape of You"
song4.artist = "Ed Sheeran"
song4.genre = "Pop"
song4.release_year = 2017
song4.duration = 233

song5 = Song()
song5.title = "Smells Like Teen Spirit"
song5.artist = "Nirvana"
song5.genre = "Grunge"
song5.release_year = 1991
song5.duration = 301

song6 = Song()
song6.title = "Bohemian Rhapsody"
song6.artist = "Queen"
song6.genre = "Rock"
song6.release_year = 1975
song6.duration = 355



# Printing one object using a formatted string
print(f"Title: {song1.title}\nArtist: {song1.artist}\nGenre: {song1.genre}")
print("--------------------------------------------------------------------------------------------------------------------")

#3restaurant
class Restaurant:
    name = "The French Bistro"
    cuisine = "French"
    rating = 4.5
    location = "Paris"
    price_range = "UGX700000"

restaurant1 = Restaurant()
restaurant1.name = "Mama Mia Pizzeria"
restaurant1.cuisine = "Italian"
restaurant1.rating = 4.2
restaurant1.location = "Rome"
restaurant1.price_range = "UGX800000"

restaurant2 = Restaurant()
restaurant2.name = "Sushi Garden"
restaurant2.cuisine = "Japanese"
restaurant2.rating = 4.7
restaurant2.location = "Tokyo"
restaurant2.price_range = "UGX900000"

restaurant3 = Restaurant()
restaurant3.name = "Spice Paradise"
restaurant3.cuisine = "Indian"
restaurant3.rating = 4.3
restaurant3.location = "Mumbai"
restaurant3.price_range = "UGX850000"

restaurant4 = Restaurant()
restaurant4.name = "El Taqueria"
restaurant4.cuisine = "Mexican"
restaurant4.rating = 4.6
restaurant4.location = "Mexico City"
restaurant4.price_range = "UGX780000"

restaurant5 = Restaurant()
restaurant5.name = "The Steakhouse"
restaurant5.cuisine = "American"
restaurant5.rating = 4.4
restaurant5.location = "New York City"
restaurant5.price_range = "UGX600000"

restaurant6 = Restaurant()
restaurant6.name = "Thai Orchid"
restaurant6.cuisine = "Thai"
restaurant6.rating = 4.8
restaurant6.location = "Bangkok"
restaurant6.price_range = "UGX780000"

# Printing one object using a formatted string
print(f"Name: {restaurant3.name}\nCuisine: {restaurant3.cuisine}\nRating: {restaurant3.rating}")
print("--------------------------------------------------------------------------------------------------------------------")

#4songplaylist
class SongPlaylist:
    name = "Summer Hits"
    genre = "Various"
    creator = "John"
    duration = 120
    number_of_songs = 15

playlist1 = SongPlaylist()
playlist2 = SongPlaylist()
playlist3 = SongPlaylist()

playlist4 = SongPlaylist()
playlist4.name = "Throwback Classics"
playlist4.genre = "Various"
playlist4.creator = "Emily"
playlist4.duration = 180
playlist4.number_of_songs = 20

playlist5 = SongPlaylist()
playlist5.name = "Chill Vibes"
playlist5.genre = "Pop"
playlist5.creator = "Sarah"
playlist5.duration = 90
playlist5.number_of_songs = 10

playlist6 = SongPlaylist()
playlist6.name = "Rap Bangers"
playlist6.genre = "Hip-Hop"
playlist6.creator = "Mike"
playlist6.duration = 150
playlist6.number_of_songs = 18

# Printing one object using a formatted string
print(f"Name: {playlist1.name}\nGenre: {playlist1.genre}\nCreator: {playlist1.creator}")
print("--------------------------------------------------------------------------------------------------------------------")

#5film Director
class FilmDirector:
    name = "Christopher Nolan"
    nationality = "British"
    birth_year = 1970
    active_years = "1998-present"
    notable_works = ["Inception", "The Dark Knight", "Interstellar"]

director1 = FilmDirector()
director2 = FilmDirector()
director3 = FilmDirector()

director4 = FilmDirector()
director4.name = "Steven Spielberg"
director4.nationality = "American"
director4.birth_year = 1946
director4.active_years = "1969-present"
director4.notable_works = ["Jurassic Park", "Jaws", "E.T. the Extra-Terrestrial"]

director5 = FilmDirector()
director5.name = "Quentin Tarantino"
director5.nationality = "American"
director5.birth_year = 1963
director5.active_years = "1987-present"
director5.notable_works = ["Pulp Fiction", "Kill Bill", "Django Unchained"]

director6 = FilmDirector()
director6.name = "Hayao Miyazaki"
director6.nationality = "Japanese"
director6.birth_year = 1941
director6.active_years = "1963-2013"
director6.notable_works = ["Spirited Away", "Princess Mononoke", "My Neighbor Totoro"]

# Printing one object using a formatted string
print(f"Name: {director1.name}\nNationality: {director1.nationality}\nBirth Year: {director1.birth_year}")
print("--------------------------------------------------------------------------------------------------------------------")


#6sport
class Sport:
    name = "Football"
    category = "Team sport"
    players = 22
    equipment = "Ball"
    origin = "Ancient China"

sport1 = Sport()
sport2 = Sport()
sport3 = Sport()

sport4 = Sport()
sport4.name = "Basketball"
sport4.category = "Team sport"
sport4.players = 10
sport4.equipment = "Basketball"
sport4.origin = "United States"

sport5 = Sport()
sport5.name = "Tennis"
sport5.category = "Individual sport"
sport5.players = 1 or 2
sport5.equipment = "Tennis racket, Tennis ball"
sport5.origin = "Medieval Europe"

sport6 = Sport()
sport6.name = "Swimming"
sport6.category = "Individual sport"
sport6.players = 1
sport6.equipment = "Swimsuit, Goggles, Cap"
sport6.origin = "Ancient Egypt"

# Printing one object using a formatted string
print(f"Name: {sport1.name}\nCategory: {sport1.category}\nPlayers: {sport1.players}")
print("--------------------------------------------------------------------------------------------------------------------")


#7building
class Building:
    name = "Empire State Building"
    location = "New York City"
    height = 443.2
    floors = 102
    architect = "William F. Lamb"

building1 = Building()
building2 = Building()
building3 = Building()

building4 = Building()
building4.name = "Burj Khalifa"
building4.location = "Dubai, United Arab Emirates"
building4.height = 828
building4.floors = 163
building4.architect = "Adrian Smith"

building5 = Building()
building5.name = "Shanghai Tower"
building5.location = "Shanghai, China"
building5.height = 632
building5.floors = 128
building5.architect = "Gensler"

building6 = Building()
building6.name = "Petronas Towers"
building6.location = "Kuala Lumpur, Malaysia"
building6.height = 452
building6.floors = 88
building6.architect = "Cesar Pelli"

# Printing one object using a formatted string
print(f"Name: {building1.name}\nLocation: {building1.location}\nHeight: {building1.height}")
print("--------------------------------------------------------------------------------------------------------------------")

#8instrument
class Instrument:
    name = "Piano"
    type = "Keyboard"
    sound = "Melodious"
    origin = "Italy"
    family = "Percussion"


instrument1 = Instrument()
instrument1.name = "Flute"
instrument1.type = "Woodwind"
instrument1.sound = "Mellow"
instrument1.origin = "Various"
instrument1.family = "Aerophone"

instrument2 = Instrument()
instrument2.name = "Trumpet"
instrument2.type = "Brass"
instrument2.sound = "Bright"
instrument2.origin = "Various"
instrument2.family = "Aerophone"

instrument3 = Instrument()
instrument3.name = "Bass Guitar"
instrument3.type = "Stringed"
instrument3.sound = "Groovy"
instrument3.origin = "United States"
instrument3.family = "Chordophone"

instrument4 = Instrument()
instrument4.name = "Guitar"
instrument4.type = "Stringed"
instrument4.sound = "Versatile"
instrument4.origin = "Spain"
instrument4.family = "Chordophone"

instrument5 = Instrument()
instrument5.name = "Drums"
instrument5.type = "Percussion"
instrument5.sound = "Rhythmic"
instrument5.origin = "Various"
instrument5.family = "Membranophone"

instrument6 = Instrument()
instrument6.name = "Violin"
instrument6.type = "Stringed"
instrument6.sound = "Melancholic"
instrument6.origin = "Italy"
instrument6.family = "Chordophone"


# Printing one object using a formatted string
print(f"Name: {instrument1.name}\nType: {instrument1.type}\nSound: {instrument1.sound}")
print("--------------------------------------------------------------------------------------------------------------------")


#9website
class Website:
    name = "Wikipedia"
    domain = "wikipedia.org"
    language = "Multiple"
    founder = "Jimmy Wales"
    launched_year = 2001

website1 = Website()
name = "Google"
domain = "google.com"
language = "Multiple"
founder = "Larry Page, Sergey Brin"
launched_year = 1998

website2 = Website()
name = "Facebook"
domain = "facebook.com"
language = "Multiple"
founder = "Mark Zuckerberg"
launched_year =  2004

website3 = Website()
name = "Amazon"  
domain = "amazon.com"
language = "Multiple"
founder = "Jeff Bezos"
launched_year = 1994

website4 = Website()
name = "YouTube"
domain = "youtube.com"
language = "Multiple"
founder = "Steve Chen, Chad Hurley, Jawed Karim"
launched_year = 2005

website5 = Website()
name = "Twitter"
domain = "twitter.com"
language = "Multiple"
founder = "Jack Dorsey, Biz Stone, Evan Williams"
launched_year = 2006

# Printing one object using a formatted string
print(f"Name: {website1.name}\nDomain: {website1.domain}\nLanguage: {website1.language}")
print("--------------------------------------------------------------------------------------------------------------------")

#10 
class Cloth:
    name = "T-Shirt"
    material = "Cotton"
    color = "White"
    size = "Medium"

cloth1 = Cloth()
cloth1.color = "Blue"
cloth1.size = "Large"

cloth2 = Cloth()
cloth2.name = "Jeans"
cloth2.material = "Denim"
cloth2.color = "Black"
cloth2.size = "32"

cloth3 = Cloth()
cloth3.name = "Dress"
cloth3.material = "Silk"
cloth3.color = "Red"
cloth3.size = "Small"

cloth4 = Cloth()
cloth4.name = "Hoodie"
cloth4.material = "Fleece"
cloth4.color = "Gray"
cloth4.size = "Medium"

cloth5 = Cloth()
cloth5.name = "Skirt"
cloth5.material = "Cotton"
cloth5.color = "Yellow"
cloth5.size = "Small"

# Printing the objects using formatted strings
print(f"Cloth 1: {cloth1.name}\nMaterial: {cloth1.material}\nColor: {cloth1.color}\nSize: {cloth1.size}")
print("--------------------------------------------------------------------------------------------------------------------")




class MobilePhone:
    brand = "Samsung"
    model = "Galaxy S21"
    storage = "128GB"
    color = "Phantom Black"
    price = 999

phone1 = MobilePhone()
brand = "iPhone"
model = "14 pro max"
storage = "256GB"

phone2 = MobilePhone()
brand = "Techno"
model = "Spark"
storage = "512GB"

phone3 = MobilePhone()
brand = "Infinix"
model = "Hot"
storage = "256GB"

phone4 = MobilePhone()
brand = "itel"
model = "P15"
storage = "64GB"

phone5 = MobilePhone()
brand = "Hauwei"
model = "P20"
storage = "512GB"

# Printing one object using a formatted string
print(f"Brand: {phone1.brand}\nModel: {phone1.model}\nStorage: {phone1.storage}")







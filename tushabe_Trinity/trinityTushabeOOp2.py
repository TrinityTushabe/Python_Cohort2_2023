'''
The code below defines classes for different objects. 
Suchas movies, furniture, songs, restaurants, songPlaylists, filmdirectors, sports, buildings, instruments, websites, and clothes.
Each class has attributes that describe the properties of the corresponding object.
The constructor method __init__ is defined for each class to initialize the attributes.
The objects are created by passing the attribute values to the constructor when creating instances of the classes.
print("--------------------------------") separates the attributes
'''

# Movie class represents a movie with attributes such as title, director, genre, release year, and duration.
class Movie:
    def __init__(self, title, director, genre, release_year, duration):
        self.title = title
        self.director = director
        self.genre = genre
        self.release_year = release_year
        self.duration = duration
        
# Create instances of the Movie class with different movie details.
movie1 = Movie("The Godfather", "Francis Ford Coppola", "Crime", 1972, 175)
movie2 = Movie("Pulp Fiction", "Quentin Tarantino", "Crime", 1994, 154)
movie3 = Movie("Inception", "Christopher Nolan", "Sci-Fi", 2010, 148)
movie4 = Movie("The Dark Knight", "Christopher Nolan", "Action", 2008, 152)
movie5 = Movie("The Matrix", "The Wachowski Brothers", "Sci-Fi", 1999, 136)
movie6 = Movie("Forrest Gump", "Robert Zemeckis", "Drama", 1994, 142)

# Print the attributes of the movie objects.
print(f"Title: {movie1.title}\nDirector: {movie1.director}\nGenre: {movie1.genre}")
print("--------------------------------------------------------------------------------------------------------------------")

# Furniture class represents a piece of furniture with attributes such as name, material, color, and price.
class Furniture:
    def __init__(self, name, material, color, price):
        self.name = name
        self.material = material
        self.color = color
        self.price = price
        
# Create instances of the Furniture class with different furniture details.
furniture1 = Furniture("Sofa", "Leather", "Black", 799.99)
furniture2 = Furniture("Bed", "Wood", "Brown", 1299.99)
furniture3 = Furniture("Desk", "Metal", "Silver", 299.99)
furniture4 = Furniture("Dining Table", "Glass", "Clear", 599.99)
furniture5 = Furniture("Bookshelf", "Wood", "White", 249.99)

# Print the attributes of the furniture objects.
print(f"Furniture 1: {furniture1.name}, Material: {furniture1.material}, Color: {furniture1.color}, Price: {furniture1.price}")
print("--------------------------------------------------------------------------------------------------------------------")

# Song class represents a song with attributes such as title, artist, genre, release year, and duration.
class Song:
    def __init__(self, title, artist, genre, release_year, duration):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.release_year = release_year
        self.duration = duration

# Create instances of the Song class with different song details.
song1 = Song("Hotel California", "Eagles", "Rock", 1976, 390)
song2 = Song("Thriller", "Michael Jackson", "Pop", 1982, 357)
song3 = Song("Hey Jude", "The Beatles", "Rock", 1968, 431)
song4 = Song("Shape of You", "Ed Sheeran", "Pop", 2017, 233)
song5 = Song("Smells Like Teen Spirit", "Nirvana", "Grunge", 1991, 301)
song6 = Song("Bohemian Rhapsody", "Queen", "Rock", 1975, 355)


# Print the attributes of the song objects.
print(f"Title: {song1.title}\nArtist: {song1.artist}\nGenre: {song1.genre}")
print("--------------------------------------------------------------------------------------------------------------------")

# Restaurant class represents a restaurant with attributes such as name, cuisine, rating, location, and price range.
class Restaurant:
    def __init__(self, name, cuisine, rating, location, price_range):
        self.name = name
        self.cuisine = cuisine
        self.rating = rating
        self.location = location
        self.price_range = price_range
        
# Create instances of the Restaurant class with different restaurant details.
restaurant1 = Restaurant("Mama Mia Pizzeria", "Italian", 4.2, "Rome", "UGX800000")
restaurant2 = Restaurant("Sushi Garden", "Japanese", 4.7, "Tokyo", "UGX900000")
restaurant3 = Restaurant("Spice Paradise", "Indian", 4.3, "Mumbai", "UGX850000")
restaurant4 = Restaurant("El Taqueria", "Mexican", 4.6, "Mexico City", "UGX780000")
restaurant5 = Restaurant("The Steakhouse", "American", 4.4, "New York City", "UGX600000")
restaurant6 = Restaurant("Thai Orchid", "Thai", 4.8, "Bangkok", "UGX780000")


# Print the attributes of the restaurant objects.
print(f"Name: {restaurant3.name}\nCuisine: {restaurant3.cuisine}\nRating: {restaurant3.rating}")
print("--------------------------------------------------------------------------------------------------------------------")

# SongPlaylist class represents a playlist of songs with attributes such as name, genre, creator, duration, and number of songs.
class SongPlaylist:
    def __init__(self, name, genre, creator, duration, number_of_songs):
        self.name = name
        self.genre = genre
        self.creator = creator
        self.duration = duration
        self.number_of_songs = number_of_songs

# Create instances of the SongPlaylist class with different playlist details.
playlist1 = SongPlaylist("Summer Hits", "Various", "John", 120, 15)
playlist2 = SongPlaylist("Throwback Classics", "Various", "Emily", 180, 20)
playlist3 = SongPlaylist("Chill Vibes", "Pop", "Sarah", 90, 10)
playlist4 = SongPlaylist("Rap Bangers", "Hip-Hop", "Mike", 150, 18)


# Print the attributes of the songPlaylist objects.
print(f"Name: {playlist1.name}\nGenre: {playlist1.genre}\nCreator: {playlist1.creator}")
print("--------------------------------------------------------------------------------------------------------------------")

# FilmDirector class represents a film director with attributes such as name, nationality, birth year, active years, and notable works.
class FilmDirector:
    def __init__(self, name, nationality, birth_year, active_years, notable_works):
        self.name = name
        self.nationality = nationality
        self.birth_year = birth_year
        self.active_years = active_years
        self.notable_works = notable_works

# Create instances of the FilmDirector class with different director details.
director1 = FilmDirector("Christopher Nolan", "British", 1970, "1998-present", ["Inception", "The Dark Knight", "Interstellar"])
director2 = FilmDirector("Steven Spielberg", "American", 1946, "1969-present", ["Jurassic Park", "Jaws", "E.T. the Extra-Terrestrial"])
director3 = FilmDirector("Quentin Tarantino", "American", 1963, "1987-present", ["Pulp Fiction", "Kill Bill", "Django Unchained"])
director4 = FilmDirector("Hayao Miyazaki", "Japanese", 1941, "1963-2013", ["Spirited Away", "Princess Mononoke", "My Neighbor Totoro"])

print(f"Name: {director1.name}\nNationality: {director1.nationality}\nBirth Year: {director1.birth_year}")
print("--------------------------------------------------------------------------------------------------------------------")

# Sport class represents a sport with attributes such as name, category, players, equipment, and origin.
class Sport:
    def __init__(self, name, category, players, equipment, origin):
        self.name = name
        self.category = category
        self.players = players
        self.equipment = equipment
        self.origin = origin
        
# Create instances of the Sport class with different sport details.
sport1 = Sport("Football", "Team sport", 22, "Ball", "Ancient China")
sport2 = Sport("Basketball", "Team sport", 10, "Basketball", "United States")
sport3 = Sport("Tennis", "Individual sport", "1 or 2", "Tennis racket, Tennis ball", "Medieval Europe")
sport4 = Sport("Swimming", "Individual sport", 1, "Swimsuit, Goggles, Cap", "Ancient Egypt")

# Print the attributes of the sport objects.
print(f"Name: {sport1.name}\nCategory: {sport1.category}\nPlayers: {sport1.players}")
print("--------------------------------------------------------------------------------------------------------------------")


# Building class represents a building with attributes such as name, location, height, floors, and architect.
class Building:
    def __init__(self, name, location, height, floors, architect):
        self.name = name
        self.location = location
        self.height = height
        self.floors = floors
        self.architect = architect

# Create instances of the Building class with different building details.
building1 = Building("Empire State Building", "New York City", 443.2, 102, "William F. Lamb")
building2 = Building("Burj Khalifa", "Dubai, United Arab Emirates", 828, 163, "Adrian Smith")
building3 = Building("Shanghai Tower", "Shanghai, China", 632, 128, "Gensler")
building4 = Building("Petronas Towers", "Kuala Lumpur, Malaysia", 452, 88, "Cesar Pelli")

# Print the attributes of the building objects.
print(f"Name: {building1.name}\nLocation: {building1.location}\nHeight: {building1.height}")
print("--------------------------------------------------------------------------------------------------------------------")


# Instrument class represents an instrument with attributes such as name, type, sound, origin, and family.
class Instrument:
    def __init__(self, name, type, sound, origin, family):
        self.name = name
        self.type = type
        self.sound = sound
        self.origin = origin
        self.family = family


# Create instances of the Instrument class with different instrument details.
instrument1 = Instrument("Piano", "Keyboard", "Melodious", "Italy", "Percussion")
instrument2 = Instrument("Flute", "Woodwind", "Mellow", "Various", "Aerophone")
instrument3 = Instrument("Trumpet", "Brass", "Bright", "Various", "Aerophone")
instrument4 = Instrument("Bass Guitar", "Stringed", "Groovy", "United States", "Chordophone")

# Print the attributes of the instrument objects.
print(f"Name: {instrument1.name}\nType: {instrument1.type}\nSound: {instrument1.sound}")
print("--------------------------------------------------------------------------------------------------------------------")

# Website class represents a website with attributes such as name, domain, language, founder, and launched year.
class Website:
    def __init__(self, name, domain, language, founder, launched_year):
        self.name = name
        self.domain = domain
        self.language = language
        self.founder = founder
        self.launched_year = launched_year
        
# Create instances of the Website class with different website details.
website1 = Website("Wikipedia", "wikipedia.org", "Multiple", "Jimmy Wales", 2001)
website2 = Website("Google", "google.com", "Multiple", "Larry Page, Sergey Brin", 1998)
website3 = Website("Facebook", "facebook.com", "Multiple", "Mark Zuckerberg", 2004)
website4 = Website("Amazon", "amazon.com", "Multiple", "Jeff Bezos", 1994)

# Print the attributes of the website objects.
print(f"Name: {website1.name}\nDomain: {website1.domain}\nLanguage: {website1.language}")
print("--------------------------------------------------------------------------------------------------------------------")

# Cloth class represents a piece of cloth with attributes such as name, material, color, and size.
class Cloth:
    def __init__(self, name, material, color, size):
        self.name = name
        self.material = material
        self.color = color
        self.size = size

# Create instances of the Cloth class with different cloth details.
cloth1 = Cloth("T-Shirt", "Cotton", "White", "Medium")
cloth2 = Cloth("Jeans", "Denim", "Black", "32")
cloth3 = Cloth("Dress", "Silk", "Red", "Small")
cloth4 = Cloth("Hoodie", "Fleece", "Gray", "Medium")

# Print the attributes of the cloth objects.
print(f"Cloth 1: {cloth1.name}\nMaterial: {cloth1.material}\nColor: {cloth1.color}\nSize: {cloth1.size}")
print("--------------------------------------------------------------------------------------------------------------------")

# MobilePhone class represents a mobile phone with attributes such as brand, model, storage, color, and price.
class MobilePhone:
    def __init__(self, brand, model, storage, color, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color
        self.price = price
# Create instances of the MobilePhone class with different phone details.
phone1 = MobilePhone("Samsung", "Galaxy S21", "128GB", "Phantom Black", 2000000)
phone2 = MobilePhone("iPhone", "14 pro max", "256GB", "", "")
phone3 = MobilePhone("Techno", "Spark", "512GB", "", "")
phone4 = MobilePhone("Infinix", "Hot", "256GB", "", "")
phone5 = MobilePhone("itel", "P15", "64GB", "", "")

# Print the attributes of the phone objects.
print(f"Brand: {phone1.brand}\nModel: {phone1.model}\nStorage: {phone1.storage}")
print("--------------------------------------------------------------------------------------------------------------------")

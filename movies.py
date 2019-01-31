from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Movie, Genre, User

engine = create_engine('sqlite:///movies.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Admin user
user = User(name="admin", email="admin@xyz.com", picture='')
session.add(user)
session.commit()

# Genres
action = Genre(name='action')
session.add(action)
session.commit()

comedy = Genre(name='comedy')
session.add(comedy)
session.commit()

drama = Genre(name='drama')
session.add(drama)
session.commit()

horror = Genre(name='horror')
session.add(horror)
session.commit()

musical = Genre(name='musical')
session.add(musical)
session.commit()

superhero = Genre(name='superhero')
session.add(superhero)
session.commit()

print("added genres!")


# Movies
roma = Movie(user_id=user.id, title="Roma",
             storyline="A year in the life of a middle-class family's maid in Mexico City in the early 1970s.",
             poster_image_url="https://upload.wikimedia.org/wikipedia/en/thumb/8/85/Roma_theatrical_poster.png/220px-Roma_theatrical_poster.png",
             # trailer_youtube_url="6BS27ngZtxg",
             genre_id=drama.id)
session.add(roma)
session.commit()


first_man = Movie(user_id=user.id, title="First Man",
                  storyline="A Biopic on the life of the legendary American Astronaut Neil Armstrong from 1961-1969, on his journey to becoming the first human to walk the moon. Exploring the sacrifices and costs on the Nation and Neil himself, during one of the most dangerous missions in the history of space travel.",
                  poster_image_url="https://m.media-amazon.com/images/M/MV5BMDBhOTMxN2UtYjllYS00NWNiLWE1MzAtZjg3NmExODliMDQ0XkEyXkFqcGdeQXVyMjMxOTE0ODA@._V1_UX182_CR0,0,182,268_AL_.jpg",
                  # trailer_youtube_url="6BS27ngZtxg",
                  genre_id=drama.id)
session.add(first_man)
session.commit()


black_panther = Movie(user_id=user.id, title="Black Panther",
                      storyline="After the events of Captain America: Civil War, Prince T'Challa returns home to the reclusive, technologically advanced African nation of Wakanda to serve as his country's new king. However, T'Challa soon finds that he is challenged for the throne from factions within his own country. When two foes conspire to destroy Wakanda, the hero known as Black Panther must team up with C.I.A. agent Everett K. Ross and members of the Dora Milaje, Wakandan special forces, to prevent Wakanda from being dragged into a world war.",
                      poster_image_url="https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
                      # trailer_youtube_url="xjDjIWPwcPU",
                      genre_id=superhero.id)
session.add(black_panther)
session.commit()

avengers = Movie(user_id=user.id, title="Avengers: Infinity War",
                 storyline="As the Avengers and their allies have continued to protect the world from threats too large for any one hero to handle, a new danger has emerged from the cosmic shadows: Thanos. A despot of intergalactic infamy, his goal is to collect all six Infinity Stones, artifacts of unimaginable power, and use them to inflict his twisted will on all of reality. Everything the Avengers have fought for has led up to this moment, the fate of Earth and existence has never been more uncertain.",
                 poster_image_url="https://m.media-amazon.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_UX182_CR0,0,182,268_AL_.jpg",
                 # trailer_youtube_url="xjDjIWPwcPU",
                 genre_id=superhero.id)
session.add(avengers)
session.commit()

bird_box = Movie(user_id=user.id, title="Bird Box",
                 storyline="In the wake of an unknown global terror, a mother must find the strength to flee with her children down a treacherous river in search of safety. Due to unseen deadly forces, the perilous journey must be made blindly.",
                 poster_image_url="https://upload.wikimedia.org/wikipedia/en/thumb/b/bd/Bird_Box_%28film%29.png/220px-Bird_Box_%28film%29.png",
                 # trailer_youtube_url="xjDjIWPwcPU",
                 genre_id=horror.id)
session.add(bird_box)
session.commit()

quite_place = Movie(user_id=user.id, title="A Quiet Place",
                    storyline="wo parents do what it takes to keep their children safe in a world full of creatures hunting every sound they can hear. Not a sound can be heard from the family hiding in silence, but all it takes is one noise and everything can go wrong.",
                    poster_image_url="https://m.media-amazon.com/images/M/MV5BMjI0MDMzNTQ0M15BMl5BanBnXkFtZTgwMTM5NzM3NDM@._V1_UX182_CR0,0,182,268_AL_.jpg",
                    # trailer_youtube_url="xjDjIWPwcPU",
                    genre_id=horror.id)
session.add(quite_place)
session.commit()

print("added movies!")

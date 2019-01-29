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

thriller = Genre(name='thriller')
session.add(thriller)
session.commit()

print("added genres!")


# Movies
roma = Movie(user_id=user.id, title="Roma",
               storyline="Roma is about",
               poster_image_url="https://upload.wikimedia.org/wikipedia/en/thumb/8/85/Roma_theatrical_poster.png/220px-Roma_theatrical_poster.png",
               trailer_youtube_url="https://www.youtube.com/watch?v=6BS27ngZtxg",
               genre_id=drama.id)
session.add(roma)
session.commit()

black_panther = Movie(user_id=user.id, title="Black Panther",
               storyline="Black Panther is about",
               poster_image_url="https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
               trailer_youtube_url="https://www.youtube.com/watch?v=xjDjIWPwcPU", 
               genre_id=superhero.id)
session.add(black_panther)
session.commit()

print("added movies!")

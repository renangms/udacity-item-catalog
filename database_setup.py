from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Genre(Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Movie(Base):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    storyline = Column(String(250), nullable=False)
    poster_image_url = Column(String(250), nullable=False)
    trailer_youtube_url = Column(String(250))

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    genre_id = Column(Integer, ForeignKey('genre.id'))
    genre = relationship(Genre)

    @property
    def serialize(self):
       return {
           'id': self.id,
           'title': self.title,
           'storyline': self.storyline,
           'genre': self.genre.name,
           'poster_image_url': self.poster_image_url,
           'trailer_youtube_url': self.trailer_youtube_url
       }


engine = create_engine('sqlite:///movies.db')
Base.metadata.create_all(engine)

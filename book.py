from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base,Categories

engine = create_engine('sqlite:///catalogs.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# create user
User1 = User(name="admin", email="asaeyl202@gmail.com")
session.add(User1)
session.commit()
#add book
book1 = Categories(bookName="Johan and Peewit",
               authorName="Peyo",
               description=" Belgian comics series", category="comics", user_id=1)

session.add(book1)
session.commit()

book2 = Categories(bookName="The Chronicles of Amber",
               authorName="Roger Zelazny",
               description="series of fantasy novels", category="Fantasy", user_id=1)

session.add(book2)
session.commit()

book3 = Categories(bookName="The Silver Branch",
               authorName="Rosemary Sutcliff",
               description="historical adventure novel for children", category="Historical", user_id=1)

session.add(book3)
session.commit()

book4 = Categories(bookName="Hild",
               authorName="Nicola Griffith",
               description="historical novel", category="Historical", user_id=1)

session.add(book4)
session.commit()

book5 = Categories(bookName="Among Others",
               authorName="Jo Walton",
               description="fantasy novel", category="Fantasy", user_id=1)

session.add(book5)
session.commit()


print "added Books!"

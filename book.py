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
book1 = Categories(bookName="The Year of Taking Chances",
               authorName="Lucy Diamond",
               coverUrl="""https://books.google.com/books/content/
               images/frontcover/F9uIBAAAQBAJ?fife=w300-rw""",
               description="hello", category="Romance", user_id=1)

session.add(book1)
session.commit()

book2 = Categories(bookName="Summoner: The Inquisition: Book 2",
               authorName="Taran Matharu",
               description="hello", category="Fantasy", user_id=1)

session.add(book2)
session.commit()

book3 = Categories(bookName="That's The Way We Met",
               authorName="Sudeep Nagarkar",
               description="hello", category="Fiction", user_id=1)

session.add(book3)
session.commit()

book4 = Categories(bookName="The Creep",
               authorName="John Arcudi",
               description="hello", category="Mystery", user_id=1)

session.add(book4)
session.commit()

book5 = Categories(bookName="Now That You're Rich: Let's fall in Love!",
               authorName="Durjoy Datta",
               description="hello", category="Romance", user_id=1)

session.add(book5)
session.commit()


print "added Books!"

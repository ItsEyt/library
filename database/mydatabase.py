from sqlalchemy import create_engine
from modules import db

class MyDB():
    engine = create_engine('sqlite:///library.db', connect_args={'check_same_thread': False}, echo = True)
    db.bind_engine(engine)
    db.Base.metadata.create_all(bind = engine)
    session = db.Session()






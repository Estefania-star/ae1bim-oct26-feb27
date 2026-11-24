from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///clinicas_veterinarias.db", echo=False)
SessionLocal = sessionmaker(bind=engine)
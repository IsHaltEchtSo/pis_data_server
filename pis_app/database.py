from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import DevelopmentConfig

engine = create_engine(DevelopmentConfig.DATABASE_URI)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
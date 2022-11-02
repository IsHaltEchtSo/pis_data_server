from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pis_app.config import DevelopmentConfig
from pis_app.constants import NAMING_CONVENTION

meta = MetaData(naming_convention=NAMING_CONVENTION)

engine = create_engine(DevelopmentConfig.DATABASE_URI)
Base = declarative_base(bind=engine, metadata=meta)
Session = sessionmaker(bind=engine)
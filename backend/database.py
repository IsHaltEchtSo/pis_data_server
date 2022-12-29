from .constants import NAMING_CONVENTION
from .instance.private_config import DevelopmentConfig

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

meta = MetaData(naming_convention=NAMING_CONVENTION)

engine = create_engine(DevelopmentConfig.DATABASE_URI)
Base = declarative_base(bind=engine, metadata=meta)
Session = sessionmaker(bind=engine, autoflush=False)
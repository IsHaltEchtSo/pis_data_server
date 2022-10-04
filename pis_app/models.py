from pis_app.database import Base, Session
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, sessionmaker


#TODO: add repr for classes
#TODO: CUD operations also make a new Zettel Update
#TODO: DB backups as csv for experimentation

class User(Base):
    """A dummy model just yet"""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(12))


zettel_links_association = Table(
    'zettel_links_table', Base.metadata,
    Column('link_id', ForeignKey('zettels.id'), primary_key=True),
    Column('backlink_id', ForeignKey('zettels.id'), primary_key=True)
)


class Zettel(Base):
    __tablename__ = 'zettels'
    id = Column(Integer, primary_key=True)
    luhmann_identifier = Column(String, unique=True, nullable=False)
    title = Column(String, unique=True, nullable=False)
    content = Column(String, default="")
    links = relationship(
        'Zettel', backref='backlinks',
        secondary=zettel_links_association,
        primaryjoin=zettel_links_association.c.link_id == id,
        secondaryjoin=zettel_links_association.c.backlink_id == id,
    )
    updates = relationship('ZettelUpdate', back_populates='zettels')


class ZettelUpdate(Base):
    __tablename__ = 'zettel_updates'
    id = Column(Integer, primary_key=True)
    zettel_id = Column(Integer, ForeignKey('zettels.id'))
    zettels = relationship('Zettel', back_populates='updates')
    updated_columns = relationship('UpdatedColumn', back_populates='zettel_update')
    transferred_to_zettelkasten = Column(Boolean, default=False)


class UpdatedColumn(Base):
    __tablename__ = 'updated_columns'
    id = Column(Integer, primary_key=True)
    zettel_update_id = Column(Integer, ForeignKey('zettel_updates.id'))
    zettel_update = relationship('ZettelUpdate', back_populates='updated_columns')
    column_name = Column(String)
    old_column_value = Column(String)
    new_column_value = Column(String)
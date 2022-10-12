from pis_app.database import Base
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship



class User(Base):
    """A dummy model just yet"""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(12))

    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"<User {self.name}>"


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
    updates = relationship('ZettelUpdate', back_populates='zettel')

    def __init__(self, luhmann_identifier: str, title: str, content: str = "") -> None:
        self.luhmann_identifier = luhmann_identifier
        self.title = title
        self.content = content

    def __repr__(self) -> str:
        return f"<Zettel {self.id}: {self.title}>"

    def add_outgoing_links(self, links_list: list) -> None:
        self.links.extend(links_list)


class ZettelUpdate(Base):
    __tablename__ = 'zettel_updates'
    id = Column(Integer, primary_key=True)
    zettel_id = Column(Integer, ForeignKey('zettels.id'))
    zettel = relationship('Zettel', back_populates='updates')
    updated_columns = relationship('UpdatedColumn', back_populates='zettel_update')
    transferred_to_zettelkasten = Column(Boolean, default=False)

    def __init__(self, zettel: Zettel=None, updated_columns: list('UpdatedColumn')=None, transferred_to_zettelkasten: Boolean=False) -> None:
        self.zettel = zettel
        self.updated_columns = updated_columns
        self.transferred_to_zettelkasten = transferred_to_zettelkasten

    def __repr__(self) -> str:
        return f"<Zettel Update {self.id} for Zettel {self.zettel_id}>"

    def add_columns(self, updated_columns: list('UpdatedColumn')) -> str:
        self.updated_columns.extend(updated_columns)


class UpdatedColumn(Base):
    __tablename__ = 'updated_columns'
    id = Column(Integer, primary_key=True)
    zettel_update_id = Column(Integer, ForeignKey('zettel_updates.id'))
    zettel_update = relationship('ZettelUpdate', back_populates='updated_columns')
    column_name = Column(String, nullable=False)
    old_column_value = Column(String, nullable=False)
    new_column_value = Column(String, nullable=False)

    def __init__(self, column_name: str, old_column_value: str, new_column_value: str) -> None:
        self.column_name = column_name
        self.old_column_value = old_column_value
        self.new_column_value = new_column_value

    def __repr__(self) -> str:
        return f"<Updated Column {self.column_name} for Zettel Update {self.zettel_update_id}>"
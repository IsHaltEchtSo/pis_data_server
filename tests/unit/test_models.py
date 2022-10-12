"""
Contains Unit Tests for pis_app/models.py file.
"""

from pis_app.models import User, Zettel, ZettelUpdate, UpdatedColumn, zettel_links_association

class TestUser:
    def test_new_user(self):
        """
        GIVEN an User Model
        WHEN an User object is instantiated
        THEN check 'name' is defined correctly 
        """
        user = User(name='max mustermann')
        assert user.name == 'max mustermann'


class TestZettel:
    def test_new_zettel(self):
        """
        GIVEN a Zettel Model
        WHEN a Zettel object is being created
        THEN check the 'luhmann_identifier', 'title', 'content' are correctly defined
        """
        zettel = Zettel(luhmann_identifier='1b', title='grey chair', content='there is a grey chair in front of me')
        assert zettel.luhmann_identifier == '1b'
        assert zettel.title == 'grey chair'
        assert zettel.content == 'there is a grey chair in front of me'

    def test_adding_zettel_link(self):
        """
        GIVEN two Zettel objects
        WHEN a Zettel is linked to the other
        THEN check 'links' and 'backlinks' are properly populated
        """
        zettel1 = Zettel(luhmann_identifier='1b', title='grey chair', content='there is a grey chair in front of me')
        zettel2 = Zettel(luhmann_identifier='1', title='chairs', content='chairs come in different shapes and colors')

        zettel1.add_outgoing_links([zettel2])

        assert zettel1.backlinks == []
        assert zettel1.links == [zettel2]
        assert zettel2.backlinks == [zettel1]
        assert zettel2.links == []


class TestZettelUpdate:
    def test_new_zettel_update(self, zettel, updated_column):
        """
        GIVEN ZettelUpdate model, a Zettel object and an UpdatedColumn object
        WHEN the ZettelUpdate object is created 
        THEN check the 'zettel', 'updated_columns', 'transferred_to_zettelkasten' fields are properly populated
        """
        zettel_update = ZettelUpdate(zettel=zettel, updated_columns=[updated_column])

        assert zettel_update.zettel == zettel
        assert zettel_update.updated_columns.__contains__(updated_column)
        assert zettel_update.transferred_to_zettelkasten == False

    def test_add_columns(self, zettel_update, updated_column):
        """
        GIVEN a ZettelUpdate object and an UpdatedColumn object
        WHEN the UpdatedColumn object is added to the ZettelUpdate object
        THEN check that 'updated_columns' contains the zettel_update object
        """
        zettel_update.add_columns(updated_columns=[updated_column])

        assert zettel_update.updated_columns.__contains__(updated_column)


class TestUpdatedColumn:
    def test_new_updated_column(self):
        """
        GIVEN the UpdatedColumn Model
        WHEN an UpdatedColumn object is being created
        THEN check 'column_name', 'old_column_value', 'new_column_value' are properly populated
        """
        updated_column = UpdatedColumn(column_name='title', old_column_value='Zettelkasten', new_column_value='The Zettelkasten')

        assert updated_column.column_name == 'title'
        assert updated_column.old_column_value == 'Zettelkasten'
        assert updated_column.new_column_value == 'The Zettelkasten'


# TODO: how to test a SQLA table object?
class TestZettelLinksAssociation:
    def test_something(self):
        pass
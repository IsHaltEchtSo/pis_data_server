from flask_wtf import FlaskForm
from pis_app.models import Zettel
from uuid import uuid4
from sqlalchemy.orm import Session


class ZettelFactory():
    """Instantiates Zettel objects using the 'create_zettel' method"""

    def __init__(self, form: FlaskForm, db_session: Session):
        self.form = form
        self.db_session = db_session


    def create_zettel(self) -> Zettel:
        zettel = self._zettel_instantiation()
        self._add_links(zettel)
        self._add_backlinks(zettel)

        return zettel


    def _zettel_instantiation(self) -> Zettel:
        zettel = Zettel(
            luhmann_identifier = self.form.luhmann_identifier.data,
            title = self.form.title.data,
            content = self.form.content.data
        )
        return zettel


    def _add_links(self, zettel: Zettel) -> None:
        if self.form.links.data:
            link_ids = [link.strip() for link in self.form.links.data.split(',')]
            for link_id in link_ids:
                link_zettel = self.db_session \
                    .query(Zettel) \
                    .filter(Zettel.luhmann_identifier == link_id) \
                    .scalar()

                # link to the zettel if it already exists
                if link_zettel:
                    zettel.links.append(link_zettel)
                # otherwise, create a placeholder zettel for the link
                else:
                    link_zettel = Zettel(luhmann_identifier=link_id, title=f"Placeholder Title: <{uuid4()}>")
                    zettel.links.append(link_zettel)


    def _add_backlinks(self, zettel: Zettel) -> None:
        if self.form.backlinks.data:
            backlink_ids = [backlink.strip() for backlink in self.form.backlinks.data.split(',')]
            for backlink_id in backlink_ids:
                backlink_zettel = self.db_session \
                    .query(Zettel) \
                    .filter(Zettel.luhmann_identifier == backlink_id) \
                    .scalar()

                # backlink to the zettel if it already exists
                if backlink_zettel:
                    zettel.backlinks.append(backlink_zettel)
                # otherwise, create a placeholder zettel for the backlink
                else: 
                    backlink_zettel = Zettel(luhmann_identifier=backlink_id, title=f"Placeholder Title: <{uuid4()}>")
                    zettel.backlinks.append(backlink_zettel)
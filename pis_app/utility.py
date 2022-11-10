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
        self._update_links(zettel)
        self._update_backlinks(zettel)

        return zettel


    def update_zettel(self, zettel: Zettel) -> Zettel:
        self._update_data(zettel)
        self._update_links(zettel, purge=True)
        self._update_backlinks(zettel, purge=True)
        return zettel


    def _zettel_instantiation(self) -> Zettel:
        zettel = Zettel(
            luhmann_id = self.form.luhmann_id.data,
            title = self.form.title.data,
            content = self.form.content.data
        )
        return zettel


    def _update_data(self, zettel: Zettel) -> None:
        if self.form.luhmann_id.data:
            zettel.luhmann_id = self.form.luhmann_id.data
        if self.form.title.data:
            zettel.title = self.form.title.data
        if self.form.content.data:
            zettel.content = self.form.content.data

    def _update_links(self, zettel: Zettel, purge=False) -> None:
        if self.form.links.data:
            if purge:
                zettel.links.clear()
            link_ids = [link.strip() for link in self.form.links.data.split(',')]
            for link_id in link_ids:
                link_zettel = self.db_session \
                    .query(Zettel) \
                    .filter(Zettel.luhmann_id == link_id) \
                    .scalar()

                # link to the zettel if it already exists
                if link_zettel:
                    zettel.links.append(link_zettel)
                # otherwise, create a placeholder zettel for the link
                else:
                    link_zettel = Zettel(luhmann_id=link_id, title=f"Placeholder Title: <{uuid4()}>")
                    zettel.links.append(link_zettel)


    def _update_backlinks(self, zettel: Zettel, purge=False) -> None:
        if self.form.backlinks.data:
            if purge:
                zettel.backlinks.clear()
            backlink_ids = [backlink.strip() for backlink in self.form.backlinks.data.split(',')]
            for backlink_id in backlink_ids:
                backlink_zettel = self.db_session \
                    .query(Zettel) \
                    .filter(Zettel.luhmann_id == backlink_id) \
                    .scalar()

                # backlink to the zettel if it already exists
                if backlink_zettel:
                    zettel.backlinks.append(backlink_zettel)
                # otherwise, create a placeholder zettel for the backlink
                else: 
                    backlink_zettel = Zettel(luhmann_id=backlink_id, title=f"Placeholder Title: <{uuid4()}>")
                    zettel.backlinks.append(backlink_zettel)



class z:
    pass
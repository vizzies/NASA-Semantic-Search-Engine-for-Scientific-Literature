from bertsearch.models import Result
from bertsearch.extensions import ma, db
from marshmallow import EXCLUDE

class ResultSchema(ma.SQLAlchemyAutoSchema):

    id = ma.Int(dump_only=True)
    text = ma.String(load_only=True)

    class Meta:
        model = Result
        sqla_session = db.session
        load_instance = True
        unknown = EXCLUDE
from flask import request
from flask_restful import Resource
from bertsearch.api.schemas import ResultSchema
from bertsearch.models import Result
from bertsearch.extensions import db
from bertsearch.commons.pagination import paginate


class ResultResource(Resource):

    def __init__(self, parser):
        self.parser = parser
        self.args = self.parser.parse_args()

    def get(self, result_id):
        schema = ResultSchema()
        result = Result.query.get_or_404(result_id)
        return {"result": schema.dump(result)}

    def put(self, result_id):
        schema = ResultSchema(partial=True)
        result = Result.query.get_or_404(result_id)
        result = schema.load(request.json, instance=result)

        db.session.commit()

        return {"msg": "result updated", "data": schema.dump(result)}

    def delete(self, result_id):
        result = Result.query.get_or_404(result_id)
        db.session.delete(result)
        db.session.commit()

        return {"msg": "result deleted"}


class ResultList(Resource):
    
    def __init__(self, parser):
        self.parser = parser
        self.args = self.parser.parse_args()
    
    def get(self):
        schema = ResultSchema(many=True)
        query = Result.query
        return paginate(query, schema)
        

    def post(self):

        schema = ResultSchema()
        result = schema.load(request.json)

        db.session.add(result)
        db.session.commit()

        return {"msg": "result created", "data": schema.dump(result)}, 201

from flask import Blueprint, current_app, jsonify
from flask_restful import Api, reqparse
import datetime as dt
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from bertsearch.api.resources import *
from bertsearch.api.schemas import *

parser = reqparse.RequestParser()

parser.add_argument("date",
                    type=lambda x: x if dt.date.fromisoformat(x) else False,
                    help="date param must be in ISO date format (YYYY-MM-DD)")
parser.add_argument("author",
                    type=str,
                    help="author param must be a string")


blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)

api.add_resource(ResultResource, "/results/<string:result_id>", 
                 endpoint="org_by_id", resource_class_kwargs={'parser': parser})

api.add_resource(ResultList, "/results",
                 endpoint="orgs_list", resource_class_kwargs={'parser': parser})



@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    """Return json error for marshmallow validation errors.

    This will avoid having to try/catch ValidationErrors in all endpoints,
    returning correct JSON response with associated HTTP 400 Status
    (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """
    return jsonify(e.messages), 400

@blueprint.errorhandler(IntegrityError)
def handle_integrity_error(e):

    """Return json error for SQL integrity errors.

    This will avoid having to try/catch ValidationErrors in all endpoints,
    returning correct JSON response with associated HTTP 400 Status
    (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """

    return str(e.orig), 400

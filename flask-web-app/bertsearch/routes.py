from flask import current_app as app_ref
from flask import request, jsonify
from reusetracker.tasks.app_tasks import start_scraper, analyze_target
from reusetracker.extensions import celery, db
from celery.app.control import Inspect

current_app = app_ref._get_current_object()



@current_app.route("/clear", methods=["GET"])
def clear_tables():
    
    db.drop_all()
    db.create_all()

    return 'All tables dropped and re-added', 200
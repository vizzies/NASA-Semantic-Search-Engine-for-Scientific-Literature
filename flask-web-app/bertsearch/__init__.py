import os
from flask import Flask
from bertsearch import api
from bertsearch.extensions import db, migrate, celery
from celery import Celery
from celery.app.task import Task as CeleryTask

def create_app(config="DevConfig"):

    app = Flask(__name__)

    app.config.from_object(f"search-api.config.{config}")
    
    with app.app_context():
        
        db.init_app(app)

        migrate.init_app(app, db=db, render_as_batch=True)

        # Include our Routes
        from . import routes

        app.register_blueprint(api.views.blueprint)

        init_celery(app)

        return app


def init_celery(app: Flask = None) -> Celery:

    app = app or create_app()

    TaskBase: CeleryTask = celery.Task

    # Initialization of instance is not here anymore
    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    # Configuration of placeholder happens here
    celery.conf.update(
        broker_url="redis://127.0.0.1:6379",
        result_backend="redis://127.0.0.1:6379",
        beat_schedule={
            "periodic_task-every-minute": {
                "task": "reusetracker.tasks.example.dummy_task",
                "schedule": crontab(minute="*"),
            }
        },
    )

    celery.Task = ContextTask

    return celery

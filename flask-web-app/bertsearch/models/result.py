from bertsearch.extensions import db


class Result(db.Model):
    """Basic user model
    """

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(5000), nullable=False)

    
    
    def __init__(self, **kwargs):
        super(Result, self).__init__(**kwargs)

    def __repr__(self):
        return f"<Result id: {self.id}, text: {self.text}"

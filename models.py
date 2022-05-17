from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    tablename = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    username = db.Column(db.String(80))
    password = db.Column(db.String(250))
    is_admin = db.Column(db.Boolean, default=False)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "is_admin": self.is_admin
        }

    def repr(self):
        return self.name

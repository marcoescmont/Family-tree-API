from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }


Harrison = {
    "name": "Harrison",
    "id": 6,
    "children": []
}

Charlotte = {
    "name": "Charlotte",
    "id": 5,
    "children": []
}

Harry = {
    "name": "Harry",
    "id": 4,
    "children": [Harrison]
}

William = {
    "name": "William",
    "id": 3,
    "children": [Charlotte]
}

Charles = {
    "name": "Charles",
    "id": 2,
    "children": [William, Harry]
}

Queen = {
    "name": "Elizabeth",
    "id": 1,
    "children": [Charles]
}

desired_name = []

def list_all(parent):
    for child in parent["children"]:
        desired_name.append(child)
        list_all(child)
    return desired_name
    

def find_one(parent, id):
    for child in parent["children"]:
        if child["id"] == id:
            return child
        return find_one(child, id)

print(find_one(Queen, 3))
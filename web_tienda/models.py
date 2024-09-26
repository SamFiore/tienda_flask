from database import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    desc = db.Column(db.String(400))
    price = db.Column(db.Integer)

    def __str__(self):
        return (f'ID:{self.id}' f'Nombre:{self.name}' f'Descripcion:{self.desc}' f'precio:{self.price}')
from diagno import db


class Item(db.Model):
  __tablename__ = "items"
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(length=30), nullable=False, unique=True)
  price = db.Column(db.Integer(), nullable=False)
  barcode = db.Column(db.String(length=12), nullable=False, unique=True)
  description = db.Column(db.String(length=1024), nullable=False, unique=True)

  def __repr__(self):
    return f'Item {self.name}'


from app import db

class WayfairManualProcesseds(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    EstokPsku = db.Column(db.String(50))
    WayfairPartNumber = db.Column(db.String(50))
    Created_At = db.Column(db.DateTime)
    Updated_At = db.Column(db.DateTime)

    def __init__(self, EstokPsku, WayfairPartNumber, Created_At):
        self.EstokPsku = EstokPsku
        self.WayfairPartNumber = WayfairPartNumber
        self.Created_At = Created_At

    def __repr__(self):
        return f'<PO {self.EstokPsku}>'

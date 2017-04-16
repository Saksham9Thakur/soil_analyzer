from app import db
class Mitti(db.Model):	
	time=db.Column(db.DateTime,primary_key=True)
	SoilMositure = db.Column(db.Float,nullable=False )
	Humidity = db.Column(db.Float, nullable=False)
	Temperature= db.Column(db.Float,nullable=False)
	ph=db.Column(db.Float,nullable=False)
	def __init__(self, time, SoilMositure,Humidity,Temperature,ph):
		self.time = time
		self.SoilMositure =SoilMositure
		self.Humidity = Humidity
		self.Temperature = Temperature
		self.ph = ph
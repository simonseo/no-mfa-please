from app.db.create_tables import create_tables

def check_tables_exists(f):
	def wrapper(*args, **kwargs):
		create_tables()
		f(*args, **kwargs)
	return wrapper

from app.db.insert_user import insert_user
from app.db.get_user import get_user


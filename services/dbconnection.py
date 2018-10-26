from sqlalchemy import create_engine
from sqlalchemy.engine import url

from django.conf import settings

class DBConnection(object):
	"""Class that represents a DB Connection"""

	DB_DRIVERS = (

		('db_mysql', 'mysql'),
		('db_pgsql', 'postgresql'),
		('db_oracle', 'oracle'),
		('db_mssql', 'mssql'),
		('db_sqlite', 'sqlite'),
	)

	def connect(self, drivername, database, host, port=None, username=None, password=None):
		"""
		Connect to a remote host via SSH tunnel with provided credentials

		Parameters
		----------
		drivername :  str
			DB driver name (one of DBConnection.DB_DRIVERS)
		database : str
			DB name
		host : str
			URI/IP of the DB host
		port : int
			Port no. to which the DB host listens to
		username : str
			DB User name
		password : str
			DB password

		Returns
		-------
		sqlalchemy.engine.Connection
			An object of type sqlalchemy.engine.Connection
		"""

		db_url = url.URL(drivername, username, password, host, port, database)

		pool_options = dict()
		pool_options['pool_size'] = settings.DB_POOL['SIZE']
		pool_options['max_overflow'] = settings.DB_POOL['MAX_OVERFLOW']
		pool_options['pool_recycle'] = settings.DB_POOL['TIMEOUT']

		engine = create_engine(db_url, **pool_options)

		return engine
	
		
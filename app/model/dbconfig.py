from django.db import models

class DBConfig(models.Model):
	"""Model representing a DB configuration"""
	
	DB_TYPE_CHOICES = (

		('db_mysql', 'MySQL'),
		('db_pgsql', 'PostgreSQL'),
		('db_oracle', 'Oracle'),
		('db_mssql', 'MS SQL'),
		('db_sqlite', 'SQLite'),
	)

	# Fields
	connection_name = models.CharField(max_length=100, help_text='Display name of DB connection')
	db_type = models.CharField(
									max_length=50,
									help_text='Type of database',
									choices = DB_TYPE_CHOICES, 
									default = 'mysql',
								)
	db_host = models.CharField(max_length=300, help_text='DB host')
	db_port = models.IntegerField(help_text='DB host port')

	db_name = models.CharField(max_length=100, help_text='Database name')
	db_username = models.CharField(max_length=100, help_text='Database user name')
	db_password = models.CharField(max_length=30, help_text='Database password')

	ssh_host = models.CharField(max_length=300, help_text='SSH host', blank=True)
	ssh_port = models.IntegerField(default=22, help_text='SSH host port', blank=True)
	ssh_username = models.CharField(max_length=100, help_text='SSH user name', blank=True)
	ssh_password = models.CharField(max_length=30, help_text='SSH password', blank=True)

	#Methods
	def __str__(self):
		"""Returns name of Connections name"""
		return self.connection_name

	def get_absolute_url(self):
		"""Returns the url to access a detail record for this DB connection."""
		return reverse('db-detail', args=[str(self.id)])

	def props(self):
		"""Returns properties of DBConfig object"""
		p = {
			'connection_name': self.connection_name,
			'db_type': self.db_type,
			'db_host': self.db_host,
			'db_port': self.db_port,
			'db_name': self.db_name,
			'db_username': self.db_username,
			'db_password': self.db_password,
			'ssh_host': self.ssh_host,
			'ssh_port': self.ssh_port,
			'ssh_username': self.ssh_username,
			'ssh_password': self.ssh_password
		}
		return p
		
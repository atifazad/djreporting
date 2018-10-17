import paramiko
from sshtunnel import SSHTunnelForwarder

from django.conf import settings

class SSHTunnel(object):
	"""Class that represents a connection to remote server via SSH tunneling"""
	
	def connect(self, host, port, username, password, remote_host, remote_port):
		"""
		Connect to a remote host via SSH tunnel with provided credentials

		Parameters
		----------
		host : str
			URI/IP of the SSH host
		port : int
			Port no. to which the SSH host listens to
		username : str
			SSH User name
		password : str
			SSH password
		remote_host : str
			URI/IP of the remote server to which to tunnel
		remote_port :  int
			Port no. to which the remote server listens to.

		Returns
		-------
		SSHTunnelForwarder
			An object of type SSHTunnelForwarder
		"""

		self.server = SSHTunnelForwarder(
		    (host, port),
		    ssh_host_key = None,
		    ssh_username = username,
		    ssh_password = None,
		    ssh_private_key = settings.SSH_PRIVATE_KEY,
		    # ssh_private_key_password="pssrd",
		    remote_bind_address=(remote_host, remote_port))

		self.server.start()

		return self.server

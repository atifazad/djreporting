from django.db import models

class Report(models.Model):
	""" Model represnting a Report (A database query) """

	title = models.CharField(max_length=300, help_text='Title of the report')
	query = models.TextField(help_text='Database query to generate report')

	#Methods
	def __str__(self):
		"""Returns title of Report"""
		return self.title

	def get_absolute_url(self):
		"""Returns the url to access a detail record for this Report."""
		return reverse('report-detail', args=[str(self.id)])

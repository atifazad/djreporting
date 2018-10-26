from django.contrib import admin
from app.models import DBConfig
from app.forms import DBConfigForm

class DBConfigAdmin(admin.ModelAdmin):
	"""DB connection form for admin"""
	form = DBConfigForm
		

# Register your models here.
admin.site.register(DBConfig, DBConfigAdmin)

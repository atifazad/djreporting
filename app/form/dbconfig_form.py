from app.model.dbconfig import DBConfig
from django.forms import ModelForm, PasswordInput

class DBConfigForm(ModelForm):
	"""Admin form to save a DBConfig"""

	class Meta:
		model = DBConfig
		widgets = {
            'db_password': PasswordInput(),
            'ssh_password': PasswordInput(),
        }
		exclude=['id']

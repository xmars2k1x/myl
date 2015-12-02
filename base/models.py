from django.contrib.auth.models import User
from django.db import models
from jsonfield import JSONField
import json

def default_json():
	to_json = {
		'utilizable': False,
		'nombre': None,
		'cartas': {}
	}

	for i in range(0, 50):
		to_json['cartas'][str('c%s' % i)] = None

	return json.dumps(to_json)

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	mazo_de_cartas = JSONField(default=default_json(), editable=False)

from django.conf import settings

def test(request):
	test = 'this is a test'
	return { 'test': test }

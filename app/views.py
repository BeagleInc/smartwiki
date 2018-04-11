import json
from urllib2 import urlopen

from django.http import JsonResponse

API_URL = 'http://api.research.beagle.ai:8005/most_similar/model={}&word={}&user=Beagle&password=GreatBeagleAI&number={}'


def relatedness(request):
    url = API_URL.format(
        request.GET['model'],
        request.GET['word'],
        request.GET['number'],
    )
    response = urlopen(url)

    return JsonResponse(json.loads(response.read()))

import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from channels import Group

@csrf_exempt
def display(request):
    if request.method != "POST":
        return HttpResponse(status=405)
    
    json_data = json.loads(request.body.decode('utf-8'))
    Group(json_data['group']).send({"text": json.dumps(json_data['data'])})

    return HttpResponse(status=200)



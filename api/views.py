from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET'])
def send(request):
    num_1=int(request.query_params['id'])
    num_2=int(request.query_params['pk'])
    result=num_1+num_2
    return Response({result})



def hello(request):
    
    return HttpResponse('<p><h1>do this in link after</h1> <strong>/api/?id=1&pk=2</strong></p>')
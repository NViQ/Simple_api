from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Log
from .serializers import LogSerializer
from django.views.generic import ListView


class LogListView(ListView):
    model = Log
    template_name = 'log_list.html'
    context_object_name = 'logs'


@api_view(['POST'])
def process_request(request):
    request_data = request.data.get('question', '')

    log = Log(request_data=request_data, response_data="Hello, I'm fine")
    log.save()

    serializer = LogSerializer(log)

    return Response(serializer.data, status=status.HTTP_200_OK)

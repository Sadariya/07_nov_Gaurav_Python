from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import event_model
from .serializers import event_serializers
from rest_framework import status

# Create your views here.


def index(request):
    if request.method == 'POST':
        id=request.POST['userid']
        print (id)
    return render(request, 'index.html')


@api_view(['GET'])
def apiweb(request):

    userdata = event_model.objects.all()
    data_serialixzers = event_serializers(userdata, many=True)

    return Response(data_serialixzers.data)


@api_view(['GET'])
def get_specific_data(request, id):

    userdata = event_model.objects.get(id=id)
    data_serializer = event_serializers(userdata)

    return Response(data_serializer.data)


@api_view(['POST'])
def adddata(request):

    if request.method == 'POST':
        data_serialixzers = event_serializers(data=request.data)
        if data_serialixzers.is_valid():
            data_serialixzers.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def deletedata(request, id):
    try:
        userid = event_model.objects.get(id=id)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        data_serializers = event_serializers(userid)
        return Response(data_serializers.data)
    if request.method == 'DELETE':
        userid.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    

@api_view(['GET', 'PUT'])
def updatedata(request, id):
    try:
        userid = event_model.objects.get(id=id)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        data_serializers = event_serializers(userid)
        return Response(data_serializers.data)
    if request.method == 'PUT':
        data_update = event_serializers(data=request.data,instance=userid)
        if data_update.is_valid():
            data_update.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else :
            return Response(status=status.HTTP_304_NOT_MODIFIED)

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import images
from .serializers import FileSerializer
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response

class ImageViewSet(viewsets.ModelViewSet):
    queryset = images.objects.all()
    serializer_class = FileSerializer

class ShowImage(APIView):
    def get(self,request):
        image_list = images.objects.all()
        image_ret = {}
        id = request.data.get('userid')
        cnt = 0
        for i in image_list:
            if (id is None) or (id == i.upload_by):
                image_ret[str(cnt)] = settings.BACKEND_URL + i.img.url
                cnt += 1
        return Response({
                'status': True,
                'data': image_ret,
            })

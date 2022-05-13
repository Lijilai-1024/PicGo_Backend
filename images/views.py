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
    def post(self,request):
        image_list = images.objects.all()
        image_ret = {}
        userid = request.data.get('userid')
        cnt = 0
        for i in image_list:
            if (userid is not None) and (userid == i.upload_by):
                image_ret[str(cnt)] = str(i.id)
                image_ret[str(cnt + 1)] = settings.BACKEND_URL + i.img.url
                cnt += 2
        return Response({
                'status': True,
                'data': image_ret,
            })

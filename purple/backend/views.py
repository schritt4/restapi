from rest_framework import status
from rest_framework.views import APIView
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
from rest_framework.response import Response
from django.http import Http404
import os


from .serializers import CurationSerializer, PlaceSerializer
from .models import Curation, Place

class CurationList(APIView):    
    def get(self, request):    # Curation 리스트 보여주기
        curations = Curation.objects.all()
        serializer = CurationSerializer(curations, many=True, context={'request':request})   # 여러개의 객체를 serialize하려면 many=True
        return Response(serializer.data)

class CurationDetail(APIView):
    def get_object(self, pk):   # Curation 객체 가져오기
        try:
            return Curation.objects.get(pk=pk)
        except Curation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        curations = self.get_object(pk)
        serializer = CurationSerializer(curations, context={'request':request})
        return Response(serializer.data)

class SearchView(APIView):
    def get(self, request):
        if not 'loc_id' in request.GET and not 'cat_id' in request.GET and not 'pur1_id' in request.GET and not 'pur2_id' in request.GET:
            places = Place.objects.all()
            serializer = PlaceSerializer(places, many=True)
            return Response(serializer.data)

        loc=request.GET.get('loc_id', None)
        cat=request.GET.get('cat_id', None)
        pur1=request.GET.get('pur1_id', None)
        pur2=request.GET.get('pur2_id', None)
        
        if pur1:
            places = Place.objects.filter(loc_id=loc, cat_id=cat, pur1_id=pur1)
            serializer = PlaceSerializer(places, many=True)
            return Response(serializer.data)
        else:
            places = Place.objects.filter(loc_id=loc, cat_id=cat, pur2_id=pur2)
            serializer = PlaceSerializer(places, many=True)
            return Response(serializer.data)

class PlaceDetail(APIView):
    def get_object(self, pk):   # Curation 객체 가져오기
        try:
            return Place.objects.get(pk=pk)
        except Place.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        places = self.get_object(pk)
        serializer = PlaceSerializer(places, context={'request':request})
        return Response(serializer.data)

class ReactAppView(View):

    def get(self, request):
        try:
            with open(os.path.join(str(settings.ROOT_DIR),
                                    'front',
                                    'build',
                                    'index.html')) as file:
                return HttpResponse(file.read())

        except:
            return HttpResponse(status=501,)
from django.shortcuts import render
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .models import Category,Profile,Sport,Comment
from .serializers import CategorySerializer,SportSerializer,UserSerializer
from rest_framework import filters
from rest_framework import generics,status
from .permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
# Create your views here.

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)


class CategoryAPIView(APIView):
    def get(self,request,format=None):
        all_category = Category.objects.all()
        serializers = CategorySerializer(all_category,many=True)
        return Response(serializers.data)


class SportAPIView(APIView):
    permission_class = (IsAuthenticatedOrReadOnly,)
    def get(self,request,format=None):
        all_sports = Sport.objects.all()
        serializer = SportSerializer(all_sports,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializers = SportSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


# class CategoryDescription(APIView):
#     def get_category_data(self,name):
#         try:
#             return Category.objects.filter(name = name)
#         except Category.DoesNotExist:
#             return Http404
        
#     def get(self,request,name,format=None):
#         categories = self.get_category_data(name)
#         serializer = CategorySerializer(categories)
#         return Response(serializer.data)

class SearchSportAPIView(generics.ListCreateAPIView):
    search_fields = ['sport_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
            






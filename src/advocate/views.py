from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    LinkSerializer,
    SignupSerializer,
    AdvocateUpdateSerializer,
    LinkRequestBodySerializer,
    AdvocateResponseSerializer,
)
from .models import (
    Advocate,
)
from utils.token_utils import get_tokens_for_user
from utils.link_utils import add_advocate_to_links
from utils.pagination_utils import CustomPagination

# Create your views here.
class Signup(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            advocate = serializer.save()
            data = {
                'advocate': serializer.data,
                'token': get_tokens_for_user(advocate)
            }
            return Response(data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class UpdateAdvocateBioView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        advocate = request.user
        serializer = AdvocateUpdateSerializer(advocate, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class AddLinksView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request_body = request.data.copy()
        advocate = request.user
        request_serializer = LinkRequestBodySerializer(data=request_body)
        if not request_serializer.is_valid():
            return Response(request_serializer.errors, status.HTTP_400_BAD_REQUEST)
        print(request_serializer.data)
        links = add_advocate_to_links(request_serializer.data['links'], advocate.id)
        serializer = LinkSerializer(data=links, many=True)
        if not serializer.is_valid():
            return Response(request_serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class AdvocateView(APIView, CustomPagination):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = Advocate.objects.all()
        result_page = self.paginate_queryset(queryset, request)
        serializer = AdvocateResponseSerializer(result_page, many=True)
        paginated_data = self.get_paginated_response(serializer.data)
        return Response(paginated_data, status.HTTP_200_OK)

class AdvocateDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        advocate = Advocate.objects.filter(pk=pk).first()
        if not advocate:
            return Response('Advocate with given id not found.', status.HTTP_404_NOT_FOUND)
        serializer = AdvocateResponseSerializer(advocate)
        return Response(serializer.data, status.HTTP_200_OK)
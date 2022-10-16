from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    LinkSerializer,
    SignupSerializer,
    AdvocateUpdateSerializer,
    LinkRequestBodySerializer,
)
from utils.token_utils import get_tokens_for_user
from utils.link_utils import add_advocate_to_links

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
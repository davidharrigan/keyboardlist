from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import DataIngestionSerializer


class DataIngestionView(APIView):
    """
    Ingest keyboard listing information from miners into the API.

    TODO: authentication
    """

    def post(self, request, format=None):
        serializer = DataIngestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({'data_ingestion': 'success'}, status_code=status.HTTP_201_CREATED)

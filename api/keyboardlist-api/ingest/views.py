from rest_framework.views import APIView
from rest_framework.response import Response


class DataIngestionView(APIView):
    """
    Ingest keyboard listing information from miners into the API.

    TODO: authentication
    """

    def post(self, request, format=None):
        pass

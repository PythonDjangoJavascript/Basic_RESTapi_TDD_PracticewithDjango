from rest_framework.views import APIView

# Response send data as Json
from rest_framework.response import Response
from rest_framework import status

from user import serializers


# This just to understand the sceleton of APIView
class HelloAPIView(APIView):
    """This is to test how we can use APIView in ouer API"""
    """We can define get, post, put, patch and delete http request here"""

    # Serializer allow as to tell api which data it should expect
    # And also conver the data to python object
    serializer_class = serializers.HelloApiSerializer

    def get(self, request, formant=None):
        """This get method returns a list of APIView features"""

        apiview_features = [
            'Uses HTTM methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over application logic',
            'Is mapped manually to URLs'
        ]

        return Response({
            "message": "Hello!",
            "APIView_features": apiview_features
        })

    def post(self, request):
        """create completely new object here create hello message with our name
            which we defined in hello serializer"""

        serializer = self.serializer_class(data=request.data)

        # serializer also allow us to validated data
        # Rulles that we defined at serialilzer class (here helloApiserializer)
        if serializer.is_valid():

            name = serializer.validated_data.get("name")
            is_employed = serializer.validated_data.get("is_employed")
            occupation = serializer.validated_data.get("occupation")

            return Response({
                "Name": f"Hello, {name}",
                "Is_employed": is_employed,
                "Occupation": occupation
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    # Here we need to specify pk as by default post request expect a pk to
    # select the item and completely update that object
    def put(self, request, pk=None):
        """Handle completely updating an object"""
        return Response({"method": "PUT", })

    def patch(self, request, pk=None):
        """Handles a partial update of an object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({"method": "Delete"})

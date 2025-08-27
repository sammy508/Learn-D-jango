from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def post_list(request):
    data = [
        {"id": 1, "title": "Hello World", "body": "First post content"},
        {"id": 2, "title": "Another Post", "body": "More content"}
    ]
    return Response(data)

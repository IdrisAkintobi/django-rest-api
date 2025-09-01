from rest_framework.response import Response
from rest_framework.decorators import api_view


#  Health check
@api_view(["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD"])
def health_check(request):
    return Response({"status": "ok"})

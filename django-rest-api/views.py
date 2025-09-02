from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema


#  Health check
@extend_schema(
    responses={"200": {"type": "object", "properties": {"status": {"type": "string"}}}}
)
@api_view(["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD"])
def health_check(request):
    return Response({"status": "ok"})

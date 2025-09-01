from rest_framework.pagination import LimitOffsetPagination

class CustomLimitOffsetPagination(LimitOffsetPagination):
    # Default items per request (fallback if ?limit is not given)
    default_limit = 20  

    # Maximum items allowed per request (protects DB)
    max_limit = 100  

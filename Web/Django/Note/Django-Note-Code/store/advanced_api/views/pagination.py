from rest_framework.pagination import PageNumberPagination


"""重写PageNumberPagination"""
class DefaultPagination(PageNumberPagination):
  page_size = 10
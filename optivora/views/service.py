# views/service.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from optivora.filterset import ServiceFilter
from optivora.models import Service
from optivora.serializers import ServiceSerializer

from restapp.pagination import ResultsSetPagination
from restapp.utils.responses import nonContent


class ServiceFieldInfoView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        field_info = []
        for field in Service._meta.fields:
            field_info.append({
                "field_name": field.name,
                "verbose_name": str(field.verbose_name),
                "help_text": str(field.help_text) if field.help_text else "",
                "type": field.get_internal_type(),
                "max_length": getattr(field, 'max_length', None),
                "choices": dict(field.choices) if field.choices else None
            })
        return Response(field_info)


class ServiceViewList(ListCreateAPIView):
    serializer_class = ServiceSerializer
    pagination_class = ResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filterset_class = ServiceFilter
    search_fields = ('name', 'description')
    ordering = ['pk']
    permission_classes = (AllowAny,)
    http_method_names = ['get']

    def get_queryset(self):
        return Service.objects.all()


class ServiceView(ListCreateAPIView):
    serializer_class = ServiceSerializer
    pagination_class = ResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filterset_class = ServiceFilter
    search_fields = (
        'name', 'name_en', 'name_uz', 'name_ru',
        'short_description', 'short_description_en', 'short_description_uz', 'short_description_ru',
        'description', 'description_en', 'description_uz', 'description_ru',
        'slug',
    )
    ordering = ['order_index', 'pk']

    def get_queryset(self):
        return Service.objects.all()

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=self.request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)


class ServiceDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return Service.objects.all()

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def get(self, request, pk):
        instance = get_object_or_404(Service, id=pk)
        serializer = ServiceSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        instance = get_object_or_404(Service, id=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=self.request.user)
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def delete(self, request, pk):
        instance = get_object_or_404(Service, id=pk)
        instance.delete()
        return Response(nonContent(), status.HTTP_204_NO_CONTENT)

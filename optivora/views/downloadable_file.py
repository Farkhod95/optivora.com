# views/downloadable_file.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from optivora.filterset import DownloadableFileFilter
from optivora.models import DownloadableFile
from optivora.serializers import DownloadableFileSerializer

from restapp.pagination import ResultsSetPagination
from restapp.utils.responses import nonContent


class DownloadableFileFieldInfoView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        field_info = []
        for field in DownloadableFile._meta.fields:
            field_info.append({
                "field_name": field.name,
                "verbose_name": str(field.verbose_name),
                "help_text": str(field.help_text) if field.help_text else "",
                "type": field.get_internal_type(),
                "max_length": getattr(field, 'max_length', None),
                "choices": dict(field.choices) if field.choices else None
            })
        return Response(field_info)


class DownloadableFileViewList(ListCreateAPIView):
    serializer_class = DownloadableFileSerializer
    pagination_class = ResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filterset_class = DownloadableFileFilter
    search_fields = ('title', 'description')
    ordering = ['pk']
    permission_classes = (AllowAny,)
    http_method_names = ['get']

    def get_queryset(self):
        return DownloadableFile.objects.all()


class DownloadableFileView(ListCreateAPIView):
    serializer_class = DownloadableFileSerializer
    pagination_class = ResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filterset_class = DownloadableFileFilter
    search_fields = (
        'title', 'title_en', 'title_uz', 'title_ru', 'title_lt',
        'description', 'description_en', 'description_uz', 'description_ru', 'description_lt',
    )
    ordering = ['pk']

    def get_queryset(self):
        return DownloadableFile.objects.all()

    def post(self, request):
        serializer = DownloadableFileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=self.request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)


class DownloadableFileDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = DownloadableFileSerializer

    def get_queryset(self):
        return DownloadableFile.objects.all()

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def get(self, request, pk):
        instance = get_object_or_404(DownloadableFile, id=pk)
        serializer = DownloadableFileSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        instance = get_object_or_404(DownloadableFile, id=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=self.request.user)
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def delete(self, request, pk):
        instance = get_object_or_404(DownloadableFile, id=pk)
        instance.delete()
        return Response(nonContent(), status.HTTP_204_NO_CONTENT)

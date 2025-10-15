# views/project_image.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from optivora.filterset import ProjectImageFilter
from optivora.models import ProjectImage
from optivora.serializers import ProjectImageSerializer

from restapp.pagination import ResultsSetPagination
from restapp.utils.responses import nonContent


class ProjectImageFieldInfoView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        field_info = []
        for field in ProjectImage._meta.fields:
            field_info.append({
                "field_name": field.name,
                "verbose_name": str(field.verbose_name),
                "help_text": str(field.help_text) if field.help_text else "",
                "type": field.get_internal_type(),
                "max_length": getattr(field, 'max_length', None),
                "choices": dict(field.choices) if field.choices else None
            })
        return Response(field_info)

class ProjectImageViewList(ListCreateAPIView):
    serializer_class = ProjectImageSerializer
    pagination_class = ResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filterset_class = ProjectImageFilter
    search_fields = ('caption', 'caption_en')
    ordering = ['pk']
    permission_classes = (AllowAny,)
    http_method_names = ['get']

    def get_queryset(self):
        return ProjectImage.objects.all()


class ProjectImageView(ListCreateAPIView):
    serializer_class = ProjectImageSerializer
    pagination_class = ResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filterset_class = ProjectImageFilter
    search_fields = ('caption', 'caption_en', 'caption_uz', 'caption_ru')
    ordering = ['order_index', 'pk']

    def get_queryset(self):
        return ProjectImage.objects.select_related('project').all()

    def post(self, request):
        serializer = ProjectImageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=self.request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)


class ProjectImageDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectImageSerializer

    def get_queryset(self):
        return ProjectImage.objects.all()

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def get(self, request, pk):
        instance = get_object_or_404(ProjectImage, id=pk)
        serializer = ProjectImageSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        instance = get_object_or_404(ProjectImage, id=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=self.request.user)
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def delete(self, request, pk):
        instance = get_object_or_404(ProjectImage, id=pk)
        instance.delete()
        return Response(nonContent(), status.HTTP_204_NO_CONTENT)

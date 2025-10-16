# views/project_deliverable.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from optivora.filterset import ProjectDeliverableFilter
from optivora.models import ProjectDeliverable
from optivora.serializers import ProjectDeliverableSerializer

from restapp.pagination import ResultsSetPagination
from restapp.utils.responses import nonContent


class ProjectDeliverableFieldInfoView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        field_info = []
        for field in ProjectDeliverable._meta.fields:
            field_info.append({
                "field_name": field.name,
                "verbose_name": str(field.verbose_name),
                "help_text": str(field.help_text) if field.help_text else "",
                "type": field.get_internal_type(),
                "max_length": getattr(field, 'max_length', None),
                "choices": dict(field.choices) if field.choices else None
            })
        return Response(field_info)


class ProjectDeliverableViewList(ListCreateAPIView):
    serializer_class = ProjectDeliverableSerializer
    pagination_class = ResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filterset_class = ProjectDeliverableFilter
    search_fields = ('name',)
    ordering = ['pk']
    permission_classes = (AllowAny,)
    http_method_names = ['get']

    def get_queryset(self):
        return ProjectDeliverable.objects.all()

class ProjectDeliverableView(ListCreateAPIView):
    serializer_class = ProjectDeliverableSerializer
    pagination_class = ResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filterset_class = ProjectDeliverableFilter
    search_fields = ('name',)
    ordering = ['pk']

    def get_queryset(self):
        return ProjectDeliverable.objects.select_related('project').all()

    def post(self, request):
        serializer = ProjectDeliverableSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=self.request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)


class ProjectDeliverableDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectDeliverableSerializer

    def get_queryset(self):
        return ProjectDeliverable.objects.all()

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def get(self, request, pk):
        instance = get_object_or_404(ProjectDeliverable, id=pk)
        serializer = ProjectDeliverableSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        instance = get_object_or_404(ProjectDeliverable, id=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=self.request.user)
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def delete(self, request, pk):
        instance = get_object_or_404(ProjectDeliverable, id=pk)
        instance.delete()
        return Response(nonContent(), status.HTTP_204_NO_CONTENT)

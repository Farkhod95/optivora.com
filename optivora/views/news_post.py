# views/news_post.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from optivora.filterset import NewsPostFilter
from optivora.models import NewsPost
from optivora.serializers import NewsPostSerializer

from restapp.pagination import ResultsSetPagination
from restapp.utils.responses import nonContent


class NewsPostFieldInfoView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        field_info = []
        for field in NewsPost._meta.fields:
            field_info.append({
                "field_name": field.name,
                "verbose_name": str(field.verbose_name),
                "help_text": str(field.help_text) if field.help_text else "",
                "type": field.get_internal_type(),
                "max_length": getattr(field, 'max_length', None),
                "choices": dict(field.choices) if field.choices else None
            })
        return Response(field_info)


class NewsPostViewList(ListCreateAPIView):
    serializer_class = NewsPostSerializer
    pagination_class = ResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filterset_class = NewsPostFilter
    search_fields = ('title', 'excerpt')
    ordering = ['pk']
    permission_classes = (AllowAny,)
    http_method_names = ['get']

    def get_queryset(self):
        return NewsPost.objects.all()


class NewsPostView(ListCreateAPIView):
    serializer_class = NewsPostSerializer
    pagination_class = ResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filterset_class = NewsPostFilter
    search_fields = (
        'title', 'title_en', 'title_uz', 'title_ru',
        'excerpt', 'excerpt_en', 'excerpt_uz', 'excerpt_ru',
        'body', 'body_en', 'body_uz', 'body_ru',
        'slug',
    )
    ordering = ['-published_at', 'pk']

    def get_queryset(self):
        return NewsPost.objects.all()

    def post(self, request):
        serializer = NewsPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=self.request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)


class NewsPostDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = NewsPostSerializer

    def get_queryset(self):
        return NewsPost.objects.all()

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def get(self, request, pk):
        instance = get_object_or_404(NewsPost, id=pk)
        serializer = NewsPostSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        instance = get_object_or_404(NewsPost, id=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=self.request.user)
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def delete(self, request, pk):
        instance = get_object_or_404(NewsPost, id=pk)
        instance.delete()
        return Response(nonContent(), status.HTTP_204_NO_CONTENT)


class NewsPostDetailPublicView(RetrieveUpdateDestroyAPIView):
    serializer_class = NewsPostSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get']

    def get_queryset(self):
        return NewsPost.objects.all()

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def get(self, request, pk):
        instance = get_object_or_404(NewsPost, id=pk)
        serializer = NewsPostSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

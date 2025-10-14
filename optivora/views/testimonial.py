# views/testimonial.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from optivora.filterset import TestimonialFilter
from optivora.models import Testimonial
from optivora.serializers import TestimonialSerializer

from restapp.pagination import ResultsSetPagination
from restapp.utils.responses import nonContent


class TestimonialFieldInfoView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        field_info = []
        for field in Testimonial._meta.fields:
            field_info.append({
                "field_name": field.name,
                "verbose_name": str(field.verbose_name),
                "help_text": str(field.help_text) if field.help_text else "",
                "type": field.get_internal_type(),
                "max_length": getattr(field, 'max_length', None),
                "choices": dict(field.choices) if field.choices else None
            })
        return Response(field_info)


class TestimonialView(ListCreateAPIView):
    serializer_class = TestimonialSerializer
    pagination_class = ResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filterset_class = TestimonialFilter
    search_fields = (
        'author_name',
        'author_role', 'author_role_en', 'author_role_uz', 'author_role_ru',
        'company', 'company_en', 'company_uz', 'company_ru',
        'quote', 'quote_en', 'quote_uz', 'quote_ru',
    )
    ordering = ['-is_featured', 'pk']

    def get_queryset(self):
        return Testimonial.objects.all()

    def post(self, request):
        serializer = TestimonialSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=self.request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)


class TestimonialDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TestimonialSerializer

    def get_queryset(self):
        return Testimonial.objects.all()

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def get(self, request, pk):
        instance = get_object_or_404(Testimonial, id=pk)
        serializer = TestimonialSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        instance = get_object_or_404(Testimonial, id=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=self.request.user)
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def delete(self, request, pk):
        instance = get_object_or_404(Testimonial, id=pk)
        instance.delete()
        return Response(nonContent(), status.HTTP_204_NO_CONTENT)

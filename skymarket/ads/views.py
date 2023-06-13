from django.shortcuts import get_object_or_404
from rest_framework import pagination, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Comment, Ad
from .permissions import IsOwner
from .serializers import AdSerializer, CommentSerializer, AdDetailSerializer


class AdPagination(pagination.PageNumberPagination):
    # Количество элементов на одной странице
    page_size = 4

    # Параметр, который указывает на максимальное количество элементов, которое можно отобразить на одной странице
    max_page_size = 4



class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return AdDetailSerializer
        else:
            return AdSerializer

    def get_permission(self):
        if self.action in ['update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsAdminUser | IsOwner]
        return super().get_permission()


    @action(detail=False)
    def me(self, request, *args, **kwargs):
        self.queryset = Ad.objects.filter(author=request.user)
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        ad_id = self.kwargs.get('ad_pk')
        return Comment.objects.filter(ad_id=ad_id)

    def perform_create(self, serializer):
        ad_id = self.kwargs.get('ad_pk')
        ad_instance = get_object_or_404(Ad, pk=ad_id)
        user_id = self.request.user
        serializer.save(author=user_id, ad=ad_instance)

from django.urls import include, path
from rest_framework import routers
from rest_framework_nested.routers import NestedSimpleRouter

from .views import AdViewSet, CommentViewSet

ads_router = routers.SimpleRouter()
ads_router.register('ads', AdViewSet, basename="ads")
comments_router = NestedSimpleRouter(ads_router, "ads", lookup="ad")
comments_router.register('comments', CommentViewSet)

urlpatterns = [
    path("", include(ads_router.urls)),
    path("", include(comments_router.urls)),
    # # path('comments/create/', CommentViewSet.as_view(), name='comment-create')

]

# urlpatterns += router.urls
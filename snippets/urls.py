from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

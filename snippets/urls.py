
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^snippets_recommlist/$',views.snippets_recommlist),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
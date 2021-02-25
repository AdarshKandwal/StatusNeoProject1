from django.urls import path
from .views import ArticleAPIView, ArticleDetails
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
 
 
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),
 
]

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
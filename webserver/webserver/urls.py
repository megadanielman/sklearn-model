from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('analysis/', include('analysis.urls')),
    path('admin/', admin.site.urls),
]

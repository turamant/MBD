from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from django.contrib import admin
from django.urls import path, include


schema_view = get_schema_view(title='Movie Api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('core.urls')),
    path('user/',include('user.urls')),
    path('docs/',include_docs_urls(title='Movie Api')),
    path('schema/',schema_view),
    path('',include('core.urls')),
]

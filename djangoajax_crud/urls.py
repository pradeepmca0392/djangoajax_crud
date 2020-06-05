"""djangoajax_crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from courses import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', TemplateView.as_view(template_name="main.html"), name='course_main'),
    path('list', views.CourseList.as_view(), name='course_list'),
    path('create', views.CourseCreate.as_view(), name='course_create'),
    path('update/<int:pk>', views.CourseUpdate.as_view(), name='course_update'),
    path('delete/<int:pk>', views.CourseDelete.as_view(), name='course_delete'),
    path('courses/<int:pk>', views.CourseDetail.as_view(), name='course_detail'),
]
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
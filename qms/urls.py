from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('quiz/', include('quizzes.urls')),
    path('', lambda request: redirect('quiz_list')),  # redirect root to quiz list
]

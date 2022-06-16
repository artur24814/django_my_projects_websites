"""dictionary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings

from django.conf.urls.static import static

from words import views
from accounts.views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', RegisterView.as_view()),
    path('dictionary/', views.Dictionary.as_view()),
    path('card-game/', views.CadrdGame.as_view()),
    path('user-dictionary/', views.UserDictionary.as_view()),
    path('update_word/<int:id>/', views.update_word),
    path('update_word/<int:id>/delete/', views.delete_word),
    path('user-card-game/', views.UserCadrdGame.as_view()),
    path('frasses/', views.FrassesView.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
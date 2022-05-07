"""cinema URL Configuration

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

from films import views
from accounts.views import LoginView, RegiseredViews, LogoutViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Error/', views.ErrorView.as_view()),
    path('', views.Home.as_view()),
    path('search/', views.SearchView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutViews.as_view()),
    path('register/', RegiseredViews.as_view()),
    path('all-films/', views.AllFilms.as_view()),
    path('all-hall/', views.AllHall.as_view()),
    path('hall/<int:id>/', views.HallDetail.as_view()),
    path('<int:id>/<str:hall>/<str:time>/', views.HallView.as_view()),
    path('reserve_ticket/<str:rowcolums>/<int:id>/<str:time>/', views.ReserveTicket.as_view()),
    path('your-ticket/', views.UserTicket),
    path('delete-ticket/<int:id>/', views.DeleteTicket),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

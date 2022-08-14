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
                  #accounts view
                  path('login/', LoginView.as_view(), name='login'),
                  path('logout/', LogoutView.as_view(), name='logout'),
                  path('register/', RegisterView.as_view(), name='create-user'),
                  #dictionary view
                  path('', views.HomeView.as_view(), name='home-view'),
                  path('pl/', views.HomeViewEn.as_view(), name='home-view-pl'),
                  path('dictionary/', views.Dictionary.as_view(), name='global-dictionary'),
                  path('card-game/', views.CardGame.as_view(), name='global-card-game'),
                  path('blog/', views.BlogView.as_view(), name='blog'),
                  path('like-post/<int:id_post>/', views.CreateLike.as_view(), name='create-like'),
                  path('comment/<int:id_post>/', views.CreateComment.as_view(), name='create-comment'),
                  #CRUD for user dictionary
                  path('user-dictionary/', views.UserDictionary.as_view(), name='user-dictionary'),
                  path('update_word/<int:id>/', views.update_word, name='update-word'),
                  path('update_word/<int:id>/delete/', views.delete_word, name='delete-word'),
                  #for user login in view
                  path('user-card-game/', views.UserCardGame.as_view(), name='user-card-game'),
                  path('frasses/', views.FrassesView.as_view(), name='frasses'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

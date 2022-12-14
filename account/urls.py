from django.urls import URLPattern, path
from . import views
from main import views as v

urlpatterns = [
    path('', v.UserListView.as_view()),
    path('<int:pk>/', v.UserDetailView.as_view()),
    path('login/', views.CustomLoginView.as_view()),
    path('logout/', views.CustomLogoutView.as_view()),
    path('register/', v.UserRegistrationView.as_view()),
]

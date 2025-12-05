from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from freddyapp import views

urlpatterns = [
    path('list', views.animatronic_list, name='animatronic_list'),
    path('new', views.animatronic_new, name='animatronic_new'),
    path('<int:id>/view', views.animatronic_view, name='animatronic_view'),
    path('<int:pk>/edit', views.AnimatronicUpdate.as_view(), name='animatronic_edit'),
    path('<int:pk>/delete', views.AnimatronicDelete.as_view(), name='animatronic_delete'),
    path('newuser', views.newuser, name='newuser'),
    path('login', LoginView.as_view(template_name='freddyapp/form.html', redirect_authenticated_user=True), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('theme', views.theme, name='theme'),
    path('clearcookies', views.clearcookies, name='clearcookies')
]
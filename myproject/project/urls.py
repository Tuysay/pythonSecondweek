from django.urls import path
from project import views
from .views import index, BBLoginView, profile, RegisterView, apl_admin_render, apl_admin_done, createapl, aplication_render, \
    apl_filter
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', index, name='index'),
    path('login/', BBLoginView.as_view(), name='login'),
    path('logout/', authViews.LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', aplication_render, name='profile'),
    path('create_aplication/', createapl, name='create'),
    path('apl_admin/', apl_admin_render, name='apl_admin_render'),
    path('apl_admin_done/', apl_admin_done, name='apl_admin_done'),
    path('processingapl/<int:id>', views.processingapl, name='processing'),
    path('done/<int:id>', views.doneapl, name='done'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('profile/<str:status>', apl_filter, name='filter'),
]



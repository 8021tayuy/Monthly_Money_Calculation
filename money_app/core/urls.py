from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('expense/add/', views.add_expense, name='add_expense'),
    path('planned/add/', views.add_planned, name='add_planned'),
    path('history/', views.history, name='history'),
    path('signup/', views.signup, name='signup'),
]
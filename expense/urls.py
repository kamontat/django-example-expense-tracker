from django.contrib import admin
from django.urls import path

from expense import views

urlpatterns = [
    path('', views.ExpenseListView.as_view(), name="list"),
    path('<int:pk>/edit/', views.ExpenseDetailView.as_view(), name="edit"),
    path('add/', views.ExpenseAddView.as_view(), name="add"),
    path('<int:pk>/delete/', views.delete_expense, name="delete")
]

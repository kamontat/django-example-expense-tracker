from django.contrib import admin
from expense import models

@admin.register(models.Expense)
class ExpenseAdmin(admin.ModelAdmin):
    pass

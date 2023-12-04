from django.core import validators
from django.db import models
from django import forms

from django.utils import timezone

# class ExpenseCategory(models.Model):
#   text = models.CharField()

class Expense(models.Model):
  CATEGORIES = [
    ("BF", "Breakfast"),
    ("L", "Lunch"),
    ("D", "Dinner"),
    ("S", "Shopping"),
  ]

  date = models.DateField(
    validators=[validators.MaxValueValidator(timezone.now().date())]
  )
  description = models.CharField(
    max_length=80,
    blank=False,
    null=False,
    validators=[validators.MinLengthValidator(2)]
  )

  # category = models.ForeignKey(ExpenseCategory)
  category = models.CharField(max_length=3, choices=CATEGORIES)
  amount = models.DecimalField(decimal_places=2, max_digits=11)

  def get_category(self):
    for (key, value) in Expense.CATEGORIES:
      if self.category == key:
        return value
    return "UNKNOWN"

  def __str__(self) -> str:
    return self.description

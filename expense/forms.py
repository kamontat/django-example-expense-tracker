from django import forms
from django.db.models import Max
from django.core.exceptions import ValidationError

from expense import models

class ExpenseDateField(forms.DateField):
  widget = forms.DateInput(attrs={'type': 'date'})
  def validate(self, value) -> None:
    parent = super().validate(value)
    if parent == False:
      return False

    max_date = models.Expense.objects.aggregate(Max("date")).get("date__max")
    if value < max_date:
      raise ValidationError("Your expense date is too old", code="too_old")

class ExpenseForm(forms.ModelForm):
  date = ExpenseDateField()
  class Meta:
    model = models.Expense
    fields = "__all__"

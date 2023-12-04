from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseNotFound
from django.db.models import Sum
from django.shortcuts import redirect
from expense import models, forms

## CRUD
class ExpenseAddView(generic.CreateView):
    # model = models.Expense
    form_class = forms.ExpenseForm
    template_name = "expense_form.html"
    success_url = reverse_lazy("list")

class ExpenseDetailView(generic.UpdateView):
    model = models.Expense
    form_class = forms.ExpenseForm
    template_name = "expense_update.html"
    success_url = reverse_lazy("list")

class ExpenseListView(generic.ListView):
    model = models.Expense
    template_name = "expense_list.html"
    ordering = ["-date"]

    extra_context = {
        "count": models.Expense.objects.count,
        "sum": lambda: models.Expense.objects.aggregate(Sum("amount")).get("amount__sum")
    }

class ExpenseDeleteView(generic.DeleteView):
    model = models.Expense
    template_name = "expense_delete.html"
    success_url = reverse_lazy("list")

def delete_expense(request, pk: int):
    try:
        expense = models.Expense.objects.get(id=pk)
        expense.delete()
        return redirect("list")
    except models.Expense.DoesNotExist:
        # TODO: Return error message
        return HttpResponseNotFound()

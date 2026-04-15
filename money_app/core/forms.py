from django import forms
from .models import Expense, PlannedExpense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'amount', 'category', 'memo']

class PlannedExpenseForm(forms.ModelForm):
    class Meta:
        model = PlannedExpense
        fields = ['due_date', 'amount', 'memo']
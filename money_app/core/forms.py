from django import forms
from .models import Expense, PlannedExpense
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'amount', 'category', 'memo']

class PlannedExpenseForm(forms.ModelForm):
    class Meta:
        model = PlannedExpense
        fields = ['due_date', 'amount', 'memo']

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

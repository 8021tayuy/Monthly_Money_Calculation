from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SalaryCycle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()  # 給料日
    end_date = models.DateField()
    income = models.IntegerField()  # 給料
    initial_balance = models.IntegerField()  # 初期残高

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.IntegerField()
    category = models.CharField(max_length=50)
    memo = models.TextField(blank=True)

class PlannedExpense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField()
    amount = models.IntegerField()
    memo = models.TextField(blank=True)
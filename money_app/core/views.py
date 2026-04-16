from django.shortcuts import render, redirect
from django.db.models import Sum
from datetime import date
from .models import Expense, PlannedExpense, SalaryCycle
from .forms import ExpenseForm, PlannedExpenseForm
from django.contrib.auth.decorators import login_required


def get_current_cycle(user):
    today = date.today()
    return SalaryCycle.objects.get(
        user=user,
        start_date__lte=today,
        end_date__gte=today
    )


def calculate_remaining(user):
    cycle = get_current_cycle(user)

    expenses = Expense.objects.filter(
        user=user,
        date__range=(cycle.start_date, cycle.end_date)
    ).aggregate(total=Sum('amount'))['total'] or 0

    planned = PlannedExpense.objects.filter(
        user=user,
        due_date__gte=date.today(),
        due_date__lte=cycle.end_date
    ).aggregate(total=Sum('amount'))['total'] or 0

    return cycle.initial_balance + cycle.income - expenses - planned


def daily_budget(user):
    cycle = get_current_cycle(user)
    remaining = calculate_remaining(user)

    days_left = (cycle.end_date - date.today()).days + 1
    return remaining // days_left if days_left > 0 else 0


@login_required
def dashboard(request):
    remaining = calculate_remaining(request.user)
    daily = daily_budget(request.user)

    return render(request, 'dashboard.html', {
        'remaining': remaining,
        'daily': daily,
    })


@login_required
def add_expense(request):
    form = ExpenseForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('dashboard')

    return render(request, 'add_expense.html', {'form': form})


@login_required
def add_planned(request):
    form = PlannedExpenseForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('dashboard')

    return render(request, 'add_planned.html', {'form': form})


@login_required
def history(request):
    cycles = SalaryCycle.objects.filter(user=request.user).order_by('-start_date')
    return render(request, 'history.html', {'cycles': cycles})
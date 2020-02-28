from django.shortcuts import render, redirect
from budgetapp.models import Income, Expense
# Create your views here.
import datetime, time
from datetime import date

def add_income(request):
    param = {}
    if request.method == "POST":
        print(request.POST)
        if request.POST.get('type_income'):
            type_income = request.POST.get('type_income')
            des = request.POST.get('description')
            amount = float(request.POST.get('amount'))
            recurr = bool(int(request.POST.get('recurring')))
            on_date_recurr = request.POST.get('recurr_date', None)
            times_recurr = request.POST.get('time_recurr', None)
            # TODO : insert model
                    
            if recurr:
                try :
                    times = int(times_recurr)
                
                except Exception as e:
                    times = 0
                    recurr = False
                    on_date_recurr = None
                if times > 0: # Add Future Event
                    today = datetime.datetime.today()
                    this_month = today.month
                    this_year = today.year
                    for i in range(times):
                        
                        tmp = this_month + i
                        if tmp > 12: # Over flow month start new year
                            tmp = tmp -12
                            this_year = today.year + 1 
                            
                        datetime_str = '{month}-{ondate}-{year}'.format(ondate=on_date_recurr, month=tmp, year=this_year)
                        dateobj = datetime.datetime.strptime(datetime_str, '%m-%d-%Y')
                        
                        transac = Income(income_type=type_income, description=des, 
                                amount=amount, recurring=recurr, 
                                ondate=on_date_recurr,
                                recurr=times_recurr,
                                date_recurr=dateobj)
                        transac.save()
                        
                    
            else:
                today = datetime.datetime.today()
                this_month = today.month
                this_year = today.year
                this_day = today.day
                
                date_str = "{m}-{d}-{y}".format(m=this_month, d=this_day, y=this_year)
                dateobj = datetime.datetime.strptime(date_str, '%m-%d-%Y')
                transac = Income(income_type=type_income, description=des, amount=amount,recurring=recurr, ondate=on_date_recurr,recurr=times_recurr,date_recurr=dateobj)
                transac.save()
            

        else:
            type_expense = request.POST.get('type_expense')
            des = request.POST.get('description4')
            amount = request.POST.get('amount5')
            # TODO : insert model
            transac = Expense(expense_type=type_expense, description=des,
                              amount=amount)
            transac.save()
            
    # TODO : Query Here       
    today = datetime.datetime.today()
    mm = today.month
    yy = today.year
    kw = "{yy}-{mm}".format(yy=yy, mm=mm)
    print(kw)
    
    incomes = Income.objects.filter(date_recurr__month=mm).filter(date_recurr__year=yy)
    expenses = Expense.objects.all()
    data = {} 
    print(incomes)
    for income in incomes:
        print(income.tid, income.amount)
        
        
        if income.income_type in data.keys() :
            amount_new =  income.amount + data.get(income.income_type)
            data.update({income.income_type: amount_new})
        else:
            data.update({income.income_type: income.amount})
    
    
    
    data_exp = {}
    for expense in expenses:
        if expense.expense_type in data_exp.keys():
            amount_new =  expense.amount + data_exp.get(expense.expense_type)
            data_exp.update({expense.expense_type: amount_new})
        else:
            data_exp.update({expense.expense_type: expense.amount})

    total_income = 0
    total_expense = 0
    
    for _, v in data.items():
        total_income += v
        
    for _, v in data_exp.items():
        total_expense += v
    
    
    netBal = str(total_income - total_expense)
    param = { "income" : data ,
        "expense" : data_exp,
        "balance" : netBal
    } 
    
    return render(request, 'detail.html', param)

def report(request):
    param = {}
    if request.method == "POST":
        from_date = request.POST.get('datepick_from')
        to_date = request.POST.get('datepick_to')
        
        from_date = from_date.split('-')
        to_date = to_date.split('-')
        
        yfd = int(from_date[0])
        mfd = int(from_date[1])
        dfd = int(from_date[-1])
        
        ytd = int(to_date[0])
        mtd = int(to_date[1])
        dtd = int(to_date[-1])
        
        print(request.POST)
        
        # expenses = Expense.objects.all()
        result = Expense.objects.filter(date_add__range=(date(yfd,mfd,dfd), date(ytd, mtd, dtd)))
        print(result)
        param = {"data": result}

    return render(request, 'report.html', param)


def clear_content(request):
    Income.objects.all().delete()
    Expense.objects.all().delete()
    return redirect('') 
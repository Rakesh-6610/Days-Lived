import sys
import datetime
import calendar

def main():
    user_input=input('Enter your birthdate (dd/mm/yyyy) : ').lower().strip().split('/')
    if len(user_input)!=3:
        sys.exit('Invalid Input')
    else:
        for i in user_input:
            if i.isalpha():
                sys.exit('Invalid Input')
        else:
            try:
                if (31>=int(user_input[0])>=1) and (12>=int(user_input[1])>=1) and (len(user_input[2])==4):
                    days_lived = days(user_input)
                    print(f'Congrats!! You are {int(days_lived/365)} years old.')
                    print(f'You survived: {days_lived} days')
                else:
                    sys.exit('Invalid Input')
            except ValueError:
                sys.exit('Invalid Input')



def days(birthdate):
    day = 0
    count = 1
    x = datetime.datetime.now()
    year = int(birthdate[2])


    while year!= int(x.strftime("%Y")):
        if count==1:
            day += year_days(birthdate)
            count+=1
        else:
            day += 366 if (calendar.isleap(year)) else 365
        year += 1
    else:
        months = filtered_months(int(x.strftime("%Y"))  , (x.strftime("%B")) , 2)
        for month in months:
            day += (int(x.strftime("%d"))) if (month==(x.strftime("%B"))) else months[month]
        else:
            return day


def year_days(birthdate):
    born_year_days = 0
    month_list = ["January","February","March","April","May","June","July","August","September","October","November","December"]

    try:
        months = filtered_months(int(birthdate[2]),month_list[(int(birthdate[1])) - 1])
    except IndexError:
        sys.exit('Invalid Input')
    else:
        for month in months:
            if month == month_list[(int(birthdate[1]))-1]:
                born_year_days += (months[month] - (int(birthdate[0])))
            else:
                born_year_days += months[month]
        else:
            return born_year_days
    



def is_leap_year(year):
    return 29 if (calendar.isleap(year)) else 28



def filtered_months(year,month,mode = 1):
    months = {
        "January" : 31,
        "February" : is_leap_year(year),
        "March" : 31,
        "April" : 30,
        "May" : 31,
        "June" : 30,
        "July" : 31,
        "August" : 31,
        "September" : 30,
        "October" : 31,
        "November": 30,
        "December" : 31
    }

    un_f_months = {}
    f_months = {}
    for m in months:
        if m==month:
            for i in months:
                if i in un_f_months:
                    pass
                else:
                    f_months.update({i : months[i]})
            else:
                if mode==1:
                    return f_months
                else:
                    un_f_months.update({m : months[m]})
                    return un_f_months
        else:
            un_f_months.update({m : months[m]})

if __name__=='__main__':
    main()
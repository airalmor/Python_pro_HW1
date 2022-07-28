from application.salary import calculate_salary as cs
from application.db.people import get_employees as ge
from datetime import datetime as dt

if __name__ == '__main__':
    print(dt.now().strftime('Current date is : \n%A, %d %B, %Y\n'))
    cs()
    ge()






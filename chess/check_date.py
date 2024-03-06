__all__ = ['check_date']

import datetime
import calendar
from sys import argv


def check_date(date: str) -> bool:
    format = '%d.%m.%Y'
    try:
        date = datetime.datetime.strptime(date, format)
        year = date.strftime('%Y')
        if calendar.isleap(int(year)):
            print("Год високосный")
        else:
            print("Год не високосный")
        print(date)
    except:
        print("Дата не существует")


if __name__ == '__main__':
    if len(argv) > 1:
        date = argv[1]
        check_date(date)
    else:
        print("Не указана дата для проверки")

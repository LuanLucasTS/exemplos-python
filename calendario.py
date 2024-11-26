import calendar
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR')
ano=2023
mes=6

print(calendar.month(ano, mes))

text_cal = calendar.HTMLCalendar(firstweekday=0)

# printing formatmonth
print(text_cal.formatmonth(2022, 6, withyear=True))

print(text_cal.formatyearpage(2022))
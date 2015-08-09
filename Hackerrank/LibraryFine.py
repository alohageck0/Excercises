__author__ = 'royalfiish'
from datetime import datetime


def check(date):
    if int(act_date.strftime(date)) == int(exp_date.strftime(date)):
        return True
    else:
        return False


actual = input()
act_date = datetime.strptime(actual, '%d %m %Y')
arr_act = actual.split(' ')
expected = input()
exp_date = datetime.strptime(expected, '%d %m %Y')
arr_exp = expected.split(' ')
if act_date <= exp_date:
    print(0)
else:
    if not check('%Y'):
        total = 10000
    elif not check('%m'):
        razn1 = int(act_date.strftime('%m')) - int(exp_date.strftime('%m'))
        total = razn1 * 500
    elif not check('%d'):
        razn1 = int(act_date.strftime('%d')) - int(exp_date.strftime('%d'))
        total = razn1 * 15
    print(total)

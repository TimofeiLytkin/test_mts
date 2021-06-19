"""Тестовые задания"""

"""
1. Написать декоратор на Python3
@print_gte(3)
def foo(x):
print(x)
выводит foo(x) если x > val
иначе выводит 'error'
"""


def print_gte(val):
    def wrapper(func):
        def inner(*args, **kwargs):
            error_massage = 'error'
            if args[0] > val:
                return func(*args, **kwargs)
            return func(error_massage)
        return inner
    return wrapper


@print_gte(3)
def foo(x):
    print(x)


"""
2. Переписать SQL запрос на Django Query API
# Модель
class Test(models.Model):
    def __str__(self):
        return '{}, {}'.format(self.a, self.b)
a = models.IntegerField(verbose_name='a', default=0, blank=True)
b = models.IntegerField(verbose_name='b', default=0, blank=True)
 
## tzt_test - имя таблицы
## SQL - sql-запрос
select distinct a, b from tzt_test where a > b;
"""

# from django.db.models import F
#
#
# response = tzt_test.objects.filter(a__gt=F('b')).distinct()

"""
3. Написать SQL запросы к приведенным таблицам
DEPARTMENT ==========
    ID   integer    PRIMARY KEY
    NAME vchar
EMPLOYEE ========
    ID   integer    PRIMARY KEY
    DEPARTMENT_ID  integer   REFERENCES DEPARTMENT(ID)
    CHIEF_ID  integer   REFERENCES EMPLOYEE(ID)
    NAME vchar
    SALARY numeric

A. Вывести список сотрудников, получающих заработную плату большую чем у 
непосредственного руководителя
B. Вывести список сотрудников, получающих максимальную заработную плату 
в своем отделе
C. Вывести список ID отделов, количество сотрудников в которых 
не превышает 3 человек
D. Вывести список сотрудников, не имеющих назначенного непосредственного 
руководителя, работающего в том же отделе
E. Вывести список ID отделов с максимальной суммарной зарплатой сотрудников
 
"""


# A.
# select E1.*
# from EMPLOYEE E1, EMPLOYEE E2
# where E1.CHIEF_ID = E2.ID and E1.SALARY > E2.SALARY

# B.
# select E1.*
# from EMPLOYEE E1
# where E1.SALARY = (
#   select max(SALARY)
#   from EMPLOYEE E2
#   where E2.DEPARTMENT_ID = E1.DEPARTMENT_ID
# )

# C.
# select DEPARTMENT_ID
# from EMPLOYEE
# group by DEPARTMENT_ID
# having count(*) <= 3

# D.
# select E1.*
# from EMPLOYEE E1
# left join EMPLOYEE E2 on (E2.ID = E1.CHIEF_ID and E2.DEPARTMENT_ID = E1.DEPARTMENT_ID)
# where E2.ID is null

# E.
# with SUM_SALARY as (
#   select DEPARTMENT_ID, sum(SALARY) SALARY
#   from EMPLOYEE
#   group by DEPARTMENT_ID
# )
#
# select DEPARTMENT_ID
# from SUM_SALARY
# where SALARY = (
#   select max(SUM_SALARY)
#   from SUM_SALARY
# )

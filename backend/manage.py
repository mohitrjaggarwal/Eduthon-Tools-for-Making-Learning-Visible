#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
n = int(input("no .of enteries:"))
list = []
dict = {'O': "Orthopedics",'P' : "Pediatrics",'E': "ENT"}
O =0
P =0
E = 0
for i in range(2*n):
    if(i%2 !=0):
        entry = str(input("enter speciality"))
        if(entry == 'O'):
            O = O + 1
        elif(entry == 'P'):
            P = P + 1
        else:
             E = E+1
    else:
        entry = int(input("id no."))

    list.append(entry)

#comparing values
if(O> P and O > E):
    r = 'O'
elif(E> P and E > O):
    r = 'E'
else:
    r = 'P'
print(dict[r])











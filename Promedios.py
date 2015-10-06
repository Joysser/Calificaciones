#Hacer un programa de tres notas y muestre la califiacion de muy bueno (20-17), bueno(16-14), regular de (13-11) y malo de (10-0)
__author__ = "Alumno"
__date__ = "$06/10/2015 10:31:32 AM$"

a=int(input('Introducir primer numero='))
b=int(input('Introducir segundo numero='))
c=int(input('Introducir tercer numero='))
d=(a+b+c)/3
if d <= 20 and d>=0:
    if d<=20 and d>=17:
        print 'Es muy bueno'
    else:
        if d<=16 and d>=14:
         print 'Es bueno'
        else:
            if d<=13 and d>= 11:
             print 'Es regular'
            else:
                    if d<=10 and d>=0:
                     print 'Es malo'
else:
    print 'numero invalido'

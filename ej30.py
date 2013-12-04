# coding: utf-8


Mario = 'chico'
Sonia = 'chica'

from datetime import datetime
x = datetime.now()


i = 0
while i < 10:
    
    persona = raw_input("quien eres?")
    
    if persona == 'Mario':
        print 'Hola Mario, eres ', Mario
        i += 1
        y = datetime.now()
        z = y - x
        print z.seconds
    elif persona == 'Sonia':
        print 'eres', Sonia
        i += 1
        
    else:
        print 'No estas en mi BBDD'
        i += 1
                     
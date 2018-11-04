"""
while True:
    try:
        vrednost = int(input('vrednost: '))
        print(2/vrednost)
        break
    except (ValueError, ArithmeticError) as ex:
        print('Izuzetak:', ex)
    except BaseException as ex:
        print('Interrupt:', type(ex))
    

"""

def podeli(a, b):
    try:
        vrednost = a / b
    finally:
        return vrednost
        
print(podeli(2, 3))
print(podeli(1, 0))


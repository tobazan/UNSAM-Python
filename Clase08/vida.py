from datetime import datetime

def vida(birth):
    '''
    nac: date en formato dd/mm/aaaa

    recibe una fecha y devuelve la cantidad de segundos
    transcurridos hasta hoy
    '''
    try:
        norm_birth = datetime.strptime(birth, '%d/%m/%Y')

    except Exception as e:
        print(e)

    now = datetime.now()
    lived = now - norm_birth
    
    return lived.total_seconds()

# print('He vivido ', vida('19/12/1990'))
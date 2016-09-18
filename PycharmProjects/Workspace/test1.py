def InputNumero():
    x=input('inserisci numero: ')
    if x>16:
        raise Exception('puppa','massimo17!')
    return x

def CheckNumero():
    try:
        a=InputNumero()
        print a
    except:
        print 'inserisci un numero <17'
        
while True:
    CheckNumero()
        

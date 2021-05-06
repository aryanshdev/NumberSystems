'''
Python Module To Quickly Convert One Number System to Another.

Made and Maintained By ARYANSH GUPTA

(c) 2021 Aryansh Gupta, CPL SOFTWARE LABS
'''


global hextob, octtod, btohex

octtod = {'0':'000','1' : '001','2' : '010','3' : '011','4' : '100','5' : '101','6': '110','7' : '111'}

hextob = {'0':'0000','1' : '0001','2' : '0010','3' : '0011','4' : '0100','5' : '0101','6': '0110','7' : '0111',\
          '8':'1000','9':'1001','a' : '1010','b':'1011','c':'1100','d':'1101','e':'1110','f':'1111',\
          'A' : '1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}

dectoh = {'0' : '0' , '1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9',\
          '10':'A','11':'B','12':'C','13':'D','14':'E','15':'F'}

btohex = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8',\
          '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}

# these are checkers to ensure data entered is in correct form

class InvalidInputError(Exception):
    def __init__(self,message=None):
        __cause__ = message
        
def binchecker(n):
    '''Checks if passed argument belongs for Binary System or not'''
    bnchecker = ['0','1']
    for i in range(len(alpha)):
        if alpha[i] in bnchecker:
            pass
        else:
            raise InvalidInputError('invalid Binary Number')
            return None

def octchecker(a):
    '''Checks if passed argument belongs for Octal System or not'''
    occhecker = ['0','1','2','3','4','5','6','7']
    for i in range(len(a)):
        if a[i] in occhecker:
            pass
        else:
            raise InvalidInputError('invalid Octal Number')
            return None
            
def decchecker(a):
    '''Checks if passed argument is sutiable for Decimal System or not'''
    dcchecker = ['1','2','3','4','5','6','7','8','9','0']
    for i in range(len(a)):
        if a[i] in dcchecker:
            pass
        else:
            raise InvalidInputError('invalid Decimal Number')
            return None

def hexchecker(n):
    '''Checks if passed argument is sutiable for Hexadecimal System or not'''
    hxchecker = ['1','2','3','4','5','6','7','8','9','0','A','B','C','D',\
                 'E','F','a','b','c','d','e','f']
    for i in range(len(n)):
        if n[i] in hxchecker:
            pass
        else:
            raise InvalidInputError('invalid Hexadecimal Number')


            return None


# real function definations

    
def dectobin(n):
    '''inputs Decimal Format, returns Binary Format'''
    bn = ''
    decchecker(str(n))
    while n > 0:
        bn += str(n%2)
        n = int(n/2)
    return int(bn[::-1])


def bintodec(n):
    '''inputs Binary Format, returns Deciaml Format'''
    n = str(n)
    g = n[::-1]
    n = list(g)
    binchecker(n)
    dec = 0
    for i in range(len(n)):
        dec += int(n[i])*(2**i)
    return dec

def dectooct(n):
    '''inputs Decimal Format, returns Octadeciaml Format'''
    oc = ''
    decchecker(str(n))
    while n > 0:
        oc += str(n%8)
        n = int(n/8)
    return int(oc[::-1])

def octtobin(n):
    '''inputs Octal Format, returns Binary Format'''
    n = str(n)
    octchecker(n) 
    bin = ''
    for i in range(len(n)):
        bin += octtod.get(n[i])
    return(int(bin))

def octtodec(n):
    '''inputs Octal Format, returns Decimal Format'''
    oc = ''
    octchecker(str(n))
    while n > 0:
        oc += str(n%8)
        n = int(n/8)
    return int(oc[::-1])

def bintooct(n):
    '''inputs Binary Format, returns Octal Format'''
    return dectooct(bintodec(n))

def hextobin(n):
    '''inputs Hexadecimal Format, returns Binary Format'''
    n = str(n)
    hexchecker(n)
    bin = ''
    for i in range(len(n)):
        bin += hextob.get(n[i])
    return int(bin)

def hextodec(n):
    '''inputs Hexadecimal Format, returns Decimal Format'''
    return bintodec(hextobin(str(n)))
def hextooct(n):
    return bintooct(hextobin(str(n)))

def dectohex(n):
    '''inputs Decimal Format, returns Hexadecimal Format'''
    decchecker(str(n))
    hx = ''
    while n >0:
        hx += dectoh.get(str(n%16))
        n = int(n/16)
    return hx[::-1]

def bintohex(n):
    '''inputs Binary Format, returns Hexadecimal Format'''
    binchecker(str(n))
    n = str(n)
    hex = ''
    n = n[::-1]
    for i in range(0,len(n),4):
        try:
            get = n[i:i+4]
        except :
            get = n[i:]
        if len(get) != 4:
                
                g = get[::-1]
                t = '0'*(4-len(get))+g
                get = t[::-1]
        hex += btohex.get(get[::-1])
    return hex[::-1]
    

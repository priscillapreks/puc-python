# def	bhaskara(a,	b,	c):
# 				x1	=	(-b	+(((b**2)-4*a*c)**(1/2)))/(2*a)
# 				x2	=	(-b	-(((b**2)-4*a*c)**(1/2)))/(2*a)
# 				return	x1,	x2



def calc_delta(a, b, c):
    return (b**2) - 4*a*c

def calc_raiz_delta(a, b, c):
    return calc_delta(a, b, c) ** (1/2)

def calc_x(a, b, c, n=1):
    return (-b + (n * calc_raiz_delta(a, b, c)))/(2*a)

def bhaskara_refatorado(a, b, c):
    x1 = calc_x(a, b, c)
    x2 = calc_x(a, b, c, -1)
    return x1, x2


# testa as funções
if __name__ == '__main__':

    if	bhaskara_refatorado(1,20,-525) == (15.0, -35.0):
        print('Passou	no	teste!')
    else:
        print('Falhou!')
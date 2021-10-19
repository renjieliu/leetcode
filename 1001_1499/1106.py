def parseBoolExpr(expression: str):
    def andd(x, *args):
        exp = str(x)
        for i in args:
            exp+=str(i)
        return 'f' if exp.find('f') != -1 else 't'

    def orr(x, *args):
        exp = str(x)
        for i in args:
            exp += str(i)
        return 'f' if exp.find('t') == -1 else 't'

    def neg(x):
        exp = str(x)
        return 't' if exp == 'f' else 'f'

    if expression == 'f':
        return False

    elif expression == 't':
        return True

    else:

        exp = expression.replace("|", 'orr').replace('&', 'andd').replace('!','neg')
        exp = exp.replace('t', '\'t\'').replace('f', '\'f\'')
        #print(exp)
        return True if eval(exp)  == 't' else False


print(parseBoolExpr('|( &(t,f,t),!(t) )'))
print(parseBoolExpr( "&(t,f)"))
print(parseBoolExpr("!(f)"))
print(parseBoolExpr("|(f,t)"))
print(parseBoolExpr('!f'))




















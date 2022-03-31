import ply.yacc as yacc
from tablaAS import tokens
estado = []


def p_S(p):
    '''S : INICIO ENTRADA PROCESOS FIN'''


def p_INICIO(p):
    '''INICIO : llaveApertura'''


def p_ENTRADA(p):
    '''ENTRADA : INPUT dosPuntos LISTA_ID'''


def p_INPUT(p):
    '''INPUT : entradas'''


def p_LISTA_ID(p):
    '''LISTA_ID : ID_NUM RESTO_LISTA'''


def p_ID_NUM(p):
    '''ID_NUM : DIGITO RESTO_ID_NUM'''


def p_RESTO_ID_NUM(p):
    '''RESTO_ID_NUM : DIGITO RESTO_ID_NUM
    | vacio'''


def p_RESTO_LISTA(p):
    '''RESTO_LISTA : coma RESTOZ'''


def p_RESTOZ(p):
    '''RESTOZ : ID_NUM RESTO_LISTA
    | ETIQUETA coma PROPIEDAD'''


def p_PROCESOS(p):
    '''PROCESOS : P dosPuntos EXPRESION'''


def p_P(p):
    '''P : procesos'''


def p_ID_TEXT(p):
    '''ID_TEXT : LETRA RESTO_ID_TEXT'''


def p_RESTO_ID_TEXT(p):
    '''RESTO_ID_TEXT : LETRA RESTO_ID_TEXT
    | DIGITO RESTO_ID_TEXT
    | vacio'''


def p_EXPRESION(p):
    '''EXPRESION : ID_TEXT asignacion RESTOX
    | FUNCION_INTERNA_4 parIzq ID_TEXT coma ID_TEXT coma ID_TEXT parDer'''

def p_RESTOX(p):
    '''RESTOX : FUNCION_INTERNA_1 parIzq ID_NUM coma ID_NUM coma ID_NUM parDer EXPRESION
    | FUNCION_INTERNA_2 parIzq ETIQUETA parDer EXPRESION
    | FUNCION_INTERNA_3 parIzq PROPIEDAD parDer EXPRESION'''


def p_FUNCION_INTERNA_1(p):
    '''FUNCION_INTERNA_1 : formato_hexadecimal'''


def p_FUNCION_INTERNA_2(p):
    '''FUNCION_INTERNA_2 : interpretar_etiqueta'''


def p_FUNCION_INTERNA_3(p):
    '''FUNCION_INTERNA_3 : interpretar_propiedad'''


def p_FUNCION_INTERNA_4(p):
    '''FUNCION_INTERNA_4 : generar_CSS'''


def p_PROPIEDAD(p):
    '''PROPIEDAD : cssTags'''


def p_ETIQUETA(p):
    '''ETIQUETA : htmlTags'''


def p_LETRA(p):
    '''LETRA : let'''


def p_DIGITO(p):
    '''DIGITO : num'''


def p_FIN(p):
    '''FIN : llaveCierre'''


def p_vacio(p):
    '''vacio : '''
    pass


def p_error(p):
    if p:
        e = str(p.type), str(p.lineno), str(p.lexpos), str(p.value)
        print("Error de Sintaxis : ", p.type, " Linea : ", p.lineno, " Posicion : ", p.lexpos, " Simbolo : ", p.value)
        parser.errok()
        estado.append(e)
    else:
        e = "EOF"
        print("Error de Sintaxis EOF.")
        estado.append(e)


def Analizador_Sintactico(cadena):
    estado.clear()
    parser.parse(cadena)
    return estado


parser = yacc.yacc()

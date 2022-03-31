import ply.lex as lex

tokens = (
    "llaveApertura",
    "dosPuntos",
    "entradas",
    "coma",
    "procesos",
    "asignacion",
    "parIzq",
    "parDer",
    "formato_hexadecimal",
    "interpretar_etiqueta",
    "interpretar_propiedad",
    "generar_CSS",
    "cssTags",
    "htmlTags",
    "num",
    "let",
    "llaveCierre"
)

t_llaveApertura = r'\['
t_dosPuntos = r':'
t_entradas = r'Entradas'
t_coma = r','
t_procesos = r'Procesos'
t_asignacion = r'='
t_parIzq = r'\('
t_parDer = r'\)'
t_formato_hexadecimal = r'\b(?:formato_hexadecimal)\b'
t_interpretar_etiqueta = r'\b(?:interpretar_etiqueta)\b'
t_interpretar_propiedad = r'\b(?:interpretar_propiedad)\b'
t_generar_CSS = r'\b(?:generar_CSS)\b'
t_cssTags = r'color|fondo-color|color\sde\sfondo|borde-color|color\sde\sborde|grosor-color|color\sde\sgrosor|cortorno-color|color\sde\scortorno|texto-decoracion-color|color\sdecorativo\sde\stexto|texto-enfasis-color|color\senfatico\sde\stexto|texto-sombra|sombra\sde\stexto|intercalado-color|color\sde\sintercalado|columna-regla-color|color\sde\sregla\sentre\scolumnas|color\sde\sregla\sde\scolumnas|color-ajuste|ajuste\sde\scolor'
t_htmlTags = r'enlace|liga|link|ancla|division|pie\sde\spagina|cabecera|encabezado|encabezado\s1|encabezado\s2|encabezado\s3|encabezado\s4|encabezado\s5|encabezado\s6|entrada|etiqueta|barra\sde\snavegacion|lista\sordenada|parrafo|tabla|cuerpo\sde\stabla|celda\sde\stabla|encabezado\sde\stabla|cabecera\sde\stabla|texto\ssubrayado|lista\sno\sordenada|lista\sdesordenada'
t_num = r'([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'
t_let = r'[a-zA-Z]'
t_llaveCierre = r'\]'
t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Error Lexico" + str(t.value))
    t.lexer.skip(1)


analizador = lex.lex()

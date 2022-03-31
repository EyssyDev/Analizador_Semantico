import re


def Analizador_Lexico(cadena):
    valido = True
    token_dos_puntos = ":"
    token_asignacion = "="
    token_coma = ","
    token_delimitador = ["[", "]"]
    token_parentesis = ["(", ")"]
    token_palabra_reservada = ["Entradas", "Procesos", "formato_hexadecimal", "interpretar_etiqueta",
                               "interpretar_propiedad", "generar_CSS"]

    token_identificador_html = ["enlace", "liga", "link", "ancla", "division", "header", "pie de pagina", "cabecera",
                                "encabezado", "encabezado 1", "encabezado 2", "encabezado 3", "encabezado 4",
                                "encabezado 5", "encabezado 6", "entrada", "etiqueta", "barra de navegacion",
                                "lista ordenada", "parrafo", "tabla", "cuerpo de tabla", "celda de tabla",
                                "encabezado de tabla", "cabecera de tabla", "texto subrayado", "lista no ordenada",
                                "lista desordenada"]

    token_identificador_css = ["color", "fondo-color", "color de fondo", "borde-color", "color de borde",
                               "grosor-color", "color de grosor", "cortorno-color", "color de cortorno",
                               "texto-decoracion-color", "color decorativo de texto", "texto-enfasis-color",
                               "color enfatico de texto", "texto-sombra", "sombra de texto", "intercalado-color",
                               "color de intercalado", "columna-regla-color", "color de regla entre columnas",
                               "color de regla de columnas", "color-ajuste", "ajuste de color"]

    token_identificador_texto = re.compile('^([a-zA-Z])([a-zA-Z]|\d)*')
    cadena = cadena.replace("[", "[ ")
    cadena = cadena.replace("]", " ]")
    cadena = cadena.replace("(", " ( ")
    cadena = cadena.replace(")", " ) ")
    cadena = cadena.replace(":", " : ")
    cadena = cadena.replace("=", " = ")
    cadena = cadena.replace(",", " , ")
    cadena = cadena.split()
    for i in cadena:
        resultadoT = re.match(token_identificador_texto, i)
        if i == token_dos_puntos:
            print("Dos Puntos")
        elif i == token_asignacion:
            print("Asignación")
        elif i == token_coma:
            print("Coma")
        elif i in token_delimitador:
            print("Delimitador")
        elif i in token_parentesis:
            print("Paréntesis")
        elif i in token_palabra_reservada:
            print("Palabra Reservada")
        elif i in token_identificador_html:
            print("Identificador html")
        elif i in token_identificador_css:
            print("Identificador css")
        elif resultadoT:
            print("Identificador letra")
        elif i.isdigit():
            print("Identificador digito")
        else:
            print("[" + str(i) + "]")
            valido = False
    return valido

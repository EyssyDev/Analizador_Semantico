import sys
import os
import re


def formato_hexadecimal(r, g, b):
    def _evaluar(a):
        isInt = True
        try:
            int(a)
        except ValueError:
            isInt = False
        if isInt:
            if int(a) < 0:
                a = -1
            elif int(a) > 255:
                a = -1
            return int(a)
        else:
            return -1

    r = _evaluar(r)
    g = _evaluar(g)
    b = _evaluar(b)

    if r | g | b == -1:
        return False

    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def interpretar_etiqueta(e):
    HTML_Tags = {
        "enlace": "a",
        "liga": "a",
        "link": "a",
        "ancla": "a",
        "division": "div",
        "pie de pagina": "footer",
        "cabecera": "head",
        "encabezado": "header",
        "encabezado 1": "h1",
        "encabezado 2": "h2",
        "encabezado 3": "h3",
        "encabezado 4": "h4",
        "encabezado 5": "h5",
        "encabezado 6": "h6",
        "entrada": "input",
        "etiqueta": "label",
        "barra de navegacion": "nav",
        "lista ordenada": "ol",
        "parrafo": "p",
        "tabla": "table",
        "cuerpo de tabla": "tbody",
        "celda de tabla": "td",
        "encabezado de tabla": "th",
        "cabecera de tabla": "thead",
        "texto subrayado": "u",
        "lista no ordenada": "ul",
        "lista desordenada": "ul"
    }
    if e in HTML_Tags:
        etiqueta_HTML = HTML_Tags[e]
        return etiqueta_HTML
    else:
        return False


def interpretar_propiedad(p):
    CSS_Properties = {
        "color": "color",
        "fondo-color": "background-color",
        "color de fondo": "background-color",
        "borde-color": "border-color",
        "color de borde": "border-color",
        "grosor-color": "outline-color",
        "color de grosor": "outline-color",
        "cortorno-color": "outline-color",
        "color de cortorno": "outline-color",
        "texto-decoracion-color": "text-decoration-color",
        "color decorativo de texto": "text-decoration-color",
        "texto-enfasis-color": "text-emphasis-color",
        "color enfatico de texto": "text-emphasis-color",
        "texto-sombra": "text-shadow",
        "sombra de texto": "text-shadow",
        "intercalado-color": "caret-color",
        "color de intercalado": "caret-color",
        "columna-regla-color": "column-rule-color",
        "color de regla entre columnas": "column-rule-color",
        "color de regla de columnas": "column-rule-color",
        "color-ajuste": "color-adjust",
        "ajuste de color": "color-adjust"
    }
    if p in CSS_Properties:
        propiedad_CSS = CSS_Properties[p]
        return propiedad_CSS
    else:
        return False


def generar_CSS(e, p, h):
    if os.path.exists("archivo.css"):
        os.remove("archivo.css")

    with open('archivo.txt', 'w') as f:
        f.write(str(e) + ' {\n\t' + str(p) + ': ' + str(h) + ';\n}')

    archivo = 'archivo.txt'
    base = os.path.splitext(archivo)[0]
    os.rename(archivo, base + '.css')


def obtener_variables(cadena):
    variables = []
    numeros = re.findall(r'[0-9]+', cadena)
    htmlTags = re.findall(r'enlace|liga|link|ancla|division|pie\sde\spagina|cabecera|encabezado|encabezado\s1|encabezado\s2|encabezado\s3|encabezado\s4|encabezado\s5|encabezado\s6|entrada|etiquetas|barra\sde\snavegacion|lista\sordenada|parrafo|tabla|cuerpo\sde\stabla|celda\sde\stabla|encabezado\sde\stabla|cabecera\sde\stabla|texto\ssubrayado|lista\sno\sordenada|lista\sdesordenada', cadena)
    cssTags = re.findall(r'color|fondo-color|color\sde\sfondo|borde-color|color\sde\sborde|grosor-color|color\sde\sgrosor|cortorno-color|color\sde\scortorno|texto-decoracion-color|color\sdecorativo\sde\stexto|texto-enfasis-color|color\senfatico\sde\stexto|texto-sombra|sombra\sde\stexto|intercalado-color|color\sde\sintercalado|columna-regla-color|color\sde\sregla\sentre\scolumnas|color\sde\sregla\sde\scolumnas|color-ajuste|ajuste\sde\scolor', cadena)
    if numeros[0] == numeros[3]:
        if numeros[1] == numeros[4]:
            if numeros[2] == numeros [5]:
                if htmlTags[0] == htmlTags[1]:
                    if cssTags[0] == cssTags[1]:
                        variables.append(numeros[0])
                        variables.append(numeros[1])
                        variables.append(numeros[2])
                        variables.append(htmlTags[0])
                        variables.append(cssTags[0])
                        return variables
    return False


def Analizador_Semantico(cadena):
    variables = obtener_variables(cadena)
    if not variables:
        return False

    hexadecimal = formato_hexadecimal(variables[0], variables[1], variables[2])
    if not hexadecimal:
        return False
    else:
        etiqueta = interpretar_etiqueta(variables[3])
        if not etiqueta:
            return False
        else:
            propiedad = interpretar_propiedad(variables[4])
            if not propiedad:
                return False
            else:
                generar_CSS(etiqueta, propiedad, hexadecimal)
                return True

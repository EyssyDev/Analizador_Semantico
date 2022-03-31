import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import lexico
import semantico
import sintactico


class index(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("vistaAnalizadorSemantico.ui", self)
        self.boton_ingresar.clicked.connect(self.procesos)

    def procesos(self):
        cadena = self.entrada.toPlainText()
        valido = lexico.Analizador_Lexico(cadena)
        if valido:
            print("\n###Léxico correcto###\n")
            validoCadena = sintactico.Analizador_Sintactico(cadena)
            if len(validoCadena) == 0:
                print("\n###Sintáctico correcto###\n")
                valido = semantico.Analizador_Semantico(cadena)
                if valido:
                    print("\n###Semántico correcto###\n")
                    self.mensaje.setText("Léxico, sintáctico y semántico correcto.")
                    print("\n###¡CSS generado exitosamente!###\n")
                else:
                    self.mensaje.setText("Semántico incorrecto.")
            else:
                self.mensaje.setText("Sintáctico incorrecto.")
        else:
            self.mensaje.setText("Léxico incorrecto.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = index()
    GUI.show()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('graphic_interface.ui', self)

        self.setWindowTitle('Proyecto Algebra Lineal')

        self.btn_hide_menu.hide()
        self.frame_menu.hide()

        self.btn_show_menu.clicked.connect(self.show_menu)
        self.btn_hide_menu.clicked.connect(self.hide_menu)
        self.btn_operaciones.clicked.connect(self.change_page_operaciones)
        self.btn_al.clicked.connect(self.change_page_al)
        self.btn_suma.clicked.connect(self.change_page_suma)
        self.btn_resta.clicked.connect(self.change_page_resta)
        self.btn_multiplicacion.clicked.connect(self.change_page_multiplicacion)
        self.btn_inversa.clicked.connect(self.change_page_inversa)
        self.btn_rango.clicked.connect(self.change_page_rango)
        self.btn_determinante.clicked.connect(self.change_page_determinante)
        self.btn_ecuaciones.clicked.connect(self.change_page_ecuaciones)
        self.btn_markov.clicked.connect(self.change_page_markov)
        self.btn_incriptacion.clicked.connect(self.change_page_incriptacion)
        self.btn_aleatorio.clicked.connect(self.change_page_aleatorio)

        self.btn_resultado_suma.clicked.connect(self.suma_matrices)
        self.btn_resultado_resta.clicked.connect(self.resta_matrices)
        self.btn_resultado_multiplicacion.clicked.connect(self.multiplicacion_de_matrices)
        self.btn_resultado_inversa.clicked.connect(self.matriz_inversa)
        self.btn_resultado_rango.clicked.connect(self.rango_matriz)
        self.btn_resultado_determinante.clicked.connect(self.determinante_matriz)
        self.btn_resultado_ecuaciones.clicked.connect(self.ecuaciones)
        self.btn_resultado_markov.clicked.connect(self.cadena_markov)
        self.btn_resultado_incriptacion.clicked.connect(self.incriptacion)
        self.btn_resultado_incriptacion_2.clicked.connect(self.cuadrados_medios_)
        self.btn_resultado_incriptacion_3.clicked.connect(self.productos_medios_)
        self.btn_resultado_incriptacion_4.clicked.connect(self.multiplicador_constante_)

    def hide_menu(self):
        self.btn_hide_menu.hide()
        self.btn_show_menu.show()
        self.frame_menu.hide()

    def show_menu(self):
        self.btn_hide_menu.show()
        self.btn_show_menu.hide()
        self.frame_menu.show()

    def change_page_operaciones(self):
        self.stackedWidget.setCurrentWidget(self.page_operaciones)

    def change_page_al(self):
        self.stackedWidget.setCurrentWidget(self.page_al)

    def change_page_suma(self):
        self.stackedWidget_2.setCurrentWidget(self.page_operaciones_suma)

    def change_page_resta(self):
        self.stackedWidget_2.setCurrentWidget(self.page_operaciones_resta)

    def change_page_multiplicacion(self):
        self.stackedWidget_2.setCurrentWidget(self.page_operaciones_multiplicacion)

    def change_page_inversa(self):
        self.stackedWidget.setCurrentWidget(self.page_inversa)

    def change_page_rango(self):
        self.stackedWidget.setCurrentWidget(self.page_rango)

    def change_page_determinante(self):
        self.stackedWidget.setCurrentWidget(self.page_determinante)

    def change_page_ecuaciones(self):
        self.stackedWidget.setCurrentWidget(self.page_ecuaciones)

    def change_page_markov(self):
        self.stackedWidget.setCurrentWidget(self.page_markov)

    def change_page_incriptacion(self):
        self.stackedWidget.setCurrentWidget(self.page_incriptacion)

    def change_page_aleatorio(self):
        self.stackedWidget.setCurrentWidget(self.page_aleatorio)

    def suma_matrices(self):

        # Solicitar dimensiones de las matrices al usuario
        filas = int(self.le_filas.text())
        columnas = int(self.le_columnas.text())

        # Solicitar valores de la primera matriz al usuario
        valores1 = self.le_m1.text().split(",")

        # Solicitar valores de la segunda matriz al usuario
        valores2 = self.le_m2.text().split(",")

        matriz1 = np.array(valores1, dtype=int).reshape(filas, columnas)
        matriz2 = np.array(valores2, dtype=int).reshape(filas, columnas)

        self.lbl_m1.setText(str(matriz1))
        self.lbl_m2.setText(str(matriz2))
        self.lbl_mas.setText('+')
        self.lbl_igual.setText('=')

        # Sumar las matrices
        suma = matriz1 + matriz2

        print("Procedimiento de suma de matrices:")
        for i in range(filas):
            for j in range(columnas):
                print(f"{matriz1[i, j]} + {matriz2[i, j]} = {suma[i, j]}")

        # Imprimir la matriz resultante
        self.lbl_resultado.setText(str(suma))

    def resta_matrices(self):

        # Solicitar dimensiones de las matrices al usuario
        filas = int(self.le_filas_2.text())
        columnas = int(self.le_columnas_2.text())

        # Solicitar valores de la primera matriz al usuario
        valores1 = self.le_m1_2.text().split(",")

        # Solicitar valores de la segunda matriz al usuario
        valores2 = self.le_m2_2.text().split(",")

        matriz1 = np.array(valores1, dtype=int).reshape(filas, columnas)
        matriz2 = np.array(valores2, dtype=int).reshape(filas, columnas)

        self.lbl_m1_2.setText(str(matriz1))
        self.lbl_m2_2.setText(str(matriz2))
        self.lbl_menos_2.setText('-')
        self.lbl_igual_2.setText('=')

        # Sumar las matrices
        resta = matriz1 - matriz2

        print("Procedimiento de resta de matrices:")
        for i in range(filas):
            for j in range(columnas):
                print(f"{matriz1[i, j]} - {matriz2[i, j]} = {resta[i, j]}")

        # Imprimir la matriz resultante
        self.lbl_resultado_2.setText(str(resta))

    def multiplicacion_de_matrices(self):

        # Solicitar dimensiones de las matrices al usuario
        filas1 = int(self.le_filas_3.text())
        columnas1 = int(self.le_columnas_3.text())
        filas2 = int(self.le_filas_4.text())
        columnas2 = int(self.le_columnas_4.text())

        # Solicitar valores de la primera matriz al usuario
        valores1 = self.le_m1_3.text().split(",")
        matriz1 = np.array(valores1, dtype=int).reshape(filas1, columnas1)

        # Solicitar valores de la segunda matriz al usuario
        valores2 = self.le_m2_3.text().split(",")
        matriz2 = np.array(valores2, dtype=int).reshape(filas2, columnas2)

        self.lbl_m1_3.setText(str(matriz1))
        self.lbl_m2_3.setText(str(matriz2))
        self.lbl_mas_2.setText('*')
        self.lbl_igual_3.setText('=')

        # Verificar si las matrices son multiplicables
        if columnas1 != filas2:
            self.label_24.setText('Error: Las dimensiones de las matrices no son compatibles para la multiplicación.')

        # Multiplicar las matrices
        producto = np.dot(matriz1, matriz2)

        # Mostrar el procedimiento paso a paso
        print("Procedimiento de multiplicación de matrices:")
        for i in range(filas1):
            for j in range(columnas2):
                multiplicacion = []
                for k in range(columnas1):
                    multiplicacion.append(f"{matriz1[i, k]} * {matriz2[k, j]}")
                print(f"({'+'.join(multiplicacion)}) = {producto[i, j]}")

        # Imprimir la matriz resultante
        self.lbl_resultado_3.setText(str(producto))

    def matriz_inversa(self):
        # Solicitar dimensiones de la matriz al usuario
        filas = int(self.le_filas_7.text())
        columnas = int(self.le_columnas_7.text())

        # Solicitar valores de la matriz al usuario
        valores = self.le_m1_4.text().split(",")
        matriz = np.array(valores, dtype=float).reshape(filas, columnas)

        # Calcular la matriz inversa
        try:
            inversa = np.linalg.inv(matriz)

            # Mostrar el procedimiento paso a paso
            print("Procedimiento para calcular la matriz inversa:")
            print("1. Matriz original:")
            self.label_59.setText(str(matriz))
            self.label_60.setText('--->')
            print(matriz)
            print("2. Matriz adjunta:")
            adjunta = np.linalg.inv(matriz) * np.linalg.det(matriz)
            self.label_61.setText(str(adjunta))
            self.label_64.setText('--->')
            print(adjunta)
            print("3. Matriz adjunta transpuesta:")
            adjunta_transpuesta = np.transpose(adjunta)
            self.label_62.setText(str(adjunta_transpuesta))
            self.label_65.setText('--->')
            print(adjunta_transpuesta)
            print("4. Dividir la matriz adjunta transpuesta entre el determinante:")
            inversa_proceso = adjunta_transpuesta / np.linalg.det(matriz)
            self.label_63.setText(str(inversa))
            print(inversa_proceso)

        except np.linalg.LinAlgError:
            self.label_35.setText('La matriz no tiene inversa')

    def rango_matriz(self):
        # Solicitar dimensiones de la matriz al usuario
        filas = int(self.le_filas_8.text())
        columnas = int(self.le_columnas_8.text())

        # Solicitar valores de la matriz al usuario
        valores = self.le_m1_5.text().split(",")
        matriz = np.array(valores, dtype=float).reshape(filas, columnas)

        # Realizar la eliminación de Gauss-Jordan para determinar el rango
        rango = np.linalg.matrix_rank(matriz)
        pivotes = []

        # Copiar la matriz para evitar modificarla
        matriz_temporal = matriz.copy()

        for i in range(min(filas, columnas)):
            # Buscar un pivote en la columna actual
            pivote_fila = np.argmax(np.abs(matriz_temporal[i:, i])) + i
            pivote = matriz_temporal[pivote_fila, i]

            # Si el pivote es cero, no hay más pivotes y terminamos
            if pivote == 0:
                break

            # Guardar el índice del pivote
            pivotes.append((pivote_fila, i))

            # Intercambiar filas para colocar el pivote en la posición actual
            matriz_temporal[[i, pivote_fila]] = matriz_temporal[[pivote_fila, i]]

            # Hacer ceros en la columna actual
            for j in range(i + 1, filas):
                factor = matriz_temporal[j, i] / pivote
                matriz_temporal[j] -= matriz_temporal[i] * factor

        m = np.round(matriz).astype(int)
        matriz_temp = np.round(matriz_temporal).astype(int)

        self.label_44.setText(str(m))
        self.label_46.setText(str(matriz_temp))
        self.label_48.setText(str(rango))

    def determinante_matriz(self):

        # Solicitar dimensiones de la matriz al usuario
        filas = int(self.le_filas_9.text())
        columnas = int(self.le_columnas_9.text())

        # Solicitar valores de la matriz al usuario
        valores = self.le_m1_6.text().split(",")
        matriz = np.array(valores, dtype=float).reshape(filas, columnas)

        # Realizar la eliminación de Gauss-Jordan para determinar el determinante
        determinante = 1
        matriz_temporal = matriz.copy()

        for i in range(min(filas, columnas)):
            pivote_fila = np.argmax(np.abs(matriz_temporal[i:, i])) + i
            pivote = matriz_temporal[pivote_fila, i]

            if pivote == 0:
                determinante = 0
                break

            if pivote_fila != i:
                matriz_temporal[[i, pivote_fila]] = matriz_temporal[[pivote_fila, i]]
                determinante *= -1

            determinante *= pivote
            matriz_temporal[i] /= pivote

            for j in range(i + 1, filas):
                factor = matriz_temporal[j, i]
                matriz_temporal[j] -= matriz_temporal[i] * factor

        m = np.round(matriz).astype(int)
        self.label_53.setText(str(m))
        mt = np.round(matriz_temporal).astype(int)
        self.label_55.setText(str(mt))
        d = np.round(determinante).astype(int)
        self.label_57.setText(str(d))

    def ecuaciones(self):
        # Solicitar los coeficientes y el vector de términos independientes al usuario

        # Coeficientes de x, y, z de la primera ecuación
        a1, b1, c1, d1 = self.le_filas_10.text().split(",")
        a1, b1, c1, d1 = int(a1), int(b1), int(c1), int(d1)

        # Coeficientes de x, y, z de la segunda ecuación
        a2, b2, c2, d2 = self.le_filas_11.text().split(",")
        a2, b2, c2, d2 = int(a2), int(b2), int(c2), int(d2)

        # Coeficientes de x, y, z de la tercera ecuación
        a3, b3, c3, d3 = self.le_filas_12.text().split(",")
        a3, b3, c3, d3 = int(a3), int(b3), int(c3), int(d3)

        # Construir la matriz y el vector
        matriz_coeficientes = np.array([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
        vector_terminos_independientes = np.array([d1, d2, d3])

        # Calcular el determinante de la matriz principal
        determinante_principal = np.linalg.det(matriz_coeficientes)

        # Calcular el determinante de la matriz con la columna de términos independientes reemplazada
        determinante_x = np.linalg.det(np.column_stack((vector_terminos_independientes, matriz_coeficientes[:, 1:])))
        determinante_y = np.linalg.det(
            np.column_stack((matriz_coeficientes[:, 0], vector_terminos_independientes, matriz_coeficientes[:, 2])))
        determinante_z = np.linalg.det(np.column_stack((matriz_coeficientes[:, :2], vector_terminos_independientes)))

        # Calcular las soluciones
        solucion_x = determinante_x / determinante_principal
        solucion_y = determinante_y / determinante_principal
        solucion_z = determinante_z / determinante_principal

        # Mostrar el procedimiento paso a paso
        self.lbl_m1_6.setText(str(matriz_coeficientes))
        self.lbl_mas_4.setText(str(vector_terminos_independientes))
        self.lbl_m2_6.setText(str(determinante_principal))
        self.lbl_igual_6.setText(str(np.column_stack((vector_terminos_independientes, matriz_coeficientes[:, 1:]))))
        self.lbl_m1_7.setText(str(np.column_stack((matriz_coeficientes[:, 0], vector_terminos_independientes,
                                                   matriz_coeficientes[:, 2]))))
        self.lbl_m1_8.setText(str(np.column_stack((matriz_coeficientes[:, :2], vector_terminos_independientes))))
        self.label_94.setText(str(solucion_x))
        self.label_92.setText(str(solucion_y))
        self.label_97.setText(str(solucion_z))

    def cadena_markov(self):
        # Solicitar al usuario la matriz de transición
        matriz_transicion = self.le_filas_13.text().split(",")

        # Solicitar al usuario el estado inicial
        estado_inicial = self.le_filas_14.text().split(",")

        # Solicitar al usuario el número de pasos
        num_pasos = int(self.le_filas_15.text())

        matriz1 = np.array(matriz_transicion, dtype=float).reshape(3, 3)
        matriz2 = np.array(estado_inicial, dtype=float).reshape(3, 1)

        self.label_103.setText(str(matriz1))
        self.label_105.setText(str(matriz2))

        estado_actual = matriz2

        for paso in range(1, num_pasos + 1):
            estado_siguiente = np.dot(matriz1, estado_actual)
            estado_actual = estado_siguiente
            self.label_106.setText(str(f'Estado despues de {paso} pasos'))
            self.label_37.setText(str(estado_actual))
            print(f'Estado despues de: {paso} pasos\n{estado_actual}')

    def incriptacion(self):

        matriz_clave = self.lbl_matriz.text().split(",")
        matriz_aleatoria = np.array(matriz_clave, dtype=float).reshape(3, 3)
        self.label_113.setText(str(matriz_aleatoria))

        if np.linalg.det(matriz_aleatoria) == 0:
            self.label_111.setText('la matriz clave no tiene inversa')
        else:
            self.label_111.setText('la matriz clave tiene inversa')
            valores = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                       'K': 11, 'L': 12, 'M': 13, 'N': 14, 'Ñ': 15, 'O': 16, 'P': 17, 'Q': 18, 'R': 19,
                       'S': 20, 'T': 21, 'U': 22, 'V': 23, 'W': 24, 'X': 25, 'Y': 26, 'Z': 27, ' ': 28}

            palabra = self.lbl_palabra.text()

            # Obtenemos el valor de cada letra de la palabra
            numeros_asignados = []
            for letra in palabra:
                if letra in valores:
                    numero = valores[letra]
                    numeros_asignados.append(numero)

            num_columnas = (len(numeros_asignados) + 2) // 3  # Calcular el número de columnas

            matriz_frase = np.empty((3, num_columnas), dtype=int)
            self.label_117.setText(str(matriz_frase))

            # Llenar la matriz_frase con los valores de la palabra
            indice = 0
            for j in range(num_columnas):
                for i in range(3):
                    if indice < len(numeros_asignados):
                        matriz_frase[i, j] = numeros_asignados[indice]
                        indice += 1
                    else:
                        matriz_frase[i, j] = 0

            resultado = np.matmul(matriz_aleatoria, matriz_frase)
            self.label_109.setText(str(resultado))

    def cuadrados_medios(self, seed, numeros_aleatorios):
        j = 0
        list_cm = []
        new_seed = str(seed ** 2)

        for z in range(numeros_aleatorios):

            if len(new_seed) < 8:
                new_seed = '0' + new_seed

            for x in new_seed:

                if j == 2 or j == 3 or j == 4 or j == 5:
                    list_cm.append(x)
                j += 1

        first_digit = list_cm[0]
        second_digit = list_cm[1]
        third_digit = list_cm[2]
        four_digit = list_cm[3]

        all_digits = int(first_digit + second_digit + third_digit + four_digit)

        if all_digits == 0:
            raise Exception('La seed no es valida')
        else:
            return all_digits

    def cuadrados_medios_(self):
        numeros_aleatorios = int(self.le_filas_16.text())
        seed = int(self.le_filas_19.text())

        for x in range(numeros_aleatorios):
            new_seed = self.cuadrados_medios(seed, numeros_aleatorios)
            seed = new_seed
            result = seed / 10000
            print('Semilla: ', seed)
            print('Resultado: ', result)

        print('\n')

    def productos_medios(self, seed, second_seed, numeros_aleatorios_2):
        j = 0
        list_pm = []
        new_seed = str(seed * second_seed)

        for z in range(numeros_aleatorios_2):

            if len(new_seed) < 8:
                new_seed = '0' + new_seed

            for x in new_seed:

                if j == 2 or j == 3 or j == 4:
                    list_pm.append(x)
                j += 1

        first_digit = list_pm[0]
        second_digit = list_pm[1]
        third_digit = list_pm[2]

        all_digits = int(first_digit + second_digit + third_digit)

        if all_digits == 0:
            raise Exception('La seed no es valida')
        else:
            return all_digits

    def productos_medios_(self):
        numeros_aleatorios_2 = int(self.le_filas_17.text())
        seed = int(self.le_filas_20.text())
        second_seed = int(self.le_filas_22.text())

        digitos_seed = len(str(seed))
        digitos_second_seed = len(str(second_seed))

        if digitos_seed == digitos_second_seed:
            for x in range(numeros_aleatorios_2):
                new_seed = self.productos_medios(seed, second_seed, numeros_aleatorios_2)
                seed = new_seed
                result = seed / 10000
                print('Semilla: ', seed)
                print('Resultado: ', result)
                seed = second_seed
                second_seed = new_seed
        else:
            print('Las semillas no tienen la misma cantidad de digitos')

        print('\n')

    def multiplicador_constante(self, constante, seed, numeros_aleatorios_3):
        j = 0
        list_mc = []
        new_seed = str(constante * seed)

        for z in range(numeros_aleatorios_3):

            if len(new_seed) < 8:
                new_seed = '0' + new_seed

            for x in new_seed:

                if j == 2 or j == 3 or j == 4 or j == 5:
                    list_mc.append(x)
                j += 1

        first_digit = list_mc[0]
        second_digit = list_mc[1]
        third_digit = list_mc[2]
        four_digit = list_mc[3]

        all_digits = int(first_digit + second_digit + third_digit + four_digit)

        if all_digits == 0:
            raise Exception('La seed no es valida')
        else:
            return all_digits

    def multiplicador_constante_(self):
        numeros_aleatorios_3 = int(self.le_filas_18.text())
        seed = int(self.le_filas_21.text())
        constante = int(self.le_filas_23.text())

        for x in range(numeros_aleatorios_3):
            new_seed = self.multiplicador_constante(constante, seed, numeros_aleatorios_3)
            seed = new_seed
            result = seed / 10000
            print('Semilla: ', seed)
            print('Resultado: ', result)

        print('\n')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

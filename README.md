<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br/>
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br/>
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
        </tr>
    </theader>
    <tbody>
        <tr>
            <td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio / Talleres / Centros de Simulación</td>
        </tr>
        <tr>
            <td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td>
            <td><span style="font-weight:bold;">Código</span>: GUIA-PRLE-001</td>
            <td><span style="font-weight:bold;">Página</span>: 1</td>
        </tr>
    </tbody>
</table>
<span style="font-weight:bold;">INFORME DE LABORATORIO</span><br/>

<table>
    <theader>
        <tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
    </theader>
    <tbody>
        <tr>
            <td>ASIGNATURA:</td>
            <td colspan="5">Progamación Web 2</td>
        </tr>
        <tr>
            <td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Python</td>
        </tr>
        <tr>
            <td>NÚMERO DE PRÁCTICA:</td>
            <td>04</td>
            <td>AÑO LECTIVO:</td>
            <td>2022 A</td>
            <td>NRO. SEMESTRE:</td>
            <td>III</td>
        </tr>
        <tr>
            <td>FECHA DE PRESENTACIÓN:</td>
            <td></td>
            <td>HORA DE PRESENTACIÓN:</td>
            <td colspan="3"></td>
        </tr>
        <tr>
            <td colspan="3">INTEGRANTE(s):
                <ul>
                    <li>Azurin Zuñiga Eberth - eazurin@unsa.edu.pe</li>
                    <li>Cárdenas Martínez Franco - fcardenasm@unsa.edu.pe</li>
                    <li>Carrillo Daza Barbara - bcarrillo@unsa.edu.pe</li>
                    <li>Hancco Condori Bryan - bhanccoco@unsa.edu.pe</li>
                    <li>Velita Aguilar Italo - ivelita@unsa.edu.pe</li>
                </ul>
            </td>
            <td>NOTA:</td>
            <td colspan="2"></td>
        </tr>
        <tr>
            <td colspan="6">DOCENTE(s):
                <ul>
                    <li>Richart Smith Escobedo Quispe - rescobedoq@unsa.edu.pe</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>
</div>

<!-- Reportes -->
## SOLUCIÓN Y RESULTADOS

---

I. SOLUCIÓN DE EJERCICIOS/PROBLEMAS <br>
* Originalmente la carpeta tiene los siguientes archivos
    ```sh
    ├── README.md
    ├── requirements.txt
    └── src
        ├── Ejercicio2a.py
        ├── Ejercicio2b.py
        ├── Ejercicio2c.py
        ├── Ejercicio2d.py
        ├── Ejercicio2e.py
        ├── Ejercicio2f.py
        ├── Ejercicio2g.py
        ├── chessPictures.py
        ├── colors.py
        ├── interpreter.py
        ├── picture.py
        └── pieces.py
    ```
* Sin embargo para poder empezar a trabajar necesitamos instalar el virtual enviroment en otra carpeta aparte en este mismo directorio, la carpeta debe ser llamada "my_env"
    ```sh
    virtualenv -p python my_env
    ```
* Quedara de la siguiente manera
    ```sh
    ├── README.md
    ├── my_env
    │   ├── Lib
    │   ├── Scripts
    │   ├── include
    │   └── pyvenv.cfg
    ├── requirements.txt
    └── src
        ├── Ejercicio2a.py
        ├── Ejercicio2b.py
        ├── Ejercicio2c.py
        ├── Ejercicio2d.py
        ├── Ejercicio2e.py
        ├── Ejercicio2f.py
        ├──Ejercicio2g.py
        ├── chessPictures.py
        ├── colors.py
        ├── interpreter.py
        ├── picture.py
        └── pieces.py
    ```
* Tenemos que instalar pygame dentro del entorno virtual con el archivo requirements.txt
    ```sh
    # On linux
    source ./my_env/bin/activate

    # On Windows
    .\my_env\Scripts\activate
    ```
    ```sh
    (my_env)
    pip install -r requirements.txt
    ```
* Cada uno tenia la tarea de implementar las funciones usando la lógica basada en listas y strings
    * Franco
        1. verticalMirror()
        2. horizontalMirror()
        3. negative()
    * Barbara <!--Dejar el espacio de abajo-->

        4. join(Picture)
        5. up(Picture)
    * Bryan <!--Dejar el espacio de abajo-->

        6. under(Picture)
						*	Primero se declaran las variables necesarias
                ```python
								result = []
      					upperIMG = p.img
      					underIMG = self.img
                ```
						*	Dentro de un bucle anidado se comparan los caracteres de las
							imagenes, dejando el resultado final
                ```python
								if upperIMG[i][j] != underIMG[i][j] and upperIMG[i][j] != " ":
 									txt += upperIMG[i][j]
  							else:
    							txt += underIMG[i][j]
                ```
						*	Finalmente ese resultado se agrega a result, para posteriormente
							enviar el resultado final
                ```python
								for i in range(len(upperIMG)):
									txt = ""
									...
									result.append(txt)
    * Eberth <!--Dejar el espacio de abajo-->

        7. horizontalRepeat(n)
        8. verticalRepeat(n)
    * Italo

        9. rotate()
            * Primero creamos el tamaño de la lista
                ```python
                # Creating all elements of the list
                for value in self.img[0]:
                  rotate.append(value)
                ```
            * Aprovechando lo dicho anteriormente que los [strings son arrays](https://www.w3schools.com/python/python_strings.asp)
                ```python
                i=1; j=0
                while i<len(self.img):
                  while j<len(self.img[i]):
                    rotate[j] = self.img[i][j] + rotate[j]
                    j+=1
                  j=0
                  i+=1
                ```
    
---

II. SOLUCIÓN DEL CUESTIONARIO

<!-- Listas puedes usar "-", "+", "*" -->
* ¿Qué son los archivos *.pyc?
    * Tambien denominado como "Compyled Python File", es donde Python almacena la versión compilada de cada módulo, con el fin de acelerar la velocidad de carga de los módulos.
        ```sh
        module.version.pyc
        ```
<br>

* ¿Para qué sirve el directorio pycache?
    * Es importante debido a que es la carpeta donde se guardan los archivos .pyc, que permiten hacer que la ejecución de los módulos sea mayor
<br>

* ¿Cuáles son los usos y lo que representa el subguión en Python?
    * Los usos del subguión(_) en Python vistos hasta se utilizan en la creación de clases, definiendo al constructor o en el nombre de la carpeta __ pycache__.
    Sin embargo existen  otras aplicaciones, como por ejemplo para evitar conflictos con las palabras clave de Python
    class _= 'Classname', tambien están los métodos Dunder (reservados para uso especial) y los Naame Mangling

---

III. CONCLUSIONES

---

## RETROALIMENTACIÓN GENERAL

---

### REFERENCIAS Y BIBLIOGRAFÍA

<!-- Enlaces -->
* [https://www.w3schools.com/python/python_reference.asp](https://www.w3schools.com/python/python_reference.asp)
* [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
 

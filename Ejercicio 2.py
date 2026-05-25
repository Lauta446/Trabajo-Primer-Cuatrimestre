#-Ejercicio 2: Sistema de Gestión de FACULTAD.

class Estudiante:
    def __init__(self, nombre, apellido, matricula, carrera):
        if not (nombre and apellido and matricula and carrera):
            raise ValueError("Nombre, apellido, matricula y carrera no pueden estar vacios.")
        self.nombre = nombre.strip()
        self.apellido = apellido.strip()
        self.matricula = matricula.strip()
        self.carrera = carrera.strip()
        self.cursos_inscriptos = []

    def agregar_curso(self, codigo):
        if codigo in self.cursos_inscriptos:
            raise ValueError(f"{self.nombre} {self.apellido} ya esta inscripto en {codigo}.")
        self.cursos_inscriptos.append(codigo)

    def quitar_curso(self, codigo):
        if codigo not in self.cursos_inscriptos:
            raise ValueError(f"{self.nombre} {self.apellido} no esta inscripto en {codigo}.")
        self.cursos_inscriptos.remove(codigo)

    def __str__(self):
        if self.cursos_inscriptos:
            return f"{self.nombre} {self.apellido} ({self.matricula}) - {self.carrera} - {', '.join(self.cursos_inscriptos)}"
        return f"{self.nombre} {self.apellido} ({self.matricula}) - {self.carrera} - sin cursos"


class Curso:
    def __init__(self, nombre, codigo, profesor, capacidad):
        if not (nombre and codigo and profesor):
            raise ValueError("Nombre del curso, codigo y profesor no pueden estar vacios")
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser positiva.")
        self.nombre = nombre.strip()
        self.codigo = codigo.strip()
        self.profesor = profesor.strip()
        self.capacidad = capacidad
        self.inscriptos = []

    def inscribir(self, matricula):
        if matricula in self.inscriptos:
            raise ValueError(f"El estudiante {matricula} ya esta inscripto en {self.codigo}")
        if len(self.inscriptos) >= self.capacidad:
            raise ValueError(f"No hay cupos en {self.codigo}")
        self.inscriptos.append(matricula)

    def dar_baja(self, matricula):
        if matricula not in self.inscriptos:
            raise ValueError(f"{matricula} no esta inscripto en {self.codigo}")
        self.inscriptos.remove(matricula)

    def __str__(self):
        return f"{self.codigo} - {self.nombre} ({len(self.inscriptos)}/{self.capacidad})"


class Facultad:
    def __init__(self):
        self._estudiantes = {}
        self._cursos = {}

  
    def agregar_estudiante(self, nombre: str, apellido: str, matricula: str, carrera: str):
        if matricula in self._estudiantes:
            raise ValueError(f"Ya existe un estudiante registrado con la matricula '{matricula}'")
        estudiante = Estudiante(nombre, apellido, matricula, carrera)
        self._estudiantes[matricula] = estudiante
        print(f"Estudiante agregado con exito: {estudiante}")

    def _buscar_estudiante(self, matricula: str) -> Estudiante:
        estudiante = self._estudiantes.get(matricula)
        if not estudiante:
            raise ValueError(f"No se encontro ningun estudiante con la matricula '{matricula}'")
        return estudiante


    def agregar_curso(self, nombre: str, codigo: str, profesor: str, capacidad_maxima: int):
        if codigo in self._cursos:
            raise ValueError(f"Ya existe un curso registrado con el codigo '{codigo}'")
        curso = Curso(nombre, codigo, profesor, capacidad_maxima)
        self._cursos[codigo] = curso
        print(f"Curso agregado con exito: {curso}")

    def _buscar_curso(self, codigo: str) -> Curso:
        curso = self._cursos.get(codigo)
        if not curso:
            raise ValueError(f"No se encontro ningun curso con el codigo '{codigo}'")
        return curso

  
    def inscribir_estudiante(self, matricula: str, codigo: str):
        estudiante = self._buscar_estudiante(matricula)
        curso = self._buscar_curso(codigo)
        curso.inscribir(matricula)
        estudiante.agregar_curso(codigo)
        print(f"Estudiante '{estudiante.nombre} {estudiante.apellido}' inscripto en '{curso.nombre}'.")

    def dar_baja_estudiante(self, matricula: str, codigo: str):
        estudiante = self._buscar_estudiante(matricula)
        curso = self._buscar_curso(codigo)
        curso.dar_baja(matricula)
        estudiante.quitar_curso(codigo)
        print(f"Estudiante '{estudiante.nombre} {estudiante.apellido}' dado de baja en '{curso.nombre}'.")

  
    def estado_cursos(self):
        print("\nEstado de cursos\n")
   
        if not self._cursos:
            print("No hay cursos registrados")
        else:
            for curso in self._cursos.values():
                print(curso)
                if curso.inscriptos:
                    inscritos = ", ".join(curso.inscriptos)
                    print(f"  Matriculas inscriptas: [{inscritos}]")
        print()

    def estado_estudiantes(self):
        print("\nEstado de estudiantes\n")
    
        if not self._estudiantes:
            print("No hay estudiantes registrados.")
        else:
            for estudiante in self._estudiantes.values():
                print(estudiante)
        print()




def mostrar_menu():
    print("1. Agregar estudiante")
    print("2. Agregar curso")
    print("3. Inscribir estudiante")
    print("4. Dar de baja estudiante")
    print("5. Ver estado de cursos")
    print("6. Ver estado de estudiantes")
    print("0. Salir")


def pedir_dato(campo):
    while True:
        valor = input(f"{campo}: ").strip()
        if valor:
            return valor
        print("No puede quedar vacio")


def pedir_entero(campo):
    while True:
        valor = input(f"{campo}: ").strip()
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        print("Ingresa un numero entero positivo")


def main():
    facultad = Facultad()
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()
        if opcion == "1":
            try:
                nombre = pedir_dato("Nombre")
                apellido = pedir_dato("Apellido")
                matricula = pedir_dato("Matricula")
                carrera = pedir_dato("Carrera")
                facultad.agregar_estudiante(nombre, apellido, matricula, carrera)
            except ValueError as e:
                print("Error:", e)
        elif opcion == "2":
            try:
                nombre = pedir_dato("Nombre del curso")
                codigo = pedir_dato("Codigo del curso")
                profesor = pedir_dato("Profesor encargado")
                capacidad = pedir_entero("Capacidad maxima")
                facultad.agregar_curso(nombre, codigo, profesor, capacidad)
            except ValueError as e:
                print("Error:", e)
        elif opcion == "3":
            try:
                matricula = pedir_dato("Matricula del estudiante")
                codigo = pedir_dato("Codigo del curso")
                facultad.inscribir_estudiante(matricula, codigo)
            except ValueError as e:
                print("Error:", e)
        elif opcion == "4":
            try:
                matricula = pedir_dato("Matricula del estudiante")
                codigo = pedir_dato("Codigo del curso")
                facultad.dar_baja_estudiante(matricula, codigo)
            except ValueError as e:
                print("Error:", e)
        elif opcion == "5":
            facultad.estado_cursos()
        elif opcion == "6":
            facultad.estado_estudiantes()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida")
        input("Presiona Enter para continuar")


if __name__ == "__main__":
    main()

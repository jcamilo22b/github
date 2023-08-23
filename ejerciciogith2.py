#crear clases
class Paciente:
    def __init__(self):
        self.nombre = ""
        self.cc = 0
        self.gen = ""
        self.servicio = ""
    
    # MÉTODO VER
    def verNom(self):
        return self.nombre
    def verSer(self):
        return self.servicio
    def verGen(self):
        return self.gen
    def verCc(self):
        return self.cc
    
    # MÉTODO ASIGNAR
    def asigNom(self, n):
        self.nombre = n
    def asigSer(self, s):
        self.servicio = s
    def asigGen(self, g):
        self.gen = g
    def asigCc(self, c):
        self.cc = c

# Clase para almacenar
class Sistema:
    # Database donde voy a almacenar los datos
    def __init__(self):
        self.database = []
    
    def inserPaciente(self, pat):
        self.database.append(pat)
        return True  #Retorna True si el paciente se insertó correctamente
        
    def verNumPac(self):
        print(f'En la base de datos hay: {str(len(self.database))} pacientes.')
    
    def verDataPaciente(self, c):
        for p in self.database:
            if c == p.verCc():
                return p

def main():
    sis = Sistema()
    while True:
        menu = input('''Elija la opción que desea realizar:
                     1. Ingresar nuevo paciente.
                     2. Ver datos del paciente. 
                     3. Ver número de pacientes.
                     4. Salir.
                     -> ''')
        if menu == '1':
            name = input('Nombre: ')
            cc = int(input('Cédula: '))
            genero = input('Género: ')
            service = input('Servicio: ')
            pac = Paciente()
            pac.asigCc(cc)
            pac.asigGen(genero)
            pac.asigNom(name)
            pac.asigSer(service)
            comprobarP = sis.inserPaciente(pac)
            if comprobarP:
                print('\nPaciente ingresado correctamente.')
            else:
                print('\nError al insertar el paciente.')

        elif menu == '2':
            c = int(input('\nDigite la cédula que está buscando: '))
            p = sis.verDataPaciente(c)
            print(f'''
                Datos del paciente:
                Nombre: {p.verNom()}
                Cédula: {str(p.verCc())}
                Género: {p.verGen()}
                Servicio: {p.verSer()}''')
        
        elif menu == '3':
            sis.verNumPac()
        
        elif menu == '4':
            print('feliz dia.') 
            break
        
        else:
            print('S\neleccione una opción válida.')
    
if __name__ == "__main__":
    main()


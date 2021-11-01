from persona import Persona
from domicilio import Domicilio

if __name__ == '__main__':

    # Persona 1 instancia con el contructor que recibe parametros
    p1 = Persona("Nicolás", "Panella", 23)
    print("Persona1{", p1, "}")

    d1 = Domicilio("Bombal", 918)
    # Agregacion domicilio
    p1.agregarDomicilio(d1)
    print("Persona1{", p1, "}")

    print("---------------------------------------------------------------------------------------------")
    # Persona 2 instancia con los contructores vacios
    p2 = Persona()
    p2.nombre = "Maria"
    p2.apellido = "Lopez"
    p2.edad = 38
    print("Persona2{", p2, "}")

    d2 = Domicilio()
    d2.calle = "Adolfo Calle"
    d2.numero = 123
    # Agregacion domicilio
    p2.agregarDomicilio(d2)
    print("Persona2{", p2, "}")



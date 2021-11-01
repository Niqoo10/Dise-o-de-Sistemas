from persona import Persona
from domicilio import Domicilio

if __name__ == '__main__':
    p1 = Persona("Nicolás", "Panella", 23)
    print("Persona1{", p1, "}")
    d1 = Domicilio("Bombal", 918)
    p1.usarDomicilio(d1, p1)

    p2 = Persona("Alberto", "Cortez", 54)
    print("Persona2{", p2, "}")
    d2 = Domicilio("Adolfo calle", 123)
    p1.usarDomicilio(d2, p2)
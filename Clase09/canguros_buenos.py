class Canguro:
    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = contenido

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

# cangurito = Canguro('gurito')
# madre_canguro = Canguro('Madre')

# madre_canguro.meter_en_marsupio('billetera')
# madre_canguro.meter_en_marsupio('llaves del auto')
# madre_canguro.meter_en_marsupio(cangurito)

# print(madre_canguro.contenido_marsupio)
# print(cangurito.contenido_marsupio)

# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito.

class Cangu:
    def __init__(self, nombre, contenido=None):
        self.nombre = nombre
        if contenido is None:
            contenido = []
        self.marsupio_cont = contenido
    
    def __str__(self):
        return f'{self.nombre} tiene en su marsupio: {self.marsupio_cont}'
    
    def meter_marsupio(self, item):
        self.marsupio_cont.append(item)

madre_canguro = Cangu('Madre')
cangurito = Cangu('gurito')
madre_canguro.meter_marsupio('billetera')
madre_canguro.meter_marsupio('llaves del auto')
madre_canguro.meter_marsupio(cangurito)

print(madre_canguro)
print(cangurito)

# el bug estaba en el metodo __init__, la solucion la saque de StackOverflow
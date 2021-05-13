class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        return len(self.items) == 0

class TorreDeControl:
    def __init__(self):
        self.cola_aterrizaje = Cola()
        self.cola_partida = Cola()
    
    def nuevo_arribo(self, vuelo):
        self.cola_aterrizaje.encolar(vuelo)

    def nueva_partida(self, vuelo):
        self.cola_partida.encolar(vuelo)

    def ver_estado(self):
        print(f'Vuelos esperando para aterrizar: {self.cola_aterrizaje.items}')
        print(f'Vuelos esperando para despegar: {self.cola_partida.items}')

    def asignar_pista(self):
        if not self.cola_aterrizaje.esta_vacia():
            vuelo = self.cola_aterrizaje.desencolar()
            print(f'El vuelo {vuelo} aterrizo con exito.')
        elif self.cola_aterrizaje.esta_vacia() and not self.cola_partida.esta_vacia():
            vuelo = self.cola_partida.desencolar()
            print(f'El vuelo {vuelo} despego con exito.')
        else:
            print('No hay vuelos en espera.')

# TEST
# torre = TorreDeControl()
# torre.nuevo_arribo('AR156')
# torre.nueva_partida('KLM1267')
# torre.nuevo_arribo('AR32')
# torre.ver_estado()
# torre.asignar_pista()
# torre.asignar_pista()
# torre.asignar_pista()
# torre.asignar_pista()
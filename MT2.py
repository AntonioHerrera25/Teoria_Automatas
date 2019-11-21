class tupla_transicion:
    def __init__(self, _estado, _caracter , _direccion):
        self.estado = _estado
        self.caracter = _caracter
        self.direccion = _direccion

class turing_machine:
    def __init__(self, transicion, string_cinta):
        if isinstance(transicion, dict):
            self.tabla_transicion = transicion
        self.cinta = list(string_cinta)
        self.current_state = 'q0'
        self.current_position = 0
    def strart(self):
        result = False
        if self.current_state == 'q0':
            while (self.current_state!= 'Alto' and self.current_state!= 'Si' and self.current_state!= 'No' and self.current_state !='Error'):
                car = self.cinta[self.current_position]
                tupla = "('" + self.current_state + "', '" + car + "')"
                if  tupla in self.tabla_transicion:
                    accion = self.tabla_transicion[tupla]
                    if isinstance(accion, tupla_transicion):
                        self.current_state = accion.estado
                        print(self.cinta[self.current_position], accion.caracter, accion.direccion, accion.estado)
                        self.cinta[self.current_position] = accion.caracter
                        if accion.direccion == 'l':
                            self.current_position = self.current_position - 1
                        else:
                            if accion.direccion == 'r':
                                self.current_position = self.current_position + 1
                            else:
                                if accion.direccion != 'o':
                                    #salida si hay error
                                    self.current_state = 'Error'

        if self.current_state!= 'Alto' or self.current_state!= 'Si' or  self.current_state!= 'No':
            result = True
        return result



MT = dict()

MT["('q0', 'a')"] = tupla_transicion('q1', 'x', 'r')
MT["('q1', 'a')"] = tupla_transicion('q1', 'a', 'r')
MT["('q1', 'b')"] = tupla_transicion('q2', 'y', 'r')
MT["('q2', 'b')"] = tupla_transicion('q2', 'b', 'r')
MT["('q2', 'c')"] = tupla_transicion('q3', 'z', 'r')
MT["('q3', 'c')"] = tupla_transicion('q3', 'c', 'r')
MT["('q3', '@')"] = tupla_transicion('q4', '@', 'l')
MT["('q4', 'c')"] = tupla_transicion('q4', 'c', 'l')
MT["('q4', 'z')"] = tupla_transicion('q4', 'z', 'l')
MT["('q4', 'b')"] = tupla_transicion('q4', 'b', 'l')
MT["('q4', 'y')"] = tupla_transicion('q4', 'y', 'l')
MT["('q4', 'a')"] = tupla_transicion('q4', 'a', 'l')
MT["('q4', 'x')"] = tupla_transicion('q0', 'y', 'r')
MT["('q1', 'y')"] = tupla_transicion('q1', 'y', 'r')
MT["('q2', 'z')"] = tupla_transicion('q2', 'z', 'r')
MT["('q0', 'y')"] = tupla_transicion('q0', 'y', 'r')
MT["('q0', 'z')"] = tupla_transicion('q0', 'z', 'r')
MT["('q0', '@')"] = tupla_transicion('Si', '@', 'r')
MT["('q1', '@')"] = tupla_transicion('Si', '@', 'r')
MT["('q2', '@')"] = tupla_transicion('Si', '@', 'r')
MT["('q1', 'y')"] = tupla_transicion('q1', 'y', 'r')
MT["('q1', 'z')"] = tupla_transicion('q1', 'z', 'r')

MT["('q0', 'c')"] = tupla_transicion('No', 'c', 'r')
MT["('q0', 'x')"] = tupla_transicion('No', 'x', 'r')
MT["('q0', 'b')"] = tupla_transicion('No', 'b', 'r')
MT["('q1', 'c')"] = tupla_transicion('No', 'c', 'r')
MT["('q2', 'a')"] = tupla_transicion('No', 'a', 'r')
MT["('q2', 'x')"] = tupla_transicion('No', 'x', 'r')
MT["('q2', 'y')"] = tupla_transicion('No', 'y', 'r')
MT["('q3', 'a')"] = tupla_transicion('No', 'a', 'r')
MT["('q3', 'b')"] = tupla_transicion('No', 'b', 'r')
MT["('q3', 'x')"] = tupla_transicion('No', 'x', 'r')
MT["('q3', 'y')"] = tupla_transicion('No', 'y', 'r')
MT["('q3', 'z')"] = tupla_transicion('No', 'z', 'r')
MT["('q4', '@')"] = tupla_transicion('No', '@', 'r')


stri = 'aaabbc@'


tm = turing_machine(MT,stri)
result = tm.strart()
print(result)
print(tm.current_state, tm.current_position)
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

MT["('q0', '@')"] = tupla_transicion('q1', '@', 'r')
MT["('q1', '@')"] = tupla_transicion('Si', '@', 'r')
MT["('q1', 'a')"] = tupla_transicion('q2', 'x', 'r')
MT["('q2', 'a')"] = tupla_transicion('q2', 'a', 'r')
MT["('q2', 'b')"] = tupla_transicion('q2', 'b', 'r')
MT["('q2', '@')"] = tupla_transicion('q3', '@', 'l')
MT["('q2', 'y')"] = tupla_transicion('q3', 'y', 'l')
MT["('q3', 'b')"] = tupla_transicion('q4', 'y', 'l')
MT["('q4', 'b')"] = tupla_transicion('q4', 'b', 'l')
MT["('q4', 'a')"] = tupla_transicion('q4', 'a', 'l')
MT["('q4', 'x')"] = tupla_transicion('q5', 'x', 'r')
MT["('q5', 'a')"] = tupla_transicion('q2', 'x', 'r')
MT["('q5', 'b')"] = tupla_transicion('q6', 'y', 'r')
MT["('q5', 'y')"] = tupla_transicion('Si', 'y', 'r')
MT["('q6', 'b')"] = tupla_transicion('q6', 'b', 'r')
MT["('q6', 'a')"] = tupla_transicion('q6', 'a', 'r')
MT["('q6', 'x')"] = tupla_transicion('q7', 'x', 'l')
MT["('q6', 'y')"] = tupla_transicion('q7', 'y', 'l')
MT["('q7', 'a')"] = tupla_transicion('q8', 'x', 'l')
MT["('q8', 'y')"] = tupla_transicion('q9', 'y', 'r')
MT["('q8', 'a')"] = tupla_transicion('q8', 'a', 'l')
MT["('q8', 'b')"] = tupla_transicion('q8', 'b', 'l')
MT["('q9', 'b')"] = tupla_transicion('q6', 'y', 'r')
MT["('q9', 'x')"] = tupla_transicion('q10', 'x', 'l')
MT["('q10', 'y')"] = tupla_transicion('q10', 'y', 'l')
MT["('q10', 'x')"] = tupla_transicion('q10', 'x', 'l')
MT["('q10', '@')"] = tupla_transicion('q11', '@', 'r')
MT["('q11', 'x')"] = tupla_transicion('q12', '1', 'r')
MT["('q12', 'x')"] = tupla_transicion('q12', 'x', 'r')
MT["('q12', 'y')"] = tupla_transicion('q13', 'y', 'r')
MT["('q12', '0')"] = tupla_transicion('Si', '0', 'r')
MT["('q13', 'y')"] = tupla_transicion('q13', 'y', 'r')
MT["('q13', 'x')"] = tupla_transicion('q14', 'x', 'l')
MT["('q13', '0')"] = tupla_transicion('q17', '0', 'l')
MT["('q14', 'y')"] = tupla_transicion('q15', '0', 'l')
MT["('q15', 'x')"] = tupla_transicion('q15', 'x', 'l')
MT["('q15', 'y')"] = tupla_transicion('q15', 'y', 'l')
MT["('q15', '1')"] = tupla_transicion('q16', '1', 'r')
MT["('q16', 'x')"] = tupla_transicion('q12', '1', 'r')
MT["('q16', '0')"] = tupla_transicion('Si', '0', 'r')
MT["('q17', 'y')"] = tupla_transicion('q18', '0', 'l')
MT["('q18', '1')"] = tupla_transicion('Si', '1', 'r')
MT["('q18', 'x')"] = tupla_transicion('Si', 'x', 'r')
MT["('q18', 'y')"] = tupla_transicion('q15', 'y', 'l')

MT["('q1', 'b')"] = tupla_transicion('No', 'b', 'r')
MT["('q3', 'a')"] = tupla_transicion('No', 'a', 'r')
MT["('q3', 'x')"] = tupla_transicion('No', 'a', 'r')
MT["('q9', 'a')"] = tupla_transicion('No', 'a', 'r')
MT["('q16', 'y')"] = tupla_transicion('No', '1', 'l')
MT["('q7', 'y')"] = tupla_transicion('No', 'x', 'l')
MT["('q7', 'b')"] = tupla_transicion('No', 'x', 'l')



stri = '@abab@'


tm = turing_machine(MT,stri)
result = tm.strart()
print(result)
print(tm.current_state, tm.current_position)
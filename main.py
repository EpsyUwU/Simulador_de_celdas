import random


class SolarCell:
    def __init__(self):
        self.electrons = 0 #cantidad inicial de electrones

    def absorb_electrons(self, count): # Este método simula la absorción de electrones por parte de la celda solar.
        self.electrons += count * 0.7

    def reflect_electrons(self, count):# Este método simula el reflejo de electrones por parte de la celda solar.
        return count * 0.1

    def lose_electrons(self, count): # Este método simula la pérdida de electrones por parte de la celda solar
        return count * 0.2


def simulate_cells(num_cells, num_electrons, simulation_time):
    cells = [SolarCell() for _ in range(num_cells)]# Este bucle ejecutara SolarCell() dependiendo del numero de celdas que haya

    for time_step in range(simulation_time): #Este bucle funciona en funcion del tiempo que le hayamos pedido
        for _ in range(num_electrons): #
            current_cell = random.choice(cells) #selecciona aleatoriamente una celda solar (SolarCell) de la lista cells y la asigna a la variable current_cell. Esto simula el hecho de que en cada iteración del bucle se está interactuando con una celda solar aleatoria.
            current_electrons = current_cell.electrons + 1 #selecciona aleatoriamente una celda solar (SolarCell) de la lista cells y la asigna a la variable current_cell. Esto simula el hecho de que en cada iteración del bucle se está interactuando con una celda solar aleatoria.

            current_cell.absorb_electrons(1) # Esta línea llama al método absorb_electrons de la celda seleccionada y le pasa un valor de 1. En el método absorb_electrons, se añade el 70% de los electrones pasados como argumento a la cantidad total de electrones de la celda. Esto simula la absorción del electrón recién llegado por parte de la celda.
            current_cell.electrons += current_cell.reflect_electrons(current_electrons) # Aquí se llama al método reflect_electrons de la celda y se le pasa current_electrons como argumento. En el método reflect_electrons, se calcula el 10% de los electrones recibidos y se retorna el valor, que se suma a la cantidad total de electrones en la celda. Esto simula la parte de los electrones que se reflejan hacia otra celda.
            current_cell.electrons -= current_cell.lose_electrons(current_electrons) #Esta línea llama al método lose_electrons de la celda y se le pasa current_electrons como argumento. En el método lose_electrons, se calcula el 20% de los electrones recibidos y se retorna el valor, que se resta de la cantidad total de electrones en la celda. Esto simula la parte de los electrones que se pierden y no llegan a ninguna otra celda.

    return [cell.electrons for cell in cells]


if __name__ == "__main__":
    num_cells = 9
    num_electrons = 50
    simulation_time = 10  # Definimos el tiempo de simulación (número de pasos de tiempo)

    final_electrons = simulate_cells(num_cells, num_electrons, simulation_time) #Mando la informacion de los primeros 3 parametros
    print(final_electrons)

# Lo que falta
# Un cubo con los resultados de la simulacion libreria de videos, poisson en la llegada de los electrones.
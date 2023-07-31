import math
import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from copy import deepcopy
import imageio
import pygame
import numpy as np

class SolarCell:
    def __init__(self):
        self.electrons = 0  # cantidad inicial de electrones

    def absorb_electrons(self, count):
        # La celda absorbe el 50% de los electrones que llegan, pero no más de 1000 electrones.
        absorbed_electrons = min(count * 0.5, 1000 - self.electrons)
        self.electrons += absorbed_electrons

    def reflect_electrons(self, count):
        # La celda refleja el 30% de los electrones que llegan, pero no más de 1000 electrones.
        reflected_electrons = min(count * 0.3, 1000 - self.electrons)
        self.electrons += reflected_electrons

    def lose_electrons(self, count):
        return count * 0.2  # La celda pierde el 20% de los electrones que llegan.




def poisson_random(avg):
    L = math.exp(-avg)
    p = 1.0
    k = 0

    while True:
        k += 1
        p *= random.uniform(0, 1)
        if p <= L:
            break

    return k - 1



def simulate_cells(num_cells, num_electrons, simulation_time):
    cells = [SolarCell() for _ in range(num_cells)]
    time_steps_per_second = 10  # Simulamos 10 time steps por cada segundo
    result = []

    for time_step in range(simulation_time * time_steps_per_second):
        # Creamos una copia profunda de las celdas antes de cada segundo para simular de manera independiente
        current_cells = [deepcopy(cell) for cell in cells]

        for cell, current_cell in zip(cells, current_cells):
            num_electrons_arrived = poisson_random(num_electrons)
            for _ in range(num_electrons_arrived):
                current_electrons = current_cell.electrons + 1

                current_cell.absorb_electrons(1)
                current_cell.reflect_electrons(current_electrons)
                current_cell.electrons -= current_cell.lose_electrons(current_electrons)

        # Guardamos el estado actual de las celdas en cada segundo
        if time_step % time_steps_per_second == 0:
            result.append([cell.electrons for cell in current_cells])

    return result


def plot_results(results):
    num_seconds = len(results)
    num_cells = len(results[0])
    x = list(range(num_cells))

    fig, ax = plt.subplots()
    ax.set_ylim(0, max(max(arr) for arr in results) * 1.1)
    ax.set_xlabel('Celdas Solares')
    ax.set_ylabel('Cantidad de Electrones')

    lines, = ax.plot(x, results[0], 'o-')

    def update(frame):
        ax.set_title(f'Segundo {frame + 1}')
        lines.set_data(x, results[frame])
        return lines,

    ani = FuncAnimation(fig, update, frames=num_seconds, interval=1000)
    plt.show()

    return ani


def save_animation_as_video(results, filename):
    num_seconds = len(results)
    num_cells = len(results[0])
    x = list(range(num_cells))

    fig, ax = plt.subplots()
    ax.set_ylim(0, max(max(arr) for arr in results) * 1.1)
    ax.set_xlabel('Celdas Solares')
    ax.set_ylabel('Cantidad de Electrones')

    lines, = ax.plot(x, results[0], 'o-')

    def update(frame):
        ax.set_title(f'Segundo {frame + 1}')
        lines.set_data(x, results[frame])
        return lines,

    ani = FuncAnimation(fig, update, frames=num_seconds, interval=1000)

    # Generar las imágenes para cada frame de la animación y almacenarlas en una lista
    images = []
    for frame in range(num_seconds):
        update(frame)
        fig.canvas.draw()
        image = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        images.append(image)

    # Guardar la lista de imágenes como un archivo de video utilizando imageio
    imageio.mimsave(filename, images, fps=1)


def save_animation_as_video(results, filename):
    num_seconds = len(results)
    num_cells = len(results[0])
    x = list(range(num_cells))

    fig, ax = plt.subplots()
    ax.set_ylim(0, max(max(arr) for arr in results) * 1.1)
    ax.set_xlabel('Celdas Solares')
    ax.set_ylabel('Cantidad de Electrones')

    lines, = ax.plot(x, results[0], 'o-')

    def update(frame):
        ax.set_title(f'Segundo {frame + 1}')
        lines.set_data(x, results[frame])
        return lines,

    ani = FuncAnimation(fig, update, frames=num_seconds, interval=1000)

    # Generar las imágenes para cada frame de la animación y almacenarlas en una lista
    images = []
    for frame in range(num_seconds):
        update(frame)
        fig.canvas.draw()
        image = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

        # Voltear la imagen verticalmente
        image = np.flipud(np.rot90(image))

        images.append(image)

    # Guardar la lista de imágenes como un archivo de video utilizando imageio
    imageio.mimsave(filename, images, fps=1)

    # Reproducir el video utilizando pygame
    pygame.init()
    screen = pygame.display.set_mode((fig.canvas.get_width_height()[0], fig.canvas.get_width_height()[1]))
    pygame.display.set_caption("Video de la animación")
    clock = pygame.time.Clock()

    for image in images:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        surf = pygame.surfarray.make_surface(image)
        screen.blit(surf, (0, 0))
        pygame.display.flip()
        clock.tick(1)  # Ajusta la velocidad de reproducción según lo desees (1 fps en este caso)


if __name__ == "__main__":
    num_cells = 9
    num_electrons = 50
    simulation_time = 10  # Definimos el tiempo de simulación (número de pasos de tiempo)

    simulation_results = simulate_cells(num_cells, num_electrons, simulation_time)

    for i, arr in enumerate(simulation_results, start=1):
        print(f"Segundo {i}: {arr}")

    # Guardar y reproducir los resultados como un archivo de video
    save_animation_as_video(simulation_results, "simulation_results.mp4")
# Lo que falta
# Un cubo con los resultados de la simulacion libreria de videos, poisson en la llegada de los electrones.
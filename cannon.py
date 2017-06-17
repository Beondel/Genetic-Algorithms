import math
import random
import numpy as np
import matplotlib.pyplot as plt


class Cannon:
    def __init__(self, theta, velocity):
        self.theta = theta * math.pi / 180
        self.v = velocity
        self.d = ((self.v ** 2) * math.sin(2 * theta)) / (9.8)
        d2 = self.d / 2
        self.max_h = (d2 * math.tan(self.theta)) - (((9.8) * (d2 ** 2)) /
                                                    (2 * ((self.v * math.cos(self.theta)) ** 2)))

    def fitness(self):
        return math.sqrt((1500 - self.d) ** 2)

    def reproduce(self):
        newTheta = self.theta + 0.1 if random.randint(0, 1) == 0 else self.theta - 0.1
        newV = self.v + 0.1 if random.randint(0, 1) == 0 else self.v - 0.1
        if newTheta > 90:
            newTheta = 89
        elif newTheta < 0:
            newTheta = 1
        if newV == 0:
            newV = 1
        return Cannon(newTheta, newV)


def cull(pop):
    cutoff = average_fitness(pop)
    fitPop = []
    for i in pop:
        if i.fitness() < cutoff:
            fitPop.append(i)
            fitPop.append(i.reproduce())
    return fitPop


def average_fitness(pop):
    totalFitness = 0
    for i in pop:
        totalFitness += i.fitness()
    cutoff = totalFitness / 100
    return cutoff


def average_distance(pop):
    totalFitness = 0
    for i in pop:
        totalFitness += i.d
    cutoff = totalFitness / 100
    return cutoff


def initialize_population():
    pop = []
    for i in range(0, 100):
        pop.append(Cannon(random.randint(1, 90), random.randint(1, 1000)))
    return pop


if __name__ == "__main__":
    x = []
    y = []
    population = initialize_population()
    x.append(0)
    y.append(average_distance(population))
    for i in population:
        print(i.fitness())
    for i in range(1, 15):
        population = cull(population)
        x.append(i)
        y.append(average_distance(population))
        for j in population:
            print(j.fitness())
    plt.scatter(x, y)
    plt.show()

import turtle
import random
import numpy as np

# Set up the screen for Turtle graphics
screen = turtle.Screen()
screen.title("Traveling Salesperson Problem with Genetic Algorithm")
screen.setup(width=550, height=600)
screen.bgpic("e3.png")
screen.bgcolor("#e0f2fe")

# Set up the Turtle graphics
t = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t.up()
t3.hideturtle()
t2.hideturtle()

t2.up()
t2.goto(-350,330)
t2.color("#0c4a6e")
t2.write("✈️Traveling Salesperson Problem with Genetic Algorithm ✈️",font=("Arial" , 20 , "bold"))
t2.up()


for i in range(5):
     t2.goto(350,-250+(i*100))
     t2.write("✈️",font=("Arial" , (i*20) , "bold"))


def generate_egypt_cities(num_cities):
     min_x, max_x = -220, 280  
     min_y, max_y = -220, 280
     return [(random.randint(min_x, max_x), random.randint(min_y, max_y)) for _ in range(num_cities)]

# Draw cities as dots on the map
def draw_cities(cities):
     for city in cities:
          t.goto(city)
          t.dot(10, '#38bdf8')


def distance(city1, city2):
     return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def route_length(cities, route):
     total_distance = 0
     for i in range(len(route)):
          total_distance += distance(cities[route[i]], cities[route[(i + 1) % len(route)]])
     return total_distance

def initial_population(num_routes, num_cities):
     return [random.sample(range(num_cities), num_cities) for _ in range(num_routes)]

#tournament selection
def select_parents(population, fitness_scores, tournament_size):
     tournament = random.sample(list(zip(population, fitness_scores)), tournament_size)
     return min(tournament, key=lambda x: x[1])[0]

# ordered crossover between two parents
def ordered_crossover(parent1, parent2):
     size = len(parent1)
     start, end = sorted(random.sample(range(size), 2))
     child = [None]*size
     child[start:end] = parent1[start:end]
     p2_filtered = [x for x in parent2 if x not in child[start:end]]
     child = [p2_filtered.pop(0) if x is None else x for x in child]
     return child

def mutate(route, mutation_rate):
     route = route[:]
     if random.random() < mutation_rate:
          i, j = random.sample(range(len(route)), 2)
          route[i], route[j] = route[j], route[i]
     return route


def genetic_algorithm(cities, num_generations, population_size, mutation_rate):
     population = initial_population(population_size, len(cities))
     best_route = None
     best_length = float('inf')

     j = 0
     for i in range(num_generations):
          fitness_scores = [route_length(cities, route) for route in population]
          new_population = []
          

          for _ in range(population_size):
               parent1 = select_parents(population, fitness_scores, 5)
               parent2 = select_parents(population, fitness_scores, 5)
               child = ordered_crossover(parent1, parent2)
               child = mutate(child, mutation_rate)
               new_population.append(child)

          population = new_population
          current_best = min(fitness_scores)
          if current_best < best_length:
               best_length = current_best
               best_route = population[fitness_scores.index(current_best)]
               t2.up()
               t2.goto(-700,220-j*90)
               j += 1
               print(f"Generation #{i}:\nroute length= {best_length}")
               t2.write(f"🔷Generation:{i}:\nroute length= {best_length}\n🛻🛻🛻🛻🛻🛻🛻🛻🛻🛻🛻🛻🛻🛻🛻🛻🛻" , font=("Arial" , 15 , "bold"))
               draw_route(cities, best_route)
               print("______________________________________________________________________________________")

     return best_route, best_length

def draw_route(cities, route):
     t.clear()  
     draw_cities(cities)  
     t.pendown()
     t.color('#0c4a6e')
     first_city = True
     for i in route:
          if first_city:
               t.penup()  
               t.goto(cities[i])
               t.pendown()  
               t.write("Starting point",font=("Arial" , 10 , "bold"))
               first_city = False
          else:
               t.goto(cities[i])
     t.goto(cities[route[0]])  
     t.penup()
     screen.update() 

def main():
     num_cities = 10
     print("***************************************************************************************")
     cities = generate_egypt_cities(num_cities)
     draw_cities(cities)
     _ , best_length = genetic_algorithm(cities, 100, 200, 0.01)
     print("Best route length:", best_length)
     print("***************************************************************************************")
     turtle.done()

# as well as population size increase the chance of get better solution increase

main()



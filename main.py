import random
import seaborn as sns

class Gym:
    def __init__(self):
        self.dumbbells = [i for i in range(10, 38) if i % 2 == 0]
        self.dumbbells_holder = {}
        self.restart_the_day()

    def restart_the_day(self):
        self.dumbbells_holder = {i: i for i in self.dumbbels}
    
    def lists_dumbbells(self):
        return [i for i in self.dumbbells_holder.values() if i != 0]
    
    def lists_spots(self):
        return [i for i, j in self.dumbbells_holder.items() if j == 0]
    
    def take_dumbbells(self, weight):
        if weight in self.dumbbells_holder.values():
            dumbbells_position = list(self.dumbbells_holder.values()).index(weight)
            key_to_dumbbells = list(self.dumbbells_holder.keys())[dumbbells_position]
            self.dumbbells_holder[key_to_dumbbells] = 0
            return weight
        else:
            return None
    
    def return_dumbbells(self, position, weight):
        if position in self.dumbbells_holder:
            self.dumbbells_holder[position] = weight

    def how_messy(self):
        messy_number = [i for i, j in self.dumbbells_holder.items() if i != j and j != 0]
        return len(messy_number) / len(self.dumbbells_holder)


class User:
    def __init__(self, type, gym):
        self.type = type #1 for regular normal user and 2 for messy disorder user
        self.gym = gym
        self.weight = 0

    def start_training(self):
        weights_list = self.gym.lists_dumbbells()
        if weights_list:
            self.weight = random.choice(weights_list)
            self.gym.take_dumbbells(self.weight)

    def end_training(self): 
        spots = self.gym.lists_spots()

        if self.type == 1:
            if self.weight in spots:
                self.gym.return_dumbbells(self.weight, self.weight)
            else:
                position = random.choice(spots)
                self.gym.return_dumbbells(position, self.weight)

        if self.type == 2:
            position = random.choice(spots)
            self.gym.return_dumbbells(position, self.weight)
        self.weight = 0

gym = Gym()
users = [User(1, gym) for i in range(10)]
users += [User(2, gym) for i in range(1)]
random.shuffle(users)

messy_list = []

for k in range(50):
    gym.restart_the_day()
    for i in range(10):
        random.shuffle(users)
        for user in users:
            user.start_training()
        for user in users:
            user.end_training()
    messy_list.append(gym.how_messy())

print(gym.dumbbells_holder)
print(gym.how_messy())

sns.displot(messy_list)

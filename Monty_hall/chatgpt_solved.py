import random

# Number of simulations to run
num_simulations = 1000000

# Number of times the player wins by switching doors
num_wins_by_switching = 0

# Number of times the player wins by sticking with the original door
num_wins_by_sticking = 0

# Simulate the game num_simulations times
for i in range(num_simulations):
  # Set up the game
  doors = ["empty", "empty", "car"]
  random.shuffle(doors)
  player_door = random.randint(0, 2)
  doors.pop(player_door)
  if player_door == 2:
    doors.pop(random.randint(0, 1))
  else:
    doors = ["empty"]

  # The player sticks with their original door
  if doors[0] == "car":
    num_wins_by_sticking += 1
  else:
    num_wins_by_switching += 1

# Calculate the probability of winning by switching doors
prob_winning_by_switching = num_wins_by_switching / num_simulations

# Calculate the probability of winning by sticking with the original door
prob_winning_by_sticking = num_wins_by_sticking / num_simulations

# Print the results
print("Probability of winning by switching doors: {:.2f}".format(prob_winning_by_switching))
print("Probability of winning by sticking with the original door: {:.2f}".format(prob_winning_by_sticking))
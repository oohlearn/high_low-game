import random
from art import logo, vs
from game_data import data

score = 0
game_over = False


# game start
def game_start():
  print(logo)
  a = random.choice(data)
  print(f'Compare A: {a["name"]}, {a["description"]}, from {a["country"]}.')
  print(vs)
  against = random.choice(data)
  while against == a:
    against = random.choice(data)
  print(
    f'Against B: {against["name"]}, {against["description"]}, from {against["country"]}.'
  )
  return [a, against]


pair = game_start()


# guess and check answer
def compare(pair, score):
  global game_over
  guess = input("Who has more follower? Type 'A' or 'B': ").lower()
  a_follower = pair[0]["follower_count"]
  b_follower = pair[1]["follower_count"]
  if guess == "a" and a_follower > b_follower:
    score += 1
    print(f"You're right! Current score: {score}.")
    return (pair[0], score)
  elif guess == "b" and a_follower < b_follower:
    score += 1
    print(f"You're right! Current score: {score}.")
    return (pair[1], score)
  else:
    print(f"You're wrong. Your final score is {score}.")
    game_over = True
    return (0,0)





  
# next round
def next_round(next_a):
  against = random.choice(data)
  print(f'Compare A: {next_a["name"]}, {next_a["description"]}, from {next_a["country"]}.')
  print(vs)
  while against == next_a:
    against = random.choice(data)
  print(
    f'Against B: {against["name"]}, {against["description"]}, from {against["country"]}.')
  return [next_a, against]

(next_a, score) = compare(pair, score)
while not game_over:
  print("\n")
  print(f"Round {score+1}")
  (next_a, score) = compare(next_round(next_a), score)
  

  



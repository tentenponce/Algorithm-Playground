import random

max_score = 10

fruits = [{
    "name": "Banana",
    "score": 4,
    "chance": 0.0,
    "pick_count": 0
}, {
    "name": "Apple",
    "score": 2,
    "chance": 0.0,
    "pick_count": 0

}, {
    "name": "Cupcake",
    "score": 7,
    "chance": 0.0,
    "pick_count": 0
}]

# get total of fruit scores
sum_of_fruit_scores = 0
for x in range(len(fruits)):
    sum_of_fruit_scores += fruits[x]["score"]

# get the percentage of the score for each fruit
for x in range(len(fruits)):
    fruit_score = fruits[x]["score"]
    fruits[x]["chance"] = fruit_score / sum_of_fruit_scores


# algorithm
def pick_fruit():
    r = random.uniform(0, 1)  # random from 0 to 1 (float)

    index = 0
    while r > 0:  # if random number (0 - 1) is greater than 0, continue
        r -= fruits[index]["chance"]  # get the percentage of the fruit score and deduct 1
        index += 1

    index -= 1
    return fruits[index]  # return the fruit that makes the random number equal or less than 0.


# test
for x in range(1000):
    fruit = pick_fruit()
    fruit["pick_count"] += 1

print(fruits)

import random

max_score = 10

fruits = [{
    "name": "Banana",
    "score": 4,
    "pick_count": 0
}, {
    "name": "Apple",
    "score": 2,
    "pick_count": 0

}, {
    "name": "Cupcake",
    "score": 7,
    "pick_count": 0
}]


def accept_reject():
    fruit_index = random.randint(0, len(fruits) - 1)
    random_fruit = fruits[fruit_index]

    random_score = random.randint(0, max_score)

    if random_score < random_fruit["score"]:
        return random_fruit
    else:
        return accept_reject()


for x in range(100):
    fruit = accept_reject()
    fruit["pick_count"] += 1

print(fruits)

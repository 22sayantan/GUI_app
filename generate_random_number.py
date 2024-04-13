import random

random_list = list()

while (len(random_list)<5):
    random_number = random.randint(1,25)
    if random_number in random_list:
        continue
    else:
        random_list.append(random_number)

random_list = sorted(random_list)
print(random_list)


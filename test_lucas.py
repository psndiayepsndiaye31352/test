import time

MAX_SUM = 500

def explore_best_succession(current_sum, list_action_available, list_action_used, memo):
    tuple_action_available = tuple(list_action_available)  # Convertir en tuple
    if (current_sum, tuple_action_available) in memo:
        return memo[(current_sum, tuple_action_available)]

    best_combination = list_action_used
    best_sum = current_sum

    for elem in list_action_available:
        name, cost = elem
        cost = int(cost)

        if current_sum + cost <= MAX_SUM:
            new_list_action_available = list_action_available[:]
            new_list_action_available.remove(elem)
            new_list_action_used = list_action_used[:]
            new_list_action_used.append(name)

            new_sum, new_combination = explore_best_succession(current_sum + cost, new_list_action_available, new_list_action_used, memo)

            if new_sum > best_sum:
                best_sum = new_sum
                best_combination = new_combination

    memo[(current_sum, tuple_action_available)] = (best_sum, best_combination)
    return best_sum, best_combination

start = time.time()

with open("data.txt") as file:
    list_action = [line.rstrip().split()[:2] for line in file]
    list_action = [tuple(item) for item in list_action]  # Convertir chaque élément en tuple

memo = {}
best_sum, best_combination = explore_best_succession(0, list_action, [], memo)

print("Maximum achievable sum:", best_sum)
print("Combination of actions:", best_combination)

end = time.time()
hours, rem = divmod(end - start, 3600)
minutes, seconds = divmod(rem, 60)
print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))

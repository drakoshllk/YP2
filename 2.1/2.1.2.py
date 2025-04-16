import itertools

def unique_target_combinations(candidates, target):
    target_combinations = []
    for i in range(1, len(candidates) + 1):
        combinations = [sorted(list(combinaton)) for combinaton in itertools.combinations(candidates, i)]
        for combination in combinations:
            if sum(combination) == target and combination not in target_combinations:
                target_combinations.append(combination)
    return target_combinations

candidates, target = [10, 1, 2, 7, 6, 1, 5], 8
print(unique_target_combinations(candidates, target))

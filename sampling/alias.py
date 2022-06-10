# ref: https://qiita.com/kaityo256/items/1656597198cbfeb7328c
# Walker's alias method
import random


def create_alias_table(num_list):
    ave = sum(num_list) / len(num_list)
    num_list = [num / ave for num in num_list]
    small = []
    large = []
    for i in range(len(num_list)):
        if num_list[i] < 1:
            small.append(i)
        else:
            large.append(i)
    index = list(range(len(num_list)))
    while len(small) != 0 and len(large) != 0:
        j = small.pop()
        k = large[-1]
        index[j] = k
        num_list[k] = num_list[k] - (1 - num_list[j])
        if num_list[k] <= 1:
            small.append(k)
            large.pop()
    return index, num_list


def get_index(index, threshold):
    r = random.randint(0, len(index) - 1)
    if threshold[r] > random.uniform(0, 1):
        return r
    else:
        return index[r]


sample = [3, 6, 9, 1, 2, 3, 7, 7, 4, 8]
print(sample)
index, threshold = create_alias_table(sample)
print("i", index)
print("t", threshold)

result = [0] * len(index)
trial = 100000
for _ in range(trial):
    i = get_index(index, threshold)
    result[i] += 1
sum_sample = sum(sample)
print([s / sum_sample for s in sample])
print([r / trial for r in result])

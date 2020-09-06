import random

# random choice / six numbers
def random_choice(n=6, first=None, second=None, third=None, fourth=None, fifth=None):
    range_nums = list(range(1, 46))
    selected_nums = [first, second, third, fourth, fifth]

    if n == 6:
        random_num = random.sample(range_nums, n)
        result  = random_num
        result.sort()
        print(result)

    elif n < 6 and n >=1:
        selected_nums = [i for i in selected_nums if i != None]
        for i in selected_nums:
            range_nums.remove(i)
        random_num = random.sample(range_nums, n)
        result = random_num + selected_nums
        result.sort()
        print(result)

    else:
        print("You can get up to six random numbers for the lottery!")
# times of lottery 


# test
print("TEST 1: n == 6")
random_choice()

print("TEST 2: n == 5 (w/ 35)")
random_choice(5, 35)

print("TEST 3: n == 4 (w/ 24, 17)")
random_choice(4, 24, 17)

print("TEST 4: n == 3 (w/ 12, 41, 9)")
random_choice(3, 12, 41, 9)

print("TEST 5: n == 2 (w/ 7, 26, 33, 38, 40)")
random_choice(2, 7, 26, 33, 38, 40)

print("TEST 6: n == 1 (w/ 10, 7, 26, 33, 38, 40)")
random_choice(1, 7, 26, 33, 38, 40)

print("TEST 7: n == 8")
random_choice(8)

import random

# random choice / six numbers


def random_choice(n=6, first=None, second=None, third=None, fourth=None, fifth=None):
    range_nums = list(range(1, 46))
    selected_nums = [first, second, third, fourth, fifth]

    if n == 6:
        random_num = random.sample(range_nums, n)
        result = random_num
        result.sort()
        return result

    elif n < 6 and n >= 1:
        selected_nums = [i for i in selected_nums if i != None]
        for i in selected_nums:
            range_nums.remove(i)
        random_num = random.sample(range_nums, n)
        result = random_num + selected_nums
        result.sort()
        return result

    else:
        print("You can get up to six random numbers for the lottery!")
# times of lottery


def times_lottery(t, n=6, a=None, b=None, c=None, d=None, e=None):
    if t > 100:
        print("You can get 100 lotteries with six random numbers at a time!")
    else:
        i = 1
        while t != 0:
            if i // 10 == 0:
                three_digit_count = '00' + str(i)
            elif i // 100 == 1:
                three_digit_count = str(i)
            else:
                three_digit_count = '0' + str(i)

            call_result = random_choice(n, a, b, c, d, e)
            result_elem_str = [str(e) for e in call_result]
            result_str = ', '.join(result_elem_str)
            print(three_digit_count + " : " + result_str)

            i += 1
            t -= 1


# test 1: random_choice
# print("TEST 1: n == 6")
# random_choice()

# print("TEST 2: n == 5 (w/ 35)")
# random_choice(5, 35)

# print("TEST 3: n == 4 (w/ 24, 17)")
# random_choice(4, 24, 17)

# print("TEST 4: n == 3 (w/ 12, 41, 9)")
# random_choice(3, 12, 41, 9)

# print("TEST 5: n == 2 (w/ 7, 26, 33, 38, 40)")
# random_choice(2, 7, 26, 33, 38, 40)

# print("TEST 6: n == 1 (w/ 10, 7, 26, 33, 38, 40)")
# random_choice(1, 7, 26, 33, 38, 40)

# print("TEST 7: n == 8")
# random_choice(8)

# test 2: time_lottery
# print("TEST 1: n == 6")
times_lottery(5)



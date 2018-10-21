def palindromic(number):
    answer = str(number)
    return answer == answer[::-1]


def largest_palindromic_number(n_min, n_max):
    k, max_value = 0, 0
    for i in range(n_max, n_min, -1):
        for j in range(n_max, i, -1):
            new_value = i * j
            if new_value > max_value and palindromic(new_value):
                max_value = new_value
                k += 1
        if k > 1:
            break
    return max_value


print(largest_palindromic_number(100, 999))
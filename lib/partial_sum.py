def partial_sum(integer_list, target_sum,  i=0, sum_=0):
    print(i, sum_)
    if target_sum < sum_:
        return False

    if i == len(integer_list):
        return sum_ == target_sum

    if solve(integer_list, target_sum, i + 1, sum_):
        return True

    if solve(integer_list, target_sum, i + 1, sum_ + integer_list[i]):
        return True

    return False


if __name__ == '__main__':
    # n個の整数
    integer_list = [1,3,5,12,7]

    print(partial_sum(integer_list, 11))
    # print(solve(integer_list, 2))
    # => True
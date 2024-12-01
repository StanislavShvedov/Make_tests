def vote(votes):
    count_list = []
    for i in votes:
        count_list.append(votes.count(i))
        if votes.count(i) == max(count_list):
            result = i
    return result


if __name__ == '__main__':
    print(vote([1, 1, 1, 2, 3]))
    print(vote([1, 2, 3, 2, 2]))
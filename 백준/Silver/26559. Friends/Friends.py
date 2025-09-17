sets = int(input())


for set in range(sets):
    dataset = []

    dataset_count = int(input())
    for i  in range(dataset_count):
        name, friends_cnt = input().split()
        friends_cnt = int(friends_cnt)
        dataset.append((name, friends_cnt))
    
    dataset.sort(key=lambda x: x[1], reverse=True)
    print(', '.join([i[0] for i in dataset]))

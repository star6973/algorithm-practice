N, K = map(int, input().split())
bag = dict()
keys_bag = []
for i in range(N):
    W, V = map(int, input().split())
    bag[W] = V
    keys_bag.append(W)

bag = dict(sorted(bag.items(), key=lambda x: x[0]))
keys_bag.sort()

value_bag = []
for i in range(len(keys_bag)):
    a = keys_bag[i]
    b = bag[keys_bag[i]]
    print("i = ", keys_bag[i])
    for j in range(i+1, len(keys_bag)):
        a += keys_bag[j]
        b += bag[keys_bag[j]]
        print("j = ", keys_bag[j])
        if a == K:
            print("같다")
            break
        elif a > K:
            print("커짐")
            a -= keys_bag[j]
            b -= bag[keys_bag[j]]
        else:
            print("진행")
            continue
    value_bag.append(b)
    print()

print(value_bag)
print(max(value_bag))
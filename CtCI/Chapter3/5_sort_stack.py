def stack_sort(stack):
    temp = [] # descendantly sorted

    while stack:
        if not temp:
            temp.append(stack.pop())
            continue

        val = stack.pop()
        if val <= temp[-1]:
            temp.append(val)
            continue

        cnt = 0
        while temp and temp[-1] < val:
            stack.append(temp.pop())
            cnt += 1

        temp.append(val)
        for _ in range(cnt):
            temp.append(stack.pop())

    while temp:
        stack.append(temp.pop())


A = [4,2,6,3,5,6,3,4,5,3,2,4]
stack_sort(A)
print(A)

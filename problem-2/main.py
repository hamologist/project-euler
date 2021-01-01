import fileinput
from typing import List

def fib(lim: int) -> List[int]:
    prev = 1
    cur = 1

    fib_list: List[int] = []
    while cur < lim:
        fib_list.append(cur)
        temp = cur
        cur += prev
        prev = temp

    return fib_list

if __name__ == '__main__':
    user_input: List[str] = [line.strip().split(' ') for line in fileinput.input()][0]
    limit = int(user_input[0])
    fibs = fib(limit)
    ans = 0

    print(fibs)
    for num in fibs:
        if num % 2 == 0:
            ans += num

    print(ans)

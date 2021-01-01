import fileinput
from typing import List

def find_multiples(num: int, lim: int) -> List[int]:
    multis: List[int] = []
    max_multiple = int((lim-1)/num)

    for i in range(1, max_multiple+1):
        multis.append(i*num)

    return multis

if __name__ == '__main__':
    user_input: List[str] = [line.strip().split(' ') for line in fileinput.input()][0]
    limit = int(user_input[0])
    multiples = [int(num) for num in user_input[1:]]

    ref = set()
    ans = 0
    for multiple in multiples:
        ref.update(find_multiples(multiple, limit))

    for multiple in ref:
        ans += multiple

    print(ans)

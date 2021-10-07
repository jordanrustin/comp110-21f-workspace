

def plus_two(y: int, zs: list[int]) -> list[int]:
    global x
    x += 2
    y += 2
    zs[0] += 2
    result: list[int] = [x, y, zs[0]]
    return result


x: int = 1
y: int = 2
zs: list[int] = [3]

print(plus_two(y, zs))
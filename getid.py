def solution(x, y):
    v = y - 1
    g = x + v
    id = (g + 1) * g // 2
    id -= v
    return str(id)

if __name__ == '__main__':
	solution(3, 3)
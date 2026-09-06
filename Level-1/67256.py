def solution(numbers, hand):
    xy = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    cl = xy['*']
    cr = xy['#']
    result = []

    for num in numbers:
        if num in (1, 4, 7):
            result.append('L')
            cl = xy[num]
        if num in (3, 6, 9):
            result.append('R')
            cr = xy[num]
        if num in (2, 5, 8, 0):
            target = xy[num]
            dl = abs(cl[0] - target[0]) + abs(cl[1] - target[1])
            dr = abs(cr[0] - target[0]) + abs(cr[1] - target[1])
            if dl < dr:
                result.append('L')
                cl = target
            if dr < dl:
                result.append('R')
                cr = target
            if dr == dl:
                if hand == 'right':
                    result.append('R')
                    cr = target
                if hand == 'left':
                    result.append('L')
                    cl = target

    return ''.join(result)
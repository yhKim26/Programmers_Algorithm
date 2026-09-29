

def solution(n, times):

    times.sort()
    top_t = times[len(times)-1]
    left_t, right_t = 0, top_t*n
    while left_t < right_t :
        mid_t = (left_t + right_t) // 2
        count_people = 0
        for t in times:
            count_people += mid_t // t

        if count_people >= n:
            right_t = mid_t

        else:
            left_t = mid_t +1

    return right_t

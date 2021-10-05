def solution(total_lambs):
    if total_lambs >10**9:
        return 0
    min_list = []
    x=0
    runningTotal = 0
    while x<= total_lambs:
        current_value = 2**x
        runningTotal += current_value
        min_list.append(current_value)
        if runningTotal >total_lambs:
            break
        x += 1
        #print(min_list)
   
    max_list=[1,1]
    fibrunningtotal = 2
    y=2
    while y<=total_lambs:
        fibrunningtotal += int(max_list[-1]+max_list[-2])
        max_list.append(max_list[-1] + max_list[-2])
        if fibrunningtotal > total_lambs:
            break
        y += 1
    answer = len(max_list) - len(min_list)
    return answer

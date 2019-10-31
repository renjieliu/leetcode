def exclusiveTime(n: int, logs: 'List[str]'):
    # n = 2, logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    reset = -float('inf')
    output = [0] * n
    stk = [reset] * n
    cutoff = []
    prev_run = reset

    for i in logs:
        #print(stk, cutoff, output)
        #break the current string
        info = i.split(':')
        currRun = int(info[0])
        action = info[1]
        action_time = int(info[2])

        if action == "start":
            # cut off the current running function
            if prev_run == reset: #no function is running at the time
                stk[currRun] = action_time
                prev_run = currRun
            else:
                output[prev_run] += action_time-1 - stk[prev_run] + 1 #the execution time for the prev running function, it stops at the previous time slot.
                stk[prev_run] = reset
                cutoff.append(prev_run) #append the prev running function to the stack and
                stk[currRun] = action_time
                prev_run = currRun

        elif action == "end":
            #calculate current function running total
            output[currRun] += action_time - stk[currRun] + 1
            stk[currRun] = reset
            #pop one function for the parked cut-off, and it becomes the running one.
            if len(cutoff) > 0:
                prev_run = cutoff.pop()
                stk[prev_run] = action_time + 1 #it will start from the next timeslot, as it's single threaded, per question.
            else: #no function was previously cutoff
                prev_run = reset

    return output


print(exclusiveTime(n=3, logs=["0:start:0", "1:start:2", "2:start:3",  "2:end:4", "1:end:5", "0:end:9"]))

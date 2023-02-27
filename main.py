import csv
import time
import random
#length, final = map(int, input().split())

def recurse(nums = [1]):
    for i1 in reversed(range(len(nums))):
        n1 = nums[i1]
        if n1*2**(length+1-len(nums)) < final:
            break
        for n2 in nums[:i1+1]:
            suma = n1 + n2
            if suma < nums[-1]:
                continue
            if len(nums) == length:
                if suma == final:
                    return nums + [suma]
                else:
                    continue
            result = recurse(nums + [suma])
            if result:
                return result
    return None

start_time = time.time()
with open('Book1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['number','array'])
    for i in range(0,1):
        #ran = random.randint(2,1000)
        ran = 10001
        for j in range(1,100):
            length = j
            final = ran
            res = recurse()
            if res:
                len_res = len(res)
                writer.writerow([ran, res])
                break
end_time = time.time() - start_time
print(end_time)



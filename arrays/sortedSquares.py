def sortedSquares(nums):
    if len(nums) == 1 :
        return [(nums[0]**2)]

    beg, end = 0, len(nums) - 1
    ret = []
    while(beg <= end):
        if nums[beg]**2 > nums[end]**2 :
            ret.append(nums[beg]**2)
            beg+=1
        else: 
            ret.append(nums[end]**2)
            end-=1
    ret.reverse()
    return ret


print(sortedSquares([-4,-1,0,3,10]))
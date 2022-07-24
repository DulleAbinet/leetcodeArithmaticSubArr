class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        new_bool_List = [True]*len(r)
        for cnt in range(len(r)):
            temp = nums[l[cnt]:r[cnt]+1] 
            temp.sort()
            if len(temp) > 1:
                d = temp[1]-temp[0]                
            t = 2
            while t < len(temp) and len(temp) != 1:   
                if d == temp[t]-temp[t-1]:
                    t +=1
                    continue    
                else:
                    new_bool_List[cnt] = False 
                    break
                
        return new_bool_List

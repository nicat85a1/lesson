"""class py_solution:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(py_solution().is_valid_parenthese("()[]{}"))
print(py_solution().is_valid_parenthese("([)]"))"""

"""class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

print(py_solution().sub_sets([4,5,6]))"""

class py_solution(object):
   def twoSum(self, nums, target_num):      
       """
       :type nums: list[int]
      :type target: int
      :return type: list[int]
      """
       result_dict = dict()
       pos = 0
       while pos < len(nums):
           if (target_num - nums[pos]) not in result_dict:
               result_dict[nums[pos]] = pos
               pos += 1
           else:
               return [result_dict[target_num - nums[pos]], pos]
print(py_solution().twoSum([10,20,10,40,50,60,70],50)) # 2 ve 3 index 50 ye eşit.
print(py_solution().twoSum([10,20,10,40,50,60,70],52))

class py_solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))

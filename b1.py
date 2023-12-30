
def input_target():
    try:
        # Read the length of nums
        length = int(input().strip())

        # Read the nums list
        nums = list(map(int, input().strip().split()))

        # Read the target
        target = int(input().strip())

        return length, nums, target

    except ValueError:
        # Handle the case where input conversion to integer fails
        print("Invalid input. Please enter valid integers.")
        return None


class Solution:
    def searchInsert(self, nums, target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        nums.append(target)
        nums = sorted(nums)      
        for i in range(len(nums)):
            if nums[i]==target:
                return i 
               
if __name__ == "__main__":
    length, nums, target = input_target()
    s = Solution()
    print(s.searchInsert(nums, target))
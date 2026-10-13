def remove_duplicates(nums):
    seen = {}
    for item in nums:
        seen[item] = True
    return list(seen.keys())

def rotate_list(nums, k):
    if not nums:
        return []
    k = k % len(nums)
    return nums[-k:] + nums[:-k]

if __name__ == "__main__":
    print("--- Testing remove_duplicates ---")
    print(remove_duplicates([1, 2, 2, 3, 4, 4]))  
    print(remove_duplicates([3, 1, 3, 2, 1]))    
    print(remove_duplicates([]))                  
    
    print("\n--- Testing rotate_list ---")
    sample_list = [1, 2, 3, 4, 5]
    print(f"Rotate {sample_list} by 2 steps: {rotate_list(sample_list, 2)}")
  

def remove_duplicates(nums):
    unique_items = []
    for item in nums:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items 
if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 4, 4]))  
    print(remove_duplicates([3, 1, 3, 2, 1]))     
    print(remove_duplicates([]))                  

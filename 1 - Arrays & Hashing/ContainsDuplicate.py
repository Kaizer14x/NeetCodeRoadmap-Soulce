def containsDuplicate(self, nums):
    noDuplicate = set()
    for i in nums : 
        if i in noDuplicate : 
            return True
        else : 
            noDuplicate.add(i)
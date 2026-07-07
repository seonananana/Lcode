
class RandomizedSet:

    def __init__(self):

        self.nums = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:

        if val in self.val_to_index:
            return False
        
        # 새로운 값 추가
        self.val_to_index[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:

        if val not in self.val_to_index:
            return False
        
        index_to_remove = self.val_to_index[val]
        last_val = self.nums[-1]
        
        self.nums[index_to_remove] = last_val
        self.val_to_index[last_val] = index_to_remove

        self.nums.pop()
        del self.val_to_index[val]
        
        return True

    def getRandom(self) -> int:
 
        return random.choice(self.nums)
Dynamic Arrays (Python `list`)  
│  
├── **How it works?**  
│   └── Resizes automatically when full (usually doubles capacity).  
│  
├── **Time Complexity**  
│   ├── Access: O(1)  
│   ├── Append: O(1) (amortized)  
│   ├── Insert/Delete at end: O(1)  
│   └── Insert/Delete at middle: O(n) (shifting elements)  
│  
└── **When to use?**  
    └── Need flexible size? Use `list` instead of static arrays.  

Pattern: Dynamic Array Problems
Most array problems in Python use list (dynamic array).

Common operations:

arr = []  
arr.append(1)       # O(1)  
arr.pop()           # O(1)  
arr.insert(0, 5)    # O(n) (slow!)  

Example Problem: Implement a Dynamic Array
Let’s build a simple dynamic array to understand resizing:

class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.array = self._make_array(self.capacity)

    def append(self, element):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)  # Double capacity
        self.array[self.size] = element
        self.size += 1

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def _make_array(self, capacity):
        return [None] * capacity

# Test
arr = DynamicArray()
arr.append(1)
arr.append(2)
print(arr.array)  # [1, 2, None, None] (capacity doubled)
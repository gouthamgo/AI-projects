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
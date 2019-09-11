#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n^2)
```python
a)  a = 0 <-- O(1) constant
    while (a < n * n * n):
      a = a + n * n <-- O(n^2)
```

b) O(n^2)
```python
b)  sum = 0 <-- O(1) constant
    for i in range(n): <-- O(1) linear search
      j = 1 <-- O(1) constant
      while j < n:
        j *= 2 <-- O(n^2)
        sum += 1
```

c)
```python
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

highest_floor(n-story)
  low = 0
  high = n-story - 1
  while (low <= high)
    n-story_mid = (n-story_low + n-story_high) / 2
    if (n-story[])

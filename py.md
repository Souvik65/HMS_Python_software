

# **Sorting & Searching Algorithms in Python**

## **1. Bubble Sort**

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort([5, 2, 8, 3, 1]))
```

---

## **2. Insertion Sort**

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort([5, 2, 8, 3, 1]))
```

---

## **3. Selection Sort**

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([5, 2, 8, 3, 1]))
```

---

## **4. Multilevel Inheritance**

```python
class A:
    def showA(self):
        print("This is A")

class B(A):
    def showB(self):
        print("This is B")

class C(B):
    def showC(self):
        print("This is C")

obj = C()
obj.showA()
obj.showB()
obj.showC()
```

---

## **5. Multiple Inheritance**

```python
class A:
    def showA(self):
        print("This is A")

class B:
    def showB(self):
        print("This is B")

class C(A, B):
    def showC(self):
        print("This is C")

obj = C()
obj.showA()
obj.showB()
obj.showC()
```

---

## **6. Binary Search (Recursive)**

```python
def binary_search(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, mid + 1, high, target)
    else:
        return binary_search(arr, low, mid - 1, target)

nums = [1, 3, 5, 7, 9, 11]
index = binary_search(nums, 0, len(nums) - 1, 7)
print(index)
```


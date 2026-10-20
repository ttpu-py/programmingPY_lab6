# Laboratory Practice n. 6 - Python (Exercises 1-8)

Turin Polytechnic University in Tashkent - Course of Computer Science

Topic: **linear and binary search algorithms**.

---

## First-time Git setup

Before you commit your code, configure your Git username and email.
Run these commands once in your terminal:

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.student.email@example.com"
```

If you do not run these commands, Git can block your commit with an author identity error.

---

## How to start

1. Open this repository in GitHub Codespaces: click **Code -> Codespaces -> Create codespace on main**.
2. Wait for the environment to load. Python installs automatically.
3. Open the file for the exercise, for example `ex1.py`.
4. Write your code below the comment `# Write your solution below.`
5. Click the **Run Python File** button (top-right of the editor) or press the play button.

You can also run any file in the terminal:

```bash
python ex1.py
```

Do not rename the files. Some files already contain data. Use this data in your solution.

---

## How to submit

Run these commands in the terminal:

```bash
git add .
git commit -m "Solve lab 6"
git push
```

We grade only the code on GitHub.

---

## Useful reminders

```python
range(len(my_list))             # indices: 0, 1, 2, ...
(low + high) // 2               # integer division to find the midpoint
my_list.copy()                  # make a copy of a list
my_list.insert(index, value)    # insert a value at a specific index
text.lower()                    # change text to lower case for comparison
my_list[:3]                     # slice the first 3 items of a list
from dataset import ...         # import datasets from dataset.py
```

---

## Exercise 1 - Linear search

Implement the linear search algorithm from scratch. Your goal is to check elements in a list one by one from start to end, locate a target number, and count how many comparisons your code makes along the way.

The data is in `ex1.py`:

```python
numbers = [22, 8, 45, 13, 90, 34, 17, 56, 3, 90]
```

1. Search for the number `34` in `numbers`. Print the index where you found it and how many comparisons you made.
2. Search for `100`. Since it is not in the list, print `-1` and the total comparisons made.
3. Test your search on a larger list: import `large_unsorted_numbers` from `dataset.py` and search for `999999`. Print the result.

Hints:
- Do not use Python's built-in `list.index()` or `in` operator — write your own loop to practice how linear search works.
- Create a counter variable that increases by 1 each time you compare a number.
- Stop your search with `break` or `return` as soon as you find the target.

Output:

```text
Target 34 found at index 5 in 6 steps.
Target 100 not found (-1) in 10 steps.
Large list search: target 999999 not found (-1) in 5000 steps.
```

---

## Exercise 2 - Finding all occurrences

Sometimes a value appears multiple times in a list. Write a program that searches through a list of student names and finds every position where a name appears, rather than stopping at the first match.

The data is in `ex2.py`:

```python
names = [
    "Malika", "Aziz", "Dilnoza", "Sardor", "Aziz",
    "Javohir", "Nigora", "Aziz", "Kamola", "Aziz"
]
```

1. Find all indices where `"Aziz"` appears. Print the list of matching indices and how many times `"Aziz"` was found.
2. Search for `"Dilnoza"`. Print the matching indices and the total count.
3. Search for `"Bekzod"`. If the name does not exist in the list, print `No matches found.`

Hints:
- Start with an empty list: `matches = []`.
- Loop through the list with `for i in range(len(names)):`. Whenever you find a match, append index `i` to your list.
- Check if your list is empty using `if len(matches) == 0:` or `if not matches:`.

Output:

```text
Searching for 'Aziz':
Matches found at indices: [1, 4, 7, 9]
Total occurrences: 4

Searching for 'Dilnoza':
Matches found at indices: [2]
Total occurrences: 1

Searching for 'Bekzod':
No matches found.
```

---

## Exercise 3 - Searching with conditions

Searching is not only about finding exact values; we often need to search for elements that meet a condition. You have a list of student exam marks, and your goal is to find scores that match specific criteria.

The data is in `ex3.py`:

```python
scores = [55, 72, 88, 45, 93, 60, 78, 82, 95, 67]
```

1. Find the first score strictly greater than `90`. Stop your search immediately when you find it. Print the score, its index, and how many scores you checked.
2. Find the lowest (minimum) score and its index without using Python's `min()` function.
3. Find all scores between `70` and `85` (inclusive). Print the matching scores and how many there are.

Hints:
- For step 1, use `break` as soon as you find the first score above 90.
- For step 2, assume `scores[0]` is the lowest so far. Loop through the remaining scores and update your lowest variable whenever you see a smaller value.

Output:

```text
First score > 90: 93 at index 4 (5 comparisons)
Minimum score: 45 at index 3
Scores between 70 and 85: [72, 78, 82] (total: 3)
```

---

## Exercise 4 - Binary search trace

Binary search is much faster than linear search, but it requires the data to be sorted first. Implement binary search and print what happens at each step so you can observe how the algorithm cuts the search space in half.

The data is in `ex4.py`:

```python
sorted_numbers = [3, 8, 13, 17, 22, 34, 45, 56, 71, 90]
```

1. Search for `45` using binary search. At each step, print the step number, the search bounds (`low`, `high`), the middle index `mid`, and the value at `mid`.
2. Search for `20` using binary search. If it is not in the list, print `-1`.

Hints:
- Set `low = 0` and `high = len(arr) - 1`.
- Use a `while low <= high:` loop. Find the middle index using `mid = (low + high) // 2`.
- If the middle value is smaller than the target, search the right half. If it is bigger, search the left half.

Output:

```text
Searching for 45:
Step 1: low=0, high=9, mid=4, value=22
Step 2: low=5, high=9, mid=7, value=56
Step 3: low=5, high=6, mid=5, value=34
Step 4: low=6, high=6, mid=6, value=45
Found 45 at index 6.

Searching for 20:
Step 1: low=0, high=9, mid=4, value=22
Step 2: low=0, high=3, mid=1, value=8
Step 3: low=2, high=3, mid=2, value=13
Step 4: low=3, high=3, mid=3, value=17
Target 20 not found (-1).
```

---

## Exercise 5 - The race: Linear vs Binary Search

Why do we bother sorting data to use binary search? In this exercise, compare how many comparisons linear search and binary search take on a large list of 5,000 sorted numbers.

The data is in `dataset.py`:

```python
from dataset import large_sorted_numbers
```

1. Search for the last number in `large_sorted_numbers`. Count how many comparisons linear search makes, and how many comparisons binary search makes.
2. Search for a missing number (`-999`) using both algorithms and count the comparisons.
3. Print the comparison table.
4. Print a one-sentence conclusion about which algorithm is faster and why.

Hints:
- You can access the last item of any list in Python with `my_list[-1]`.
- Linear search checks elements one by one ($O(n)$).
- Binary search cuts the remaining items in half every step ($O(\log n)$), which takes only about 12-13 steps for 5,000 items!

Output:

```text
List size: 5000 elements

Test 1 - Target near end (35004):
Linear search: 5000 comparisons
Binary search: 13 comparisons

Test 2 - Target not in list (-999):
Linear search: 5000 comparisons
Binary search: 12 comparisons

Conclusion:
Binary search cuts the search space in half in each step (O(log n)).
Linear search checks each element one by one (O(n)).
```

---

## Exercise 6 - Searching names in alphabetical order

Binary search works on any sorted data, including words! In this exercise, search through an alphabetical list of student names. If a name is missing, determine where it belongs in the list.

The data is in `ex6.py`:

```python
sorted_names = [
    "Aziz", "Bekzod", "Dilnoza", "Farrukh", "Jasur",
    "Javohir", "Kamola", "Madina", "Malika", "Nigora",
    "Sanjar", "Sardor", "Shahnoza", "Umida", "Zafar"
]
```

1. Search for `"Malika"` using binary search. Print the index where you found her and how many steps it took.
2. Search for `"bahrom"` (all lower case).
3. If a name is not found, print `-1` and print between which two existing names it belongs.

Hints:
- In Python, string comparisons like `"apple" < "banana"` follow alphabetical order.
- To compare without worrying about capital letters, convert names to lower case with `.lower()`.
- When binary search finishes without finding the target, the `low` pointer shows exactly where the item belongs! Look at `sorted_names[low - 1]` and `sorted_names[low]`.

Output:

```text
Search for 'Malika':
Found at index 8 in 4 steps.

Search for 'bahrom':
Not found (-1).
'bahrom' belongs between 'Aziz' and 'Bekzod'.
```

---

## Exercise 7 - Finding the insertion point

Imagine you have a sorted leaderboard. When a new score arrives, where should it be placed? Use binary search to find the correct index for a new number without sorting the whole list again.

The data is in `ex7.py`:

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
```

1. Search for a target number using binary search.
2. If the number already exists in `numbers`, print its current index.
3. If the number is missing, find the index where it should be inserted so the list remains sorted.
4. Test with these four values:
   - `40` (already exists)
   - `35` (belongs between 30 and 40)
   - `5` (belongs before the first element)
   - `95` (belongs after the last element)
5. For missing numbers, insert each one into a fresh copy of `numbers` and print the updated list.

Hints:
- When binary search finishes without finding the target, the variable `low` is the exact index where the target belongs.
- Use `numbers.copy()` to make a copy before inserting, and use `my_list.insert(index, value)`.

Output:

```text
Target 40: already exists at index 3
List: [10, 20, 30, 40, 50, 60, 70, 80]

Target 35: insert at index 3
Updated list: [10, 20, 30, 35, 40, 50, 60, 70, 80]

Target 5: insert at index 0
Updated list: [5, 10, 20, 30, 40, 50, 60, 70, 80]

Target 95: insert at index 8
Updated list: [10, 20, 30, 40, 50, 60, 70, 80, 95]
```

---

## Exercise 8 - Searching a product catalog

In real applications, data is usually stored as dictionaries. You have an online store catalog with 1,000 products. The catalog is sorted by product `"id"`, but it is **not** sorted by `"category"` or `"price"`. Choose the right search algorithm for each task!

Import `products` in `ex8.py`:

```python
from dataset import products
```

Sample product record:

```python
{"id": 1001, "name": "Mouse #1001", "category": "Electronics", "price": 10.0, "in_stock": False}
```

1. **Search by ID**: The products are sorted by `"id"`. Use **binary search** to find a product:
   - Search for ID `1450` and print its details.
   - Search for ID `9999`. If not found, print `Product 9999 not found.`
2. **Search by Category**: Products are not sorted by category. Use **linear search** to find all items in category `"Electronics"`. Print the total count and the first 3 items.
3. **Search by Price Range**: Use **linear search** to find all products with a price between `$20.0` and `$25.0`. Find and print the cheapest product in this price range.

Hints:
- To access fields of a product dictionary, use `product["id"]` or `product["price"]`.
- In binary search, compare your target ID with `catalog[mid]["id"]`.
- To get the first 3 items of a list in Python, use slicing: `my_list[:3]`.

Output:

```text
--- Search by ID (Binary Search) ---
Found: {'id': 1450, 'name': 'Gym Bag #1450', 'category': 'Sports', 'price': 51.91, 'in_stock': True}
Product 9999 not found.

--- Search by Category (Linear Search) ---
Found 200 products in category 'Electronics'.
First 3 items:
1. Mouse #1001 (Price: $10.0)
2. Keyboard #1006 (Price: $99.95)
3. Monitor #1011 (Price: $180.0)

--- Search by Price Range (Linear Search) ---
Found 27 products between $20.0 and $25.0.
Cheapest in range: Monitor #1091 (Price: $20.0)
```
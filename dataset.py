"""
Laboratory Practice n. 6 - Dataset Module
Turin Polytechnic University in Tashkent - Course of Computer Science

Topic: Linear and Binary Search Algorithms.

This file provides small and large datasets for your exercises.
You can import any variable into your exercise files.

Example:
    from dataset import large_sorted_numbers, products
"""

import random

# Seed for reproducible results across all students
_rng = random.Random(42)

# --- Small datasets (for tracing and simple tests) ---

small_numbers = [22, 8, 45, 13, 90, 34, 17, 56, 3, 90]

names = [
    "Malika", "Aziz", "Dilnoza", "Sardor", "Aziz",
    "Javohir", "Nigora", "Aziz", "Kamola", "Aziz"
]

scores = [55, 72, 88, 45, 93, 60, 78, 82, 95, 67]

small_sorted_numbers = [3, 8, 13, 17, 22, 34, 45, 56, 71, 90]

sorted_names = [
    "Aziz", "Bekzod", "Dilnoza", "Farrukh", "Jasur",
    "Javohir", "Kamola", "Madina", "Malika", "Nigora",
    "Sanjar", "Sardor", "Shahnoza", "Umida", "Zafar"
]

insert_numbers = [10, 20, 30, 40, 50, 60, 70, 80]


# --- Large datasets (for performance comparison and realistic search) ---

# 5,000 sorted unique integers (step ~ 7)
large_sorted_numbers = [10 + i * 7 + (i % 3) for i in range(5000)]

# 5,000 unsorted integers (shuffled copy of large_sorted_numbers)
large_unsorted_numbers = list(large_sorted_numbers)
_rng.shuffle(large_unsorted_numbers)

# Product catalog: 1,000 product records sorted by product 'id'
_categories = ["Electronics", "Books", "Clothing", "Home", "Sports"]
_item_templates = {
    "Electronics": ["Mouse", "Keyboard", "Monitor", "Headphones", "Webcam", "USB Hub", "Speaker", "Charger"],
    "Books": ["Python Guide", "Algorithm Handbook", "Data Science 101", "Math Basics", "Clean Code"],
    "Clothing": ["T-Shirt", "Hoodie", "Cap", "Jacket", "Backpack", "Running Shoes"],
    "Home": ["Desk Lamp", "Ceramic Mug", "Water Bottle", "Notebook", "Pen Set", "Desk Pad"],
    "Sports": ["Jump Rope", "Yoga Mat", "Dumbbell Set", "Fitness Band", "Gym Bag"]
}

products = []
for i in range(1000):
    pid = 1001 + i
    cat = _categories[i % len(_categories)]
    item_list = _item_templates[cat]
    base_name = item_list[(i // len(_categories)) % len(item_list)]
    item_name = f"{base_name} #{pid}"
    price = round(10.0 + ((i * 17) % 190) + ((i % 10) * 0.99), 2)
    products.append({
        "id": pid,
        "name": item_name,
        "category": cat,
        "price": price,
        "in_stock": (i % 6 != 0)
    })


if __name__ == "__main__":
    print("Dataset summary:")
    print(f" - small_numbers: {len(small_numbers)} elements")
    print(f" - names: {len(names)} elements")
    print(f" - scores: {len(scores)} elements")
    print(f" - small_sorted_numbers: {len(small_sorted_numbers)} elements")
    print(f" - sorted_names: {len(sorted_names)} elements")
    print(f" - insert_numbers: {len(insert_numbers)} elements")
    print(f" - large_sorted_numbers: {len(large_sorted_numbers)} elements (min: {large_sorted_numbers[0]}, max: {large_sorted_numbers[-1]})")
    print(f" - large_unsorted_numbers: {len(large_unsorted_numbers)} elements")
    print(f" - products: {len(products)} records (id: {products[0]['id']} to {products[-1]['id']})")
    print("\nSample product record:")
    print(products[0])

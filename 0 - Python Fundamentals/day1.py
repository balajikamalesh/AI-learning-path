"""
Day 1 — Python Fundamentals for JavaScript Developers
Python-to-FDE learning plan

Run:
    python3 day1.py

This file collects the Day 1 examples and exercises in one place.
The customer-management assignment intentionally contains TODOs so you
can implement the functions yourself.
"""

# ============================================================
# 1. VARIABLES AND DATA TYPES
# ============================================================

name = "Balaji"
age = 32
salary = 45000.50
is_active = True
address = None

MAX_CUSTOMERS = 1000  # Uppercase is a convention for constants.

print("\n--- 1. Variables and data types ---")
print(name, age, salary, is_active, address)

# Exercise 1:
x = 10
y = "20"
# Predict the output before running:
print("Exercise 1:", x + int(y)) # 30


# ============================================================
# 2. DATA STRUCTURES
# ============================================================

# Lists — similar to JavaScript arrays
customers_names = ["John", "Jane", "David"]
customers_names.append("Sarah")
print("\n--- 2A. Lists ---")
print("First customer:", customers_names[0]) # First customer: John
print("All customers:", customers_names) # All customers: ['John', 'Jane', 'David', 'Sarah']
print("Number of customers:", len(customers_names)) # Number of customers: 4
print("Contains Balaji?", "Balaji" in customers_names) # Contains Balaji? False

# Slicing: end index is excluded
numbers = [10, 20, 30, 40, 50]
print("First three numbers:", numbers[0:3]) # First three numbers: [10, 20, 30]

# Dictionaries — similar to JavaScript objects
customer = {
    "id": 1,
    "name": "John",
    "age": 28,
    "country": "India"
}
print("\n--- 2B. Dictionaries ---")
print("Customer name:", customer["name"]) # Customer name: John
print("Email, if present:", customer.get("email")) # Email, if present: None
print("Email with default:", customer.get("email", "Not provided")) # Email with default: Not provided

# Tuples — ordered and immutable
coordinates = (10, 20)
print("\n--- 2C. Tuples ---")
print("Coordinates:", coordinates) # Coordinates: (10, 20)

# Sets — unique values
customer_ids = {1, 2, 3, 3, 4}
print("\n--- 2D. Sets ---")
print("Unique customer IDs:", customer_ids) # Unique customer IDs: {1, 2, 3, 4}

# Exercise 2:
# 1. Create a list containing five customer names.
# 2. Add another customer.
# 3. Remove the second customer.
# 4. Print the total number of customers.
# 5. Check whether "Balaji" exists in the list.


# ============================================================
# 3. CONDITIONAL STATEMENTS
# ============================================================

customer_age = 25

print("\n--- 3. Conditionals ---")
if customer_age >= 18:
    print("Adult")
else:
    print("Minor")

# Python logical operators: and, or, not
if customer_age >= 18 and customer_age <= 30:
    print("Young adult")

# Use `is None` to check for None
if address is None:
    print("Address has not been provided")

# Exercise 3:
# Write a program that categorizes a customer by age:
#   Below 18: Minor
#   18–30: Young adult
#   31–50: Adult
#   Above 50: Senior


# ============================================================
# 4. LOOPS
# ============================================================

loop_customers = ["John", "Jane", "David"]

print("\n--- 4. Loops ---")
for customer_name in loop_customers:
    print(customer_name)

# enumerate() gives both index and value
for index, customer_name in enumerate(loop_customers):
    print(index, customer_name)

# range(5) produces 0, 1, 2, 3, 4
for i in range(5):
    print("Range value:", i)

# Exercise 4:
exercise_customers = [
    {"name": "John", "age": 25},
    {"name": "Jane", "age": 32},
    {"name": "David", "age": 45},
    {"name": "Sarah", "age": 19}
]

# TODO: Write a loop that prints only customers whose age is above 30.


# ============================================================
# 5. FUNCTIONS
# ============================================================

def calculate_discount(price, discount):
    """Return the discount amount for a given price and percentage."""
    return price * discount / 100


print("\n--- 5. Functions ---")
print("10% discount on 1000:", calculate_discount(1000, 10))


def greet(person_name, greeting="Hello"):
    """Return a greeting. `greeting` has a default value."""
    return f"{greeting}, {person_name}!"


print(greet("Balaji"))
print(greet("Balaji", "Welcome"))


def create_customer(name, age, country):
    """Example of a function called with keyword arguments."""
    print(name, age, country)


create_customer(name="John", age=30, country="India")


# Exercise 5:
def calculate_average_age(customers):
    # TODO: Calculate and return the average age.
    # Consider what should happen if the list is empty.
    pass


# ============================================================
# 6. CUSTOMER MANAGEMENT SYSTEM — MAIN ASSIGNMENT
# ============================================================

customers = [
    {
        "id": 1,
        "name": "John",
        "age": 28,
        "country": "India",
        "account_status": "active",
        "annual_revenue": 50000
    },
    {
        "id": 2,
        "name": "Jane",
        "age": 35,
        "country": "USA",
        "account_status": "inactive",
        "annual_revenue": 75000
    },
    {
        "id": 3,
        "name": "David",
        "age": 42,
        "country": "India",
        "account_status": "active",
        "annual_revenue": 90000
    },
    {
        "id": 4,
        "name": "Sarah",
        "age": 19,
        "country": "UK",
        "account_status": "active",
        "annual_revenue": 30000
    },
    {
        "id": 5,
        "name": "Michael",
        "age": 55,
        "country": "USA",
        "account_status": "inactive",
        "annual_revenue": 110000
    }
]


def get_active_customers(customers):
    # TODO: Return only customers whose account_status is "active".
    pass


def get_customer_by_id(customers, customer_id):
    # TODO: Find and return the customer with the matching ID.
    # Decide what to return if no customer is found.
    pass


def get_customers_by_country(customers, country):
    # TODO: Return customers belonging to the specified country.
    pass


def get_total_revenue(customers):
    # TODO: Calculate and return total annual revenue.
    pass


# Bonus challenges:
def get_highest_revenue_customer(customers):
    # TODO: Return the customer with the highest annual_revenue.
    pass


def count_customers_by_status(customers):
    # TODO: Count how many customers are active and inactive.
    pass


def get_customers_older_than(customers, minimum_age):
    # TODO: Return customers whose age is greater than minimum_age.
    pass


# Uncomment these calls as you implement each function.
#
# print("\n--- Customer management assignment ---")
# print("Active customers:", get_active_customers(customers))
# print("Customer with ID 1:", get_customer_by_id(customers, 1))
# print("Customers in India:", get_customers_by_country(customers, "India"))
# print("Average age:", calculate_average_age(customers))
# print("Total revenue:", get_total_revenue(customers))
#
# Bonus:
# print("Highest revenue customer:", get_highest_revenue_customer(customers))
# print("Counts by status:", count_customers_by_status(customers))
# print("Customers older than 30:", get_customers_older_than(customers, 30))


# ============================================================
# 7. QUICK REFERENCE
# ============================================================

"""
JavaScript                 Python
------------------------------------------------
const / let                regular assignment
true / false               True / False
null                       None
array.push(value)          list.append(value)
array.length               len(array)
array.includes(value)      value in array
array.slice(0, 2)          array[0:2]
object[key]                dictionary[key]
async function             async def
Promise.all(...)           asyncio.gather(...)
try / catch                try / except
&&                         and
||                         or
!                          not
function                   def
"""

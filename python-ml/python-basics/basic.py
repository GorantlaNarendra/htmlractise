# basics.py

# --- Basic Data Types ---
integer_num = 10          # int
float_num = 3.14          # float
string_text = "Hello, Python!"  # str
boolean_value = True      # bool
list_values = [1, 2, 3, 4, 5]   # list
tuple_values = (10, 20, 30)     # tuple
dict_values = {"name": "Narendra", "age": 25}  # dict

print("Integer:", integer_num)
print("Float:", float_num)
print("String:", string_text)
print("Boolean:", boolean_value)
print("List:", list_values)
print("Tuple:", tuple_values)
print("Dictionary:", dict_values)

print("\n--- For Loop Example ---")
# Print each number in the list
for num in list_values:
    print("Number:", num)

# Using range() in for loop
print("\nNumbers from 1 to 5:")
for i in range(1, 6):
    print(i)

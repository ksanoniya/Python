# data type in python
# Data types in Python define the type of a value.
# Python has several built-in data types, including:

# types of data in python
# buildin data types:
# user defined data types:

# 1. Numeric Types: int, float, complex
# 2. Sequence Types: list, tuple, range 
# 3. Text Type: str
# 4. Mapping Type: dict
# 5. Set Types: set, frozenset
# 6. Boolean Type: bool
# 7. Binary Types: bytes, bytearray, memoryview
# 8. None Type: NoneType

# Examples of numeric types:
my_int = 10          # Integer
my_float = 10.5      # Float
my_complex = 3 + 4j  # Complex number
# Examples of sequence types:
my_list = [1, 2, 3]          # List
my_tuple = (1, 2, 3)         # Tuple
my_range = range(1, 10)      # Range
# Examples of text type:
my_string = "Hello, World!"  # String
# Examples of mapping type:
my_dict = {"key": "value"}   # Dictionary
# Examples of set types:
my_set = {1, 2, 3}            # Set
my_frozenset = frozenset([1, 2, 3])  # Frozenset
# Examples of boolean type:
my_bool_true = True           # Boolean True
my_bool_false = False         # Boolean False
# Examples of binary types:
my_bytes = b"Hello"          # Bytes
my_bytearray = bytearray([1, 2, 3])  # Bytearray
my_memoryview = memoryview(my_bytes)  # Memoryview
# Example of None type:
my_none = None               # NoneType
# You can check the type of a variable using the `type()` function:
print(type(my_int))          # <class 'int'>
print(type(my_float))        # <class 'float'>
print(type(my_complex))      # <class 'complex'>
print(type(my_list))         # <class 'list'>
print(type(my_tuple))        # <class 'tuple'>
print(type(my_range))        # <class 'range'>
print(type(my_string))       # <class 'str'>
print(type(my_dict))        # <class 'dict'>
print(type(my_set))          # <class 'set'>
print(type(my_frozenset))    # <class 'frozenset'>
print(type(my_bool_true))    # <class 'bool'>
print(type(my_bool_false))   # <class 'bool'>
print(type(my_bytes))        # <class 'bytes'>
print(type(my_bytearray))    # <class 'bytearray'>
print(type(my_memoryview))   # <class 'memoryview'>
print(type(my_none))         # <class 'NoneType'>

# You can also convert between different data types using built-in functions:
my_int_to_float = float(my_int)          # Convert int to float
my_float_to_int = int(my_float)          # Convert float to int
my_str_to_int = int("10")                # Convert string to int


# Python String Methods — Reference
Strings are immutable: every method returns a NEW string, never modifies the original.

---

## CASE

```python
s = "  Hello, World!  "
```

#### `upper()` / `lower()` / `title()` / `swapcase()` / `capitalize()` / `casefold()`
```python
print("hello".upper())          # → "HELLO"
print("HELLO".lower())          # → "hello"
print("hello world".title())    # → "Hello World"
print("hello World".swapcase()) # → "HELLO wORLD"
print("hello world".capitalize()) # → "Hello world"  (only first char)
print("RÉSUMÉ".casefold())      # → "résumé"  (aggressive lower, good for comparisons)
```

---

## SEARCHING

```python
text = "the cat sat on the mat"
```

#### `find()` / `rfind()` / `index()` / `rindex()` / `count()`
```python
print(text.find("at"))          # → 5   first occurrence, -1 if missing
print(text.rfind("at"))         # → 20  last occurrence, -1 if missing
print(text.index("at"))         # → 5   like find(), but raises ValueError if missing
print(text.rindex("at"))        # → 20  like rfind(), but raises ValueError if missing
print(text.count("at"))         # → 3   counts non-overlapping occurrences
print(text.count("at", 6))      # → 2   count within a range
```

---

## CHECKING — all return bool

#### `startswith()` / `endswith()` / `isalnum()` / `isalpha()` / `isdigit()` / `isnumeric()` / `isspace()` / `islower()` / `isupper()` / `istitle()`
```python
print("Hello".startswith("He"))     # → True
print("Hello".endswith("lo"))       # → True
print("hello123".isalnum())         # → True   letters and/or digits only
print("hello".isalpha())            # → True   letters only
print("123".isdigit())              # → True   digits only (0–9)
print("123".isnumeric())            # → True   broader: includes ², ³, ½ etc.
print("   ".isspace())              # → True   whitespace only
print("hello world".islower())      # → True
print("HELLO".isupper())            # → True
print("Hello World".istitle())      # → True

# isdigit vs isnumeric edge case
print("²".isdigit())    # → True   (superscript 2 counts as digit)
print("½".isdigit())    # → False
print("½".isnumeric())  # → True   (numeric but not digit)
```

---

## STRIPPING

#### `strip()` / `lstrip()` / `rstrip()`
```python
print(s.strip())        # → "Hello, World!"   removes leading & trailing whitespace
print(s.lstrip())       # → "Hello, World!  " removes leading only
print(s.rstrip())       # → "  Hello, World!" removes trailing only
print("xxHelloxx".strip("x"))  # → "Hello"  strips specific characters
```

---

## REPLACING & REMOVING

#### `replace()` / `expandtabs()`
```python
print("aabbcc".replace("b", "X"))      # → "aaXXcc"  replaces all occurrences
print("aabbcc".replace("b", "X", 1))   # → "aaXbcc"  optional count limit
print("hello\nworld\t!".expandtabs(4)) # replaces \t with spaces (default 8)
```

---

## SPLITTING & JOINING

#### `split()` / `rsplit()` / `splitlines()` / `join()`
```python
print("a,b,c".split(","))          # → ["a", "b", "c"]
print("a,b,c".split(",", 1))       # → ["a", "b,c"]  limit splits
print("a,,b".split(","))           # → ["a", "", "b"]  empty strings preserved
print("  hello  world  ".split())  # → ["hello", "world"]  splits on any whitespace, no empties

print("hello world".rsplit(" ", 1))        # → ["hello", "world"]  split from the right
print("line1\nline2\nline3".splitlines())  # → ["line1", "line2", "line3"]

print(", ".join(["a", "b", "c"]))  # → "a, b, c"
print("".join(["h", "i"]))         # → "hi"
```

---

## PADDING & ALIGNMENT

#### `ljust()` / `rjust()` / `center()` / `zfill()`
```python
print("hi".ljust(10))         # → "hi        "
print("hi".rjust(10))         # → "        hi"
print("hi".center(10))        # → "    hi    "
print("hi".ljust(10, "-"))    # → "hi--------"  custom fill character
print("42".zfill(5))          # → "00042"  zero-pad (useful for numbers)
```

---

## FORMATTING

#### `format()`
```python
print("Hello, {}!".format("world"))           # → "Hello, world!"
print("Hello, {name}!".format(name="world"))  # → "Hello, world!"
name, age = "Alice", 30
print(f"{name} is {age} years old")           # → "Alice is 30 years old"
print(f"{3.14159:.2f}")                        # → "3.14"
```

---

## ENCODING & MISC

#### `encode()` / `decode()`
```python
print("hello".encode("utf-8"))          # → b"hello"  bytes object
print(b"hello".decode("utf-8"))         # → "hello"
```

#### `maketrans()` / `translate()`
```python
print("hello".maketrans("aeiou", "12345"))        # creates translation table
table = str.maketrans("aeiou", "12345")
print("hello world".translate(table))             # → "h2ll4 w4rld"
```

#### misc
```python
print("hello" * 3)         # → "hellohellohello"  repetition
print("hello" + " world")  # → "hello world"      concatenation (use join for many strings)
print(len("hello"))        # → 5
print("hello"[1:4])        # → "ell"  slicing works on strings too
```
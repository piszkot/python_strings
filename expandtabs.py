# Demonstrates the expandtabs() method, which replaces tab characters (\t) with spaces.
# The argument defines the tab stop interval.
# It does NOT simply insert N spaces, but pads the text to the nearest multiple of N.

data = "Name\tAge\tCity\nAlice\t23\tParis\nBob\t7\tLondon"

print("=== Without expandtabs() ===")
print(data)

print("\n=== With expandtabs(8) ===")
print(data.expandtabs(8))

print("\n=== With expandtabs(16) ===")
print(data.expandtabs(16))

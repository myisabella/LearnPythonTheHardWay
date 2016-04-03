formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# Q: Why does %r sometimes print things with single-quote when I wrote them
# with double-quotes?
# A: Python is going to print the strings in the most efficient way it can,
# not replicate exactly the way you wrote them.
def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])

assert count_upper_case("A") == 1
assert count_upper_case("a") == 0
assert count_upper_case("!") == 0
assert count_upper_case(" ") == 0
assert count_upper_case("3") == 0
print ("all tests passed")
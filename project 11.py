def is_group_member(string, s):
    for value in string:
        if s == value:
            return True
    return False


print(is_group_member("Hello", "H"))
print(is_group_member("Good", "f"))


def belongs_to_group(numbers, n):
    for value in numbers:
      if n == value:
          return True
    return False


print(belongs_to_group([11,13,15,14], 15))
print(belongs_to_group([1,2,3,5], 6))









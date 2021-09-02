"""This uses relational operators to test inequalities between two variables."""
__author__ = "730308364"

left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")

left_hand_side = int(left)
right_hand_side = int(right)

greater_than = bool(left_hand_side < right_hand_side)
greater_or_equal = bool(left_hand_side >= right_hand_side)
equal_to = bool(left_hand_side == right_hand_side)
not_equal_to = bool(left_hand_side != right_hand_side)

print(str(left_hand_side) + " < " + str(right_hand_side) + " is " + str(greater_than) )
print(str(left_hand_side) + " >= " + str(right_hand_side) + " is " + str(greater_or_equal) )
print(str(left_hand_side) + " == " + str(right_hand_side) + " is " + str(equal_to) )
print(str(left_hand_side) + " != " + str(right_hand_side) + " is " + str(not_equal_to) )
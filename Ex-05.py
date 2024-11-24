"""""
Problem Statement
Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).
Here's a sample run of the program (user input is in bold italics):
What is the length of side 1? 3
What is the length of side 2? 4
What is the length of side 3? 5.5
The perimeter of the triangle is 12.5
"""""

# Solution :


def main():

    side_01: float = float(input("What is the length of side1 ? "))
    side_02: float = float(input("What is the length of side2 ? "))
    side_03: float = float(input("What is the length of side3 ? "))
    total_length: float = side_01+side_02+side_03
    print(f"The perimeter of triangle is {total_length}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

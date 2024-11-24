"""
Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:
E = m * c**2
Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation. You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.
Here's a sample run of the program (user input is in bold italics):
Enter kilos of mass: 100
e = m * C^2...
m = 100.0 kg
C = 299792458 m/s
8.987551787368176e+18 joules of energy!
"""

# Solution :

C = 299792458


def main():
    print("Delete this line and write your code here! :)")

    mass_in_energy: float = float(input("Enter kilos of mass: "))
    energy_in_joules: float = mass_in_energy * (C**2)
    print("e = m * m C**2...")
    print("m = " + str(mass_in_energy) + "Kgs")
    print("C = " + str(C) + "m/s")
    print(str(energy_in_joules) + "joules of energy")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

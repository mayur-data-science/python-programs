class Polygon:
    """Bluprint for polygon calculation"""

    def __init__(self, no_of_sides=3):
        self._no_of_sides = no_of_sides
        # self.index_cal = 3
        self.type_of_polygons = [
                    "Triangle",
                    "Square",
                    "Pentagon",
                    "Hexagon",
                    "Heptagon",
                    "Octagon",
                    "Nanagon",
                    "Decagon"
                    ]

    def polygon_sides_input(self):
        """Method for user input between 3 to 10 """
        _x = False  # local variable

        while not _x:  # first while loop starts

            self.no_of_sides = input(
                "Enter Total number of sides of polygon :  "
                )

            try:
                self.no_of_sides = int(self.no_of_sides)
                if self.no_of_sides <= 2 or self.no_of_sides >= 11:
                    print(
                      "Please enter total number of polygon sides greater"
                      "than 2 and less than 11"
                      )
                    continue
                break
            except ValueError as ex:
                print(
                    "Please dont enter letters or words only enter number : ",
                    ex)
                # x = False

    def display_polygon_sides(self):
        """Method for displaying which type of polygon it is"""
        if self.no_of_sides == 3:
            print(f"Its Equilateral {self.type_of_polygons[0]}")
        elif self.no_of_sides == 4:
            print(f"Its {self.type_of_polygons[1]}")
        elif self.no_of_sides == 5:
            print(f"its Regular {self.type_of_polygons[2]}")
        elif self.no_of_sides == 6:
            print(f"its Regular {self.type_of_polygons[3]}")
        elif self.no_of_sides == 7:
            print(f"its regular {self.type_of_polygons[4]}")
        elif self.no_of_sides == 8:
            print(f"its regular {self.type_of_polygons[5]}")
        elif self.no_of_sides == 9:
            print(f"its regular {self.type_of_polygons[6]}")
        elif self.no_of_sides == 10:
            print(f"its Regular {self.type_of_polygons[7]}")

    def sum_of_interior_angle(self):
        """Method for calculating sum of all interior angles of polygon"""
        return 180*(self.no_of_sides-2)

    def number_of_diagonals(self):
        """Calculate the diagonals of polygon"""
        return (self.no_of_sides*(self.no_of_sides-3))/2


poly = Polygon()
poly.polygon_sides_input()
poly.display_polygon_sides()
sum_of_interior_angl = poly.sum_of_interior_angle()
print(f"The sum of interior angles of a polygon is : {sum_of_interior_angl}°")
number_of_diagonals = poly.number_of_diagonals()
print(f"number of Diagonal of {poly.type_of_polygons[poly.no_of_sides-3]} : {number_of_diagonals}")

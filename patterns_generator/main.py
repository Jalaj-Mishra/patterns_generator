class Triangle():
    """A class that prints patterns in triangle designs with the given number of rows, and values user wants to print.
    This Class prints only norml traingles with only single value."""
    def __init__(self, rows, cols, spaces, value):
        self.rows = rows
        self.cols = cols
        self.spaces = spaces
        self.value = value

    def RAT(self):
        for row in range(self.rows):
            for col in range(row + 1):
                print(self.value, end=" ")
            print()

    def RRAT(self):
        for row in range(self.rows):
            for cols in range(self.rows - row):
                print(self.value, end=" ")
            print()
    
    def LAT(self):
        for row in range(self.rows):
            for sps in range(self.rows - row - 1):
                print(" ", end=" ")
            for col in range(row+1):
                print(self.value, end=" ")
            print()


    def RLAT(self):
        for row in range(self.rows):
            for sps in range(row):
                print(" ", end=" ")
            for cols in range(self.rows - row):
                print(self.value, end=" ")
            print()
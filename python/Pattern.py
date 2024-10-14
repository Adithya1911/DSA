#  Pattern-1: Rectangular Star Pattern


class Pattern:
    def printRectangularStarPattern(self, number: int) -> None:
        """
        Prints a rectangular star pattern of size nxn.

        Parameters:
        number (int): The size of the square matrix. Must be a positive integer.

        Returns:
        None: The function does not return any value. It prints the star pattern directly.
        """
        for i in range(1, number + 1):
            for j in range(1, number + 1):
                print("*", end="")
            print()
    def printTriangularStarPattern(self, number: int) -> None:
        """
        Prints a triangular star pattern of size nxn.

        Parameters:
        number (int): The size of the square matrix. Must be a positive integer.

        Returns:
        None: The function does not return any value. It prints the star pattern directly.
        """
        for i in range(1, number + 1):
            for j in range(1, i + 1):
                print("*", end=" ")
            print()   

    def printTriangularNumberPattern(self, number: int) -> None:
        """
        Prints a triangular number pattern of size nxn.

        Parameters:
        number (int): The size of the square matrix. Must be a positive integer.

        Returns:
        None: The function does not return any value. It prints the number pattern directly.
        """
        for i in range(1, number + 1):
            for j in range(1, i + 1):
                print(i, end=" ")
            print()


    def printTriangularNumberPattern2(self, number: int) -> None:
        """
        Prints a triangular number pattern of size nxn.

        Parameters:
        number (int): The size of the square matrix. Must be a positive integer.

        Returns:
        None: The function does not return any value. It prints the number pattern directly.
        """
        for i in range(1, number + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()
    
    def printInverseTriangularstar(self,number:int)->None:
        """
        Prints an inverse triangular star pattern of size nxn.
        
        Parameters:
        number (int): The size of the square matrix. Must be a positive integer.
        
        Returns:
        None: The function does not return any value. It prints the star pattern directly.
        """
        for i in range(number, 0, -1):
            for j in range(1, i + 1):
                print("*", end=" ")
            print()
                 
    def printInverseTriangularNumbers(self,number:int)->None:
        """
        Prints an inverse triangular number pattern of size nxn.
        
        Parameters:
        number (int): The size of the square matrix. Must be a positive integer.
        
        Returns:
        None: The function does not return any value. It prints the number pattern directly.
        """
        for i in range(number, 0, -1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()


            
            
def main():
    number=int(input("Enter the value of number N:"))
    pattern = Pattern()
    # pattern.printRectangularStarPattern(number)
    # pattern.printTriangularStarPattern(number)
    # pattern.printTriangularNumberPattern(number)
    # pattern.printTriangularNumberPattern2(number)
    # pattern.printInverseTriangularstar(number)
    pattern.printInverseTriangularNumbers(number)


if __name__ == "__main__":
    main()
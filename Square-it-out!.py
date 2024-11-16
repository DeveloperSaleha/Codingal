def filter_squares(start, end):
    squares = [num ** 2 for num in range(start, end + 1)]
    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]
    print("Square values:", squares)
    print("Even square values:", even_squares)
    print("Odd square values:", odd_squares)
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
filter_squares(start, end)
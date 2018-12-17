track = []
crashed = False
for line in open("Day13Input.txt"):
    if line:  # Create a 2D list with rows and columns
        track.append([char for char in line])

# Up: item 0  Right: item 1  Down: item 2  Left: item 3
directionsRow = [-1, 0, 1, 0]
directionsColumn = [0, 1, 0, -1]


def turnleft(direction):
    return (direction + 3) % 4


def turnright(direction):
    return(direction + 1) % 4


class Cart(object):
    def __init__(self, row, column, direction, intersection):
        self.row = row  # Cart's row (y value)
        self.column = column  # Cart's column (x value)
        self.direction = direction
        self.intersection = intersection


# Identify and add carts
carts = []
for r in range(len(track)):  # For every row in the track
    for c in range(len(track[r])):  # For every column in the track
        if track[r][c] == '^':  # If there is a cart going upwards
            track[r][c] = '|'  # Replace it with a vertical track
            carts.append(Cart(r, c, 0, 0))  # Add it to the carts list
        elif track[r][c] == '>':  # If there is a cart going right
            track[r][c] = '-'  # Replace it with a horizontal track
            carts.append(Cart(r, c, 1, 0))  # Add it to the carts list
        elif track[r][c] == 'v':  # If there is a cart going upwards
            track[r][c] = '|'  # Replace it with a vertical track
            carts.append(Cart(r, c, 2, 0))  # Add it to the carts list
        elif track[r][c] == '<':  # If there is a cart going left
            track[r][c] = '-'  # Replace it with a horizontal track
            carts.append(Cart(r, c, 3, 0))  # Add it to the carts list

while not crashed:  # While there hasn't been a crash
    # Resort the carts (using lambda to sort by row THEN column)
    carts = sorted(carts, key=lambda cart: (cart.row, cart.column))
    for cart in carts:  # Loop through all carts
        newRow = cart.row + directionsRow[cart.direction]  # Work out next row move for cart
        newColumn = cart.column + directionsColumn[cart.direction]  # Work out next column move for cart
        if track[newRow][newColumn] == '\\':  # If the next move is on a left turn ('\\' used to ignore escape chars)
            # If the cart is going up into turn, turn left
            # If it is going right into this turn, turn downwards
            # If it is going down into this turn, turn right
            # If it is going left into this turn, turn upwards
            cart.direction = {0: 3, 1: 2, 2: 1, 3: 0}[cart.direction]
        elif track[newRow][newColumn] == '/':  # If the next move is on a right turn
            cart.direction = {0: 1, 1: 0, 2: 3, 3: 2}[cart.direction]  # Change direction accordingly
        elif track[newRow][newColumn] == '+':  # If the next move is on an intersection
            if cart.intersection == 0:  # And if the cart is on its 1st out of 3 intersections
                cart.direction = turnleft(cart.direction)  # Turn the cart left
            elif cart.intersection == 1:  # If the cart is on its 2nd out of 3 intersections
                pass  # Do nothing
            elif cart.intersection == 2:  # If the cart is on its 3rd out of 3 intersections
                cart.direction = turnright(cart.direction)  # Turn the cart left
            cart.intersection = (cart.intersection + 1) % 3  # Ensure the intersections always stays out of 3
        if (newRow, newColumn) in [(other.row, other.column) for other in carts]:  # If another cart is already there
            carts = [other for other in carts if (other.row, other.column) not in
                     [(cart.row, cart.column), (newRow, newColumn)]]  # Remove both carts from carts list
            print(newColumn, newRow)  # Print where the collision happened
            crashed = True  # Set the crashed flag to true
        # Finally, end the tick and set the cart's row + column to their new values
        cart.row = newRow
        cart.column = newColumn

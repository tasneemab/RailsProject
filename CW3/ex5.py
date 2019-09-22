# checking if the position we works with still in range
def inRange(pos, rowLength, colLength):
    if pos[0] < 0 or rowLength <= pos[0]:
        return False
    elif pos[1] < 0 or colLength <= pos[1]:
        return False
    else:
        return True


# find if there's a legal path as described
def legalPath(mat, pos):
    rowLength = len(mat)
    colLength = len(mat[0])
    up = False
    down = False
    right = False
    left = False
    points = []  # list to save the points in our legal path

    # checking if we got to the end of the matrix, stop condition
    if mat[pos[0]][pos[1]] is 0 and pos[0] == rowLength - 1 and pos[1] == colLength - 1:
        return True

    # checking current position
    if mat[pos[0]][pos[1]] is 0 and inRange(pos, rowLength, colLength):
        points.append(pos)

        # checking to cell below the current one
        updatedPos = (pos[0] + 1, pos[1])
        if inRange(updatedPos, rowLength, colLength) and updatedPos not in points:
            down = legalPath(mat, updatedPos)
            if down:
                points.append(updatedPos)
                return down

        # checking to cell above the current one
        updatedPos = (pos[0] - 1, pos[0])
        if inRange(updatedPos, rowLength, colLength) and updatedPos not in points:
            up = legalPath(mat, updatedPos)
            if up:
                points.append(updatedPos)
                return up

        # checking to cell after the current one
        updatedPos = (pos[0], pos[1] + 1)
        if inRange(updatedPos, rowLength, colLength) and updatedPos not in points:
            right = legalPath(mat, updatedPos)
            if right:
                points.append(updatedPos)
                return right

        # checking to cell before the current one
        updatedPos = (pos[0], pos[1] - 1)
        if inRange(updatedPos, rowLength, colLength) and updatedPos not in points:
            left = legalPath(mat, updatedPos)
            if left:
                points.append(updatedPos)
                return left
        return up or down or right or left

    else:
        return False


def main():
    mat = [[0, 1, 3],
           [0, 3, 2],
           [0, 0, 0]]
    pos = (0, 0)
    print(legalPath(mat, pos))


if __name__ == '__main__':
    main()

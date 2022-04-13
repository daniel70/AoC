from pprint import pprint

pattern = r".#./..#/###"
square = [[0 if c == '.'else 1 for c in line] for line in pattern.split("/")]
pprint(square)
square_90 = [[square[j][i] for j in range(len(square))] for i in range(len(square[0])-1, -1, -1)]
pprint(square_90)
flip = [[square[j][i] for j in range(len(square))] for i in range(len(square[0]))]
pprint(flip)

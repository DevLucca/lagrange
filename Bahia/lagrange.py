def lagrange( x, points ):
    result = 0
    xs = [ ( pos, point[0] ) for pos, point in enumerate( points ) ]
    for pos, point in enumerate( points ): # Itera a lista de pontos, trazendo a tupla do ponto
        result += point[1] * lagrangeParts( x, pos, xs ) # point[1] se refere ao Y

    return result

def lagrangeParts( x, pos, xs ):
    cpxs = list( xs )
    del cpxs[ pos ]
    upPart = [ x - xsone[ 1 ] for xsone in cpxs ]
    downPart = [ xs[pos][1] - xsone[ 1 ] for xsone in cpxs ]
    result = 1
    for x in upPart:
        result *= x  
    data = result
    result = 1
    for x in downPart:
        result *= x
    data /= result
    return data

if __name__ == "__main__":
    try:
        x = 3.7
        points = [(2,65), (3,92), (4,132)]
        print( lagrange( x, points ) )

    except Exception as e:
        print( e )
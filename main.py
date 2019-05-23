size = 10
file = open( '1000.txt' )
i = 0
while True:
    chunk = file.read( size )
    if not chunk:
        break
    i += 1
    if 1 < i and i % size == 1:
        print
    print( chunk )

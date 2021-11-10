import sys


iSize = input( "Enter size of tree[recommend 6 to 64]:" )

#check input is rational
count = 0
while True :
    if float( iSize ) < 0 :
        count = count + 1
        #print (count)
        if count == 2 :
            print( "\n¡Why you no read?!\n")
            sys.exit( "I have better things to do. Go away now!" )
        print( "\nHow can a tree have negative size?\n")
        iSize = input( "Enter size of tree[recommend 6 to 64]:" )
    else:
        break


#Calculate stem before any rounding or truncation
stemLen = int( float( iSize ) / 4 )
stemWidth = int( float( iSize ) / 6 )

#truncate and cast input string to integer for looping and character counts.
size = int( float( iSize ) )

#print top of tree
for cv in range( size ):
    y = cv * "A"
    x = int((size - 1 - cv)/2) * " "
    print( x + y )

#print stem of tree
for cv in range( stemLen ):
    y = "|" * stemWidth
    x = " " * int( ( size * 0.5 - stemWidth * 0.5) )
    print( x + y )
##just appending a comment as a test

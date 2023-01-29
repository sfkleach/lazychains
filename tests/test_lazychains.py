from lazychains import lazychain

"""
A quickly generated set of tests to cover the rush in grabbing the name (oops).
We will backfill these asap.
"""

def test_basic_functionality():
    c = lazychain( "abc" )
    assert "a" == c.head() 
    assert "b" == c[1]
    c = c.tail().tail()
    assert not c.is_expanded()
    assert "c" == c.head() 
    assert c.is_expanded()
    assert not c.tail()
    c = c.new( "first item" )
    assert 2 == len( c )
    assert ['first item', 'c'] == list(c)
    assert 'c' == c[-1]
    c = c.tail().new( 'z' ).new( 'y' ).new( 'x' )
    assert 'x, y, z, c' == ', '.join( c )
    assert 'y' in c and not 'pqr' in c
    assert c[0] == 'x' and c[-1] == 'c'
    assert c[1] == 'y' and c[-2] == 'z'
    assert c[2] == 'z' and c[-3] == 'y'
    assert c[3] == 'c' and c[-4] == 'x'
    
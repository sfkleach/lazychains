from lazychains import lazychain, chain


def test_smoketest_functionality():
    """
    A quickly generated test to cover the basic functionality. Done in a rush 
    following the not-so-great decision to grab the name on PyPI.
    The tests need backfilling properly.
    """
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

def test_nullary_construction():
    # Arrange
    lc = lazychain()
    sc = chain()
    # Act
    len_lc = len(lc)
    len_sc = len(sc)
    # Assert
    assert 0 == len_lc
    assert 0 == len_sc

def test_negative_indexes():
    # Arrange
    c = lazychain( "abc" )
    # Act
    x = c[-1]
    y = c[-2]
    z = c[-3]
    # Assert
    assert x == "c"
    assert y == "b"
    assert z == "a"

def test_lazycall():
    """
    Turner's Sieve
    """
    import itertools
    def sieve( L ):
        ( p, t ) = L.dest()
        return t.filter( lambda x: x % p != 0 ).lazycall( sieve ).new( p )
    primes = sieve( lazychain( itertools.count(2) ) )
    assert [2,3,5,7,11,13,17,19,23,29,31,37] == list( itertools.islice( primes, 12 ) )

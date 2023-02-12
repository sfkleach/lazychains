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
    assert not lc
    assert not sc
    assert 0 == len_lc
    assert 0 == len_sc

def test_nonnullary_construction():
    # Arrange
    lc = lazychain([99])
    sc = chain([88])
    # Assert
    assert lc
    assert sc

def test_new():
    # Arrange
    lc0 = lazychain()
    sc0 = chain()
    # Act
    lc1 = lc0.new(99)
    sc1 = sc0.new(88)
    # Assert
    assert not lc0 and lc1
    assert not sc0 and sc1
    assert 1 == len(lc1)
    assert 1 == len(sc1)
    assert [99] == list(lc1)
    assert [88] == list(sc1)

def test_bool_is_expanded():
    # Arrange
    lc0 = lazychain("pqr")
    lc1 = lazychain("pqr")
    sc0 = chain("stu")
    sc1 = chain("stu")
    # Act
    l1 = bool(lc1)
    s1 = bool(sc1)
    # Assert
    assert l1 is True
    assert s1 is True
    assert not lc0.is_expanded()
    assert lc1.is_expanded()
    assert sc0.is_expanded()
    assert sc1.is_expanded()

def test_expanded_len():
    # Arrange
    sample = "abcdef"
    c0 = lazychain( sample )
    depth = 3
    # Act
    p = c0.expanded_len()
    c0.len_is_at_least(depth)
    q = c0.expanded_len()
    c0.expand()
    r = c0.expanded_len()
    # Assert
    assert 0 == p
    assert depth == q
    assert len(sample) == r

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

def test_dest():
    # Arrange
    c = lazychain( "abc" )
    # Act
    x, y = c.dest()
    # Assert
    assert x == "a"
    assert not y.is_expanded()
    assert ["b", "c"] == list(y)

def test_head():
    # Arrange
    c = lazychain( "abc" )
    # Act
    x = c.head()
    # Assert
    assert x == "a"
    assert c.is_expanded()
    assert 1 == c.expanded_len()

def test_tail():
    # Arrange
    c = lazychain( "abc" )
    # Act
    y = c.tail()
    # Assert
    assert not y.is_expanded()
    assert 1 == c.expanded_len()
    assert ["b", "c"] == list(y)

def test_map():
    # Arrange
    c = lazychain( "abcdef" )
    # Act
    c = c.map(lambda x: f"-{x}-")
    c0 = c[0]
    c5 = c[5]
    # Assert
    assert "-a-" == c0
    assert "-f-" == c5
    assert 6 == len(c)

def test_filter():
    # Arrange
    c = lazychain( "abcdef" )
    # Act
    x = list(c.filter(lambda x: x in "cat"))
    # Assert
    assert ["a", "c"] == x

def test_zip():
    # Arrange
    c0 = lazychain( "ab" )
    c1 = chain(range(0, 6))
    # Act
    x = list(c0.zip(c1))
    # Assert
    assert [("a", 0), ("b", 1)] == x

def test_contains():
    # Arrange
    c = lazychain( "abxyz" )
    # Assert
    assert "a" in c
    assert "g" not in c
    assert "x" in c
    assert "z" in c

def test_add():
    # Arrange
    c0 = lazychain( "ab" )
    c1 = chain(range(0, 6))
    # Act
    c_new = c0 + c1
    x = list(c_new)
    # Assert
    assert ["a", "b", 0, 1, 2, 3, 4, 5] == x
    assert c_new.tail().tail() is c1

def test_len_is_at_least():
    # Arrange
    c = lazychain( "abxyz" )
    # Assert
    assert c.len_is_at_least(0) and c.len_is_at_least(5)
    assert not c.len_is_at_least(6) and not c.len_is_at_least(9999999)

def len_is_more_than():
    # Arrange
    c = lazychain( "abxyz" )
    # Assert
    assert c.len_is_more_than(0) and c.len_is_more_than(4)
    assert not c.len_is_more_than(5) and not c.len_is_more_than(9999999)

def test_len_is_at_most():
    # Arrange
    c = lazychain( "abxyz" )
    # Assert
    assert not c.len_is_at_most(0) and c.len_is_at_most(5)
    assert c.len_is_at_most(6) and c.len_is_at_most(9999999)

def len_is_less_than():
    # Arrange
    c = lazychain( "abxyz" )
    # Assert
    assert not c.len_is_less_than(0) and not c.len_is_less_than(5)
    assert c.len_is_less_than(6) and c.len_is_less_than(9999999)

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

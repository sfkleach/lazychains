# lazychains

A Python library to provide "chains", which are Lisp-like singly linked lists 
that support the lazy expansion of iterators. For example, we can construct a 
Chain of three characters from the iterable "abc" and it initially starts as 
unexpanded, shown by the three dots:

.. code:: python

   >>> from lazychains import lazychain
   >>> c = lazychain( "abc")
   >>> c
   chain([...])

We can force the expansion of *c* by performing (say) a lookup or by forcing the whole
chain of items by calling expand:

.. code:: python

   >>> c[1]                   # Force the expansion of the next 2 elements.
   True
   >>> c
   chain(['a','b',...])
   >>> c.expand()             # Force the expansion of the whole chain.
   chain(['a','b','c'])

As we will see, chains are generally less efficient than ordinary arrays. So,
as a default you should definitely carry on using ordinary arrays and tuples
most of the time. But they have a couple of special features that makes them the 
perfect choice for some problems.

   * Chains are immutable and hence can safely share their trailing segments.
   * Chains can make it easy to work with extremely large (or infinite) 
     sequences.

Expanded or Unexpanded
----------------------

When you construct a chain from an iterator, you can choose whether or not
it should be immediately expanded by calling chain rather than lazychain.
The difference between the two is pictured below. First we can see what happens
in the example given above where we create the chain using lazychain on 
"abc".

IMAGE GOES HERE

By contrast, we would immediately go to a fully expanded chain if we were to
simply apply chain:

.. code:: python

   >>> from lazychains import chain
   >>> c = chain( "abc" )
   >>> c
   chain(['a','b','c'])
   >>> 


IMAGE GOES HERE

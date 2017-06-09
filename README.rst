NYT Entity Uploader
===================

A wrapper for making requests to the `NYT Entity Service
API <https://github.com/newsdev/nyt-entity-service>`__.

Usage
-----

First: You should be running an instance of the `NYT Entity Service
API <https://github.com/newsdev/nyt-entity-service>`__.

Second: You should export ``ENTITYSVC_BASE_URL`` before running the
uploader to point to your own running entity service API endpoint.

Example 1: As a python module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can run the uploader as a python module and pass the name as a
keyword argument.

::

    $ export ENTITYSVC_BASE_URL='http://localhost.newsdev.net:8000'
    $ python
    Python 3.6.1 (default, Apr  4 2017, 09:40:21)
    [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.38)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from entity_uploader import UploadEntity
    >>> e = UploadEntity(name="Bank of America")
    >>> e.to_dict()
    {'name': 'Bank of America', 'uuid': 'f514b0e1-eea5-4676-aed2-2f9ee501cd5e', 'score': 0, 'created': True}

Example 2: Running example.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``example.py`` is a sample implementation that reads a list of entity
names from ``example_entities.txt``.

::

    $ export ENTITYSVC_BASE_URL='http://localhost.newsdev.net:8000'
    $ python example.py

    {'name': 'Bank of America', 'uuid': 'f514b0e1-eea5-4676-aed2-2f9ee501cd5e', 'score': 0, 'created': True}
    {'name': 'Bank of America', 'uuid': 'f514b0e1-eea5-4676-aed2-2f9ee501cd5e', 'score': 95, 'created': False}
    {'name': 'Bank of America', 'uuid': 'f514b0e1-eea5-4676-aed2-2f9ee501cd5e', 'score': 100, 'created': False}
    {'name': "banque d'amerique", 'uuid': 'cb626971-1989-4d78-870d-e6835017c936', 'score': 62, 'created': True}
    {'name': 'Bank of America', 'uuid': 'f514b0e1-eea5-4676-aed2-2f9ee501cd5e', 'score': 95, 'created': False}
    {'name': 'Bank of America', 'uuid': 'f514b0e1-eea5-4676-aed2-2f9ee501cd5e', 'score': 90, 'created': False}
    {'name': 'Bank of America', 'uuid': 'f514b0e1-eea5-4676-aed2-2f9ee501cd5e', 'score': 86, 'created': False}
    {'name': 'Bank of America', 'uuid': 'f514b0e1-eea5-4676-aed2-2f9ee501cd5e', 'score': 86, 'created': False}
    {'name': 'Bank of America', 'uuid': 'f514b0e1-eea5-4676-aed2-2f9ee501cd5e', 'score': 86, 'created': False}

In this example, the default ``create_if_below`` score is 80. The first
entity, ``Bank of America`` is created. The next entity,
``Bank of America, N.A.`` is not created because it has a similarity
score of 95. The UUID of the matching entity, ``Bank of America``, is
returned. The same is true for the next entity, ``BANK OF AMERICA``,
which has an even higher score of 100. The next entity,
``banque d'amerique``, is created as a new entity because it has a
matching score of 62, which is lower than the default
``create_if_below`` score of 80. The last few entities in
``example_entities.txt`` match the first entity with varying degrees of
closeness.

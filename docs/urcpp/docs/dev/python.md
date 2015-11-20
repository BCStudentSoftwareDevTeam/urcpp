# Developing in Python

We're not quite going to go so far as to rigorously adhere to PEP-8. However, our code needs to be neat.

## The Musts

1. Spaces, not tabs.

1. 2 spaces per indent level.

1. UNIX line endings.

Those two are for sanity. They're arbitrary, and now law. If you aren't using an editor that can do this, always, then get a new editor or fix the one you've got.

## The Shoulds

* If you're writing a function, and its getting long, consider whether you can break any of it out into another function. Every function should really try and do just one thing.

* If you're writing a function, and it seems really complex, ask someone to talk about it. It might be you're making it too complex. We'd rather take a little extra time to think about our code than to spend the next year debugging the first idea that popped into someone's head... but was convoluted and complex.

* Prefer simple over complex. If you know a fancy way to do something, **don't**.

* Test. We really should have unit tests for as many things as possible.

* Love peewee. We're using an ORM for a reason: wherever possible, let peewee do the database work for you.

* ...

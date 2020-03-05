# TDD Naan Factory Exercise 🌮
This exercise is going to bring together lots of concepts.

Learning Outcomes
Learning outcomes include:

- git
- github
- functions
- TDD
- separation of concerns
- DRY code
- DOD

# Intalling and running
To run the naan factory do the following:
'''python
import naan_factory
run_factory()
'''

TDD - test driven development
- write the test
- run it, and read the error
- code and make it pass the test

this helps with:
- Stop over engineering
- Maintainable code
- Reduce technical debt
- Goes well with agile and working code
- errors can be your guide in complex systems

We write unit tests.

## Unit Tests
Test single pieces of code. Like a function.

base of a test Usually has 3 phases.

setup phase (know variables)
calling of the function / piece of code with know variables
asserting for expect output
User stories for Naan Factory

'''
#1 
As a user, I can use the make_dough with 'water' and 'flour' to make 'dough'.

#2
As a user, I can use the bake_dough with dough to get naan. 

#3
As a user, I can user the run_factory with water and flour and get naan.
'''
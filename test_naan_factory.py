from naan_factory_functions import *

# 1
# As a user, I can use the make_dough with water and flour to make dough.
print(make_dough('water', 'flour') == 'dough')

#2
#As a user, I can use the bake_dough with dough to get naan.
print(bake_dough('dough') == 'naan')

#3
#As a user, I can user the run_factory with water and flour and get naan.
print(run_factory('water', 'flour') == 'naan')
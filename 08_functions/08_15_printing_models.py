# This code imports functions from a separate file to print models names that will be printed, and then print the model names that have been printed.

import os
os.system('cls')

import printing_functions
from printing_functions import print_models
from printing_functions import show_completed_models

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print("\n")
THE SHOPPING CART
A grocery checkout system.

Prerequisites
Anaconda 3.7+
Python 3.7+
Pip
Installation
Fork this remote repository (https://github.com/sondejste/shopping-cart) under your own control, then "clone" or download your remote copy onto your local computer.

Navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

cd 
Use Anaconda to create and activate a new virtual environment, perhaps called "shopping-env":

conda create -n shopping-env python=3.8
conda activate shopping-env

Setup
In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your local tax rate in deceimal form (e.g. 7% = .07):

TAX_RATE=

Usage
Run the game script:

python shopping_cart.py
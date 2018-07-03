import os

from mod import f

def setup_function(func):
    # The setup_function() function tests ensure that neither the yes.txt nor the
    # no.txt files exist.
    files = os.listdir('.')
    if 'no.txt' in files:
        os.remove('no.txt')
    if 'yes.txt' in files:
        os.remove('yes.txt')

def teardown_function(func):
    # The f_teardown() function removes the yes.txt file, if it was created.
    files = os.listdir('.')
    if 'yes.txt' in files:
        os.remove('yes.txt')

def test_f():
    exp = 42
    f()
    with open('yes.txt', 'r') as fhandle:
        obs = int(fhandle.read())
    assert obs == exp

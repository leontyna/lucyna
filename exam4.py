import os

from mod import f

def test_f(tmpdir):
    exp = 42
    f(tmpdir)
    with open(tmpdir.join('yes.txt'), 'r') as fhandle:
        obs = int(fhandle.read())
    assert obs == exp
    
def test_f_with_no(tmpdir):
    with open(tmpdir.join('no.txt'), 'x'):
        pass
    f(tmpdir)
    assert not os.path.exists(tmpdir.join('yes.txt'))

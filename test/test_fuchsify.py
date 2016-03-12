import os.path
import unittest

from   sage.all import SR
from   fuchsia import import_matrix_from_file, fuchsify, transform, singularities

class Test(unittest.TestCase):
    def assertFuchsifyWorks(t, filename):
        M = import_matrix_from_file(filename)
        x = SR.var("x")
        t.assertIn(x, M.variables())
        M_pranks = singularities(M, x).values()
        t.assertNotEqual(M_pranks, [0]*len(M_pranks))
        F, T = fuchsify(M, x)
        F = F.simplify_rational()
        t.assertEqual(F, transform(M, x, T).simplify_rational())
        F_pranks = singularities(F, x).values()
        t.assertEqual(F_pranks, [0]*len(F_pranks))

    def test_git_409(t):
        t.assertFuchsifyWorks(os.path.join(os.path.dirname(__file__),
            "..", "examples", "git_409.mtx"))

    def test_git_410(t):
        t.assertFuchsifyWorks(os.path.join(os.path.dirname(__file__),
            "..", "examples", "git_410.mtx"))

    def test_henn_324(t):
        t.assertFuchsifyWorks(os.path.join(os.path.dirname(__file__),
            "data", "henn_324.mtx"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
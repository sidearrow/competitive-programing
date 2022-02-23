from unittest import TestCase

from .union_find import UnionFind


class UnionFindTest(TestCase):
    def test_main(self):
        uf = UnionFind(5)
        self.assertEqual(1, uf.get_root(1))

        uf.unite(0, 1)
        uf.unite(0, 2)
        self.assertEqual(uf.get_root(1), uf.get_root(2))
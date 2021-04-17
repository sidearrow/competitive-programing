from unittest import TestCase
from lib.segment_tree import SegmentTree


class SegmentTreeTest(TestCase):
    def test_sum(self):
        size = 5
        init = [1, 2, 3, 4, 5]
        func = lambda x, y: x + y
        default = 0
        st = SegmentTree(size, init, func, default)

        test_cases = [
            (0, 1, 1),
            (0, 2, 3),
            (2, 4, 7),
            (4, 5, 5),
        ]
        for tc in test_cases:
            a, b, res = tc
            self.assertEqual(st.get(a, b), res)

        # [11, 2, 33, 4, 55]
        st.set(0, 11)
        st.set(2, 33)
        st.set(4, 55)
        test_cases = [
            (0, 2, 13),
            (1, 3, 35),
            (2, 4, 37),
            (3, 5, 59),
        ]
        for tc in test_cases:
            a, b, res = tc
            self.assertEqual(st.get(a, b), res)

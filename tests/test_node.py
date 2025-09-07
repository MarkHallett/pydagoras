#test_dag.py

import unittest

try:
    from pydagoras.node import Node

except ModuleNotFoundError:
    # for running tests, if pydagoras is not installed
    import sys, os

    cwd = os.getcwd()
    src_path = f'{cwd}/../src'
    src_pydagoras_path = f'{cwd}/../src/pydagoras'

    sys.path.insert(0, src_path)
    sys.path.insert(0, src_pydagoras_path)

    from pydagoras.node import Node


class TestNode(unittest.TestCase):
    def test_node_initialization(self):
        node = Node('A')
        self.assertEqual(node.node_id, 'A')

    def test_node_value_assignment(self):
        node = Node('B')
        node.set_value(10)
        self.assertEqual(node.get_value(), 10)

    def test_tooltip_assignment(self):
        node = Node('C')
        node.set_tooltip('This is a tooltip')
        self.assertEqual(node.tooltip, 'This is a tooltip')

    def test_node_str_representation(self):
        node = Node('D', nodetype='in')
        node.set_value(5)
        expected_str = 'Node(id:D, type:in, value:5, calc:None, usedby:None)'
        self.assertEqual(str(node), expected_str)

    def test_node_pp_json(self):
        node = Node('E', nodetype='in', tooltip='Output node')
        node.set_value(20)
        expected_json = {
            "node_id": "E",
            "value": 20,
            "calc": None,
            "usedby": None,
            "nodetype": "in",
            "display_name": "E",
            "tooltip": "Output node"
        }
        self.assertEqual(node.pp_json(), expected_json)

if __name__ == '__main__':
    unittest.main()

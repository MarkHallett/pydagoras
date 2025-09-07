# tests/test_dag_dot.py

import unittest

try:
    from pydagoras.node import Node
    from pydagoras.dag_dot import DAG_dot, calc

except ModuleNotFoundError:
    # for running tests, if pydagoras is not installed
    import sys, os

    cwd = os.getcwd()
    src_path = f'{cwd}/../src'
    src_pydagoras_path = f'{cwd}/../src/pydagoras'

    sys.path.insert(0, src_path)
    sys.path.insert(0, src_pydagoras_path)

    from dag_dot import DAG_dot, calc


class TestDAGDot(unittest.TestCase):
    def setUp(self):
        self.dag_dot = DAG_dot(label='Test DAG')


    def test_makeNode_adds_node(self):
        n = self.dag_dot.makeNode('test', calc=None)
        self.assertIn(n, self.dag_dot.nodes)
        self.assertTrue(any(node.node_id == 'test' for node in self.dag_dot.nodes))

    def test_input_and_output_nodes(self):
        n_in = self.dag_dot.makeNode('input', calc=None, nodetype='in')
        n_out = self.dag_dot.makeNode('output', calc=None, nodetype='out')
        self.assertIn(n_in, self.dag_dot.input_nodes)
        self.assertEqual(self.dag_dot.output_node, n_out)

    def test_drawNode_adds_to_graph(self):
        n = self.dag_dot.makeNode('draw', calc=None)
        self.assertIn(n.display_name, self.dag_dot.G.nodes())

    def test_set_and_get_value(self):
        n = self.dag_dot.makeNode('val', calc=None)
        self.dag_dot.set_value(n, 123)
        self.assertEqual(self.dag_dot.dag.get_value(n.node_id), 123)

    def test_get_colors(self):
        self.assertEqual(DAG_dot.get_colors('e'), ('red', 'red'))
        self.assertEqual(DAG_dot.get_colors('anything'), ('blue', 'green'))

    def test_calc_decorator_success(self):

        @calc
        def triple(node=None):
            return node.get_value() * 3

        my_dag = DAG_dot(label='Eg DAG')
        n2 = my_dag.makeNode('x3', calc=triple, tooltip='multiply')
        my_dag.makeNode('In', calc=None, usedby=[n2], nodetype='in')

        my_dag.set_input('In', 10)

        result = my_dag.output_node.get_value()
        self.assertEqual(result, 30)

    def test_calc_decorator_exception(self):

        @calc
        def fail(node=None):
            raise ValueError("fail")

        my_dag = DAG_dot(label='Eg DAG')
        n2 = my_dag.makeNode('Eg fail', calc=fail, tooltip='eg_error')
        n1 = my_dag.makeNode('In', calc=None, usedby=[n2], nodetype='in')
        my_dag.set_input('In', 10)

        self.assertEqual(n2.tooltip, 'fail')

        #print(my_dag.G.to_string())  # Print the graph representation  


if __name__ == '__main__':
    unittest.main()

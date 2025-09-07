# filepath: /Users/python/pydagoras/dev/2026-09-06_tests/pydagoras/src/pydagoras/test_dag.py

import os
import sys
import json
import unittest

#jfrom pydagoras.dag_dot import DAG_dot, calc
#from pydagoras.dag import DAG

try:
    from pydagoras.dag import DAG
    from pydagoras.dag_dot import DAG_dot, calc

    #from pydagoras.node import Node
    #from pydagoras.dag_dot import DAG_dot, calc

except ModuleNotFoundError:
    # for running tests, if pydagoras is not installed
    import sys, os

    cwd = os.getcwd()
    src_path = f'{cwd}/../src'
    src_pydagoras_path = f'{cwd}/../src/pydagoras'

    sys.path.insert(0, src_path)
    sys.path.insert(0, src_pydagoras_path)

    from pydagoras.dag import DAG
    from pydagoras.dag_dot import DAG_dot, calc


class TestDAG(unittest.TestCase):
    def setUp(self):
        # Ensure a fresh shared state for each test
        DAG._DAG__shared_state.clear()

    def test_set_and_get_value(self):
        dag = DAG()
        dag.set_value('x', 42)
        self.assertEqual(dag.get_value('x'), 42)

    def test_get_value_missing_key(self):
        dag = DAG()
        self.assertIsNone(dag.get_value('missing'))

    def test_shared_state_across_instances(self):
        dag1 = DAG()
        dag2 = DAG()
        dag1.set_value('shared', 'yes')
        self.assertEqual(dag2.get_value('shared'), 'yes')

    def test_direct_values_assignment(self):
        dag = DAG()
        dag.values['direct'] = 'set'
        self.assertEqual(dag.get_value('direct'), 'set')

    def test_dynamic_attribute_shared(self):
        dag1 = DAG()
        dag1.custom_attr = 'custom'
        dag2 = DAG()
        self.assertTrue(hasattr(dag2, 'custom_attr'))
        self.assertEqual(dag2.custom_attr, 'custom')

    def test_values_dict_is_shared(self):
        dag1 = DAG()
        dag2 = DAG()
        dag1.set_value('a', 1)
        dag2.set_value('b', 2)
        self.assertEqual(dag1.values, dag2.values)
        self.assertEqual(dag1.values, {'a': 1, 'b': 2})

    def test_str(self):
        dag = DAG()
        dag.set_value('a', 1)
        dag.set_value('b', 2)
        self.assertEqual(str(dag), "DAG(values={'a': 1, 'b': 2})")
       
        dag_json = json.dumps(dag.values, sort_keys=True, indent=2)
        print(dag_json)
        print(str(dag_json))

    def test_pp_json(self):
        dag = DAG()
        dag.set_value('a', 1)
        dag.set_value('b', 2)
        expected_json = {
            "a": 1,
            "b": 2
        }
        self.assertEqual(dag.pp_json(), expected_json)  

if __name__ == '__main__':
    unittest.main()

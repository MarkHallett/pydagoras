# eg_use_pydagoras.py
# a script to provide an example of creating and using a DAG using pydagoras


import os
import sys

try:
    from pydagoras.dag_dot import DAG_dot, calc
except ModuleNotFoundError as e:
    cwd = os.getcwd()
    src_path = f'{cwd}/../src'
    src_pydagoras_path = f'{cwd}/../src/pydagoras'

    sys.path.insert(0, src_path)
    sys.path.insert(0, src_pydagoras_path)

    from dag import DAG
    from dag_dot import DAG_dot, calc

def run():

    print('#######################################')

    @calc
    def tripple(node=None):
        return node.get_value() * 3

    dag = DAG_dot(label='Eg DAG')
    n2 = dag.makeNode('x3', calc=tripple, tooltip='multiply')
    n1 = dag.makeNode('In', calc=None, usedby=[n2], nodetype='in')

    print('Initial DAG')
    print(dag.G.to_string()) # 
    print('Updates --------------')
    dag.set_input('In', 10)

    print('Outputs --------------')
    dag.ppInputs() # 
    dag.ppOutput() # 
    dag.pp()

    print('Final DAG')
    print(dag.G.to_string()) # 

if __name__ == '__main__':
    run()
    print('Done.')

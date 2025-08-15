# dag_dot

import logging
import pygraphviz as pgv
from pydagoras.dag import DAG

logger = logging.getLogger()


class Node(object):
    def __init__(self, node_id=None, calc=None, usedby=None, nodetype=None, display_name=None, tooltip='notset'):
        self.calc = calc
        self.node_id = node_id
        self.usedby = usedby
        #self.value = None
        self.dag = DAG()   
        self.dag.set_value(node_id, None)
    
        self.nodetype = nodetype
        if display_name:
            self.display_name = display_name
        else:
            self.display_name = node_id
        self.tooltip = tooltip
        self.orig_tooltip = tooltip

    def pp(self):
        print(f'NODE: {self.nodetype}, id:{self.node_id}, value:{self.get_value()}')
        print(f'      display_name:{self.display_name} tooltip:{self.tooltip} ')
        print(f'      calc: {self.calc} usedby:{self.usedby[0].node_id if self.usedby else None}')
        
    def set_tooltip(self, tooltip):
        self.tooltip = tooltip

    def set_value(self, value):
        self.dag.set_value(self.node_id, value)
        
    def get_value(self):
        return self.dag.get_value(self.node_id)


if __name__ == '__main__':
    print('##########################################')
    def calc_simple(node=None):
        # calc_simple
        return DAG().get_value(node.node_id) + 2

    # (self, node_id=None, calc=None, usedby=None, nodetype=None, display_name=None, tooltip='notset'):
    #        self.defNode(n,usedby, nodetype, tooltip)

    my_node = Node(node_id='a', nodetype='in')
    my_node.dag.set_value('a', 1)
    my_node.pp()  # Output: Input a = 1
    
    my_node2 = Node(node_id='b', nodetype='internal', calc=calc_simple, usedby=[my_node])
    my_node2.dag.set_value('b', 2)
    my_node2.pp()  # Output: Input b = 2


    my_node2 = Node(node_id='c', nodetype='out')
    my_node2.dag.set_value('c', 2)
    my_node2.pp()  # Output: Input b = 2

    print(DAG().values)  # Output: {'a': 1, 'b': 2}


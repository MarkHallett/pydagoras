# dag_dot.py

import logging
from pydagoras.dag import DAG

logger = logging.getLogger()


class Node:

    def __init__(self, node_id=None, calc=None, usedby=None, nodetype=None, display_name=None, tooltip='notset'):
        self.calc = calc
        self.node_id = node_id
        self.usedby = usedby
        self.dag = DAG()   
        self.dag.set_value(node_id, None)
        self.nodetype = nodetype
    
        if display_name:
            self.display_name = display_name
        else:
            self.display_name = node_id

        self.tooltip = tooltip # use tooltip to show errors when present
        self.orig_tooltip = tooltip


    def __str__(self):
        return f'Node(id:{self.node_id}, type:{self.nodetype}, value:{self.get_value()}, calc:{self.calc}, usedby:{[n.node_id for n in self.usedby] if self.usedby else None})'

    def pp_json(self): 
        return { "node_id": self.node_id, \
                 "value": self.get_value(), \
                 "calc": self.calc, \
                 "usedby": [n.node_id for n in self.usedby] if self.usedby else None, \
                 "nodetype": self.nodetype, \
                 "display_name": self.display_name, \
                 "tooltip": self.tooltip}
        
    def __repr__(self):
        return f'Node({str(self.pp_json())})'

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

    my_node = Node(node_id='a', nodetype='in')
    my_node.dag.set_value('a', 1)
    my_node.pp()  # Output: Input a = 1
    
    import json
    print( json.dumps(my_node.pp_json(), indent=2) )
    print( repr(my_node))

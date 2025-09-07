# dag_dot.py

from functools import wraps

import logging
import pygraphviz as pgv
from pydagoras.dag import DAG
from pydagoras.node import Node

logger = logging.getLogger(__name__)


class DAG_dot:

    def __init__(self, label):
        logger.info(f'creating {label=}')
        self.label = label
        self.dag = DAG()  # Initialize the DAG instance
        self.G=pgv.AGraph(directed=True, strict=True, rankdir='LR', label=label, labelloc="t")
        self.input_nodes = []
        self.internal_nodes = []
        self.output_node = None
        self.nodes = []  # List to keep track of all nodes


        @calc
        def calc_out(node=None):
            return self.n_out.get_value() 

        self.n_out = self.makeNode('out', calc=calc_out, usedby=[], nodetype='out') 
        
    def __str__(self):
        return f'DAG_dot(label:{self.label}, nodes:{len(self.nodes)})'


    def makeNode(self,label,calc,usedby=None, nodetype='internal', display_name=None, tooltip=''):
        if usedby is None:
            usedby = [self.n_out]
        n = Node(label,calc,usedby,nodetype,display_name,tooltip)
        if nodetype == 'in':
            self.input_nodes.append(n)
        elif nodetype == 'out':
            self.output_node = n
        else:
            self.internal_nodes.append(n)
        self.nodes.append(n)  # Add the node to the list of all nodes

        self.drawNode(n,usedby, nodetype, tooltip)
        return n


    def drawNode(self,node,usedby,nodetype,tooltip):
        doc = node.display_name
        if nodetype == 'in':
            self.G.add_node(doc, shape="square", tooltip=tooltip)
            for n in usedby:
                self.draw_edge(doc,n.display_name)
        elif nodetype == 'internal':
            self.G.add_node(doc, tooltip=tooltip)
            for n in usedby:
                self.draw_edge(doc,n.display_name)
        elif nodetype == 'out':
            self.G.add_node(doc, color="white")


    def draw_edge(self,node1,node2):
        self.G.add_edge(node1,node2,label='Undefined', fontname="Courier")


    def update_node(self,node1,node2,value,tooltip='not set XXX'):
        fontcolor, color = self.get_colors(value)
        self.G.add_node(node1,color=color,fontcolor=fontcolor,tooltip=tooltip)
        self.G.add_edge(node1,node2, label=value,fontcolor=fontcolor,color=color, fontname="Courier")
 
    # special cases
    @classmethod
    def get_colors(cls, value):
        if value in ( 'e',):
            return 'red', 'red'
        return 'blue', 'green'

    def set_input(self,node_id,value): # set values in all node
        for node in self.nodes:
            if node.node_id == node_id:
                for usedby in node.usedby:
                    self.update_node(node.display_name,usedby.node_id, value=value, tooltip=node.tooltip)
                    self.set_input(usedby.node_id, value)  # recursion 
                    #self.setValue(node, value)
                self.setValue(node, value)


    def setValue(self,n,v):
        if v == self.dag.get_value(n):
            return

        # build the DAG
        n.set_value(v) 
        x = self.dag.get_value(n.node_id)

        for u in n.usedby:
            if u.calc == None:
                continue
            
            new_value = u.calc(self, node=n)  # Call the calc function with self and node, contains error handling
            self.dag.set_value(u.node_id, new_value)

        if not n.usedby:
            return

        if n.usedby[0].usedby == []: # output node
            msg = 'update dag_dot.py %s %s' %(n.usedby[0].node_id, n.get_value())
            logger.info (msg)


    def ppInputs(self):
        for n in self.input_nodes:
            print(n)

    def ppInternals(self):
        for n in self.internal_nodes:
            print(n)

    def ppOutput(self):
        print(self.output_node)

    def pp(self):
        print(f'DAG: {self.label}')
        print('Inputs:')
        self.ppInputs()
        print('Internals:')
        self.ppInternals()
        print('Output:')
        self.ppOutput()

    def pp_json(self):
        values = self.dag.values  # Print the values of all nodes in the DAG
        return {
            "label": self.label,
            "values": values
        }



    def get_value(self):
         return self.dag.get_value(self.label)

    def set_value(self, node, value):
        self.dag.set_value(node.node_id, value)
        self.setValue(node,value)


def calc(f1): # decorator deffinition
    @wraps(f1)
    def f3(dag, *args, **kwargs):
        node=kwargs['node']

        u_node = node.usedby[0] if node.usedby else None
        #        self.update_node(u_node.node_id,o_node.node_id, value='-', tooltip=node.tooltip)

        try:
            rtn = f1(*args, **kwargs) # Call the original function
            u_node.set_value(rtn)  # Set the value of the node
            u_node.set_tooltip(u_node.orig_tooltip)  # Set the tooltip of the node

        except Exception as e:
            logger.error('Error in %s: %s' %(u_node.node_id,str(e)))
            rtn = 'e'
            u_node.set_value(rtn)  # Set the value of the node
            u_node.set_tooltip(str(e))  # Set the tooltip of the node

        for u_node in node.usedby:
            #print(f'Updating node: {u_node.node_id} with value: {rtn}')
            dag.set_input(u_node.node_id, rtn)

        return rtn
    return f3

if __name__ == '__main__':

    @calc
    def calc_triple(node=None):
        return node.get_value() * 3 

    my_dag = DAG_dot(label='Test DAG')
    n2 = my_dag.makeNode('b', calc=calc_triple)
    n1 = my_dag.makeNode('a', calc=None, usedby=[n2], nodetype='in') #, display_name='Input A')
    my_dag.set_input('a', 10)
    
    print(f'{my_dag=}')  

    my_dag.pp()

    import json
    print(json.dumps(my_dag.pp_json(), sort_keys=True, indent=2))
    
    print('Graph representation:')  
    print(my_dag.G.to_string())  # Print the graph representation  

    print(repr(my_dag))  
    
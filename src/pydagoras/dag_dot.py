# dag_dot

import logging
import pygraphviz as pgv

logger = logging.getLogger(__name__)

from .node import Node

class DAG(object):
    '''Base DAG'''
    #__shared_state = {} 

    def __init__(self, label):
        logger.info(f'creating {label=}')
        #self.__dict__ = self.__shared_state
        #if hasattr(self, 'o'):
        #    return
        self.label = label

        self.G=pgv.AGraph(directed=True, strict=True, rankdir='LR', label=label, labelloc="t")
        self.input_nodes=[]

    def makeNode(self,label,calc,usedby,nodetype, display_name=None, tooltip=''):
        n = Node(label,calc,usedby,nodetype,display_name,tooltip)
        if nodetype == 'in':
            self.input_nodes.append(n)
        self.defNode(n,usedby, nodetype, tooltip)
        return n

    def defNode(self,node,usedby,nodetype,tooltip):
        doc = node.display_name
        if nodetype == 'in':
            self.G.add_node(doc, shape="square", tooltip=tooltip)
            for n in usedby:
                self.AddEdge(doc,n.display_name)
        elif nodetype == 'internal':
            self.G.add_node(doc, tooltip=tooltip)
            for n in usedby:
                self.AddEdge(doc,n.display_name)
        elif nodetype == 'out':
            self.G.add_node(doc, color="white")


    def AddEdge(self,node1,node2):
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

    def set_input(self,node_id,value):
        for node in self.input_nodes:
            if node.node_id == node_id:
                for usedby in node.usedby:
                    self.update_node(node.display_name,usedby.node_id, value=value, tooltip=node.tooltip)
                self.setValue(node,value)


    def setValue(self,n,v):
        if v == n.value:
            return

        # build the DAG
        n.value = v
        for u in n.usedby:
           if u.calc == None:
               continue
           try:
              new_value = u.calc(node=n)
           except Exception as e:
              print('Error in setValue')
              print (str(e))
              new_value = 'e' # ??

           self.setValue(u,new_value)

        if not n.usedby:
            return

        if n.usedby[0].usedby == []:
            msg = 'update dag_dot.py %s %s' %(n.usedby[0].node_id, n.value)
            logger.info (msg)


    def ppInputs(self):
        for n in self.input_nodes:
            n.pp()


    def ppOutput(self):
        for k, v in self.__dict__ .items():
            if type(v) == type(Node()):
                if v.usedby == []:
                    print (f'{v.node_id} = {v.value}')


def calc(f1): # decorator deffinition
    def f3(self,*args, **kwargs):
        node=kwargs['node']

        for u_node in node.usedby:
            for o_node in u_node.usedby:
                self.update_node(u_node.node_id,o_node.node_id, value='-', tooltip=node.tooltip)

        try:
            rtn = f1(self,*args, **kwargs)
            if node.usedby[0].nodetype == 'out':
                print(f'OUT: {node.value}')

        except Exception as e:
            print ('Error in %s: %s' %(u_node.node_id,str(e)))
            rtn = 'e'

        for u_node in node.usedby:
            for o_node in u_node.usedby:
                self.update_node(u_node.node_id,o_node.node_id, value=rtn, tooltip=u_node.tooltip)

        return rtn
    return f3


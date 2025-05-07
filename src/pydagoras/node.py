# dag_dot

import logging
import pygraphviz as pgv

logger = logging.getLogger()


class Node(object):
    def __init__(self, node_id=None, calc=None,usedby=None, nodetype=None, display_name=None, tooltip='notset2'):
        self.calc = calc
        self.node_id = node_id
        self.usedby = usedby
        self.value = None
        self.nodetype = nodetype
        if display_name:
            self.display_name = display_name
        else:
            self.display_name = node_id
        self.tooltip = tooltip

    def pp(self):
        print ( "Input %s = %s " %( self.node_id, self.value))


# eg_use_pydagoras.py

import pydagoras

class TestDag1(pydagoras.DAG):
    __shared_state = {}  
    def __init__(self, filename=None):
        self.__dict__ = self.__shared_state
        super(TestDag1, self).__init__(filename)
        if hasattr(self, 'o'):
            return

        self.o = self.makeNode(label='Out', calc=self.calc_output, usedby = [], nodetype='out')
        self.aa = self.makeNode(label='calc_A', calc=self.calcRateA, usedby=[self.o], nodetype='internal', display_name='AA', tooltip='aa')
        self.a = self.makeNode(label='A', calc=None, usedby=[self.aa], nodetype='in', display_name='In', tooltip='in')


    @pydagoras.calc
    def calcRateA(self, node):
        return self.a.value * 2 

    @pydagoras.calc
    def calc_output(self, node):
        return self.aa.value 

def run():
    pydagoras.DAG('xx')
    pydagoras.Node()

    my_dag = TestDag1('test')
    TestDag1().set_input('A',4 ) 
    print(TestDag1().o.value)

    my_dag2 = TestDag1('test2')
    print(my_dag2.o.value)
    print (my_dag.G.to_string())

    TestDag1().ppInputs()
    TestDag1().ppOutput()
    
if __name__ == '__main__':
    run()

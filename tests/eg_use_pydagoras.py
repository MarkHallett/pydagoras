# eg_use_pydagoras.py

import os
os.system('pip install pydagoras')  # Ensure pydagoras is imported to initialize it


from pydagoras.dag_dot import DAG_dot, calc

class EgDag(DAG_dot):
    def __init__(self):
        self.title = 'Eg DAG'
        super().__init__(self.title)

        # define nodes
        self.o = self.makeNode(label='Out', calc=self.calc_output, usedby = [], nodetype='out')
        self.aa = self.makeNode(label='calc_A', calc=self.calcRateA, usedby=[self.o], nodetype='internal', tooltip='x2')
        self.a = self.makeNode(label='A', calc=None, usedby=[self.aa], nodetype='in', display_name='In', tooltip='in')

    @calc
    def calcRateA(self, node):
        return self.a.get_value() * 2 

    @calc
    def calc_output(self, node):
        return self.aa.get_value()


def run():

    print('\n** Create the DAG')
    my_dag = EgDag()

    print('\n** print DAG initial output')
    print (my_dag.G.to_string())

    print('\n** set input to 4')
    EgDag().set_input('A',4 ) 

    print('\n** set input to 6')
    EgDag().set_input('A',6 ) 

    print('\n** print DAG final output')
    print (my_dag.G.to_string())

    EgDag().ppInputs()
    return
    EgDag().ppOutput()
    
    print('\n** XXXXXXXX print DAG final output')
    print (my_dag.G.to_string())
    print (my_dag.pp())

if __name__ == '__main__':
    run()
    print('Done.')


# Package

## How to download and install pydagroas


!!! warning
    It is good practice to install into a virtual env

To download the package from pypi and install into site-apckages use

    pip install pydagoras

To download and install a particular version from github use

    pip install git+https://github.com/MarkHallett/pydagoras@v0.0.7



## How to use

The code below will create the DAG in the diagram below.
![basic_dag](images/basic_dag.png "basic_dag")

### Creating the nodes

within a class derived from `pydagoras.DAG` first define the calculation within the nodes, then create the nodes.

``` python title='creating nodes', linenums='1'
# output node
self.o = self.makeNode(label='GBP/USD/EUR',
                       calc=None,usedby = [],
                       nodetype='out')

# internal nodes
self.i1 = self.makeNode(label='calc_B',
                        calc=self.calcRateB,
                        usedby=[self.o], nodetype='internal')

self.i2 = self.makeNode(label='calc_A',
                        calc=self.calcRateA,
                        usedby=[self.bb], nodetype='internal')
        
# input nodes
self.a = self.makeNode(label='gbp-usd',
                       calc=None,usedby=[self.i2], 
                       nodetype='in')

self.b = self.makeNode(label='usd-eur',
                       calc=None,usedby=[self.i2], 
                       nodetype='in')

self.c = self.makeNode(label='eur-gbp',
                       calc=None,usedby=[self.i1], 
                       nodetype='in')
```
### Updating nodes
``` python title='updating nodes', linenums='1'
my_dag.set_input('a',1.5)
my_dag.set_input('b',0.75)
my_dag.set_input('c',0.9)
```

### DAG output
``` python title='DAG output value', linenums='1'
my_dag.o.value
```







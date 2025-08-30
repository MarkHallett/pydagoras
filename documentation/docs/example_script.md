In the pydagoras github repository folder `tests` includes the script `eg_use_pydagoras.py`

The following simple DAG
<br>
<br>
![image](images/eg_dag.png){: style="height:100px;width:350px"}
<br>
will be created, updated and displayed by the following code

``` python title="Import the necessary code from pydagoras" linenums="4" 
from pydagoras.dag_dot import DAG_dot, calc
```
``` python title="Define the node calculations" linenums="10" 
    @calc
    def tripple(node=None):
        return node.get_value() * 3
```
``` python title="Create the DAG" linenums="14" 
    dag = DAG_dot(label='Eg DAG')
```
``` python title="Define the input node and single calculation node" linenums="15" 
    n2 = dag.makeNode('x3', calc=tripple, tooltip='multiply')
    n1 = dag.makeNode('In', calc=None, usedby=[n2], nodetype='in')
```
``` python title="Print the initial DAG" linenums="19"
    print(dag.G.to_string())  
```
``` python title="Update the DAG input" linenums="22" 
    dag.set_input('In', 10)
```
``` python title="Print the final DAG" linenums="30"
    print(dag.G.to_string()) 
```
<br>
Putting it all together...

``` python title="eg_use_pydagoras.py" linenums="1"
# eg_use_pydagoras.py
# a script to provide an example of creating and using a DAG using pydagoras

from pydagoras.dag_dot import DAG_dot, calc

def run():

    print('#######################################')

    @calc
    def tripple(node=None):
        return node.get_value() * 3

    dag = DAG_dot(label='Eg DAG')
    n2 = dag.makeNode('x3', calc=tripple, tooltip='multiply')
    n1 = dag.makeNode('In', calc=None, usedby=[n2], nodetype='in')

    print('Initial DAG')
    print(dag.G.to_string()) # (1)

    print('Updates --------------')
    dag.set_input('In', 10)

    print('Outputs --------------')
    dag.ppInputs() # (2)
    dag.ppOutput() # (3)
    dag.pp() 

    print('Final DAG')
    print(dag.G.to_string()) # (4)

if __name__ == '__main__':
    run()
    print('Done.')

```

1.  ![image](images/eg_dag_start.png) <pre>strict digraph  {
	graph [label="Eg DAG",
		labelloc=t,
		rankdir=LR
	];
	out	 [color=white];
	x3	 [tooltip=multiply];
	x3 -> out	 [fontname=Courier,
		label=Undefined];
	In	 [shape=square];
	In -> x3	 [fontname=Courier,
		label=Undefined];
}</pre>
2.  <pre>DAG: Eg DAG
Inputs:
NODE: in, id:In, value:10
      display_name:In tooltip:
      calc: None usedby:x3</pre>
3.  <pre> NODE: out, id:out, value:30
      display_name:out tooltip: 
      calc: <function DAG_dot.__init__.<locals>.calc_out at 0x1007b9b20> usedby:None
    </pre>
4.  ![image](images/eg_dag_end.png) <pre>strict digraph  {
	graph [label="Eg DAG",
		labelloc=t,
		rankdir=LR
	];
	out	 [color=white];
	x3	 [color=green,
		fontcolor=blue,
		tooltip=multiply];
	x3 -> out	 [color=green,
		fontcolor=blue,
		fontname=Courier,
		label=30];
	In	 [color=green,
		fontcolor=blue,
		shape=square];
	In -> x3	 [color=green,
		fontcolor=blue,
		fontname=Courier,
		label=10];
}</pre>



------------------------



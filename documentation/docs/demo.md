# Demo

The demo site [www.pydagoras.com](https://www.pydagoras.com/) provides the oppertunity to update DAG inputs and see the DAG update.

First the site makes a websocket connection, the connection status can be seen on the site. This allow the browser to recieve DAG updates. 
<br>
Update to the dag can be made via the input boxes under the DAG.
<br>
<br>
The following tabs match the tabs in the demo and show screen shots of the 3 example DAG images, after they have been updated.

=== "Basic DAG"
    ![basic_dag](images/basic_dag.png){height=40px width=500px align=left}
    This basic DAG is made up of 3 input nodes ( the square boxes towards the left), 3 internal nodes ( the oval shapes ) and an output on the right.
=== "Duplicate nodes DAG"
    ![duplicate_nodes_dag](images/dup_nodes_dag.png "duplicate_nodes"){height=40px width=500px align=left}
    In this DAG the node D is is used twice D_1 and D_2. It could have been drawn as a single node with 2 exit lines, but this representation becomes messy as the number of nodes increases.
=== "FX DAG"
    ![fx_dag](images/fx_dag.png "fx_dag"){height=40px width=500px align=left}
    This DAG calculates the amount returend after cycling through 3 curreny pairs.

On the demo site, below each DAG there are input boxes for the DAG input nodes.
Under the input boxes is a toggle switch.
Depending on the state of the toggle, values can be entered one at a time, or in bulk.
These values are sent via an API to the backend.
Once the DAG has been recaluclated, its image representation will be returned to the frontend to be displayed, and the DAG will then be refreshed in the browser.
<br>
<br>
The video below shows the demo site being used, where;

* Single then multiple updates are made to a basic DAG using the GUI.
* Then the back end is used to show updates to multipe DAGs and multiple nodes.

<video width="640"  controls>
    <source src="../videos/pydagoras.mp4" type="video/mp4">
</video>


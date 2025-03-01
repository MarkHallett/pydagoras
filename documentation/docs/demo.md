# Demo

The demo site [www.pydagoras.com](https://www.pydagoras.com/) provides the opertunity to update DAG inputs and see the DAG update.

First it is required to make a websocket connection, this will supply the backend with input values, and allow the browser to recieve updated DAGs.
To make this connection click the `connect` button, and see the connection status appear.
   ![connect](images/connect.png "connect")


The following tabs match the tabs in the browser and show screen shots of the 3 example DAG images.

=== "Basic DAG"
    ![basic_dag](images/basic_dag.png "basic_dag")
=== "Long calculation"
    ![long_calc_dag](images/long_calc_dag.png "long_calc_dag")
=== "Duplicate nodes"
    ![duplicate_nodes_dag](images/duplicate_nodes_dag.png "duplicate_nodes")

Below each DAG there are input boxes for the DAG input values.
Depending on the state of the toggle, values can be entered one at a time, or in bulk.
When the DAG has been recaluclated the image of the DAG will be refreshed.


The video below shows the demo site being used, where;

* Single then multiple updates are made to a basic DAG using the GUI.
* Then the back end is used to show updates to multipe DAGs and multiple nodes.

<video width="640"  controls>
    <source src="../videos/pydagoras.mp4" type="video/mp4">
</video>


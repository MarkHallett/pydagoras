# Example use
A small example application has been created and hosted to demonstrate how the `pydagoras` package can be used. The source code for the application is available on GitHub.

## System overview
The diagram below shows how the website connects, using websockets, to the front end process, and which connects to the backend process using FastAPI.
   ![system_overview](images/system_overview.png "system_overview")

## Front end
The frontend process running on the pydagoras sever provides a secure web site at [www.pydagoras.com](https://www.pydagoras.com/). On three tabs the site shows three different DAGs to demonstrate how the pydagoras Python package can be used to  create DAGs. It is possible to update the inputs of these DAGs either individually or in bulk, and see the resulting effect on the DAGs. From a browser it is necessary to open a secure websocket to the frontend process, which collects updates to the input data, and passes it on to the backend using FastAPI.

## Backend
The backend process creates three example DAGs, it does this by defining each of the nodes in tearms of input parameters and a calculation function. When an input changes the output of the node is recalculated, this new output is then passed to input nodes further along the DAG. Finally when the output of the DAG is changed, the new status of the whole DAG is returned.



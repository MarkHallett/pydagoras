# Example app
A small example application has been created and hosted to demonstrate how the `pydagoras` package can be used. The source code for the application is available on GitHub.

## System overview
The diagram below shows how the website connects, to the front end process, and which connects to the backend process using FastAPI and websockets.
   ![system_overview](images/system_overview.png "system_overview")

## Front end
The frontend process, running on the pydagoras sever, provides a secure web site at [www.pydagoras.com](https://www.pydagoras.com/). On three tabs the site shows three different DAGs to demonstrate how the pydagoras Python package can be used to create DAGs. It is possible to update the inputs of these DAGs either individually or in bulk, and see the resulting effect on the DAGs. By opening the site from a browser, a secure websocket from the frontend to the backend is created, This connection is used to update the browser with DAG updates as they happen. The frontend also can be used to send updates to the backend using FastAPI. 

## Backend
The backend process creates the three example DAGs, it does this by defining each of the nodes in tearms of input parameters and a calculation function. When an input of a node changes the output of the node is recalculated. This new output is then passed to other input nodes further along the DAG. Finally when the output of the DAG changes, the new status of the whole DAG is returned, this is serverd by the frontend and is visable in the browser.



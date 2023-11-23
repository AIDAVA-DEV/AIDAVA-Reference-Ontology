# Changes Folder

This folder contains all the changes made to the project. Each change is a folder with the following structure:

```bash
changes
└───change_issue_number
    └───README.md
    └───apply.py
```

The `apply.py` file contains the code that implements the change. The `README.md` file contains a description of the change.

`apply.py` should contain a function called `apply` that takes a `Graph` object as input and returns a `Graph` object as output.

```python
from rdflib import Graph
    
def apply(graph: Graph) -> Graph:
    # Code that implements the change
    return graph
```

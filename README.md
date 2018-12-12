 IoT Functions

A companion package to IBM Watson IoT Platform Analytics containing some custom function prototypes.

## Getting Started

These instructions will get you up and running in your local environment or in Watson Studio for development and testing purposes. 

### Prerequisites

 + python 3.X
 + numpy
 + pandas
 + iotfunctions

### Installing

To install in your local environment:
```
pip install git+https://github.com/aeisma/iot-functions.git@ --upgrade
```

To install in IBM Watson Studio from another Jupyter notebook:
```
!pip install git+https://github.com/aeisma/iot-functions.git@ --upgrade
```

Test for sucessful install:
```
import pocfunctions as fn
print(fn.__version__)
```

### Further information

+ [IBM Knowledge Center - IoT Platform Analytics](https://www.ibm.com/support/knowledgecenter/SSQP8H/iot/analytics/as_overview.html)
+ [Sample Notebook](https://www.ibm.com/support/knowledgecenter/SSQP8H/iot/analytics/as_notebook_references.html)



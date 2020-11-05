# Example JSON parsing app with tests
Python project to demonstrate simple app creation and testing approach.  

### Getting Started
- install python3.8+  
- install requirements `pip install -r requirements.txt`
- run tests `python -m pytest -v tests`

### Framework 
**json_parser/** contains the JSON parsing function `json_parser` and helper class.  
**tests/** tests separated into success and error scenarios.  
**requirements.txt** external libraries used to facilitate testing efforts e.g. pytest.  

### Notes:
Many implementation details were done in creative liberty as the ACs were vague e.g. score must be of type int.

### Improvements
Given more time, the app would be packaged and installed, prior to running tests.  
Unit tests would be added around the ParsedModel class.  
If this were to be part of a pipeline, we would dockerize the entire flow.  
Test reports and logging may be added for more comprehensive debugging.  

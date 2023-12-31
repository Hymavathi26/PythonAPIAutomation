# Python API automation

Hybrid custom Framework to test the rest APIs
![image](https://github.com/Hymavathi26/PythonAPIAutomation/assets/147125836/4d28033f-27f1-42cd-b91d-61fe43f10002)
![image](https://github.com/Hymavathi26/PythonAPIAutomation/assets/147125836/dc9c295b-fc21-4be5-a3ce-15882f68d749)
![image](https://github.com/Hymavathi26/PythonAPIAutomation/assets/147125836/88dece49-0883-462a-bbe0-4978bdea27f3)

### Tech stack
1. python 3.11
2. Requests -HTTP Requests
3. pytest - testing framework
4. Reporting - allure reporting,pytest html
5. Test Data - CSV, Excel,JSON
6. Parallel execution - x distrubute


### How to inatall packages
``pip install requests pytest pytest-html faker allure-pytest jsonschema
``

### To freeze your package version  
``pip freeze > requirements.txt``   --showing all required packages

### To install the freeze version
``pip install -r requirements.txt``   --for specific version only showing

### how to run testcases parallel
`` pip install pytest-xdist ``   ---for paraller execution need to instal this package




`` pytest -n auto tests/integration_test/test_create_booking.py -s -v ``-->to print all details about logs in console

### to work with the excel file
``pip install openpyxl
``
### to work with json schema validation
``pip install jsonschema ``

# Autotesting framework for HomeBuddy homeowners application

Simple test framework with automatic tests written on Python.

# UI testing

This is simple UI testing program, that uses Python, PyTest and Selenium web driver to manage UI testing 
of https://hb-autotests.stage.sirenltd.dev/ site.

### Prerequisites

This framework uses Chrome driver, so the Chrome web browser should be installed.
If you want to use this framework with another browser, you need to download another driver and specify it
for browser fixture in conftest.py.
See more [here](https://selenium-python.readthedocs.io/installation.html#drivers)

### Installing

To install and run tests:

```
$ git clone https://github.com/PavelStrukov/home-buddy-test-task.git

$ cd home-buddy-test-task

$ python3 -m virtualenv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ pytest path/to/test_name.py
```

Note: to see generated allure reports you need **allure to be installed** on your computer.
    See more [here](https://docs.qameta.io/allure/#_installing_a_commandline)

## Running the tests

To run all tests:
```
$ pytest
```
To run specific test:
```
$ pytest /path/to/test_file.py::TestClass::test_name
```

#### Allure test report

To generate allure test reports run tests with following additional option:

```
$ pytest --alluredir=/tmp/my_allure_results
```

To see test results:
```
$ allure serve /tmp/my_allure_results
```

## Built With

* [PyTest](https://docs.pytest.org/en/latest/) - Test framework
* [Selenium Web Driver](https://www.selenium.dev/documentation/en/webdriver/) - Driver for web browser access
* [Allure Test Report](https://docs.qameta.io/allure/) - a framework designed to create test execution reports

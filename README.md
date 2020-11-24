# Otus - Integration testing
Integration tests are another important aspect with the testing that we perform here. Frontend
and backend development come together at an integration point and testing this layer is a part
of the testing pyramid that is essential in ensuring good test coverage.

## Technologies used and tested
* vscode
* python 3.7.1
* urllib3 1.26.2
* certifi 2020.11.8
* chardet 3.0.4
* idna 2.10
* requests 2.25.0

## Requirements
* Have Python 3.* installed.
* CD into github project.
* Install a virtual environment (Optional).
    * ```console
        $ pip install virtualenv
        ```
    * ```console
        $ virtualenv env
        ```
    * On Linux:
        ```console
        $ source env/bin/activate
        ```
    * On Windows:
        ```console
        $ & env\Scripts\activate
        ```
* Install required packages
    * ```console
        $ pip install -r requirements.txt
        ```
* To execute a test case from a file:
    ```console
    $ python .\Test_assessment_response.py 
    ```
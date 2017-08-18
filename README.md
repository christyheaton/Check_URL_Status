### Summary

check_urls.py tests the HTTP status of all the URLs in a file.

### Requirements
* [Python 3](https://www.python.org/download/releases/3.0/)

### Dependencies
* [pytest](https://docs.pytest.org/en/latest/)
* [argparse](https://docs.python.org/3/library/argparse.html)
* [requests](http://docs.python-requests.org/en/master/)

### Command line inputs

**-i** File containing URLs to test **Required**

**-o** Output file otherwise uses stdout

**-h** Prints command line arguments help

### Sample runs

* Test the status of all URLs in the specified file and output results to standard output (must be run in same directory as check_urls.py)
```
python check_urls.py -i C:/Temp/urls_test.txt
```

* Test the status of all URLs in the specified file and save results to a specified log file (must be run in same directory as check_urls.py)
```
python check_urls.py -i C:/Temp/urls_test.txt -o C:/Temp/log.txt
```

* Run the test suite (must be run in same directory as check_urls.py and test_check_urls.py)
```
pytest
```

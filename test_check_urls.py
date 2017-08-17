import pytest
import os
import check_urls

def test_response_200():
    assert check_urls.get_status_code('http://httpstat.us/200') == 200

def test_response_201():
    assert check_urls.get_status_code('http://httpstat.us/201') == 201

def test_response_305():
    assert check_urls.get_status_code('http://httpstat.us/305') == 305

def test_response_403():
    assert check_urls.get_status_code('http://httpstat.us/403') == 403

def test_response_404():
    assert check_urls.get_status_code('http://httpstat.us/404') == 404

def test_response_417():
    assert check_urls.get_status_code('http://httpstat.us/417') == 417

def test_response_500():
    assert check_urls.get_status_code('http://httpstat.us/500') == 500

def test_response_524():
    assert check_urls.get_status_code('http://httpstat.us/524') == 524

def test_url_retrieve():
    assert check_urls.read_urls_from_file(os.getcwd() + '/urls_test.txt') == ['http://httpstat.us/200','http://httpstat.us/201','http://httpstat.us/305','http://httpstat.us/403','http://httpstat.us/404','http://httpstat.us/417','http://httpstat.us/500','http://httpstat.us/524']

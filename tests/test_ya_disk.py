from unittest.mock import patch

import pytest
import requests

from ya_disk import YaDiskManager, VALID_YD_TOKEN, BAD_YD_TOKEN


ya_disk_manager_valid = YaDiskManager(VALID_YD_TOKEN)
ya_disk_manager_bad = YaDiskManager(BAD_YD_TOKEN)
folder_name = 'test_folder'

@pytest.fixture(autouse=False)
def clean_folder():
    if ya_disk_manager_valid.find_folder(folder_name) == 200:
        ya_disk_manager_valid.delete_folder(folder_name)
        
    yield
    
    if ya_disk_manager_valid.find_folder(folder_name) == 200:
        ya_disk_manager_valid.delete_folder(folder_name)

def test_ya_disk_manager_find_folder_failure_404(clean_folder):
    status_code = ya_disk_manager_valid.find_folder(folder_name)
    assert status_code == 404

def test_ya_disk_manager_create_and_find_folder_success_201(clean_folder):
    create_code = ya_disk_manager_valid.create_folder(folder_name)
    assert create_code in (200, 201)
    find_code = ya_disk_manager_valid.find_folder(folder_name)
    assert find_code == 200

def test_ya_disk_manager_create_folder_failure_409(clean_folder):
    ya_disk_manager_valid.create_folder(folder_name)
    status_code = ya_disk_manager_valid.create_folder(folder_name)
    assert status_code == 409
    
def test_ya_disk_manager_delete_folder_success_202(clean_folder):
    ya_disk_manager_valid.create_folder(folder_name)
    delete_code = ya_disk_manager_valid.delete_folder(folder_name)
    assert delete_code in (200, 202, 204)

def test_ya_disk_manager_delete_folder_failure_404(clean_folder):
    status_code = ya_disk_manager_valid.delete_folder(folder_name)
    assert status_code == 404

def test_ya_disk_manager_authorization_error_401():
    status_code = ya_disk_manager_bad.find_folder(folder_name)
    assert status_code == 401

def test_ya_disk_manager_network_error_502():
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError
        status_code = ya_disk_manager_valid.find_folder(folder_name)
        assert status_code == 502

def test_ya_disk_manager_timeout_error_504():
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.exceptions.Timeout
        status_code = ya_disk_manager_valid.find_folder(folder_name)
        assert status_code == 504

def test_ya_disk_manager_request_exception_error_500():
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException
        status_code = ya_disk_manager_valid.find_folder(folder_name)
        assert status_code == 500

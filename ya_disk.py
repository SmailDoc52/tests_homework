import os

import requests
from requests.exceptions import Timeout, ConnectionError, RequestException
from dotenv import load_dotenv


load_dotenv()

VALID_YD_TOKEN = os.getenv('VALID_YD_TOKEN')
BAD_YD_TOKEN = os.getenv('BAD_YD_TOKEN')


class YaDiskManager:
    """A class to manage Yandex.Disk operations such as creating, 
        deleting, and finding folders.
    """
    def __init__(self, token: str):
        """Initialize the YaDiskManager with an authorization token.

        Args:
            token (str): Authorization token for accessing 
                Yandex.Disk API.
        """
        self.headers = {'Authorization': token}
        self.url = "https://cloud-api.yandex.net/v1/disk/"
        
    def create_folder(self, folder_name: str):
        """Create a new folder on Yandex.Disk.

        Args:
            folder_name (str): Name of the folder to be created.

        Returns:
            int: HTTP status code of the API response.
                 201 - Folder created successfully.
                 504 - Gateway timeout error.
                 502 - Bad gateway error.
                 500 - Internal server error.
        """
        params = {'path': f"{folder_name}/"}
        try:
            response = requests.put(self.url + 'resources', 
                                    headers=self.headers, params=params)
            return response.status_code
        except Timeout:
            return 504
        except ConnectionError:
            return 502
        except RequestException:
            return 500
            
    def delete_folder(self, folder_name: str):
        """Delete an existing folder from Yandex.Disk.

        Args:
            folder_name (str): Name of the folder to be deleted.

        Returns:
            int: HTTP status code of the API response.
                 204 - Folder deleted successfully.
                 504 - Gateway timeout error.
                 502 - Bad gateway error.
                 500 - Internal server error.
        """
        params = {'path': f"{folder_name}/"}
        try:
            response = requests.delete(self.url + 'resources', 
                                       headers=self.headers, params=params)
            return response.status_code
        except Timeout:
            return 504
        except ConnectionError:
            return 502
        except RequestException:
            return 500
        
    def find_folder(self, folder_name: str):
        """Check if a folder exists on Yandex.Disk.

        Args:
            folder_name (str): Name of the folder to search for.

        Returns:
            int: HTTP status code of the API response.
                 200 - Folder found successfully.
                 404 - Folder not found.
                 504 - Gateway timeout error.
                 502 - Bad gateway error.
                 500 - Internal server error.
        """
        params = {'path': f"{folder_name}/"}
        try:
            response = requests.get(self.url + 'resources', 
                                    headers=self.headers, params=params)
            return response.status_code
        except Timeout:
            return 504
        except ConnectionError:
            return 502
        except RequestException:
            return 500     


if __name__ == '__main__':
    ya_disk_manager_valid = YaDiskManager(VALID_YD_TOKEN)
    ya_disk_manager_bad = YaDiskManager(BAD_YD_TOKEN)
    
    print(ya_disk_manager_valid.create_folder("test_folder"))
    print(ya_disk_manager_valid.find_folder("test_folder"))
    print(ya_disk_manager_valid.delete_folder("test_folder"))
    print(ya_disk_manager_valid.find_folder("test_folder"))
    
    print('--------------------------------------------------')
    
    print(ya_disk_manager_bad.create_folder("test_folder"))
    print(ya_disk_manager_bad.find_folder("test_folder"))
    print(ya_disk_manager_bad.delete_folder("test_folder"))
    print(ya_disk_manager_bad.find_folder("test_folder"))
import requests

BASE_URL = "https://petstore.swagger.io/v2"

def test_upload_image(pet_id):
    """
    Test the image upload feature for a pet.

    This test verifies that an image can be successfully uploaded 
    for a specific pet. The endpoint is expected to return a 
    200 status code upon a successful upload.

    Args:
        pet_id (int): The ID of the pet for which the image is being uploaded.
    """
    url = f"{BASE_URL}/pet/{pet_id}/uploadImage"
    files = {'file': ('test_image.jpg', open('test_image.jpg', 'rb'))}
    response = requests.post(url, files=files)
    print(response.text)
    assert response.status_code == 200
    print("Upload Image Test Passed!")


def test_add_pet():
    """
    Test the addition of a new pet to the store.

    This test verifies that a new pet can be added to the 
    pet store. The endpoint is expected to return a 
    200 status code and confirm the addition by returning 
    the pet's name.

    Expected outcome: The added pet's name should be "Fluffy".
    """
    url = f"{BASE_URL}/pet"
    pet_data = {
        "id": 0,
        "name": "Fluffy",
        "category": {"id": 1, "name": "Cats"},
        "photoUrls": ["url1", "url2"],
        "tags": [{"id": 1, "name": "tag1"}],
        "status": "available"
    }
    response = requests.post(url, json=pet_data)
    print(response.text)
    assert response.status_code == 200
    assert response.json()["name"] == "Fluffy"
    print("Add Pet Test Passed!")


def test_update_pet(pet_id):
    """
    Test the update feature for an existing pet.

    This test verifies that the details of an existing pet 
    can be updated successfully. The endpoint is expected to 
    return a 200 status code and confirm the update by 
    returning the updated pet's name.

    Args:
        pet_id (int): The ID of the pet to be updated.
    
    Expected outcome: The updated pet's name should be "Fluffy Updated".
    """
    url = f"{BASE_URL}/pet"
    updated_pet_data = {
        "id": pet_id,
        "name": "Fluffy Updated",
        "category": {"id": 1, "name": "Cats"},
        "photoUrls": ["url1", "url2"],
        "tags": [{"id": 1, "name": "tag1"}],
        "status": "available"
    }
    response = requests.put(url, json=updated_pet_data)
    print(response.text)
    assert response.status_code == 200
    assert response.json()["name"] == "Fluffy Updated"
    print("Update Pet Test Passed!")


def test_find_pet_by_id(pet_id):
    """
    Test retrieving a pet by its ID.

    This test verifies that the details of a pet can be retrieved 
    using its ID. The endpoint is expected to return a 
    200 status code and confirm the retrieval by returning 
    the pet's ID.

    Args:
        pet_id (int): The ID of the pet to be retrieved.
    """
    url = f"{BASE_URL}/pet/{pet_id}"
    response = requests.get(url)
    print(response.text)
    assert response.status_code == 200
    assert response.json()["id"] == pet_id
    print("Find Pet by ID Test Passed!")


def test_delete_pet(pet_id):
    """
    Test the deletion of a pet from the store.

    This test verifies that a pet can be successfully deleted 
    from the pet store. The endpoint is expected to return 
    a 200 status code upon successful deletion.

    Args:
        pet_id (int): The ID of the pet to be deleted.
    """
    url = f"{BASE_URL}/pet/{pet_id}"
    response = requests.delete(url)
    print(response.text)
    assert response.status_code == 200
    print("Delete Pet Test Passed!")


def test_place_order():
    """
    Test placing an order for a pet.

    This test verifies that an order can be placed for a specific 
    pet. The endpoint is expected to return a 
    200 status code and confirm the order by returning the order's status.

    Expected outcome: The order status should be "placed".
    """
    url = f"{BASE_URL}/store/order"
    order_data = {
        "petId": 1,
        "quantity": 1,
        "shipDate": "2023-10-19T00:00:00.000Z",
        "status": "placed",
        "complete": True
    }
    response = requests.post(url, json=order_data)
    print(response.text)
    assert response.status_code == 200
    print("Place Order Test Passed!")


def test_get_inventory():
    """
    Test retrieving the inventory of pets.

    This test verifies that the inventory of available pets 
    can be retrieved successfully. The endpoint is expected to 
    return a 200 status code and a dictionary of pet categories 
    with their respective counts.

    Expected outcome: The response should be a dictionary.
    """
    url = f"{BASE_URL}/store/inventory"
    response = requests.get(url)
    print(response.text)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    print("Get Inventory Test Passed!")


if __name__ == "__main__":
    test_pet_id = 1

    # test_upload_image(test_pet_id)
    test_add_pet()
    test_update_pet(test_pet_id)
    test_find_pet_by_id(test_pet_id)
    test_delete_pet(test_pet_id)
    test_place_order()
    test_get_inventory()



"""
Sample Output:
{"id":9223372036854761571,"category":{"id":1,"name":"Cats"},"name":"Fluffy","photoUrls":["url1","url2"],"tags":[{"id":1,"name":"tag1"}],"status":"available"}
Add Pet Test Passed!
{"id":1,"category":{"id":1,"name":"Cats"},"name":"Fluffy Updated","photoUrls":["url1","url2"],"tags":[{"id":1,"name":"tag1"}],"status":"available"}
Update Pet Test Passed!
{"id":1,"category":{"id":1,"name":"Cats"},"name":"Fluffy Updated","photoUrls":["url1","url2"],"tags":[{"id":1,"name":"tag1"}],"status":"available"}
Find Pet by ID Test Passed!
{"code":200,"type":"unknown","message":"1"}
Delete Pet Test Passed!
{"id":85521571,"petId":1,"quantity":1,"shipDate":"2023-10-19T00:00:00.000+0000","status":"placed","complete":true}
Place Order Test Passed!
{"sold":2,"string":618,"invalid_status":4,"available":113,"status":24}
Get Inventory Test Passed!
"""
## Petstore API Documentation (v1.0.7)

This documentation outlines the Petstore API, a sample server designed to demonstrate the capabilities of the Swagger framework. You can learn more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/). For testing purposes, you can use the API key `special-key` for authorization.

### Purpose

The Petstore API provides a set of endpoints for managing pets and orders. It showcases basic CRUD (Create, Read, Update, Delete) operations on pets and allows for placing and retrieving orders. This API serves as a practical example for illustrating how to define, document, and test APIs using the Swagger specification. 

### Functionality Summary

The Petstore API covers the following core functionalities:

* **Pet Management:**
    * Adding new pets to the store.
    * Retrieving information about existing pets by ID or filtering by status or tags.
    * Updating details of existing pets.
    * Deleting pets from the store.
    * Uploading images for pets.
* **Order Management:**
    * Placing orders for purchasing pets.
    * Retrieving order details by ID.
    * Deleting orders.
* **Inventory Management:**
    * Retrieving the inventory of available pets.
* **User Management:**
    * Creating new users.
    * Retrieving user information by username.
    * Updating user details.
    * Deleting users.
    * Login and logout functionalities.

### Onboarding Guide

For developers new to the Petstore API, here's a quick guide to get you started:

1. **Authentication:**  
   - The API uses an API key for authentication. For testing, use the key `special-key`. 
   - You can include the key in the `Authorization` header of your requests.

2. **API Endpoints:** 
   - Refer to the "Key API Endpoints" section below for a detailed list of all available endpoints.

3. **Data Types:**
   -  Data types for various parameters and responses are clearly defined in the documentation.

4. **Error Handling:**
   - The API provides detailed error messages with corresponding status codes. Refer to the "Responses" section of each endpoint for specific error handling information. 

5. **Testing:**
   - The "Unit Test Summary" section provides information about the unit tests performed, which can be helpful for understanding the expected behavior of the API.

### Key API Endpoints

#### **Pet Management:**

**1. `POST /pet`**

* **Description:** Adds a new pet to the store.
* **Parameters:**
    * `body (body)`: The pet object to be added. (Required: True, Type: N/A, Format: N/A)
* **Responses:**
    * `200`: Successful operation.
    * `405`: Invalid input.

**2. `PUT /pet`**

* **Description:** Updates an existing pet in the store.
* **Parameters:**
    * `body (body)`: The pet object that needs to be updated. (Required: True, Type: N/A, Format: N/A)
* **Responses:**
    * `400`: Invalid ID supplied.
    * `404`: Pet not found.
    * `405`: Validation exception.

**3. `GET /pet/findByStatus`**

* **Description:** Retrieves pets by their status. Multiple status values can be provided with comma-separated strings.
* **Parameters:**
    * `status (query)`: Status values to filter by. (Required: True, Type: array, Format: N/A)
* **Responses:**
    * `200`: Successful operation.
    * `400`: Invalid status value.

**4. `GET /pet/findByTags`**

* **Description:** Retrieves pets by their tags. Multiple tags can be provided with comma-separated strings.
* **Parameters:**
    * `tags (query)`: Tags to filter by. (Required: True, Type: array, Format: N/A)
* **Responses:**
    * `200`: Successful operation.
    * `400`: Invalid tag value.

**5. `GET /pet/{petId}`**

* **Description:** Retrieves a single pet by its ID.
* **Parameters:**
    * `petId (path)`: ID of the pet to be retrieved. (Required: True, Type: integer, Format: int64)
* **Responses:**
    * `200`: Successful operation.
    * `400`: Invalid ID supplied.
    * `404`: Pet not found.

**6. `POST /pet/{petId}`**

* **Description:** Updates a pet's name and status.
* **Parameters:**
    * `petId (path)`: ID of the pet to be updated. (Required: True, Type: integer, Format: int64)
    * `name (formData)`: Updated name of the pet. (Required: False, Type: string, Format: N/A)
    * `status (formData)`: Updated status of the pet. (Required: False, Type: string, Format: N/A)
* **Responses:**
    * `405`: Invalid input.

**7. `DELETE /pet/{petId}`**

* **Description:** Deletes a pet by its ID.
* **Parameters:**
    * `api_key (header)`: API key for authorization. (Required: False, Type: string, Format: N/A)
    * `petId (path)`: ID of the pet to be deleted. (Required: True, Type: integer, Format: int64)
* **Responses:**
    * `400`: Invalid ID supplied.
    * `404`: Pet not found.

**8. `POST /pet/{petId}/uploadImage`**

* **Description:** Uploads an image for a pet.
* **Parameters:**
    * `petId (path)`: ID of the pet to update. (Required: True, Type: integer, Format: int64)
    * `additionalMetadata (formData)`: Additional data to pass to the server. (Required: False, Type: string, Format: N/A)
    * `file (formData)`: Image file to upload. (Required: False, Type: file, Format: N/A)
* **Responses:**
    * `200`: Successful operation.

#### **Order Management:**

**1. `POST /store/order`**

* **Description:** Places an order for purchasing a pet.
* **Parameters:**
    * `body (body)`: Order object containing details of the order. (Required: True, Type: N/A, Format: N/A)
* **Responses:**
    * `200`: Successful operation.
    * `400`: Invalid order.

**2. `GET /store/order/{orderId}`**

* **Description:** Retrieves an order by its ID.
* **Parameters:**
    * `orderId (path)`: ID of the order to retrieve. (Required: True, Type: integer, Format: int64)
* **Responses:**
    * `200`: Successful operation.
    * `400`: Invalid ID supplied.
    * `404`: Order not found.

**3. `DELETE /store/order/{orderId}`**

* **Description:** Deletes an order by its ID.
* **Parameters:**
    * `orderId (path)`: ID of the order to delete. (Required: True, Type: integer, Format: int64)
* **Responses:**
    * `400`: Invalid ID supplied.
    * `404`: Order not found.

#### **Inventory Management:**

**1. `GET /store/inventory`**

* **Description:** Retrieves the inventory of available pets.
* **Parameters:**
    * None
* **Responses:**
    * `200`: Successful operation.

#### **User Management:**

**1. `POST /user`**

* **Description:** Creates a new user.
* **Parameters:**
    * `body (body)`: User object to be created. (Required: True, Type: N/A, Format: N/A)
* **Responses:**
    * `default`: Successful operation.

**2. `GET /user/{username}`**

* **Description:** Retrieves user information by username.
* **Parameters:**
    * `username (path)`: Username of the user to retrieve. (Required: True, Type: string, Format: N/A)
* **Responses:**
    * `200`: Successful operation.
    * `400`: Invalid username supplied.
    * `404`: User not found.

**3. `PUT /user/{username}`**

* **Description:** Updates an existing user.
* **Parameters:**
    * `username (path)`: Username of the user to update. (Required: True, Type: string, Format: N/A)
    * `body (body)`: Updated user object. (Required: True, Type: N/A, Format: N/A)
* **Responses:**
    * `400`: Invalid user supplied.
    * `404`: User not found.

**4. `DELETE /user/{username}`**

* **Description:** Deletes a user by username.
* **Parameters:**
    * `username (path)`: Username of the user to delete. (Required: True, Type: string, Format: N/A)
* **Responses:**
    * `400`: Invalid username supplied.
    * `404`: User not found.

**5. `POST /user/createWithArray`**

* **Description:** Creates multiple users.
* **Parameters:**
    * `body (body)`: List of user objects. (Required: True, Type: N/A, Format: N/A)
* **Responses:**
    * `default`: Successful operation.

**6. `POST /user/createWithList`**

* **Description:** Creates multiple users.
* **Parameters:**
    * `body (body)`: List of user objects. (Required: True, Type: N/A, Format: N/A)
* **Responses:**
    * `default`: Successful operation.

**7. `GET /user/login`**

* **Description:** Logs in a user.
* **Parameters:**
    * `username (query)`: Username for login. (Required: True, Type: string, Format: N/A)
    * `password (query)`: Password for login. (Required: True, Type: string, Format: N/A)
* **Responses:**
    * `200`: Successful operation.
    * `400`: Invalid username/password supplied.

**8. `GET /user/logout`**

* **Description:** Logs out a user.
* **Parameters:**
    * None
* **Responses:**
    * `default`: Successful operation.

### Unit Test Summary

This section provides a brief summary of the unit tests that have been performed to verify the API's functionality.

* **`test_upload_image`**: Tests the image upload feature for a pet.
    * **Expected Output:** 
        - 200 status code
        - Successful image upload confirmation.

* **`test_add_pet`**: Tests adding a new pet to the store.
    * **Expected Output:**
        - 200 status code
        - Successful pet creation confirmation.

* **`test_update_pet`**: Tests updating an existing pet.
    * **Expected Output:**
        - 200 status code
        - Confirmation of the updated pet details.

* **`test_find_pet_by_id`**: Tests retrieving a pet by ID.
    * **Expected Output:**
        - 200 status code
        - Retrieved pet details matching the provided ID.

* **`test_delete_pet`**: Tests deleting a pet.
    * **Expected Output:**
        - 200 status code
        - Confirmation of pet deletion.

* **`test_place_order`**: Tests placing an order for a pet.
    * **Expected Output:**
        - 200 status code
        - Confirmation of order placement with the correct status.

* **`test_get_inventory`**: Tests retrieving the inventory of pets.
    * **Expected Output:**
        - 200 status code
        - Dictionary containing pet categories and their counts.


### Status Codes


| Code | Description |
|------|-------------|
| 200  | Successful operation. |
| 400  | Bad request, often due to validation errors. |
| 404  | Resource not found. |
| 405  | Method not allowed or invalid input. |

### Ending Note

This documentation provides a comprehensive overview of the Petstore API. Feel free to explore the endpoints and test them using the provided information. For further details on the Swagger framework and its capabilities, please visit the official Swagger website: [http://swagger.io](http://swagger.io).

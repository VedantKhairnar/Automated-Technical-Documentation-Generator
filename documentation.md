## Petstore API Documentation (v1.0.7)

This documentation provides a comprehensive overview of the Petstore API, outlining its purpose, functionality, and key endpoints. The Petstore API is a sample API server designed for demonstrating the capabilities of Swagger, a tool for designing, building, and documenting RESTful APIs.

### Purpose Explanation

The Petstore API is a simulated online store for pets. It allows users to manage pet information, place orders, and interact with an inventory system. This API serves as a practical example for understanding RESTful API design principles and best practices.

### Functionality Summary

The Petstore API provides the following key functionalities, validated by unit tests:

- **Pet Management:** 
    - **Adding Pets:** New pets can be added to the store with specific details like name, category, and status.
    - **Updating Pets:** Existing pet details can be updated, including name and status.
    - **Retrieving Pets:** Pets can be retrieved by their unique IDs or by filtering based on status or tags.
    - **Deleting Pets:** Pets can be removed from the store.
- **Order Management:**
    - **Placing Orders:** Users can place orders for specific pets.
    - **Retrieving Orders:** Orders can be fetched based on their unique IDs.
    - **Deleting Orders:** Orders can be cancelled.
- **Inventory Management:**
    - **Retrieving Inventory:** The API allows users to retrieve a map of pet status codes and their corresponding quantities in the inventory.
- **User Management:**
    - **Creating Users:** Users can be registered with the system.
    - **Retrieving Users:** User information can be fetched by username.
    - **Updating Users:** Logged-in users can update their own profile information.
    - **Deleting Users:** Logged-in users can delete their accounts.
    - **Login/Logout:** Users can authenticate and log out of the system.

### Onboarding Guide

For developers onboarding to the Petstore API, here's a quick guide:

1. **Understanding RESTful API Basics:** Familiarize yourself with the RESTful API design principles (e.g., resources, HTTP methods, status codes).
2. **API Key:** For testing authorization filters, use the API key `special-key`.
3. **Explore the Documentation:** Carefully review the documentation for each endpoint, including the required parameters, expected responses, and any specific notes.
4. **Use a REST Client:** Employ a tool like Postman or cURL to interact with the API endpoints and send requests.
5. **Test Thoroughly:** Utilize the unit test examples provided to verify the API's functionality and gain insights into expected behaviors.

### Key API Endpoints

#### Pet Management

**1. Upload Image:**
    - Path: `/pet/{petId}/uploadImage`
    - Method: `POST`
    - Description: Upload an image for a specific pet.
    - Parameters:
        - `petId` (path): ID of the pet (Required: True, Type: integer, Format: int64)
        - `additionalMetadata` (formData): Additional data to pass to the server (Required: False, Type: string)
        - `file` (formData): File to upload (Required: False, Type: file)
    - Responses:
        - `200`: Successful operation

**2. Add Pet:**
    - Path: `/pet`
    - Method: `POST`
    - Description: Add a new pet to the store.
    - Parameters:
        - `body` (body): Pet object to be added (Required: True, Type: N/A)
    - Responses:
        - `405`: Invalid input

**3. Update Pet:**
    - Path: `/pet`
    - Method: `PUT`
    - Description: Update an existing pet in the store.
    - Parameters:
        - `body` (body): Pet object to be updated (Required: True, Type: N/A)
    - Responses:
        - `400`: Invalid ID supplied
        - `404`: Pet not found
        - `405`: Validation exception

**4. Find Pets by Status:**
    - Path: `/pet/findByStatus`
    - Method: `GET`
    - Description: Retrieve pets based on their status. Multiple status values can be provided with comma-separated strings.
    - Parameters:
        - `status` (query): Status values to filter by (Required: True, Type: array)
    - Responses:
        - `200`: Successful operation
        - `400`: Invalid status value

**5. Find Pets by Tags:**
    - Path: `/pet/findByTags`
    - Method: `GET`
    - Description: Retrieve pets based on their tags. Multiple tags can be provided with comma-separated strings. 
    - Parameters:
        - `tags` (query): Tags to filter by (Required: True, Type: array)
    - Responses:
        - `200`: Successful operation
        - `400`: Invalid tag value

**6. Get Pet by ID:**
    - Path: `/pet/{petId}`
    - Method: `GET`
    - Description: Retrieve a specific pet based on its ID.
    - Parameters:
        - `petId` (path): ID of the pet to return (Required: True, Type: integer, Format: int64)
    - Responses:
        - `200`: Successful operation
        - `400`: Invalid ID supplied
        - `404`: Pet not found

**7. Update Pet by ID:**
    - Path: `/pet/{petId}`
    - Method: `POST`
    - Description: Update the details of a specific pet.
    - Parameters:
        - `petId` (path): ID of the pet to be updated (Required: True, Type: integer, Format: int64)
        - `name` (formData): Updated name of the pet (Required: False, Type: string)
        - `status` (formData): Updated status of the pet (Required: False, Type: string)
    - Responses:
        - `405`: Invalid input

**8. Delete Pet by ID:**
    - Path: `/pet/{petId}`
    - Method: `DELETE`
    - Description: Delete a pet from the store.
    - Parameters:
        - `api_key` (header): Authorization key (Required: False, Type: string)
        - `petId` (path): ID of the pet to delete (Required: True, Type: integer, Format: int64)
    - Responses:
        - `400`: Invalid ID supplied
        - `404`: Pet not found

#### Order Management

**1. Place Order:**
    - Path: `/store/order`
    - Method: `POST`
    - Description: Place an order for a pet.
    - Parameters:
        - `body` (body): Order object to be placed (Required: True, Type: N/A)
    - Responses:
        - `200`: Successful operation
        - `400`: Invalid Order

**2. Get Order by ID:**
    - Path: `/store/order/{orderId}`
    - Method: `GET`
    - Description: Retrieve an order by its ID. For valid responses, try integer IDs between 1 and 10.
    - Parameters:
        - `orderId` (path): ID of the order to be fetched (Required: True, Type: integer, Format: int64)
    - Responses:
        - `200`: Successful operation
        - `400`: Invalid ID supplied
        - `404`: Order not found

**3. Delete Order by ID:**
    - Path: `/store/order/{orderId}`
    - Method: `DELETE`
    - Description: Delete an order from the system. For valid responses, try positive integer IDs.
    - Parameters:
        - `orderId` (path): ID of the order to be deleted (Required: True, Type: integer, Format: int64)
    - Responses:
        - `400`: Invalid ID supplied
        - `404`: Order not found

#### Inventory Management

**1. Get Inventory:**
    - Path: `/store/inventory`
    - Method: `GET`
    - Description: Retrieve a map of pet status codes and their corresponding quantities.
    - Responses:
        - `200`: Successful operation

#### User Management

**1. Create User with List:**
    - Path: `/user/createWithList`
    - Method: `POST`
    - Description: Create multiple users.
    - Parameters:
        - `body` (body): List of user objects (Required: True, Type: N/A)
    - Responses:
        - `default`: Successful operation

**2. Get User by Username:**
    - Path: `/user/{username}`
    - Method: `GET`
    - Description: Retrieve a user by their username.
    - Parameters:
        - `username` (path): Username to be fetched (Required: True, Type: string)
    - Responses:
        - `200`: Successful operation
        - `400`: Invalid username supplied
        - `404`: User not found

**3. Update User by Username:**
    - Path: `/user/{username}`
    - Method: `PUT`
    - Description: Update the details of a specific user. This can only be done by the logged-in user.
    - Parameters:
        - `username` (path): Username to be updated (Required: True, Type: string)
        - `body` (body): Updated user object (Required: True, Type: N/A)
    - Responses:
        - `400`: Invalid user supplied
        - `404`: User not found

**4. Delete User by Username:**
    - Path: `/user/{username}`
    - Method: `DELETE`
    - Description: Delete a user from the system. This can only be done by the logged-in user.
    - Parameters:
        - `username` (path): Username to be deleted (Required: True, Type: string)
    - Responses:
        - `400`: Invalid username supplied
        - `404`: User not found

**5. Login:**
    - Path: `/user/login`
    - Method: `GET`
    - Description: Authenticate a user.
    - Parameters:
        - `username` (query): Username for login (Required: True, Type: string)
        - `password` (query): Password for login (Required: True, Type: string)
    - Responses:
        - `200`: Successful operation
        - `400`: Invalid username/password supplied

**6. Logout:**
    - Path: `/user/logout`
    - Method: `GET`
    - Description: Log out a user.
    - Responses:
        - `default`: Successful operation

**7. Create User with Array:**
    - Path: `/user/createWithArray`
    - Method: `POST`
    - Description: Create multiple users.
    - Parameters:
        - `body` (body): List of user objects (Required: True, Type: N/A)
    - Responses:
        - `default`: Successful operation

**8. Create User:**
    - Path: `/user`
    - Method: `POST`
    - Description: Create a new user. This can only be done by the logged-in user.
    - Parameters:
        - `body` (body): Created user object (Required: True, Type: N/A)
    - Responses:
        - `default`: Successful operation

### Ending Note

This documentation serves as a guide for interacting with the Petstore API. As you explore the API, remember to consult this documentation for detailed information on each endpoint and its associated functionalities. For further information about Swagger, please visit [http://swagger.io](http://swagger.io).
# Swagger Petstore (v1.0.7)

This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters.

## Path: /pet/{petId}/uploadImage
### Method: POST
Description: 
Parameters:
- petId (path): ID of pet to update (Required: True, Type: integer, Format: int64)
- additionalMetadata (formData): Additional data to pass to server (Required: False, Type: string, Format: N/A)
- file (formData): file to upload (Required: False, Type: file, Format: N/A)
Responses:
- 200: successful operation

## Path: /pet
### Method: POST
Description: 
Parameters:
- body (body): Pet object that needs to be added to the store (Required: True, Type: N/A, Format: N/A)
Responses:
- 405: Invalid input

### Method: PUT
Description: 
Parameters:
- body (body): Pet object that needs to be added to the store (Required: True, Type: N/A, Format: N/A)
Responses:
- 400: Invalid ID supplied
- 404: Pet not found
- 405: Validation exception

## Path: /pet/findByStatus
### Method: GET
Description: Multiple status values can be provided with comma separated strings
Parameters:
- status (query): Status values that need to be considered for filter (Required: True, Type: array, Format: N/A)
Responses:
- 200: successful operation
- 400: Invalid status value

## Path: /pet/findByTags
### Method: GET
Description: Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.
Parameters:
- tags (query): Tags to filter by (Required: True, Type: array, Format: N/A)
Responses:
- 200: successful operation
- 400: Invalid tag value

## Path: /pet/{petId}
### Method: GET
Description: Returns a single pet
Parameters:
- petId (path): ID of pet to return (Required: True, Type: integer, Format: int64)
Responses:
- 200: successful operation
- 400: Invalid ID supplied
- 404: Pet not found

### Method: POST
Description: 
Parameters:
- petId (path): ID of pet that needs to be updated (Required: True, Type: integer, Format: int64)
- name (formData): Updated name of the pet (Required: False, Type: string, Format: N/A)
- status (formData): Updated status of the pet (Required: False, Type: string, Format: N/A)
Responses:
- 405: Invalid input

### Method: DELETE
Description: 
Parameters:
- api_key (header): No description (Required: False, Type: string, Format: N/A)
- petId (path): Pet id to delete (Required: True, Type: integer, Format: int64)
Responses:
- 400: Invalid ID supplied
- 404: Pet not found

## Path: /store/inventory
### Method: GET
Description: Returns a map of status codes to quantities
Parameters:
Responses:
- 200: successful operation

## Path: /store/order
### Method: POST
Description: 
Parameters:
- body (body): order placed for purchasing the pet (Required: True, Type: N/A, Format: N/A)
Responses:
- 200: successful operation
- 400: Invalid Order

## Path: /store/order/{orderId}
### Method: GET
Description: For valid response try integer IDs with value >= 1 and <= 10. Other values will generated exceptions
Parameters:
- orderId (path): ID of pet that needs to be fetched (Required: True, Type: integer, Format: int64)
Responses:
- 200: successful operation
- 400: Invalid ID supplied
- 404: Order not found

### Method: DELETE
Description: For valid response try integer IDs with positive integer value. Negative or non-integer values will generate API errors
Parameters:
- orderId (path): ID of the order that needs to be deleted (Required: True, Type: integer, Format: int64)
Responses:
- 400: Invalid ID supplied
- 404: Order not found

## Path: /user/createWithList
### Method: POST
Description: 
Parameters:
- body (body): List of user object (Required: True, Type: N/A, Format: N/A)
Responses:
- default: successful operation

## Path: /user/{username}
### Method: GET
Description: 
Parameters:
- username (path): The name that needs to be fetched. Use user1 for testing.  (Required: True, Type: string, Format: N/A)
Responses:
- 200: successful operation
- 400: Invalid username supplied
- 404: User not found

### Method: PUT
Description: This can only be done by the logged in user.
Parameters:
- username (path): name that need to be updated (Required: True, Type: string, Format: N/A)
- body (body): Updated user object (Required: True, Type: N/A, Format: N/A)
Responses:
- 400: Invalid user supplied
- 404: User not found

### Method: DELETE
Description: This can only be done by the logged in user.
Parameters:
- username (path): The name that needs to be deleted (Required: True, Type: string, Format: N/A)
Responses:
- 400: Invalid username supplied
- 404: User not found

## Path: /user/login
### Method: GET
Description: 
Parameters:
- username (query): The user name for login (Required: True, Type: string, Format: N/A)
- password (query): The password for login in clear text (Required: True, Type: string, Format: N/A)
Responses:
- 200: successful operation
- 400: Invalid username/password supplied

## Path: /user/logout
### Method: GET
Description: 
Parameters:
Responses:
- default: successful operation

## Path: /user/createWithArray
### Method: POST
Description: 
Parameters:
- body (body): List of user object (Required: True, Type: N/A, Format: N/A)
Responses:
- default: successful operation

## Path: /user
### Method: POST
Description: This can only be done by the logged in user.
Parameters:
- body (body): Created user object (Required: True, Type: N/A, Format: N/A)
Responses:
- default: successful operation


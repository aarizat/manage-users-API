# manage-users-API
 API to create and get users
 
 
 ## Endpoint
 
 ```
 POST https://manage-users-api.herokuapp.com/api/v1/users
 GET https://manage-users-api.herokuapp.com/api/v1/users/<id>
 ```
 
 ## Examples:
 #### POST https://manage-users-api.herokuapp.com/api/v1/users
  
 * Payload:
 ```
 {
    "name": "pedro",
    "last_name": "rodriguez",
    "address": "calle 106A",
    "phone1": "321 776",
    "phone2": "3333333"
}
```
* Response:
```
{
  "user_id": "ID-GENERATED"
}
```
#### GET https://manage-users-api.herokuapp.com/api/v1/users/<id>
* Response
```
{
    "name": "pedro",
    "last_name": "rodriguez",
    "address": "calle 106A",
    "phone1": "321 776",
    "phone2": "3333333"
}
```

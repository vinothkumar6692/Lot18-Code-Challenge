<img src = "http://avis-vin.lefigaro.fr/var/img/91/22681-650x330-logo-lot18-noir-sur-fond-blanc-ok.jpg" align = "right" height="142" width="142">

# Lot18-Code-Challenge
A RESTful Web Service for a mock Wine store using Python Flask.

Introduction
=======

Acme wines is a mock wine store that delivers wine all over the country. When selling wine there are a number of rules and regulations that Acme must follow. The objective is to build a mock order validation and management service that will be used to determine if a data set of orders are considered valid or invalid. Acme often gets a large number of orders, so the program is expected to process a large amount of data quickly and efficiently.


Requirements
=======

* Python
* Python Flask
* Schematics
* Six

Validation Rules
=======

1) No wine can ship to New Jersey, Connecticut, Pennsylvania, Massachusetts, Illinois, Idaho or Oregon
2) Valid zip codes must be 5 or 9 digits
3) Everyone ordering must be 21 or older
4) Email address must be valid
5) The sum of digits in a zip code may not exceed 20 ("90210": 9+0+2+1+0 = 12)
6) Customers from NY may not have .net email addresses
7) If the state and zip code of the following record is the same as the current record, it automatically passes.

API Documentation
=======

All of the API route (Flask) implementations can be found in the `app.py` file.

---
### IMPORT orders
---

Import a CSV file which contains all the order information.

* **URL**

`/import/`

* **Method:**

`POST`

*  **URL Params**

**Required:**

 `*None*`

**Optional:**

 `*None*`

* **Success Response:**

* **Code:** 200 <br />

* **Content:**
  
  ```json
  {
    "Status": "Ok"
  }
  ``` 

* **Error Response:**

* **Content:**

  ```json
    {
    "Error": "<err message>"
  }
  ``` 


---
### GET Orders
---

Returns the list of all orders for Acme wines. Optionally, filter only the list of valid and invalid orders by specifying in the URL params.

* **URL**

  `/orders`

* **Method:**
  
  `GET`
  
*  **URL Params**

   **Required:**
 
     `*None*`

   **Optional:**
 
     `*valid*`

* **Success Response:**

  * **Code:** 200 <br />


---
### GET Order id
---

Returns the order information for a specific order ID.

* **URL**

`/catalog/<order_id>/`

* **Method:**

`GET`

*  **URL Params**

**Required:**

 `*None*`
 

**Optional:**

 `*None*`

* **Success Response:**

* **Code:** 200 <br />

* **Error Response:**

* **Content:**

  ```json
  	{
		"Error": "Invalid Order ID"
	}
  ``` 






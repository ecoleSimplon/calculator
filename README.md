# Calculator Api !

Calculator api is a RESTful Api to make simple operations : addition, subtraction, multiplication, division between two numbers.


# Install and Deploy

**Install**
```sh
git clone git@github.com:ecoleSimplon/calculator.git
```
From root directory :
```sh
pip3 install -r requirements.txt
```
**Deploy locally**

From root directory :

```sh
docker build -t calculator-api .
```
```sh
docker run --name calculator-api-container -d -p 5000:5000 calculator-api
```
**Deploy Azure Web app**

Create .env on root directory
```sh
ASP_NAME=your_plan
RG_NAME=your_ressource_group
AZURE_WEB_APP_NAME=your_unique_web_app_name
SKU=your_sku
SCM_DO_BUILD_DURING_DEPLOYMENT=true_for_build
```
```sh
chmod +x webAppUpdate.sh
```
```sh
./webAppUpdate.sh deploy
```
**Destroy Web App Ressources**
```sh
./webAppUpdate.sh destroy
```

## Tests

From root directory :

```sh
python3 tests/api_responses.py http://localhost:5000
```

## Routes

 - Addition :
 ```sh
 http://localhost:5000/addition
 ```
 - Subtraction :
  ```sh
 http://localhost:5000/subtraction
 ```
 - Multiplication :
  ```sh
 http://localhost:5000/multiplication
 ```
 - Division :
  ```sh
 http://localhost:5000/division
 ```


## Exemple of use

```sh
http://localhost:5000/addition?a=1&b=2
```

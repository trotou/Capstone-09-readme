# Getting Started with Capstone

## Getting Started

### Building

You must have Python `3 >=3.6, <= 3.9` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. These dependencies are defined in the `requirements.txt` file that comes with the SDK.To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type `pip --version`. This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including `requirements.txt`) for the SDK.
* Run the command `pip install -r requirements.txt`. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Capstone-Python&step=installDependencies)

### Installation

The following section explains how to use the capstone library in a new project.

#### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Capstone-Python&step=pyCharm)

Click on `Open` in PyCharm to browse to your generated SDK directory and then click `OK`.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Capstone-Python&step=openProject0)

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Capstone-Python&projectName=capstone&step=openProject1)

#### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Capstone-Python&projectName=capstone&step=createDirectory)

Name the directory as "test".

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Capstone-Python&step=nameDirectory)

Add a python file to this project.

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Capstone-Python&projectName=capstone&step=createFile)

Name it "testSDK".

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?workspaceFolder=Capstone-Python&projectName=capstone&step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```python
from capstone.capstone_client import CapstoneClient
```

![Add a new project in PyCharm - Step 5](https://apidocs.io/illustration/python?workspaceFolder=Capstone-Python&projectName=capstone&libraryName=capstone.capstone_client&className=CapstoneClient&step=projectFiles)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

#### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on `Run`

![Run Test Project - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Capstone-Python&projectName=capstone&libraryName=capstone.capstone_client&className=CapstoneClient&step=runProject)

### Initialize the API Client

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `access_token` | `string` | The OAuth 2.0 Access Token to use for API requests. |
| `environment` | Environment | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |

The API client can be initialized as follows:

```python
from capstone.capstone_client import CapstoneClient
from capstone.configuration import Environment

client = CapstoneClient(
    access_token='AccessToken',
    environment=Environment.PRODUCTION,)
```

### Authorization

This API uses `OAuth 2 Bearer token`.

## Client Class Documentation

### Capstone Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

### Controllers

| Name | Description |
|  --- | --- |
| login | Gets LoginController |
| usuarios | Gets UsuariosController |
| gerentes | Gets GerentesController |
| garcons | Gets GarconsController |
| operadores | Gets OperadoresController |
| fornecedores | Gets FornecedoresController |
| fornecedor_produto | Gets FornecedorProdutoController |
| forma_de_pagamento | Gets FormaDePagamentoController |
| mesas | Gets MesasController |
| contas | Gets ContasController |
| produtos | Gets ProdutosController |
| conta_produto | Gets ContaProdutoController |
| caixa | Gets CaixaController |
| operador_caixa | Gets OperadorCaixaController |
| ordens_de_compra | Gets OrdensDeCompraController |
| produtos_das_ordens_de_compra | Gets ProdutosDasOrdensDeCompraController |

## API Reference

### List of APIs

* [Login](#login)
* [Gerentes](#gerentes)
* [Garcons](#garcons)
* [Operadores](#operadores)
* [Fornecedores](#fornecedores)
* [Fornecedor Produto](#fornecedor-produto)
* [Forma De Pagamento](#forma-de-pagamento)
* [Mesas](#mesas)
* [Contas](#contas)
* [Produtos](#produtos)
* [Conta Produto](#conta-produto)
* [Caixa](#caixa)
* [Operador Caixa](#operador-caixa)
* [Ordens De Compra](#ordens-de-compra)
* [Produtos Das Ordens De Compra](#produtos-das-ordens-de-compra)
* [Usuarios](#usuarios)

### Login

#### Overview

##### Get instance

An instance of the `LoginController` class can be accessed from the API Client.

```
login_controller = client.login
```

#### Logar Com Usuário

Realiza o login do usuário na aplicação.

```python
def logar_com_usu_rio(self,
                     body,
                     content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LogarComUsuarioRequest`](#logar-com-usuario-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = LogarComUsuarioRequest()
body.username = 'john.doe'
body.password = '1234'
content_type = 'application/json'

result = login_controller.logar_com_usu_rio(body, content_type)
```

##### Example Response

```
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyNjg5NTY3MiwianRpIjoiZTczMjI1ODctYmFmNS00OTM3LTlkN2UtNmVjOTA1YWQ2ZmY1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6NiwidXNlcm5hbWUiOiJzaWx2aW8ucm9tYW5vIiwidHlwZSI6MSwicGFzc3dvcmRfaGFzaCI6InBia2RmMjpzaGEyNTY6MjYwMDAwJGxRNGVZOEhmOGI1VkdHeUYkZTJhOWVhNmNmZTMzNjJiYjk4ODM2ZjRmZGJjMDFiNWQ4ZTliNTM3MzRlNjQ1NTNhMDZjZDI1ZmEyMzg4MjA2MiJ9LCJuYmYiOjE2MjY4OTU2NzIsImV4cCI6MTYyNjg5NjU3Mn0.kKyo5TCM4DVxDIa52CKiiK077F5erl3t7pzAhyyw7GA"
}
```

### Gerentes

#### Overview

##### Get instance

An instance of the `GerentesController` class can be accessed from the API Client.

```
gerentes_controller = client.gerentes
```

#### Exibir Gerentes

Endpoint destinado à criação de gerente diretamente na tabela managers (gerentes). É utilizado de forma automatizada quando realizada a criação de usuário do tipo 1 (tabela users).

```python
def exibir_gerentes(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = gerentes_controller.exibir_gerentes()
```

##### Example Response

```
[
  {
    "id": 1,
    "name": "Matheus Ribeiro",
    "cpf": "98765432101",
    "id_user": 3
  },
  {
    "id": 6,
    "name": "trtrt",
    "cpf": "11122211133",
    "id_user": 15
  },
  {
    "id": 7,
    "name": "mano",
    "cpf": "22277799989",
    "id_user": 17
  },
  {
    "id": 8,
    "name": "john",
    "cpf": "00013211000",
    "id_user": 23
  },
  {
    "id": 3,
    "name": "Silvio Romano",
    "cpf": "98765432102",
    "id_user": 6
  },
  {
    "id": 4,
    "name": "Cosmonauta",
    "cpf": "00000000110",
    "id_user": 10
  }
]
```

#### Alterar Gerente

Realiza alteração de nome ou cpf do gerente selecionado por id, através de url params.

```python
def alterar_gerente(self,
                   body)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CriarGerenteRequest`](#criar-gerente-request) | Body, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = CriarGerenteRequest()
body.name = 'usuario_teste'
body.cpf = '00010011000'
body.id_user = 1

result = gerentes_controller.alterar_gerente(body)
```

##### Example Response

```
{
  "id": 6,
  "name": "Gilmar Turbano"
}
```

#### Remover Gerente

Remove o gerente selecionado por id, através de url params.

```python
def remover_gerente(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = gerentes_controller.remover_gerente()
```

### Garcons

#### Overview

##### Get instance

An instance of the `GarconsController` class can be accessed from the API Client.

```
garcons_controller = client.garcons
```

#### Exibir Garcons

Endpoint destinado à criação de garçom diretamente na tabela waiters (garçons). É utilizado de forma automatizada quando realizada a criação de usuário do tipo 2 (tabela users).

```python
def exibir_garcons(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = garcons_controller.exibir_garcons()
```

##### Example Response

```
[
  {
    "id": 1,
    "name": "Vinicius Alves",
    "cpf": "98765432101",
    "account_list": [
      {
        "id": 5,
        "date": "Mon, 20 Jul 2020 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 1,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 2,
        "date": "Thu, 15 Jul 2021 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 1,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          }
        ]
      },
      {
        "id": 3,
        "date": "Thu, 15 Jul 2021 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 1,
        "id_table": 2,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          }
        ]
      },
      {
        "id": 4,
        "date": "Thu, 15 Jul 2021 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 1,
        "id_table": 2,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 5,
            "name": "frango empanado",
            "description": "hmmmm",
            "price": 111.99,
            "stock": 40
          },
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          },
          {
            "id": 3,
            "name": "Fanta",
            "description": "",
            "price": 11.99,
            "stock": 100
          }
        ]
      },
      {
        "id": 38,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 1,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 39,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 1,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      }
    ]
  },
  {
    "id": 3,
    "name": "garcom",
    "cpf": "99977755512",
    "account_list": [
      {
        "id": 6,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 8,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 9,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 10,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 11,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 13,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 14,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 16,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 17,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 18,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 19,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 20,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          }
        ]
      },
      {
        "id": 7,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          },
          {
            "id": 5,
            "name": "frango empanado",
            "description": "hmmmm",
            "price": 111.99,
            "stock": 40
          },
          {
            "id": 3,
            "name": "Fanta",
            "description": "",
            "price": 11.99,
            "stock": 100
          }
        ]
      },
      {
        "id": 21,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 4,
            "name": "coxinha",
            "description": "hmmmm",
            "price": 1.99,
            "stock": 40
          },
          {
            "id": 3,
            "name": "Fanta",
            "description": "",
            "price": 11.99,
            "stock": 100
          },
          {
            "id": 5,
            "name": "frango empanado",
            "description": "hmmmm",
            "price": 111.99,
            "stock": 40
          }
        ]
      },
      {
        "id": 12,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          },
          {
            "id": 5,
            "name": "frango empanado",
            "description": "hmmmm",
            "price": 111.99,
            "stock": 40
          }
        ]
      },
      {
        "id": 15,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 4,
            "name": "coxinha",
            "description": "hmmmm",
            "price": 1.99,
            "stock": 40
          },
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          }
        ]
      },
      {
        "id": 22,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 4,
            "name": "coxinha",
            "description": "hmmmm",
            "price": 1.99,
            "stock": 40
          },
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          }
        ]
      },
      {
        "id": 23,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 4,
            "name": "coxinha",
            "description": "hmmmm",
            "price": 1.99,
            "stock": 40
          },
          {
            "id": 3,
            "name": "Fanta",
            "description": "",
            "price": 11.99,
            "stock": 100
          }
        ]
      },
      {
        "id": 24,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 4,
            "name": "coxinha",
            "description": "hmmmm",
            "price": 1.99,
            "stock": 40
          },
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          }
        ]
      },
      {
        "id": 25,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 5,
            "name": "frango empanado",
            "description": "hmmmm",
            "price": 111.99,
            "stock": 40
          },
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          }
        ]
      },
      {
        "id": 26,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          },
          {
            "id": 5,
            "name": "frango empanado",
            "description": "hmmmm",
            "price": 111.99,
            "stock": 40
          }
        ]
      },
      {
        "id": 40,
        "date": "Sun, 20 Jun 2021 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": "closed",
        "total_value": 0.0,
        "product_list": []
      },
      {
        "id": 41,
        "date": "Sun, 20 Jun 2021 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": "opened",
        "total_value": 0.0,
        "product_list": []
      }
    ]
  }
]
```

#### Alterar Garcom

Realiza alteração de nome ou cpf do garçom selecionado por id, através de url params.

```python
def alterar_garcom(self,
                  body,
                  content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AlterarGarcomRequest`](#alterar-garcom-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = AlterarGarcomRequest()
body.cpf = '12345678988'
content_type = 'application/json'

result = garcons_controller.alterar_garcom(body, content_type)
```

##### Example Response

```
{
  "id": 1,
  "name": "garcom-teste",
  "cpf": "98765432101",
  "account_list": [
    {
      "id": 5,
      "date": "Mon, 20 Jul 2020 00:00:00 GMT",
      "id_cashier": 1,
      "id_waiter": 1,
      "id_table": 1,
      "id_payment_method": 1,
      "status": null,
      "total_value": null,
      "product_list": []
    },
    {
      "id": 2,
      "date": "Thu, 15 Jul 2021 00:00:00 GMT",
      "id_cashier": 1,
      "id_waiter": 1,
      "id_table": 1,
      "id_payment_method": 1,
      "status": null,
      "total_value": null,
      "product_list": [
        {
          "id": 2,
          "name": "Coca Cola",
          "description": "",
          "price": 12.99,
          "stock": 70
        }
      ]
    },
    {
      "id": 3,
      "date": "Thu, 15 Jul 2021 00:00:00 GMT",
      "id_cashier": 1,
      "id_waiter": 1,
      "id_table": 2,
      "id_payment_method": 1,
      "status": null,
      "total_value": null,
      "product_list": [
        {
          "id": 2,
          "name": "Coca Cola",
          "description": "",
          "price": 12.99,
          "stock": 70
        }
      ]
    },
    {
      "id": 4,
      "date": "Thu, 15 Jul 2021 00:00:00 GMT",
      "id_cashier": 1,
      "id_waiter": 1,
      "id_table": 2,
      "id_payment_method": 1,
      "status": null,
      "total_value": null,
      "product_list": [
        {
          "id": 5,
          "name": "frango empanado",
          "description": "hmmmm",
          "price": 111.99,
          "stock": 40
        },
        {
          "id": 2,
          "name": "Coca Cola",
          "description": "",
          "price": 12.99,
          "stock": 70
        },
        {
          "id": 3,
          "name": "Fanta",
          "description": "",
          "price": 11.99,
          "stock": 100
        }
      ]
    },
    {
      "id": 38,
      "date": "Wed, 20 Jul 2022 00:00:00 GMT",
      "id_cashier": 1,
      "id_waiter": 1,
      "id_table": 1,
      "id_payment_method": 1,
      "status": null,
      "total_value": null,
      "product_list": []
    },
    {
      "id": 39,
      "date": "Wed, 20 Jul 2022 00:00:00 GMT",
      "id_cashier": 1,
      "id_waiter": 1,
      "id_table": 1,
      "id_payment_method": 1,
      "status": null,
      "total_value": null,
      "product_list": []
    }
  ]
}
```

#### Remover Garcom

Remove o garçom selecionado por id, através de url param

```python
def remover_garcom(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = garcons_controller.remover_garcom()
```

### Operadores

#### Overview

##### Get instance

An instance of the `OperadoresController` class can be accessed from the API Client.

```
operadores_controller = client.operadores
```

#### Exibir Operadores

Endpoint destinado à criação de operador diretamente na tabela operators (operadores). É utilizado de forma automatizada quando realizada a criação de usuário do tipo 3 (tabela users).

```python
def exibir_operadores(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = operadores_controller.exibir_operadores()
```

##### Example Response

```
[
  {
    "id": 1,
    "name": "Joilson dos Corre",
    "cpf": "12312312334",
    "cashier_list": [
      {
        "id": 1,
        "initial_value": 150.0,
        "balance": 259.8
      },
      {
        "id": 3,
        "initial_value": 350.0,
        "balance": 0.0
      }
    ]
  }
]
```

#### Alterar Operador

Realiza alteração de nome ou cpf do operador selecionado por id, através de url params.

```python
def alterar_operador(self,
                    body)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CriarOperadorRequest`](#criar-operador-request) | Body, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = CriarOperadorRequest()
body.name = 'usuario_teste'
body.cpf = '00010011000'
body.id_user = 1

result = operadores_controller.alterar_operador(body)
```

##### Example Response

```
{
  "id": 1,
  "name": "Joilson dos Corre",
  "cpf": "12312312334",
  "cashier_list": [
    {
      "id": 1,
      "initial_value": 150.0,
      "balance": 259.8
    },
    {
      "id": 3,
      "initial_value": 350.0,
      "balance": 0.0
    }
  ]
}
```

#### Remover Operador

Remove o operador selecionado por id, através de url params.

```python
def remover_operador(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = operadores_controller.remover_operador()
```

### Fornecedores

#### Overview

##### Get instance

An instance of the `FornecedoresController` class can be accessed from the API Client.

```
fornecedores_controller = client.fornecedores
```

#### Criar Fornecedor

Endpoint destinado à criação de fornecedor diretamente na tabela provider (fornecedor).

```python
def criar_fornecedor(self,
                    body,
                    content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CriarFornecedorRequest`](#criar-fornecedor-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = CriarFornecedorRequest()
body.trading_name = 'Distribuidora Portão SA'
body.cnpj = '1009889000016'
body.phone = '992422126'
content_type = 'application/json'

result = fornecedores_controller.criar_fornecedor(body, content_type)
```

##### Example Response

```
{
  "id": 5,
  "trading_name": "Distribuidora Portão SA",
  "cnpj": "1009889000016",
  "phone": "992422126",
  "product_list": []
}
```

#### Exibir Fornecedores

Exibe todos os fornecedores registrados.

```python
def exibir_fornecedores(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = fornecedores_controller.exibir_fornecedores()
```

##### Example Response

```
[
  {
    "id": 1,
    "trading_name": "latao SA",
    "cnpj": "1109889000013",
    "phone": "992422124",
    "product_list": [
      {
        "id": 4,
        "name": "coxinha",
        "description": "hmmmm",
        "price": 1.99,
        "stock": 40
      },
      {
        "id": 2,
        "name": "Coca Cola",
        "description": "",
        "price": 12.99,
        "stock": 70
      },
      {
        "id": 3,
        "name": "Fanta",
        "description": "",
        "price": 11.99,
        "stock": 100
      },
      {
        "id": 5,
        "name": "frango empanado",
        "description": "hmmmm",
        "price": 111.99,
        "stock": 40
      }
    ]
  },
  {
    "id": 5,
    "trading_name": "Distribuidora Portão SA",
    "cnpj": "1009889000016",
    "phone": "992422126",
    "product_list": []
  }
]
```

#### Alterar Fornecedor

Realiza alteração de nome do fornecedor, cnpj ou telefone selecionado por id, através de url params.

```python
def alterar_fornecedor(self,
                      body,
                      content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AlterarFornecedorRequest`](#alterar-fornecedor-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = AlterarFornecedorRequest()
body.cnpj = '1109889000013'
content_type = 'application/json'

result = fornecedores_controller.alterar_fornecedor(body, content_type)
```

##### Example Response

```
{
  "id": 1,
  "trading_name": "latao SA",
  "cnpj": "1109889000013",
  "phone": "992422124",
  "product_list": [
    {
      "id": 4,
      "name": "coxinha",
      "description": "hmmmm",
      "price": 1.99,
      "stock": 40
    },
    {
      "id": 2,
      "name": "Coca Cola",
      "description": "",
      "price": 12.99,
      "stock": 70
    },
    {
      "id": 3,
      "name": "Fanta",
      "description": "",
      "price": 11.99,
      "stock": 100
    },
    {
      "id": 5,
      "name": "frango empanado",
      "description": "hmmmm",
      "price": 111.99,
      "stock": 40
    }
  ]
}
```

#### Remover Fornecedor

Remove o fornecedor selecionado por id, através de url params.

```python
def remover_fornecedor(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = fornecedores_controller.remover_fornecedor()
```

### Fornecedor Produto

#### Overview

##### Get instance

An instance of the `FornecedorProdutoController` class can be accessed from the API Client.

```
fornecedor_produto_controller = client.fornecedor_produto
```

#### Criar Fornecedor Produto

Realiza a criação de chaves estrangeiras, id_provider e id_product, diretamente na tabela provider_product (fornecedor produto).

```python
def criar_fornecedor_produto(self,
                            body,
                            content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CriarFornecedorProdutoRequest`](#criar-fornecedor-produto-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = CriarFornecedorProdutoRequest()
body.id_product = 1
body.id_provider = 1
content_type = 'application/json'

result = fornecedor_produto_controller.criar_fornecedor_produto(body, content_type)
```

##### Example Response

```
{
  "id": 1,
  "id_product": 2,
  "id_provider": 1
}
```

#### Exibir Fornecedores

Exibe todos os elos entre as tabelas "provider" e "product" registrados.

```python
def exibir_fornecedores(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = fornecedor_produto_controller.exibir_fornecedores()
```

##### Example Response

```
[
  {
    "id": 3,
    "id_product": 2,
    "id_provider": 1
  },
  {
    "id": 4,
    "id_product": 3,
    "id_provider": 1
  },
  {
    "id": 5,
    "id_product": 5,
    "id_provider": 1
  },
  {
    "id": 1,
    "id_product": 2,
    "id_provider": 1
  }
]
```

#### Alterar Fornecedor

Realiza alteração do id_product (id do produto) ou do id_provider (id do fornecedor) selecionado por id único, através de url params.

```python
def alterar_fornecedor(self,
                      body,
                      content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AlterarFornecedorRequest1`](#alterar-fornecedor-request-1) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = AlterarFornecedorRequest1()
body.id_product = 2
content_type = 'application/json'

result = fornecedor_produto_controller.alterar_fornecedor(body, content_type)
```

##### Example Response

```
{
  "id": 1,
  "id_product": 2,
  "id_provider": 1
}
```

#### Remover Fornecedor

Remove o elo selecionado por id, através de url params.

```python
def remover_fornecedor(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = fornecedor_produto_controller.remover_fornecedor()
```

### Forma De Pagamento

#### Overview

##### Get instance

An instance of the `FormaDePagamentoController` class can be accessed from the API Client.

```
forma_de_pagamento_controller = client.forma_de_pagamento
```

#### Criar Forma De Pagamento

Realiza a criação de forma de pagamento diretamente na tabela payment_method (forma de pagamento).

```python
def criar_forma_de_pagamento(self,
                            body,
                            content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CriarFormaDePagamentoRequest`](#criar-forma-de-pagamento-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = CriarFormaDePagamentoRequest()
body.name = 'bitcoin'
body.description = 'criptomoeda'
content_type = 'application/json'

result = forma_de_pagamento_controller.criar_forma_de_pagamento(body, content_type)
```

##### Example Response

```
{
  "id": 4,
  "name": "bitcoin",
  "description": "criptomoeda",
  "account_list": []
}
```

#### Exibir Formas De Pagamento

Exibe todas as formas de pagamento registradas e os respectivos produtos pagos por meio da determinada forma.

```python
def exibir_formas_de_pagamento(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = forma_de_pagamento_controller.exibir_formas_de_pagamento()
```

##### Example Response

```
[
  {
    "id": 1,
    "name": "Dinheiro",
    "description": "",
    "account_list": [
      {
        "id": 5,
        "date": "Mon, 20 Jul 2020 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 1,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 2,
        "date": "Thu, 15 Jul 2021 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 1,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          }
        ]
      },
      {
        "id": 3,
        "date": "Thu, 15 Jul 2021 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 1,
        "id_table": 2,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          }
        ]
      },
      {
        "id": 4,
        "date": "Thu, 15 Jul 2021 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 1,
        "id_table": 2,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 5,
            "name": "frango empanado",
            "description": "hmmmm",
            "price": 111.99,
            "stock": 40
          },
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          },
          {
            "id": 3,
            "name": "Fanta",
            "description": "",
            "price": 11.99,
            "stock": 100
          }
        ]
      },
      {
        "id": 6,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 8,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 9,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 10,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 11,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 13,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 14,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 16,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 17,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 18,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 19,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 20,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          }
        ]
      },
      {
        "id": 7,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          },
          {
            "id": 5,
            "name": "frango empanado",
            "description": "hmmmm",
            "price": 111.99,
            "stock": 40
          },
          {
            "id": 3,
            "name": "Fanta",
            "description": "",
            "price": 11.99,
            "stock": 100
          }
        ]
      },
      {
        "id": 21,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 4,
            "name": "coxinha",
            "description": "hmmmm",
            "price": 1.99,
            "stock": 40
          },
          {
            "id": 3,
            "name": "Fanta",
            "description": "",
            "price": 11.99,
            "stock": 100
          },
          {
            "id": 5,
            "name": "frango empanado",
            "description": "hmmmm",
            "price": 111.99,
            "stock": 40
          }
        ]
      },
      {
        "id": 12,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          },
          {
            "id": 5,
            "name": "frango empanado",
            "description": "hmmmm",
            "price": 111.99,
            "stock": 40
          }
        ]
      },
      {
        "id": 15,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 4,
            "name": "coxinha",
            "description": "hmmmm",
            "price": 1.99,
            "stock": 40
          },
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          }
        ]
      },
      {
        "id": 22,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 4,
            "name": "coxinha",
            "description": "hmmmm",
            "price": 1.99,
            "stock": 40
          },
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          }
        ]
      },
      {
        "id": 23,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 4,
            "name": "coxinha",
            "description": "hmmmm",
            "price": 1.99,
            "stock": 40
          },
          {
            "id": 3,
            "name": "Fanta",
            "description": "",
            "price": 11.99,
            "stock": 100
          }
        ]
      },
      {
        "id": 24,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 4,
            "name": "coxinha",
            "description": "hmmmm",
            "price": 1.99,
            "stock": 40
          },
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          }
        ]
      },
      {
        "id": 25,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 5,
            "name": "frango empanado",
            "description": "hmmmm",
            "price": 111.99,
            "stock": 40
          },
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          }
        ]
      },
      {
        "id": 26,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": [
          {
            "id": 2,
            "name": "Coca Cola",
            "description": "",
            "price": 12.99,
            "stock": 70
          },
          {
            "id": 5,
            "name": "frango empanado",
            "description": "hmmmm",
            "price": 111.99,
            "stock": 40
          }
        ]
      },
      {
        "id": 38,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 1,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 39,
        "date": "Wed, 20 Jul 2022 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 1,
        "id_table": 1,
        "id_payment_method": 1,
        "status": null,
        "total_value": null,
        "product_list": []
      },
      {
        "id": 40,
        "date": "Sun, 20 Jun 2021 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": "closed",
        "total_value": 0.0,
        "product_list": []
      },
      {
        "id": 41,
        "date": "Sun, 20 Jun 2021 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 3,
        "id_table": 1,
        "id_payment_method": 1,
        "status": "opened",
        "total_value": 0.0,
        "product_list": []
      },
      {
        "id": 42,
        "date": "Wed, 21 Jul 2021 00:00:00 GMT",
        "id_cashier": 1,
        "id_waiter": 1,
        "id_table": 1,
        "id_payment_method": 1,
        "status": "opened",
        "total_value": 0.0,
        "product_list": []
      }
    ]
  },
  {
    "id": 3,
    "name": "Propina",
    "description": "",
    "account_list": []
  },
  {
    "id": 2,
    "name": "Cartão de Crédito",
    "description": "Cartao de Credito",
    "account_list": []
  },
  {
    "id": 4,
    "name": "bitcoin",
    "description": "criptomoeda",
    "account_list": []
  }
]
```

#### Alterar Forma De Pagamento

Realiza alteração do nome ou descrição da forma de pagamento selecionado por id, através de url params.

```python
def alterar_forma_de_pagamento(self,
                              body,
                              content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AlterarFormaDePagamentoRequest`](#alterar-forma-de-pagamento-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = AlterarFormaDePagamentoRequest()
body.description = 'Dinheiro'
content_type = 'application/json'

result = forma_de_pagamento_controller.alterar_forma_de_pagamento(body, content_type)
```

##### Example Response

```
{
  "id": 2,
  "name": "Cartão de Crédito",
  "description": "Cartao de Credito",
  "account_list": []
}
```

#### Remover Forma De Pagamento

Remove a forma de pagamento selecionada por id, através de url params.

```python
def remover_forma_de_pagamento(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = forma_de_pagamento_controller.remover_forma_de_pagamento()
```

### Mesas

#### Overview

##### Get instance

An instance of the `MesasController` class can be accessed from the API Client.

```
mesas_controller = client.mesas
```

#### Criar Mesa

Cria uma nova mesa a partir da informação enviada no json.

```python
def criar_mesa(self,
              body,
              content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CriarMesaRequest`](#criar-mesa-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = CriarMesaRequest()
body.number = '1'
content_type = 'application/json'

result = mesas_controller.criar_mesa(body, content_type)
```

##### Example Response

```
{
  "id": 1,
  "number": 1,
  "account_list": []
}
```

#### Exibir Mesa

Retorna um array com as mesas cadastradas. É possível utilizar query params para busca por id da mesa. (ex: /table?id=1).

```python
def exibir_mesa(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = mesas_controller.exibir_mesa()
```

##### Example Response

```
[
  {
    "id": 1,
    "number": 1,
    "account_list": []
  },
  {
    "id": 2,
    "number": 2,
    "account_list": []
  }
]
```

#### Alterar Mesa

Realiza alterações nos registros da mesa a partir do json recebido. É necessário informar o id por url params (ex: /table/1).

```python
def alterar_mesa(self,
                body,
                content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AlterarMesaRequest`](#alterar-mesa-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = AlterarMesaRequest()
body.description = 'Dinheiro'
content_type = 'application/json'

result = mesas_controller.alterar_mesa(body, content_type)
```

##### Example Response

```
{
  "id": 1,
  "number": 10,
  "account_list": []
}
```

#### Remover Mesa

Realiza a deleção do registro de uma mesa a partir do id passado por url params (ex: /table/1).

```python
def remover_mesa(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = mesas_controller.remover_mesa()
```

### Contas

#### Overview

##### Get instance

An instance of the `ContasController` class can be accessed from the API Client.

```
contas_controller = client.contas
```

#### Criar Conta

Realiza a criação de uma nova mesa a partir do json recebido. Para isso é necessário que existam caixas, garçons, mesas e métodos de pagamento criados anteriormente para realizar a vinculação por chave estrangeira.
Por padrão todas as contas são criadas no padrão "opened".

```python
def criar_conta(self,
               body,
               content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CriarContaRequest`](#criar-conta-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = CriarContaRequest()
body.date = '07/21/2021'
body.id_cashier = 1
body.id_waiter = 1
body.id_table = 1
body.id_payment_method = 1
content_type = 'application/json'

result = contas_controller.criar_conta(body, content_type)
```

##### Example Response

```
{
  "id": 1,
  "date": "Wed, 21 Jul 2021 00:00:00 GMT",
  "id_cashier": 1,
  "waiter": "garcom-teste",
  "id_table": 1,
  "payment_method": "Dinheiro",
  "status": "opened",
  "total_value": 0,
  "product_list": []
}
```

#### Exibir Conta

Retorna as contas registradas. É possível realizar consultas através de query params (ex: /account?id=1).

```python
def exibir_conta(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = contas_controller.exibir_conta()
```

##### Example Response

```
[
  {
    "id": 1,
    "date": "Mon, 20 Jul 2020 00:00:00 GMT",
    "id_cashier": 1,
    "waiter": "garcom-teste",
    "id_table": 1,
    "payment_method": "Dinheiro",
    "status": "opened",
    "total_value": 90.0,
    "product_list": []
  },
  {
    "id": 2,
    "date": "Mon, 21 Jul 2020 00:00:00 GMT",
    "id_cashier": 1,
    "waiter": "garcom-teste",
    "id_table": 1,
    "payment_method": "Dinheiro",
    "status": "opened",
    "total_value": 50.0,
    "product_list": []
  }
]
```

#### Encerrar Conta

Converte o status da conta de "opened" para "closed". Funciona ao passar o id da conta por query params (ex: /account/1/close_account).

```python
def encerrar_conta(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = contas_controller.encerrar_conta()
```

#### Alterar Conta

Realiza alteração do id_cashier (id do caixa), id_waiter (id do garçom), id_table (id da mesa) e do id_payment_method (método de pagamento) selecionado por id único, através de url params.

```python
def alterar_conta(self,
                 body,
                 content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AlterarContaRequest`](#alterar-conta-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = AlterarContaRequest()
body.id_mesa = 2
content_type = 'application/json'

result = contas_controller.alterar_conta(body, content_type)
```

#### Remover Mesa

Remove a conta selecionada por id, através de url params.

```python
def remover_mesa(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = contas_controller.remover_mesa()
```

### Produtos

#### Overview

##### Get instance

An instance of the `ProdutosController` class can be accessed from the API Client.

```
produtos_controller = client.produtos
```

#### Criar Produto

Realiza a criação de um produto diretamente na tabela products (produtos).

```python
def criar_produto(self,
                 body,
                 content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CriarProdutoRequest`](#criar-produto-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = CriarProdutoRequest()
body.name = 'quindim'
body.description = 'doce caseiro'
body.price = 4
content_type = 'application/json'

result = produtos_controller.criar_produto(body, content_type)
```

##### Example Response

```
{
  "id": 7,
  "name": "quindim",
  "description": "doce caseiro",
  "price": 4.0,
  "stock": 0
}
```

#### Exibir Produto

Exibe todos os produtos registrados.

```python
def exibir_produto(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = produtos_controller.exibir_produto()
```

##### Example Response

```
[
  {
    "id": 3,
    "name": "Fanta",
    "description": "",
    "price": 11.99,
    "stock": 100
  },
  {
    "id": 4,
    "name": "coxinha",
    "description": "hmmmm",
    "price": 1.99,
    "stock": 40
  },
  {
    "id": 2,
    "name": "Coca Cola",
    "description": "",
    "price": 12.99,
    "stock": 70
  },
  {
    "id": 5,
    "name": "frango empanado",
    "description": "hmmmm",
    "price": 111.99,
    "stock": 40
  },
  {
    "id": 7,
    "name": "quindim",
    "description": "doce caseiro",
    "price": 4.0,
    "stock": 0
  }
]
```

#### Alterar Produto

Realiza alteração de nome, descrição, preço e quantidade em stock selecionado por id, através de url params.

```python
def alterar_produto(self,
                   body,
                   content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AlterarProdutoRequest`](#alterar-produto-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = AlterarProdutoRequest()
body.description = 'produto perecível'
content_type = 'application/json'

result = produtos_controller.alterar_produto(body, content_type)
```

##### Example Response

```
{
  "id": 2,
  "name": "Coca Cola",
  "description": "produto meramente gostosinho",
  "price": 12.99,
  "stock": 70
}
```

#### Remover Produto

Remove o produto selecionado por id, através de url params.

```python
def remover_produto(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = produtos_controller.remover_produto()
```

### Conta Produto

#### Overview

##### Get instance

An instance of the `ContaProdutoController` class can be accessed from the API Client.

```
conta_produto_controller = client.conta_produto
```

#### Criar Conta Produto

Realiza a criação de chaves estrangeiras (id_account e id_product) e da quantidade de produtos registrados na determinada conta, diretamente na tabela account_product (conta produto).

```python
def criar_conta_produto(self,
                       body,
                       content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CriarContaProdutoRequest`](#criar-conta-produto-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = CriarContaProdutoRequest()
body.id_account = '42'
body.id_product = '2'
body.quantity = 4
content_type = 'application/json'

result = conta_produto_controller.criar_conta_produto(body, content_type)
```

##### Example Response

```
{
  "id": 28,
  "id_account": 42,
  "id_product": 2,
  "quantity": 4
}
```

#### Exibir Conta Produto

Exibe todos os elos entre as tabelas "account" e "product" registrados.

```python
def exibir_conta_produto(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = conta_produto_controller.exibir_conta_produto()
```

##### Example Response

```
[
  {
    "id": 2,
    "id_account": 3,
    "id_product": 2,
    "quantity": 20
  },
  {
    "id": 3,
    "id_account": 4,
    "id_product": 5,
    "quantity": 1
  },
  {
    "id": 4,
    "id_account": 20,
    "id_product": 2,
    "quantity": 1
  },
  {
    "id": 5,
    "id_account": 4,
    "id_product": 5,
    "quantity": 1
  },
  {
    "id": 6,
    "id_account": 4,
    "id_product": 2,
    "quantity": 2
  },
  {
    "id": 7,
    "id_account": 4,
    "id_product": 3,
    "quantity": 1
  },
  {
    "id": 8,
    "id_account": 7,
    "id_product": 2,
    "quantity": 2
  },
  {
    "id": 9,
    "id_account": 7,
    "id_product": 5,
    "quantity": 1
  },
  {
    "id": 10,
    "id_account": 7,
    "id_product": 3,
    "quantity": 1
  },
  {
    "id": 11,
    "id_account": 21,
    "id_product": 4,
    "quantity": 2
  },
  {
    "id": 12,
    "id_account": 21,
    "id_product": 3,
    "quantity": 1
  },
  {
    "id": 13,
    "id_account": 21,
    "id_product": 5,
    "quantity": 1
  },
  {
    "id": 14,
    "id_account": 12,
    "id_product": 2,
    "quantity": 2
  },
  {
    "id": 15,
    "id_account": 12,
    "id_product": 5,
    "quantity": 1
  },
  {
    "id": 16,
    "id_account": 15,
    "id_product": 4,
    "quantity": 1
  },
  {
    "id": 17,
    "id_account": 15,
    "id_product": 2,
    "quantity": 1
  },
  {
    "id": 18,
    "id_account": 22,
    "id_product": 4,
    "quantity": 1
  },
  {
    "id": 19,
    "id_account": 22,
    "id_product": 2,
    "quantity": 1
  },
  {
    "id": 20,
    "id_account": 23,
    "id_product": 4,
    "quantity": 1
  },
  {
    "id": 21,
    "id_account": 23,
    "id_product": 3,
    "quantity": 1
  },
  {
    "id": 22,
    "id_account": 24,
    "id_product": 4,
    "quantity": 1
  },
  {
    "id": 23,
    "id_account": 24,
    "id_product": 2,
    "quantity": 1
  },
  {
    "id": 24,
    "id_account": 25,
    "id_product": 5,
    "quantity": 1
  },
  {
    "id": 25,
    "id_account": 25,
    "id_product": 2,
    "quantity": 1
  },
  {
    "id": 26,
    "id_account": 26,
    "id_product": 2,
    "quantity": 1
  },
  {
    "id": 27,
    "id_account": 26,
    "id_product": 5,
    "quantity": 1
  },
  {
    "id": 1,
    "id_account": 6,
    "id_product": 2,
    "quantity": 10
  },
  {
    "id": 28,
    "id_account": 42,
    "id_product": 2,
    "quantity": 4
  }
]
```

#### Alterar Conta Produto

Realiza alteração das chaves estrangeiras (id_account, id_product) e da quantidade de produtos adicionados à conta, selecionados por id, através de url params.

```python
def alterar_conta_produto(self,
                         body,
                         content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AlterarContaProdutoRequest`](#alterar-conta-produto-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = AlterarContaProdutoRequest()
body.id_account = 6
content_type = 'application/json'

result = conta_produto_controller.alterar_conta_produto(body, content_type)
```

##### Example Response

```
{
  "id": 1,
  "id_account": 6,
  "id_product": 2,
  "quantity": 10
}
```

#### Remover Conta Produto

Remove o elo selecionado por id, através de url params.

```python
def remover_conta_produto(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = conta_produto_controller.remover_conta_produto()
```

### Caixa

#### Overview

##### Get instance

An instance of the `CaixaController` class can be accessed from the API Client.

```
caixa_controller = client.caixa
```

#### Criar Caixa

Cria um novo Caixa

```python
def criar_caixa(self,
               body,
               content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CriarCaixaRequest`](#criar-caixa-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = CriarCaixaRequest()
body.initial_value = 15
body.balance = 0
content_type = 'application/json'

result = caixa_controller.criar_caixa(body, content_type)
```

##### Example Response

```
{
  "id": 4,
  "initial_value": 15.0,
  "balance": 0.0
}
```

#### Exibir Caixa

Retorna todos os caixas existentes

```python
def exibir_caixa(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = caixa_controller.exibir_caixa()
```

##### Example Response

```
[
  {
    "id": 2,
    "initial_value": 150.0,
    "balance": 0.0
  },
  {
    "id": 4,
    "initial_value": 15.0,
    "balance": 0.0
  },
  {
    "id": 1,
    "initial_value": 150.0,
    "balance": 259.8
  },
  {
    "id": 3,
    "initial_value": 350.0,
    "balance": 0.0
  }
]
```

#### Alterar Caixa

Altera valores do caixa

```python
def alterar_caixa(self,
                 body,
                 content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AlterarCaixaRequest`](#alterar-caixa-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = AlterarCaixaRequest()
body.balance = 50
content_type = 'application/json'

result = caixa_controller.alterar_caixa(body, content_type)
```

##### Example Response

```
{
  "id": 1,
  "initial_value": 150.0,
  "balance": 520.0
}
```

#### Remover Caixa

Deleta o caixa selecionado por Id

```python
def remover_caixa(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = caixa_controller.remover_caixa()
```

### Operador Caixa

#### Overview

##### Get instance

An instance of the `OperadorCaixaController` class can be accessed from the API Client.

```
operador_caixa_controller = client.operador_caixa
```

#### Criar Operador Caixa

Realiza a criação de chaves estrangeiras, id_operator e id_cashier, diretamente na tabela operator_cashier (operador caixa).

```python
def criar_operador_caixa(self,
                        body,
                        content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CriarOperadorCaixaRequest`](#criar-operador-caixa-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = CriarOperadorCaixaRequest()
body.id_operator = 1
body.id_cashier = 1
content_type = 'application/json'

result = operador_caixa_controller.criar_operador_caixa(body, content_type)
```

#### Exibir Operador Caixa

Exibe todos os operadores de caixa

```python
def exibir_operador_caixa(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = operador_caixa_controller.exibir_operador_caixa()
```

##### Example Response

```
[
  {
    "id": 1,
    "id_operator": 1,
    "id_cashier": 1
  },
  {
    "id": 2,
    "id_operator": 1,
    "id_cashier": 3
  }
]
```

#### Alterar Operador Caixa

Altera relação de caixa para operadores

```python
def alterar_operador_caixa(self,
                          body,
                          content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AlterarOperadorCaixaRequest`](#alterar-operador-caixa-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = AlterarOperadorCaixaRequest()
body.id_operator = 2
content_type = 'application/json'

result = operador_caixa_controller.alterar_operador_caixa(body, content_type)
```

##### Example Response

```
{
  "id": 1,
  "id_operator": 1,
  "id_cashier": 1
}
```

#### Remover Operador Caixa

Deleta relação caixa e operador

```python
def remover_operador_caixa(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = operador_caixa_controller.remover_operador_caixa()
```

### Ordens De Compra

#### Overview

##### Get instance

An instance of the `OrdensDeCompraController` class can be accessed from the API Client.

```
ordens_de_compra_controller = client.ordens_de_compra
```

#### Criar Ordem De Compra

Cria uma ordem de compra

```python
def criar_ordem_de_compra(self,
                         body,
                         content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CriarOrdemDeCompraRequest`](#criar-ordem-de-compra-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = CriarOrdemDeCompraRequest()
body.id_manager = 1
body.id_provider = 1
body.date = '01/27/2022'
content_type = 'application/json'

result = ordens_de_compra_controller.criar_ordem_de_compra(body, content_type)
```

##### Example Response

```
{
  "id": 4,
  "id_manager": 1,
  "id_provider": 1,
  "date": "Wed, 20 Jul 2022 00:00:00 GMT",
  "is_finished": false,
  "total_value": 0.0,
  "products_list": []
}
```

#### Exibir Ordem De Compra

Exibe todas as ordens de compra

```python
def exibir_ordem_de_compra(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = ordens_de_compra_controller.exibir_ordem_de_compra()
```

##### Example Response

```
[
  {
    "id": 1,
    "id_manager": 1,
    "id_provider": 1,
    "date": "Mon, 07 Nov 2022 00:00:00 GMT",
    "is_finished": true,
    "total_value": 0.0,
    "products_list": []
  },
  {
    "id": 3,
    "id_manager": 1,
    "id_provider": 1,
    "date": "Tue, 17 May 2022 00:00:00 GMT",
    "is_finished": true,
    "total_value": 0.0,
    "products_list": []
  }
]
```

#### Alterar Ordem De Compra

Altera dados da ordem de compra selecionada por Id

```python
def alterar_ordem_de_compra(self,
                           body,
                           content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AlterarOrdemDeCompraRequest`](#alterar-ordem-de-compra-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = AlterarOrdemDeCompraRequest()
body.date = '10/07/2022'
content_type = 'application/json'

result = ordens_de_compra_controller.alterar_ordem_de_compra(body, content_type)
```

##### Example Response

```
{
  "id": 4,
  "id_manager": 1,
  "id_provider": 1,
  "date": "Fri, 07 Oct 2022 00:00:00 GMT",
  "is_finished": false,
  "total_value": 0.0,
  "products_list": []
}
```

#### Remover Ordem De Compra

Remove ordem de compra selecionada por Id

```python
def remover_ordem_de_compra(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = ordens_de_compra_controller.remover_ordem_de_compra()
```

### Produtos Das Ordens De Compra

#### Overview

##### Get instance

An instance of the `ProdutosDasOrdensDeCompraController` class can be accessed from the API Client.

```
produtos_das_ordens_de_compra_controller = client.produtos_das_ordens_de_compra
```

#### Criar Produto Ordem De Compra

Cria a relação entre produtos e ordens de compra

```python
def criar_produto_ordem_de_compra(self,
                                 body,
                                 content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CriarProdutoOrdemDeCompraRequest`](#criar-produto-ordem-de-compra-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = CriarProdutoOrdemDeCompraRequest()
body.id_order = 1
body.id_product = 1
body.quantity = 1
body.cost = 2.5
content_type = 'application/json'

result = produtos_das_ordens_de_compra_controller.criar_produto_ordem_de_compra(body, content_type)
```

##### Example Response

```
{
  "id": 1,
  "id_order": 5,
  "id_product": 5,
  "quantity": 10,
  "cost": 2
}
```

#### Exibir Produto Ordem De Compra

```python
def exibir_produto_ordem_de_compra(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = produtos_das_ordens_de_compra_controller.exibir_produto_ordem_de_compra()
```

##### Example Response

```
[
  {
    "id": 1,
    "id_order": 5,
    "id_product": 5,
    "quantity": 10,
    "cost": 2.0
  }
]
```

#### Alterar Produto Ordem De Compra

Altera dados dos produtos ordens de compra

```python
def alterar_produto_ordem_de_compra(self,
                                   body,
                                   content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AlterarProdutoOrdemDeCompraRequest`](#alterar-produto-ordem-de-compra-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = AlterarProdutoOrdemDeCompraRequest()
body.cost = 3
content_type = 'application/json'

result = produtos_das_ordens_de_compra_controller.alterar_produto_ordem_de_compra(body, content_type)
```

##### Example Response

```
{
  "id": 1,
  "id_order": 5,
  "id_product": 5,
  "quantity": 10,
  "cost": 3.0
}
```

#### Remover Produto Ordem De Compra

Deleta a relação Produto ordem de compra por Id

```python
def remover_produto_ordem_de_compra(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = produtos_das_ordens_de_compra_controller.remover_produto_ordem_de_compra()
```

### Usuarios

#### Overview

##### Get instance

An instance of the `UsuariosController` class can be accessed from the API Client.

```
usuarios_controller = client.usuarios
```

#### Criar Usuario

Realiza a criação do usuário de todos os tipos:
1 - Gerente
2 - Garçom
3 - Operador de caixa

```python
def criar_usuario(self,
                 body,
                 content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CriarUsuarioRequest`](#criar-usuario-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = CriarUsuarioRequest()
body.username = 'Trump'
body.mtype = 1
body.password = '1234'
body.name = 'Trump'
body.cpf = '00010011000'
content_type = 'application/json'

result = usuarios_controller.criar_usuario(body, content_type)
```

##### Example Response

```
{
  "name": "john",
  "type": "Manager",
  "username": "john.doe",
  "cpf": "00013211000",
  "password": "pbkdf2:sha256:260000$HwqCyC3YWEAB2sev$edcdd7aaf6485a5a698452cb6bb877391d6fc09cdf4e41e6d3499cf8a33d5764"
}
```

#### Exibir Usuarios

Exibe todos os usuários registrados.

```python
def exibir_usuarios(self)
```

##### Response Type

`mixed`

##### Example Usage

```python
result = usuarios_controller.exibir_usuarios()
```

##### Example Response

```
[
  {
    "id": 1,
    "username": "vinicius.alves",
    "type": 2,
    "password_hash": "pbkdf2:sha256:260000$Idtyg2UavYLjWsXi$cd72db69fdf25390f72cead97086701f6a562eaa91d232aa3042afb1c07581a4"
  },
  {
    "id": 15,
    "username": "rtrtrtr",
    "type": 1,
    "password_hash": "pbkdf2:sha256:260000$U5ecsCZTwdVl7kjW$9e512a233fe9c88d59d20b7c4b268d8a8ab977f4e04a6587a643e7d7af036aa8"
  },
  {
    "id": 3,
    "username": "tico.rib",
    "type": 1,
    "password_hash": "pbkdf2:sha256:260000$xJm5qTIzNFJizT0l$aeecc70f1419966f9fbc86b340a08aa089458e4971b2c09801482389e0ea0463"
  },
  {
    "id": 16,
    "username": "testanto5",
    "type": 2,
    "password_hash": "pbkdf2:sha256:260000$Bbk4NOWLvfwnyq42$f96ca36bcfb0ccb7ec3aaf394e67e743cee82739dfbebafe7ab03fec5f8b60fb"
  },
  {
    "id": 17,
    "username": "manager",
    "type": 1,
    "password_hash": "pbkdf2:sha256:260000$nsvboVSb37BoqzGl$50f318bb9500b940b75e21f69b6645179a9a5bdf756502bea55e77d0d595dca3"
  },
  {
    "id": 5,
    "username": "joao",
    "type": 3,
    "password_hash": "pbkdf2:sha256:260000$EjDieYaqHWKS6lkB$246e0fc5a949aeb6e9dd1481f11bdfaa9bc5e58c88ecec9576c7315eb02046d7"
  },
  {
    "id": 6,
    "username": "silvio.romano",
    "type": 1,
    "password_hash": "pbkdf2:sha256:260000$lQ4eY8Hf8b5VGGyF$e2a9ea6cfe3362bb98836f4fdbc01b5d8e9b53734e64553a06cd25fa23882062"
  },
  {
    "id": 18,
    "username": "garcomtest",
    "type": 3,
    "password_hash": "pbkdf2:sha256:260000$uKFuxrnzOHvj40ZY$5f3b7427738144b52197da67b8cdbabbc544fc5f4b607c36f8ff6d7ce1609f24"
  },
  {
    "id": 10,
    "username": "Sputnick",
    "type": 1,
    "password_hash": "pbkdf2:sha256:260000$45GE0tfve0elMqSM$c29db45ff9f79f1bd0da734e0c760be38b182cb8bceecae6b273d34e68fdc6f3"
  },
  {
    "id": 12,
    "username": "Trump",
    "type": 1,
    "password_hash": "pbkdf2:sha256:260000$lCh9eVq2fjIwpFNR$5d5a803f13cc4927208a8946add03bfac295eeba56b1773e24ad6f18652c0b2a"
  },
  {
    "id": 23,
    "username": "john.doe",
    "type": 1,
    "password_hash": "pbkdf2:sha256:260000$HwqCyC3YWEAB2sev$edcdd7aaf6485a5a698452cb6bb877391d6fc09cdf4e41e6d3499cf8a33d5764"
  }
]
```

#### Alterar Usuario

Realiza alteração de nome ou tipo do usuário selecionado por id, através de url params.

```python
def alterar_usuario(self,
                   body,
                   content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AlterarUsuarioRequest`](#alterar-usuario-request) | Body, Required | - |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
body = AlterarUsuarioRequest()
body.mtype = '3'
content_type = 'application/json'

result = usuarios_controller.alterar_usuario(body, content_type)
```

##### Example Response

```
{
  "id": 18,
  "username": "garcomtest",
  "type": 2,
  "password_hash": "pbkdf2:sha256:260000$uKFuxrnzOHvj40ZY$5f3b7427738144b52197da67b8cdbabbc544fc5f4b607c36f8ff6d7ce1609f24"
}
```

#### Remover Usuario

Remove o usuário selecionado por id, através de url params.

```python
def remover_usuario(self,
                   content_type)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | `string` | Header, Required | - |

##### Response Type

`mixed`

##### Example Usage

```python
content_type = 'application/json'

result = usuarios_controller.remover_usuario(content_type)
```

## Model Reference

### Structures

* [Logar Com Usuario Request](#logar-com-usuario-request)
* [Criar Usuario Request](#criar-usuario-request)
* [Alterar Usuario Request](#alterar-usuario-request)
* [Criar Gerente Request](#criar-gerente-request)
* [Criar Garcom Request](#criar-garcom-request)
* [Alterar Garcom Request](#alterar-garcom-request)
* [Criar Operador Request](#criar-operador-request)
* [Criar Fornecedor Request](#criar-fornecedor-request)
* [Alterar Fornecedor Request](#alterar-fornecedor-request)
* [Criar Fornecedor Produto Request](#criar-fornecedor-produto-request)
* [Alterar Fornecedor Request 1](#alterar-fornecedor-request-1)
* [Criar Forma De Pagamento Request](#criar-forma-de-pagamento-request)
* [Alterar Forma De Pagamento Request](#alterar-forma-de-pagamento-request)
* [Criar Mesa Request](#criar-mesa-request)
* [Alterar Mesa Request](#alterar-mesa-request)
* [Criar Conta Request](#criar-conta-request)
* [Alterar Conta Request](#alterar-conta-request)
* [Criar Produto Request](#criar-produto-request)
* [Alterar Produto Request](#alterar-produto-request)
* [Criar Conta Produto Request](#criar-conta-produto-request)
* [Alterar Conta Produto Request](#alterar-conta-produto-request)
* [Criar Caixa Request](#criar-caixa-request)
* [Alterar Caixa Request](#alterar-caixa-request)
* [Criar Operador Caixa Request](#criar-operador-caixa-request)
* [Alterar Operador Caixa Request](#alterar-operador-caixa-request)
* [Criar Ordem De Compra Request](#criar-ordem-de-compra-request)
* [Alterar Ordem De Compra Request](#alterar-ordem-de-compra-request)
* [Criar Produto Ordem De Compra Request](#criar-produto-ordem-de-compra-request)
* [Alterar Produto Ordem De Compra Request](#alterar-produto-ordem-de-compra-request)

#### Logar Com Usuario Request

##### Class Name

`LogarComUsuarioRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `string` | Required | - |
| `password` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "username": "silvio.romano",
  "password": "1234"
}
```

#### Criar Usuario Request

##### Class Name

`CriarUsuarioRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `string` | Required | - |
| `mtype` | `int` | Required | - |
| `password` | `string` | Required | - |
| `name` | `string` | Required | - |
| `cpf` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "username": "Trump",
  "type": 1,
  "password": "1234",
  "name": "Trump",
  "cpf": "00010011000"
}
```

#### Alterar Usuario Request

##### Class Name

`AlterarUsuarioRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "type": "3"
}
```

#### Criar Gerente Request

##### Class Name

`CriarGerenteRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Required | - |
| `cpf` | `string` | Required | - |
| `id_user` | `int` | Required | - |

##### Example (as JSON)

```json
{
  "name": "usuario_teste",
  "cpf": "00010011000",
  "id_user": 1
}
```

#### Criar Garcom Request

##### Class Name

`CriarGarcomRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Required | - |
| `cpf` | `string` | Required | - |
| `id_user` | `int` | Required | - |

##### Example (as JSON)

```json
{
  "name": "usuario_teste",
  "cpf": "00010011000",
  "id_user": 1
}
```

#### Alterar Garcom Request

##### Class Name

`AlterarGarcomRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cpf` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "cpf": "12345678988"
}
```

#### Criar Operador Request

##### Class Name

`CriarOperadorRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Required | - |
| `cpf` | `string` | Required | - |
| `id_user` | `int` | Required | - |

##### Example (as JSON)

```json
{
  "name": "usuario_teste",
  "cpf": "00010011000",
  "id_user": 1
}
```

#### Criar Fornecedor Request

##### Class Name

`CriarFornecedorRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trading_name` | `string` | Required | - |
| `cnpj` | `string` | Required | - |
| `phone` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "trading_name": "Distribuidora Portão SA",
  "cnpj": "1009889000016",
  "phone": "992422126"
}
```

#### Alterar Fornecedor Request

##### Class Name

`AlterarFornecedorRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cnpj` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "cnpj": "1109889000013"
}
```

#### Criar Fornecedor Produto Request

##### Class Name

`CriarFornecedorProdutoRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id_product` | `int` | Required | - |
| `id_provider` | `int` | Required | - |

##### Example (as JSON)

```json
{
  "id_product": 1,
  "id_provider": 1
}
```

#### Alterar Fornecedor Request 1

##### Class Name

`AlterarFornecedorRequest1`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id_product` | `int` | Required | - |

##### Example (as JSON)

```json
{
  "id_product": 2
}
```

#### Criar Forma De Pagamento Request

##### Class Name

`CriarFormaDePagamentoRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Required | - |
| `description` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "name": "Dinheiro",
  "description": ""
}
```

#### Alterar Forma De Pagamento Request

##### Class Name

`AlterarFormaDePagamentoRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "description": "Dinheiro"
}
```

#### Criar Mesa Request

##### Class Name

`CriarMesaRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "number": "1"
}
```

#### Alterar Mesa Request

##### Class Name

`AlterarMesaRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "description": "Dinheiro"
}
```

#### Criar Conta Request

##### Class Name

`CriarContaRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date` | `string` | Required | - |
| `id_cashier` | `int` | Required | - |
| `id_waiter` | `int` | Required | - |
| `id_table` | `int` | Required | - |
| `id_payment_method` | `int` | Required | - |

##### Example (as JSON)

```json
{
  "date": "19/07/2021",
  "id_cashier": 1,
  "id_waiter": 1,
  "id_table": 1,
  "id_payment_method": 1
}
```

#### Alterar Conta Request

##### Class Name

`AlterarContaRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id_mesa` | `int` | Required | - |

##### Example (as JSON)

```json
{
  "id_mesa": 2
}
```

#### Criar Produto Request

##### Class Name

`CriarProdutoRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Required | - |
| `description` | `string` | Required | - |
| `price` | `int` | Required | - |

##### Example (as JSON)

```json
{
  "name": "Café espresso",
  "description": "",
  "price": 6
}
```

#### Alterar Produto Request

##### Class Name

`AlterarProdutoRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "description": "produto meramente gostosinho"
}
```

#### Criar Conta Produto Request

##### Class Name

`CriarContaProdutoRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id_account` | `string` | Required | - |
| `id_product` | `string` | Required | - |
| `quantity` | `int` | Required | - |

##### Example (as JSON)

```json
{
  "id_account": "5",
  "id_product": "1",
  "quantity": 4
}
```

#### Alterar Conta Produto Request

##### Class Name

`AlterarContaProdutoRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id_account` | `int` | Required | - |

##### Example (as JSON)

```json
{
  "id_account": 6
}
```

#### Criar Caixa Request

##### Class Name

`CriarCaixaRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `initial_value` | `int` | Required | - |
| `balance` | `int` | Required | - |

##### Example (as JSON)

```json
{
  "initial_value": 15,
  "balance": 0
}
```

#### Alterar Caixa Request

##### Class Name

`AlterarCaixaRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance` | `int` | Required | - |

##### Example (as JSON)

```json
{
  "balance": 50
}
```

#### Criar Operador Caixa Request

##### Class Name

`CriarOperadorCaixaRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id_operator` | `int` | Required | - |
| `id_cashier` | `int` | Required | - |

##### Example (as JSON)

```json
{
  "id_operator": 1,
  "id_cashier": 1
}
```

#### Alterar Operador Caixa Request

##### Class Name

`AlterarOperadorCaixaRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id_operator` | `int` | Required | - |

##### Example (as JSON)

```json
{
  "id_operator": 2
}
```

#### Criar Ordem De Compra Request

##### Class Name

`CriarOrdemDeCompraRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id_manager` | `int` | Required | - |
| `id_provider` | `int` | Required | - |
| `date` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "id_manager": 1,
  "id_provider": 1,
  "date": "19/07/2022"
}
```

#### Alterar Ordem De Compra Request

##### Class Name

`AlterarOrdemDeCompraRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "date": "10/07/2022"
}
```

#### Criar Produto Ordem De Compra Request

##### Class Name

`CriarProdutoOrdemDeCompraRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id_order` | `int` | Required | - |
| `id_product` | `int` | Required | - |
| `quantity` | `int` | Required | - |
| `cost` | `float` | Required | - |

##### Example (as JSON)

```json
{
  "id_order": 1,
  "id_product": 1,
  "quantity": 1,
  "cost": 2.5
}
```

#### Alterar Produto Ordem De Compra Request

##### Class Name

`AlterarProdutoOrdemDeCompraRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cost` | `int` | Required | - |

##### Example (as JSON)

```json
{
  "cost": 3
}
```

## Utility Classes Documentation

### ApiHelper

A utility class for processing API Calls. Also contains classes for supporting standard datetime formats.

#### Methods

| Name | Description |
|  --- | --- |
| json_deserialize | Deserializes a JSON string to a Python dictionary. |

#### Classes

| Name | Description |
|  --- | --- |
| HttpDateTime | A wrapper for datetime to support HTTP date format. |
| UnixDateTime | A wrapper for datetime to support Unix date format. |
| RFC3339DateTime | A wrapper for datetime to support RFC3339 format. |

## Common Code Documentation

### HttpResponse

Http response received.

#### Parameters

| Name | Type | Description |
|  --- | --- | --- |
| status_code | int | The status code returned by the server. |
| reason_phrase | str | The reason phrase returned by the server. |
| headers | dict | Response headers. |
| text | str | Response body. |
| request | HttpRequest | The request that resulted in this response. |

### HttpRequest

Represents a single Http Request.

#### Parameters

| Name | Type | Tag | Description |
|  --- | --- | --- | --- |
| http_method | HttpMethodEnum |  | The HTTP method of the request. |
| query_url | str |  | The endpoint URL for the API request. |
| headers | dict | optional | Request headers. |
| query_parameters | dict | optional | Query parameters to add in the URL. |
| parameters | dict &#124; str | optional | Request body, either as a serialized string or else a list of parameters to form encode. |
| files | dict | optional | Files to be sent with the request. |


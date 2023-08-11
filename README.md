# ApiUserAddress  
O projeto envolve o desenvolvimento de uma API para um sistema de gerenciamento de cadastro de clientes. 
A API receberá dados pessoais fornecidos pelos usuários para registrar as informações. 
Além disso, a API realizará consultas ao serviço da ViaCEP, um serviço online que fornece informações de endereço com base em um CEP fornecido. 
A API processará a resposta da ViaCEP e a transformará em uma resposta personalizada. Essa resposta será então persistida em um banco de dados. 
Em resumo, a API atua como um intermediário entre os usuários e a ViaCEP, enriquecendo os dados recebidos e armazenando-os para posterior recuperação e análise.

### Executando o Projeto com Docker
  * Certifique-se de ter o Docker instalado na sua máquina.
  * Execute o projeto usando o Docker Compose para inciar o MongoDB:
  ```shell
    $ docker-compose up -d
  ```
  * Execute o comando no arquivo "run.py" para iniciar o servidor local do aplicativo em um ambiente de desenvolvimento local.
  
# Endpoints

## URLS para test no Innsominia, Postman e etc..


### `/users/create`
### Requisição
Observação: Para realizar o cadastramento do CPF, utilize o serviço disponível em https://www.4devs.com.br/gerador_de_cpf. Essa é a única validação que pode acarretar problemas de criação, portanto, é importante utilizar um CPF válido gerado por esse serviço para evitar possíveis inconsistências no cadastro.
- Método: POST
- URL: `/users/create`
- Corpo da Requisição (JSON):
```json
    {
    "nome": "Michael",
    "data_de_nascimento": "30/06/1994",
    "email": "eduardo@email.com",
    "telefone": "+123(45) 0987-1234",
    "documento": "879.898.170-63"
    }
	
```
### Resposta

A resposta é um objeto JSON.

Exemplo de resposta bem-sucedida:
```json
[
	{
		"data": "Usuario registrado com sucesso"
	},
	201
]
```

### `/users/update`
### Requisição
Observação: Para realizar o cadastramento do CPF, utilize o serviço disponível em https://www.4devs.com.br/gerador_de_cpf. Essa é a única validação que pode acarretar problemas de criação, portanto, é importante utilizar um CPF válido gerado por esse serviço para evitar possíveis inconsistências no cadastro.
- Método: PUT
- URL: `/users/update`
- Corpo da Requisição (JSON):
```json
      {
        "user_id": "64d3c2b424893e1486bf736f",	
        "nome": "EduardoMascMichael",
        "data_de_nascimento": "30/06/2023",
        "email": "Michaelatualizado@email.com",
        "telefone": "+123(45) 0987-1234",
        "documento": "879.898.170-63"
      }
        
```
### Resposta

A resposta é um objeto JSON.

Exemplo de resposta bem-sucedida:
```json
[
	{
	"data": "Usuario atualizado com sucesso"
}]
```

### `/users/find`
### Requisição
- Método: GET
- URL: `/users/find`
### Resposta

A resposta é um objeto JSON.
Exemplo de resposta bem-sucedida:
```json
[
  {
  {
    "data": [
      {
        "_id": "64d548c2bf329809526af12d",
        "data_de_nascimento": "30/06/1994",
        "documento": "879.898.170-63",
        "email": "Michaelatualizado@email.com",
        "nome": "EduardoMascMichael",
        "telefone": "+123(45) 0987-1234"
      },
      {
        "_id": "64d548c8bf329809526af12f",
        "data_de_nascimento": "30/06/1994",
        "documento": "879.898.170-63",
        "email": "eduardo@email.com",
        "nome": "Michael",
        "telefone": "+123(45) 0987-1234"
      }
    ]
  }]
```

### `/users/delete`
### Requisição
- Método: DELETE
- URL: `/users/delete`
- Corpo da Requisição (JSON):
```json
      {
        "user_id": "string"
      }
        
```
### Resposta

A resposta é um objeto JSON.

Exemplo de resposta bem-sucedida:
```json
{
	"data": "Usario foi deletado"
}
```

### `/users/consulta_cep`
### Requisição
- Método: GET
- URL: `/users/consulta_cep`
### Resposta

A resposta é um objeto JSON.

Exemplo de resposta bem-sucedida:
```json
{
	"endereco": {
		"bairro": "Jardim Matarazzo",
		"cep": "03813-000",
		"cidade": "São Paulo",
		"compl": null,
		"logr": "Rua Figueira da Polinésia",
		"uf": "SP"
	},
	"sucesso": "true"
}
```

### `/users/check_cep`
### Requisição
- Método: GET
- URL: `/users/check_cep`
### Resposta

A resposta é um objeto JSON.

Exemplo de resposta bem-sucedida:
```json
	"data": [
		{
			"_id": "64d57c43b72985d4f4e8da74",
			"bairro": "bairro",
			"cidade": "cidade",
			"complemento": "complemento",
			"endereco": "endereco",
			"logradouro": "logradouro",
			"uf": "uf"
		},
		{
			"_id": "64d5a3476c087e8af6b2610a",
			"bairro": "Jardim Matarazzo",
			"cidade": "São Paulo",
			"complemento": null,
			"logradouro": "Rua Figueira da Polinésia",
			"uf": "SP"
		},
	]

```

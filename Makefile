.PHONY: help up build down shell makemigrations migrate seed test

help:  ## Mostra os comandos disponíveis
	@awk 'BEGIN {FS = ":.*##"; printf "\nComandos disponíveis:\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

up: ## Liga o servidor
	docker-compose up

build: ## Reconstrói a imagem do Docker
	docker-compose up --build

down: ## Desliga o servidor e remove os contentores
	docker-compose down

shell: ## Abre o terminal de dentro do Docker
	docker-compose run web bash

makemigrations: ## Cria novas migrações do Django
	docker-compose run web python manage.py makemigrations

migrate: ## Aplica as migrações no banco de dados
	docker-compose run web python manage.py migrate

seed: ## Roda o script de popular o banco de dados 
	docker-compose run web python manage.py seed

test: ## Roda os testes usando o pytest dentro do Docker
	docker-compose run web pytest
.PHONY: ;


build-auth: 
	docker build -t posty-auth ./auth/

build-logic: 
	docker build -t posty-logic ./logic/

run-auth:
	docker run -d -p 3001:3001 posty-auth

run-logic:
	docker run -d -p 3000:3000 posty-logic

rebuild-logic:
	docker-compose down && docker-compose build posty-logic && docker-compose up -d

rebuild-auth:
	docker-compose down && docker-compose build posty-auth && docker-compose up -d

build:
	docker-compose build

down:
	docker-compose down

up:
	docker-compose up

backend-sh: build
	docker-compose run --rm backend /bin/bash

frontend-sh: build
	docker-compose run --rm frontend /bin/bash

frontend-run: build
	docker-compose run --rm frontend node frontend-entrypoint.js


start-todo-application:
	docker-compose up -d --build todo_app

create-superuser:
	docker exec -it django_todo_app python3 manage.py createsuperuser

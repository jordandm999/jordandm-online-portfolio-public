run-mcp:
	uvicorn src.mcp.main:app --reload

run-django:
	python src/website/manage.py runserver 
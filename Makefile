PYTHON = python
MANAGE = $(PYTHON) manage.py

local:
	$(MANAGE) runserver --settings=core.settings.local

prod:
	$(MANAGE) runserver --settings=core.settings.prod

makemigrations:
	$(MANAGE) makemigrations --settings=core.settings.local

migrate:
	$(MANAGE) migrate --settings=core.settings.local

shell:
	$(MANAGE) shell --settings=core.settings.local

createsuperuser:
	$(MANAGE) createsuperuser --settings=core.settings.local

collectstatic:
	$(MANAGE) collectstatic --noinput --settings=core.settings.local

check:
	$(MANAGE) check --settings=core.settings.prod

collect:
	$(MANAGE) collectstatic --noinput --settings=core.settings.prod

.PHONY: default
default: local

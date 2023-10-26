test:
	docker-compose down --volumes --remove-orphans
	docker-compose run --rm web odoo -i base -d test_db --stop-after-init
	docker-compose run --rm web odoo -i prendario -d test_db --test-enable --stop-after-init

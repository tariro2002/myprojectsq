#!/usr/bin/env bash
set -o errexit
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'Admin1234!')" | python manage.py shell
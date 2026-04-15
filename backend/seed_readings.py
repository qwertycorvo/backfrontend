import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import DecibelReading

# Create sample readings
r1 = DecibelReading.objects.create(
    db_value=75.5,
    location="Main Street"
)

r2 = DecibelReading.objects.create(
    db_value=98.2,
    location="Highway 1"
)

print(f"Created reading: {r1}")
print(f"Created reading: {r2}")

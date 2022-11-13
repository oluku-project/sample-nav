from .models import Machine
from faker import Faker


fake = Faker()

def filldata(x):
    for i in range(0,x):
        Machine.objects.create(name=fake.name(),
        gps_loc = fake.iban(),
        description = fake.paragraph(nb_sentences=1),
        barcode = fake.ssn())
# name = models.CharField(max_length=100)
#   gps_loc = models.CharField(max_length=200)
#   description = models.TextField()
#   barcode = models.CharField(max_length=100)

from django.db import models

# Create your models here.
class Product(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),((DELETE,'Delete')))
    title =models.CharField(max_length=200)
    price =models.FloatField()
    Description=models.TextField()
    image=models.ImageField(upload_to='media/')
    priorty=models.IntegerField(default=0)
    delet_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

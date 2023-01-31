from django.db import models
from datetime import date

# Create your models here.
class Enterprise(models.Model):
    en_code = models.CharField(primary_key=True, max_length=2, null=False, verbose_name='Code')
    en_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.en_name}"

    class Meta:
        db_table = 'enterprise'
        verbose_name = 'Enterprise'
        verbose_name_plural = 'Enterprises'

class Store(models.Model):
    st_enterprise = models.ForeignKey('Enterprise', on_delete=models.CASCADE)
    st_code = models.CharField(primary_key=True, max_length=2)
    st_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.st_name}"

    class Meta:
        db_table = 'store'
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

class Department(models.Model):
    de_enterprise = models.ForeignKey('Enterprise', on_delete=models.CASCADE)
    de_store = models.ForeignKey('Store', on_delete=models.CASCADE)
    de_code = models.CharField(primary_key=True, max_length=2)
    de_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.de_name}"

    class Meta:
        db_table = 'department'
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

class Transaction(models.Model):
    tr_enterprise = models.ForeignKey('Enterprise', on_delete=models.CASCADE)
    tr_store = models.ForeignKey('Store', on_delete=models.CASCADE)
    tr_department = models.ForeignKey('Department', on_delete=models.CASCADE)
    tr_code = models.FloatField(primary_key=True)
    tr_date_time = models.DateTimeField(blank = True, null = True)
    tr_type_doc = models.CharField(max_length=1)
    tr_usd_value = models.FloatField()

    def __str__(self):
        return f"{self.tr_date_time} {self.tr_type_doc} {self.tr_usd_value} {self.tr_department} {self.tr_enterprise} {self.tr_store} {self.tr_code}"

    class Meta:
        db_table = 'transaction'
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'


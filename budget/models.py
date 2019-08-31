from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name= 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



class Setting(models.Model):
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    logo = models.ImageField()
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    active = models.BooleanField(default=False)
    
    class Meta:
        verbose_name= 'Setting'
        verbose_name_plural = 'Settings'

    def __str__(self):
        return self.title

class Year(models.Model):
    desc = models.CharField(max_length=150,default="Year")
    year = models.CharField(max_length=50,default="document year")
    class Meta:
        verbose_name='Year'
        verbose_name_plural ='Years'

    def __str__(self):
        return self.year


class Publication(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted =models.DateField()
    image = models.ImageField()
    category = models.ForeignKey(Category,on_delete = models.CASCADE)



    def __str__(self):
        return self.title


class Document(models.Model):
    file_title = models.CharField(max_length=100)
    file_media = models.FileField()
    category = models.ForeignKey(Category,on_delete = models.CASCADE,default="GENERAL")
    doc_year = models.ForeignKey(Year,on_delete = models.CASCADE)
    governors_speech = models.BooleanField(default=False)
    image_data = models.ImageField(null=True,blank=True)
    class Meta:
        verbose_name= 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.file_title



class Work(models.Model):
    work_title = models.CharField(max_length=100)
    work_image = models.ImageField()

    class Meta:
        verbose_name = 'Work'
        verbose_name_plural='Works'

    def __str__(self):
        return self.work_title
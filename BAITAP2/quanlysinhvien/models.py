# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SinhVien(models.Model):
    hoten = models.CharField(max_length=200)
    masv = models.CharField(max_length=200)
    nganhhoc = models.CharField(max_length = 100)

    def __str__(self):
        return self.masv

        
        
        



# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import SinhVien
from django.utils.encoding import python_2_unicode_compatible

# Register your models here.

admin.site.register(SinhVien)

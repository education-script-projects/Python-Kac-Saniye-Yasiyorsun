#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import *

kacsaniyeyasadin_ico = """
#########################################################
#         KAÇ SANİYE YAŞADIN ? - GH0ST S0FTWARE         #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#        Mail Address : pentestdatabase@gmail.com       #
# LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################
"""

print kacsaniyeyasadin_ico

dogum_tarihi = datetime.strptime(raw_input("Doğum gününüz (gün.ay.yıl): "), "%d.%m.%Y")

yas = datetime.now() - dogum_tarihi

print("{} saniyedir yaşıyosun dostum allah uzun ömürler versin :)".format(yas.total_seconds()))

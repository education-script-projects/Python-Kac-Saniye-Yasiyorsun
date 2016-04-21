#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import *

dogum_tarihi = datetime.strptime(raw_input("Doğum gününüz (gün.ay.yıl): "), "%d.%m.%Y")

yas = datetime.now() - dogum_tarihi

print("{} saniyedir yaşıyosun dostum allah uzun ömürler versin :)".format(yas.total_seconds()))

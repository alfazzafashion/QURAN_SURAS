#!/usr/bin/env python
#
# Hi There!
#
# You may be wondering what this giant blob of binary data here is, you might
# even be worried that we're up to something nefarious (good for you for being
# paranoid!). This is a base85 encoding of a zip file, this zip file contains
# an entire copy of pip (version 22.0.4).
#
# Pip is a thing that installs packages, pip itself is a package that someone
# might want to install, especially if they're looking to run this get-pip.py
# script. Pip has a lot of code to deal with the security of installing
# packages, various edge cases on various platforms, and other such sort of
# "tribal knowledge" that has been encoded in its code base. Because of this
# we basically include an entire copy of pip inside this blob. We do this
# because the alternatives are attempt to implement a "minipip" that probably
# doesn't do things correctly and has weird edge cases, or compress pip itself
# down into a single file.
#
# If you're wondering how this is created, it is generated using
# `scripts/generate.py` in https://github.com/pypa/get-pip.

from quran_suras import QuranSuras

quran_suras = QuranSuras()
suras = quran_suras.get_sura_by_number(sura_number=1, amount=1)
print(suras)
suras = quran_suras.get_sura_by_name(sura_name="النحل", amount=1)
print(suras)
sura_name = quran_suras.get_sura_name(sura_number=1)
print(sura_name)
sura_number = quran_suras.get_sura_number(sura_name="النمل")
print(sura_number)
page = quran_suras.get_page(page_number=1)
print(page)
radios = quran_suras.get_radios("id", 1)
print(radios)

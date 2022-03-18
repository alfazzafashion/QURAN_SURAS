# quran_suras

<p align="center">
    
![](mp3-quran.png)
    
A python [method](https://codeberg.org/Awiteb/quran_suras/src/branch/master/quran_suras/quran_suras.py) based on the API of the [mp3quran](https://www.mp3quran.net/), which helps you to fetch the surahs of the Qur’an via the surah number or name and more

## Installation
Use the package manager pip to install quran_suras.
~~~
pip3 install quran_suras
~~~
Features
* get surah by number
* get surah by name
* get surah name by number
* get surah number by name
* get quran page url by number
* get islamic radio url by language

## Usage
you can find examples [here](https://github.com/alfazzafashion/quran_suras/tree/main/modules)

## get surah by number:
~~~
from quran_suras import QuranSuras

quran_suras = QuranSuras()

suras = quran_suras.get_sura_by_number(sura_number=15, amount=1)
print(suras)
~~~

### Example Result
~~~
{
    'sura_name': 'يوسف', 
        'result': [
            {'reader': 'أحمد الحذيفي', 
                'url': 'https://server8.mp3quran.net/ahmad_huth/015.mp3'
            }
            ]
}
~~~

## get surah by name:
~~~
from quran_suras import QuranSuras

quran_suras = QuranSuras()

suras = quran_suras.get_sura_by_name(sura_name="النحل", amount=1)
print(suras)
~~~

### Example Result
~~~
{
    'sura_name': 'النحل', 
        'result': [
            {'reader': 'أحمد الحواشي', 
                'url': 'https://server11.mp3quran.net/hawashi/016.mp3'
                }
            ]
}
~~~

## get surah name by number:
~~~
from quran_suras import QuranSuras

quran_suras = QuranSuras()

sura_name = quran_suras.get_sura_name(sura_number=88)
print(sura_name)
~~~

### Example Result
~~~
الغاشية
~~~

## get surah number by name:
~~~
from quran_suras import QuranSuras

quran_suras = QuranSuras()

sura_number = quran_suras.get_sura_number(sura_name="النمل")
print(sura_number)
~~~

### Example Result
~~~
27
~~~

## get page from quran by page number:
~~~
from quran_suras import QuranSuras

quran_suras = QuranSuras()
page = quran_suras.get_page(page_number=601)
print(page)
~~~

### Example Result

![](https://www.mp3quran.net/api/quran_pages_arabic/601.png)

~~~
get radios by language:

from quran_suras import QuranSuras

quran_suras = QuranSuras()

radios = quran_suras.get_radios('en', 3)
print(radios) 
~~~

### Example Result
~~~
{
  'language': 'en', 
  'result': [
    {'name': '---Amazing short Recitations---', 
      'url': 'http://live.mp3quran.net:9702/'}, 
    {'name': '--Quran Tafseer--', 
      'url': 'http://live.mp3quran.net:9718/'}, 
    {'name': '-Beautiful Recitations-', 
      'url': 'http://live.mp3quran.net:9992/'}
  ]
}
~~~

## Meta

Libraries: [quran-suras](https://libraries.io/pypi/quran-suras)
License: [GNU General Public License v3 (GPLv3)](#LICENSE)

[Hashes](https://pip.pypa.io/en/stable/cli/pip_install/#hash-checking-mode) for quran_suras-1.1.4-py3-none-any.whl
| Algorithm 	| Hash digest |
| :------------ | :---------- |
| SHA256		| 838914d88f4d20890ce81eab5de156654be1ed069ab40638c0579b6e77eb9e57 |
| MD5			| ecef13e418d8a36a4669858eb849916e |
| BLAKE2-256	| 84d484c9f94856589e009b6c7b39e7b476ba5a6c59d0953cc0e8eb199c704625 |

## Author: [Awiteb](mailto:Awiteb@hotmail.com)

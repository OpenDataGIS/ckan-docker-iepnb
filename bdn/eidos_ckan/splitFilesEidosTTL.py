#!/usr/bin/python3
import os

# TODO: Descargar desde datos.iepnb.es

# path_orig = '/usr/lib/ckan/default/src/loadProcess/eidos.ttl.completo'
path_orig = os.path.join(os.path.dirname(__file__), 'data/eidos.ttl')
path_tmp = os.path.join(os.path.dirname(__file__), 'data/tmp/')
headers = ''
file_orig = open(path_orig, 'r', encoding="utf8")
lines = file_orig.readlines()

had_headers = False
new_item = ''
count = 0

if not os.path.exists(path_tmp):
    os.makedirs(path_tmp)

for line in lines:
    if not had_headers:
        if line.startswith('@prefix'):
            headers += line
        else:
            had_headers = True
    else:
        new_item += line
        if line.strip().startswith('a '):
            new_type = line.strip()[2:].strip()[:-1].strip().replace(':', '_')

        if not line.strip():
            count = count + 1
            file_tmp = open(path_tmp + '{}{}.ttl'.format(new_type, count), 'w', encoding="utf8")
            file_tmp.write(headers)
            file_tmp.write(new_item)
            file_tmp.close()

            new_item = ''

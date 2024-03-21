# Load TTLs
Ad-hoc CKAN software to retrieve data from EIDOS TTL and ingest datasets into CKAN.

**Requeriments:**
The code compiles with Python 3. The required libraries can be found in `requirements.txt`.

## Configuration
The necessary steps to configure the environment and install the libraries are as follows. First create the `venv` directory where it will run (or replace `whoami` with the desired user name if you create for example one for `ckan`):
```bash
# Linux
cd src/eidos_ckan/
python3 -m venv .env    # sudo apt-get install python3-venv
. .env/bin/activate
python3 -m pip install  install -r requirements.txt

# Windows
cd src/eidos_ckan/
python -m venv .env
.env/Scripts/activate.bat  # CMD || .env\Scripts\Activate.ps1  # Powershell
pip install  install -r requirements.txt
```

## Launch
1. Download https://datos.iepnb.es/datasets/eidos.ttl
	```bash
	curl -o eidos.ttl https://datos.iepnb.es/datasets/eidos.ttl
	```
2. Update `splitFilesEidosTTL.py` parameters:
	- `ckan_url`: CKAN site.
	- `path_orig`: Folder of EIDOS complete TTL.
	- `path_tmp`: Temp folder for TTLs

2. Execute splitFilesEidosTTL:
	```bash
	python3 splitFilesEidosTTL.py
	```
3. Create a `eidos-prueba` organization in CKAN.
4. Update `loadEidosTTL.py` parameters:
	- `ckan_url`: CKAN site.
	- `api_key`: http://{ckan_site_url}:5000/user/admin authorization key.
	- `path_tmp`: SplitFilesEidosTTL.py `path_tmp`
	
5. Load TTLs into CKAN
	```bash
	python3 loadEidosTTL.py
	```

## Sample:
**Darwin_Location100422.ttl**
```json
{
   "owner_org":"eidos-prueba",
   "type":"location",
   "Plinian_hasCell":[
      "https://datos.iepnb.es/recurso/sector-publico/cuadricula-espacial/celda/10kmE384N189"
   ],
   "Plinian_isLocationOf":[
      "https://datos.iepnb.es/recurso/sector-publico/medio-ambiente/pliniancore/TaxonRecord/20075",
      "https://datos.iepnb.es/recurso/sector-publico/medio-ambiente/pliniancore/TaxonRecord/20082",
      "https://datos.iepnb.es/recurso/sector-publico/medio-ambiente/pliniancore/TaxonRecord/20092"
   ],
   "title":"10kmE384N189",
   "name":"location_10kme384n189",
   "uri":"https://datos.iepnb.es/recurso/sector-publico/medio-ambiente/pliniancore/Location/10kmE384N189",
   "Darwin_locationID":[
      "10kmE384N189"
   ]
}
```
>**Note**<br>
> `Inserted location` - https://datos.iepnb.es/recurso/sector-publico/medio-ambiente/pliniancore/Location/10kmE384N189
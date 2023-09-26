#!/bin/bash

# Update ckanext-scheming and ckanext-scheming_dcat settings defined in the env var
echo "Set up ckanext-scheming_dcat. Clear index"
ckan -c $CKAN_INI search-index clear

echo "Loading ckanext-scheming and ckanext-scheming_dcat settings into ckan.ini"
ckan config-tool $CKAN_INI \
    "scheming.dataset_schemas=$CKANEXT__SCHEMING_DCAT_DATASET_SCHEMA" \
    "scheming.presets=$CKANEXT__SCHEMING_DCAT_PRESETS" 

echo "ckanext-scheming_dcat. Rebuild index"
ckan -c $CKAN_INI search-index rebuild
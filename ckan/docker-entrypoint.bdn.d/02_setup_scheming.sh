#!/bin/bash

# Update ckanext-scheming and ckanext-scheming_dcat settings defined in the env var
echo "Loading ckanext-scheming and ckanext-scheming_dcat settings into ckan.ini"
ckan config-tool $CKAN_INI \
    "scheming.dataset_schemas=$CKANEXT__SCHEMING_DCAT_DATASET_SCHEMA" \
    "scheming.presets=$CKANEXT__SCHEMING_DCAT_PRESETS" 
#!/bin/bash

# Update ckanext-scheming and ckanext-schemingdcat settings defined in the env var
echo "Loading ckanext-scheming and ckanext-schemingdcat settings into ckan.ini"
ckan config-tool $CKAN_INI \
    "scheming.dataset_schemas=$CKANEXT__SCHEMINGDCAT_DATASET_SCHEMA" \
    "scheming.presets=$CKANEXT__SCHEMINGDCAT_PRESETS" 

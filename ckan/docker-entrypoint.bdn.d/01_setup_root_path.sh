#!/bin/bash

# Update ckan.root_path to the CKAN config file
echo "Loading ckan.root_path in the CKAN config file"
ckan config-tool $CKAN_INI \
    "ckan.root_path = $BDN_CKAN__ROOT_PATH" 
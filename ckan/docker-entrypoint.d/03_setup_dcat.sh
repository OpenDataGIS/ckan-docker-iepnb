#!/bin/bash

# Add ckanext-dcat settings to the CKAN config file
echo "[docker-entrypoint.03_setup_dcat] Loading ckanext-dcat settings in the CKAN config file"
ckan config-tool $CKAN_INI \
    "ckanext.dcat.base_uri = $CKANEXT__DCAT__BASE_URI" \
    "ckanext.dcat.catalog_endpoint = $CKANEXT__DCAT__DEFAULT_CATALOG_ENDPOINT" \
    "ckanext.dcat.rdf.profiles = $CKANEXT__DCAT__RDF_PROFILES"
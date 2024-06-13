#!/bin/bash

# Update ckanext-scheming and ckanext-schemingdcat settings defined in the env var
echo "[docker-entrypoint.02_setup_scheming] Clear index"
ckan -c $CKAN_INI search-index clear

echo "[docker-entrypoint.02_setup_scheming] Loading ckanext-scheming and ckanext-schemingdcat settings into ckan.ini"
ckan config-tool $CKAN_INI \
    "scheming.dataset_schemas=$CKANEXT__SCHEMINGDCAT_DATASET_SCHEMA" \
    "scheming.group_schemas=$CKANEXT__SCHEMINGDCAT_GROUP_SCHEMAS" \
    "scheming.organization_schemas=$CKANEXT__SCHEMINGDCAT_ORGANIZATION_SCHEMAS" \
    "scheming.presets=$CKANEXT__SCHEMINGDCAT_PRESETS" \
    "schemingdcat.facet_list=$CKANEXT__SCHEMINGDCAT_FACET_LIST" \
    "schemingdcat.organization_custom_facets=$CKANEXT__SCHEMINGDCAT_ORGANIZATION_CUSTOM_FACETS" \
    "schemingdcat.group_custom_facets=$CKANEXT__SCHEMINGDCAT_GROUP_CUSTOM_FACETS" \
    "schemingdcat.geometadata_base_uri=$CKANEXT__SCHEMINGDCAT_GEOMETADATA_BASE_URI" \
    "schemingdcat.default_package_item_icon=$CKANEXT__SCHEMINGDCAT_DEFAULT_PACKAGE_ITEM_ICON" \
    "schemingdcat.default_package_item_show_spatial=$CKANEXT__SCHEMINGDCAT_DEFAULT_PACKAGE_ITEM_SHOW_SPATIAL" \
    "schemingdcat.show_metadata_templates_toolbar=$CKANEXT__SCHEMINGDCAT_SHOW_METADATA_TEMPLATES_TOOLBAR" \
    "schemingdcat.metadata_templates_search_identifier=$CKANEXT__METADATA_TEMPLATES_SEARCH_IDENTIFIER"

echo "[docker-entrypoint.02_setup_scheming] Rebuild index"
ckan -c $CKAN_INI search-index rebuild
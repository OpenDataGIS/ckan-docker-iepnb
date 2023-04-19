#!/bin/bash

# Update ckanext-iepnb settings
echo "Set up ckanext-iepnb. Clear index"
ckan -c $CKAN_INI search-index clear

echo "ckanext-iepnb. Load envvars"
ckan config-tool $CKAN_INI \
    "iepnb.server=$CKANEXT__IEPNB_SERVER" \
    "iepnb.path_menu =$CKANEXT__IEPNB_PATH_MENU" \
    "iepnb.breadcrumbs=$CKANEXT__IEPNB_BREADCRUMBS" \
    "iepnb.popular_tags=$CKANEXT__IEPNB_POPULAR_TAGS" \
    "iepnb.facet_list=$CKANEXT__IEPNB_FACET_LIST"

echo "ckanext-iepnb. Rebuild index"
ckan -c $CKAN_INI search-index rebuild
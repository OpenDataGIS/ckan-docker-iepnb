#!/bin/bash

# Update ckanext-iepnb settings
echo "ckanext-iepnb. Load envvars"
ckan config-tool $CKAN_INI \
    "iepnb.server=$CKANEXT__IEPNB_SERVER" \
    "iepnb.path_menu =$CKANEXT__IEPNB_PATH_MENU" \
    "iepnb.breadcrumbs=$CKANEXT__IEPNB_BREADCRUMBS" \
    "iepnb.popular_tags=$CKANEXT__IEPNB_POPULAR_TAGS"
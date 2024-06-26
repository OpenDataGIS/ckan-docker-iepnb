#!/bin/bash

# Update ckanext-iepnb settings
echo "ckanext-iepnb. Load envvars"
ckan config-tool $CKAN_INI \
    "iepnb.server=$CKANEXT__IEPNB_SERVER" \
    "iepnb.server_i18n=$CKANEXT__IEPNB_SERVER_I18N" \
    "iepnb.path_menu=$CKANEXT__IEPNB_PATH_MENU" \
    "iepnb.breadcrumbs=$CKANEXT__IEPNB_BREADCRUMBS" \
    "iepnb.popular_tags=$CKANEXT__IEPNB_POPULAR_TAGS" \
    "iepnb.featured_datasets=$CKANEXT__IEPNB_FEATURED_DATASETS"
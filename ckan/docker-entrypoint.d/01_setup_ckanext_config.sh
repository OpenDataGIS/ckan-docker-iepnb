#!/bin/bash

# ckanext-scheming/ckanext-schemingdcat: Update settings defined in the envvars (https://github.com/ckan/ckanext-pages#configuration)
echo "[docker-entrypoint.01_setup_ckanext_config] Clear index"
ckan -c $CKAN_INI search-index clear

# ckan: Update core settings
## Add SMTP settings if CKAN__SMTP_ENABLED is True
if [ "$CKAN__SMTP_ENABLED" = "True" ]; then
    echo "[docker-entrypoint.01_setup_ckanext_config] Adding SMTP settings to the CKAN config file"
    ckan config-tool $CKAN_INI \
        "smtp.server=$CKAN_SMTP_SERVER" \
        "smtp.starttls=$CKAN_SMTP_STARTTLS" \
        "smtp.user=$CKAN_SMTP_USER" \
        "smtp.password=$CKAN_SMTP_PASSWORD" \
        "smtp.mail_from=$CKAN_SMTP_MAIL_FROM" \
        "smtp.reply_to=" \
        "email_to=" \
        "error_email_from="
fi

echo "[docker-entrypoint.02_setup_scheming] Loading ckanext-scheming and ckanext-schemingdcat settings into ckan.ini"
ckan config-tool $CKAN_INI \
    "schemingdcat.facet_list=$CKANEXT__SCHEMINGDCAT__FACET_LIST" \
    "schemingdcat.organization_custom_facets=$CKANEXT__SCHEMINGDCAT__ORGANIZATION_CUSTOM_FACETS" \
    "schemingdcat.group_custom_facets=$CKANEXT__SCHEMINGDCAT__GROUP_CUSTOM_FACETS" \
    "schemingdcat.geometadata_base_uri=$CKANEXT__SCHEMINGDCAT__GEOMETADATA_BASE_URI" \
    "schemingdcat.default_package_item_icon=$CKANEXT__SCHEMINGDCAT__DEFAULT_PACKAGE_ITEM_ICON" \
    "schemingdcat.default_package_item_show_spatial=$CKANEXT__SCHEMINGDCAT__DEFAULT_PACKAGE_ITEM_SHOW_SPATIAL" \
    "schemingdcat.show_metadata_templates_toolbar=$CKANEXT__SCHEMINGDCAT__SHOW_METADATA_TEMPLATES_TOOLBAR" \
    "schemingdcat.metadata_templates_search_identifier=$CKANEXT__SCHEMINGDCAT__METADATA_TEMPLATES_SEARCH_IDENTIFIER"

## Update ckanext-iepnb settings
echo "ckanext-iepnb. Load envvars"
ckan config-tool $CKAN_INI \
    "iepnb.server=$CKANEXT__IEPNB_SERVER" \
    "iepnb.server_i18n=$CKANEXT__IEPNB_SERVER_I18N" \
    "iepnb.path_menu =$CKANEXT__IEPNB_PATH_MENU" \
    "iepnb.breadcrumbs=$CKANEXT__IEPNB_BREADCRUMBS" \
    "iepnb.popular_tags=$CKANEXT__IEPNB_POPULAR_TAGS" \
    "iepnb.featured_datasets=$CKANEXT__IEPNB_FEATURED_DATASETS"

# Rebuild index
echo "[docker-entrypoint.01_setup_ckanext_config] Rebuild index"
ckan -c $CKAN_INI search-index rebuild
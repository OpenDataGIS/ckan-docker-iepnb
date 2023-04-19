#!/bin/bash

# Set the name of the token to revoke
TOKEN_NAME="xloader"

# Get the list of tokens and extract the IDs for tokens with the specified name
TOKEN_IDS=$(ckan -c $CKAN_INI user token list ckan_admin | grep "$TOKEN_NAME" | awk -F'[][]' '{print $2}' | tr -d '[]')

# Revoke each previous token of xloader
for TOKEN_ID in $TOKEN_IDS
do
  ckan -c $CKAN_INI user token revoke $TOKEN_ID
  if [ $? -eq 0 ]; then
    echo "API Token $TOKEN_ID has been revoked"
  fi
done

# Add ckanext.xloader.api_token to the CKAN config file
echo "Loading ckanext-xloader settings in the CKAN config file"
ckan config-tool $CKAN_INI \
    "ckanext.xloader.api_token=xxx" \
    "ckanext.xloader.jobs_db.uri=$CKANEXT__XLOADER__JOBS__DB_URI"

# Create ckanext-xloader API_TOKEN
echo "Set up ckanext.xloader.api_token in the CKAN config file"
ckan config-tool $CKAN_INI "ckanext.xloader.api_token=$(ckan -c $CKAN_INI user token add ckan_admin xloader | tail -n 1 | tr -d '\t')"

#TODO: Setup worker background
#echo "Set up CKAN jobs worker"
#ckan -c $CKAN_INI jobs worker default
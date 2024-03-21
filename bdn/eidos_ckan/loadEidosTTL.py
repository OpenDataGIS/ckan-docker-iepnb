#!/usr/bin/python3

from rdflib import Graph

import urllib
import urllib.request
import urllib.parse
import json

import os
import glob

owner_org = 'test'

sparql_header = """
    PREFIX Geo:   <http://www.opengis.net/ont/geosparql#>
    PREFIX Darwin: <http://rs.tdwg.org/dwc/terms/>
    PREFIX rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX Malla: <https://datos.iepnb.es/def/sector-publico/cuadricula-espacial#>
    PREFIX CuadriculaEsp: <https://datos.iepnb.es/def/sector-publico/cuadricula-espacial#>
    PREFIX xsd:   <http://www.w3.org/2001/XMLSchema#>
    PREFIX Dublin: <http://purl.org/dc/terms/>
    PREFIX Plinian: <https://datos.iepnb.es/def/sector-publico/medio-ambiente/pliniancore#>
    PREFIX DC:   <http://purl.org/dc/terms/>
    PREFIX geoSf: <http://www.opengis.net/ont/sf#>

    """


def insert_dataset(dataset_dict):
    ckan_url = 'https://des.iepnb.es/bdn'
    api_key = 'api-key'

    # request = urllib2.Request(intranet_url + '/api/action/package_create')
    request = urllib.request.Request(ckan_url + '/api/action/package_create')
    # data_string = urllib.parse.quote(json.dumps(dataset_dict))
    # data_string = urllib.parse.urlencode(dataset_dict).encode("utf-8")
    data_string = json.dumps(dataset_dict).encode("utf-8")

    #print("data_string")
    #print(data_string)

    request.add_header('Authorization', api_key)
    request.add_header('Content-Type', ' application/json ')

    # Make the HTTP request.
    # response = urllib2.urlopen(request, data_string)
    #print('Enviando a ckan')
    response = urllib.request.urlopen(request, data_string)
    #print('Finalizado envio a ckan')
    assert response.code == 200

    # Use the json module to load CKAN's response into a dictionary.
    response_dict = json.loads(response.read())
    assert response_dict['success'] is True

    # package_create returns the created package as its result.
    created_package = response_dict['result']
    # print (created_package)


def insert_darwin_location(g, filename):
    fields = ['Plinian_hasCell', 'Plinian_isLocationOf', 'Darwin_locationID']

    insert_generic(g, filename, fields, 'location', 'Darwin:Location', 'Darwin_locationID', 'Darwin_locationID')


def insert_darwin_measurementorfact(g, filename):
    fields = ['Darwin_measurementAccuracy', 'Darwin_measurementDeterminedDate',
              'Darwin_measurementID', 'Darwin_measurementMethod',
              'Darwin_measurementRemarks', 'Darwin_measurementType',
              'Darwin_measurementValue', 'Plinian_AppliesTo',
              'Darwin_measurementUnit']

    insert_generic(g, filename, fields, 'measurement_or_fact',
                   'Darwin:MeasurementOrFact', 'Darwin_measurementID', 'Darwin_measurementValue')


def insert_darwin_taxon(g, filename):
    fields = ['Darwin_class', 'Darwin_family', 'Darwin_genus',
              'Darwin_higherClassification', 'Darwin_informationWithheld',
              'Darwin_infraspecificEpithet', 'Darwin_kingdom',
              'Darwin_nameAccordingTo', 'Darwin_namePublishedIn',
              'Darwin_namePublishedInYear', 'Darwin_order', 'Darwin_phylum',
              'Darwin_scientificName', 'Darwin_scientificNameAuthorship',
              'Darwin_specificEpithet', 'Darwin_taxonConceptID',
              'Darwin_taxonID', 'Darwin_taxonRank', 'Darwin_taxonRemarks', 
              'Darwin_taxonomicStatus', 'Darwin_verbatimTaxonRank',
              'Darwin_subgenus']

    insert_generic(g, filename, fields, 'taxon',
                   'Darwin:Taxon', 'Darwin_taxonID', 'Darwin_scientificName')


def insert_dc_managementconservationtype(g, filename):
    fields = ['DC_ManagementID', 'DC_ManagementType', 'DC_Objectives',
              'Darwin_Year', 'Darwin_ConservationMeasurementUnstructured',
              'Darwin_HumanAndEnvironmentalRelevance',
              'Darwin_HumanAndEnvironmentalRelevanceUnstructured',
              'Darwin_ManagementConservationUnstructured',
              'Darwin_ManagementPlan', 'Darwin_ManagementRemarks']

    insert_generic(g, filename, fields, 'management_conservation_type',
                   'DC:ManagementConservationType', 'DC_ManagementID', 'DC_ManagementID')


def insert_plinian_collection(g, filename):
    fields = ['Plinian_Code', 'Plinian_CollectionDescription',
              'Plinian_Country_txt', 'Plinian_IDCollection', 'Plinian_Year']

    insert_generic(g, filename, fields, 'collection',
                   'Plinian:Collection', 'Plinian_IDCollection', 'Plinian_CollectionDescription')


def insert_plinian_directthreatstype(g, filename):
    fields = ['Plinian_DirectThreatID', 'Plinian_DirectThreatUnstructured']

    insert_generic(g, filename, fields, 'direct_threats_type',
                   'Plinian:DirectThreatsType', 'Plinian_DirectThreatID', 'Plinian_DirectThreatID')


def insert_plinian_distributiontype(g, filename):
    fields = ['Plinian_DistributionID', 'Plinian_DistributionScope',
              'Plinian_DistributionScopeType', 'Plinian_DistributionUnstructured',
              'Plinian_Distribution_Type', 'Plinian_GeographicEntity',
              'Plinian_temporalCoverage']

    insert_generic(g, filename, fields, 'distribution_type',
                   'Plinian:DistributionType', 'Plinian_DistributionID', 'Plinian_DistributionID')


def insert_plinian_habitatstype(g, filename):
    fields = ['Plinian_HabitatUnstructured', 'Plinian_HabitatsID']

    insert_generic(g, filename, fields, 'habitats_type',
                   'Plinian:HabitatsType', 'Plinian_HabitatsID', 'Plinian_HabitatsID')


def insert_plinian_invasivenesstype(g, filename):
    fields = ['Plinian_IDInvasiveness', 'Plinian_InvasivenessUnstructured',
              'Plinian_Route', 'Plinian_origin', 'Plinian_vector']

    insert_generic(g, filename, fields, 'invasiveness_type',
                   'Plinian:InvasivenessType', 'Plinian_IDInvasiveness', 'Plinian_IDInvasiveness')


def insert_plinian_legislationtype(g, filename):
    fields = ['Plinian_LegislationID', 'Plinian_LegislationName',
              'Plinian_LegislationRead', 'Plinian_ProtectionLegalStatus',
              'Plinian_Remarks']

    insert_generic(g, filename, fields, 'legislation_type',
                   'Plinian:LegislationType', 'Plinian_LegislationID', 'Plinian_LegislationName')


def insert_plinian_populationbiologytype(g, filename):
    fields = ['Plinian_IDPopulationBiology',
              'Plinian_PopulationBiologyUnstructured']

    insert_generic(g, filename, fields, 'population_biology_type',
                   'Plinian:PopulationBiologyType', 'Plinian_IDPopulationBiology', 'Plinian_IDPopulationBiology')


def insert_plinian_recordmetadatatype(g, filename):
    fields = ['Plinian_hasRevision']

    insert_generic(g, filename, fields, 'record_metadata_type',
                   'Plinian:RecordMetadataType', 'Plinian_hasRevision', 'Plinian_hasRevision')


def insert_plinian_referencetype(g, filename):
    fields = ['Plinian_identifier', 'Plinian_reference', 'Plinian_language',
              'Plinian_creator', 'Plinian_date', 'Plinian_publisher',
              'Plinian_source', 'Plinian_title', 'Plinian_type']

    insert_generic(g, filename, fields, 'reference_type',
                   'Plinian:ReferenceType', 'Plinian_identifier', 'Plinian_identifier')


def insert_plinian_taxonrecord(g, filename):
    fields = ['Plinian_CodeCITES', 'Plinian_CodeEUNIS', 'Plinian_CodeEURING',
              'Plinian_CodePhoto', 'Plinian_CodeRedNatura',
              'Plinian_FullDescriptionUnstructured', 'Plinian_TaxonRecordID',
              'Plinian_grupoTaxonomico', 'Plinian_hasCollection',
              'Plinian_hasDirectThreats', 'Plinian_hasDistribution',
              'Plinian_hasHabitats', 'Plinian_hasHierarchy',
              'Plinian_hasLegislation', 'Plinian_hasLocation',
              'Plinian_hasMeasurement', 'Plinian_hasPopulationBiology',
              'Plinian_hasRecordMetadata', 'Plinian_hasThreatStatus',
              'Plinian_hasVernacularName', 'DC_hasManagementConservation']

    insert_generic(g, filename, fields, 'taxon_record',
                   'Plinian:TaxonRecord', 'Plinian_TaxonRecordID',
                   'Plinian_grupoTaxonomico')


def insert_plinian_threatstatustype(g, filename):
    fields = ['Darwin_ThreatCategory', 'Darwin_ThreatStatusID',
              'Darwin_ThreatStatusUnstructured', 'Darwin_coverageArea',
              'Plinian_Authority', 'Plinian_Criterion', 'Plinian_Year']

    insert_generic(g, filename, fields, 'threat_status_type',
                   'Plinian:ThreatStatusType', 'Darwin_ThreatStatusID', 'Darwin_ThreatStatusID')


def insert_plinian_vernacularname(g, filename):
    fields = ['Plinian_Language', 'Plinian_Name', 'Plinian_VernacularNameID']

    insert_generic(g, filename, fields, 'vernacular_name',
                   'Plinian:VernacularName', 'Plinian_VernacularNameID', 'Plinian_Name')


def insert_generic(g, filename, fields, _type, rdf_type, name_field,
                   title_field):

    dataset_dict = {}
    dataset_dict['owner_org'] = owner_org
    dataset_dict['type'] = _type

    for fld in fields:
        #fld = fld_aux.replace('.', '')

        sparql_query = sparql_header + """
            SELECT ?uri ?""" + fld + """
            WHERE {
                ?uri rdf:type """ + rdf_type + "."

        sparql_query += '    OPTIONAL { '
        sparql_query += '?uri {} ?{}'.format(fld.replace('_', ':'), fld)
        sparql_query += '}. \n'

        sparql_query += """
            }
        """
        #print(sparql_query)
        results = g.query(sparql_query)
        # print(results)

        aux = []
        for row in results:
            _valor = eval('row["' + fld + '"]')
            if _valor:
                # dataset_dict[fld] = str(_valor)
                aux.append(str(_valor))

                if fld == title_field:
                    dataset_dict['title'] = str(row[title_field])

                if fld == name_field:
                    # si no está este campo, que dé fallo
                    dataset_dict['name'] = _type + '_' + str(row[name_field])
                    # aprovechamos para rellenar este campo tambien
                    dataset_dict['uri'] = str(row.uri)

        #dataset_dict[fld.replace('j0_', 'DC_')] = aux
        dataset_dict[fld] = aux

    # print(dataset_dict)

    try:
        insert_dataset(dataset_dict)
        os.remove(filename)
        print('Inserted {} - {}'.format(_type, row.uri))
    except Exception as e:
        print('Error {} inserting {} - {}'.format(e, _type, row.uri))


def call_action_by_type(dataset_type, g, filename):
    if dataset_type == 'Darwin_Location':
        insert_darwin_location(g, filename)
    elif dataset_type == 'Darwin_MeasurementOrFact':
        insert_darwin_measurementorfact(g, filename)
    elif dataset_type == 'Darwin_Taxon':
        insert_darwin_taxon(g, filename)
    elif dataset_type == 'j.0_ManagementConservationType':
        insert_dc_managementconservationtype(g, filename)
    elif dataset_type == 'Plinian_Collection':
        insert_plinian_collection(g, filename)
    elif dataset_type == 'Plinian_DirectThreatsType':
        insert_plinian_directthreatstype(g, filename)
    elif dataset_type == 'Plinian_DistributionType':
        insert_plinian_distributiontype(g, filename)
    elif dataset_type == 'Plinian_HabitatsType':
        insert_plinian_habitatstype(g, filename)
    elif dataset_type == 'Plinian_InvasivenessType':
        insert_plinian_invasivenesstype(g, filename)
    elif dataset_type == 'Plinian_LegislationType':
        insert_plinian_legislationtype(g, filename)
    elif dataset_type == 'Plinian_PopulationBiologyType':
        insert_plinian_populationbiologytype(g, filename)
    elif dataset_type == 'Plinian_RecordMetadataType':
        insert_plinian_recordmetadatatype(g, filename)
    elif dataset_type == 'Plinian_ReferenceType':
        insert_plinian_referencetype(g, filename)
    elif dataset_type == 'Plinian_TaxonRecord':
        insert_plinian_taxonrecord(g, filename)
    elif dataset_type == 'Plinian_ThreatStatusType':
        insert_plinian_threatstatustype(g, filename)
    elif dataset_type == 'Plinian_VernacularName':
        insert_plinian_vernacularname(g, filename)
    else:
        pass


path_tmp = os.path.join(os.path.dirname(__file__), 'data/tmp/')

items = ['Darwin_Location', 'Darwin_MeasurementOrFact', 'Darwin_Taxon',
         'j.0_ManagementConservationType',
         'Plinian_Collection',
         'Plinian_DirectThreatsType', 'Plinian_DistributionType',
         'Plinian_HabitatsType', 'Plinian_InvasivenessType',
         'Plinian_LegislationType', 'Plinian_PopulationBiologyType',
         # ESTE NO TIENE UN ID EN CAMPO APARTE
         # 'Plinian_RecordMetadataType',
         'Plinian_ReferenceType',
         'Plinian_TaxonRecord',
         'Plinian_ThreatStatusType',
         'Plinian_VernacularName']

for prefix in items:
    print(path_tmp + prefix + '*')
    for filename in glob.glob(path_tmp + prefix + '*'):
        g = Graph()
        g.parse(filename, format='turtle')
        call_action_by_type(prefix, g, filename)

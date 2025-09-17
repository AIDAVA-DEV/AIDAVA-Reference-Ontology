
# AIDAVA RO

This repository contains the AIDAVA reference ontology (AIDAVA RO), as well as versions of the SPHN schema and a list of termonologies: 

- A file with the SPHN schema version 2023.2 - [sphn_rdf_schema_2023.2.ttl](https://github.com/AIDAVA-DEV/AIDAVA-Reference-Ontology/blob/main/sphn_rdf_schema_2023.2.ttl) - the original SPHN schema with no changes - this is the initial base of the AIDAVA RO
[AIDAVA-Reference-Ontology.ttl](https://github.com/AIDAVA-DEV/AIDAVA-Reference-Ontology/blob/main/AIDAVA-Reference-Ontology.ttl) - the file with the changes implemented for the AIDAVA RO
- A file with **subset** of SPHN that should be loaded with the AIDAVA ontology - [sphn_rdf_schema.ttl](https://github.com/AIDAVA-DEV/AIDAVA-Reference-Ontology/blob/main/sphn_rdf_schema.ttl) - a reduced file, from which are removed definitions and statements that were changed for the purposes of the AIDAVA project and were moved to the [AIDAVA-Reference-Ontology.ttl](https://github.com/AIDAVA-DEV/AIDAVA-Reference-Ontology/blob/main/AIDAVA-Reference-Ontology.ttl) file 
- A **merge** between the AIDAVA ontology file and SPHN subset file - [aidava-sphn.ttl](https://github.com/AIDAVA-DEV/AIDAVA-Reference-Ontology/blob/main/aidava-sphn.ttl) - this is the file used as the current reference ontology in the AIDAVA project for data onboarding because it contains both SPHN (with some parts missing, that are changed in AIDAVA RO) and the AIDAVA RO changes AIDAVA-Reference-Ontology.ttl. 

The changes of the ontology file are done in Protege. The **AIDAVA-Reference-Ontology.ttl** is loaded and it prompts to be loaded also the expected external terminologies and the SPHN terminology (the subset one should be selected). All changes and additions are done in the **AIDAVA-Reference-Ontology.ttl** file. Then, the **AIDAVA-Reference-Ontology.ttl** file is merged with the loaded SPHN ontology (**sphn_rdf_schema.ttl**) and exported as **aidava-sphn.ttl** file. If there are changes that are directly changing the SPHN schema and not just adding on top of it, the statements relevant to the changes are removed from the **aidava-sphn.ttl** file (by loading that file separately in Protege and removing what’s needed and then saving). 


## Resources

In the AIDAVA project are used some of the external terminologies available in [external-terminologies](https://github.com/AIDAVA-DEV/AIDAVA-Reference-Ontology/tree/main/external-terminologies), as well as some additional resources, listed below. For the terminology resources we have provided metadata in the form of dcat descriptions available in [terminology-descriptions](https://github.com/AIDAVA-DEV/AIDAVA-Reference-Ontology/tree/main/terminology-descriptions) that should be loaded to the repository of the reference ontology along with the resources. This was motivated by the need to be able to extract up to date general information about the resource in formats such as FHIR. 

In addition, there are lists of LOINC codes that are used for assigning FHIR categories for the FHIR IPS Profile Observation, that would also be loaded to specific named graphs, as described below. 

### Named graph suggestions

#### AIDAVA RO 
 - aidava-sphn.ttl: https://rdf.aidava.eu/ontology/aidava-sphn 

#### Termonologies

 - https://rdf.aidava.eu/ontology/terminology/snomed-ct-int
 - https://rdf.aidava.eu/ontology/terminology/snomed-ct-nl
 - https://rdf.aidava.eu/ontology/terminology/snomed-ct-et
 - https://rdf.aidava.eu/ontology/terminology/snomed-ct-de
 - https://rdf.aidava.eu/ontology/terminology/snomed-ct-at
 - https://rdf.aidava.eu/ontology/terminology/loinc
 - https://rdf.aidava.eu/ontology/terminology/ucum
 - https://rdf.aidava.eu/ontology/terminology/atc
 - https://rdf.aidava.eu/ontology/terminology/icd10gm
 - https://rdf.aidava.eu/ontology/mapping/snomed-ct-int_to_icd10gm 

 #### Descriptions of Termonologies

 - https://rdf.aidava.eu/metadata/description/snomed-ct-int
 - https://rdf.aidava.eu/metadata/description/snomed-ct-nl
 - https://rdf.aidava.eu/metadata/description/snomed-ct-et
 - https://rdf.aidava.eu/metadata/description/snomed-ct-de
 - https://rdf.aidava.eu/metadata/description/snomed-ct-at
 - https://rdf.aidava.eu/metadata/description/loinc
 - https://rdf.aidava.eu/metadata/description/ucum
 - https://rdf.aidava.eu/metadata/description/atc
 - https://rdf.aidava.eu/metadata/description/icd10gm

#### FHIR categories value sets

 - https://rdf.aidava.eu/ontology/terminology/loinc/category/laboratory
 - https://rdf.aidava.eu/ontology/terminology/loinc/category/vitalsigns


## AIDAVA RO development summary 

There are many additions to SPHN in the AIDAVA RO, as well as many changes: 

---
---

### Additions:

**1. Classes:** The classes were introduced usually with new properties that are highlighted, and some properties from SPHN had to be redefined to include it as a domain and/or range. 

---

#### Person 

Related Issues: #126

**IRI** 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/Person

**Description** 	
a unique person that can be represented by different roles such as being a patient or a healthcare practitioner

**In Domain Of** 

 - sphn:SPHNConcept
 - ***has administrative gender*** *op* max 1 min 0
 - ***has subject name*** *op* min 0 max 1
 - ***has birth datetime*** *dp* min 0 max 1
 - sphn:hasIdentifier *dp* max 1 min 0

In Range Of 	
 - ***is feature of*** *op* 

---

#### Patient 

Related Issues: #16, #68, #50, #78, #79, #126

**IRI** 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/Patient

**Description** 	
Individual receiving health care services

**Sub Class Of** 
 - sphn:SPHNConcept
 - Person

**In Domain Of** 

 - ***has administrative gender*** *op* max 1 min 0
 - ***has birth date*** *op* min 1 max 1
 - ***has contact information*** *op* min 0 max 1
 - ***has subject name*** *op* max 1 min 1
 - ***is feature of*** *op* min 0 max 1
 - ***has birth datetime*** *dp* min 1 max 1
 - sphn:hasIdentifier *dp* min 0 max 1
 - ***has birth date*** *op*
 - ***has drug administration event*** *op*
 - ***has drug prescription*** *op*
 - ***has measurement*** *op*
 - ***has problem condition*** *op*
 - ***has procedure*** *op*

**In Range Of** 	

 - ***as patient*** *op* 

---

#### Healthcare Personnel
Related Issues: #126

**IRI** 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/HealthcarePersonnel

**Description** 

a person that is affiliated with a healthcare organization in the role of a healthcare proffesional, practitioner or someone with a formal responsibility in the provisioning of healthcare or related services

**In Domain Of**	

 - ***has contact information*** *op* max 1 min 0
 - ***is feature of*** *op* max 1 min 0
 - ***has subject name*** *op* min 0
 - ***is part of*** *op* min 0
 - ***has job title*** *dp* min 0
 - sphn:hasIdentifier min 0 

---

#### Subject Name
Related Issues: #126

**IRI** 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/SubjectName

**Description** 
Name of a human

**In Domain Of**

 - ***has family name*** *dp* min 1 max 1
 - ***has full name*** *dp* max 1 min 0
 - ***has given name*** *dp* min 1 

**In Range Of** 	has subject name*** *op*

---

#### Healthcare Organization
Related Issues: #126

**IRI** 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/HealthcareOrganization

**Description** 	
The Healthcare Organization is a hospital, clinic or a healthcare facility

**In Domain Of** 	

 - sphn:hasCode max 1 min 0
 - ***has address*** *op* min 0 max 1
 - ***has contact information*** *op* min 0 max 1
 - sphn:hasIdentifier max 1 min 0
 - sphn:hasName min 0 
	

**In Range Of** 	
 - ***has healthcare organization*** *op*
 - ***is part of*** *op*

---

#### Department
Related Issues: #126

**IRI** 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/Department

**Description** 
a department of an organization or an institution

**In Domain Of**	

 - ***has address*** *op* max 1 min 0
 - ***has contact information*** *op* min 0 max 1
 - ***is part of*** *op*
 - sphn:hasIdentifier min 0
 - sphn:hasName min 0

**In Range Of** 	

 - ***is part of*** *op* min 0

---

#### Contact Information
Related Issues: #126

**IRI** 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/ContactInformation

**Description** 
the contact information of a person or an organization

**In Domain Of** 	

 - ***has contact type*** *dp*
 - ***has email address*** *dp*
 - ***has fax*** *dp*
 - ***has language*** *dp*
 - ***has phone number*** *dp*

**In Range Of** 	
 - ***has contact information*** *op*

---

#### Address
Related Issues: #126

**IRI** 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/Address

**Description** 
The address of a person or an organization

**In Domain Of**

 - sphn:hasFreeText min 0 max 1
 - ***has city*** *dp*
 - ***has country*** *dp*
 - ***has postal code*** *dp*

**In Range Of** 	has address*** *op*

---

#### Product
Related Issues: #21

**IRI** 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/Product

**Description** 	
a pharmaceutical or biologic product

**In Domain Of** 
 - sphn:hasCode max 1 min 0

---

#### Set
Related Issues: #127 

**IRI** 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/Set

**Description** 	
A set is an information object for which there may be zero or more items.

**In Domain Of** 	
 - ***has member*** *op*
 - ***has measurement*** *op* min 1 

---

#### Observation Category 
Related to FHIR IPS representation issues

**IRI** 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/ObservationCategory

**Description** 	
Obsevation category allowing to group LOINC codes of type Measurement

**In Range Of** 
- has category *op* 

**Instances** 
 - Laboratory
 - Vital Signs 
 - Social History 

---

#### Vital signs
Related to FHIR IPS representation issues

**IRI** 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/VitalSigns

**Description** 	
Class representing Vital signs in FHIR IPS implementation

**2. Value Sets**

---

#### Encounter Class

**IRI** 	http://terminology.hl7.org/ValueSet/encounter-class
Related to FHIR IPS representation issues

**Description** 	
This value set defines a set of codes that can be used to indicate the class of encounter: a specific code indicating class of service provided.

Super Class Of 	

 - Ambulatory
 - Emergency
 - Home Health
 - Inpatient Encounter
 - Observation Encounter
 - Virtual

**3. Properties**

---

#### has record date time 
Related Issues: #135

**IRI** https://biomedit.ch/rdf/sphn-ontology/sphn#hasRecordDateTime 

**Sub Property Of**
 - has datetime *dp* 

**Super Property Of**
 - has first record datetime *dp* 

**Domain**

Drug Prescription, Body Position, Simple Score, Electrocardiographic Procedure, Body Surface Area, Administrative Gender, Sample, Oncology Treatment Assessment, Measurement, Radiotherapy Procedure, Cardiac Index, Administrative Case, Tumor Grade, Procedure, Civil Status, Access Device Presence, Adverse Event, TNM Classification, Tumor Specimen, Consent, Allergy, Diagnostic Radiologic Examination, Allergy Episode, Lab Result, FOPH Procedure, Problem Condition, Tumor Stage, Drug Administration Event, Healthcare Encounter, Body Mass Index

**Range**

xsd:DateTime 

---

#### Provenance and relative temporality related properties 
Related Issues: #141, #31, #12, #14, #17

**Object properties**
 - has part 
 - precedes - domains and ranges:  sphn:HealthcareEncounter, sphn:Procedure, sphn:Measurement, sphn:TumorGrade, sphn:ProblemCondition, sphn:TNMClassification, sphn:TumorStage, sphn:AdministrativeCase

**Data properties** - with domain sphn:DataFile
 - audit event timestamp
 - author specialty
 - committer
 - composer
 - file path
 - file source
 - source type
 - subject of care

---

#### List of all object properties added: 
 - has address
 - has administrative gender
 - has birth date
 - has category
 - Condition code
 - has contact information
 - has drug administration event
 - has drug prescription
 - has healthcare organization
 - has measurement
 - has member
 - has part
 - has patient
 - has problem condition
 - has procedure
 - has subject name
 - interprets
 - is feature of
 - is part of
 - precedes
 - using substance

---

#### List of all data properties added: 
 - audit event timestamp
 - author specialty
 - committer
 - composer
 - file path
 - file source
 - has city
 - has contact type
 - has country
 - has email address
 - has family name
 - has fax
 - has full name
 - has given name
 - has job title
 - has language
 - has phone number
 - has postal code
 - source type
 - subject of care

---
---

### Deprecated

#### Deprecated Classes

 - Oncology Diagnosis
 - Biosample
 - Blood Pressure
 - Body Height
 - Body Temperature
 - Body Weight
 - Cardiac Output
 - Catheter
 - Central Venous Pressure
 - Circumference Measure
 - Data Provider Institute - replaced with Healthcare Organization
 - Diagnosis
 - FOPH Diagnosis
 - Heart Rate
 - Inhaled Oxygen Concentration
 - Lab Result
 - Nursing Diagnosis
 - Oxygen Saturation
 - Systemic Arterial Blood Pressure

#### Deprecated Properties	

 - hasDiastolicPressure  
 - hasDataProviderInstitute - changed to hasHealthCareOrganization                                                 	  
 - hasMeanPressure                                                    	  
 - hasOxygenEquipment                                                        	  
 - hasOxygenFlowRate                                                        	  
 - hasRegularityCode                                                        	  
 - hasSubjectPseudoIdentifier
 - hasSystolicPressure

---
---

### Changes related to main profiles

#### Data File related
Issues: #93, #126

**New properties with domain sphn:DataFile:** 

 - has patient *op* 
 - audit event timestamp *dp*
 - author specialty *dp*
 - committer *dp*
 - composer *dp*
 - file path *dp*
 - file source *dp*
 - source type *dp*
 - subject of care *dp*

**In Range Of**	

 - sphn:hasDataFile *op* 

**Changes to domains of sphn:hasDataFile:** 

 - original domains: Electrocardiogram
 - new domains: Access Device Presence, Administrative Case, Administrative Gender, Adverse Event, Allergy, Allergy Episode, Biobanksample, Birth Date, Body Mass Index, Body Position, Body Surface Area, Cardiac Index, Civil Status, Consent, Data File, Death Date, Death Status, Diagnostic Radiologic Examination, Drug Administration Event, Drug Prescription, Electrocardiogram, Electrocardiographic Procedure, FOPH Procedure, Gestational Age At Birth, Healthcare Encounter, Measurement, Oncology Treatment Assessment, Problem Condition, Procedure, Radiotherapy Procedure, Sample, Simple Score, TNM Classification, Tumor Grade, Tumor Specimen, Tumor Stage, Variant Descriptor

---

#### Problem Condiion related
Issues: #13, #20, #25, #26, #38, #66. #141

**Equivalent class** changed to snomed:404684003 (clinical finding)

**New properties with domain sphn:ProblemCondition:** 

 - has patient *op* 
 - interprets *op*
 - precedes *op*

**Changed properties with domain sphn:ProblemCondition:** 

 - sphn:hasStatusCode  *op* - with SNOMED code restrictions - some (261665006 or 410516002 or 410590009 or 410592001 or 410594000 or 410605003 or 415684004 or 723510000)
 - sphn:hasBodySite *op* 

**New properties with range sphn:ProblemCondition:**	

 - has problem condition *op* - with domain Patient

---

#### Measurement related
Issues: #7, #9, #10, #11, #65, #41, #51, #38, #40, #123, 141

**Equivalent class** changed to snomed:363787002 (observable entity)

**New properties with domain sphn:Measurement:** 

 - has patient *op* 
 - precedes *op*
 
**Changed properties with domain sphn:Measurement:** 

 - has code *op* min 1 max 1
 - has medical device *op* min 1 max 1
 - has patient *op* min 1 max 1
 - has body site *op* min 0 max 1
 - has data determination *op* min 0 max 1
 - has lab test *op* min 0 max 1
 - has measurement method *op* min 0 max 1
 - has physiologic state *op* min 0 max 1
 - has qualitative result code *op* min 0 max 1
 - has quantity *op* min 1 (change in cardinality)
 - has reference range *op* min 0 max 1
 - has sample *op* min 0 max 1
 - has free text *dp* min 0 max 1

**New properties with range sphn:Measurement:**	

 - has measurement *op* - with domain Patient
 - interprets *op* - with domain Problem Condition
 - has member *op* - with domain Set

---

#### Procedure related
Issues: #21, #59, #82, #23, #141

**New properties with domain sphn:Procedure:** 

 - has patient *op* 
 - precedes *op*
 - using substance *op* - with ranges Product and Substance
 
**Changed properties with domain sphn:Procedure:** 

 - has status code *op* min 1 max 1 - with restriction of SNOMED codes some (385651009 or 385655000 or 385656004 or 385660001 or 410513005 or 410537005 or 410545000 or 723510000)
 - has datetime *dp* min 1 max 1
 - has start datetime *dp* min 0 max 1 (cardinality changed)
 - has free text *dp* min 0 max 1

**New properties with range sphn:Procedure:**	

 - has procedure *op* - with domain Patient


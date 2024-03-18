# AIDAVA-Reference-Ontology
AIDAVA Reference Ontology

The current working version of AIDAVA RO is based on SPHN schema but it has the following differences/changes: 

## Added: 

### Patient 
IRI 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/Patient

Description 	

Individual receiving health care services

Sub Class Of 	

    SPHN Concept c
    has administrative gender op max 1
    and has administrative gender op min 0
    has birth date op min 1
    and has birth date op max 1

In Domain Of 	

    has administrative gender op
    has birth date op
    has subject name op
    has adress dp

In Range Of 	has patient op
Restriction 	

    has subject name op min 1
    has adress dp min 0
    has identifier dp min 0 

### Product
IRI 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/Product 

Description : 
a pharmaceutical or biologic product

Sub Class Of 	

    SPHN Concept c
    has code op some
    and has code op max 1
    and has code op min 0 

### Subject Name

IRI 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/SubjectName

Description 	

Name of a human
Sub Class Of 	

    SPHN Concept c
    has family name dp min 0
    and has coding datetime dp max 1

In Domain Of 	

    has family name dp
    has given name dp

In Range Of 	has subject name op
Restriction 	has given name dp min 0 

### AIDAVA object properties 

IRI 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/AIDAVAobjectproperties

Super Property Of 	

    has administrative gender op
    has birth date op
    Condition code op
    has patient op
    has subject name op
    interprets op
    using substance op

#### hasAdministrativeGender
IRI 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/hasAdministrativeGender

Description 	

the gender of the individual used for administrative purposes

Sub Property Of 	AIDAVA object properties op

Domain 	Patient c

Range 	Administrative Gender 

#### hasBirthDate

IRI 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/hasBirthDate

Description 	

The date of birth for the individual

Sub Property Of 	AIDAVA object properties op

Domain 	Patient c
Range 	Birth Date 

#### hasConditionCode
IRI 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/hasConditionCode

Description 	

The code for a Condition class instance

Sub Property Of 	

    AIDAVA object properties op
    has code op

Domain 	Condition c

Range 	Code 

#### hasPatient 
IRI 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/hasPatient

Sub Property Of 	AIDAVA object properties op

Domain 	

Body Mass Index or Death Status or Cardiac Index or Biobanksample or Administrative Gender or Civil Status or FOPH Diagnosis or Allergy Episode or ICD-O Diagnosis or Tumor Grade or Body Weight or Adverse Event or Problem Condition or Tumor Specimen or Allergy or Electrocardiographic Procedure or Administrative Case or Diagnosis or Gestational Age At Birth or Death Date or Lab Result or Oncology Treatment Assessment or Sample or Tumor Stage or Oxygen Saturation or Respiratory Rate or Body Height or Body Temperature or Inhaled Oxygen Concentration or Radiotherapy Procedure or Access Device Presence or Measurement or Variant Descriptor or Birth Date or Drug Prescription or Simple Score or Body Surface Area or Circumference Measure or Diagnostic Radiologic Examination or Nursing Diagnosis or Drug Administration Event or Healthcare Encounter or Consent or TNM Classification or Data File or Body Position or Blood Pressure or Cardiac Output or FOPH Procedure or Procedure or Heart Rate c

Range 	Patient 

#### hasSubjectName 

IRI 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/hasSubjectName

Description 	

a name associated with the patient

Sub Property Of 	AIDAVA object properties op

Domain 	Patient c

Range 	Subject Name 
#### interprets 

IRI 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/interprets

Description 	

a relation between a clinical finding and an observable entity

Sub Property Of 	AIDAVA object properties op

Domain 	Problem Condition c

Range 	Measurement 

#### usingSubstance 

IRI 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/usingSubstance

Description 	

a relation between a procedure and substance or pharmaceutical / biologic product

Sub Property Of 	AIDAVA object properties op

Domain 	Procedure c

Range 	Product or Substance 

### AIDAVA data properties

IRI 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/AIDAVADataProperties

Super Property Of 	

    has adress dp
    has family name dp
    has given name dp

#### hasAdress

IRI 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/hasAdress
Description 	

an address for the individual

Sub Property Of 	AIDAVA data properties dp

Domain 	Patient c

Range 	xsd:string

#### hasFamilyName

IRI 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/hasFamilyName
Description 	

family name (often called 'Surname')

Sub Property Of 	AIDAVA data properties dp

Domain 	Subject Name c

Range 	xsd:string

#### hasGivenName 

IRI 	https://biomedit.ch/rdf/sphn-ontology/AIDAVA/hasGivenName
Description 	

given names (not always 'first'), includes middle names

Sub Property Of 	AIDAVA data properties dp

Domain 	Subject Name c

Range 	xsd:string


## Changed 
### Measurement
sphn:Measurement Equivalentclass http://snomed.info/id/363787002

Multiple properties are added

### Procedure 
Multiple properties are added

### ProblemCondition 
Multiple properties are added

### hasBodySite
IRI 	https://biomedit.ch/rdf/sphn-ontology/sphn#hasBodySite

Description 	

body site where the concept was measured, performed or collected
Sub Property Of 	SPHN attribute object op

Super Property Of 	

    has insertion point op
    has manifestation body site op
    has progression body site op
    has resting point op

Domain 	

Circumference Measure or Body Temperature or Heart Rate or Allergy Episode or Blood Pressure or Diagnosis or Diagnostic Radiologic Examination or Access Device Presence or Electrocardiographic Procedure or Procedure or FOPH Procedure or Problem Condition or Oncology Treatment Assessment or Oxygen Saturation or Measurement or Tumor Specimen or Sample or Radiotherapy Procedure c

Range 	Body Site 

### hasCode
Domain 	
Cardiac Output or Body Site or Data File or Electrocardiographic Procedure or Measurement or Data Provider Institute or Chromosome or Drug or Heart Rate or Transcript or Body Position or Adverse Event or Drug Administration Event or Simple Score or Pharmaceutical Dose Form or Radiotherapy Procedure or Tumor Stage or Data Determination or Civil Status or Medical Device or Diagnosis or Time Pattern or Drug Prescription or Physiologic State or FOPH Diagnosis or Organism or Unit or Allergy Episode or Intent or Lab Result or Substance or Administrative Gender or Gene or Laterality or Care Handling or Cardiac Index or Consent or Protein or Product or Measurement Method or Problem Condition or Variant Descriptor or Sample or Allergy or Death Status or Location or Diagnostic Radiologic Examination or Lab Analyzer or Lab Test or FOPH Procedure or Oncology Treatment Assessment or ICD-O Diagnosis or Reference or Nursing Diagnosis or Tumor Grade or Tumor Specimen or Procedure or Allergen or Chromosomal Location 

## Deprecated
OncologyDiagnosis
BloodPressure
BodyHeight
BodyTemperature
BodyWeight
CardiacOutput
CircumferenceMeasure
Diagnosis
FOPH Diagnosis
Heart Rate
Inhaled Oxygen Concentration
Lab Result
Nursing Diagnosis
Oxygen Saturation
Systemic Arterial Blood Pressure 

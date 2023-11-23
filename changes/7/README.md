# 7

## Issue Overview

The current mapping process within the SPHN encounters a issue when dealing with Blood Pressure measurements due to the absence of IF-THEN-ELSE rules support in our mapping tool.

## Problem Statement

When mapping a JSON file to SPHN, the differentiation between types of Blood Pressure (such as systolic and diastolic pressure) requires forming distinct relations in SPHN: hasSystolicPressure and hasDiastolicPressure. However, achieving this differentiation requires a conditional value check. Depending on this value, the appropriate SPHN relation should be created (either hasSystolicPressure or hasDiastolicPressure). Unfortunately, our current mapping tool lacks the capability to execute IF-THEN-ELSE-based mappings. We need to re-design SPHN Measurement Class to handle this mapping.

## Example Scenario

For instance, consider the following JSON-to-SPHN mapping scenario:

```json
"entry": [
     {
         "fullUrl": "http://nictiz2.wildfhir.org/fhir3-0-2-i2/Observation/gpdata-observation-contact01-bpdiastolic",
         "resource": {
             "resourceType": "Observation",
             "id": "gpdata-observation-contact01-bpdiastolic",
             "meta": {
                 "versionId": "1",
                 "lastUpdated": "2022-07-05T06:30:39.272-04:00",
                 "profile": [
                     "http://nictiz.nl/fhir/StructureDefinition/gp-DiagnosticResult"
                 ]
             },     
            "code": {
                 "coding": [
                     {
                         "system": "https://referentiemodel.nhg.org/tabellen/nhg-tabel-45-diagnostische-bepalingen",
                         "code": "1740",
                         "display": "diastolische bloeddruk"
                     },
                     {
                         "system": "http://loinc.org",
                         "code": "8462-4",
                         "display": "Diastolic blood pressure"
                     }
                 ]
             },
```

In SPHN, this JSON should ideally map to `hasDiastolicPressure` due to the `type` indicating a diastolic blood pressure reading. However, our mapping tool doesn't provide the functionality to dynamically select between `hasSystolicPressure` or `hasDiastolicPressure` based on such conditions.

## Proposed Approach
The proposed approach involves establishing a connection between the `sphn:Measurement` entity and the `sphn:Code` class using the `hasCode` relation. This way, diverse types of measurements, including but not limited to systolic and diastolic pressures, can be accurately represented under the broader `sphn:Measurement` category with associated codes.
By removing specific relations for individual measurement types, it will enable the simplification of the ontology, facilitate mapping.

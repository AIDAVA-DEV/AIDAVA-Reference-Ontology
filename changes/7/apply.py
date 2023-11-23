from rdflib import Graph


def apply(graph: Graph) -> Graph:
    # delete restriction on sphn:hasSystolicPressure
    delete_query = """
        PREFIX sphn: <https://biomedit.ch/rdf/sphn-ontology/sphn#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#> 
        DELETE {         
            ?s owl:onProperty sphn:hasSystolicPressure .
            ?s ?sp ?so .
        }
        WHERE {
            ?s owl:onProperty sphn:hasSystolicPressure .
            ?s ?sp ?so .
        
        }
    """

    # Execute the DELETE query
    graph.update(delete_query)

    # delete property definitions for sphn:hasSystolicPressure
    delete_query = """
        PREFIX sphn: <https://biomedit.ch/rdf/sphn-ontology/sphn#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#> 
        DELETE {         
            sphn:hasSystolicPressure ?sp ?so .
        }
        WHERE {
            sphn:hasSystolicPressure ?sp ?so .
        
        }
    """

    # Execute the DELETE query
    graph.update(delete_query)

    # delete restriction on sphn:hasDiastolicPressure
    delete_query = """
        PREFIX sphn: <https://biomedit.ch/rdf/sphn-ontology/sphn#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#> 
        DELETE {         
            ?s owl:onProperty sphn:hasDiastolicPressure .
            ?s ?sp ?so .
        }
        WHERE {
            ?s owl:onProperty sphn:hasDiastolicPressure .
            ?s ?sp ?so .
        
        }
    """

    # Execute the DELETE query
    graph.update(delete_query)

    # delete property definitions for sphn:hasDiastolicPressure
    delete_query = """
        PREFIX sphn: <https://biomedit.ch/rdf/sphn-ontology/sphn#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#> 
        DELETE {         
            sphn:hasDiastolicPressure ?sp ?so .
        }
        WHERE {
            sphn:hasDiastolicPressure ?sp ?so .
        
        }
    """

    # Execute the DELETE query
    graph.update(delete_query)

    # hasCode
    # TODO: this is not working
    # update_query = """
    #     PREFIX sphn: <https://biomedit.ch/rdf/sphn-ontology/sphn#>
    #     PREFIX owl: <http://www.w3.org/2002/07/owl#>
    #     INSERT DATA {
    #         sphn:Measurement rdfs:subClassOf
    #         [ a owl:Class ;
    #             owl:intersectionOf ( [ owl:intersectionOf ( [ a owl:Restriction ;
    #                         owl:minCardinality "0"^^xsd:nonNegativeInteger ;
    #                         owl:onProperty sphn:hasCode ] [ a owl:Restriction ;
    #                         owl:maxCardinality "1"^^xsd:nonNegativeInteger ;
    #                         owl:onProperty sphn:hasCode ] ) ]
    #     }
    # """

    # # Execute the DELETE query
    # graph.update(delete_query)

    return graph

# sparqlvoc

A RDF-based vocabulary to model SPARQL queries into RDF. Sparqlvoc offers OWL-classes, properties and SHACL shapes, with which SPARQL queries can be represented, queried, generated, validated, analysed, transformed and reused. With Sparqlvoc SPARQL queries themselves become semantic objects worthy of inspection.

# Status

Highly unstable & unfinished. Work in progress.

# Simple example

```
BASE <https:example.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT *
WHERE {?s ?p ?o;
 .}
```

Modeled as:

```
prefix ex: <https://www.example.org/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix sparql: <http://www.w3.org/ns/sparql#model/def/>
 
ex:exampleQuery 
                rdf:type sparql:QueryUnit;
                rdf:_1 ex:prologue;
                rdf:_2 ex:selectQuery.
                
ex:prologue 
                rdf:type sparql:Prologue;
                rdf:_1 ex:baseDecl;
                rdf:_2 ex:prefixDecl.
               
ex:baseDecl 
                rdf:type sparql:BaseDecl;
                rdf:_1 ex:base;              
                rdf:_2 ex:iriRefBase.

ex:base
                rdf:type sparql:Base.

ex:iriRefBase 
                rdf:type sparql:IRIRef;
                rdf:value "https:example.org/".
                
ex:prefixDecl    
                rdf:type sparql:PrefixDecl;
                rdf:_1 ex:prefix;
                rdf:_2 ex:pname_NS;
                rdf:_3 ex:iriRef_RDF.

ex:prefix
                rdf:type sparql:Prefix.

ex:pname_NS   
                rdf:type sparql:PNAME_NS;
                rdf:_1 ex:prefix_RDF;
                rdf:_2 ex:colon.
                
ex:prefix_RDF 
                rdf:type sparql:PN_PREFIX;
                rdf:value "rdf".

ex:colon
                rdf:type sparql:Colon.
                
ex:iriRef_RDF 
                rdf:type sparql:IRIRef;
                rdf:value "http://www.w3.org/1999/02/22-rdf-syntax-ns#".
               
ex:selectQuery
                rdf:type sparql:SelectQuery;
                rdf:_1 ex:selectClause1;
                rdf:_2 ex:whereClause1.
                
ex:selectClause1
                rdf:type sparql:SelectClause;
                rdf:_1 ex:select;
                rdf:_2 ex:wildcard.

ex:select
                rdf:type sparql:Select.
                
ex:wildcard 
                rdf:type sparql:Wildcard.

ex:whereClause1 
                rdf:type sparql:WhereClause;
                rdf:_1 ex:where;
                rdf:_2 ex:groupGraphPattern.

ex:where
                rdf:type sparql:Where.

ex:groupGraphPattern
                rdf:type sparql:GroupGraphPattern;
                rdf:_1 ex:openCurlyBracket ;
                rdf:_2 ex:groupGraphPatternSub ;
                rdf:_3 ex:closedCurlyBracket.

ex:openCurlyBracket 
                rdf:type sparql:OpenCurlyBracket.

ex:closedCurlyBracket
                rdf:type sparql:ClosedCurlyBracket.
                
ex:groupGraphPatternSub
                rdf:type sparql:GroupGraphPatternSub;
                rdf:_1 ex:triplesBlock.
                
ex:triplesBlock
                rdf:type sparql:TriplesBlock;
                rdf:_1 ex:triplesSameSubjectPath.

ex:triplesSameSubjectPath
                rdf:type sparql:TriplesSameSubjectPath;
                rdf:_1 ex:varOrTerm1;
                rdf:_2 ex:propertyListPathNotEmpty.
                
ex:varOrTerm1
                rdf:type sparql:VarOrTerm;
                rdf:_1 ex:variable_s.

ex:variable_s
                rdf:type sparql:Variable1;
                rdf:value 's'.
                
ex:propertyListPathNotEmpty
                rdf:type sparql:PropertyListPathNotEmpty;
                rdf:_1 ex:verbSimple;
                rdf:_2 ex:objectListPath.

ex:verbSimple 
                rdf:type sparql:VerbSimple;
                rdf:_1 ex:variable_p.

ex:variable_p
                rdf:type sparql:Variable1;
                rdf:value 'p'.                

ex:objectListPath
                rdf:type sparql:ObjectListPath;
                rdf:_1 ex:objectPath.

ex:objectPath
                rdf:type sparql:ObjectPath;
                rdf:_1 ex:graphNodePath.

ex:graphNodePath 
                rdf:type sparql:GraphNodePath;
                rdf:_1 ex:varOrTerm2.
                
ex:varOrTerm2
                rdf:type sparql:VarOrTerm;
                rdf:_1 ex:variable_o.

ex:variable_o
                rdf:type sparql:Variable1;
                rdf:value 'o'.

```


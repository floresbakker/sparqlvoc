# sparqlvoc

A RDF-based vocabulary to model SPARQL queries into RDF. Sparqlvoc offers OWL-classes, properties and SHACL shapes, with which SPARQL queries can be represented, queried, generated, validated, analysed, transformed and reused. With Sparqlvoc SPARQL queries themselves become semantic objects worthy of inspection.

The vocabulary models the SPARQL query language as an abstract syntax tree, consisting of the following nodes in a tree:

- tree
  - node
    - non-terminal node
    - terminal node
        - keyword
        - symbol
        - symbol sequence
        - character sequence

As a source for the model we use the grammar from the SPARQL 1.1 specification: https://www.w3.org/TR/sparql11-query/#grammar.

Sparqlvoc offers five algorithms captured in five SHACL nodeshapes to generate an actual SPARQL query based on its RDF-based abstract syntax tree. These five algorithms align with the above mentioned model of the abstract syntax tree and its components.

1. shp:NonTerminalNode
2. shp:Keyword
3. shp:Symbol
4. shp:SymbolSequence
5. shp:CharacterSequence

# Status

Highly unstable & unfinished. Work in progress.

# Simple example

```
BASE <https:example.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT *
WHERE { ?s ?p ?o }
```

Modeled as:

```
prefix ex: <https://www.example.org/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix sparql: <http://www.w3.org/ns/sparql#model/def/>

ex:exampleQueryTree
                rdf:type sparql:AbstractSyntaxTree;
                rdf:_1   ex:exampleQuery.

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
                rdf:_1 ex:lessThan;
                rdf:_2 ex:iriValue_Base;
                rdf:_3 ex:greaterThan.

ex:lessThan
                rdf:type sparql:LessThan.

ex:greaterThan
                rdf:type sparql:GreaterThan.
                              
ex:iriValue_Base
                rdf:type sparql:IRIValue;
                rdf:value "https://example.org/".
                
ex:prefixDecl    
                rdf:type sparql:PrefixDecl;
                rdf:_1 ex:prefix;
                rdf:_2 ex:pname_NS;
                rdf:_3 ex:iriRef_RDF.

ex:prefix
                rdf:type sparql:Prefix.

ex:pname_NS   
                rdf:type sparql:PNAME_NS;
                rdf:_1 ex:pn_prefix_RDF;
                rdf:_2 ex:colon.
                
ex:pn_prefix_RDF 
                rdf:type sparql:PN_PREFIX;
                rdf:_1 ex:pn_chars_base_RDF.
                

ex:pn_chars_base_RDF
                rdf:type sparql:PN_CHARS_BASE;
                rdf:value "rdf".

ex:colon
                rdf:type sparql:Colon.
                
ex:iriRef_RDF 
                rdf:type sparql:IRIRef;
                rdf:_1 ex:lessThan;
                rdf:_2 ex:iriValue_RDF;
                rdf:_3 ex:greaterThan.

ex:iriValue_RDF
                rdf:type sparql:IRIValue;
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
                rdf:type sparql:Variable;
                rdf:_1 ex:variable1_s.

ex:variable1_s                
                rdf:type sparql:Variable1;
                rdf:_1 ex:questionMark;
                rdf:_2 ex:variable1_s_name.

ex:questionMark
                rdf:type sparql:QuestionMark.

ex:variable1_s_name 
                rdf:type sparql:CharacterSequence;
                rdf:value 's'.
                
ex:propertyListPathNotEmpty
                rdf:type sparql:PropertyListPathNotEmpty;
                rdf:_1 ex:verbSimple;
                rdf:_2 ex:objectListPath.

ex:verbSimple 
                rdf:type sparql:VerbSimple;
                rdf:_1 ex:variable_p.

ex:variable_p
                rdf:type sparql:Variable;
                rdf:_1 ex:variable1_p.                    

ex:variable1_p
                rdf:type sparql:Variable1;
                rdf:_1 ex:questionMark;
                rdf:_2 ex:variable1_p_name.  
                
ex:variable1_p_name 
                rdf:type sparql:CharacterSequence;
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
                rdf:type sparql:Variable;
                rdf:_1 ex:variable1_o.

ex:variable1_o
                rdf:type sparql:Variable1;
                rdf:_1 ex:questionMark;
                rdf:_2 ex:variable1_o_name.                   

ex:variable1_o_name 
                rdf:type sparql:CharacterSequence;
                rdf:value 'o'.                   
```

# Extended example - Filter clause

```
BASE <https://example.org/> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
SELECT * WHERE { ?s ?p ?o 
FILTER ( ?s = ?o ) }
```

This example makes use, through the FILTER keyword, of the expressions component in SPARQL. 

This is modeled as:

```
prefix ex: <https://www.example.org/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix sparql: <http://www.w3.org/ns/sparql#model/def/>

ex:exampleQueryTree
                rdf:type sparql:AbstractSyntaxTree;
                rdf:_1   ex:exampleQuery.

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
                rdf:_1 ex:lessThan;
                rdf:_2 ex:iriValue_Base;
                rdf:_3 ex:greaterThan.

ex:lessThan
                rdf:type sparql:LessThan.

ex:greaterThan
                rdf:type sparql:GreaterThan.
                              
ex:iriValue_Base
                rdf:type sparql:IRIValue;
                rdf:value "https://example.org/".
                
ex:prefixDecl    
                rdf:type sparql:PrefixDecl;
                rdf:_1 ex:prefix;
                rdf:_2 ex:pname_NS;
                rdf:_3 ex:iriRef_RDF.

ex:prefix
                rdf:type sparql:Prefix.

ex:pname_NS   
                rdf:type sparql:PNAME_NS;
                rdf:_1 ex:pn_prefix_RDF;
                rdf:_2 ex:colon.
                
ex:pn_prefix_RDF 
                rdf:type sparql:PN_PREFIX;
                rdf:_1 ex:pn_chars_base_RDF.
                
ex:pn_chars_base_RDF
                rdf:type sparql:PN_CHARS_BASE;
                rdf:value "rdf".

ex:colon
                rdf:type sparql:Colon.
                
ex:iriRef_RDF 
                rdf:type sparql:IRIRef;
                rdf:_1 ex:lessThan;
                rdf:_2 ex:iriValue_RDF;
                rdf:_3 ex:greaterThan.

ex:iriValue_RDF
                rdf:type sparql:IRIValue;
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
                rdf:_3 ex:graphPatternNotTriples;
                rdf:_4 ex:closedCurlyBracket.

ex:openCurlyBracket 
                rdf:type sparql:OpenCurlyBracket.

ex:closedCurlyBracket
                rdf:type sparql:ClosedCurlyBracket.
                
ex:groupGraphPatternSub
                rdf:type sparql:GroupGraphPatternSub;
                rdf:_1 ex:triplesBlock.

ex:graphPatternNotTriples
                rdf:type sparql:GraphPatternNotTriples;
                rdf:_1 ex:filterClause.

ex:filterClause
                rdf:type sparql:FilterClause;
                rdf:_1 ex:filter;
                rdf:_2 ex:constraint.

ex:filter
                rdf:type sparql:Filter.
                
ex:constraint
                rdf:type sparql:Constraint;
                rdf:_1 ex:brackettedExpression.

ex:brackettedExpression
                rdf:type sparql:BrackettedExpression;
                rdf:_1 ex:openParenthesis;
                rdf:_2 ex:expression;
                rdf:_3 ex:closedParenthesis.

ex:openParenthesis
                rdf:type sparql:OpenParenthesis.
                
ex:closedParenthesis
                rdf:type sparql:ClosedParenthesis.

ex:expression
                rdf:type sparql:Expression;
                rdf:_1 ex:conditionalOrExpression.

ex:conditionalOrExpression
                rdf:type sparql:ConditionalOrExpression;
                rdf:_1 ex:conditionalAndExpression.

ex:conditionalAndExpression
                rdf:type sparql:ConditionalAndExpression;
                rdf:_1 ex:valueLogical.
                
ex:valueLogical
                rdf:type sparql:ValueLogical;
                rdf:_1 ex:relationalExpression.
                
ex:relationalExpression
                rdf:type sparql:RelationalExpression;
                rdf:_1 ex:numericExpression1;
                rdf:_2 ex:equal;
                rdf:_3 ex:numericExpression2.

ex:numericExpression1
                rdf:type sparql:NumericExpression;
                rdf:_1 ex:additiveExpression1.

ex:additiveExpression1
                rdf:type sparql:AdditiveExpression;
                rdf:_1 ex:multiplicativeExpression1.

ex:multiplicativeExpression1
                rdf:type sparql:MultiplicativeExpression;
                rdf:_1 ex:unaryExpression1.

ex:unaryExpression1
                rdf:type sparql:UnaryExpression;
                rdf:_1 ex:primaryExpression1.

ex:primaryExpression1
                rdf:type sparql:PrimaryExpression;
                rdf:_1 ex:variable_s.

ex:equal
                rdf:type sparql:Equal.

ex:numericExpression2
                rdf:type sparql:NumericExpression;
                rdf:_2 ex:additiveExpression2.

ex:additiveExpression2
                rdf:type sparql:AdditiveExpression;
                rdf:_2 ex:multiplicativeExpression2.

ex:multiplicativeExpression2
                rdf:type sparql:MultiplicativeExpression;
                rdf:_2 ex:unaryExpression2.

ex:unaryExpression2
                rdf:type sparql:UnaryExpression;
                rdf:_2 ex:primaryExpression2.

ex:primaryExpression2
                rdf:type sparql:PrimaryExpression;
                rdf:_2 ex:variable_o.
                
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
                rdf:type sparql:Variable;
                rdf:_1 ex:variable1_s.

ex:variable1_s                
                rdf:type sparql:Variable1;
                rdf:_1 ex:questionMark;
                rdf:_2 ex:variable1_s_name.

ex:questionMark
                rdf:type sparql:QuestionMark.

ex:variable1_s_name 
                rdf:type sparql:CharacterSequence;
                rdf:value 's'.
                
ex:propertyListPathNotEmpty
                rdf:type sparql:PropertyListPathNotEmpty;
                rdf:_1 ex:verbSimple;
                rdf:_2 ex:objectListPath.

ex:verbSimple 
                rdf:type sparql:VerbSimple;
                rdf:_1 ex:variable_p.

ex:variable_p
                rdf:type sparql:Variable;
                rdf:_1 ex:variable1_p.                    

ex:variable1_p
                rdf:type sparql:Variable1;
                rdf:_1 ex:questionMark;
                rdf:_2 ex:variable1_p_name. 
 
ex:variable1_p_name 
                rdf:type sparql:CharacterSequence;
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
                rdf:type sparql:Variable;
                rdf:_1 ex:variable1_o.

ex:variable1_o
                rdf:type sparql:Variable1;
                rdf:_1 ex:questionMark;
                rdf:_2 ex:variable1_o_name.     
                   
ex:variable1_o_name 
                rdf:type sparql:CharacterSequence;
                rdf:value 'o'.                         
```
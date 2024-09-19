# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 18:40:53 2023

@author: Flores Bakker

The SPARQL Vocabulary.



Usage: 

1. Place an arbitrary ontology (as turtle file *.ttl) in the input folder.
2. In the command prompt, run 'python sparqlvoc.py'
3. Go to the output folder and grab your enriched turtle file, now including SPARQL fragments.


"""
import os
import pyshacl
import rdflib 
from rdflib import Namespace

# Get the current working directory in which the Ontosparql.py file is located.
current_dir = os.getcwd()

# Set the path to the desired standard directory. 
directory_path = os.path.abspath(os.path.join(current_dir, '..'))

# namespace declaration
sparql = Namespace("http://www.w3.org/ns/sparql#model/def/")

# Function to read a graph (as a string) from a file 
def readGraphFromFile(file_path):
    # Open each file in read mode
    with open(file_path, 'r', encoding='utf-8') as file:
            # Read the content of the file and append it to the existing string
            file_content = file.read()
    return file_content

# Function to write a graph to a file
def writeGraph(graph):
    graph.serialize(destination=directory_path+"/sparqlvoc/Tools/Output/"+filename_stem+"-sparql.ttl", format="turtle")

# Function to call the PyShacl engine so that a RDF model of an HTML document can be serialized to HTML-code.
def iteratePyShacl(sparql_generator, serializable_graph):
        
        # call PyShacl engine and apply the SPARQL vocabulary to the serializable SPARQL model
        pyshacl.validate(
        data_graph=serializable_graph,
        shacl_graph=sparql_generator,
        data_graph_format="turtle",
        shacl_graph_format="turtle",
        advanced=True,
        inplace=True,
        inference=None,
        iterate_rules=False, #rather than setting this to true, it is better to do the iteration in the script as PyShacl seems to have some buggy behavior around iteration.
        debug=False,
        )
        
       
        statusquery = serializable_graph.query('''
            
prefix sparql: <http://www.w3.org/ns/sparql#model/def/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

ASK
WHERE 
  # 
  {
  ?query rdf:type sparql:QueryUnit;
        sparql:fragment [].
}
        ''')   

        resultquery = serializable_graph.query('''
            
prefix sparql: <http://www.w3.org/ns/sparql#model/def/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?sparql_fragment
WHERE {
  ?query rdf:type sparql:QueryUnit;
         sparql:fragment ?sparql_fragment.
  
}

        ''')   

        # Check whether another iteration is needed. If every OWL and RDFS construct contains a sparql:syntax statement, the processing is considered done.
        for status in statusquery:
            print ('status = ', status)
            if status == False:
                writeGraph(serializable_graph)
                iteratePyShacl(sparql_generator, serializable_graph)
            else: 
                 print ("File " + filename_stem+"-sparql.ttl" + " created in output folder.")
                 writeGraph(serializable_graph)
        
                 for result in resultquery:
                    sparql_fragment = result["sparql_fragment"]
                    output_file_path = directory_path+"/sparqlvoc/Tools/Output/"+filename_stem+".rq"
                    
                    # Write the HTML content to the output file
                    with open(output_file_path, "w", encoding="utf-8") as file:
                        file.write(sparql_fragment)
                    print ("File " + filename_stem+".rq" + " created in output folder.")

                 
# loop through any turtle files in the input directory
for filename in os.listdir(directory_path+"/sparqlvoc/Tools/Input"):
    if filename.endswith(".ttl"):
        file_path = os.path.join(directory_path+"/sparqlvoc/Tools/Input", filename)
        
        # Establish the stem of the file name for reuse in newly created files
        filename_stem = os.path.splitext(filename)[0]
        
        # Get the SPARQL vocabulary and place it in a string
        sparql_generator = readGraphFromFile(directory_path+"/sparqlvoc/Specification/sparqlvoc - core.ttl")
        
        # Get some SPARQL code represented in triples
        sparql_query_string = readGraphFromFile(file_path)    + sparql_generator
        
        # Create a graph of the string consisting of the manchester syntax and the ontology to be transformed 
        serializable_graph = rdflib.Graph().parse(data=sparql_query_string , format="ttl")
        serializable_graph.bind("sparql", sparql)
                        
        # Inform user
        print ('\nCreating sparql fragments for file',filename, '...')
        
        # Call the shacl engine with the SPARQL vocabulary
        iteratePyShacl(sparql_generator, serializable_graph)
        
        # Inform user
        print ('Done.')

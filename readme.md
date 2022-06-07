Binary Serialization/DeSerialization Library from Scratch! 

(with custom bytecode format **ACODE**)

I created a custom byte format called A-code. 


**Notes**:

1. This goal of this library is to serialize and deserialize python dictionaries
2. This library only deals with self-contained dictionaries which do not point to other items in the memory
3. Thus A-Code consists of only rules for basic data types currently

The Read/write pair rules are defined as follows

UTF-8	      |      Code
----------- |    -----------   
Preprocessor(A-Code) 	    |        \AA
int           |      \Ai
float         |      \Af
char	        |      \Ac
string	      |      \As
eof	          |      \A00
Normal characters	 |  [datatype][Ascii]


Serialization Algorithm:

Output format after serializing

[k,v," ",k,[k,v,"",k,v,""], k,[v1,v2,v3,v4]]

\AA \Asx\AsAditya \Asy\Ad\Asa\Ai1 \Asz\Ai3 \A00

Steps:

Serialization (Converting into Code)

1. The first characters should mark the custom protocol for our identification
2. The final characters should contain eof code
3. Dump each item in the dictionary as single item in code with format of keys and values as [type][data]
4. Each item of dictionary should be seperated with space in A-Code

DeSerialisation (Creating Dictionary from Code) 

1. While reading the Code, split the code into seperate items 
2. Split each item into key and value. 
3. identify key (value and datatype)
4. identify value (value and datatype)
5. Create a new Resultant Dictionary Object and dump those keys and values in the new dictionary.
6. The Error Handling for Invalid Code format is present in the function itself.
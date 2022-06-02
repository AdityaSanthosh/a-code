Binary Serialization/DeSerialization Library from Scratch! (with custom bytecode format)

IN PROGRESS

I created a custom byte format called A-code. 

The Read/write pair rules for it are defined as follows

Elemental Data

1. Int
2. Float
3. String
4. Char
5. EmptySpace

Data Structures

1. Lists
2. Dictionary

Goal 1: Reconstruct Dicts

A-Code Table:

ASCII	            Code

A-Code	            \AA
{	                \0Ds
}	                \0De
Empty space	        \0a
' / char	        \0c
“ / string	        \0s
: (end of key)	    \0eok
, (end of item)	    \0eoi
eof	                \00
Normal characters	Ascii format

Steps:

Serialisation (Converting into Code)

1. The first character should mark the custom protocol for our identification
2. Know if the character is an empty space. If yes. Disregard it. 
3. Know if the character starts an object. Now it needs to be enclosed. If not throw an InvalidInputFormat Error
    1. If the character is ‘  It starts a Char. 
    2. If it is “ it starts a string. 
    3.  If it is { it starts a dict. 
    4. It it is [ it starts a list.
4. We also need to identify separate each code frame while deserialising. So we will use empty space character between each token while serialisation

For large Files, We need to Divide them into batches of small sizes and serialise them. 

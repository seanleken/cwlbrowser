grammar cwl;

//PARSER
main_file           : '#!/usr/bin/env cwl-runner'  NL version NL ('$graph:' NL)? (workflow|tool)+ EOF;
workflow            :identification?  'class: Workflow' NL 
                     (label NL| doc NL| requirements | description| inputs|outputs|steps|hints)+;
tool                : identification? class_ NL
                     (inputs | baseCommand | stdin_ | stdout_ | outputs)+;
label               : 'label:' (STRING|name) ;
doc                 : 'doc:' (STRING|name) ;
description         : 'description:' (STRING | name)NL?;
inputs              : 'inputs:' ('[]' NL | NL input_+);
outputs             : 'outputs:' ('[]' NL | NL output+);
steps               : 'steps:' NL step+;
step                : name ':' NL run (in_ | out_)+;
in_                 : 'in:' ('[]' NL? | '['WORD']' NL? | NL in_or_out+);
out_                : 'out:' ('[]' NL? | '['WORD']' NL?| NL  in_or_out+);
in_or_out           : (identification | name ':') ((NL |'{')
                      (type_|doc|default|secondaryFiles)+ (NL?|'}') | array) NL?;
run                 : 'run:' (NL tool | STRING NL);
input_              : (identification | name ':') NL (type_ NL? | doc NL?|
                     default NL? | source | label NL? |inputBinding | description|secondaryFiles)+;
output              : (identification | name ':' NL) (doc NL? |
                      default | source | label NL | outputSource | outputBinding | type_ NL | description)+;
source              : 'source:' STRING NL;
name                : (WORD|NUMBER)+;
type_               : 'type:' name ;
tag                 : '"#' WORD '"';
inputBinding        : 'inputBinding:' (NL (position |prefix|glob)+ | '{}' NL);
outputBinding       : 'outputBinding:' (NL (position |prefix| glob)+ | '{}' NL); 
position            : 'position:' NUMBER NL;
prefix              : 'prefix:' STRING  NL;
identification      : '-'? 'id:' (STRING | name) NL;
outputSource        : 'outputSource:' name NL;
class_              : '-'? 'class:' ('Workflow' | 'CommandLineTool' | name);
baseCommand         : 'baseCommand:' name NL arguments?;
stdin_              : 'stdin:' WORD NL;
glob                : 'glob:' '$('name')' NL;
arguments           : 'arguments:' NL argument+;
argument            : '-'? STRING NL;
stdout_              : 'stdout:' WORD NL;
requirements        : 'requirements:' NL class_  NL;
array               : '[' (name ','?)+ ']';
default             : 'default:' NL? (STRING  | file_);
file_                : '-'? '{'?  'class: File' (','| NL) 
                      (location (NL?|','?)|secondaryFiles NL?)+ '}'?;
location            :  'location:' (name | STRING);
secondaryFiles      : '-'? 'secondaryFiles:' NL '-'? (file_ | STRING NL?);
version             : 'cwlVersion:' 'v1.0';
hints               : 'hints:' NL name NL?;

//LEXER
WORD                : ('A'..'Z'|'a'..'z'|'/'|'.'|'-'|'_'|'['|']'|'('|')'|'?')+;
STRING              : '"' .*? '"';
NUMBER              : [0-9]+;
NL                  : '\n'+;
WHITESPACE          : ' ' -> skip ;

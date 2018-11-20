grammar cwl;

//PARSER
main_file           : '#!/usr/bin/env cwl-runner'  NL version NL ('$graph:' NL)? (workflow|tool)+ EOF;
workflow            :identification?  'class: Workflow' NL 
                     (label NL| doc NL| requirements | description| inputs|outputs|steps|hints)+;
tool                : identification? class_ NL
                     (inputs | baseCommand | stdin_ | stdout_ | outputs| stderr_)+;
label               : 'label:' (STRING|word) ;
doc                 : 'doc:' (STRING|word) ;
description         : 'description:' (STRING | word)NL?;
inputs              : 'inputs:' ('[]' NL | NL input_+);
outputs             : 'outputs:' ('[]' NL | NL output+);
steps               : 'steps:' NL step+;
step                : word ':' NL run (in_ | out_)+;
in_                 : 'in:' ('[]' NL? | array NL? | NL in_or_out+);
out_                : 'out:' ('[]' NL? | array NL?| NL  in_or_out+);
in_or_out           : (identification | word ':') ((NL |'{')?
                      (type_|doc|default|secondaryFiles| word)+ (NL|'}')? | array) NL?;
run                 : 'run:' (NL tool | STRING NL | word NL);
input_              : (identification | word ':') NL (type_ NL? | doc NL?|
                     default NL? | source | label NL? |inputBinding | description|secondaryFiles)+;
output              : (identification | word ':' NL) (doc NL? |
                      default | source | label NL | outputSource | outputBinding | type_ NL | description)+;
source              : 'source:' STRING NL;
word                : (CHAR|NUMBER)+;
type_               : 'type:' word ;
tag                 : '"#' CHAR '"';
inputBinding        : 'inputBinding:' (NL (position |prefix|glob|separate)+ | '{}' NL);
separate            : 'separate:' word;
outputBinding       : 'outputBinding:' (NL (position |prefix| glob)+ | '{}' NL); 
position            : 'position:' NUMBER NL;
prefix              : 'prefix:' STRING  NL;
identification      : '-'? 'id:' (STRING | word) NL;
outputSource        : 'outputSource:' word NL;
class_              : '-'? 'class:' ('Workflow' | 'CommandLineTool' | word);
baseCommand         : 'baseCommand:' word NL arguments?;
stdin_              : 'stdin:' word NL;
glob                : 'glob:' '$('? word ')'? NL;
arguments           : 'arguments:' NL argument+;
dockerrequirement   : 'DockerRequirement:' NL dockerpull;
dockerpull          : 'dockerPull:' word NL;
argument            : '-'? STRING NL;
stdout_              : 'stdout:' word NL;
stderr_             : 'stderr:' word NL;
requirements        : 'requirements:' NL class_  NL;
array               : '['? (word ','?)+ ']'?;
default             : 'default:' NL? (STRING  | file_);
file_                : '-'? '{'?  'class: File' (','| NL) 
                      (location (NL?|','?)|secondaryFiles NL?)+ '}'?;
location            :  'location:' (word | STRING);
secondaryFiles      : '-'? 'secondaryFiles:' NL? '-'? (file_ | STRING NL?| word NL?);
version             : 'cwlVersion:' 'v1.0';
hints               : 'hints:' NL dockerrequirement;

//LEXER
CHAR                : ('A'..'Z'|'a'..'z'|'/'|'.'|'-'| '_' | '[' | ']' |'('|')'|'?')+;
STRING              : '"' .*? '"';
LETTER              : ('A'..'Z'|'a'..'z')+;
NUMBER              : [0-9]+;
NL                  : '\n'+;
WHITESPACE          : ' ' -> skip ;

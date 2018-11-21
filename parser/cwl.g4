grammar cwl;

//PARSER
main_file           : '#!/usr/bin/env cwl-runner'   version  ('$graph:' )? (workflow|tool)+ EOF;
workflow            :identification?  'class: Workflow'  
                     (label | doc | requirements | description| inputs|outputs|steps|hints)+;
tool                : identification? class_ 
                     (inputs | baseCommand | stdin_ | stdout_ | outputs| stderr_)+;
label               : 'label:' (STRING|word) ;
doc                 : 'doc:' (STRING|word) ;
description         : 'description:' (STRING | word);
in_                 : 'in:' (word  |  in_or_out+);
out_                : 'out:' (word  |   in_or_out+);
inputs              : 'inputs:' (word word|  input_+);
outputs             : 'outputs:' (word word|  output+);
steps               : 'steps:'  step+;
step                : word ':'  run (in_ | out_)+;
in_or_out           : (identification | word word ':') '{'?
                      (type_|doc|default|secondaryFiles|word|',')+ '}'?;
run                 : 'run:' ( tool | STRING  | word );
input_              : (identification | word word ':')  (type_  | doc |
                     default  | source | label  |inputBinding | description|secondaryFiles|format_)+;
output              : (identification | word':' ) (doc  |
                      default | source | label  | outputSource | outputBinding | type_  | description)+;
source              : 'source:' STRING ;
type_               : 'type:' word+ ;
tag                 : '"#' word '"';
inputBinding        : 'inputBinding:' ((position |prefix|glob|separate)+ | '{}');
separate            : 'separate:' word;
outputBinding       : 'outputBinding:' ((position |prefix| glob)+ | '{}'); 
position            : 'position:' NUMBER ;
prefix              : 'prefix:' STRING  ;
identification      : 'id:' (STRING | word) ;
outputSource        : 'outputSource:' word ;
class_              : 'class:' ('Workflow' | 'CommandLineTool' | word);
baseCommand         : 'baseCommand:' word  arguments?;
stdin_              : 'stdin:' word ;
glob                : 'glob:' '$('? word ')'? ;
arguments           : 'arguments:'  argument+;
dockerrequirement   : 'DockerRequirement:'  dockerpull;
dockerpull          : 'dockerPull:' word ;
argument            : STRING ;
stdout_              : 'stdout:' word ;
stderr_             : 'stderr:' word ;
word                : (LETTERS|CHAR|NUMBER)+;
requirements        : 'requirements:'  class_  ;
default             : 'default:'  (STRING  | file_);
file_                : '{'?  'class: File' ','? 
                      (location ','?|secondaryFiles )+ '}'?;
location            :  'location:' (word | STRING);
secondaryFiles      : 'secondaryFiles:'  (file_ | STRING | word );
version             : 'cwlVersion:' 'v1.0';
hints               : 'hints:'  dockerrequirement;
format_              : 'format:' 'edam:format_' NUMBER; 
comment             : '#' word;

//LEXER


STRING              : '"' .*?'"';
LETTERS             : ('A'..'Z'|'a'..'z')+;
NUMBER              : [0-9]+;
CHAR                : ~('A'..'Z'|'a'..'z'|'\n'|' '|'-'|':'|'0'..'9')+;
NL                  : ('\r'? '\n' | '\r')+ -> skip;
HYPHEN              : '-'-> skip;
WHITESPACE          : ' ' -> skip ;

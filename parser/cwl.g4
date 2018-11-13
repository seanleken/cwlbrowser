grammar cwl;

//PARSER
workflow            :'#!/usr/bin/env cwl-runner' NL version NL  identification?
                    'class: Workflow' NL (label| doc| description| inputs|outputs|steps)+
                      EOF;
label               : 'label:' STRING NL;
doc                 : 'doc:' STRING NL;
description         : 'description:' STRING NL;
inputs              : 'inputs:' ('[]' NL | NL input_+);
outputs             : 'outputs:' ('[]' NL | NL output+);
steps               : 'steps:' NL step+;
step                : name ':' NL run (in_ | out_)+;
in_                  : 'in: ' ('[]' NL | '['WORD']' NL | NL in_or_out+);
out_                 : 'out: ' ('[]' NL | '['WORD']' NL | NL  in_or_out+);
in_or_out           : (identification | name NL) type_ (doc)?;
run                 : 'run:' NL (class_ inputs | baseCommand | stdin_ | stdout_ | outputs)+;
input_              : name ':' NL (identification | type_ | doc |
                     default | source | label |inputBinding)+;
output              : name ':' NL (identification | doc |
                      default | source | label | outputSource | type_)+;
source              : 'source:' STRING NL;
name                : (WORD|NUMBER)+;
type_                : 'type:' ('File' | 'integer' | 'string' | 'float' | 'double' | 'stdout' | 'stdin') NL;
tag                 : '"#' WORD '"';
inputBinding        : 'inputBinding:' NL (position |prefix)+;
position            : 'position:' NUMBER NL;
prefix              : 'prefix:' WORD NL;
identification      : '-id:' STRING NL;
outputSource        : 'outputSource:' name;
class_               : 'class:' ('Workflow' | 'CommandLineTool');
baseCommand         : 'baseCommand:' name NL;
stdin_               : 'stdin:' WORD NL;
stdout_              : 'stdout:' WORD NL;
default             : 'default:' STRING;
version             : 'cwlVersion:' 'v1.0';

//LEXER
WORD                : ('A'..'Z'|'a'..'z'|'/'|'.')+;
STRING              : '"' .*? '"';
NUMBER              : [0-9]+;
NL                  : '\n'+;
WHITESPACE          : ' ' -> skip ;

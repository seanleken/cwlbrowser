grammar cwl;

//PARSER
workflow            :'#!/usr/bin/env cwl-runner' version identification?
                    'class: Workflow' (label| doc| description| inputs|outputs|steps)+
                      EOF;
label               : 'label:' STRING '\n';
doc                 : 'doc:' STRING '\n';
description         : 'description:' STRING 'NL;
inputs              : 'inputs:' ('[]' NL | NL input_+);
outputs             : 'outputs:' ('[]' NL | NL output+);
steps               : 'steps:' NL step+;
step                : name ':' run (in_ | out_)+;
in_                  : 'in: ' ('[]' | '['WORD']' | in_or_out+);
out_                 : 'out: ' ('[]' | '['WORD']' | in_or_out+);
in_or_out           : (identification | name) type_ (doc)?;
run                 : 'run:' class_ inputs baseCommand stdin_? stdout_? outputs?;
input_              : name ':' identification? type_? doc?
                     default? source? label? inputBinding?;
output              : name ':' identification?  doc?
                      default? source? label? outputSource? type_?;
source              : 'source:' tag;
name                : (WORD|NUMBER)+;
type_                : 'type:' ('File' | 'integer' | 'string' | 'float' | 'double' | 'stdout' | 'stdin');
tag                 : '"#' WORD '"';
inputBinding        : 'inputBinding:' position? prefix?;
position            : 'position:' NUMBER;
prefix              : 'prefix:' WORD;
identification      : '-id:' tag;
outputSource        : 'outputSource:' name;
class_               : 'class:' ('Workflow' | 'CommandLineTool');
baseCommand         : 'baseCommand:' name;
stdin_               : 'stdin:' WORD;
stdout_              : 'stdout:' WORD;
default             : 'default:' STRING;
version             : 'cwlVersion:' 'v1.0';

//LEXER
WORD                : ('A'..'Z'|'a'..'z'|'/'|'.')+;
STRING              : '"' .*? '"';
NUMBER              : [0-9]+;
NL                  : '\n';
WHITESPACE          : ' ' -> skip ;

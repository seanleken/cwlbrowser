grammar cwl;

//PARSER
workflow            :'#!/usr/bin/env cwl-runner' version identification?
                    'class: Workflow' (label | doc | description | steps
                    | inputs | outputs)+;
label               : 'label:' STRING;
doc                 : 'doc:' STRING;
description         : 'description:' STRING;
inputs              : 'inputs:' ('[]' | input_+);
outputs             : 'outputs:' ('[]' | output+);
steps               : 'steps:' step+;
step                : name ':' run (in_ | out_)+;
in_                  : 'in: ' ('[]' | in_or_out+);
out_                 : 'out: ' ('[]' | in_or_out+);
in_or_out           : (identification | name) type_ (doc)?;
run                 : 'run:' class_ inputs baseCommand (stdin_ | stdout_)+;
input_               : name':' (identification | type_ |  doc
                    |  default |  source | label | inputBinding)+;
output              : name ':' (identification | type_ | doc
                    | default | source | label | outputSource)+;
source              : 'source:' tag;
name                : WORD;
type_                : 'type:' ('File' | 'integer' | 'string' | 'float' | 'double');
tag                 : '"#' WORD '"';
inputBinding        : 'inputBinding:' ( position | prefix)+?;
position            : INTEGER;
prefix              : 'prefix:' WORD;
identification      : '-id:' tag;
outputSource        : 'outputSource:' WORD;
class_               : ('Workflow' | 'CommandLineTool');
baseCommand         : 'baseCommand:' WORD;
stdin_               : 'stdin:' WORD;
stdout_              : 'stdout:' WORD;
default             : 'default:' STRING;
version             : 'cwlVersion:' 'v' INTEGER '.' INTEGER;

//LEXER
WORD                : [a-z|A-Z|'.']+;
STRING              : '"' .*? '"';
NEWLINE             : ('\r'? '\n' | '\r')+ -> skip;
INTEGER             : [0-9]+;
WHITESPACE          : ' ' -> skip ;

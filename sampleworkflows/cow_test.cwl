#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: [singularity, run]
inputs:
  image: 
    type: File
    inputBinding:
      position: 1
  in_file:
    type: File
    inputBinding:
      position: 2
      prefix: -i
  out_file:
    type: string
    inputBinding:
      position: 3
      prefix: -o


outputs:
  cow_pic:
    type: File
    outputBinding: 
      glob: $(inputs.out_file)
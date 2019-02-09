cwlVersion: v1.0
class: Workflow

inputs:
  sing_image: File
  words: string
  out_file: string


outputs:
  classout:
    type: File
    outputSource: compile/cow_pic

steps:
  file_make:
    run: stdout.cwl
    in:
      message: words
    out: [example_out]

  compile:
    run: cow_test.cwl
    in:
      image: sing_image
      in_file: file_make/example_out
      out_file: out_file
    out: [cow_pic]
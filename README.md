MiMoTable Dataset
==================
This is the dataset MiMoTable in paper "MiMoTable: A Multi-scale Spreadsheet Benchmark with Meta Operations for Table Reasoning".

Spreadsheet Files
----------------
The `data/{language}/spreadsheet` directory contains the spreadsheet files.

Questions and Answers
----------------
The `data/{language}/problems.json` file contains the questions, answers and other related infos. Each line contains one sample. The fields in each sample are described as below.

- **spreadsheet_list**: the paths of spreadsheets used to answer the question.
- **table_type**: the type of tables described in paper.
- **table_difficulty**: the table difficulty, three level, simple/medium/hard
- **question**
- **meta_operation_list**: the meta operations of question.
- **question_difficulty**: the question difficulty described in paper.
- **answer**
- **output_files**: the output files of Edit and Visualize, xlsx or png.


Related Prompt
---------------
The `src` directory contains the code for building related prompt.

- meta_operation_classification.py
- model_inference.py
- performance_evaluation.py

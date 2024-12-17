import sys
import pandas as pd

def format_one_sheet(sheet_name, sheet_data):
    format_str = f"<Sheet><Sheet Name>{sheet_name}</Sheet Name><Sheet Content>{sheet_data}</Sheet Content></Sheet>"
    return format_str

def format_one_excel(excel_name, sheet, per_sheet_len):
    format_str = f"<Table><Table Name>{excel_name}</Table Name><Table Content>"
    for sheet_name, sheet_data in sheet.items():
        sheet_data = sheet_data.to_markdown()[:per_sheet_len]
        format_str += format_one_sheet(sheet_name, sheet_data)
    format_str += "</Table Content></Table>"
    return format_str

def simple_get_answer_prompt(q, table_content):
    prompt = '''Below is the table content in markdown, please answer the question according the table content.
    
%s

<Question>%s</Question>'''%(table_content, q)
    return prompt

if __name__ == '__main__':
    # the input excel file path
    file_path = sys.argv[1]
    # the question need to be answer
    question = sys.argv[2]

    context_size = 128000
    sheet = pd.read_excel(file_path, sheet_name=None)
    sheet_num = 0
    sheet_num += len(sheet.items())
    per_sheet_len = int(context_size / sheet_num)
    multi_excel_str = []
    file_name = file_path.split("/")[-1]
    excel_str = format_one_excel(file_name, sheet, per_sheet_len)
    prompt = simple_get_answer_prompt(question, excel_str)
    print(prompt)
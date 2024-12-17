import sys

def build_prompt(question):
    prompt = '''You are a spreadsheet question classification expert. Given a user’s question about an Excel spreadsheet, classify the question according to the requirements and output it in the specified format.

<Requirements>
The following operation classification already exists, presented in the format of operation name: operation description. If the user’s question can be classified as some of the operations, output the operation names. One question can be classified into multiple operations.
Lookup: Locate the position of the specific target.
Edit: Modify, delete, or add to a table.
Calculate: The numerical computation, sum, avg, max, etc.
Compare: Compare two or more targets in a table.
Visualize: Show in chart. Reasoning: Inferring information from the table content that is not explicitly included.
</Requirements>
<Output Format>
operation name 1, operation name 2, ...
</Output Format>

<Question>
what country hosted the most tournaments?
</Question>
Lookup, Calculate, Compare

<Question>
%s
</Question>'''%(question)
    return prompt

if __name__ == '__main__':
    # the question to be classified
    question = sys.argv[1]

    prompt = build_prompt(question)
    print(prompt)
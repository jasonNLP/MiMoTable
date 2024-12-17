import sys

def build_prompt(question, correct_answer, candidate_answer):
    prompt = '''For the following questions, given the correct answer, determine whether the candidate’s answer is correct. If it is correct, output "Correct"; if it is incorrect, output "Incorrect"; if it is uncertain whether it is correct, output "Uncertain". As long as the candidate’s answer contains the key information that can correctly answer the question, it is considered correct. If the question is open-ended, give a score between 0-1 according to the correct answer. Do not output any other content.

<Question>
%s
</Question>
<Correct Answer>
%s
</Correct Answer>
<Candidate answer>
%s
</Candidate answer>'''%(question, correct_answer, candidate_answer)
    return prompt

if __name__ == '__main__':
    # the question to be classified
    question = sys.argv[1]
    # correct answer
    correct_answer = sys.argv[2]
    # candidate answer
    candidate_answer = sys.argv[3]

    prompt = build_prompt(question, correct_answer, candidate_answer)
    print(prompt)
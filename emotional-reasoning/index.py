'''
TODO 
  Capture stdout as a separate variable
'''

SINGLE_ANSWER = 'SINGLE_ANSWER'
MULTI_RESPONSE = 'MULTI_RESPONSE'

steps = [
  {
    'id': 1,
    'prompt': 'What\'s on your mind?\n',
    'type': SINGLE_ANSWER
  },
  {
    'id': 2,
    'prompt': 'How is that making you feel?',
    'type': MULTI_RESPONSE
  },
  {
    'id': 3,
    'prompt': 'Why do you feel {0}?',
    'type': MULTI_RESPONSE,
    'repeat_for_each_response_from': 2
  },
  {
    'id': 4,
    'prompt': 'Can you question or challenge these thoughts?',
    'type': MULTI_RESPONSE,
  },
  {
    'id': 5,
    'prompt': 'Are there any specific actions you\'d like to take?',
    'type': MULTI_RESPONSE
  }, 
  {
    'id': 6,
    'prompt': 'How do you feel now?\n',
    'type': SINGLE_ANSWER
  }
]

question_response_map = {
  
}
    
def loop_of_inputs(prompt):
  responses = []
  last_response = ''

  while last_response != '' or len(responses) == 0:
    if len(responses) == 0:
      last_response = input('{prompt} Press \'return\' without any input when you\'re finished.\n'.format(prompt=prompt))
    else:
      last_response = input()

    if last_response != '':
      responses.append(last_response)

  return responses

def handle_question_type(step, additional_prompt_args = []):
  if step['type'] == SINGLE_ANSWER:
    response = input(step['prompt'].format(*additional_prompt_args))
    return response
  elif step['type'] == MULTI_RESPONSE:
    responses = loop_of_inputs(step['prompt'].format(*additional_prompt_args))
    return responses

def main(steps):
  for i in range(len(steps)):
    step = steps[i] 

    if 'repeat_for_each_response_from' in step:
      related_responses = question_response_map[step['repeat_for_each_response_from']]
      responses = []

      for j in range(len(related_responses)):
        response = handle_question_type(step, related_responses[j])
        responses.append(response)
        question_response_map[step['id']] = responses
    else:    
      response = handle_question_type(step)
      question_response_map[step['id']] = response

main(steps)

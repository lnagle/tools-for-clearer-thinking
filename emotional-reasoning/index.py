'''
TODO 
  Capture stdout as a separate variable
'''

SINGLE_ANSWER = 'SINGLE_ANSWER'
MULTI_RESPONSE = 'MULTI_RESPONSE'

steps = [
  {
    'id': 1,
    'prompt': 'What\'s on your mind?',
    'type': SINGLE_ANSWER
  },
  {
    'id': 2,
    'prompt': 'How is that making you feel?',
    'type': MULTI_RESPONSE
  },
  # {
  #   'id': 3,
  #   'prompt': 'Why do you feel {emotion}?',
  #   'type': MULTI_RESPONSE,
  #   'repeat_for_each_response_from': 2
  # },
  # {
  #   'id': 4,
  #   'prompt': 'Can you question or challenge these thoughts?',
  #   'type': MULTI_RESPONSE,
  # },
  # {
  #   'id': 5,
  #   'prompt': 'Are there any specific actions you\'d like to take?',
  #   'type': MULTI_RESPONSE
  # }, 
  # {
  #   'id': 6,
  #   'prompt': 'How do you feel now?',
  #   'type': SINGLE_ANSWER
  # }
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

def handle_question_type(step):
  if step['type'] == SINGLE_ANSWER:
    response = input(step['prompt'])
    return response
  elif step['type'] == MULTI_RESPONSE:
    responses = loop_of_inputs(step['prompt'])
    return responses

def main(steps):
  for i in range(len(steps)):
    step = steps[i] 
    response = handle_question_type(step)
    question_response_map[step['id']] = response

main(steps)    
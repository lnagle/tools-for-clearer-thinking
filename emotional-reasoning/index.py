'''
TODO 
  Capture stdout as a separate variable
'''

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

emotions = loop_of_inputs('What are you feeling?')

for emotion in emotions:
  emotion_prompt = 'Why are you feeling {emotion}?'.format(emotion=emotion)
  loop_of_inputs(emotion_prompt)
  
action = input('Are there any actions you\'d like to take?\n')

summary = input('Briefly summarize this session and how you\'re feeling now.\n')

print('Exiting')

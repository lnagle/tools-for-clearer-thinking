'''
TODO 
  Create abstraction for loop of inputs
  Capture stdout as a separate variable
'''

emotion = input('What are you feeling?\n')

reasons = []
reason = ''

while reason != '' or len(reasons) == 0:
  if len(reasons) == 0:
    reason = input('Why are you feeling {emotion}? Press \'enter\' without any input when you\'re finished.\n'.format(emotion=emotion))
  else:
    reason = input()
  
  reasons.append(reason)

action = input('Are there any actions you\'d like to take?\n')

summary = input('Briefly summarize this session, including your emotion, why you\'re feeling it, and any actions you\'d like to take\n')

print('Exiting')

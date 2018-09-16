def q_gen(q_data):
"""
inputs q_data = list of tuples[(word, entity type)...()]
@returns q = list of questions from generated entity type
"""
q = []
q_template = {'UNKNOWN': None, 'PERSON':"Who was ", 'LOCATION':"Where is", 'ORGANIZATION': "What was the ",
                   'EVENT': "What was the ", 'WORK_OF_ART': "What was the ", 'CONSUMER_GOOD': "What was the ", 'OTHER': "What's the importance of "}
# Person, detect if common or proper to see common + "the "

for t in q_data: 
    q.append(q_template[t[1]] + t[0])
return q





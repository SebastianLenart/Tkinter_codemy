from random import randint
import random

answer_list = []

global our_states
our_states = ["california", "florida", "texas"]

global out_states_capitals
our_states_capitals = {
    "california": "cap_c",
    "florida": "cap_f",
    "texas": "cap_t"
}

global rando
rando = randint(0, len(our_states) - 1)

answer = our_states[rando]
"""
answer_list.append(our_states[rando])
# print(our_states)
our_states.remove(our_states[rando])
# print(our_states)

random.shuffle(our_states)
rando = randint(0, len(our_states) - 1)
answer_list.append(our_states[rando])
our_states.remove(our_states[rando])
random.shuffle(our_states)
rando = randint(0, len(our_states) - 1)
answer_list.append(our_states[rando])
print(answer_list)
"""


count = 1
while count < 4:
    rando = randint(0, len(our_states) - 1)
    if count == 1:
        answer = our_states[rando]
    answer_list.append(our_states[rando])
    our_states.remove(our_states[rando])
    random.shuffle(our_states)

    count += 1
print(answer_list)
print(answer)


























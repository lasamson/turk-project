# main script
from boto.mturk.connection import MTurkConnection
from boto.mturk.question import (QuestionContent,Question,QuestionForm,
Overview,AnswerSpecification,SelectionAnswer,FormattedContent,FreeTextAnswer)
import threading

# credentials and other constant variables
ACCESS_KEY_ID = ''
SECRET_ACCESS_KEY = ''
HOST = 'mechanicalturk.sandbox.amazonaws.com'
HIT_ID = ''

# keep track of the number of assignments for the specified HIT
num_assignments = 0

# establish a connection with MTurk API using Boto SDK
mtc = MTurkConnection(aws_access_key_id=ACCESS_KEY_ID,
                      aws_secret_access_key=SECRET_ACCESS_KEY,
                      host=HOST)

# periodically checks for new assignments for the specified HIT
def check_hit():
    global num_assignments
    # get the current number of assignments for the specified HIT
    cur_num_assignments = int(mtc.get_assignments(HIT_ID).NumResults)
    # if there are new assignments, recalculate the cost function and update the cost
    if cur_num_assignments > num_assignments:
        num_assignments = cur_num_assignments
        # debugging
        print(num_assignments)
        # call cost function with num_assignments as argument
        # make POST request to update the cost
    else:
        # if there are no new assignments, alert the user
        print('No changes. Checking again in 30s.')
    # run the function again in 30 seconds to check for new assignments
    threading.Timer(30, check_hit).start()

# check_hit()

def extend_hit_assignments(exp_inc):
    mtc.extend_hit(hit_id=HIT_ID, expiration_increment=exp_inc)

# testing extend_hit_assignments
hit = mtc.get_hit(HIT_ID)[0]
print(hit.AssignmentDurationInSeconds)
extend_hit_assignments(3600)
hit = mtc.get_hit(HIT_ID)[0]
print(hit.AssignmentDurationInSeconds)



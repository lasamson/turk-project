# helper script that lists each of the user's HITs by title and id
from boto.mturk.connection import MTurkConnection
from boto.mturk.question import QuestionContent,Question,QuestionForm,Overview,AnswerSpecification,SelectionAnswer,FormattedContent,FreeTextAnswer

# credentials and other constant variables
ACCESS_KEY_ID = ''
SECRET_ACCESS_KEY = ''
HOST = 'mechanicalturk.sandbox.amazonaws.com'

# establish a connection with MTurk API using Boto SDK
mtc = MTurkConnection(aws_access_key_id=ACCESS_KEY_ID,
                      aws_secret_access_key=SECRET_ACCESS_KEY,
                      host=HOST)

# list all of the user's HITs by their title and id
hits = mtc.search_hits()
for hit in hits:
    print(hit.Title + ": " + hit.HITId)

    # mtc.extend_hit(hit_id=hit.HITId, expiration_increment=3600)
    # mtc.set_sqs_notification(hit.HITTypeId, 'https://sqs.us-west-2.amazonaws.com/846491338745/mturk_queue', event_types=['AssignmentSubmitted'])
# collection = DOMTree.documentElement
#
# HIT = collection.getElementsByTagName("HIT")[0]
# HITId = HIT.getElementsByTagName("HITId")
# print(HITId)

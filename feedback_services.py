#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from dao.feedback_table import FeedbackTable
import settings
import datetime

class ConversationService():
    def __init__(self):
        self.data_file = settings.DATABASES['filepath']
        self.conversation = ConversationTable(self.data_file)

    def add_conversation(self, thread_id, authority_email, attendees, subject, from_email, person):
        self.conversation.insert(thread_id, 
            authority_email, attendees, 
            '', 
            subject,
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            from_email,person, '')
    
    def get_conversation(self, thread_id):
        return self.conversation.get_conversation(thread_id)
    
    def get_manager_assistant_conversation(self, assistant_type, authority_email):
        return self.conversation.get_manager_assistant_conversation(assistant_type, authority_email)

    def delete_conversation(self, thread_id):
        self.conversation.delete(thread_id=thread_id)
    
    def delete_manager_conversation(self, authority_email, from_email):
        self.conversation.delete(authority_email=authority_email, from_email=from_email)

    def update_conversation(self, conversation, sent_message):
        conversation_dict = {
            'authority_email': conversation[1],
            'attendees': conversation[2],
            'calendar_id': conversation[3],
            'subject' : conversation[4],
            'last_update': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'from_email':conversation[6],
            'person':conversation[7],
            'sent_email_msg':sent_message
        }

        thread_id = conversation[0]
        self.conversation.update(conversation_dict, thread_id=thread_id)


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from data_definition.db import Table

class FeedbackTable(Table):

    def __init__(self, data_file):
        super(ConversationTable, self).__init__(data_file, 'feedback_customer_reviews',
                                   ['customer_id VARCHAR(255) PRIMARY KEY',
                                    'customer_name VARCHAR(255)',
                                    'customer_email VARCHAR(255)',
                                    'customer_address VARCHAR(255)',
                                    'customer_number INT(10)',
                                    'feedback TEXT(1200) NOT NULL', 
                                    'time_of_feedback VARCHAR(255) NOT NULL',
                                    'loaction VARCHAR(255)', 
                                    'stopwords INT(9)',
                                    'punctuations INT(9)',
                                    'tokens INT(9)',
                                    'html_tag INT(9)',
                                    'hash_tags INT(9)',
                                    'special_characters INT(9)',
                                    'digits INT(9)',
                                    'extra_space INT(9)'])
        
    def select(self, *args, **kwargs):
        cursor = super(ConversationTable, self).select(*args, **kwargs)
        results = cursor.fetchall()
        cursor.close()
        return results

    def insert(self, *args):
        self.free(super(ConversationTable, self).insert(*args))

    def update(self, set_args, **kwargs):
        self.free(super(ConversationTable, self).update(set_args, **kwargs))

    def delete(self, **kwargs):
        self.free(super(ConversationTable, self).delete(**kwargs))

    def delete_all(self):
        self.free(super(ConversationTable, self).delete_all())

    def drop(self):
        self.free(super(ConversationTable, self).drop())

    def get_conversation(self, thread_id):
        results = self.select('*', thread_id=thread_id)
        if len(results) > 0:
            return results[0]

        return None
        
    def get_manager_assistant_conversation(self, assistant_type, authority_email):
        results = self.select('*', person=assistant_type, authority_email=authority_email)
        if len(results) > 0:
            return results
        return None


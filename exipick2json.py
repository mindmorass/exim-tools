#!/usr/bin/env python

# the only purpose of this script is to take exipick
# output and convert the data into JSON
# JSON should make it easy to import into any language
# and perform some real logic instead of bash scripts
# currently works with Python 2 - migration to 3 is needed

# example exipick command to run the output piped into this script

# exipick -bpa --flatq --unsorted --show-vars message_exim_id,semder_host_address,sender_host_authenticated,sender_local,sender_set_untrusted,spam_score,warning_count,authenticated_id,allow_unqualified_sender,authenticated_sender,body_linecount,body_zerocount,deliver_frozen_at,deliver_freeze,dont_deliver,recipients,first_delivery,message_age,message_body_size,message_body,received_protocol,recipients_count,recipients_undel_count,sender_address,reply_address,sender_address_domain,sender_helo_name,message_linecount,message_size,sender_host_name,sender_ident,shown_message_size,smtp_active_hostname

import os
import re
import json
import sys
exipick_input = sys.stdin.read()

class ExipickJson():

    def __init__(self):
        self.data = []
        self.output = []

        self.new_msg()

        self.show_vars = [
          'message_exim_id',
          'sender_address',
        ]

        lines = exipick_input.splitlines()
        for line in lines:
            self.output.append(line)

    def set_show_vars(self, var_list):
        self.show_vars = var_list

    def new_msg(self):
        self.metadata = {}
        self.metadata['message_headers'] = []
        self.recipients = [] # reset recipents back to a blank slate (new id)
        self.metadata['recipients'] = self.recipients
       
    # extract value from (key='value') strings as metadata

    def extract_metadata(self, message_key, message):
        regex_string = '{}=\'(.*?)\''.format(message_key)
        m = re.search(regex_string, message)
        if m:
            self.metadata[message_key] = m.group(1)

    def extract_recipients(self, message):
        regex = 'recipients=\'(.*?)\''
        m = re.search(regex, message)
        if m:
            for r in m.group(1).split(', '):
                self.recipients.append(r)

    def extract_message_headers(self, message):
        self.metadata['message_headers'].append(h)

    def jsonipick(self):
       
        # regular expressions for field extraction from exipick message
        # key is the metadata field name for the output JSON

        for msg in self.output:

            self.new_msg()

            # loop through regex dict and extract the existing metadata into JSON format

            for k in self.show_vars:
                self.extract_metadata(k, msg)

            self.extract_recipients(msg)
            self.data.append(self.metadata)

#### MAIN ####
# might be good to export this a module someday instead of a directly used class

# instantiate the class

o = ExipickJson()

# set the exim variables we want to extract 
# some vars require extra logic such as recipients and message_headers

o.set_show_vars([
   'authenticated_id',
   'warning_count',
   'sender_host_address',
   'message_size',
   'spam_score',
   'sender_set_untrusted',
   'sender_local',
   'sender_host_authenticated',
   'allow_unqualified_recipient',
   'allow_unqualified_sender',
   'authenticated_sender',
   'body_linecount',
   'body_zerocount',
   'deliver_frozen_at',
   'deliver_freeze',
   'first_delivery',
   'message_age',
   'message_body',
   'message_body_size',
   'received_protocol',
   'recipients_count',
   'recipients_undel_count',
   'reply_address',
   'sender_address',
   'sender_address_domain',
   'sender_helo_name',
   'message_linecount',
   'sender_host_name',
   'sender_ident',
   'shown_message_size',
   'smtp_active_hostname'
])

# run extractions

o.jsonipick()

# print extractions as JSON

print json.dumps(o.data)

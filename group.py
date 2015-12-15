import api
import json
import pandas as pd

CLIENT = api.GroupmeClient()

class Group(object):
    """docstring for Group"""
    def __init__(self, group_id):
        self.group_id = group_id
        self.raw_messages = None

    def collect_messages(self):
        """
        """
        self.raw_messages = CLIENT.get_all_group_messages(self.group_id)
    
    def handle_messages(self):
        self.id_to_name = dict()

        message_ids = list()
        created_ats = list()
        sender_ids = list()
        texts = list()

        liker_ids = list()
        receiver_ids = list()

        for message in self.raw_messages:

            message_ids.append(message["id"])
            sender_id = message["sender_id"]
            sender_ids.append(sender_id)
            created_ats.append(message["created_at"])
            texts.append(message["text"])

            sender_name = message["name"]
            if sender_id not in self.id_to_name:
                self.id_to_name[sender_id] = sender_name

            likes = message["favorited_by"]
            for like in likes:
                liker_ids.append(like)
                receiver_ids.append(sender_id)

        self.messages = pd.DataFrame({"message_id" : message_ids,
            "sender_id" : sender_ids,
            "created_at" : created_ats,
            "text" : texts})

        self.likes = pd.DataFrame({"liker_id" : liker_ids,
            "receiver_id" : receiver_ids})
                
    def __repr__(self):
        return "Group(group_id={})".format(self.group_id)


    def create_like_network(self):
        pass;
        
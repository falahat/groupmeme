from . import api
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
        messages_created_at = list()
        sender_ids = list()
        texts = list()

        liker_ids = list()
        receiver_ids = list()
        likes_created_at = list()

        for message in self.raw_messages:

            message_ids.append(message["id"])
            sender_id = message["sender_id"]
            sender_ids.append(sender_id)
            messages_created_at.append(message["created_at"])
            texts.append(message["text"])

            sender_name = message["name"]
            if sender_id not in self.id_to_name:
                self.id_to_name[sender_id] = sender_name

            likes = message["favorited_by"]
            for like in likes:
                liker_ids.append(like)
                receiver_ids.append(sender_id)
                likes_created_at.append(message["created_at"])

        self.messages = pd.DataFrame({"message_id" : message_ids,
            "sender_id" : sender_ids,
            "created_at" : messages_created_at,
            "text" : texts})

        self.likes = pd.DataFrame({"liker_id" : liker_ids,
            "created_at" : likes_created_at,
            "receiver_id" : receiver_ids})
                
    def __repr__(self):
        return "Group(group_id={})".format(self.group_id)


    def create_like_network(self):
        pass;
        
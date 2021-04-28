from data.db_con import *
import webbrowser
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
# from db_con import insert_data


class FillSlots(Action):
    def name(self) -> Text:
        return "user_details_form"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["uname", "passwd"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        # All slots are filled.
        return [SlotSet("requested_slot", None)]


class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_details_thanks",
                                 UserName=tracker.get_slot("uname"),
                                 Password=tracker.get_slot("passwd"))
        insert_data(tracker.get_slot("uname"), tracker.get_slot("passwd"))
        dispatcher.utter_message("Thanks for valuable feedback")

        return []

class ActionFetch(Action):
    f1=0
    def name(self) -> Text:
        return "action_fetch"

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_message")
        r = fetch_data()
        for i in r:
            dispatcher.utter_message(i[0],i[1])
            dispatcher.utter_message(tracker.get_slot("uname"),tracker.get_slot("passwd"))
            if (tracker.get_slot("uname")==i[0] and tracker.get_slot("passwd")==i[1]):
                dispatcher.utter_message(template="utter_greetagain")
                ActionFetch.f1=1
                break
        else:
            dispatcher.utter_message(text="Username password mismatch !\n")




        return []

class ActionStudentDetails(Action):
    def name(self) -> Text:
        return "action_StudentDetails"

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        if ActionFetch.f1==1:
            dispatcher.utter_message(template="utter_message")
            result=fetch_studentdetails()
            for i in result:
                dispatcher.utter_message("name:",i[0],"\n","father name:",i[1],"\n","rollno:",i[2],"\n","faculty advisor:",i[3],"\n","mobile no:",i[4],"\n","religion:",i[5],"\n")





        return []


class ActionGetthelink(Action):
    def name(self) -> Text:
        return "action_Getthelink"

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        url="https://mis.geca.ac.in/academic/iitmsJYBHWhGToc6CXeqRuLRcRfIKb2GZDoGdja7EafuiQ21Mv50OS8d3l8BvvTUIzrV3?enc=3Q2Y1k5BriJsFcxTY7ebQiVQQYDmXojG3GHsHqmcpc0="
        dispatcher.utter_message("You are being redirected to the information page")
        webbrowser.open(url)



        return []








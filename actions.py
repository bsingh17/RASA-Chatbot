# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import UserUtteranceReverted
        

class SalesForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    def name(self):
        return "sales_form"
    @staticmethod
    def required_slots(tracker):
        return [
            "person_name",
            "business_email",
            "city",
            "phone_number",
            ]
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("Thanks for getting in touch, we’ll contact you soon")
        return []

class ActionGreetUser(Action):
    def name(self):
        return "action_greet"
    def run(self,dispatcher,tracker,domain):
        dispatcher.utter_message(template="utter_greet")
        return [UserUtteranceReverted()]
        
class ActionGetUniqueCode(Action):
    def name(self):
        return "action_get_unique_code"
    def run(self,dispatcher,tracker,domain):
        email=tracker.get_slot("unique_code")
        output= 'The customer care team will contact you soon on {}'.format(email)
        dispatcher.utter_message(output)
        return []
    

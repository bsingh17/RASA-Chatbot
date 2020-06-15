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
        dispatcher.utter_message("Which course would you like to take?")
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
        output= 'Which course would you like to take?'.format(email)
        dispatcher.utter_message(output)
        return []
        
class ActionGetCourse(Action):
    def name(self):
        return "action_get_course"
    def run(self,dispatcher,tracker,domain):
        
        output= 'Pay for the selected course and enter the payment confirmation code to get the course confirmation email'
        dispatcher.utter_message(output)
        return []
    
class ActionPaymentConfirmed(Action):
    def name(self):
        return "action_payment_confirmed"
    def run(self,dispatcher,tracker,domain):
        
        output= 'Thanks For taking the course. You will be getting dashboard access through mail.'
        dispatcher.utter_message(output)
        return []

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime as dt


class ActionShowTime(Action):

    def name(self) -> Text:  # регистрируем имя действия
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # при вызове действия возвращаться ответ с текущим временем:
        dispatcher.utter_message(text=f'Сейчас {dt.now().strftime("%H:%M")}')

        return []


class ActionMyAction1(Action):

    def name(self) -> Text:
        return "action_my_action1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="My action 1")
        print("My action 1:")
        print(tracker.slots)
        print("Slot ACCOUNT_ID: {}" . format(tracker.get_slot("ACCOUNT_ID")))
        print("Slot ADDRESSES: {}" . format(tracker.get_slot("ADDRESSES")))
        return []


# class ActionRestart(Action):
#
#     def name(self) -> Text:
#         return "action_restart"
#
#     async def run(
#             self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:
#         # custom behavior
#         dispatcher.utter_message(response="utter_main_menu")
#         return [...]
#
#
# class ActionSessionStart(Action):
#
#     def name(self) -> Text:
#         return "action_session_start"
#
#     async def run(
#             self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:
#         # custom behavior
#         dispatcher.utter_message(response="utter_main_menu")
#         return [...]

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
# actions.py
class ActionSubmitOrderForm(Action):
    def name(self) -> Text:
        return "action_submit_order_form"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        confirm = tracker.get_slot("confirm")
        if confirm == "yes":
            # Ambil data yang diisi oleh pengguna
            order_type = tracker.get_slot("type")
            order_size = tracker.get_slot("size")
            order_color = tracker.get_slot("color")
            
            # Contoh URL API endpoint
            api_url = "http://127.0.0.1:8000/cloth/"
            
            # Data yang akan dikirim ke API
            payload = {
                "type": order_type,
                "size": order_size,
                "color": order_color
            }
            
            try:
                # Kirim POST request ke API
                response = requests.post(api_url, json=payload)
                
                # Periksa status response
                if response.status_code == 200:
                    dispatcher.utter_message(template="utter_order_received")
                else:
                    dispatcher.utter_message(text="Failed to place order. Please try again later.")
            except Exception as e:
                dispatcher.utter_message(text=f"An error occurred: {str(e)}")
        else:
            dispatcher.utter_message(text="Your order has been cancelled.")
        
        return []
        
class ActionGetCoffeeMenu(Action):

    def name(self) -> Text:
        return "action_get_coffee_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Daftar menu kopi
        coffee_menu = [
            {"name": "Espresso", "price": "Rp20.000"},
            {"name": "Latte", "price": "Rp25.000"},
            {"name": "Cappuccino", "price": "Rp27.000"},
            {"name": "Americano", "price": "Rp22.000"},
        ]

        menu_text = "Berikut adalah pilihan kopi yang tersedia:\n"
        for coffee in coffee_menu:
            menu_text += f"- {coffee['name']}: {coffee['price']}\n"

        dispatcher.utter_message(text=menu_text)
        return []
        


class ActionGetRotiMenu(Action):

    def name(self) -> Text:
        return "action_get_roti_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        api_url = 'http://127.0.0.1:8000/bread/'
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an error for bad responses
            bread_menu = response.json()
        except requests.exceptions.RequestException as e:
            dispatcher.utter_message(text="Maaf, saya tidak bisa mendapatkan menu roti saat ini.")
            return []

        menu_text = "Berikut adalah pilihan roti yang tersedia:\n"
        for bread in bread_menu:
            menu_text += f"- {bread['name']}: {bread['price']}\n"

        menu_text += "*request by api\n"
        dispatcher.utter_message(text=menu_text)
        return []

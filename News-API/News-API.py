# Read News using NewsAPI
import requests
import json
import time
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__=="__main__":
    apikey="Your ApiKey"
    r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={apikey}")
    data=r.content # this is string format and not parsed
    parsed=json.loads(data)
    for i in range(1,10):
        title=parsed['articles'][i]['title']
        speak(title)
        time.sleep(1)
        speak("The content is :")
        content=parsed['articles'][i]['content']
        speak(content)
        time.sleep(3)
        speak("Next headline :")
        time.sleep(1)

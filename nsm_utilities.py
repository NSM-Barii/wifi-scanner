# WIFI SCANNER  // UTILITIES MODULE

# UI IMPORTS
import pywifi.iface
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.console import Console
console = Console()

# NETWORK IMPORTS
import pywifi, socket, ipaddress
from scapy.all import sniff


# ETC IMPORTS 
import threading, os, random, time, pyttsx3



class Utilities():
    """This class will hold secondary methods that will provide info for main program logic"""


    def __init__(self):
        pass

    
    @staticmethod
    def tts(say, lock = False, voice_rate = 20, voice_sound=False) -> str:
        """This method will be used to speak to the user through voice engines, use a thread locker if using threads to prevent race conditions"""
        

        # CREATE OBJECT
        engine = pyttsx3.init()


        # SET VARIABLES
        try:
          
            rate = engine.getProperty('rate')
            voices = engine.getProperty('voices')


            # SET RATE
            engine.setProperty('rate', rate - voice_rate)
        
            
            # NOW TO CHOOSE THE VOICE WE WANT TO USE
            if voice_sound != False:
                voice_sound = int(voice_sound)
                engine.setProperty('voice', voices[voice_sound])
                T = "1"

            elif len(voices) > 1:
                engine.setProperty('voice', voices[1].id)
                T = "2"

            else:
                engine.setProperty('voice', voices[0].id)
                T = "3"
            
            # FOR DEBUGGING
            #console.print(T)
            
            # NOW TO SPEAK TTS
            if not lock:
                    
                engine.say(say)
                engine.runAndWait()
                
            else:

                with lock:
                    engine.say(say)
                    engine.runAndWait()
            

        except Exception as e:
            console.print(e)


    
    @staticmethod
    def clear_screen():
        """This will be used to clear the os screen"""

        # WINDOWS
        if os.name == "nt":
            os.system('cls')

        # LINUX
        elif os.name == "Posix" or os.name == "unix":
            os.system('clear')
        
        else:
            console.print("[bold red]Utilities Module Error:[/bold red] [yellow]failed to clear screen, platform not supported[yellow]")


# FOR MODULE TESTING
if __name__ == "__main__":

    Utilities().test_static()
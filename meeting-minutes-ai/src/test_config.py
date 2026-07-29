from config import get_api_key

def main():
    if get_api_key():
        print ("API Key loaded successfully!!")
    else:
        print ("Issues finding API key, check .env")

main()
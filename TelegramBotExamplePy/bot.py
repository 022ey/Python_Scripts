from telegram.ext import Updater, CommandHandler
import requests
import re

def get_url(): #get the url
    contents = requests.get('https://random.dog/woof.json').json() #get the json
    url = contents['url'] #get the url
    return url


def get_image_url(): #get the url
    allowed_extension = ['jpg','jpeg','png'] #allowed extension
    file_extension = '' #file extension
    while file_extension not in allowed_extension: #while the file extension is not in the allowed extension
        url = get_url() #get the url
        file_extension = re.search("([^.]*)$",url).group(1).lower() #regex to get the file extension
    return url 


def bop(bot, update): #bop is the function
    url = get_image_url() #get the url
    chat_id = update.message.chat_id #get the chat id
    bot.send_photo(chat_id=chat_id, photo=url) #Send the message to the bot and print the response


def main():
    updater = Updater('TOKEN') #replace TOKEN with your bot token
    dp = updater.dispatcher #dispatcher object
    dp.add_handler(CommandHandler('bop', bop)) # bop is the command
    updater.start_polling() #start polling
    updater.idle() #idle


if __name__ == '__main__': #if the file is run directly
    main() #run the main function
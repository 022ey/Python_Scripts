#!/usr/bin/env python3
# Path: Discord Webhook Automation/discord_webhook.py
import requests

discord_webhook_url = 'your webhook url'
Message = {
  "content": "./Hello_World",
  "username": "Name for your discord webhook",
  "avatar_url": "Your Avatar Image URL",
  "tts": False,
  "embeds": [
    {
      "title": "Title",
      "description": "Description",
      "url": "https://discordapp.com",
      "color": 16711680,
      "footer": {
        "text": "Footer Text"
      },
      "image": {
        "url": "https://discordapp.com"
      },
      "thumbnail": {
        "url": "https://discordapp.com"
      },
      "author": {
        "name": "Author Name",
        "url": "https://discordapp.com",
        "icon_url": "https://discordapp.com"
      },
      "fields": [
        {
          "name": "Field Name",
          "value": "Field Value",
          "inline": True
        }
      ]
    }
  ]
}
requests.post(discord_webhook_url, data=Message)

# Message can consist of the following:
# content: The message to be sent
# username: The name of the user
# avatar_url: The URL of the user's avatar
# tts: Whether or not the message should be read aloud
# embeds: An array of embeds to be sent with the message
# The embeds are formatted as follows:
# title: The title of the embed
# description: The description of the embed
# url: The URL of the embed
# timestamp: The timestamp of the embed
# color: The color of the embed
# footer: The footer of the embed
# footer_icon: The icon of the footer
# image: The image of the embed
# thumbnail: The thumbnail of the embed
# For more info check out the discord API: https://discordapp.com/developers/docs/resources/channel#embed-object
# The following are the fields of the embed:
# title: The title of the embed
# description: The description of the embed
# url: The URL of the embed
# timestamp: The timestamp of the embed
# color: The color of the embed
# footer: The footer of the embed
# footer_icon: The icon of the footer
# image: The image of the embed
# thumbnail: The thumbnail of the embed

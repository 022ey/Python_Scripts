import requests
import json

from flask import Flask, render_template, request , redirect , url_for

app = Flask(__name__)

#_____________________________________________
#FORMATTED
def formatted_messages(code , channel_id):
    messages =  []
    headers  = {'authorization': code}
    r        = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)
    jsonn    = json.loads(r.text)

    for value in jsonn:
        user    = value['author']['username']
        content = value['content']
        message = f'{user} :\n{content}'
        messages.append(message)

    messages.reverse()
    for message in messages:
            with open(f'Scraped Messages/Message_{channel_id}_Formatted.txt' ,"a", encoding='utf-8') as myfile:
                myfile.write(message)
                myfile.write("\n")
                myfile.write("\n")

#__________________________________________________
#DEFAULT
def retrive_messages(code , channel_id):
    headers  = {'authorization': code}
    r        = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)
    jsonn    = json.loads(r.text)

    for value in jsonn:
        with open(f'Scraped Messages/Message_{channel_id}.txt' ,"a", encoding='utf-8') as myfile:
            myfile.write(value['content'])
            myfile.write("\n")

#___________________________________________________

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        try:
            if request.form['parse_type'] == "formatted":
                try:
                    auth_code  = request.form["code"]
                    cid = request.form["cid"]
                    formatted_messages(auth_code, cid)
                    print(auth_code)
                    print(cid)
                    return render_template('success.html')

                except:
                    return render_template('error.html')

            elif request.form['parse_type'] == "default":
                try:
                    auth_code  = request.form["code"]
                    cid = request.form["cid"]
                    retrive_messages(auth_code, cid)
                    print(auth_code)
                    print(cid)
                    return render_template('success.html')

                except:
                    return render_template('error.html')

        except:
            return render_template('radio_error.html')

    else:
        return render_template('index.html')


#__________________________________________________

if __name__ == '__main__':
    app.run( debug = True)

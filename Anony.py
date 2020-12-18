import requests
import json
import io



TOKEN = '1173070241:AAFwWOscW1H96viyN1gBKQiFp1PzBChHp5o'
URL = 'https://api.telegram.org/bot{}/'.format(TOKEN)
#chat = '982910057'
admins=['charindith']
forwarders=['982910057']



def get_updates(offset=None):
    url = URL + 'getUpdates'
    if offset:
        url += '?offset={}'.format(offset)
    js = get_json_from_url(url)
    return js


def forwardMsg(update):
    msg_id=update['message']['message_id']
    chat=update['message']['chat']['id']
    use=update['message']['from']['username']
    
    chat=str(chat)
    for i in forwarders:
    	p=requests.get('https://api.telegram.org/bot'+TOKEN
                   +'/forwardMessage?from_chat_id='+chat
                   +'&message_id='+str(msg_id)+
                   '&chat_id='+i)
    pp='@'+use
    sendText(pp,str(982910057))
    	


def sendSticker(sticker,chat):
    chat=str(chat)
    r=requests.get(URL+'/sendSticker?chat_id='+chat+'&sticker='+sticker)
    
    print(r.text)

    
def sendDoc(doc_id, caption,chat):
    chat=str(chat)
    caption=' '
    r=requests.get('https://api.telegram.org/bot' + TOKEN
                 + '/sendDocument?chat_id=' + chat + '&document='
                 + doc_id + '&caption=' + caption)
    print(r.text)

def sendPhoto(doc_id,caption,chat):
    chat=str(chat)
    caption=' '
    r=requests.get('https://api.telegram.org/bot' + TOKEN
                 + '/sendPhoto?chat_id=' + chat + '&photo='
                 + doc_id+'&caption='+caption )
    print(r.text)

def sendVideo(doc_id,caption,chat):
    chat=str(chat)
    caption=' '
    r=requests.get('https://api.telegram.org/bot' + TOKEN
                 + '/sendVideo?chat_id=' + chat + '&video='
                 + doc_id+'&caption='+caption )
    print(r.text)

def sendText(text,chat):
    chat=str(chat)
    r=requests.get('https://api.telegram.org/bot' + TOKEN
                 + '/sendMessage?chat_id=' + chat + '&text='
                 + text )
    print(r.text)

def sendAudio(doc_id,caption,chat):
    chat=str(chat)
    caption=' '
    r=requests.get('https://api.telegram.org/bot' + TOKEN
                 + '/sendAudio?chat_id=' + chat + '&audio='
                 + doc_id+'&caption='+caption )
    print(r.text)

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_url(url):
    response = requests.get(url)
    content = response.content.decode('utf8')
    return content


def uploader(updates):
    for update in updates['result']:
         


        try:
            
            
        #if update['message']['from']['username'] in admins:
            if update['message']['chat']['type']=='private':
                try:
                    doc_id = update['message']['text']
                    
                    chat=update['message']['chat']['id']
                    sendText(doc_id,chat)
                except:
                
                    try:
                        try:
                            caption = update['message']['caption']
                        except:
                            caption=' '
                        doc_id = update['message']['document']['file_id']
                        chat=update['message']['chat']['id']
                        sendDoc(doc_id,caption,chat)
                    except:
                        try:
                            doc_id = update['message']['photo'][-1]['file_id']
                            chat=update['message']['chat']['id']
                            try:
                                caption = update['message']['caption']
                            except:
                                caption=' '
                            sendPhoto(doc_id,caption,chat)
                        except:
                            try:
                                doc_id = update['message']['video']['file_id']
                                chat=update['message']['chat']['id']
                                try:
                                    caption = update['message']['caption']
                                except:
                                    caption=' '
                                sendVideo(doc_id,caption,chat)
                            except:
                                
                                
                                try:
                                    doc_id=update['message']['audio']['file_id']
                                    chat=update['message']['chat']['id']
                                    try:
                                        caption = update['message']['caption']
                                    except:
                                        caption=' '
                                    sendAudio(doc_id,caption,chat)
                                    
                                except:
                                    doc_id = update['message']['sticker']['file_id']
                                    chat=update['message']['chat']['id']
                                    sendSticker(doc_id,chat)

                
                                            
                
        except Exception as e:
            print(e)
        forwardMsg(update)                
        
        
        

def get_last_update_id(updates):
    update_ids = []
    for update in updates['result']:
        update_ids.append(int(update['update_id']))
    return max(update_ids)


last_update_id = None
while True:

    updates = get_updates(last_update_id)
    #print(updates)
    

    try:
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            print(last_update_id)
        
            uploader(updates)
    except:
        print('df')

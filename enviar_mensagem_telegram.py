#pip install python-telegram-bot
import asyncio
from telegram import Bot

telegram_token = 'SEU_TOKEN'
chat_id = 'SEU_CHAT_ID'
mensagem = 'teste pc'
foto = 'CAMINHO_FOTO'
video = "CAMINHO_VIDEO"
documento = 'CAMINHO_DOCUMENTO'

async def enviar_mensagem():
    bot = Bot(token=telegram_token)
    await bot.send_message(chat_id=chat_id, text=mensagem)
    #Envia arquivo
    await bot.send_document(chat_id=chat_id, document=open(documento, 'rb'))
    #Envia foto
    await bot.send_photo(chat_id=chat_id, photo=open(foto, 'rb'))
    #Envia video
    await bot.send_video(chat_id=chat_id, video=open(video, 'rb'))

loop = asyncio.get_event_loop()
loop.run_until_complete(enviar_mensagem())

'''
send_audio(): Envia um arquivo de áudio.
send_voice(): Envia uma mensagem de voz.
send_video_note(): Envia uma nota de vídeo (vídeo curto que será reproduzido quando selecionado).
send_sticker(): Envia um sticker (adesivo).
send_animation(): Envia uma animação (GIF ou arquivo de vídeo animado).
send_poll(): Envia uma enquete.
send_location(): Envia uma localização geográfica.
'''

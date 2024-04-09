from optparse import AmbiguousOptionError
from urllib import request
from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery


async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Тестовая покупка через Telegram bot',
        description='Тестируем возможность оплаты для пожертоваваний',
        payload='Техническая инфа для сбора статистики',
        provider_token='381764678:TEST:82388',
        currency='rub',
        prices=[
            LabeledPrice(
                label='Тестовое название продукта',
                amount=99000 # цена продукта *100
                ),
            LabeledPrice(
                label='НДС',
                amount=20000
                ),
            LabeledPrice(
                label='Скидка',
                amount=-20000
                ),
            LabeledPrice(
                    label='Бонус',
                    amount=-40000
                )
            ],
        max_tip_amount=5000,
        suggested_tip_amounts=[1000, 2000, 3000, 4000],
        start_parameter='research',
        provider_data=None,
        photo_url='https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.stack.imgur.com%2F6hlSI.png&lr=213&pos=1&rpt=simage&text=как%20создать%20новую%20ветку%20в%20git',
        photo_size=100,
        photo_height=450,
        photo_width=800,
        need_name=True,
        need_phone_number=True,
        need_email= True,
        need_shipping_address=False,
        send_phone_number_to_provider=True,
        send_email_to_provider=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=None, 
        request_timeout=15
        )
    

async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot): #handler для request_timeout=15
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
    
async def successful_payment(message: Message): #если пользователь оплатил, а мы подтвердили доставку
    msg = f'Спасибо за оплату {message.successful_payment.total_amount // 100} {message.successful_payment.currency}!' \
    f'\r\n Наш менеджер получил заявку и уже набирает Ваш номер телефона.' \
    f'\r\n Пока можете скачать цифровую версию продукта'
    await message.answer(msg)

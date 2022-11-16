from config import dp
from aiogram import executor
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from inline import *


@dp.message_handler(commands='start')
async def start(msg: Message):
    img = open("image/Без названия.jpg", "rb")
    text = f"Assalomu Aleykum {msg.from_user.full_name}, Musiqa botga Hush kelibsiz"
    await msg.answer_photo(img, caption=text, reply_markup=Start)


@dp.callback_query_handler(text="😡")
async def yoqmadi(call: CallbackQuery):
    await call.answer(f"Don't like 👎🏻", show_alert=True)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="😍")
async def yoqdi(call: CallbackQuery):
    await call.answer(f"Like 👍🏻", show_alert=True)
    await call.answer(cache_time=30)



@dp.callback_query_handler(text="telegram")
async def botlar(call: CallbackQuery):
    img = open("image/Experimental Alphabet.jpg", "rb")
    txt = f"1. Fast food - https://t.me/fast_food_ml_bot\n" \
          f"2. Free lesson course - https://t.me/free_lesson_course_bot"
    await call.message.answer_photo(img, txt, reply_markup=Start)
    await call.message.delete()


#Zarubej
@dp.callback_query_handler(text="zarubej")
async def zarubej(call: CallbackQuery):
    img = open("image/Иллюстрация наушников _ Премиум векторы.jpg", "rb")
    txt = f"1. Best friend(Feat. Doja cat\n" \
          f"2. Akcent - That's My Name\n" \
          f"3. AronChupa - I'm an Albatroaz\n" \
          f"4. Bruno Mars - to the moon\n" \
          f"5. David Tavare Summer Love\n" \
          f"6. Deadwood - BASS boossted\n" \
          f"7. Lyukke Li - I fallow\n" \
          f"8. Illkay & Inna - Talk\n" \
          f"9. Imany - Don't be so shy\n" \
          f"10. In Da Club - 50 Cent"
    await call.message.answer_photo(img, txt, reply_markup=Zarubej)
    await call.message.delete()

@dp.callback_query_handler(text="1")
async def one1(call: CallbackQuery):
    music = open("Car music/484027436896.m4a", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Best friend(Feat. Doja cat\n" \
          f"2. Akcent - That's My Name\n" \
          f"3. AronChupa - I'm an Albatroaz\n" \
          f"4. Bruno Mars - to the moon\n" \
          f"5. David Tavare Summer Love\n" \
          f"6. Deadwood - BASS boossted\n" \
          f"7. Lyukke Li - I fallow\n" \
          f"8. Illkay & Inna - Talk\n" \
          f"9. Imany - Don't be so shy\n" \
          f"10. In Da Club - 50 Cent"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="2")
async def one2(call: CallbackQuery):
    music = open("Car music/Akcent - That's My Name (Ultra Music).mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Best friend(Feat. Doja cat\n" \
          f"2. Akcent - That's My Name\n" \
          f"3. AronChupa - I'm an Albatroaz\n" \
          f"4. Bruno Mars - to the moon\n" \
          f"5. David Tavare Summer Love\n" \
          f"6. Deadwood - BASS boossted\n" \
          f"7. Lyukke Li - I fallow\n" \
          f"8. Illkay & Inna - Talk\n" \
          f"9. Imany - Don't be so shy\n" \
          f"10. In Da Club - 50 Cent"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="3")
async def one3(call: CallbackQuery):
    music = open("Car music/AronChupa - I'm an Albatroaz (Remix).mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Best friend(Feat. Doja cat\n" \
          f"2. Akcent - That's My Name\n" \
          f"3. AronChupa - I'm an Albatroaz\n" \
          f"4. Bruno Mars - to the moon\n" \
          f"5. David Tavare Summer Love\n" \
          f"6. Deadwood - BASS boossted\n" \
          f"7. Lyukke Li - I fallow\n" \
          f"8. Illkay & Inna - Talk\n" \
          f"9. Imany - Don't be so shy\n" \
          f"10. In Da Club - 50 Cent"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="4")
async def one4(call: CallbackQuery):
    music = open("Car music/Bruno Mars - to the moon.m4a", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Best friend(Feat. Doja cat\n" \
          f"2. Akcent - That's My Name\n" \
          f"3. AronChupa - I'm an Albatroaz\n" \
          f"4. Bruno Mars - to the moon\n" \
          f"5. David Tavare Summer Love\n" \
          f"6. Deadwood - BASS boossted\n" \
          f"7. Lyukke Li - I fallow\n" \
          f"8. Illkay & Inna - Talk\n" \
          f"9. Imany - Don't be so shy\n" \
          f"10. In Da Club - 50 Cent"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="5")
async def one5(call: CallbackQuery):
    music = open("Car music/David Tavare - Summer Love.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Best friend(Feat. Doja cat\n" \
          f"2. Akcent - That's My Name\n" \
          f"3. AronChupa - I'm an Albatroaz\n" \
          f"4. Bruno Mars - to the moon\n" \
          f"5. David Tavare Summer Love\n" \
          f"6. Deadwood - BASS boossted\n" \
          f"7. Lyukke Li - I fallow\n" \
          f"8. Illkay & Inna - Talk\n" \
          f"9. Imany - Don't be so shy\n" \
          f"10. In Da Club - 50 Cent"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="6")
async def one6(call: CallbackQuery):
    music = open("Car music/Deadwood ~ Bass Boosted by 𝑃ℎ𝑜𝑛𝑥.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Best friend(Feat. Doja cat\n" \
          f"2. Akcent - That's My Name\n" \
          f"3. AronChupa - I'm an Albatroaz\n" \
          f"4. Bruno Mars - to the moon\n" \
          f"5. David Tavare Summer Love\n" \
          f"6. Deadwood - BASS boossted\n" \
          f"7. Lyukke Li - I fallow\n" \
          f"8. Illkay & Inna - Talk\n" \
          f"9. Imany - Don't be so shy\n" \
          f"10. In Da Club - 50 Cent"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="7")
async def one7(call: CallbackQuery):
    music = open("Car music/I Fallow Rivers   Lykke Li.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Best friend(Feat. Doja cat\n" \
          f"2. Akcent - That's My Name\n" \
          f"3. AronChupa - I'm an Albatroaz\n" \
          f"4. Bruno Mars - to the moon\n" \
          f"5. David Tavare Summer Love\n" \
          f"6. Deadwood - BASS boossted\n" \
          f"7. Lyukke Li - I fallow\n" \
          f"8. Illkay & Inna - Talk\n" \
          f"9. Imany - Don't be so shy\n" \
          f"10. In Da Club - 50 Cent"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="8")
async def one8(call: CallbackQuery):
    music = open("Car music/Ilkay Sencan x INNA - Talk.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Best friend(Feat. Doja cat\n" \
          f"2. Akcent - That's My Name\n" \
          f"3. AronChupa - I'm an Albatroaz\n" \
          f"4. Bruno Mars - to the moon\n" \
          f"5. David Tavare Summer Love\n" \
          f"6. Deadwood - BASS boossted\n" \
          f"7. Lyukke Li - I fallow\n" \
          f"8. Illkay & Inna - Talk\n" \
          f"9. Imany - Don't be so shy\n" \
          f"10. In Da Club - 50 Cent"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="9")
async def one9(call: CallbackQuery):
    music = open("Car music/Imany - Don t Be So Shy (Filatov   Karas Remix)  Official Mu.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Best friend(Feat. Doja cat\n" \
          f"2. Akcent - That's My Name\n" \
          f"3. AronChupa - I'm an Albatroaz\n" \
          f"4. Bruno Mars - to the moon\n" \
          f"5. David Tavare Summer Love\n" \
          f"6. Deadwood - BASS boossted\n" \
          f"7. Lyukke Li - I fallow\n" \
          f"8. Illkay & Inna - Talk\n" \
          f"9. Imany - Don't be so shy\n" \
          f"10. In Da Club - 50 Cent"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="10")
async def one10(call: CallbackQuery):
    music = open("Car music/In Da Club   50 Cent.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Best friend(Feat. Doja cat\n" \
          f"2. Akcent - That's My Name\n" \
          f"3. AronChupa - I'm an Albatroaz\n" \
          f"4. Bruno Mars - to the moon\n" \
          f"5. David Tavare Summer Love\n" \
          f"6. Deadwood - BASS boossted\n" \
          f"7. Lyukke Li - I fallow\n" \
          f"8. Illkay & Inna - Talk\n" \
          f"9. Imany - Don't be so shy\n" \
          f"10. In Da Club - 50 Cent"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej)
    await call.answer(cache_time=30)


#zarubejorqaga
@dp.callback_query_handler(text="left1")
async def leftbosh(call: CallbackQuery):
    img = open("image/Без названия.jpg", "rb")
    txt = f"Bosh Sahifa"
    await call.message.answer_photo(img, txt, reply_markup=Start)
    await call.message.delete()

#Zarubej1
@dp.callback_query_handler(text="right1")
async def zarubej1(call: CallbackQuery):
    img = open("image/Иллюстрация наушников _ Премиум векторы.jpg", "rb")
    txt = f"11. Inna - Hot\n" \
          f"12. Manaskin - Beggin\n" \
          f"13. Mc Dg\n" \
          f"14. Minelli - Rampampam\n" \
          f"15. Music remix\n" \
          f"16. Remix muisc mp3\n" \
          f"17. Rihanna - Don't stop\n" \
          f"18. Snoop Dogg ft b-real - run\n" \
          f"19. The music basscar mp3\n" \
          f"20. The Black Eyed Peas - Shut up"
    await call.message.answer_photo(img, txt, reply_markup=Zarubej1)
    await call.message.delete()

@dp.callback_query_handler(text="11")
async def one11(call: CallbackQuery):
    music = open("Car music/Inna - Hot (Official Video HD).mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Inna - Hot\n" \
          f"12. Manaskin - Beggin\n" \
          f"13. Mc Dg\n" \
          f"14. Minelli - Rampampam\n" \
          f"15. Music remix\n" \
          f"16. Remix muisc mp3\n" \
          f"17. Rihanna - Don't stop\n" \
          f"18. Snoop Dogg ft b-real - run\n" \
          f"19. The music basscar mp3\n" \
          f"20. The Black Eyed Peas - Shut up"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="12")
async def one12(call: CallbackQuery):
    music = open("Car music/Manaskin - Beggin.m4a", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Inna - Hot\n" \
          f"12. Manaskin - Beggin\n" \
          f"13. Mc Dg\n" \
          f"14. Minelli - Rampampam\n" \
          f"15. Music remix\n" \
          f"16. Remix muisc mp3\n" \
          f"17. Rihanna - Don't stop\n" \
          f"18. Snoop Dogg ft b-real - run\n" \
          f"19. The music basscar mp3\n" \
          f"20. The Black Eyed Peas - Shut up"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="13")
async def one13(call: CallbackQuery):
    music = open("Car music/Mc Dg.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Inna - Hot\n" \
          f"12. Manaskin - Beggin\n" \
          f"13. Mc Dg\n" \
          f"14. Minelli - Rampampam\n" \
          f"15. Music remix\n" \
          f"16. Remix muisc mp3\n" \
          f"17. Rihanna - Don't stop\n" \
          f"18. Snoop Dogg ft b-real - run\n" \
          f"19. The music basscar mp3\n" \
          f"20. The Black Eyed Peas - Shut up"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="14")
async def one14(call: CallbackQuery):
    music = open("Car music/Minelli - Rampampam _ Official Video.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Inna - Hot\n" \
          f"12. Manaskin - Beggin\n" \
          f"13. Mc Dg\n" \
          f"14. Minelli - Rampampam\n" \
          f"15. Music remix\n" \
          f"16. Remix muisc mp3\n" \
          f"17. Rihanna - Don't stop\n" \
          f"18. Snoop Dogg ft b-real - run\n" \
          f"19. The music basscar mp3\n" \
          f"20. The Black Eyed Peas - Shut up"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="15")
async def one15(call: CallbackQuery):
    music = open("Car music/mrtrqg6wit15e0fjwv.m4a", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Inna - Hot\n" \
          f"12. Manaskin - Beggin\n" \
          f"13. Mc Dg\n" \
          f"14. Minelli - Rampampam\n" \
          f"15. Music remix\n" \
          f"16. Remix muisc mp3\n" \
          f"17. Rihanna - Don't stop\n" \
          f"18. Snoop Dogg ft b-real - run\n" \
          f"19. The music basscar mp3\n" \
          f"20. The Black Eyed Peas - Shut up"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="16")
async def one16(call: CallbackQuery):
    music = open("Car music/Remix music.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Inna - Hot\n" \
          f"12. Manaskin - Beggin\n" \
          f"13. Mc Dg\n" \
          f"14. Minelli - Rampampam\n" \
          f"15. Music remix\n" \
          f"16. Remix muisc mp3\n" \
          f"17. Rihanna - Don't stop\n" \
          f"18. Snoop Dogg ft b-real - run\n" \
          f"19. The music basscar mp3\n" \
          f"20. The Black Eyed Peas - Shut up"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="17")
async def one17(call: CallbackQuery):
    music = open("Car music/Rihanna - Don't Stop The Music.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Inna - Hot\n" \
          f"12. Manaskin - Beggin\n" \
          f"13. Mc Dg\n" \
          f"14. Minelli - Rampampam\n" \
          f"15. Music remix\n" \
          f"16. Remix muisc mp3\n" \
          f"17. Rihanna - Don't stop\n" \
          f"18. Snoop Dogg ft b-real - run\n" \
          f"19. The music basscar mp3\n" \
          f"20. The Black Eyed Peas - Shut up"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="18")
async def one18(call: CallbackQuery):
    music = open("Car music/snoop dogg ft b-real - run nigga run.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Inna - Hot\n" \
          f"12. Manaskin - Beggin\n" \
          f"13. Mc Dg\n" \
          f"14. Minelli - Rampampam\n" \
          f"15. Music remix\n" \
          f"16. Remix muisc mp3\n" \
          f"17. Rihanna - Don't stop\n" \
          f"18. Snoop Dogg ft b-real - run\n" \
          f"19. The music basscar mp3\n" \
          f"20. The Black Eyed Peas - Shut up"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="19")
async def one19(call: CallbackQuery):
    music = open("Car music/T.ME_MUSICBASS_CARS.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Inna - Hot\n" \
          f"12. Manaskin - Beggin\n" \
          f"13. Mc Dg\n" \
          f"14. Minelli - Rampampam\n" \
          f"15. Music remix\n" \
          f"16. Remix muisc mp3\n" \
          f"17. Rihanna - Don't stop\n" \
          f"18. Snoop Dogg ft b-real - run\n" \
          f"19. The music basscar mp3\n" \
          f"20. The Black Eyed Peas - Shut up"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="20")
async def one20(call: CallbackQuery):
    music = open("Car music/The Black Eyed Peas - Shut Up (Official Music Video).mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Inna - Hot\n" \
          f"12. Manaskin - Beggin\n" \
          f"13. Mc Dg\n" \
          f"14. Minelli - Rampampam\n" \
          f"15. Music remix\n" \
          f"16. Remix muisc mp3\n" \
          f"17. Rihanna - Don't stop\n" \
          f"18. Snoop Dogg ft b-real - run\n" \
          f"19. The music basscar mp3\n" \
          f"20. The Black Eyed Peas - Shut up"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej1)
    await call.answer(cache_time=30)

#zarubej orqaga1
@dp.callback_query_handler(text="left2")
async def leftzar1(call: CallbackQuery):
    img = open("image/Иллюстрация наушников _ Премиум векторы.jpg", "rb")
    txt = f"1. Best friend(Feat. Doja cat\n" \
          f"2. Akcent - That's My Name\n" \
          f"3. AronChupa - I'm an Albatroaz\n" \
          f"4. Bruno Mars - to the moon\n" \
          f"5. David Tavare Summer Love\n" \
          f"6. Deadwood - BASS boossted\n" \
          f"7. Lyukke Li - I fallow\n" \
          f"8. Illkay & Inna - Talk\n" \
          f"9. Imany - Don't be so shy\n" \
          f"10. In Da Club - 50 Cent"
    await call.message.answer_photo(img, txt, reply_markup=Zarubej)
    await call.message.delete()


#zarubej2
@dp.callback_query_handler(text="right2")
async def zarubej2(call: CallbackQuery):
    img = open("image/Иллюстрация наушников _ Премиум векторы.jpg", "rb")
    txt = f"21. Timbaland_The_Way - Sebastian\n" \
          f"22. Tom Boxer - Morena\n" \
          f"23. Zivert - Life\n" \
          f"24. Aromati - Luxor\n" \
          f"25. Чёрный мерен"
    await call.message.answer_photo(img, txt, reply_markup=Zarubej2)
    await call.message.delete()

@dp.callback_query_handler(text="21")
async def one21(call: CallbackQuery):
    music = open("Car music/Timbaland_The_Way_I_Are_ft_Keri_Hilson,_D_O_E_,_Sebastian_Official.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"21. Timbaland_The_Way - Sebastian\n" \
          f"22. Tom Boxer - Morena\n" \
          f"23. Zivert - Life\n" \
          f"24. Aromati - Luxor\n" \
          f"25. Чёрный мерен"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej2)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="22")
async def one22(call: CallbackQuery):
    music = open("Car music/Tom Boxer - Morena (Mert Altın Remix).mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"21. Timbaland_The_Way - Sebastian\n" \
          f"22. Tom Boxer - Morena\n" \
          f"23. Zivert - Life\n" \
          f"24. Aromati - Luxor\n" \
          f"25. Чёрный мерен"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej2)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="23")
async def one23(call: CallbackQuery):
    music = open("Car music/Zivert - Life   Премьера клипа.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"21. Timbaland_The_Way - Sebastian\n" \
          f"22. Tom Boxer - Morena\n" \
          f"23. Zivert - Life\n" \
          f"24. Aromati - Luxor\n" \
          f"25. Чёрный мерен"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej2)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="24")
async def one24(call: CallbackQuery):
    music = open("Car music/Ароматы   Luxor.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"21. Timbaland_The_Way - Sebastian\n" \
          f"22. Tom Boxer - Morena\n" \
          f"23. Zivert - Life\n" \
          f"24. Aromati - Luxor\n" \
          f"25. Чёрный мерен"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej2)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="25")
async def one25(call: CallbackQuery):
    music = open("Car music/Чёрный мерен.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"21. Timbaland_The_Way - Sebastian\n" \
          f"22. Tom Boxer - Morena\n" \
          f"23. Zivert - Life\n" \
          f"24. Aromati - Luxor\n" \
          f"25. Чёрный мерен"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Zarubej2)
    await call.answer(cache_time=30)


#zarube1 orqaga
@dp.callback_query_handler(text="left3")
async def zarubej1(call: CallbackQuery):
    img = open("image/Иллюстрация наушников _ Премиум векторы.jpg", "rb")
    txt = f"11. Inna - Hot\n" \
          f"12. Manaskin - Beggin\n" \
          f"13. Mc Dg\n" \
          f"14. Minelli - Rampampam\n" \
          f"15. Music remix\n" \
          f"16. Remix muisc mp3\n" \
          f"17. Rihanna - Don't stop\n" \
          f"18. Snoop Dogg ft b-real - run\n" \
          f"19. The music basscar mp3\n" \
          f"20. The Black Eyed Peas - Shut up"
    await call.message.answer_photo(img, txt, reply_markup=Zarubej1)
    await call.message.delete()








#russia
@dp.callback_query_handler(text="russia")
async def russia(call: CallbackQuery):
    img = open("image/Violin Fiddle Cello Piano Music logo.jpg", "rb")
    txt = f"Quyidagilarni tanlang!"
    await call.message.answer_photo(img, txt, reply_markup=Russia)
    await call.message.delete()

@dp.callback_query_handler(text="rleft")
async def rleft(call: CallbackQuery):
    img = open("image/Без названия.jpg", "rb")
    txt = f"Bosh Sahifa"
    await call.message.answer_photo(img, txt, reply_markup=Start)
    await call.message.delete()


#Hammali
@dp.callback_query_handler(text="Hammali")
async def hammali(call: CallbackQuery):
    img = open("image/Hammalinavai.jpg", "rb")
    txt = f"1. HammAli & Navai - Девочка война\n" \
          f"2. HammAli,_Loc-Dog-Любимая_песня\n" \
          f"3. HammAli & Navai - Запах снов\n" \
          f"4. HammAli & Navai - Ты моя химия\n" \
          f"5. HammAli & Navai – Ноты\n" \
          f"6. HammAli & Navai – Фары-Туманыm\n" \
          f"7. HammAli   Navai - Мама\n" \
          f"8. HammAli   Navai-1 - Цветок\n" \
          f"9. HammAli_&_Navai_Как_тебя_забыть\n" \
          f"10. HammAli_&_Navai_Привет,_ну_как.mp3"
    await call.message.answer_photo(img, txt, reply_markup=Hammali)
    await call.message.delete()

@dp.callback_query_handler(text="h1")
async def h1(call: CallbackQuery):
    music = open("Ruscha music/Hammali navai/191722385.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. HammAli & Navai - Девочка война\n" \
          f"2. HammAli,_Loc-Dog-Любимая_песня\n" \
          f"3. HammAli & Navai - Запах снов\n" \
          f"4. HammAli & Navai - Ты моя химия\n" \
          f"5. HammAli & Navai – Ноты\n" \
          f"6. HammAli & Navai – Фары-Туманыm\n" \
          f"7. HammAli   Navai - Мама\n" \
          f"8. HammAli   Navai-1 - Цветок\n" \
          f"9. HammAli_&_Navai_Как_тебя_забыть\n" \
          f"10. HammAli_&_Navai_Привет,_ну_как.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="h2")
async def h2(call: CallbackQuery):
    music = open("Ruscha music/Hammali navai/HammAli,_Loc-Dog-Любимая_песня.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. HammAli & Navai - Девочка война\n" \
          f"2. HammAli,_Loc-Dog-Любимая_песня\n" \
          f"3. HammAli & Navai - Запах снов\n" \
          f"4. HammAli & Navai - Ты моя химия\n" \
          f"5. HammAli & Navai – Ноты\n" \
          f"6. HammAli & Navai – Фары-Туманыm\n" \
          f"7. HammAli   Navai - Мама\n" \
          f"8. HammAli   Navai-1 - Цветок\n" \
          f"9. HammAli_&_Navai_Как_тебя_забыть\n" \
          f"10. HammAli_&_Navai_Привет,_ну_как.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="h3")
async def h3(call: CallbackQuery):
    music = open("Ruscha music/Hammali navai/HammAli & Navai - Запах снов.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. HammAli & Navai - Девочка война\n" \
          f"2. HammAli,_Loc-Dog-Любимая_песня\n" \
          f"3. HammAli & Navai - Запах снов\n" \
          f"4. HammAli & Navai - Ты моя химия\n" \
          f"5. HammAli & Navai – Ноты\n" \
          f"6. HammAli & Navai – Фары-Туманыm\n" \
          f"7. HammAli   Navai - Мама\n" \
          f"8. HammAli   Navai-1 - Цветок\n" \
          f"9. HammAli_&_Navai_Как_тебя_забыть\n" \
          f"10. HammAli_&_Navai_Привет,_ну_как.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="h4")
async def h4(call: CallbackQuery):
    music = open("Ruscha music/Hammali navai/HammAli & Navai - Ты моя химия.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. HammAli & Navai - Девочка война\n" \
          f"2. HammAli,_Loc-Dog-Любимая_песня\n" \
          f"3. HammAli & Navai - Запах снов\n" \
          f"4. HammAli & Navai - Ты моя химия\n" \
          f"5. HammAli & Navai – Ноты\n" \
          f"6. HammAli & Navai – Фары-Туманыm\n" \
          f"7. HammAli   Navai - Мама\n" \
          f"8. HammAli   Navai-1 - Цветок\n" \
          f"9. HammAli_&_Navai_Как_тебя_забыть\n" \
          f"10. HammAli_&_Navai_Привет,_ну_как.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="h5")
async def h5(call: CallbackQuery):
    music = open("Ruscha music/Hammali navai/HammAli & Navai – Ноты.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. HammAli & Navai - Девочка война\n" \
          f"2. HammAli,_Loc-Dog-Любимая_песня\n" \
          f"3. HammAli & Navai - Запах снов\n" \
          f"4. HammAli & Navai - Ты моя химия\n" \
          f"5. HammAli & Navai – Ноты\n" \
          f"6. HammAli & Navai – Фары-Туманыm\n" \
          f"7. HammAli   Navai - Мама\n" \
          f"8. HammAli   Navai-1 - Цветок\n" \
          f"9. HammAli_&_Navai_Как_тебя_забыть\n" \
          f"10. HammAli_&_Navai_Привет,_ну_как.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="h6")
async def h6(call: CallbackQuery):
    music = open("Ruscha music/Hammali navai/HammAli & Navai – Фары-Туманы.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. HammAli & Navai - Девочка война\n" \
          f"2. HammAli,_Loc-Dog-Любимая_песня\n" \
          f"3. HammAli & Navai - Запах снов\n" \
          f"4. HammAli & Navai - Ты моя химия\n" \
          f"5. HammAli & Navai – Ноты\n" \
          f"6. HammAli & Navai – Фары-Туманыm\n" \
          f"7. HammAli   Navai - Мама\n" \
          f"8. HammAli   Navai-1 - Цветок\n" \
          f"9. HammAli_&_Navai_Как_тебя_забыть\n" \
          f"10. HammAli_&_Navai_Привет,_ну_как.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="h7")
async def h7(call: CallbackQuery):
    music = open("Ruscha music/Hammali navai/HammAli   Navai - Мама.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. HammAli & Navai - Девочка война\n" \
          f"2. HammAli,_Loc-Dog-Любимая_песня\n" \
          f"3. HammAli & Navai - Запах снов\n" \
          f"4. HammAli & Navai - Ты моя химия\n" \
          f"5. HammAli & Navai – Ноты\n" \
          f"6. HammAli & Navai – Фары-Туманыm\n" \
          f"7. HammAli   Navai - Мама\n" \
          f"8. HammAli   Navai-1 - Цветок\n" \
          f"9. HammAli_&_Navai_Как_тебя_забыть\n" \
          f"10. HammAli_&_Navai_Привет,_ну_как.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="h8")
async def h8(call: CallbackQuery):
    music = open("Ruscha music/Hammali navai/HammAli   Navai-1 - Цветок.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. HammAli & Navai - Девочка война\n" \
          f"2. HammAli,_Loc-Dog-Любимая_песня\n" \
          f"3. HammAli & Navai - Запах снов\n" \
          f"4. HammAli & Navai - Ты моя химия\n" \
          f"5. HammAli & Navai – Ноты\n" \
          f"6. HammAli & Navai – Фары-Туманыm\n" \
          f"7. HammAli   Navai - Мама\n" \
          f"8. HammAli   Navai-1 - Цветок\n" \
          f"9. HammAli_&_Navai_Как_тебя_забыть\n" \
          f"10. HammAli_&_Navai_Привет,_ну_как.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="h9")
async def h9(call: CallbackQuery):
    music = open("Ruscha music/Hammali navai/HammAli_&_Navai_Как_тебя_забыть.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. HammAli & Navai - Девочка война\n" \
          f"2. HammAli,_Loc-Dog-Любимая_песня\n" \
          f"3. HammAli & Navai - Запах снов\n" \
          f"4. HammAli & Navai - Ты моя химия\n" \
          f"5. HammAli & Navai – Ноты\n" \
          f"6. HammAli & Navai – Фары-Туманыm\n" \
          f"7. HammAli   Navai - Мама\n" \
          f"8. HammAli   Navai-1 - Цветок\n" \
          f"9. HammAli_&_Navai_Как_тебя_забыть\n" \
          f"10. HammAli_&_Navai_Привет,_ну_как.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="h10")
async def h10(call: CallbackQuery):
    music = open("Ruscha music/Hammali navai/HammAli_&_Navai_Привет,_ну_как.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. HammAli & Navai - Девочка война\n" \
          f"2. HammAli,_Loc-Dog-Любимая_песня\n" \
          f"3. HammAli & Navai - Запах снов\n" \
          f"4. HammAli & Navai - Ты моя химия\n" \
          f"5. HammAli & Navai – Ноты\n" \
          f"6. HammAli & Navai – Фары-Туманыm\n" \
          f"7. HammAli   Navai - Мама\n" \
          f"8. HammAli   Navai-1 - Цветок\n" \
          f"9. HammAli_&_Navai_Как_тебя_забыть\n" \
          f"10. HammAli_&_Navai_Привет,_ну_как.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali)
    await call.answer(cache_time=30)



@dp.callback_query_handler(text="hleft")
async def horqaga(call: CallbackQuery):
    img = open("image/Без названия.jpg", "rb")
    txt = f"Bosh Sahifa"
    await call.message.answer_photo(img,  txt, reply_markup=Russia)
    await call.message.delete()


#Hammali1
@dp.callback_query_handler(text="hright")
async def hammali1(call: CallbackQuery):
    img = open("image/Hammalinavai.jpg", "rb")
    txt = f"11. HammAli_&_Navai_Сколько_не_виделись\n" \
          f"12. HammAli__Navai-Прятки\n" \
          f"13. hammali__navai_-_pamjat_ne_razrushit_(zf.fm)\n" \
          f"14. HammAli__Navai___Привет,_ну_как_ты_там_вообще\n" \
          f"15. HammAli_Navai_-_Zadyhayus\n" \
          f"16. JONY, HammAli & Navai – Без тебя я не я\n" \
          f"17. zenmusicorg_HammAli_Navai___KHoc" \
          f"18. Аномалия   HammAli   Navai\n" \
          f"19. Любить_это_так_бесполезно_HammAli_Navai\n" \
          f"20. Но_ты_меня_так_зацепила_Bass_prod"
    await call.message.answer_photo(img, txt, reply_markup=Hammali1)
    await call.message.delete()


@dp.callback_query_handler(text="h11")
async def h11(call: CallbackQuery):
    music = open("Ruscha music/HammAli_&_Navai_Сколько_не_виделись.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. HammAli_&_Navai_Сколько_не_виделись\n" \
          f"12. HammAli__Navai-Прятки\n" \
          f"13. hammali__navai_-_pamjat_ne_razrushit_(zf.fm)\n" \
          f"14. HammAli__Navai___Привет,_ну_как_ты_там_вообще\n" \
          f"15. HammAli_Navai_-_Zadyhayus\n" \
          f"16. JONY, HammAli & Navai – Без тебя я не я\n" \
          f"17. zenmusicorg_HammAli_Navai___KHoc" \
          f"18. Аномалия   HammAli   Navai\n" \
          f"19. Любить_это_так_бесполезно_HammAli_Navai\n" \
          f"20. Но_ты_меня_так_зацепила_Bass_prod"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="h12")
async def h12(call: CallbackQuery):
    music = open("Ruscha music/HammAli__Navai-Прятки.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. HammAli_&_Navai_Сколько_не_виделись\n" \
          f"12. HammAli__Navai-Прятки\n" \
          f"13. hammali__navai_-_pamjat_ne_razrushit_(zf.fm)\n" \
          f"14. HammAli__Navai___Привет,_ну_как_ты_там_вообще\n" \
          f"15. HammAli_Navai_-_Zadyhayus\n" \
          f"16. JONY, HammAli & Navai – Без тебя я не я\n" \
          f"17. zenmusicorg_HammAli_Navai___KHoc" \
          f"18. Аномалия   HammAli   Navai\n" \
          f"19. Любить_это_так_бесполезно_HammAli_Navai\n" \
          f"20. Но_ты_меня_так_зацепила_Bass_prod"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="h13")
async def h13(call: CallbackQuery):
    music = open("Ruscha music/Hammali navai/hammali__navai_-_pamjat_ne_razrushit_(zf.fm).mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. HammAli_&_Navai_Сколько_не_виделись\n" \
          f"12. HammAli__Navai-Прятки\n" \
          f"13. hammali__navai_-_pamjat_ne_razrushit_(zf.fm)\n" \
          f"14. HammAli__Navai___Привет,_ну_как_ты_там_вообще\n" \
          f"15. HammAli_Navai_-_Zadyhayus\n" \
          f"16. JONY, HammAli & Navai – Без тебя я не я\n" \
          f"17. zenmusicorg_HammAli_Navai___KHoc" \
          f"18. Аномалия   HammAli   Navai\n" \
          f"19. Любить_это_так_бесполезно_HammAli_Navai\n" \
          f"20. Но_ты_меня_так_зацепила_Bass_prod"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="h14")
async def h14(call: CallbackQuery):
    music = open("Ruscha music/Hammali navai/HammAli__Navai___Привет,_ну_как_ты_там_вообще.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. HammAli_&_Navai_Сколько_не_виделись\n" \
          f"12. HammAli__Navai-Прятки\n" \
          f"13. hammali__navai_-_pamjat_ne_razrushit_(zf.fm)\n" \
          f"14. HammAli__Navai___Привет,_ну_как_ты_там_вообще\n" \
          f"15. HammAli_Navai_-_Zadyhayus\n" \
          f"16. JONY, HammAli & Navai – Без тебя я не я\n" \
          f"17. zenmusicorg_HammAli_Navai___KHoc" \
          f"18. Аномалия   HammAli   Navai\n" \
          f"19. Любить_это_так_бесполезно_HammAli_Navai\n" \
          f"20. Но_ты_меня_так_зацепила_Bass_prod"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="h15")
async def h15(call: CallbackQuery):
    music = open("Ruscha music/Hammali navai/HammAli_Navai_-_Zadyhayus.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. HammAli_&_Navai_Сколько_не_виделись\n" \
          f"12. HammAli__Navai-Прятки\n" \
          f"13. hammali__navai_-_pamjat_ne_razrushit_(zf.fm)\n" \
          f"14. HammAli__Navai___Привет,_ну_как_ты_там_вообще\n" \
          f"15. HammAli_Navai_-_Zadyhayus\n" \
          f"16. JONY, HammAli & Navai – Без тебя я не я\n" \
          f"17. zenmusicorg_HammAli_Navai___KHoc" \
          f"18. Аномалия   HammAli   Navai\n" \
          f"19. Любить_это_так_бесполезно_HammAli_Navai\n" \
          f"20. Но_ты_меня_так_зацепила_Bass_prod"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="h16")
async def h16(call: CallbackQuery):
    music = open("Ruscha music/Hammali navai/JONY, HammAli & Navai – Без тебя я не я.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. HammAli_&_Navai_Сколько_не_виделись\n" \
          f"12. HammAli__Navai-Прятки\n" \
          f"13. hammali__navai_-_pamjat_ne_razrushit_(zf.fm)\n" \
          f"14. HammAli__Navai___Привет,_ну_как_ты_там_вообще\n" \
          f"15. HammAli_Navai_-_Zadyhayus\n" \
          f"16. JONY, HammAli & Navai – Без тебя я не я\n" \
          f"17. zenmusicorg_HammAli_Navai___KHoc" \
          f"18. Аномалия   HammAli   Navai\n" \
          f"19. Любить_это_так_бесполезно_HammAli_Navai\n" \
          f"20. Но_ты_меня_так_зацепила_Bass_prod"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="h17")
async def h17(call: CallbackQuery):
    music = open("Ruscha music/Hammali navai/zenmusicorg_HammAli_Navai___KHoc.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. HammAli_&_Navai_Сколько_не_виделись\n" \
          f"12. HammAli__Navai-Прятки\n" \
          f"13. hammali__navai_-_pamjat_ne_razrushit_(zf.fm)\n" \
          f"14. HammAli__Navai___Привет,_ну_как_ты_там_вообще\n" \
          f"15. HammAli_Navai_-_Zadyhayus\n" \
          f"16. JONY, HammAli & Navai – Без тебя я не я\n" \
          f"17. zenmusicorg_HammAli_Navai___KHoc" \
          f"18. Аномалия   HammAli   Navai\n" \
          f"19. Любить_это_так_бесполезно_HammAli_Navai\n" \
          f"20. Но_ты_меня_так_зацепила_Bass_prod"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali1)
    await call.answer(cache_time=30)



@dp.callback_query_handler(text="h18")
async def h18(call: CallbackQuery):
    music = open("Ruscha music/Hammali navai/Аномалия   HammAli   Navai.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. HammAli_&_Navai_Сколько_не_виделись\n" \
          f"12. HammAli__Navai-Прятки\n" \
          f"13. hammali__navai_-_pamjat_ne_razrushit_(zf.fm)\n" \
          f"14. HammAli__Navai___Привет,_ну_как_ты_там_вообще\n" \
          f"15. HammAli_Navai_-_Zadyhayus\n" \
          f"16. JONY, HammAli & Navai – Без тебя я не я\n" \
          f"17. zenmusicorg_HammAli_Navai___KHoc" \
          f"18. Аномалия   HammAli   Navai\n" \
          f"19. Любить_это_так_бесполезно_HammAli_Navai\n" \
          f"20. Но_ты_меня_так_зацепила_Bass_prod"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="h19")
async def h19(call: CallbackQuery):
    music = open("Ruscha music/Hammali navai/Любить_это_так_бесполезно_HammAli_Navai.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. HammAli_&_Navai_Сколько_не_виделись\n" \
          f"12. HammAli__Navai-Прятки\n" \
          f"13. hammali__navai_-_pamjat_ne_razrushit_(zf.fm)\n" \
          f"14. HammAli__Navai___Привет,_ну_как_ты_там_вообще\n" \
          f"15. HammAli_Navai_-_Zadyhayus\n" \
          f"16. JONY, HammAli & Navai – Без тебя я не я\n" \
          f"17. zenmusicorg_HammAli_Navai___KHoc" \
          f"18. Аномалия   HammAli   Navai\n" \
          f"19. Любить_это_так_бесполезно_HammAli_Navai\n" \
          f"20. Но_ты_меня_так_зацепила_Bass_prod"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="h20")
async def h20(call: CallbackQuery):
    music = open("Ruscha music/Hammali navai/Но_ты_меня_так_зацепила_Bass_prod.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. HammAli_&_Navai_Сколько_не_виделись\n" \
          f"12. HammAli__Navai-Прятки\n" \
          f"13. hammali__navai_-_pamjat_ne_razrushit_(zf.fm)\n" \
          f"14. HammAli__Navai___Привет,_ну_как_ты_там_вообще\n" \
          f"15. HammAli_Navai_-_Zadyhayus\n" \
          f"16. JONY, HammAli & Navai – Без тебя я не я\n" \
          f"17. zenmusicorg_HammAli_Navai___KHoc" \
          f"18. Аномалия   HammAli   Navai\n" \
          f"19. Любить_это_так_бесполезно_HammAli_Navai\n" \
          f"20. Но_ты_меня_так_зацепила_Bass_prod"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="hleft1")
async def hammali(call: CallbackQuery):
    img = open("image/Hammalinavai.jpg", "rb")
    txt = f"1. HammAli & Navai - Девочка война\n" \
          f"2. HammAli,_Loc-Dog-Любимая_песня\n" \
          f"3. HammAli & Navai - Запах снов\n" \
          f"4. HammAli & Navai - Ты моя химия\n" \
          f"5. HammAli & Navai – Ноты\n" \
          f"6. HammAli & Navai – Фары-Туманыm\n" \
          f"7. HammAli   Navai - Мама\n" \
          f"8. HammAli   Navai-1 - Цветок\n" \
          f"9. HammAli_&_Navai_Как_тебя_забыть\n" \
          f"10. HammAli_&_Navai_Привет,_ну_как"
    await call.message.answer_photo(img, txt, reply_markup=Hammali)
    await call.message.delete()


#Hammali2
@dp.callback_query_handler(text="hright1")
async def hammali2(call: CallbackQuery):
    img = open("image/Hammalinavai.jpg", "rb")
    txt = f"21. Почему_ты_опять_не_спишь_HammAli\n" \
          f"22.Ты позвонишь ночью    HammAli   Navai"
    await call.message.answer_photo(img, txt, reply_markup=Hammali2)
    await call.message.delete()

@dp.callback_query_handler(text="h21")
async def h21(call: CallbackQuery):
    music = open("Ruscha music/Hammali navai/Почему_ты_опять_не_спишь_HammAli.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"21. Почему_ты_опять_не_спишь_HammAli\n" \
          f"22.Ты позвонишь ночью    HammAli   Navai"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali2)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="h22")
async def h22(call: CallbackQuery):
    music = open("Ruscha music/Hammali navai/Ты позвонишь ночью    HammAli   Navai.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"21. Почему_ты_опять_не_спишь_HammAli\n" \
          f"22.Ты позвонишь ночью    HammAli   Navai"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Hammali2)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="hleft2")
async def hammali2(call: CallbackQuery):
    img = open("image/Hammalinavai.jpg", "rb")
    txt = f"11. HammAli_&_Navai_Сколько_не_виделись\n" \
          f"12. HammAli__Navai-Прятки\n" \
          f"13. hammali__navai_-_pamjat_ne_razrushit_(zf.fm)\n" \
          f"14. HammAli__Navai___Привет,_ну_как_ты_там_вообще\n" \
          f"15. HammAli_Navai_-_Zadyhayus\n" \
          f"16. JONY, HammAli & Navai – Без тебя я не я\n" \
          f"17. zenmusicorg_HammAli_Navai___KHoc" \
          f"18. Аномалия   HammAli   Navai\n" \
          f"19. Любить_это_так_бесполезно_HammAli_Navai\n" \
          f"20. Но_ты_меня_так_зацепила_Bass_prod"
    await call.message.answer_photo(img, txt, reply_markup=Hammali1)
    await call.message.delete()



#Jahkhalib
@dp.callback_query_handler(text="khalib")
async def jahkhalib(call: CallbackQuery):
    img = open("image/Jah Khalib — Воронеж.jpg", "rb")
    txt = f"1. HammAli_Navai_Jah_Khalib-Боже_как_завидую\n" \
          f"2. Jah Khalib - Моя Любовь\n" \
          f"3. Just Do it it.    Jah Khalib\n" \
          f"4. muzlome_Jah_Khalib_-_Tvoi_sonnye_glaza_48616018\n" \
          f"5. Muzmedia.uz-originalni\n" \
          f"6. Колыбельная   Jah Khalib\n" \
          f"7. Лейла(Vman Remix)   Jah Khalib\n" \
          f"8. На_своём_вайбе_feat_Гуф_Jah_Khalib_feat_Гуф\n" \
          f"9. Созвездие Ангела   Jah Khalib\n" \
          f"10. Jah_Khalib_Следуй_за_мной_Следуй_за_мной"
    await call.message.answer_photo(img, txt, reply_markup=Jahkhalib)
    await call.message.delete()


@dp.callback_query_handler(text="jh1")
async def jh1(call: CallbackQuery):
    music = open("Ruscha music/Jah khalib/HammAli_Navai_Jah_Khalib-Боже_как_завидую.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. HammAli_Navai_Jah_Khalib-Боже_как_завидую\n" \
          f"2. Jah Khalib - Моя Любовь\n" \
          f"3. Just Do it it.    Jah Khalib\n" \
          f"4. muzlome_Jah_Khalib_-_Tvoi_sonnye_glaza_48616018\n" \
          f"5. Muzmedia.uz-originalni\n" \
          f"6. Колыбельная   Jah Khalib\n" \
          f"7. Лейла(Vman Remix)   Jah Khalib\n" \
          f"8. На_своём_вайбе_feat_Гуф_Jah_Khalib_feat_Гуф\n" \
          f"9. Созвездие Ангела   Jah Khalib\n" \
          f"10. Jah_Khalib_Следуй_за_мной_Следуй_за_мной"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Jahkhalib)
    await call.answer(cache_time=30)



@dp.callback_query_handler(text="jh2")
async def jh2(call: CallbackQuery):
    music = open("Ruscha music/Jah khalib/Jah Khalib - Моя Любовь.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. HammAli_Navai_Jah_Khalib-Боже_как_завидую\n" \
          f"2. Jah Khalib - Моя Любовь\n" \
          f"3. Just Do it it.    Jah Khalib\n" \
          f"4. muzlome_Jah_Khalib_-_Tvoi_sonnye_glaza_48616018\n" \
          f"5. Muzmedia.uz-originalni\n" \
          f"6. Колыбельная   Jah Khalib\n" \
          f"7. Лейла(Vman Remix)   Jah Khalib\n" \
          f"8. На_своём_вайбе_feat_Гуф_Jah_Khalib_feat_Гуф\n" \
          f"9. Созвездие Ангела   Jah Khalib\n" \
          f"10. Jah_Khalib_Следуй_за_мной_Следуй_за_мной"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Jahkhalib)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="jh3")
async def jh3(call: CallbackQuery):
    music = open("Ruscha music/Jah khalib/Just Do it it.    Jah Khalib.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. HammAli_Navai_Jah_Khalib-Боже_как_завидую\n" \
          f"2. Jah Khalib - Моя Любовь\n" \
          f"3. Just Do it it.    Jah Khalib\n" \
          f"4. muzlome_Jah_Khalib_-_Tvoi_sonnye_glaza_48616018\n" \
          f"5. Muzmedia.uz-originalni\n" \
          f"6. Колыбельная   Jah Khalib\n" \
          f"7. Лейла(Vman Remix)   Jah Khalib\n" \
          f"8. На_своём_вайбе_feat_Гуф_Jah_Khalib_feat_Гуф\n" \
          f"9. Созвездие Ангела   Jah Khalib\n" \
          f"10. Jah_Khalib_Следуй_за_мной_Следуй_за_мной"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Jahkhalib)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="jh4")
async def jh4(call: CallbackQuery):
    music = open("Ruscha music/Jah khalib/muzlome_Jah_Khalib_-_Tvoi_sonnye_glaza_48616018.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. HammAli_Navai_Jah_Khalib-Боже_как_завидую\n" \
          f"2. Jah Khalib - Моя Любовь\n" \
          f"3. Just Do it it.    Jah Khalib\n" \
          f"4. muzlome_Jah_Khalib_-_Tvoi_sonnye_glaza_48616018\n" \
          f"5. Muzmedia.uz-originalni\n" \
          f"6. Колыбельная   Jah Khalib\n" \
          f"7. Лейла(Vman Remix)   Jah Khalib\n" \
          f"8. На_своём_вайбе_feat_Гуф_Jah_Khalib_feat_Гуф\n" \
          f"9. Созвездие Ангела   Jah Khalib\n" \
          f"10. Jah_Khalib_Следуй_за_мной_Следуй_за_мной"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Jahkhalib)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="jh5")
async def jh5(call: CallbackQuery):
    music = open("Ruscha music/Jah khalib/Muzmedia.uz-originalni.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. HammAli_Navai_Jah_Khalib-Боже_как_завидую\n" \
          f"2. Jah Khalib - Моя Любовь\n" \
          f"3. Just Do it it.    Jah Khalib\n" \
          f"4. muzlome_Jah_Khalib_-_Tvoi_sonnye_glaza_48616018\n" \
          f"5. Muzmedia.uz-originalni\n" \
          f"6. Колыбельная   Jah Khalib\n" \
          f"7. Лейла(Vman Remix)   Jah Khalib\n" \
          f"8. На_своём_вайбе_feat_Гуф_Jah_Khalib_feat_Гуф\n" \
          f"9. Созвездие Ангела   Jah Khalib\n" \
          f"10. Jah_Khalib_Следуй_за_мной_Следуй_за_мной"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Jahkhalib)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="jh6")
async def jh6(call: CallbackQuery):
    music = open("Ruscha music/Jah khalib/Колыбельная   Jah Khalib.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. HammAli_Navai_Jah_Khalib-Боже_как_завидую\n" \
          f"2. Jah Khalib - Моя Любовь\n" \
          f"3. Just Do it it.    Jah Khalib\n" \
          f"4. muzlome_Jah_Khalib_-_Tvoi_sonnye_glaza_48616018\n" \
          f"5. Muzmedia.uz-originalni\n" \
          f"6. Колыбельная   Jah Khalib\n" \
          f"7. Лейла(Vman Remix)   Jah Khalib\n" \
          f"8. На_своём_вайбе_feat_Гуф_Jah_Khalib_feat_Гуф\n" \
          f"9. Созвездие Ангела   Jah Khalib\n" \
          f"10. Jah_Khalib_Следуй_за_мной_Следуй_за_мной"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Jahkhalib)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="jh7")
async def jh7(call: CallbackQuery):
    music = open("Ruscha music/Jah khalib/Лейла(Vman Remix)   Jah Khalib.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. HammAli_Navai_Jah_Khalib-Боже_как_завидую\n" \
          f"2. Jah Khalib - Моя Любовь\n" \
          f"3. Just Do it it.    Jah Khalib\n" \
          f"4. muzlome_Jah_Khalib_-_Tvoi_sonnye_glaza_48616018\n" \
          f"5. Muzmedia.uz-originalni\n" \
          f"6. Колыбельная   Jah Khalib\n" \
          f"7. Лейла(Vman Remix)   Jah Khalib\n" \
          f"8. На_своём_вайбе_feat_Гуф_Jah_Khalib_feat_Гуф\n" \
          f"9. Созвездие Ангела   Jah Khalib\n" \
          f"10. Jah_Khalib_Следуй_за_мной_Следуй_за_мной"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Jahkhalib)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="jh8")
async def jh8(call: CallbackQuery):
    music = open("Ruscha music/Jah khalib/На_своём_вайбе_feat_Гуф_Jah_Khalib_feat_Гуф.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. HammAli_Navai_Jah_Khalib-Боже_как_завидую\n" \
          f"2. Jah Khalib - Моя Любовь\n" \
          f"3. Just Do it it.    Jah Khalib\n" \
          f"4. muzlome_Jah_Khalib_-_Tvoi_sonnye_glaza_48616018\n" \
          f"5. Muzmedia.uz-originalni\n" \
          f"6. Колыбельная   Jah Khalib\n" \
          f"7. Лейла(Vman Remix)   Jah Khalib\n" \
          f"8. На_своём_вайбе_feat_Гуф_Jah_Khalib_feat_Гуф\n" \
          f"9. Созвездие Ангела   Jah Khalib\n" \
          f"10. Jah_Khalib_Следуй_за_мной_Следуй_за_мной"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Jahkhalib)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="jh9")
async def jh9(call: CallbackQuery):
    music = open("Ruscha music/Jah khalib/Созвездие Ангела   Jah Khalib", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. HammAli_Navai_Jah_Khalib-Боже_как_завидую\n" \
          f"2. Jah Khalib - Моя Любовь\n" \
          f"3. Just Do it it.    Jah Khalib\n" \
          f"4. muzlome_Jah_Khalib_-_Tvoi_sonnye_glaza_48616018\n" \
          f"5. Muzmedia.uz-originalni\n" \
          f"6. Колыбельная   Jah Khalib\n" \
          f"7. Лейла(Vman Remix)   Jah Khalib\n" \
          f"8. На_своём_вайбе_feat_Гуф_Jah_Khalib_feat_Гуф\n" \
          f"9. Созвездие Ангела   Jah Khalib\n" \
          f"10. Jah_Khalib_Следуй_за_мной_Следуй_за_мной"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Jahkhalib)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="jh10")
async def jh10(call: CallbackQuery):
    music = open("Ruscha music/Jah khalib/Jah_Khalib_Следуй_за_мной_Следуй_за_мной", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. HammAli_Navai_Jah_Khalib-Боже_как_завидую\n" \
          f"2. Jah Khalib - Моя Любовь\n" \
          f"3. Just Do it it.    Jah Khalib\n" \
          f"4. muzlome_Jah_Khalib_-_Tvoi_sonnye_glaza_48616018\n" \
          f"5. Muzmedia.uz-originalni\n" \
          f"6. Колыбельная   Jah Khalib\n" \
          f"7. Лейла(Vman Remix)   Jah Khalib\n" \
          f"8. На_своём_вайбе_feat_Гуф_Jah_Khalib_feat_Гуф\n" \
          f"9. Созвездие Ангела   Jah Khalib\n" \
          f"10. Jah_Khalib_Следуй_за_мной_Следуй_за_мной"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Jahkhalib)
    await call.answer(cache_time=30)



@dp.callback_query_handler(text="jhleft")
async def jhleft(call: CallbackQuery):
    img = open("image/Violin Fiddle Cello Piano Music logo.jpg", "rb")
    txt = f"Bosj Sahifa"
    await call.message.answer_photo(img, txt, reply_markup=Russia)
    await call.message.delete()




#Miyagi
@dp.callback_query_handler(text="miyagi")
async def miyagi(call: CallbackQuery):
    img = open("image/MIYAGI - Untitled Collection #255604526 _ OpenSea.png", "rb")
    txt = f"1. Miyagi - Заплаканная (feat. Amigo)\n" \
          f"2. 10_MiyaGi-Syn.mp3\n" \
          f"3. Miyagi 808945204\n" \
          f"4. Miya Giaudio  \n" \
          f"5. Captain   MiyaGi\n" \
          f"6. Dlbm   MiyaGi   Endshpil , NERAK\n" \
          f"7. Fire Man   Miyagi   Эндшпиль  \n" \
          f"8. Miyagi   Andy Panda Kosandra [NR] \n" \
          f"9. Miyagi & Andy Panda - Utopia\n" \
          f"10. MiyaGi & Эндшпиль - Колизей"
    await call.message.answer_photo(img, txt, reply_markup=Miyagi)
    await call.message.delete()



@dp.callback_query_handler(text="m1")
async def m1(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/2_5379812503813357649.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Miyagi - Заплаканная (feat. Amigo)\n" \
          f"2. 10_MiyaGi-Syn.mp3\n" \
          f"3. Miyagi 808945204\n" \
          f"4. Miya Giaudio  \n" \
          f"5. Captain   MiyaGi\n" \
          f"6. Dlbm   MiyaGi   Endshpil , NERAK\n" \
          f"7. Fire Man   Miyagi   Эндшпиль  \n" \
          f"8. Miyagi   Andy Panda Kosandra [NR] \n" \
          f"9. Miyagi & Andy Panda - Utopia\n" \
          f"10. MiyaGi & Эндшпиль - Колизей"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="m2")
async def m2(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/10_MiyaGi-Syn", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Miyagi - Заплаканная (feat. Amigo)\n" \
          f"2. 10_MiyaGi-Syn.mp3\n" \
          f"3. Miyagi 808945204\n" \
          f"4. Miya Giaudio  \n" \
          f"5. Captain   MiyaGi\n" \
          f"6. Dlbm   MiyaGi   Endshpil , NERAK\n" \
          f"7. Fire Man   Miyagi   Эндшпиль  \n" \
          f"8. Miyagi   Andy Panda Kosandra [NR] \n" \
          f"9. Miyagi & Andy Panda - Utopia\n" \
          f"10. MiyaGi & Эндшпиль - Колизей"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="m3")
async def m3(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/808945204.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Miyagi - Заплаканная (feat. Amigo)\n" \
          f"2. 10_MiyaGi-Syn.mp3\n" \
          f"3. Miyagi 808945204\n" \
          f"4. Miya Giaudio  \n" \
          f"5. Captain   MiyaGi\n" \
          f"6. Dlbm   MiyaGi   Endshpil , NERAK\n" \
          f"7. Fire Man   Miyagi   Эндшпиль  \n" \
          f"8. Miyagi   Andy Panda Kosandra [NR] \n" \
          f"9. Miyagi & Andy Panda - Utopia\n" \
          f"10. MiyaGi & Эндшпиль - Колизей"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="m4")
async def m4(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/audio.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Miyagi - Заплаканная (feat. Amigo)\n" \
          f"2. 10_MiyaGi-Syn.mp3\n" \
          f"3. Miyagi 808945204\n" \
          f"4. Miya Giaudio  \n" \
          f"5. Captain   MiyaGi\n" \
          f"6. Dlbm   MiyaGi   Endshpil , NERAK\n" \
          f"7. Fire Man   Miyagi   Эндшпиль  \n" \
          f"8. Miyagi   Andy Panda Kosandra [NR] \n" \
          f"9. Miyagi & Andy Panda - Utopia\n" \
          f"10. MiyaGi & Эндшпиль - Колизей"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi)
    await call.answer(cache_time=30)



@dp.callback_query_handler(text="m5")
async def m5(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/Captain   MiyaGi.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Miyagi - Заплаканная (feat. Amigo)\n" \
          f"2. 10_MiyaGi-Syn.mp3\n" \
          f"3. Miyagi 808945204\n" \
          f"4. Miya Giaudio  \n" \
          f"5. Captain   MiyaGi\n" \
          f"6. Dlbm   MiyaGi   Endshpil , NERAK\n" \
          f"7. Fire Man   Miyagi   Эндшпиль  \n" \
          f"8. Miyagi   Andy Panda Kosandra [NR] \n" \
          f"9. Miyagi & Andy Panda - Utopia\n" \
          f"10. MiyaGi & Эндшпиль - Колизей"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="m6")
async def m6(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/Dlbm   MiyaGi   Endshpil , NERAK.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Miyagi - Заплаканная (feat. Amigo)\n" \
          f"2. 10_MiyaGi-Syn.mp3\n" \
          f"3. Miyagi 808945204\n" \
          f"4. Miya Giaudio  \n" \
          f"5. Captain   MiyaGi\n" \
          f"6. Dlbm   MiyaGi   Endshpil , NERAK\n" \
          f"7. Fire Man   Miyagi   Эндшпиль  \n" \
          f"8. Miyagi   Andy Panda Kosandra [NR] \n" \
          f"9. Miyagi & Andy Panda - Utopia\n" \
          f"10. MiyaGi & Эндшпиль - Колизей"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi)
    await call.answer(cache_time=30)



@dp.callback_query_handler(text="m7")
async def m7(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/Fire Man   Miyagi   Эндшпиль.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Miyagi - Заплаканная (feat. Amigo)\n" \
          f"2. 10_MiyaGi-Syn.mp3\n" \
          f"3. Miyagi 808945204\n" \
          f"4. Miya Giaudio  \n" \
          f"5. Captain   MiyaGi\n" \
          f"6. Dlbm   MiyaGi   Endshpil , NERAK\n" \
          f"7. Fire Man   Miyagi   Эндшпиль  \n" \
          f"8. Miyagi   Andy Panda Kosandra [NR] \n" \
          f"9. Miyagi & Andy Panda - Utopia\n" \
          f"10. MiyaGi & Эндшпиль - Колизей"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="m8")
async def m8(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/Kosandra [NR]   Miyagi   Andy Panda.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Miyagi - Заплаканная (feat. Amigo)\n" \
          f"2. 10_MiyaGi-Syn.mp3\n" \
          f"3. Miyagi 808945204\n" \
          f"4. Miya Giaudio  \n" \
          f"5. Captain   MiyaGi\n" \
          f"6. Dlbm   MiyaGi   Endshpil , NERAK\n" \
          f"7. Fire Man   Miyagi   Эндшпиль  \n" \
          f"8. Miyagi   Andy Panda Kosandra [NR] \n" \
          f"9. Miyagi & Andy Panda - Utopia\n" \
          f"10. MiyaGi & Эндшпиль - Колизей"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi)
    await call.answer(cache_time=30)



@dp.callback_query_handler(text="m9")
async def m9(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/Miyagi & Andy Panda - Utopia.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Miyagi - Заплаканная (feat. Amigo)\n" \
          f"2. 10_MiyaGi-Syn.mp3\n" \
          f"3. Miyagi 808945204\n" \
          f"4. Miya Giaudio  \n" \
          f"5. Captain   MiyaGi\n" \
          f"6. Dlbm   MiyaGi   Endshpil , NERAK\n" \
          f"7. Fire Man   Miyagi   Эндшпиль  \n" \
          f"8. Miyagi   Andy Panda Kosandra [NR] \n" \
          f"9. Miyagi & Andy Panda - Utopia\n" \
          f"10. MiyaGi & Эндшпиль - Колизей"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="m10")
async def m10(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/MiyaGi & Эндшпиль - Колизей.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Miyagi - Заплаканная (feat. Amigo)\n" \
          f"2. 10_MiyaGi-Syn.mp3\n" \
          f"3. Miyagi 808945204\n" \
          f"4. Miya Giaudio  \n" \
          f"5. Captain   MiyaGi\n" \
          f"6. Dlbm   MiyaGi   Endshpil , NERAK\n" \
          f"7. Fire Man   Miyagi   Эндшпиль  \n" \
          f"8. Miyagi   Andy Panda Kosandra [NR] \n" \
          f"9. Miyagi & Andy Panda - Utopia\n" \
          f"10. MiyaGi & Эндшпиль - Колизей"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi)
    await call.answer(cache_time=30)


#miyagiorqa
@dp.callback_query_handler(text="mleft")
async def leftbosh(call: CallbackQuery):
    img = open("image/Violin Fiddle Cello Piano Music logo.jpg", "rb")
    txt = f"Bosh Sahifa"
    await call.message.answer_photo(img, txt, reply_markup=Russia)
    await call.message.delete()


#Miyagi1
@dp.callback_query_handler(text="mright")
async def miyagi1(call: CallbackQuery):
    img = open("image/miyagi.png", "rb")
    txt = f"11. Miyagi & Эндшпиль - Ночь (Official Audio)\n" \
          f"12. Miyagi - Эндшпиль-Не теряя\n" \
          f"13. Miyagi feat Andy Panda - Там Ревели Горы \n" \
          f"14. Miyagi-jendshpil-rapapam-remix-edit_Kamola.net\n" \
          f"15. Miyagi-Malboro\n" \
          f"16. MiyaGi_&_Эндшпиль_Люби_меня_ft_Сим\n" \
          f"17. MiyaGi___I_Got_Iove\n" \
          f"18. Miyagi_feat._Kadi-Родная_пой\n" \
          f"19. Silhouette - Miyagi   Эндшпиль\n" \
          f"20. Where Are You - Ollane feat Miyagi Andy Panda.mp3"
    await call.message.answer_photo(img, txt, reply_markup=Miyagi1)
    await call.message.delete()



@dp.callback_query_handler(text="m11")
async def m11(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/Miyagi & Эндшпиль - Ночь (Official Audio).mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Miyagi & Эндшпиль - Ночь (Official Audio)\n" \
          f"12. Miyagi - Эндшпиль-Не теряя\n" \
          f"13. Miyagi feat Andy Panda - Там Ревели Горы \n" \
          f"14. Miyagi-jendshpil-rapapam-remix-edit_Kamola.net\n" \
          f"15. Miyagi-Malboro\n" \
          f"16. MiyaGi_&_Эндшпиль_Люби_меня_ft_Сим\n" \
          f"17. MiyaGi___I_Got_Iove\n" \
          f"18. Miyagi_feat._Kadi-Родная_пой\n" \
          f"19. Silhouette - Miyagi   Эндшпиль\n" \
          f"20. Where Are You - Ollane feat Miyagi Andy Panda.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="m12")
async def m12(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/Miyagi - Эндшпиль-Не теряя.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Miyagi & Эндшпиль - Ночь (Official Audio)\n" \
          f"12. Miyagi - Эндшпиль-Не теряя\n" \
          f"13. Miyagi feat Andy Panda - Там Ревели Горы \n" \
          f"14. Miyagi-jendshpil-rapapam-remix-edit_Kamola.net\n" \
          f"15. Miyagi-Malboro\n" \
          f"16. MiyaGi_&_Эндшпиль_Люби_меня_ft_Сим\n" \
          f"17. MiyaGi___I_Got_Iove\n" \
          f"18. Miyagi_feat._Kadi-Родная_пой\n" \
          f"19. Silhouette - Miyagi   Эндшпиль\n" \
          f"20. Where Are You - Ollane feat Miyagi Andy Panda.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="m13")
async def m13(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/Miyagi feat Andy Panda - Там Ревели Горы .mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Miyagi & Эндшпиль - Ночь (Official Audio)\n" \
          f"12. Miyagi - Эндшпиль-Не теряя\n" \
          f"13. Miyagi feat Andy Panda - Там Ревели Горы \n" \
          f"14. Miyagi-jendshpil-rapapam-remix-edit_Kamola.net\n" \
          f"15. Miyagi-Malboro\n" \
          f"16. MiyaGi_&_Эндшпиль_Люби_меня_ft_Сим\n" \
          f"17. MiyaGi___I_Got_Iove\n" \
          f"18. Miyagi_feat._Kadi-Родная_пой\n" \
          f"19. Silhouette - Miyagi   Эндшпиль\n" \
          f"20. Where Are You - Ollane feat Miyagi Andy Panda.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="m14")
async def m14(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/Miyagi-jendshpil-rapapam-remix-edit_Kamola.net.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Miyagi & Эндшпиль - Ночь (Official Audio)\n" \
          f"12. Miyagi - Эндшпиль-Не теряя\n" \
          f"13. Miyagi feat Andy Panda - Там Ревели Горы \n" \
          f"14. Miyagi-jendshpil-rapapam-remix-edit_Kamola.net\n" \
          f"15. Miyagi-Malboro\n" \
          f"16. MiyaGi_&_Эндшпиль_Люби_меня_ft_Сим\n" \
          f"17. MiyaGi___I_Got_Iove\n" \
          f"18. Miyagi_feat._Kadi-Родная_пой\n" \
          f"19. Silhouette - Miyagi   Эндшпиль\n" \
          f"20. Where Are You - Ollane feat Miyagi Andy Panda.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="m15")
async def m15(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/Miyagi-Malboro.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Miyagi & Эндшпиль - Ночь (Official Audio)\n" \
          f"12. Miyagi - Эндшпиль-Не теряя\n" \
          f"13. Miyagi feat Andy Panda - Там Ревели Горы \n" \
          f"14. Miyagi-jendshpil-rapapam-remix-edit_Kamola.net\n" \
          f"15. Miyagi-Malboro\n" \
          f"16. MiyaGi_&_Эндшпиль_Люби_меня_ft_Сим\n" \
          f"17. MiyaGi___I_Got_Iove\n" \
          f"18. Miyagi_feat._Kadi-Родная_пой\n" \
          f"19. Silhouette - Miyagi   Эндшпиль\n" \
          f"20. Where Are You - Ollane feat Miyagi Andy Panda.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="m16")
async def m16(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/MiyaGi_&_Эндшпиль_Люби_меня_ft_Сим.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Miyagi & Эндшпиль - Ночь (Official Audio)\n" \
          f"12. Miyagi - Эндшпиль-Не теряя\n" \
          f"13. Miyagi feat Andy Panda - Там Ревели Горы \n" \
          f"14. Miyagi-jendshpil-rapapam-remix-edit_Kamola.net\n" \
          f"15. Miyagi-Malboro\n" \
          f"16. MiyaGi_&_Эндшпиль_Люби_меня_ft_Сим\n" \
          f"17. MiyaGi___I_Got_Iove\n" \
          f"18. Miyagi_feat._Kadi-Родная_пой\n" \
          f"19. Silhouette - Miyagi   Эндшпиль\n" \
          f"20. Where Are You - Ollane feat Miyagi Andy Panda.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="m17")
async def m15(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/MiyaGi___I_Got_Iove.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Miyagi & Эндшпиль - Ночь (Official Audio)\n" \
          f"12. Miyagi - Эндшпиль-Не теряя\n" \
          f"13. Miyagi feat Andy Panda - Там Ревели Горы \n" \
          f"14. Miyagi-jendshpil-rapapam-remix-edit_Kamola.net\n" \
          f"15. Miyagi-Malboro\n" \
          f"16. MiyaGi_&_Эндшпиль_Люби_меня_ft_Сим\n" \
          f"17. MiyaGi___I_Got_Iove\n" \
          f"18. Miyagi_feat._Kadi-Родная_пой\n" \
          f"19. Silhouette - Miyagi   Эндшпиль\n" \
          f"20. Where Are You - Ollane feat Miyagi Andy Panda.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="m18")
async def m18(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/Miyagi_feat._Kadi-Родная_пой.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Miyagi & Эндшпиль - Ночь (Official Audio)\n" \
          f"12. Miyagi - Эндшпиль-Не теряя\n" \
          f"13. Miyagi feat Andy Panda - Там Ревели Горы \n" \
          f"14. Miyagi-jendshpil-rapapam-remix-edit_Kamola.net\n" \
          f"15. Miyagi-Malboro\n" \
          f"16. MiyaGi_&_Эндшпиль_Люби_меня_ft_Сим\n" \
          f"17. MiyaGi___I_Got_Iove\n" \
          f"18. Miyagi_feat._Kadi-Родная_пой\n" \
          f"19. Silhouette - Miyagi   Эндшпиль\n" \
          f"20. Where Are You - Ollane feat Miyagi Andy Panda.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi1)
    await call.answer(cache_time=30)



@dp.callback_query_handler(text="m19")
async def m19(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/Silhouette - Miyagi   Эндшпиль.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Miyagi & Эндшпиль - Ночь (Official Audio)\n" \
          f"12. Miyagi - Эндшпиль-Не теряя\n" \
          f"13. Miyagi feat Andy Panda - Там Ревели Горы \n" \
          f"14. Miyagi-jendshpil-rapapam-remix-edit_Kamola.net\n" \
          f"15. Miyagi-Malboro\n" \
          f"16. MiyaGi_&_Эндшпиль_Люби_меня_ft_Сим\n" \
          f"17. MiyaGi___I_Got_Iove\n" \
          f"18. Miyagi_feat._Kadi-Родная_пой\n" \
          f"19. Silhouette - Miyagi   Эндшпиль\n" \
          f"20. Where Are You - Ollane feat Miyagi Andy Panda.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="m20")
async def m20(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/Where Are You - Ollane feat Miyagi Andy Panda.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Miyagi & Эндшпиль - Ночь (Official Audio)\n" \
          f"12. Miyagi - Эндшпиль-Не теряя\n" \
          f"13. Miyagi feat Andy Panda - Там Ревели Горы \n" \
          f"14. Miyagi-jendshpil-rapapam-remix-edit_Kamola.net\n" \
          f"15. Miyagi-Malboro\n" \
          f"16. MiyaGi_&_Эндшпиль_Люби_меня_ft_Сим\n" \
          f"17. MiyaGi___I_Got_Iove\n" \
          f"18. Miyagi_feat._Kadi-Родная_пой\n" \
          f"19. Silhouette - Miyagi   Эндшпиль\n" \
          f"20. Where Are You - Ollane feat Miyagi Andy Panda.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi1)
    await call.answer(cache_time=30)


#miyagiorqa
@dp.callback_query_handler(text="mleft1")
async def mleft1(call: CallbackQuery):
    img = open("image/MIYAGI - Untitled Collection #255604526 _ OpenSea.png", "rb")
    txt = f"1. Miyagi - Заплаканная (feat. Amigo)\n" \
          f"2. 10_MiyaGi-Syn.mp3\n" \
          f"3. Miyagi 808945204\n" \
          f"4. Miya Giaudio  \n" \
          f"5. Captain   MiyaGi\n" \
          f"6. Dlbm   MiyaGi   Endshpil , NERAK\n" \
          f"7. Fire Man   Miyagi   Эндшпиль  \n" \
          f"8. Miyagi   Andy Panda Kosandra [NR] \n" \
          f"9. Miyagi & Andy Panda - Utopia\n" \
          f"10. MiyaGi & Эндшпиль - Колизей"
    await call.message.answer_photo(img, txt, reply_markup=Miyagi)
    await call.message.delete()

#Miyagi2
@dp.callback_query_handler(text="mright1")
async def miyagi2(call: CallbackQuery):
    img = open("image/Watch this reel by miyagi_clan on Instagram.jpg", "rb")
    txt = f"21. Yamakasi   Miyagi,Andy Panda\n" \
          f"22. Заново жить    MiyaGi\n" \
          f"23. Не жалея - Miyagi Andy Panda\n" \
          f"24. Самурай   Miyagi"
    await call.message.answer_photo(img, txt, reply_markup=Miyagi2)
    await call.message.delete()

@dp.callback_query_handler(text="m21")
async def m21(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/Yamakasi   Miyagi,Andy Panda.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"21. Yamakasi   Miyagi,Andy Panda\n" \
          f"22. Заново жить    MiyaGi\n" \
          f"23. Не жалея - Miyagi Andy Panda\n" \
          f"24. Самурай   Miyagi"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi2)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="m22")
async def m22(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/Заново жить    MiyaGi.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"21. Yamakasi   Miyagi,Andy Panda\n" \
          f"22. Заново жить    MiyaGi\n" \
          f"23. Не жалея - Miyagi Andy Panda\n" \
          f"24. Самурай   Miyagi"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi2)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="m23")
async def m23(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/Не жалея - Miyagi Andy Panda.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"21. Yamakasi   Miyagi,Andy Panda\n" \
          f"22. Заново жить    MiyaGi\n" \
          f"23. Не жалея - Miyagi Andy Panda\n" \
          f"24. Самурай   Miyagi"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi2)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="m24")
async def m24(call: CallbackQuery):
    music = open("Ruscha music/Miyagi/Самурай   Miyagi.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"21. Yamakasi   Miyagi,Andy Panda\n" \
          f"22. Заново жить    MiyaGi\n" \
          f"23. Не жалея - Miyagi Andy Panda\n" \
          f"24. Самурай   Miyagi"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Miyagi2)
    await call.answer(cache_time=30)



#miyagiorqa
@dp.callback_query_handler(text="mleft2")
async def mleft2(call: CallbackQuery):
    img = open("image/miyagi.png", "rb")
    txt = f"11. Miyagi & Эндшпиль - Ночь (Official Audio)\n" \
          f"12. Miyagi - Эндшпиль-Не теряя\n" \
          f"13. Miyagi feat Andy Panda - Там Ревели Горы \n" \
          f"14. Miyagi-jendshpil-rapapam-remix-edit_Kamola.net\n" \
          f"15. Miyagi-Malboro\n" \
          f"16. MiyaGi_&_Эндшпиль_Люби_меня_ft_Сим\n" \
          f"17. MiyaGi___I_Got_Iove\n" \
          f"18. Miyagi_feat._Kadi-Родная_пой\n" \
          f"19. Silhouette - Miyagi   Эндшпиль\n" \
          f"20. Where Are You - Ollane feat Miyagi Andy Panda"
    await call.message.answer_photo(img, txt, reply_markup=Miyagi1)
    await call.message.delete()




#Ruscha
@dp.callback_query_handler(text="rossia")
async def rossia(call: CallbackQuery):
    img = open("image/Violin Fiddle Cello Piano Music logo.jpg", "rb")
    txt = f"1. 4_5897682497675726077\n" \
          f"2. Jakone, AVG, MACAN - Samyjj molodojj\n" \
          f"3. Time - MOT.mp3\n" \
          f"4. Баста_Выпускной_Медлячок_.hd.mp3\n" \
          f"5. Сахро – Без меня.mp3\n" \
          f"6. Фир-Ночь.m4a"
    await call.message.answer_photo(img, txt, reply_markup=Rossia)
    await call.message.delete()


@dp.callback_query_handler(text="r1")
async def r1(call: CallbackQuery):
    music = open("Ruscha music/Mot/4_5897682497675726077.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. 4_5897682497675726077\n" \
          f"2. Jakone, AVG, MACAN - Samyjj molodojj\n" \
          f"3. Time - MOT.mp3\n" \
          f"4. Баста_Выпускной_Медлячок_.hd.mp3\n" \
          f"5. Сахро – Без меня.mp3\n" \
          f"6. Фир-Ночь.m4a"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Rossia)
    await call.answer(cache_time=30)



@dp.callback_query_handler(text="r2")
async def r2(call: CallbackQuery):
    music = open("Ruscha music/Mot/Jakone, AVG, MACAN - Samyjj molodojj.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. 4_5897682497675726077\n" \
          f"2. Jakone, AVG, MACAN - Samyjj molodojj\n" \
          f"3. Time - MOT.mp3\n" \
          f"4. Баста_Выпускной_Медлячок_.hd.mp3\n" \
          f"5. Сахро – Без меня.mp3\n" \
          f"6. Фир-Ночь.m4a"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Rossia)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="r3")
async def r3(call: CallbackQuery):
    music = open("Ruscha music/Mot/Time - MOT.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. 4_5897682497675726077\n" \
          f"2. Jakone, AVG, MACAN - Samyjj molodojj\n" \
          f"3. Time - MOT.mp3\n" \
          f"4. Баста_Выпускной_Медлячок_.hd.mp3\n" \
          f"5. Сахро – Без меня.mp3\n" \
          f"6. Фир-Ночь.m4a"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Rossia)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="r4")
async def r4(call: CallbackQuery):
    music = open("Ruscha music/Mot/Баста_Выпускной_Медлячок_.hd.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. 4_5897682497675726077\n" \
          f"2. Jakone, AVG, MACAN - Samyjj molodojj\n" \
          f"3. Time - MOT.mp3\n" \
          f"4. Баста_Выпускной_Медлячок_.hd.mp3\n" \
          f"5. Сахро – Без меня.mp3\n" \
          f"6. Фир-Ночь.m4a"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Rossia)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="r5")
async def r5(call: CallbackQuery):
    music = open("Ruscha music/Mot/Сахро – Без меня.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. 4_5897682497675726077\n" \
          f"2. Jakone, AVG, MACAN - Samyjj molodojj\n" \
          f"3. Time - MOT.mp3\n" \
          f"4. Баста_Выпускной_Медлячок_.hd.mp3\n" \
          f"5. Сахро – Без меня.mp3\n" \
          f"6. Фир-Ночь.m4a"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Rossia)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="r6")
async def r6(call: CallbackQuery):
    music = open("Ruscha music/Mot/Фир-Ночь.m4a", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. 4_5897682497675726077\n" \
          f"2. Jakone, AVG, MACAN - Samyjj molodojj\n" \
          f"3. Time - MOT.mp3\n" \
          f"4. Баста_Выпускной_Медлячок_.hd.mp3\n" \
          f"5. Сахро – Без меня.mp3\n" \
          f"6. Фир-Ночь.m4a"
    await call.message.answer(txt, reply_markup=Rossia)
    await call.answer(cache_time=30)
    await call.message.delete()


@dp.callback_query_handler(text="rrleft")
async def rleft(call: CallbackQuery):
    img = open("image/Violin Fiddle Cello Piano Music logo.jpg", "rb")
    txt = f"Bosh Sahifa"
    await call.message.answer_photo(img, txt, reply_markup=Russia)
    await call.message.delete()





#English
@dp.callback_query_handler(text="english")
async def english(call: CallbackQuery):
    img = open("image/Premium Vector _ Piano orchestra logo template.jpg", "rb")
    txt = f"1. Yeah Right\n" \
          f"2. My money don't jiggle jiggle\n" \
          f"3. 2PAC - Only Fear of Death (Izzamuzzic Remix)\n" \
          f"4. Bruno Mars - Greenade\n" \
          f"5. 17 Drip or Drown Remix (feat. Lil Ya.m4a\n" \
          f"6. Apologize   Timbaland feat. OneRepublic.mp3\n" \
          f"7. Drake - God's plan\n" \
          f"8. Dangerous   David Guetta ft Sam Martin.mp3\n" \
          f"9. Dr. Dre - Still D.R.E. (Feat. Snoop Dogg).mp3\n" \
          f"10. Ed Sheeran - Shape Of You (Lyrics).mp3"
    await call.message.answer_photo(img, txt, reply_markup=English)
    await call.message.delete()


@dp.callback_query_handler(text="e1")
async def e1(call: CallbackQuery):
    music = open("English music/2_5210771722143269660.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Yeah Right\n" \
          f"2. My money don't jiggle jiggle\n" \
          f"3. 2PAC - Only Fear of Death (Izzamuzzic Remix)\n" \
          f"4. Bruno Mars - Greenade\n" \
          f"5. 17 Drip or Drown Remix (feat. Lil Ya\n" \
          f"6. Apologize   Timbaland feat. OneRepublic\n" \
          f"7. Drake - God's plan\n" \
          f"8. Dangerous   David Guetta ft Sam Martin\n" \
          f"9. Dr. Dre - Still D.R.E. (Feat. Snoop Dogg)\n" \
          f"10. Ed Sheeran - Shape Of You (Lyrics)"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=English)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="e2")
async def e2(call: CallbackQuery):
    music = open("English music/2_5467726988259105741.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Yeah Right\n" \
          f"2. My money don't jiggle jiggle\n" \
          f"3. 2PAC - Only Fear of Death (Izzamuzzic Remix)\n" \
          f"4. Bruno Mars - Greenade\n" \
          f"5. 17 Drip or Drown Remix (feat. Lil Ya\n" \
          f"6. Apologize   Timbaland feat. OneRepublic\n" \
          f"7. Drake - God's plan\n" \
          f"8. Dangerous   David Guetta ft Sam Martin\n" \
          f"9. Dr. Dre - Still D.R.E. (Feat. Snoop Dogg)\n" \
          f"10. Ed Sheeran - Shape Of You (Lyrics)"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=English)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="e3")
async def e3(call: CallbackQuery):
    music = open("English music/2PAC - Only Fear of Death (Izzamuzzic Remix).mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Yeah Right\n" \
          f"2. My money don't jiggle jiggle\n" \
          f"3. 2PAC - Only Fear of Death (Izzamuzzic Remix)\n" \
          f"4. Bruno Mars - Greenade\n" \
          f"5. 17 Drip or Drown Remix (feat. Lil Ya\n" \
          f"6. Apologize   Timbaland feat. OneRepublic\n" \
          f"7. Drake - God's plan\n" \
          f"8. Dangerous   David Guetta ft Sam Martin\n" \
          f"9. Dr. Dre - Still D.R.E. (Feat. Snoop Dogg)\n" \
          f"10. Ed Sheeran - Shape Of You (Lyrics)"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=English)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="e4")
async def e4(call: CallbackQuery):
    music = open("English music/5_6177028308773896885.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Yeah Right\n" \
          f"2. My money don't jiggle jiggle\n" \
          f"3. 2PAC - Only Fear of Death (Izzamuzzic Remix)\n" \
          f"4. Bruno Mars - Greenade\n" \
          f"5. 17 Drip or Drown Remix (feat. Lil Ya\n" \
          f"6. Apologize   Timbaland feat. OneRepublic\n" \
          f"7. Drake - God's plan\n" \
          f"8. Dangerous   David Guetta ft Sam Martin\n" \
          f"9. Dr. Dre - Still D.R.E. (Feat. Snoop Dogg)\n" \
          f"10. Ed Sheeran - Shape Of You (Lyrics)"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=English)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="e5")
async def e5(call: CallbackQuery):
    music = open("English music/17 Drip or Drown Remix (feat. Lil Ya.m4a", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Yeah Right\n" \
          f"2. My money don't jiggle jiggle\n" \
          f"3. 2PAC - Only Fear of Death (Izzamuzzic Remix)\n" \
          f"4. Bruno Mars - Greenade\n" \
          f"5. 17 Drip or Drown Remix (feat. Lil Ya\n" \
          f"6. Apologize   Timbaland feat. OneRepublic\n" \
          f"7. Drake - God's plan\n" \
          f"8. Dangerous   David Guetta ft Sam Martin\n" \
          f"9. Dr. Dre - Still D.R.E. (Feat. Snoop Dogg)\n" \
          f"10. Ed Sheeran - Shape Of You (Lyrics)"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=English)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="e6")
async def e6(call: CallbackQuery):
    music = open("English music/Apologize   Timbaland feat. OneRepublic.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Yeah Right\n" \
          f"2. My money don't jiggle jiggle\n" \
          f"3. 2PAC - Only Fear of Death (Izzamuzzic Remix)\n" \
          f"4. Bruno Mars - Greenade\n" \
          f"5. 17 Drip or Drown Remix (feat. Lil Ya\n" \
          f"6. Apologize   Timbaland feat. OneRepublic\n" \
          f"7. Drake - God's plan\n" \
          f"8. Dangerous   David Guetta ft Sam Martin\n" \
          f"9. Dr. Dre - Still D.R.E. (Feat. Snoop Dogg)\n" \
          f"10. Ed Sheeran - Shape Of You (Lyrics)"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=English)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="e7")
async def e7(call: CallbackQuery):
    music = open("English music/AUD-20201109-WA0481.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Yeah Right\n" \
          f"2. My money don't jiggle jiggle\n" \
          f"3. 2PAC - Only Fear of Death (Izzamuzzic Remix)\n" \
          f"4. Bruno Mars - Greenade\n" \
          f"5. 17 Drip or Drown Remix (feat. Lil Ya\n" \
          f"6. Apologize   Timbaland feat. OneRepublic\n" \
          f"7. Drake - God's plan\n" \
          f"8. Dangerous   David Guetta ft Sam Martin\n" \
          f"9. Dr. Dre - Still D.R.E. (Feat. Snoop Dogg)\n" \
          f"10. Ed Sheeran - Shape Of You (Lyrics)"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=English)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="e8")
async def e8(call: CallbackQuery):
    music = open("English music/Dangerous   David Guetta ft Sam Martin.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Yeah Right\n" \
          f"2. My money don't jiggle jiggle\n" \
          f"3. 2PAC - Only Fear of Death (Izzamuzzic Remix)\n" \
          f"4. Bruno Mars - Greenade\n" \
          f"5. 17 Drip or Drown Remix (feat. Lil Ya\n" \
          f"6. Apologize   Timbaland feat. OneRepublic\n" \
          f"7. Drake - God's plan\n" \
          f"8. Dangerous   David Guetta ft Sam Martin\n" \
          f"9. Dr. Dre - Still D.R.E. (Feat. Snoop Dogg)\n" \
          f"10. Ed Sheeran - Shape Of You (Lyrics)"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=English)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="e9")
async def e9(call: CallbackQuery):
    music = open("English music/Dr. Dre - Still D.R.E. (Feat. Snoop Dogg).mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Yeah Right\n" \
          f"2. My money don't jiggle jiggle\n" \
          f"3. 2PAC - Only Fear of Death (Izzamuzzic Remix)\n" \
          f"4. Bruno Mars - Greenade\n" \
          f"5. 17 Drip or Drown Remix (feat. Lil Ya\n" \
          f"6. Apologize   Timbaland feat. OneRepublic\n" \
          f"7. Drake - God's plan\n" \
          f"8. Dangerous   David Guetta ft Sam Martin\n" \
          f"9. Dr. Dre - Still D.R.E. (Feat. Snoop Dogg)\n" \
          f"10. Ed Sheeran - Shape Of You (Lyrics)"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=English)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="e10")
async def e10(call: CallbackQuery):
    music = open("English music/Ed Sheeran - Shape Of You (Lyrics).mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Yeah Right\n" \
          f"2. My money don't jiggle jiggle\n" \
          f"3. 2PAC - Only Fear of Death (Izzamuzzic Remix)\n" \
          f"4. Bruno Mars - Greenade\n" \
          f"5. 17 Drip or Drown Remix (feat. Lil Ya\n" \
          f"6. Apologize   Timbaland feat. OneRepublic\n" \
          f"7. Drake - God's plan\n" \
          f"8. Dangerous   David Guetta ft Sam Martin\n" \
          f"9. Dr. Dre - Still D.R.E. (Feat. Snoop Dogg)\n" \
          f"10. Ed Sheeran - Shape Of You (Lyrics)"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=English)
    await call.answer(cache_time=30)



@dp.callback_query_handler(text="eleft")
async def eleft(call: CallbackQuery):
    img = open("image/Без названия.jpg", "rb")
    txt = f"Bosh Sahifa"
    await call.message.answer_photo(img, txt, reply_markup=Start)
    await call.message.delete()



#English1
@dp.callback_query_handler(text="eright")
async def eright(call: CallbackQuery):
    img = open("image/Premium Vector _ Piano orchestra logo template.jpg", "rb")
    txt = f"11. Eminem-Never-Love-Again-320\n" \
          f"12. G-Eazy & Halsey - Him & I (Official Music Video)\n" \
          f"13. Gangsta s Paradise (feat. L.V.)   Coolio feat. L.V\n" \
          f"14. Kina_feat._Adriana_Proenza-Can_we_kiss_forever\n" \
          f"15. LIT - Parker Morris\n" \
          f"16. Sam Smith - Fire On Fire (From Watership Down)\n" \
          f"17. Selena Gomez - Dance Again\n" \
          f"18. Somebody s Me   Enrique Lglesias\n" \
          f"19. Stronger Than I Was - Eminem\n" \
          f"20. Thunder   Imagine Dragon.mp3\n" \
          f"21. Zivert - Life   Премьера клипа.mp3"
    await call.message.answer_photo(img, txt, reply_markup=English1)
    await call.message.delete()


@dp.callback_query_handler(text="e11")
async def e11(call: CallbackQuery):
    music = open("English music/Eminem-Never-Love-Again-320.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Eminem-Never-Love-Again-320\n" \
          f"12. G-Eazy & Halsey - Him & I (Official Music Video)\n" \
          f"13. Gangsta s Paradise (feat. L.V.)   Coolio feat. L.V\n" \
          f"14. Kina_feat._Adriana_Proenza-Can_we_kiss_forever\n" \
          f"15. LIT - Parker Morris\n" \
          f"16. Sam Smith - Fire On Fire (From Watership Down)\n" \
          f"17. Selena Gomez - Dance Again\n" \
          f"18. Somebody s Me   Enrique Lglesias\n" \
          f"19. Stronger Than I Was - Eminem\n" \
          f"20. Thunder   Imagine Dragon.mp3\n" \
          f"21. Zivert - Life   Премьера клипа.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=English1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="e12")
async def e12(call: CallbackQuery):
    music = open("English music/G-Eazy & Halsey - Him & I (Official Music Video).mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Eminem-Never-Love-Again-320\n" \
          f"12. G-Eazy & Halsey - Him & I (Official Music Video)\n" \
          f"13. Gangsta s Paradise (feat. L.V.)   Coolio feat. L.V\n" \
          f"14. Kina_feat._Adriana_Proenza-Can_we_kiss_forever\n" \
          f"15. LIT - Parker Morris\n" \
          f"16. Sam Smith - Fire On Fire (From Watership Down)\n" \
          f"17. Selena Gomez - Dance Again\n" \
          f"18. Somebody s Me   Enrique Lglesias\n" \
          f"19. Stronger Than I Was - Eminem\n" \
          f"20. Thunder   Imagine Dragon.mp3\n" \
          f"21. Zivert - Life   Премьера клипа.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=English1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="e13")
async def e13(call: CallbackQuery):
    music = open("English music/Gangsta s Paradise (feat. L.V.)   Coolio feat. L.V.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Eminem-Never-Love-Again-320\n" \
          f"12. G-Eazy & Halsey - Him & I (Official Music Video)\n" \
          f"13. Gangsta s Paradise (feat. L.V.)   Coolio feat. L.V\n" \
          f"14. Kina_feat._Adriana_Proenza-Can_we_kiss_forever\n" \
          f"15. LIT - Parker Morris\n" \
          f"16. Sam Smith - Fire On Fire (From Watership Down)\n" \
          f"17. Selena Gomez - Dance Again\n" \
          f"18. Somebody s Me   Enrique Lglesias\n" \
          f"19. Stronger Than I Was - Eminem\n" \
          f"20. Thunder   Imagine Dragon.mp3\n" \
          f"21. Zivert - Life   Премьера клипа.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=English1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="e14")
async def e14(call: CallbackQuery):
    music = open("English music/Kina_feat._Adriana_Proenza-Can_we_kiss_forever.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Eminem-Never-Love-Again-320\n" \
          f"12. G-Eazy & Halsey - Him & I (Official Music Video)\n" \
          f"13. Gangsta s Paradise (feat. L.V.)   Coolio feat. L.V\n" \
          f"14. Kina_feat._Adriana_Proenza-Can_we_kiss_forever\n" \
          f"15. LIT - Parker Morris\n" \
          f"16. Sam Smith - Fire On Fire (From Watership Down)\n" \
          f"17. Selena Gomez - Dance Again\n" \
          f"18. Somebody s Me   Enrique Lglesias\n" \
          f"19. Stronger Than I Was - Eminem\n" \
          f"20. Thunder   Imagine Dragon.mp3\n" \
          f"21. Zivert - Life   Премьера клипа.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=English1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="e15")
async def e15(call: CallbackQuery):
    music = open("English music/LIT - Parker Morris.m4a", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Eminem-Never-Love-Again-320\n" \
          f"12. G-Eazy & Halsey - Him & I (Official Music Video)\n" \
          f"13. Gangsta s Paradise (feat. L.V.)   Coolio feat. L.V\n" \
          f"14. Kina_feat._Adriana_Proenza-Can_we_kiss_forever\n" \
          f"15. LIT - Parker Morris\n" \
          f"16. Sam Smith - Fire On Fire (From Watership Down)\n" \
          f"17. Selena Gomez - Dance Again\n" \
          f"18. Somebody s Me   Enrique Lglesias\n" \
          f"19. Stronger Than I Was - Eminem\n" \
          f"20. Thunder   Imagine Dragon.mp3\n" \
          f"21. Zivert - Life   Премьера клипа.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=English1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="e16")
async def e16(call: CallbackQuery):
    music = open("English music/Sam Smith - Fire On Fire (From Watership Down).mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Eminem-Never-Love-Again-320\n" \
          f"12. G-Eazy & Halsey - Him & I (Official Music Video)\n" \
          f"13. Gangsta s Paradise (feat. L.V.)   Coolio feat. L.V\n" \
          f"14. Kina_feat._Adriana_Proenza-Can_we_kiss_forever\n" \
          f"15. LIT - Parker Morris\n" \
          f"16. Sam Smith - Fire On Fire (From Watership Down)\n" \
          f"17. Selena Gomez - Dance Again\n" \
          f"18. Somebody s Me   Enrique Lglesias\n" \
          f"19. Stronger Than I Was - Eminem\n" \
          f"20. Thunder   Imagine Dragon.mp3\n" \
          f"21. Zivert - Life   Премьера клипа.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=English1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="e17")
async def e17(call: CallbackQuery):
    music = open("English music/Selena Gomez - Dance Again.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Eminem-Never-Love-Again-320\n" \
          f"12. G-Eazy & Halsey - Him & I (Official Music Video)\n" \
          f"13. Gangsta s Paradise (feat. L.V.)   Coolio feat. L.V\n" \
          f"14. Kina_feat._Adriana_Proenza-Can_we_kiss_forever\n" \
          f"15. LIT - Parker Morris\n" \
          f"16. Sam Smith - Fire On Fire (From Watership Down)\n" \
          f"17. Selena Gomez - Dance Again\n" \
          f"18. Somebody s Me   Enrique Lglesias\n" \
          f"19. Stronger Than I Was - Eminem\n" \
          f"20. Thunder   Imagine Dragon.mp3\n" \
          f"21. Zivert - Life   Премьера клипа.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=English1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="e18")
async def e18(call: CallbackQuery):
    music = open("English music/Somebody s Me   Enrique Lglesias.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Eminem-Never-Love-Again-320\n" \
          f"12. G-Eazy & Halsey - Him & I (Official Music Video)\n" \
          f"13. Gangsta s Paradise (feat. L.V.)   Coolio feat. L.V\n" \
          f"14. Kina_feat._Adriana_Proenza-Can_we_kiss_forever\n" \
          f"15. LIT - Parker Morris\n" \
          f"16. Sam Smith - Fire On Fire (From Watership Down)\n" \
          f"17. Selena Gomez - Dance Again\n" \
          f"18. Somebody s Me   Enrique Lglesias\n" \
          f"19. Stronger Than I Was - Eminem\n" \
          f"20. Thunder   Imagine Dragon.mp3\n" \
          f"21. Zivert - Life   Премьера клипа.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=English1)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="e19")
async def e19(call: CallbackQuery):
    music = open("English music/Stronger Than I Was - Eminem.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Eminem-Never-Love-Again-320\n" \
          f"12. G-Eazy & Halsey - Him & I (Official Music Video)\n" \
          f"13. Gangsta s Paradise (feat. L.V.)   Coolio feat. L.V\n" \
          f"14. Kina_feat._Adriana_Proenza-Can_we_kiss_forever\n" \
          f"15. LIT - Parker Morris\n" \
          f"16. Sam Smith - Fire On Fire (From Watership Down)\n" \
          f"17. Selena Gomez - Dance Again\n" \
          f"18. Somebody s Me   Enrique Lglesias\n" \
          f"19. Stronger Than I Was - Eminem\n" \
          f"20. Thunder   Imagine Dragon.mp3\n" \
          f"21. Zivert - Life   Премьера клипа.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=English1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="e20")
async def e20(call: CallbackQuery):
    music = open("English music/Thunder   Imagine Dragon.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Eminem-Never-Love-Again-320\n" \
          f"12. G-Eazy & Halsey - Him & I (Official Music Video)\n" \
          f"13. Gangsta s Paradise (feat. L.V.)   Coolio feat. L.V\n" \
          f"14. Kina_feat._Adriana_Proenza-Can_we_kiss_forever\n" \
          f"15. LIT - Parker Morris\n" \
          f"16. Sam Smith - Fire On Fire (From Watership Down)\n" \
          f"17. Selena Gomez - Dance Again\n" \
          f"18. Somebody s Me   Enrique Lglesias\n" \
          f"19. Stronger Than I Was - Eminem\n" \
          f"20. Thunder   Imagine Dragon.mp3\n" \
          f"21. Zivert - Life   Премьера клипа.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=English1)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="e21")
async def e21(call: CallbackQuery):
    music = open("English music/Zivert - Life   Премьера клипа.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Eminem-Never-Love-Again-320\n" \
          f"12. G-Eazy & Halsey - Him & I (Official Music Video)\n" \
          f"13. Gangsta s Paradise (feat. L.V.)   Coolio feat. L.V\n" \
          f"14. Kina_feat._Adriana_Proenza-Can_we_kiss_forever\n" \
          f"15. LIT - Parker Morris\n" \
          f"16. Sam Smith - Fire On Fire (From Watership Down)\n" \
          f"17. Selena Gomez - Dance Again\n" \
          f"18. Somebody s Me   Enrique Lglesias\n" \
          f"19. Stronger Than I Was - Eminem\n" \
          f"20. Thunder   Imagine Dragon.mp3\n" \
          f"21. Zivert - Life   Премьера клипа.mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=English1)
    await call.answer(cache_time=30)

#english1orqaga
@dp.callback_query_handler(text="eleft1")
async def eleft1(call: CallbackQuery):
    img = open("image/Premium Vector _ Piano orchestra logo template.jpg", "rb")
    txt = f"1. Yeah Right\n" \
          f"2. My money don't jiggle jiggle\n" \
          f"3. 2PAC - Only Fear of Death (Izzamuzzic Remix)\n" \
          f"4. Bruno Mars - Greenade\n" \
          f"5. 17 Drip or Drown Remix (feat. Lil Ya\n" \
          f"6. Apologize   Timbaland feat. OneRepublic\n" \
          f"7. Drake - God's plan\n" \
          f"8. Dangerous   David Guetta ft Sam Martin\n" \
          f"9. Dr. Dre - Still D.R.E. (Feat. Snoop Dogg)\n" \
          f"10. Ed Sheeran - Shape Of You (Lyrics)"
    await call.message.answer_photo(img, txt, reply_markup=English)
    await call.message.delete()


#Uzbekmusic
@dp.callback_query_handler(text="uzbek")
async def uzbek(call: CallbackQuery):
    img = open("image/Logo _ relax.jpg", "rb")
    txt = f"1. Shoxrux – Bolaligim\n" \
          f"2. Alisher Uzoqov - Nahotki\n" \
          f"3. Bojalar - Nilufar\n" \
          f"4. Bojalar - Shalola\n" \
          f"5. JAVA - Dunyo seni Tog'angmas\n" \
          f"6. Bolalar - Kel Yashaylik\n" \
          f"7. Bolalar - Mening Dostim\n" \
          f"8. Shoxrux - Ikki Qalb \n" \
          f"9. Shoxrux Repper – Bir Bora \n" \
          f"10 Shoxrux – Yoroney"
    await call.message.delete()
    await call.message.answer_photo(img, txt, reply_markup=Uzbek)



@dp.callback_query_handler(text="u1")
async def u1(call: CallbackQuery):
    music = open("Uzbekcha music/002 Shoxrux – Bolaligim.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Shoxrux – Bolaligim\n" \
          f"2. Alisher Uzoqov - Nahotki\n" \
          f"3. Bojalar - Nilufar\n" \
          f"4. Bojalar - Shalola\n" \
          f"5. JAVA - Dunyo seni Tog'angmas\n" \
          f"6. Bolalar - Kel Yashaylik\n" \
          f"7. Bolalar - Mening Dostim\n" \
          f"8. Shoxrux - Ikki Qalb \n" \
          f"9. Shoxrux Repper – Bir Bora \n" \
          f"10 Shoxrux – Yoroney"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Uzbek)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="u2")
async def u2(call: CallbackQuery):
    music = open("Uzbekcha music/7026612859663599616.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Shoxrux – Bolaligim\n" \
          f"2. Alisher Uzoqov - Nahotki\n" \
          f"3. Bojalar - Nilufar\n" \
          f"4. Bojalar - Shalola\n" \
          f"5. JAVA - Dunyo seni Tog'angmas\n" \
          f"6. Bolalar - Kel Yashaylik\n" \
          f"7. Bolalar - Mening Dostim\n" \
          f"8. Shoxrux - Ikki Qalb \n" \
          f"9. Shoxrux Repper – Bir Bora \n" \
          f"10 Shoxrux – Yoroney"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Uzbek)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="u3")
async def u3(call: CallbackQuery):
    music = open("Uzbekcha music/bestmusicuz   Bojalar.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Shoxrux – Bolaligim\n" \
          f"2. Alisher Uzoqov - Nahotki\n" \
          f"3. Bojalar - Nilufar\n" \
          f"4. Bojalar - Shalola\n" \
          f"5. JAVA - Dunyo seni Tog'angmas\n" \
          f"6. Bolalar - Kel Yashaylik\n" \
          f"7. Bolalar - Mening Dostim\n" \
          f"8. Shoxrux - Ikki Qalb \n" \
          f"9. Shoxrux Repper – Bir Bora \n" \
          f"10 Shoxrux – Yoroney"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Uzbek)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="u4")
async def u4(call: CallbackQuery):
    music = open("Uzbekcha music/Bojalar_-_Shalola.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Shoxrux – Bolaligim\n" \
          f"2. Alisher Uzoqov - Nahotki\n" \
          f"3. Bojalar - Nilufar\n" \
          f"4. Bojalar - Shalola\n" \
          f"5. JAVA - Dunyo seni Tog'angmas\n" \
          f"6. Bolalar - Kel Yashaylik\n" \
          f"7. Bolalar - Mening Dostim\n" \
          f"8. Shoxrux - Ikki Qalb \n" \
          f"9. Shoxrux Repper – Bir Bora \n" \
          f"10 Shoxrux – Yoroney"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Uzbek)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="u5")
async def u5(call: CallbackQuery):
    music = open("Uzbekcha music/JAVA - Dunyo seni Tog'angmas.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Shoxrux – Bolaligim\n" \
          f"2. Alisher Uzoqov - Nahotki\n" \
          f"3. Bojalar - Nilufar\n" \
          f"4. Bojalar - Shalola\n" \
          f"5. JAVA - Dunyo seni Tog'angmas\n" \
          f"6. Bolalar - Kel Yashaylik\n" \
          f"7. Bolalar - Mening Dostim\n" \
          f"8. Shoxrux - Ikki Qalb \n" \
          f"9. Shoxrux Repper – Bir Bora \n" \
          f"10 Shoxrux – Yoroney"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Uzbek)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="u6")
async def u6(call: CallbackQuery):
    music = open("Uzbekcha music/Kel yashaylik birga (uzhitsnet) - Bolalar guruhi-1.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Shoxrux – Bolaligim\n" \
          f"2. Alisher Uzoqov - Nahotki\n" \
          f"3. Bojalar - Nilufar\n" \
          f"4. Bojalar - Shalola\n" \
          f"5. JAVA - Dunyo seni Tog'angmas\n" \
          f"6. Bolalar - Kel Yashaylik\n" \
          f"7. Bolalar - Mening Dostim\n" \
          f"8. Shoxrux - Ikki Qalb \n" \
          f"9. Shoxrux Repper – Bir Bora \n" \
          f"10 Shoxrux – Yoroney"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Uzbek)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="u7")
async def u7(call: CallbackQuery):
    music = open("Uzbekcha music/Mening Dostim Taronanet - Bolalar-1.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Shoxrux – Bolaligim\n" \
          f"2. Alisher Uzoqov - Nahotki\n" \
          f"3. Bojalar - Nilufar\n" \
          f"4. Bojalar - Shalola\n" \
          f"5. JAVA - Dunyo seni Tog'angmas\n" \
          f"6. Bolalar - Kel Yashaylik\n" \
          f"7. Bolalar - Mening Dostim\n" \
          f"8. Shoxrux - Ikki Qalb \n" \
          f"9. Shoxrux Repper – Bir Bora \n" \
          f"10 Shoxrux – Yoroney"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Uzbek)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="u8")
async def u8(call: CallbackQuery):
    music = open("Uzbekcha music/Shoxrux - Ikki Qalb (mp3uz.net).mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Shoxrux – Bolaligim\n" \
          f"2. Alisher Uzoqov - Nahotki\n" \
          f"3. Bojalar - Nilufar\n" \
          f"4. Bojalar - Shalola\n" \
          f"5. JAVA - Dunyo seni Tog'angmas\n" \
          f"6. Bolalar - Kel Yashaylik\n" \
          f"7. Bolalar - Mening Dostim\n" \
          f"8. Shoxrux - Ikki Qalb \n" \
          f"9. Shoxrux Repper – Bir Bora \n" \
          f"10 Shoxrux – Yoroney"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Uzbek)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="u9")
async def u9(call: CallbackQuery):
    music = open("Uzbekcha music/Shoxrux Repper – Bir Bora (DVStudio Presents).mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Shoxrux – Bolaligim\n" \
          f"2. Alisher Uzoqov - Nahotki\n" \
          f"3. Bojalar - Nilufar\n" \
          f"4. Bojalar - Shalola\n" \
          f"5. JAVA - Dunyo seni Tog'angmas\n" \
          f"6. Bolalar - Kel Yashaylik\n" \
          f"7. Bolalar - Mening Dostim\n" \
          f"8. Shoxrux - Ikki Qalb \n" \
          f"9. Shoxrux Repper – Bir Bora \n" \
          f"10 Shoxrux – Yoroney"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Uzbek)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="u10")
async def u10(call: CallbackQuery):
    music = open("Uzbekcha music/Shoxrux – Yoroney.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"1. Shoxrux – Bolaligim\n" \
          f"2. Alisher Uzoqov - Nahotki\n" \
          f"3. Bojalar - Nilufar\n" \
          f"4. Bojalar - Shalola\n" \
          f"5. JAVA - Dunyo seni Tog'angmas\n" \
          f"6. Bolalar - Kel Yashaylik\n" \
          f"7. Bolalar - Mening Dostim\n" \
          f"8. Shoxrux - Ikki Qalb \n" \
          f"9. Shoxrux Repper – Bir Bora \n" \
          f"10 Shoxrux – Yoroney"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Uzbek)
    await call.answer(cache_time=30)


#startorqagauz
@dp.callback_query_handler(text="uleft")
async def uleft(call: CallbackQuery):
    img = open("image/Без названия.jpg", "rb")
    txt = f"Bosh Sahifa"
    await call.message.delete()
    await call.message.answer_photo(img, txt, reply_markup=Start)

#uzbek1
@dp.callback_query_handler(text="uright")
async def uright(call: CallbackQuery):
    img = open("image/Classic Geometric Square Rr Logo Letter Stock Vector (Royalty Free) 1272442909 _ Shutterstock.jpg", "rb")
    txt = f"11. Yorqinxoja_Umarov-Yomgir\n" \
          f"12. Nilufar_bintu_Ulug'bek_Kullul_qulub_Cover_Musicn\n" \
          f"13. Ulug'bek Rahmatullayev - Qirmizi olma \n" \
          f"14. Ulugbek_Rahmatullayev-Yolgonchim \n" \
          f"15. Ulug'bek Rahmatullayev - Seni deya (Music 2021).mp3"
    await call.message.delete()
    await call.message.answer_photo(img, txt, reply_markup=Uzbek1)

@dp.callback_query_handler(text="u11")
async def u11(call: CallbackQuery):
    music = open("Uzbekcha music/Yorqinxoja_Umarov-Yomgir.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Yorqinxoja_Umarov-Yomgir\n" \
          f"12. Nilufar_bintu_Ulug'bek_Kullul_qulub_Cover_Musicn\n" \
          f"13. Ulug'bek Rahmatullayev - Qirmizi olma \n" \
          f"14. Ulugbek_Rahmatullayev-Yolgonchim \n" \
          f"15. Ulug'bek Rahmatullayev - Seni deya (Music 2021).mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Uzbek1)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="u12")
async def u12(call: CallbackQuery):
    music = open("Uzbekcha music/Ulugbek/Nilufar_bintu_Ulug'bek_Kullul_qulub_Cover_Music_2022.mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Yorqinxoja_Umarov-Yomgir\n" \
          f"12. Nilufar_bintu_Ulug'bek_Kullul_qulub_Cover_Musicn\n" \
          f"13. Ulug'bek Rahmatullayev - Qirmizi olma \n" \
          f"14. Ulugbek_Rahmatullayev-Yolgonchim \n" \
          f"15. Ulug'bek Rahmatullayev - Seni deya (Music 2021).mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Uzbek1)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="u13")
async def u13(call: CallbackQuery):
    music = open("Uzbekcha music/Ulugbek/Ulug'bek Rahmatullayev - Qirmizi olma (Music 2021).mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Yorqinxoja_Umarov-Yomgir\n" \
          f"12. Nilufar_bintu_Ulug'bek_Kullul_qulub_Cover_Musicn\n" \
          f"13. Ulug'bek Rahmatullayev - Qirmizi olma \n" \
          f"14. Ulugbek_Rahmatullayev-Yolgonchim \n" \
          f"15. Ulug'bek Rahmatullayev - Seni deya (Music 2021).mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Uzbek1)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="u14")
async def u14(call: CallbackQuery):
    music = open("Uzbekcha music/Ulugbek/Ulugbek_Rahmatullayev-Yolgonchim(1).mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Yorqinxoja_Umarov-Yomgir\n" \
          f"12. Nilufar_bintu_Ulug'bek_Kullul_qulub_Cover_Musicn\n" \
          f"13. Ulug'bek Rahmatullayev - Qirmizi olma \n" \
          f"14. Ulugbek_Rahmatullayev-Yolgonchim \n" \
          f"15. Ulug'bek Rahmatullayev - Seni deya (Music 2021).mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Uzbek1)
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="u15")
async def u15(call: CallbackQuery):
    music = open("Uzbekcha music/Ulugbek/Ulug'bek Rahmatullayev - Seni deya (Music 2021).mp3", "rb")
    await call.message.answer_audio(music, reply_markup=Iks)
    txt = f"11. Yorqinxoja_Umarov-Yomgir\n" \
          f"12. Nilufar_bintu_Ulug'bek_Kullul_qulub_Cover_Musicn\n" \
          f"13. Ulug'bek Rahmatullayev - Qirmizi olma \n" \
          f"14. Ulugbek_Rahmatullayev-Yolgonchim \n" \
          f"15. Ulug'bek Rahmatullayev - Seni deya (Music 2021).mp3"
    await call.message.delete()
    await call.message.answer(txt, reply_markup=Uzbek1)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="uleft1")
async def uleft1(call: CallbackQuery):
    img = open("image/Logo _ relax.jpg", "rb")
    txt = f"1. Shoxrux – Bolaligim\n" \
          f"2. Alisher Uzoqov - Nahotki\n" \
          f"3. Bojalar - Nilufar\n" \
          f"4. Bojalar - Shalola\n" \
          f"5. JAVA - Dunyo seni Tog'angmas\n" \
          f"6. Bolalar - Kel Yashaylik\n" \
          f"7. Bolalar - Mening Dostim\n" \
          f"8. Shoxrux - Ikki Qalb \n" \
          f"9. Shoxrux Repper – Bir Bora \n" \
          f"10 Shoxrux – Yoroney"
    await call.message.delete()
    await call.message.answer_photo(img, txt, reply_markup=Uzbek)


if __name__ == '__main__':
    executor.start_polling(dp)

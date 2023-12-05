import telebot
from telebot import types
from PIL import Image


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()


def resize_image(image_path):
    with Image.open(image_path) as image:
        photo = image.resize((600, 600))
        return photo


botBitl = telebot.TeleBot(read_file('token.ini'))


@botBitl.message_handler(commands=['start'])
def startBot(message):
    first_mess = f"<b>Выберите раздел дискографии</b>"
    markup = types.InlineKeyboardMarkup()
    uk_albums = types.InlineKeyboardButton(text='Британские альбомы', callback_data='uk_albums')
    markup.add(uk_albums)
    us_albums = types.InlineKeyboardButton(text='Американские альбомы', callback_data='us_albums')
    markup.add(us_albums)
    compil_63_90 = types.InlineKeyboardButton(text='Сборники 1971-1990', callback_data='compil_63_90')
    markup.add(compil_63_90)
    # compil_91_23 = types.InlineKeyboardButton(text='Сборники 1991-2023', callback_data='compil_91_23')
    # markup.add(compil_91_23)
    # uk_singles = types.InlineKeyboardButton(text='Британские синглы 1962-1970', callback_data='uk_singles')
    # markup.add(uk_singles)
    # us_singles = types.InlineKeyboardButton(text='Американские синглы 1962-1970', callback_data='us_singles')
    # markup.add(us_singles)
    # singles_71up = types.InlineKeyboardButton(text="Синглы 1971-2023", callback_data='singles_71up')
    # markup.add(singles_71up)
    # eps = types.InlineKeyboardButton(text='Мини-альбомы (EP)', callback_data='eps')
    # markup.add(eps)

    botBitl.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)


@botBitl.callback_query_handler(func=lambda call: True)
def response_choice(function_call):
    if function_call.message:
        if function_call.data == 'uk_albums':
            doo = types.InlineKeyboardMarkup()
            please_me = types.InlineKeyboardButton(text='Please Please Me', callback_data='please_me')
            doo.add(please_me)
            with_the_beatles = types.InlineKeyboardButton(text='With The Beatles', callback_data='with_the_beatles')
            doo.add(with_the_beatles)
            a_hard_days_night = types.InlineKeyboardButton(text="A Hard Day's Night", callback_data='a_hard_days_night')
            doo.add(a_hard_days_night)
            beatles_for_sale = types.InlineKeyboardButton(text='Beatles For Sale', callback_data='beatles_for_sale')
            doo.add(beatles_for_sale)
            help_ = types.InlineKeyboardButton(text='Help!', callback_data='help_')
            doo.add(help_)
            rubber_soul = types.InlineKeyboardButton(text='Rubber Soul', callback_data='rubber_soul')
            doo.add(rubber_soul)
            revolver = types.InlineKeyboardButton(text='Revolver', callback_data='revolver')
            doo.add(revolver)
            sgt_pepper = types.InlineKeyboardButton(text="Sgt. Pepper's Lonely Hearts Club Band",
                                                    callback_data='sgt_pepper')
            doo.add(sgt_pepper)
            the_beatles = types.InlineKeyboardButton(text='The Beatles (The White Album)', callback_data='the_beatles')
            doo.add(the_beatles)
            yellow_submarine = types.InlineKeyboardButton(text='Yellow Submarine', callback_data='yellow_submarine')
            doo.add(yellow_submarine)
            abbey_road = types.InlineKeyboardButton(text='Abbey Road', callback_data='abbey_road')
            doo.add(abbey_road)
            let_it_be = types.InlineKeyboardButton(text='Let It Be', callback_data='let_it_be')
            doo.add(let_it_be)

            botBitl.send_message(function_call.message.chat.id, 'выбери альбом', parse_mode='html', reply_markup=doo)
            botBitl.answer_callback_query(function_call.id)

        elif function_call.data == 'us_albums':
            doo = types.InlineKeyboardMarkup()
            introducing_the_beatles = types.InlineKeyboardButton(text='Introducing... the Beatles',
                                                                 callback_data='introducing_the_beatles')
            doo.add(introducing_the_beatles)
            meet_the_beatles = types.InlineKeyboardButton(text='Meet The Beatles!', callback_data='meet_the_beatles')
            doo.add(meet_the_beatles)
            the_beatles_second_album = types.InlineKeyboardButton(text="The Beatles' Second Album",
                                                                  callback_data='the_beatles_second_album')
            doo.add(the_beatles_second_album)
            a_hard_days_night_us = types.InlineKeyboardButton(text="A Hard Day's Night (US edition)",
                                                              callback_data='a_hard_days_night_us')
            doo.add(a_hard_days_night_us)
            something_new = types.InlineKeyboardButton(text='Something New', callback_data='something_new')
            doo.add(something_new)
            beatles_65 = types.InlineKeyboardButton(text="Beatles' 65", callback_data='beatles_65')
            doo.add(beatles_65)
            the_early_beatles = types.InlineKeyboardButton(text='The Early Beatles', callback_data='the_early_beatles')
            doo.add(the_early_beatles)
            beatles_vi = types.InlineKeyboardButton(text="Beatles VI",
                                                    callback_data='beatles_vi')
            doo.add(beatles_vi)
            help_us = types.InlineKeyboardButton(text='Help! (US edition)', callback_data='help_us')
            doo.add(help_us)
            rubber_soul_us = types.InlineKeyboardButton(text='Rubber Soul (US edition)', callback_data='rubber_soul_us')
            doo.add(rubber_soul_us)
            yesterday_and_today = types.InlineKeyboardButton(text='Yesterday And Today',
                                                             callback_data='yesterday_and_today')
            doo.add(yesterday_and_today)
            revolver_us = types.InlineKeyboardButton(text='Revolver (US edition)', callback_data='revolver_us')
            doo.add(revolver_us)
            magical_mystery_tour_lp = types.InlineKeyboardButton(text='Magical Mystery Tour (LP)',
                                                                 callback_data='magical_mystery_tour_lp')
            doo.add(magical_mystery_tour_lp)

            botBitl.send_message(function_call.message.chat.id, 'выбери альбом', parse_mode='html', reply_markup=doo)
            botBitl.answer_callback_query(function_call.id)

        elif function_call.data == 'compil_63_90':
            doo = types.InlineKeyboardMarkup()
            oldies_but_goldies = types.InlineKeyboardButton(text='A Collection of Beatles Oldies (But Goldies!)',
                                                                 callback_data='oldies_but_goldies')
            doo.add(oldies_but_goldies)
            hey_jude = types.InlineKeyboardButton(text='Hey Jude/The Beatles Again', callback_data='hey_jude')
            doo.add(hey_jude)
            in_the_beginning = types.InlineKeyboardButton(text='In the Beginning (Circa 1960)',
                                                          callback_data='in_the_beginning')
            doo.add(in_the_beginning)
            red_album = types.InlineKeyboardButton(text="The Beatles 1962-1966 (The Red Album)",
                                                   callback_data='red_album')
            doo.add(red_album)
            blue_album = types.InlineKeyboardButton(text='The Beatles 1967-1970 (The Blue Album)',
                                                    callback_data='blue_album')
            doo.add(blue_album)
            rock_n_roll_music = types.InlineKeyboardButton(text="Rock 'n' Roll Music",
                                                           callback_data='rock_n_roll_music')
            doo.add(rock_n_roll_music)
            love_songs = types.InlineKeyboardButton(text='Love Songs', callback_data='love_songs')
            doo.add(love_songs)
            rarities_uk = types.InlineKeyboardButton(text="Rarities (UK edition)", callback_data='rarities_uk')
            doo.add(rarities_uk)
            rarities_us = types.InlineKeyboardButton(text='Rarities (US edition)', callback_data='rarities_us')
            doo.add(rarities_us)
            ballads = types.InlineKeyboardButton(text='The Beatles Ballads', callback_data='ballads')
            doo.add(ballads)
            reel_music = types.InlineKeyboardButton(text='Reel Music', callback_data='reel_music')
            doo.add(reel_music)
            greatest_hits_uk = types.InlineKeyboardButton(text='20 Greatest Hits (UK edit)',
                                                          callback_data='greatest_hits_uk')
            doo.add(greatest_hits_uk)
            greatest_hits_us = types.InlineKeyboardButton(text='20 Greatest Hits (US edit)',
                                                          callback_data='greatest_hits_us')
            doo.add(greatest_hits_us)
            past_masters_1 = types.InlineKeyboardButton(text="Past Masters. Volume One", callback_data='past_masters_1')
            doo.add(past_masters_1)
            past_masters_2 = types.InlineKeyboardButton(text="Past Masters. Volume Two", callback_data='past_masters_2')
            doo.add(past_masters_2)

            botBitl.send_message(function_call.message.chat.id, 'выбери альбом', parse_mode='html', reply_markup=doo)
            botBitl.answer_callback_query(function_call.id)

        elif function_call.message:
            if function_call.data == "introducing_the_beatles":
                photo = open('images/beatles/us_albums/introducing_the_beatles.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. I Saw Her Standing There\n2. Misery\n3. Anna (Go To Him)\n4. Chains\n5. Boys\n'
                                     '6. Love Me Do\n7. P.S. I Love You\n8. Baby It\'s You\n9. Do You Want To Know A '
                                     'Secret\n10. A Taste Of Honey\n11. There\'s A Place\n12. Twist And Shout',
                                     parse_mode='html')
            elif function_call.data == "meet_the_beatles":
                photo = open('images/beatles/us_albums/meet_the_beatles.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. I Want To Hold Your Hand\n2. I Saw Her Standing There\n3. This Boy\n4. It '
                                     'Won\'t Be Long\n5. All I\'ve Got To Do\n6. All My Loving\n7. Don\'t Bother Me\n'
                                     '8. Little Child\n9. Till There Was You\n10. Hold Me Tight\n11. I Wanna Be Your '
                                     'Man\n12. Not A Second Time',
                                     parse_mode='html')
            elif function_call.data == "the_beatles_second_album":
                photo = open('images/beatles/us_albums/the_beatles_second_album.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Roll Over Beethoven\n2. Thank You Girl\n3. You Really Got A Hold On Me\n4. '
                                     'Devil In Her Heart\n5. Money (That\'s What I Want)\n6. You Can\'t Do That\n7. '
                                     'Long Tall Sally\n8. I Call Your Name\n9. Please Mister Postman\n10. I\'ll Get '
                                     'You\n11. She Loves You',
                                     parse_mode='html')
            elif function_call.data == "a_hard_days_night_us":
                photo = open('images/beatles/us_albums/a_hard_days_night_us.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. A Hard Day\'s Night\n2. Tell Me Why\n3. I\'ll Cry Instead\n4. I Should Have '
                                     'Known Better (Instrumental)\n5. I\'m Happy Just To Dance With You\n6. And I Love '
                                     'Her (Instrumental)\n7. I Should Have Known Better\n8. If I Fell\n9. And I Love '
                                     'Her\n10. Ringo\'s Theme (This Boy)\n11. Can\'t Buy Me Love\n12. A Hard Day\'s '
                                     'Night (Instrumental)',
                                     parse_mode='html')
            elif function_call.data == "something_new":
                photo = open('images/beatles/us_albums/something_new.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. I\'ll Cry Instead\n2. Things We Said Today\n3. Any Time At All\n4. When I Get '
                                     'Home\n5. Slow Down\n6. Matchbox\n7. Tell Me Why\n8. And I Love Her\n9. I\'m '
                                     'Happy Just To Dance With You\n10. If I Fell\n11. Komm, Gib Mir Deine Hand',
                                     parse_mode='html')
            elif function_call.data == "beatles_65":
                photo = open('images/beatles/us_albums/beatles_65.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. No Reply\n2. I\'m A Loser\n3. Baby\'s In Black\n4. Rock And Roll Music\n5. '
                                     'I\'ll Follow The Sun\n6. Mr. Moonlight\n7. Honey Don\'t\n8. I\'ll Be Back\n9. '
                                     'She\'s A Woman\n10. I Feel Fine\n11. Everybody\'s Trying To Be My Baby',
                                     parse_mode='html')
            elif function_call.data == "the_early_beatles":
                photo = open('images/beatles/us_albums/the_early_beatles.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Love Me Do\n2. Twist And Shout\n3. Anna (Go To Him)\n4. Chains\n5. Boys\n6. '
                                     'Ask Me Why\n7. Please Please Me\n8. P.S. I Love You\n9. Baby It\'s You\n10. A '
                                     'Taste Of Honey\n11. Do You Want To Know A Secret',
                                     parse_mode='html')
            elif function_call.data == "beatles_vi":
                photo = open('images/beatles/us_albums/beatles_vi.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Kansas City\n2. Eight Days A Week\n3. You Like Me Too Much\n4. Bad Boy\n5. I '
                                     'Don\'t Want To Spoil The Party\n6. Words Of Love\n7. What You\'re Doing\n8. Yes '
                                     'It Is\n9. Dizzy Miss Lizzy\n10. Tell Me What You See\n11. Every Little Thing',
                                     parse_mode='html')
            elif function_call.data == "help_us":
                photo = open('images/beatles/us_albums/help_us.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Help!\n2. The Night Before\n3. From Me To You Fantasy\n4. You\'ve Got To Hide '
                                     'Your Love Away\n5. I Need You\n6. In The Tyrol\n7. Another Girl\n8. Another Hard '
                                     'Day\'s Night\n9. Ticket To Ride\n10. The Bitter End-You Can\'t Do That\n11. '
                                     'You\'re Going To Lose That Girl\n12. The Chase',
                                     parse_mode='html')
            elif function_call.data == "rubber_soul_us":
                photo = open('images/beatles/us_albums/rubber_soul_us.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. I\'ve Just Seen A Face\n2. Norwegian Wood (This Bird Has Flown)\n3. You '
                                     'Won\'t See Me\n4. Think For Yourself\n5. The Word\n6. Michelle\n7. It\'s Only '
                                     'Love\n8. Girl\n9. I\'m Looking Through You\n10. In My Life\n11. Wait\n12. Run '
                                     'For Your Life',
                                     parse_mode='html')
            elif function_call.data == "yesterday_and_today":
                photo = open('images/beatles/us_albums/yesterday_and_today.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Drive My Car\n2. I\'m Only Sleeping\n3. Nowhere Man\n4. Dr. Robert\n5. '
                                     'Yesterday\n6. Act Naturally\n7. And Your Bird Can Sing\n8. If I Needed Someone\n'
                                     '9. We Can Work It Out\n10. What Goes On\n11. Day Tripper',
                                     parse_mode='html')
            elif function_call.data == "revolver_us":
                photo = open('images/beatles/us_albums/revolver_us.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Taxman\n2. Eleanor Rigby\n3. Love You To\n4. Here, There And Everywhere\n5. '
                                     'Yellow Submarine\n6. She Said She Said\n7. Good Day Sunshine\n8. For No One\n9. '
                                     'I Want To Tell You\n10. Got To Get You Into My Life\n11. Tomorrow Never Knows',
                                     parse_mode='html')
            elif function_call.data == "magical_mystery_tour_lp":
                photo = open('images/beatles/us_albums/magical_mystery_tour_lp.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Magical Mystery Tour\n2. The Fool On The Hill\n3. Flying\n4. Blue Jay Way\n5. '
                                     'Your Mother Should Know\n6. I Am The Walrus\n7. Hello Goodbye\n8. Strawberry '
                                     'Fields Forever\n9. Penny Lane\n10. Baby You\'re A Rich Man\n11. All You Need Is '
                                     'Love',
                                     parse_mode='html')
            elif function_call.data == "please_me":
                photo = open('images/beatles/uk_albums/please_me.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. I Saw Her Standing There\n2. Misery\n3. Anna (Go To Him)\n4. Chains\n5. '
                                     'Boys\n6. Ask Me Why\n7. Please Please Me\n8. Love Me Do\n9. P.S. I Love You\n10. '
                                     'Baby It\'s You\n11. Do You Want To Know A Secret\n12. A Taste Of Honey\n13. '
                                     'There\'s A Place\n14. Twist And Shout',
                                     parse_mode='html')
            elif function_call.data == "with_the_beatles":
                photo = open('images/beatles/uk_albums/with_the_beatles.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. It Won\'t Be Long\n2. All I\'ve Got To Do\n3. All My Loving\n4. Don\'t Bother '
                                     'Me\n5. Little Child\n6. Till There Was You\n7. Please Mister Postman\n8. Roll '
                                     'Over Beethoven\n9. Hold Me Tight\n10. You Really Got A Hold On Me\n11. I Wanna '
                                     'Be Your Man\n12. Devil In Her Heart\n13. Not A Second Time\n14. Money (That\'s '
                                     'What I Want)',
                                     parse_mode='html')
            elif function_call.data == "a_hard_days_night":
                photo = open('images/beatles/uk_albums/a_hard_days_night.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. A Hard Day\'s Night\n 2. I Should Have Known Better\n 3. If I Fell\n 4. '
                                     'I\'m Happy Just To Dance With You\n 5. And I Love Her\n 6. Tell Me Why\n 7. '
                                     'Can\'t Buy Me Love\n 8. Any Time At All\n 9. I\'ll Cry Instead\n 10. Things We '
                                     'Said Today\n 11. When I Get Home\n 12. You Can\'t Do That\n 13. I\'ll Be Back',
                                     parse_mode='html')
            elif function_call.data == "beatles_for_sale":
                photo = open('images/beatles/uk_albums/beatles_for_sale.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. No Reply\n 2. I\'m A Loser\n 3. Baby\'s In Black\n 4. Rock And Roll Music\n '
                                     '5. I\'ll Follow The Sun\n 6. Mr. Moonlight\n 7. Kansas City\n 8. Eight Days A '
                                     'Week\n 9. Words Of Love\n 10. Honey Don\'t\n 11. Every Little Thing\n 12. I '
                                     'Don\'t Want To Spoil The Party\n 13. What You\'re Doing\n 14. Everybody\'s '
                                     'Trying To Be My Baby',
                                     parse_mode='html')
            elif function_call.data == "help_":
                photo = open('images/beatles/uk_albums/help_.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Help!\n2. The Night Before\n3. You\'ve Got To Hide Your Love Away\n4. I Need '
                                     'You\n5. Another Girl\n6. You\'re Going To Lose That Girl\n7. Ticket To Ride\n8. '
                                     'Act Naturally\n9. It\'s Only Love\n10. You Like Me Too Much\n11. Tell Me What '
                                     'You See\n12. I\'ve Just Seen A Face\n13. Yesterday\n14. Dizzy Miss Lizzy',
                                     parse_mode='html')
            elif function_call.data == "rubber_soul":
                photo = open('images/beatles/uk_albums/rubber_soul.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Drive My Car\n2. Norwegian Wood (This Bird Has Flown)\n3. You Won\'t See Me\n'
                                     '4. Nowhere Man\n5. Think For Yourself\n6. The Word\n7. Michelle\n8. What Goes '
                                     'On\n9. Girl\n10. I\'m Looking Through You\n11. In My Life\n12. Wait\n13. If I '
                                     'eeded Someone\n14. Run For Your Life',
                                     parse_mode='html')
            elif function_call.data == "revolver":
                photo = open('images/beatles/uk_albums/revolver.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Taxman\n2. Eleanor Rigby\n3. I\'m Only Sleeping\n4. Love You To\n5. Here, '
                                     'There And Everywhere\n6. Yellow Submarine\n7. She Said She Said\n8. Good Day '
                                     'Sunshine\n9. And Your Bird Can Sing\n10. For No One\n11. Dr. Robert\n12. I Want '
                                     'To Tell You\n13. Got To Get You Into My Life\n14. Tomorrow Never Knows',
                                     parse_mode='html')
            elif function_call.data == "sgt_pepper":
                photo = open('images/beatles/uk_albums/sgt_pepper.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Sgt. Pepper\'s Lonely Hearts Club Band\n2. With A Little Help From My Friends'
                                     '\n3. Lucy In The Sky With Diamonds\n4. Getting Better\n5. Fixing A Hole\n6. She'
                                     '\'s Leaving Home\n7. Being For The Benefit Of Mr. Kite\n8. Within You Without Yo'
                                     'u\n9. When I\'m Sixty Four\n10. Lovely Rita\n11. Good Morning Good Morning\n12.'
                                     ' Sgt. Pepper\'s Lonely Hearts Club Band (Reprise)\n13. A Day In The Life',
                                     parse_mode='html')
            elif function_call.data == "the_beatles":
                photo = open('images/beatles/uk_albums/the_beatles.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Back In The U.S.S.R.\n2. Dear Prudence\n3. Glass Onion\n4. Ob-La-Di, Ob-La-'
                                     'Da\n5. Wild Honey Pie\n6. The Continuing Story Of Bungalow Bill\n7. While My '
                                     'Guitar Gently Weeps\n8. Happiness Is A Warm Gun\n9. Martha My Dear\n10. I\'m So'
                                     ' Tired\n11. Blackbird\n12. Piggies\n13. Rocky Raccoon\n14. Don\'t Pass Me By\n'
                                     '15. Why Don\'t We Do It In The Road\n16. I Will\n17. Julia\n18. Birthday\n19. '
                                     'Yer Blues\n20. Mother Nature\'s Son\n21. Everybody\'s Got Something To Hide '
                                     'Except Me And My Monkey\n22. Sexy Sadie\n6. Helter Skelter\n23. Long, Long, '
                                     'Long\n24. Revolution 1\n25. Honey Pie\n26. Savoy Truffle\n27. Cry Baby Cry\n'
                                     '28. Revolution 9\n29. Good Night',
                                     parse_mode='html')
            elif function_call.data == "yellow_submarine":
                photo = open('images/beatles/uk_albums/yellow_submarine.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Yellow Submarine\n2. Only A Northern Song\n3. All Together Now\n4. Hey Bulld'
                                     'og\n5. It\'s All Too Much\n6. All You Need Is Love\n7. Pepperland\n8. Sea Of '
                                     'Time\n9. Sea Of Holes\n10. Sea Of Monsters\n11. March Of The Meanies\n12. Pepp'
                                     'erland Laid Waste\n13. Yellow Submarine In Pepperland',
                                     parse_mode='html')
            elif function_call.data == "abbey_road":
                photo = open('images/beatles/uk_albums/abbey_road.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Come Together\n2. Something\n3. Maxwell\'s Silver Hammer\n4. Oh! Darling\n5. '
                                     'Octopus\'s Garden\n6. I Want You (She\'s So Heavy)\n7.  Here Comes The Sun\n8.  '
                                     'Because\n9.  You Never Give Me Your Money\n10.  Sun King\n11.  Mean Mr. '
                                     'Mustard\n12.  Polythene Pam\n13.  She Came In Through The Bathroom Window\n14. '
                                     ' Golden Slumbers\n15.  Carry That Weight\n16.  The End\n17.  Her Majesty',
                                     parse_mode='html')
            elif function_call.data == "let_it_be":
                photo = open('images/beatles/uk_albums/let_it_be.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Two Of Us\n2. Dig A Pony\n3. Across The Universe\n4. I Me Mine\n5. Dig It\n6. '
                                     'Let It Be\n7. Maggie Mae\n8. I\'ve Got A Feeling\n9. One After 909\n10. The '
                                     'Long And Winding Road\n11. For You Blue\n12. Get Back',
                                     parse_mode='html')
            elif function_call.data == "oldies_but_goldies":
                photo = open('images/beatles/compil_63_90/oldies_but_goldies.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. She Loves You\n2. From Me To You\n3. We Can Work It Out\n4. Help!\n5. Mich'
                                     'elle\n6. Yesterday\n7. I Feel Fine\n8. Yellow Submarine\n9. Can\'t Buy Me Lo'
                                     've\n10. Bad Boy\n11. Day Tripper\n12. A Hard Day\'s Night\n13. Ticket To Rid'
                                     'e\n14. Paperback Writer\n15. Eleanor Rigby\n16. I Want To Hold Your Hand',
                                     parse_mode='html')
            elif function_call.data == "hey_jude":
                photo = open('images/beatles/compil_63_90/hey_jude.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Can\'t Buy Me Love\n2. I Should Have Known Better\n3. Paperback Writer\n4. Ra'
                                     'in\n5. Lady Madonna\n6. Revolution\n7. Hey Jude\n8. Old Brown Shoe\n9. Don\'t L'
                                     'et Me Down\n10. The Ballad Of John And Yoko',
                                     parse_mode='html')
            elif function_call.data == "in_the_beginning":
                photo = open('images/beatles/compil_63_90/in_the_beginning.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Ain\'t She Sweet\n2. Cry For A Shadow\n3. Let\'s Dance\n4. My Bonnie\n5. Tak'
                                     'e Out Some Insurance On Me\n6. What\'d I Say\n7. Sweet Georgia Brown\n8. When t'
                                     'he Saints Go Marching In\n9. Ruby Baby\n10. Why\n11. Nobody\'s Child\n12. Ya Ya',
                                     parse_mode='html')
            elif function_call.data == "red_album":
                photo = open('images/beatles/compil_63_90/red_album.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Love Me Do\n2. Please Please Me\n3. From Me To You\n4. She Loves You\n5. I '
                                     'Want To Hold Your Hand\n6. All My Loving\n7. Can\'t Buy Me Love\n8. A Hard '
                                     'Day\'s Night\n9. And I Love Her\n10. Eight Days A Week\n11. I Feel Fine\n12. '
                                     'Ticket To Ride\n13. Yesterday\n14. Help!\n15. You\'ve Got To Hide Your Love '
                                     'Away\n16. We Can Work It Out\n17. Day Tripper\n18. Drive My Car\n19. Norwegian'
                                     ' Wood (This Bird Has Flown)\n20. Nowhere Man\n8. Michelle\n21. In My Life\n10. '
                                     'Girl\n22. Paperback Writer\n23. Eleanor Rigby\n24. Yellow Submarine',
                                     parse_mode='html')
            elif function_call.data == "blue_album":
                photo = open('images/beatles/compil_63_90/blue_album.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Strawberry Fields Forever\n2. Penny Lane\n3. Sgt. Pepper\'s Lonely Hearts Club'
                                     ' Band\n4. With A Little Help From My Friends\n5. Lucy In The Sky With Diamond'
                                     's\n6. A Day In The Life\n7. All You Need Is Love\n8. I Am The Walrus\n9. Hello '
                                     'Goodbye\n10. The Fool On The Hill\n11. Magical Mystery Tour\n12. Lady Madonna'
                                     '\n13. Hey Jude\n14. Revolution\n15. Back In The U.S.S.R.\n16. While My Guitar '
                                     'Gently Weeps\n17. Ob-La-Di, Ob-La-Da\n18. Get Back\n19. Don\'t Let Me Down\n20. '
                                     'The Ballad Of John And Yoko\n21. Old Brown Shoe\n22. Here Comes The Sun\n23. '
                                     'Come Together\n24. Something\n25. Octopus\'s Garden\n26. Let It Be\n27. Across '
                                     'The Universe\n28. The Long And Winding Road',
                                     parse_mode='html')
            elif function_call.data == "rock_n_roll_music":
                photo = open('images/beatles/compil_63_90/rock_n_roll_music.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Twist And Shout\n2. I Saw Her Standing There\n3. You Can\'t Do That\n4. I '
                                     'Wanna Be Your Man\n5. I Call Your Name\n6. Boys\n7. Long Tall Sally\n8. Rock '
                                     'And Roll Music\n9. Slow Down\n10. Kansas City\n11. Money (That\'s What I '
                                     'Want)\n12. Bad Boy\n13. Matchbox\n14. Roll Over Beethoven\n15. Dizzy Miss '
                                     'Lizzy\n16. Any Time At All\n17. Helter Skelter\n18. Drive My Car\n19. '
                                     'Everybody\'s Trying To Be My Baby\n20. The Night Before\n21. I\'m Down\n22. '
                                     'Revolution\n23. Back In The U.S.S.R.\n24. Taxman\n25. Got To Get You Into My '
                                     'Life\n26. Hey Bulldog\n27. Birthday\n28. Get Back',
                                     parse_mode='html')
            elif function_call.data == "love_songs":
                photo = open('images/beatles/compil_63_90/love_songs.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Yesterday\n2. I\'ll Follow The Sun\n3. I Need You\n4. Girl\n5. In My Life\n6. '
                                     'Words Of Love\n7. Here, There And Everywhere\n8. Something\n9. And I Love '
                                     'Her\n10. If I Fell\n11. I\'ll Be Back\n12. Tell Me What You See\n13. Yes It '
                                     'Is\n14. Michelle\n15. It\'s Only Love\n16. You\'re Going To Lose That Girl\n17. '
                                     'Every Little Thing\n18. For No One\n19. She\'s Leaving Home\n20. The Long And '
                                     'Winding Road\n21. This Boy\n22. Norwegian Wood (This Bird Has Flown)\n23. '
                                     'You\'ve Got To Hide Your Love Away\n24. I Will\n25. P.S. I Love You',
                                     parse_mode='html')
            elif function_call.data == "rarities_uk":
                photo = open('images/beatles/compil_63_90/rarities_uk.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Across The Universe\n2. Yes It Is\n3. This Boy\n4. The Inner Light\n5. I\'ll '
                                     'Get You\n6. Thank You Girl\n7. Komm, Gib Mir Deine Hand\n8. You Know My Name '
                                     '(Look Up The Number)\n9. Sie Liebt Dich\n10. Rain\n11. She\'s A Woman\n12. '
                                     'Matchbox\n13. I Call Your Name\n14. Bad Boy\n15. Slow Down\n16. I\'m Down\n17. '
                                     'Long Tall Sally',
                                     parse_mode='html')
            elif function_call.data == "rarities_us":
                photo = open('images/beatles/compil_63_90/rarities_us.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Love Me Do (with Ringo Starr).\n2. Misery.\n3. There\'s A Place.\n4. Sie '
                                     'Liebt Dich.\n5. And I Love Her (German \'Something New\' mix).\n6. Help! (Single '
                                     'edit).\n7. I\'m Only Sleeping (UK album edit).\n8. I Am The Walrus (England '
                                     'version).\n9. Penny Lane (NA radio edit).\n10. Helter Skelter (Mono version)'
                                     '\n11. Don\'t Pass Me By (Mono version).\n12. The Inner Light\n13. Across The '
                                     'Universe (Wildlife edit)\n14. You Know My Name (Look Up The Number)\n15. Sgt. '
                                     'Pepper Inner Groove',
                                     parse_mode='html')
            elif function_call.data == "ballads":
                photo = open('images/beatles/compil_63_90/ballads.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Yesterday\n2.  Hey Jude\n3. Norwegian Wood (This Bird Has Flown)\n4. Do You '
                                     'Want To Know A Secret\n5. For No One\n6. Michelle\n7. Nowhere Man\n8. You\'ve '
                                     'Got To Hide Your Love Away\n9. Across The Universe (Wildlife version)\n10. All '
                                     'My Loving\n11. Something\n12.  Let It Be (Single edit)\n13. The Fool On The '
                                     'Hill\n14. Till There Was You\n15. The Long And Winding Road\n16. Here Comes The '
                                     'Sun\n17. Blackbird\n18. And I Love Her\n19. She\'s Leaving Home\n20. Here, There '
                                     'And Everywhere',
                                     parse_mode='html')
            elif function_call.data == "reel_music":
                photo = open('images/beatles/compil_63_90/reel_music.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. A Hard Day\'s Night\n2. I Should Have Known Better\n3. Can\'t Buy Me Love\n4. '
                                     'And I Love Her\n5. Help!\n6. You\'ve Got To Hide Your Love Away\n7. Ticket To '
                                     'Ride\n8. Magical Mystery Tour\n9. I Am The Walrus\n10. Yellow Submarine\n11. '
                                     'All You Need Is Love (YS edit)\n12. Let It Be (Album edit)\n13. Get Back (Album '
                                     'edit)\n14. The Long And Winding Road',
                                     parse_mode='html')
            elif function_call.data == "greatest_hits_uk":
                photo = open('images/beatles/compil_63_90/greatest_hits_uk.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Love Me Do (Single edit)\n2.  Day Tripper\n3.  We Can Work It Out\n4. From '
                                     'Me To You\n5. She Loves You\n6. I Want To Hold Your Hand\n7. Can\'t Buy Me '
                                     'Love\n8. A Hard Day\'s Night\n9. I Feel Fine\n10. Ticket To Ride\n11. Help!\n12. '
                                     'Paperback Writer\n13. Yellow Submarine\n14. Eleanor Rigby\n15. All You Need Is '
                                     'Love\n16. Hello Goodbye\n17. Lady Madonna\n18. Hey Jude\n19. Get Back (Single '
                                     'edit)\n20. The Ballad Of John And Yoko',
                                     parse_mode='html')
            elif function_call.data == "greatest_hits_us":
                photo = open('images/beatles/compil_63_90/greatest_hits_us.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. She Loves You\n2.  Yesterday\n3.  We Can Work It Out\n4.  Paperback Writer\n'
                                     '5. Love Me Do (album edit)\n6. I Want To Hold Your Hand\n7. Can\'t Buy Me Love\n'
                                     '8. A Hard Day\'s Night\n9. I Feel Fine\n10. Eight Days A Week\n11. Ticket To '
                                     'Ride\n12. Help!\n13. Penny Lane\n14. All You Need Is Love\n15. Hello Goodbye\n'
                                     '16. Hey Jude (Shorted version).\n17. Get Back (Single edit)\n18. Come Together\n'
                                     '19. Let It Be (Single edit)\n20. The Long And Winding Road',
                                     parse_mode='html')
            elif function_call.data == "past_masters_1":
                photo = open('images/beatles/compil_63_90/past_masters_1.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Love Me Do (Single edit)\n2. From Me To You\n3. Thank You Girl\n4. She Loves '
                                     'You\n5. I\'ll Get You\n6. I Want To Hold Your Hand\n7. This Boy\n8. Komm, Gib '
                                     'Mir Deine Hand\n9. Sie Liebt Dich\n10. Long Tall Sally\n11. I Call Your '
                                     'Name\n12. Slow Down\n13. Matchbox\n14. I Feel Fine\n15. She\'s A Woman\n16. '
                                     'Bad Boy\n17. Yes It Is\n18. I\'m Down',
                                     parse_mode='html')
            elif function_call.data == "past_masters_2":
                photo = open('images/beatles/compil_63_90/past_masters_2.jpg', 'rb')
                photo = resize_image(photo)
                botBitl.send_photo(function_call.message.chat.id, photo=photo)
                botBitl.send_message(function_call.message.chat.id,
                                     '1. Day Tripper\n2. We Can Work It Out\n3. Paperback Writer\n4. Rain\n5. Lady '
                                     'Madonna\n6. The Inner Light\n7. Hey Jude\n8. Revolution\n9. Get Back (Single '
                                     'edit)\n10. Don\'t Let Me Down\n11. The Ballad Of John And Yoko\n12. Old Brown '
                                     'Shoe\n13. Across The Universe (Wildlife edit)\n14. Let It Be (Single edit)\n15. '
                                     'You Know My Name (Look Up The Number)',
                                     parse_mode='html')

            botBitl.answer_callback_query(function_call.id)


botBitl.infinity_polling()

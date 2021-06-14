# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")
init python:
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # функция переводит текущее время в название времени суток
    import datetime
    def get_t():
        h = int(datetime.datetime.now().strftime("%H"))
        res = "night" # по умолчанию ночь
        # границы любого времени суток можно поменять
        if (h > 6) and (h < 11):
            res = "morning"
        if (h >= 11) and (h <= 18):
            res = "day"
        if (h > 18) and (h < 23):
            res = "evening"
        return res
    last_t = None
    # функция меняет музыку и освещение в меню
    # в зависимости от времени суток
    def change_mus():
        global last_t
        if last_t != get_t():
            last_t = get_t()
            # перезапускаем отрисовку меню
            renpy.restart_interaction()
            # меняем мелодию в главном меню
            config.main_menu_music = last_t + ".ogg"
            if renpy.music.get_playing() != last_t + ".ogg":
                renpy.music.play(last_t + ".ogg")
    # функцию - в action
    ChangeMus = renpy.curry(change_mus)
    # картинка для фона главного меню
    #style.mm_root.background = "back.jpg"
    # в main_menu после style "mm_root":
    # timer .05 repeat True action ChangeMus()
    # if last_t:
        # add last_t

init:
    # фильтры для освещения
    image morning = "#8404"
    image day     = "#0000"
    image evening = "#0484"
    image night   = "#000b"
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene back2
    with dissolve
    show dude4
    #play audio "day.ogg"
    e "начало."
    jump choise
    e "конец"

    return
label choise:
    python:
        import requests
        import json
        #import certifi
        try:
            response = requests.get('https://api.thedogapi.com/v1/images/search')
            items = json.loads(response.text)
            b=items[0][u'breeds'][0][u'name']
        except:
            b='buldog'
    e "хочу узнать какую породу собак ти любиш"
    e "нравляться [b]"

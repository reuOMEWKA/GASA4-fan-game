# Игра начинается здесь:
label start:
    window hide
    play music ooo volume 0.4
    scene black
    pause (2)
    title "Приветствую."
    pause (2)
    title "Вам никогда не хотелось приблизиться к Вашей любимой вселенной,{w=.15} поболтать с её героями?"
    title "Заставить их {i}любить{/i} Вас.{w=.3} Лелеять,{w=.15} обожать,{w=.15} быть {i}одержимыми{/i} вами..."
    pause (2)
    show nar eyes_o at nar with fade
    title "Я дам Вам такую возможность."
    show nar eyes_uno
    show user b1 with slowdissolve
    pause (1)
    title "Отдам контроль над марионеткой,{w=.15} дабы Вы смогли ощутить то счастье,{w=.15} радость от вида знакомых персонажей."
    show nar eyes_oh
    title "Но,{w=.15} ах,{w=.15} не волнуйтесь..{w=.3}{nw}"
    show nar eyes_ch
    extend "нет нужды в ревности."
    show user b2
    show nar eyes_uno
    title "Весь контроль их действий,{w=.15} мыслей,{w=.15} слов{w=.15} и даже {i}биологических{/i} факторов{w=.15} пренадлежат Вам."
    show user b3
    show nar eyes_o
    pause (3)
    show nar eyes_oh
    title "Чтож, почему бы нам не начать?"
    show nar eyes_ch
    show user b4:
        linear 0.2 yalign 0.5
    pause (0.2)
    hide user
    show user b5 with sshake
    pause (0.2)
    show nar eyes_oq
    title "Невежливо сидеть,{w=.15} пока твой новый хозяин стоит,{w=.15} не так ли,{w=.15} {glitch=59.94}amor meus{/glitch}?"
    show nar eyes_o
    pause (1)
    show nar eyes_uno
    title "Точно...{w=.3} Раз уж теперь {i}Вы{/i} хозяин марионетки,{w=.15} вам стоит дать ей имя..."
    show nar eyes_ch
    title "Приму любое,{w=.15} выбор только за вами!"
    with slowdissolve
    hide nar
    hide user
    with slowdissolve
    stop music fadeout 1
    pause (0.5)
    scene choice
    with slowdissolve
    play music uwa volume 0.3
    jump name
label name:
    python:
        y = renpy.input("", allow="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'/.", default="МС", length=12)
        y = y.strip()
    "[y].{w=.3} Вас устраивает данное имя?"
    menu:
        "Да, более чем.":
            jump continue
        "Хотя, если подумать...":
            "Всё в порядке.{w=.3} Просто впишите новое имя."
            jump name
label continue:
    stop music fadeout 1
    scene black
    with slowdissolve
    pause (0.5)
    show nar eyes_ch at nar
    show user b6
    with slowdissolve
    play music ooo volume 0.4
    title "Восхитительно!{w=.3} Думаю,{w=.15} [y] нравиться их новое имя!"
    show nar eyes_oq
    title "Или же ей....{w=.3}или ему..."
    show nar eyes_uno
    title "Будет неправильно выбирать за Вас,{w=.15} какие местоимения должны использоваться {i}Вашей{/i} марионеткой."
    hide nar
    jump choiceGENDER

label choiceGENDER:
    show screen choiceGENDER
    title "Какие местоимения будут иметь [y]?"

label male:
    $ male = True
    $ female = False
    $ person = False
    jump A


label female:
    $ female = True
    $ male = False
    $ person = False
    jump A

label person:
    $ person = True
    $ female = False
    $ male = False
    jump A

label A:
    hide user
    show nar eyes_oq at nar
    show user b7
    if person:
        title "Нейтральные местоимения,{w=.15} хм?"
        show nar eyes_oh
        title "Хороший выбор.{w=.3} Думаю,{w=.15} [y] нравиться."
        show nar eyes_o
        title "Хотя,{w=.15} они вроде и не ребёнок,{w=.15} чтобы радоваться по мелочам..."
        show nar eyes_oq
        title "Или,{w=.15} может,{w=.15} я ошибаюсь?"

    if male:
        title "Мужские местоимения,{w=.15} хм?"
        show nar eyes_oh
        title "Хороший выбор.{w=.3} Думаю,{w=.15} [y] нравиться."
        show nar eyes_o
        title "Хотя,{w=.15} он вроде и не ребёнок,{w=.15} чтобы радоваться по мелочам..."
        title "Или,{w=.15} может,{w=.15} я ошибаюсь?"

    if female:
        title "Женские местоимения,{w=.15} хм?"
        show nar eyes_oh
        title "Хороший выбор.{w=.3} Думаю,{w=.15} [y] нравиться."
        show nar eyes_o
        title "Хотя,{w=.15} она вроде и не ребёнок,{w=.15} чтобы радоваться по мелочам..."
        show nar eyes_oq
        title "Или,{w=.15} может,{w=.15} я ошибаюсь?"
    hide nar
    jump choiceAGE

label choiceAGE:
    show screen choiceAGE
    title "Сколько лет [y]?"

label teen:
    $ teenager = True
    $ kiddo = False
    $ adult = False
    jump end
label kid:
    $ kiddo = True
    $ teenager = False
    $ adult = False
    jump end
label adult:
    $ adult = True
    $ teenager = False
    $ kiddo = False
    jump end

label end:
    hide user
    show nar eyes_oq at nar
    if kiddo:
        show user b8_k
        title "Значит всё же ребёнок,{w=.15} да?"
        show nar eyes_o
        show user b9_k
        title "Учти, что если Вы выберите этот вариант,{w=.15} то [y] не сможет завести романтических отношений с персонажами."
        show nar eyes_uno
        title "Но мне то какая разница?"
    if teenager:
        show user b8_t
        title "Значит подросток,{w=.15} да?"
        show user b9_t
    if adult:
        show user b8_a
        title "Значит взрослый,{w=.15} да?"
        show user b9_a
    
    show nar eyes_ch
    title "Интересный выбор,{w=.15} правда."
    show nar eyes_o
    title "Надеюсь,{w=.15} Вы знаете возраст персонажей,{w=.15} с которыми хотите встетиться в игре."
    show nar eyes_uno
    title "Чтож...{w=.3}давай же начнём нашу невинную игру,{w=.15} игрок."
    stop music fadeout 1

    if kiddo:
        with slowdissolve
        jump kidstory
    if teenager:
        with slowdissolve
        jump teenstory
    if adult:
        with slowdissolve
        jump adstory
return
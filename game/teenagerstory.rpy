label teenstory:
    scene black with slowdissolve
    pause (0.4)
    play music uwa volume 0.5
    scene choice with slowdissolve
    show cr talk at lilleft
    cr "Привет!!"
    show cr shy
    cr "Вас, ам, не должно здесь быть.."
    cr "Типа, пока что готов детский рут..."
    show cr say
    cr "Но было бы жестоко, если бы я заставила Вас всё читать с начала."
    cr "Потому я дам вам возможность перейти на детский рут, сохранив имя и местоимения"
    menu:
        "Перейти на детский рут (7-14 лет)":
            $ teenager = False
            $ kiddo = True
            show cr happy
            cr "Отлично! Хорошей игры!!"
            scene black with slowdissolve
            pause (0.4)
            jump kidstory
        "Выйти в главный экран":
            show cr happy
            cr "Как скажешь! Хорошего дня!!"
return
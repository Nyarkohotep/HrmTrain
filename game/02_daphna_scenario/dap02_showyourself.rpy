#########################
######### LEVEL 02 ##########
#########################
####REQUEST_02 Show Your Self####
#########################
label dap_request_02: #LV.2 (Whoring = 3 - 9)
    
    $music("Daphne Theme")

label dap_request_02_complete:
    if daphne.whoring < 3:
        $hero("Похоже что она еще не готова к этому разговору...// Может позже....")
        call daphne_main_menu_requests
    pass
    if IsRunNumber(1):
        $hero("Итак, мисс Гринграсс. Настало время поучиться держаться на сцене. Вы готовы?")
        $daphne("~55 00 1 def// Да, сэр, что я должна сделать? Ходить?")
        $hero("Нет, мисс, лежать.")
        $daphne("~46 w0 1 def// ...?!")
        $hero(g4, "Ох, прошу прощения, мисс, я смотрел на вас и вдруг замечтался...")
        $daphne("~37 s0 1 neu// О чем это вы замечтались?")
        $hero("Я-то? Замечтался о... о проблемах факультета, да...",
            m," Нет-нет, не нужно ничего такого сложного \"ходить, лежать\"... Просто уменьшим количество вашей одежды.")
        $daphne("~37 c0 1 dis// Одежды, сэр? Но... я и сейчас в такой одежде, что мама посчитала бы это одеждой шлюхи!")
        $hero("Мисс Гринграсс, на конкурсе не будет вашей мамы, но будет жюри, которое ожидает увидеть конкурсанток в подходящих нарядах.// Вы, конечно, можете выйти на подиум в, как это по-рюсски... v tulup.//"
         "Но вряд ли ваш стиль оценят. На вас должно оставаться минимум одежды, чтобы члены жюри отметили вашу внешность.")
        $daphne("~73 c0 1 pri// О, сэр. Это... это ужасно. Меня будут рассматривать, как породистую ... лошадь!")
        $hero("#Хе-хе. Вариант \"суку\" мне нравился больше.")
        $daphne("~73 00 1 pri// Вы что-то сказали, сэр?")
        $hero("О, это не стоит вашего внимания, мисс. Так от чего вы избавитесь вначале?")
        $daphne("~73 00 1 ehh// Ну, я могу сменить топ на более открытый. Надеюсь, этого достаточно?")
        $hero("Мисс, это ваш конкурс ваш успех и ваш провал. Вам решать достаточно этого или нет.")
        $daphne("~73 01 1 pur// Хм,... Ну, я надеюсь, что этого пока хватит.")

        $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
        $daphne.ItemsCustomize(delete={"sleeves"}).chibi.State(appearance="c")#.Refresh()
        pause.5
        $screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
        $screens.Show("ctc").Pause().Hide("ctc")

        $hero("У вас симпатичные руки, мисс Гринграсс, я никогда не видел их обнаженными.")
        $daphne("~73 00 2 ang// Ох, сэр, пожалуйста.")
        $hero("Зеленые лямки лифчика не слишком гармонируют.")
        $daphne("~73 00 2 pou// Ох, сэр, ну я же рассчитывала, что придется...")
        $hero("Оголяться перед мужчиной?")
        $daphne("~73 n2 3 def// Ну, да...")
        $hero("Все в порядке, мисс. Вы выглядите очень привлекательно. Думаю, вы заслужили сегодня небольшую награду.")
        $daphne.whoring += 1
    elif IsRunNumber(2):
        $hero("Ну что ж, мисс Гринграсс. Давайте дальше учиться держаться на сцене.")
        $daphne("~55 00 2 def// Мне ходить... или?")
        $hero("Или! Вам надо избавиться еще от одной детали одежды.")
        $daphne("~46 00 2 ehh// Отлично, давно хотела снять эти чулки, в них я выгляжу по-уродски.")

        $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
        $daphne.ItemsCustomize(delete={"stockings"}).chibi.State(appearance="c")#.Refresh()
        pause.5
        $screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
        $screens.Show("ctc").Pause().Hide("ctc")

        $hero("Вот это энтузиазм! Вам следует сохранять его, мисс, пока вы будете снимать всю остальную одежду.")
        $daphne("~46 w0 1 ehh// ВСЮ?!...")
        $hero(g4, "Эм... Это я образно, мисс.",m ,"Давайте лучше посмотрим, что я сегодня смогу вам подарить.")
        $daphne.whoring += 1
    elif IsRunNumber(3):
        $hero("Итак, мисс Гринграсс, ваша форма приближается к той, в которой вы будете выступать.")
        $daphne("~55 00 1 neu// Сэр, она и так уже почти такая!")
        $hero("Отнюдь, мисс, нам еще многое предстоит. Пора избавиться от еще одной вещи.")
        $daphne("~55 00 1 ehh// От какой?")
        $hero("Решите сами, мисс.")
        $daphne("~26 01 2 ope// Вы же не ожидаете, сэр, что я буду демонстрировать вам нижнее белье?! Как это будет выглядеть?!")
        $hero("На сцене на вас должно остаться только то, что вы называете нижним бельем, мисс.//"
            "Кстати, уверен, ВАШЕ нижнее белье самого высокого качества и подобрано с присущим вам изяществом...//"
            "Так что его не стыдно продемонстрировать в самом изысканном обществе.")
        $daphne("~26 01 2 smi// Эм... Вы, конечно, правы, сэр.")
        $hero("#(Гребаные пески, все время приходится следить за языком, чтобы не ляпнуть \"На колени, шлюха!\")")
        $daphne("~37 00 2 smi// Я говорю, вы правы, насчет изящества...//~73 00 2 smi// Сэр?")
        $hero("А? Да, так о чем я... Я с удовольствием полюбуюсь вашим нижним бельем, мисс. Когда вы будете готовы, конечно.")
        $daphne("~73 01 2 ehh// О... Я даже не знаю... Оно действительно изящное, в конце концов я волшебница в Мерлин знает каком!...")
        $hero("#(Только она начинает нести эту пургу, у меня тут же все опускается...)")
        $daphne("~73 01 2 pur// Но я пока не готова, сэр. И раз сегодня нужно что-то снять...//~55 01 2 pou// Тогда я сниму лифчик. Отвернитесь, сэр!//~55 01 3 pou// Хотя нет, лучше я сама отвернусь.")

        $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
        $daphne.ItemsCustomize(delete={"bra"}, update={"combi:cheer_topbase_withnipples"}).chibi.State(appearance="f")#.Refresh()
        pause.5
        $screens.Hide(Dissolve(1), "blkfade") 
        $screens.Show("ctc").Pause().Hide("ctc")

        $hero("Гхм, вы решили показать мне ваши стоящие соски? Я оценил, они превосходны!")
        $daphne("~37 00 2 ope// Что?! Сэр!")
        $hero("Мисс Гринграсс, вы могли снять блузку и за вашим плотным лифчиком я бы не увидел этих волнующих подробностей.// Но вы предпочли продемонстрировать мне, что возбуждены.")
        $daphne("~26 00 3 wo// Что? Нет! Да как вы смеете!")
        $hero("Мисс Гринграсс, не нужно сердиться, это хорошая новость, что вы возбуждаетесь, когда демонстрируете себя мужчине.// Это поможет вам и не только на конкурсе.")
        $daphne("~26 00 3 ope// Это... это совсем не из-за того, что я сняла лифчик, чтоб вы знали!")
        $hero("Хм. Неужели вас так возбудил разговор о том, как вы будете стоять перед зрителями в одном нижнем белье?")
        $daphne("~26 00 3 dis// Сэр, это просто за гранью!!! Я немедленно пожалуюсь родителям!")
        $hero("Которым вы даже не сообщили, что пытаетесь стать Мисс Хогвартс?//"
            "Они ведь не читают \"пророка\", не так ли?")
        $daphne("~55 s0 3 pou")
        $hero("Полагаю, вы хотели торжественно вернуться с победой, либо сохранить в тайне, если провалитесь.//"
            "Но вряд ли, девушка, от миссис Гринграсс удастся скрыть, если вы со свистом вылетите в первом туре.//"
            "Ваши недруги на факультете об этом позаботятся.//")
        $daphne("~37 01 3 dis// ........................")
        $hero("#(Похоже, я все же немного перегнул палку... Но думаю, девушка слишком много поставила на этот конкурс, так что все обойдется.)//"
            "Мисс, конечно, как поступить, решать вам.// Но в знак моего особого к вам отношения подарок вам я все равно приготовил.")
        $daphne.whoring += 1
        $daphne.liking-=7
    elif IsRunNumber(4):
        $hero("Ну что ж, мисс Гринграсс, вы выглядите потрясающе....")
        $daphne("~73 01 1 smi// ....Спасибо профессор.")
        $hero("За исключением одного «но»....")
        $daphne("~37 n0 1 pou// «но»....// Что-то не так, сэр?//~37 00 2 neu// Мне ведь уже нечего снимать....")
        $hero(g9, "#(Это мы еще проверим)")
        $daphne("~73 00 2 pri// Что, сэр?")
        $hero(m, "Эм.... Я говорю, что сегодня вам нужно научиться правильно демонстрировать свое нижнее белье.")
        $daphne("~26 00 3 dis// {size=+5}Всмысле?!{/size}")
        $daphne("{size=+5}Сэр, это не позволительно!{/size}")
        $hero(".................// А два дня назад мне показалось, что для вас это в порядке вещей.....// Ну тогда надейтесь на удачу.....// Только она сможет вам помочь.....// Можете быть свободны мисс Гринграсс....")
        $daphne("~55 00 2 dis// Пф!...")
        $daphne.liking-=15
        $wtevent.Finalize("daphne_goout")
        $hero(g4, "#(Не умеешь ты держать рот на замке, Джинни)")
    elif IsRunNumber(5):
        if daphne.whoring < 5:
            $daphne("Сэр, у меня сейчас есть дела...// Давайте продолжим позже....")
            call daphne_goout
        pass
        $daphne("..............//~46 00 1 neu// Сэр, простите меня за то что было....// Просто я...//~73 01 1 ang// .....Я не могу профессор.")
        $hero(m, "Ничего Дафна....// Я не сержусь....// Просто мне показалось, что вы готовы к этому....")
        $daphne("~37 n0 1 pou// ....Я тоже так думала, сэр....//~46 w0 1 dis// Но... я не могу находиться в нижнем белье, когда на меня пялиться куча народу.")
        $hero("Ну во первых мисс Гринграсс, здесь кроме меня никого нет.")
        $hero("А во вторых - что плохого в том, что вы в нижнем белье?// Вас же не просят полностью раздеваться....")
        $daphne("~26 00 3 dis// Профессор?!....")
        $hero("Не предирайтесь к словам....// Это в качестве примера...")
        $daphne("~37 00 2 neu// Эм........// Ну... я даже не знаю....// ................")
        $hero("....Вы же хотели сделать сюрприз родителям.... мисс Гринграсс?!")
        $daphne("~73 n0 1 pri// .................// .....Ну хорошо профессор.//~46 00 1 neu// Вы правы.... здесь нет ничего постыдного.")
        $hero(g9, "#(Хе-хе, никто и не сомневался)")
        $daphne("~73 01 2 ehh// ....Сэр?!")
        $hero(m, "Эм... Я говрю, что рад тому, что вы разобрались в себе.// Ну мисс... если вы готовы...")
        $daphne("~73 01 2 pur// Да, да...// ......Я готова.")
        $hero("Хорошо.....// ....Так что бы вы хотели снять?")
        $daphne("~37 02 3 dis// Эм... «Хотела бы...»//~73 00 2 pri// ......Незнаю, профессор...")
        $hero(".......................// Скажем так - мисс Гринграсс...// Что вы бы не постеснялись снять?")
        $daphne(".....Не постеснялась бы, сэр?//~73 c0 1 pri// #..........................//~37 00 2 ope// Думаю я могла бы снять блузку....//~37 00 2 neu// Дайте мне минуту...")
        "> Вы замечаете, что Дафна немного не уверенна в себе, но она все-таки снимает блузку."

        $screens.Show(Dissolve(1), "blkfade") #Черный экран
        $daphne.ItemsCustomize(delete={"combi"}, update={"bra"}) #delete - снять (одетую) вешь. update - одеть вещь.
        pause.5
        $screens.Hide(Dissolve(1), "blkfade") 
        $screens.Show("ctc").Pause().Hide("ctc")

        $hero("Хорошо мисс Гринграсс....// Чувствуете себя не ловко?")
        $daphne(".... Нет, сэр.//~73 01 3 ang// #(На самом деле мне немного не по себе)")
        $hero("Я же говорил...// Здесь нет ничего постыдного...")
        $daphne("~55 00 1 neu// ............// ....Думаю я смогу больше, сэр...")
        $hero(g9, "#(Разумеется....)")
        $daphne("~37 s0 2 ope// Э-э..... Сэр....")
        $hero(m, "Я вас понял Дафна....// Мне отвернуться?")
        $daphne("~37 01 1 neu// Я хотела сказать....// Эм....// ....Мне же все ровно нужно будет стоять на сцене.... перед этими.....// ................")
        $hero("....Вы имеете ввиду, когда на вас будут смотреть, мисс Гринграсс?")
        $daphne("~73 01 3 ang// .....Да, профессор.")
        $hero("#(А Снейп был прав....)")
        $hero(g9, "#(Мне стоило с ней повозиться...)")
        $hero(m, "Да, вы правы Дафна....// Ну хорошо....// Я смотрю....// Можете приступать....")
        $daphne("~37 00 2 neu")
        "> Ваши слова пошли на пользу Дафне...."
        "> Она хоть и смущенно, но снимает с себя юбку."

        $screens.Show(Dissolve(1), "blkfade") #Черный экран
        $daphne.ItemsCustomize(delete={"skirt"}) #delete - снять (одетую) вешь. update - одеть вещь.
        pause.5
        $screens.Hide(Dissolve(1), "blkfade") 
        $screens.Show("ctc").Pause().Hide("ctc")

        $daphne("~73 01 2 smi// Вот.... сэр....")
        menu:
            "\"Ваше белье бесподобно мисс Гринграсс\"":
                $daphne("~55 00 1 neu// Спасибо, сэр...")
                $hero("Хм....// «Спасибо... сэр...»// Что-то это мне напоминает....// Ах да....")
                stop music
                $screens.Show(Dissolve(1), "blkfade") #По хорошему здесь должен быть whitefade, но игру выкидывает, когда я его ставлю. Хз почему.
                pause 1.5
                "Мне нравятся ваши трусики Гермиона..."
                "Спасибо, профессор..."
                $hero("..................")
                $hero("#(Хм....)")
                $hero(g9, "#(Интересно... что сейчас делает Гермиона)")
                $daphne("~55 02 2 ehh// #.....Сэр?!")
                $hero(m, "......?!")
                $screens.Hide(Dissolve(1), "blkfade")
                $daphne("~37 00 2 neu// ...Сэр, вы меня слышите?// ....Я что-то сделала не так?!")
                $hero("Оу... Я извеняюсь...// Кажется я немного призадумался....")
                play music "music/Bittersweet Symphony (Instrumental).mp3"
                $hero("#(Ах да, белье....)")
            "\"Ну, а теперь снимайте остальное мисс Гринграсс\"":
                $daphne("~77 w0 2 wo// {size=+7}ЧТО!?{/size}// Ну, знаете....// Это переходит все границы...")
                $daphne("~55 01 2 dis//")

                $screens.Show(Dissolve(1), "blkfade")
                $daphne.ItemsCustomize(delete={"bra"}, update={"combi:cheer_topbase_withnipples"})
                $daphne.ItemsCustomize(update={"skirt:cheer_long"})
                pause.5
                $screens.Hide(Dissolve(1), "blkfade") 
                $screens.Show("ctc").Pause().Hide("ctc")

                $wtevent.Finalize("daphne_goout")
                $hero(g4, "Кажется я перегнул....")
                $daphne.liking -= 20
                $wtevent.Finalize ("night_start")

        $hero(m, "Отлично мисс Гринграсс...// Видите... все это может только казаться сложным.")
        $daphne("....Да?!//~73 01 1 smi// .....Наверное вы правы, профессор.")
        $hero(m, "#(Хм....)// #(Сиськи и в прямь маловаты....)")
        $hero(g9, "#(....Что-бы с ними сделать?!)")
        a6 "Ты задолбал..."
        a7 "Мне напомнить из-за чего ты тут застрял?"
        $hero(m, "#(.....Точно)// #(Похоже что ты прав....)// #(И так сойдет....)")
        a6 "Если бы не твоя самодеятельность, ничего этого небыло бы."
        $daphne("~55 s0 1 pou// Эм....// ....Профессор, вы меня слышите?")
        $hero("Гхм..... Простите... я не на долго задумался.// ....Вы что-то сказали?")
        $daphne("~73 02 3 ang// Я говорю, мне долго еще так стоять?")

        menu:
            "- Отпустить её -":
                $hero("Можете одеваться мисс Гринграсс....")
                $daphne("~73 01 1 smi// Хорошо, сэр...")

                $screens.Show(Dissolve(1), "blkfade")
                $daphne.ItemsCustomize(delete={"bra"}, update={"combi:cheer_topbase_withnipples"})
                $daphne.ItemsCustomize(update={"skirt:cheer_long"})
                pause.5
                $screens.Hide(Dissolve(1), "blkfade") 
                $screens.Show("ctc").Pause().Hide("ctc")

                $daphne.liking += 3
                $hero("Не спешите мисс Гринграсс...// Вы сегодня хорошо постарались, и заслуживаете поощрение....")
            "- Она может больше -": #Немного разглядываем, Дафна стесняется, и мы её отпускаем(нужны чибики в нижнем белье). Они есть?
                $hero("Подойдите ко мне Дафна....// Я хочу на вас посмотреть по ближе...")
                $daphne("~37 00 2 neu// Эм... Ну если так нужно, сэр...")
                pause 1.0
                dev "К большому сожалению, данная сюжетная линия пока дописана только до этого момента..."
                dev "{size=-3}(Но, вам остаются доступны другие сюжетные линии){/size}"
                dev "Оставьте ваши вопросы, благодарности и пожелания на нашем {a=http://wtrus.ixbb.ru/viewtopic.php?id=9}ФОРУМЕ{/a}."
                dev "Так вы простимулируете нас, и продолжение появится быстрее. :)"
            
                $screens.Show(Dissolve(1), "blkfade")
                $daphne.ItemsCustomize(delete={"bra"}, update={"combi:cheer_topbase_withnipples"})
                $daphne.ItemsCustomize(update={"skirt:cheer_long"})
                pause.5
                $screens.Hide(Dissolve(1), "blkfade") 
                $screens.Show("ctc").Pause().Hide("ctc")
            
                $hero("Не спешите мисс Гринграсс...// Вы сегодня хорошо постарались, и заслуживаете поощрение....")
        $daphne.whoring += 2
    elif IsRunNumber(6):
        pause 1.0
        dev "К большому сожалению, данная сюжетная линия пока дописана только до этого момента..."
        dev "{size=-3}(Но, вам остаются доступны другие сюжетные линии){/size}"
        dev "Оставьте ваши вопросы, благодарности и пожелания на нашем {a=http://wtrus.ixbb.ru/viewtopic.php?id=9}ФОРУМЕ{/a}."
        dev "Так вы простимулируете нас, и продолжение появится быстрее. :)"
        call daphne_main_menu_requests

    return
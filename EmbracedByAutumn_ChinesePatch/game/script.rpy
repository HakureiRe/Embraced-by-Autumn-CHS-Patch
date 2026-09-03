# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image ctc_animation = Animation("gui/ctc/ctc.png", 0.6, "gui/ctc/ctc2.png", 0.08, "gui/ctc/ctc3.png", 0.08, "gui/ctc/ctc4.png", 0.08, "gui/ctc/ctc5.png", 0.08, "gui/ctc/ctc6.png", 0.08, "gui/ctc/ctc7.png", 0.08, "gui/ctc/ctc8.png", 0.08, "gui/ctc/ctc9.png", 0.08, "gui/ctc/ctc10.png", 0.08, "gui/ctc/ctc11.png", 0.08, "gui/ctc/ctc12.png", 0.08, "gui/ctc/ctc13.png", 0.08,"gui/ctc/ctc14.png", 0.6, "gui/ctc/ctc13.png", 0.08, "gui/ctc/ctc12.png", 0.08, "gui/ctc/ctc11.png", 0.08,  "gui/ctc/ctc10.png", 0.08, "gui/ctc/ctc9.png", 0.08, "gui/ctc/ctc8.png", 0.08, "gui/ctc/ctc7.png", 0.08, "gui/ctc/ctc6.png", 0.08, "gui/ctc/ctc5.png", 0.08, "gui/ctc/ctc4.png", 0.08, "gui/ctc/ctc3.png", 0.08, "gui/ctc/ctc2.png", 0.08, xpos=0.925, ypos=0.92, xanchor=1.0, yanchor=1.0)

image ctc_animation_nvl = Animation("gui/ctc/ctc.png", 0.6, "gui/ctc/ctc2.png", 0.08, "gui/ctc/ctc3.png", 0.08, "gui/ctc/ctc4.png", 0.08, "gui/ctc/ctc5.png", 0.08, "gui/ctc/ctc6.png", 0.08, "gui/ctc/ctc7.png", 0.08, "gui/ctc/ctc8.png", 0.08, "gui/ctc/ctc9.png", 0.08, "gui/ctc/ctc10.png", 0.08, "gui/ctc/ctc11.png", 0.08, "gui/ctc/ctc12.png", 0.08, "gui/ctc/ctc13.png", 0.08,"gui/ctc/ctc14.png", 0.6, "gui/ctc/ctc13.png", 0.08, "gui/ctc/ctc12.png", 0.08, "gui/ctc/ctc11.png", 0.08,  "gui/ctc/ctc10.png", 0.08, "gui/ctc/ctc9.png", 0.08, "gui/ctc/ctc8.png", 0.08, "gui/ctc/ctc7.png", 0.08, "gui/ctc/ctc6.png", 0.08, "gui/ctc/ctc5.png", 0.08, "gui/ctc/ctc4.png", 0.08, "gui/ctc/ctc3.png", 0.08, "gui/ctc/ctc2.png", 0.08, xpos=0.925, ypos=0.90, xanchor=1.0, yanchor=1.0)


# MC
define Marcel = Character("马塞尔", image="marcel", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")

# LIs
define Claudine = Character("克洛蒂娜", image="claudie", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Luce = Character("露丝", image="lu", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Mirabel = Character("米拉贝尔", image="mira", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Celine = Character("塞琳", image="cel", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")

# Side characters
define Al = Character("阿尔贝汀姨妈", image="al", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Bru = Character("布吕吉埃夫人", image="al", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Marie = Character("玛丽-诺埃尔", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Thérèse = Character("特蕾莎", image="thérèse", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Noémie = Character("诺艾米", image="no", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Dubois = Character("杜布瓦夫人", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Fel = Character("费利克斯", image="fel", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")


# Sub characters
define Mum = Character("母亲", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Du = Character("杜普莱西先生", image="MDu", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Laroche = Character("拉罗什先生", image="CDad", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Amelie = Character("阿梅莉", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Va = Character("瓦雷纳先生", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Dad = Character("父亲", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Man = Character("壮汉", image="MDu", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Headmaster = Character("校长", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")

# Extras
define Cla = Character("同学甲", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Claa = Character("同学乙", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Claaa = Character("同学丙", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Claaaa = Character("同学丁", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Claaaaa = Character("同学戊", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define W = Character("？？？", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Class = Character("全班", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Cook = Character("厨师", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Girl = Character("安静的女孩", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Priest = Character("神父", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Girll = Character("打扮花哨的女孩", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Girlll = Character("害羞的女孩", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Girllll = Character("优雅的女孩", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define GirlR = Character("黑发女孩", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define GirlT = Character("高个子女孩", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define Te = Character("金发女教师", what_prefix="“", what_suffix="”", window_background="gui/textbox_speak.png", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")

define narrator = Character(None, ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed")
define nv = Character(None, kind=nvl, ctc="ctc_animation_nvl", ctc_pause="ctc_animation_nvl", ctc_position="fixed")
define gui.nvl_spacing = 20

init python:
    class Wiggle(object):
        def __init__(self, freq, amp, octaves=1, ampMulti=.5, time=0):
            from random import random
            self.randoms = [(1+random(), 1+random()) for i in range(0, 100)]
            self.freq = freq
            self.amp = amp
            self.octaves = octaves
            self.ampMulti = ampMulti
            self.time = time

        def __call__(self, time, at):
            from math import sin, pi, ceil
            r1, r2 = self.randoms[int(ceil(time*self.freq)%100)]

            return r1*self.amp*sin(2*pi*self.freq*time) + r2*self.amp*self.ampMulti*sin(2*pi*self.freq*2*self.octaves*(time+self.time))


label example:
    $ all_moves(x_express=Wiggle(freq=.5, amp=10), y_express=Wiggle(freq=.6, amp=10), z_express=Wiggle(freq=.4, amp=1))

init python:
    style.menu_choice_button.background = Frame("gui/choice.png",50,0)
    style.menu_choice_button.hover_background = Frame("gui/choice.png",50,0)
    style.menu_choice.font = "fonts/NotoSansSC-VF.ttf"
    style.menu_choice.size = 36
    style.menu_choice.idle_color = "#5c3e27"
    style.menu_choice.hover_color = "#a2846d"

    style.menu_choice.xalign = 0.5
    style.menu_choice.yalign = 0.5

    style.menu_choice_button.yminimum = 130
    style.menu_choice_button.xminimum = 1920

    style.nvl_window.background = "gui/nvl.png"
    style.nvl_window.left_padding = -140
    style.nvl_window.right_padding = 550



# The game starts here.

label start:

    window hide
    stop music fadeout 1.0
    stop ambience fadeout 1.0
    scene black
    with fade

    $ renpy.pause(0.5)

    scene cafe g
    with circleirisout
    $ renpy.pause(0.5)
    show overlay2
    show message1 at message
    show logo2
    with datetrans

    $ renpy.pause(4.0)

    hide message1
    hide logo2
    hide overlay2
    with datetrans2

    $ save_name = (__("{u}序章{/u}{vspace=1}  9月12日{vspace=1}  布景") )

    $ renpy.pause(1.0)

    play music "bgm/Energetic.ogg" fadein 1.0

    scene cafe
    show al smile at center
    with dissolve
    window show dissolve

    Al "亲爱的孩子，距离上次见到你已经过去太久了！我真是太高兴了，我们终于团聚了！"
    Marcel neutral b "啊，呃……早上好，阿尔贝汀姨妈。我很高兴——"
    "我开了口，却无法继续说下去。"

    scene cafe blur:
        size (1920, 1080) crop (250, 160, 960, 540)
    show al smile3 at center
    with hpunch

"以姨妈那副端庄刻板的外表而言，这举动实在出乎意料的冲动——她突然张开双臂，一把将我搂进怀里。"
"她身上有香水味，我说的可不是那种淡淡的味道。她{i}真的{/i}是香水味扑鼻，浓得化不开——是紫罗兰的香气。"
"我的鼻子发痒，眼睛发酸，还得强忍住想对着姨妈的连衣裙咳嗽个不停的冲动。"
Al "还有你，莱奥妮！"

scene cafe
show al smile:
    xpos 0.70 xanchor 0.5
show leonie neutral:
    xpos 0.30 xanchor 0.5
with wipeleft_slow

"当姨妈终于从我身上脱身，转向母亲时，我松了一口气。"
"姨妈没有拥抱她（也许她不想弄皱那件昂贵的上衣），但她还是在她两边脸颊上各亲了一口。"
Al "坐下，你们两个，坐下！这张桌我已经留好了。我一直在等呢！"
"母亲和我在指引下落了座；不过是这家雅致的巴黎咖啡馆里众多顾客中的两位。"

show image "border" onlayer border
scene cafe:
    subpixel True
    size (1920, 1080) crop (0, 180, 1280, 720)
    linear 20.0 crop (350, 180, 1280, 720)
with wiperight_slow

"我才十五岁，却在生命中光顾过不少巴黎的名流咖啡馆，那些地方是知识分子和文人雅士常聚之所。"
"那些都是陈设奢华、装点考究的场所，镶金的镜子和低垂的水晶吊灯到处皆是。"
"每当父亲想把我引荐给他那些显赫的“朋友”时，我就随他一起去那样的地方。"
"不过我想，我怕是再也不会去太多那样的地方了——至少不会和父亲一起去了。"
"我才十五岁，但我在巴黎的人生实际上已经结束了。"
"阿尔贝汀姨妈安排我们见面的那家咖啡馆，与我所熟悉的那些咖啡馆颇为相似，圆桌陈列其间，精致的吊灯高悬于天花板。"
"清晨时分尚早，因此只有寥寥几位客人落座于桌旁。"
"四周弥漫着浓重的咖啡豆香气，还有我姨妈的香水味。"
"我很高兴这里很安静。我向来不大喜欢人群，而近来更是对此尤为厌恶。"
"我不想让任何人看见我；也不想让任何人打量我。"
"我真希望自己能就此消失。"

hide image "border" onlayer border
scene cafe
show al neutral:
    xpos 0.70 xanchor 0.5
show leonie neutral:
    xpos 0.30 xanchor 0.5
with wipeleft_slow

Al "那么，马塞尔。"
show al smile2 with dissolve
"阿尔贝汀姨妈朝我露出鼓励的微笑，仿佛在经历了这一切之后我还有心情回以一笑似的，随即俯身越过桌面。"
Al "你近来过得怎么样？"
show leonie frown with dissolve
Mum "他过得怎么样？"
"母亲挑了挑她那修整精致的眉毛。"
Mum "你{i}觉得{/i}他会过得怎么样？"
show al sigh2 with dissolve
Al "是啊，这个嘛……"
"姨妈皱了皱眉，随即困惑地靠回椅背。"
show al frown with dissolve
Al "我也料想过，在这样的境况下，那可怜的孩子心情会相当低落……"
show al neutral with dissolve
Al "可我上一次见他，已经是好几年前了！我想知道他到底过得好不好！"
show leonie sigh with dissolve
Mum "他就那样，正如能预想的一般撑过来了，可我怀疑他现在没有闲谈的心情。你也没有，是吧，亲爱的？"
Marcel sad b "不是没有心情。我只是……不擅长这个。我不像我父亲。"
show leonie shock with dissolve
Mum "这也算件好事！"
Mum "我真不敢相信你父亲会这样对我们……"
show leonie angry with dissolve
"她的鼻翼张了张。心情不好的时候，她常常会这样。"
Mum "不，其实我{i}能{/i}相信你父亲做出这种事。我太容易相信了！他一向都这么没心没肺！"
Mum "他从来不肯帮我抚养你。他总在法国四处风流快活，却把我留下来收拾残局！"
Mum "以我当时的处境，我尽力了，可他却偏偏做出这种事来！"
Mum "他怎么{i}能{/i}这样？简直不可理喻！"
Mum "我忍受他那些浮华浪荡的做派，是冲着他的工作、他的钱，还有他的名声……"

stop music fadeout 2.0

Mum "而现在，我们连这些都没有了！他把圣雷米这个姓氏变成了天大的笑柄！"

scene sky with wipeup_slow
play music "bgm/Mysterious.ogg" fadein 1.0

"我的父亲，乔治·德·圣雷米，是亨利二世国王一位私生子的后裔。"
"据说我们的血管里流淌着王室的血脉，但在过去的两百年间早已被冲淡了。"
"尽管与王室沾亲带故，我的父亲却没有任何头衔。他既不是子爵，也不是公爵，只是一个寻常人。"
"父亲出生在一个并不富裕的家庭，但他凭借自己的聪明才智与本事，一步步攀上了顶峰。"
"他离开家前往巴黎，在那里（通过一些我并不十分清楚的手段）当上了演员。"
"父亲多次向我讲述他从出生地帕雷勒莫尼耶尔出走、前往巴黎的经历，可其中的细节却总在变化。"
"我也说不清哪些是真，哪些是假。"
"父亲总喜欢添油加醋，以至于真相与谎言已经无从分辨。"
"我想，他这种自我夸耀的癖好，多半源于他在剧院里度过的岁月。"
"父亲在巴黎各大剧院的舞台上演出。他今夜是罗密欧，明夜是浮士德博士，观众们都喜爱他。"
"母亲原本是那些为明星着迷的少女之一，十七岁那年看了父亲的演出。"
"她爱上了他，并在演出结束后固执地守候数小时，只盼着能在父亲离开剧院时望上他一眼……"
"终于，母亲引起了父亲的注意。父亲一向喜爱美好的事物——他自己也这么对我说过——而他觉得有着一头金发和一双小鹿般眼睛的母亲，尤其动人。"
"他把她带回自己的公寓，占有了她，九个月后我便出生了。"
"不过，父亲并非因为有了孩子才舍弃舞台的浮华与光彩。他从来都不是一个顾家的人。"
"相反，他比以往更起劲地投入到工作中，也正因如此，他把我的母亲抛在了脑后。"
"他倒还算好心，为我和母亲买下一套公寓居住，但尽管曾有过一些敷衍的承诺，他却始终没娶她。我觉得他并不怎么在意。"
"事实上，我想他或许早已后悔与母亲的那段情事。"
"母亲则定然为此后悔。她总说，和乔治·德·圣雷米纠缠在一起，是她一生中最大的错误……"
"然后她会看看我，眉头皱起，说：“可若是不曾遇见他，我也不会拥有你，马塞尔。”随即吻我——多半是出于愧疚。"
"即便母亲并非真的想要我，我想我也多半不会太在意。毕竟又不是我自己求着要出生的。"
"母亲在过去十五年里受尽了苦。她与父亲的那段关系人尽皆知（小报上登过许多关于此事的报道），这使得她寻觅真爱、拥有真爱的机会尽数葬送……"
"或者，即便算不上一份“真爱”，至少是某种形式的爱。"
"在大众心目中，她被视作我父亲的附属品。"
"不过，我的父亲并非铁石心肠。我知道他关心着我们，只是以他自己那套与众不同的方式。"
"我很少见到他，可他总会给我买昂贵的礼物，偶尔还会带我去听歌剧，去看戏，或是去精致的餐馆与咖啡馆……"
"不过，说实话，我对九岁生日时他送我一条雪纺连衣裙和配套的无边帽这件事至今仍有些耿耿于怀，因为他显然忘了自己有个儿子，而不是女儿。"
"母亲看到那条裙子时哼了一声，说父亲多半是打算把它送给他的另一个私生子，一定是在包裹上填错了地址。"
"就算父亲除我之外还有别的孩子，我也不会感到惊讶；但若真有，我也不知情。同样，我也并不想知道。"
"有哪个做儿子的、做女儿的，愿意知晓自己父母堕落的全部真相呢？"
"我本乐意对父亲那一次又一次、众多的风流韵事装聋作哑……"
"但他近来卷入的那桩丑闻却无法视而不见。各家报纸都在报道，我的同学们似乎也都知道了。"
"有时（其实往往如此），我真希望父亲不是个名人。这可真是得不偿失。"

scene cafe
show al neutral:
    xpos 0.70 xanchor 0.5
show leonie angry:
    xpos 0.30 xanchor 0.5
with wipedown_slow

Mum "他竟能这样对待我们，太过分了；简直过分至极！我真真切切地相信，他心里{i}只{/i}有他自己！"
"母亲眼中迸射出毫不掩饰的怒意。"
"她或许是个娇小的女人（她几乎比我还矮整整一个头），但她的脾气可万万招惹不得。"
Mum "他的同学早就因为他是私生子，在学校里就把他孤立起来了！他们把他的日子搅得像活受罪！"
Mum "他们嘲笑他有个当演员的父亲，还对他父亲那些见不得人的风流韵事冷嘲热讽！"
Mum "马塞尔天天忙着抵挡辱骂和讥讽，哪里还能专心念书？"
Mum "他才十五岁。他本该专心完成学业，而不是护着他那张漂亮的脸蛋，躲开黑板擦和网球拍！"
show leonie sad with dissolve
Mum "你知道吗，今年四月，有个坏透了的男孩在马塞尔上楼梯时推了他一把。"
Mum "马塞尔绊了一跤，摔倒了，把腿扭伤得厉害，整整三天都不能走路！"
Mum "幸好他什么也没摔断，可他身上那些淤青……"
"母亲倒吸一口气。她的声音因激动而颤抖。"
show leonie frown with dissolve
Mum "我当然向学校投诉过，可他们说那不过是孩子们打打闹闹——男孩子就是这样，诸如此类的鬼话！你能想象吗？"
show al sigh with dissolve
Al "唉，我太清楚了。少年有时候可怕得很；尤其是那些半大的男孩。"
show al neutral with dissolve
Al "所以我才刻意只教女孩。她们更好塑造——虽说那位‘娇弱’的性别，有时也野得很呢！"
show leonie neutral with dissolve
Mum "说到这个，你的工作{i}到底{/i}怎么样了？我差点忘了问。希望你的姑娘们没给你添太多麻烦。"
show al smile with dissolve
Al "她们还是跟往常一样闹腾，不过我没什么可抱怨的。"
Al "我的姑娘们确实会惹些乱子，上帝保佑她们，可她们骨子里都挺温柔可爱的……"
Al "至少，我很愿意这样相信！"
Al "好在，在米延想惹麻烦也不容易。那里实在没什么可闹腾的——除了绵羊和奶牛之外！"
show al neutral with dissolve
Al "话虽如此，我还是尽量把姑娘们管得严些。我希望她们长大，都成为端庄体面的年轻淑女！"
show leonie sigh with dissolve
Mum "而不是像我这样不知检点的女人？"
show al shock with dissolve
Al "哦，不，莱奥妮，我不是那个意思——"
show leonie sad with dissolve
Mum "我明白你的意思……{w}而且你说得对。"
Mum "我们两姐妹里，你一向是那个理智的人，阿尔贝汀。你上了师范学校，如今是一所声誉良好的学院的女校长。"
Mum "而我呢，这辈子一天工都没做过。我靠乔治的钱过活，独自一人照料马塞尔。"
Mum "我还算什么女人哪。"
show al neutral with dissolve
Al "你不该这样苛责自己，莱奥妮。你当时又怎么会知道……"
Mum "我刚一开始追求乔治的时候，你就警告过我。父亲和母亲也警告过我。"
Mum "你们都说他是个不成器的浪荡子——说他一定会伤透我的心——可我没听。我以为自己比你们都明白。"
show al sigh with dissolve
Al "年轻人总以为自己比谁都明白。"
Al "我劝过你打消念头，可我知道，你从不会听你这个无趣的大姐的话。你向来都有股倔脾气！"
show leonie neutral with dissolve
Mum "你不因此怨我？"
Al "当时确实怨过，但现在不怨了。你犯了个错，而从那以后，你一直在为此付出代价。"
show leonie smile with dissolve
"母亲干笑了一声。"
Mum "至少乔治给我买了那套公寓，而且他现在还寄钱过来。这已经比你们所有人原先料想的都要好了。"
show al annoyed with dissolve
Al "我承认，我当时最担心的是他让你大着肚子走人，身上却连一个子儿都不剩。"
Al "我想，他没有彻底断了你的生计，总算还算是厚道。"
show leonie sad with dissolve
Mum "我知道。这才是最糟的地方。乔治并不是那么坏的人。真的不是。他粗心，他自私，他把自己的享乐看得比什么都重，可他{i}确实{/i}帮过我——用他自己的方式——而且他也确实对马塞尔流露过几分关心。"
Mum "可现在，我却忍不住希望他当初干脆别费这个心了。"
show al neutral with dissolve
Al "你是被他牵连，沾了污名。"
Mum "说得对。我本该在他拒绝娶我的那一刻，就跟他断了关系，可那时我能去哪儿？我靠什么养活自己？"
show al shock with dissolve
Al "你本可以回家来的，莱奥妮。我们会张开双臂接纳你！"
show leonie frown with dissolve
Mum "你们真的会吗？"
show al neutral with dissolve
Al "这个嘛，父亲始终没能从你和乔治那件事的打击中完全缓过来……"
"母亲哼了一声。"
Al "……可是母亲很想你。她想看看你现在过得好不好。"
show al annoyed with dissolve
Al "你好多年没见过她了，莱奥妮。她很担心你——现在这桩丑闻传开了，她会更加担心。"
show leonie sad with dissolve
Mum "我知道我该回去——我早就该回去了——可是……"
"母亲的脑袋颓然垂下，活像一个坏掉的木偶。"
Mum "我不知道自己能否面对这样的耻辱。"
Mum "我怀疑父亲永远不会接纳我，也不会接纳马塞尔。你知道他是什么脾气的。"
show leonie sigh with dissolve
Mum "就算他肯让我踏进家门——这本身就是一个天大的假设——我知道他会对我啧啧摇头，叹息，说些刻薄话……"
Mum "我不想应付那些，也不希望马塞尔去应付。"
show leonie shock with dissolve
Mum "我不想让我唯一的儿子被自己的亲祖父嫌弃！"
show al neutral with dissolve
Al "听起来，把父亲的感受先放一边，他也已经承受了太多。"
Al "我猜他在学校里过得不怎么好吧？"
show leonie frown with dissolve
Mum "天哪，那所糟糕透顶的学校……"
Mum "我想尽我所能给马塞尔最好的机会，可我恐怕做得一塌糊涂。单靠我自己，我给不了他应得的生活。"
show leonie sad with dissolve
Mum "这个世界对我的马塞尔这样的孩子并不仁慈。人人都苛刻得要命！"
Marcel neutral b "母亲……"
"我把手覆在她的手上。"
Marcel smile b "我觉得您把我抚养得很好。"
show al smile with dissolve
Al "他确实举止无可挑剔！比我校里的有些姑娘还要温和呢！"
show leonie neutral with dissolve
Mum "您真的这么觉得吗？"
Al "确实。那群丫头可真够呛！简直是一群小亚马逊！"
Mum "听了这话我很高兴。我对马塞尔真的尽力了，可恐怕还是不够。"
Marcel neutral b "您从来都给了我我想要的一切，母亲。"
show leonie sad with dissolve
Mum "可我却没能给你一个父亲……"
Marcel smile b "那正好，我本也不太想要一个父亲。"
"那当然是句谎言。我{i}确实{/i}想要一个父亲，但未必是{i}我自己的{/i}父亲。"
"我只想要一个肩膀宽厚、体面、略带乏味的男人，能让我唤作“爸爸”，好让学校里的老师们不再用怜悯或厌恶（时而如此）的眼神看我，也让同学们不再把我当成麻风病人那样避之不及。"
"然而事到如今，很少有人愿意接纳我和我这可疑的血统——就连我从未谋面的祖父也不例外。"
show leonie neutral with dissolve
Mum "哦，马塞尔……"
"我想母亲定是看穿了我的谎话，因为她哼了一声。"
Mum "你真是个好孩子。你承受了太多太多……"
show leonie frown with dissolve
Mum "而现在，因为那个男人——"
"母亲常把父亲称作“那个人”，尤其是在她心情不佳的时候。有时她说，她连听到他的名字都受不了。她说那名字可憎。"
Mum "——你还要承受更多。"
show leonie angry with dissolve
Mum "他毁了你，就像他毁了我一样！他把我们全家都毁了！"
"母亲的话或许听来有些夸张，却也并非全无道理。"
"两周前，《吉尔·布拉斯》上刊登了一篇有关父亲种种癖好的罪证性报道。自那以后，这便成了人们热议的话题。"
"毕竟，父亲作为一名演员相当有名；他一度深受爱戴，如今却因酒后与人争执、向他人之妻献殷勤而声名狼藉。"
"倘若他的放荡只停留在简单、容易理解的层面上，公众的哗然或许还不至于如此强烈，可是……"
show leonie sad with dissolve
Mum "我就是不明白{i}为什么{/i}。如果他非做不可，为什么不能守口如瓶？"
Mum "又或者……"
"母亲的脸色变得苍白。"
Mum "也许他一直都在守这个秘密。也许他一直以来都在做{i}那种事{/i}——甚至在我认识他之前——而我从来都不知道。"
"母亲呻吟着，一只手捂住嘴。"
Mum "我不知道哪种更糟。我不知道该作何感受。"
show leonie shock with dissolve
Mum "哦，我一定像个十足的傻瓜……！"
show al neutral with dissolve
Al "好啦，好啦，莱奥妮……"
"阿尔贝汀姨妈试图安慰母亲，可她的话语却无法驱散母亲的绝望。"
show leonie sad with dissolve
Mum "竟然跟别的男人有私情……"
show leonie shock with dissolve
Mum "不，不是男人——是个{i}男孩！{/i}他还是个孩子，比我们亲爱的马塞尔大不了多少！"
show leonie angry with dissolve
Mum "他怎么能做出那种事？他{i}怎么{/i}能？"
"母亲那激动的声音愈发高亢，直到引来了坐在最近一桌客人们的注意。"
"他们在椅子上转过身来，扭头打量着母亲，嘴巴大张，活像市场上摆着的死鱼。"
show leonie sad with dissolve
"母亲察觉他们在看，脸颊泛起红晕。她像个孩子似的咬着嘴唇，低下了头，眼眶湿润。"
"自从读了《吉尔·布拉斯》上的那篇文章，这两个星期以来她哭了很多次。"
"她哭的时候，我替她把头发拢到耳后，竭尽全力安慰她，可那反倒让她哭得更厉害了。"
"“你不该这样照顾我的，马塞尔。”她噙着泪对我说。“我是你母亲。照顾你是我分内的事……！”"
"不过，我觉得母亲眼下的状态连照顾谁都做不到——甚至连她自己也不行。"
show leonie neutral with dissolve
Mum "我想乔治干这种事已经很久了。一定是的。那些迹象一直都在。"
Mum "很久以来就有些传闻，说他跟那些年轻演员有些过于亲近，可他都辟谣了。他说那不过是诽谤。"
Mum "好吧，现在我知道了真相——至少是部分真相。"
show leonie sad with dissolve
Mum "这让我怀疑，他到底是否真心爱过我，还是说，他只是任由我主动示好，好挡住那些流言蜚语。"
Mum "好吧，如今一切都败露了，人人都知道了真相。他们知道他利用了我，而我们已经身败名裂。"
show leonie shock with dissolve
Mum "马塞尔如今绝不能再回学校了。他的同学们要是再见着他，会把他撕了的；我敢肯定！"
show leonie sad with dissolve
Mum "我真不知道我们还能怎么再在公共场合露面……"
show al sad with dissolve
Al "哦，莱奥妮……"
"姨妈的脸上因忧虑而柔和下来。她摇了摇头；只是一个对我们的遭遇除了同情之外别无他法的旁观者。"
Al "过了这么多年，你来找我，就是为了这个吗？"
show leonie neutral with dissolve
Mum "没错。我想不出还能向谁求助。"
show leonie shock with dissolve
Mum "我知道上次见你已经是很久以前的事了，可我已经走投无路了！"
Mum "我不知道自己要怎么办，也不知道该拿马塞尔怎么办。他需要完成学业，可他不能在这里完成。这不可能。"
show leonie neutral with dissolve
Mum "我想，要是卖掉那套公寓，我们或许可以搬走，可谁知道消息有没有已经传开呢？"
show al neutral with dissolve
Al "我在米延讷也听说了那桩丑闻。那里的地方报纸也登了。"
Al "莱奥妮，我一看到那消息，就特别为你担心。我不知道之后会发生什么……"
show leonie shock with dissolve
Mum "我自己也不知道！"
Mum "哦，天哪。恐怕全法国都知道这件事了，从阿尔萨斯到阿基坦！"
show leonie sad with dissolve
Mum "要是乔治从前没那么英俊、没那么成功、没那么雄心勃勃就好了。"
Mum "要是他从没变得像今天这么出名，这一切都不会发生！"
"母亲的下唇微微颤抖。她用颤抖的手指，把一缕发丝拢到耳垂后面。"
Mum "我希望自己当初没有爱上那个混账男人。要是我的名字没跟他绑在一起，那么……"
"母亲的声音渐渐低了下去，她叹了口气，摇了摇头。"
show leonie sigh with dissolve
Mum "不。那也解决不了任何问题。"
Mum "要是从没遇见那个男人，我就不会有我的马塞尔了，而他是发生在我身上最好的事。"
show leonie neutral with dissolve
Mum "他是那个男人给我的唯一真正的礼物，我不希望他受苦。"
show leonie shock with dissolve
Mum "我希望他能像法国任何一个男孩那样，有快乐的校园生活，也有光明的前途！可我不知道，背着这桩丑闻，还有没有可能！"
Al "所以，你要见我，是因为担心马塞尔？"
show leonie neutral with dissolve
Mum "没错。阿尔贝汀，我知道这么多年我们往来极少，这时候开口求你帮忙，或许显得唐突……"
show al smile with dissolve
Al "胡说，莱奥妮！不管马塞尔那个浪荡父亲做了什么，你都是我的妹妹，我爱你。这一点从未改变，也永远不会改变。"
Al "只要能看见你们母子俩笑，我什么都愿意为你们做。"
show leonie smile with dissolve
Mum "这些天来我确实没怎么笑，那是肯定的……"
"不过，尽管说了这番话，母亲的唇角仍旧微微上挑——尽管那笑意十分微弱。"
"我不禁想，那是不是因为阿尔贝汀姨妈在旁的缘故。"
"一张友善的面孔往往能起很大的作用，尤其是在你觉得整个世界都与你为敌的时候。"
show leonie neutral with dissolve
Mum "我刚刚在想……我没有钱送马塞尔出国，我猜你也没有，但身为校长，你总该有些门路吧。"
Mum "你能不能帮马塞尔在别的学校弄到一个名额——也许是在乡下的学校？"
Mum "也许他能在那里，远离巴黎，相对平静地完成学业。"
show al neutral with dissolve
Al "我可以试试，但米延讷是个小村庄。我的学校是附近唯一一所这样的机构，而且只收年轻姑娘。"
Al "我可以看看能不能让马塞尔进讷韦尔的一所男校，可没人保证他们肯收他……"
show al sigh with dissolve
Al "而且巴黎之外的男孩子，跟巴黎城里的同样残忍。"
show leonie frown with dissolve
Mum "你当然说得对。不管马塞尔去哪里，这桩事都会如影随形地跟着他。"
"母亲皱起眉头。她用指尖轻轻敲击着桌面。"
Mum "就没有一点办法了吗？我只想让我儿子快乐！"

stop music fadeout 2.0

show al neutral with dissolve
Al "嗯……"
"阿尔贝汀姨妈坐得稍微直了些。她那绿色的眼睛直视着母亲那蓝色的眸子。"
"我从父亲那里继承了个子，而其余的相貌——蓝眼睛与金发——则来自母亲。"
"对于一个男孩而言，我生得格外秀气，这也成了同学们乐于取笑我的又一个把柄。说真的，在折磨我这件事上，他们从来不缺素材。"

play music "bgm/Friendship.ogg" fadein 1.0

Al "我倒是有一个可能的办法，不过……"
show leonie neutral with dissolve
Mum "你有办法？！"
"母亲坐直了身子，手指在桌面上蜷曲着。"
Mum "是什么办法？！"
show al frown with dissolve
Al "这是个非常之举，而且伴随着相当多的风险。我不确定你是否会赞成。"
show leonie angry with dissolve
Mum "我当然会赞成！只要是为了我儿子，我怎么会不赞成？！"
show al neutral with dissolve
Al "你确定吗，莱奥妮？你愿意为了马塞尔走到任何一步吗？"
show leonie shock with dissolve
Mum "为了我儿子，没有什么手段是过分的！"
Al "那好。既然如此……{w} 你何不让马塞尔在我学校注册入学呢？"
Al "也许它不像巴黎的学校那么气派，也没有那么多经费，可那里的姑娘们很快乐，我们的老师也称职。"
Al "乡村的空气或许会对他有些好处……"
show al neutral with dissolve
Al "而且，虽然他得离开你，可他仍会住在亲人附近。作为他的姨妈，我会照顾他，还会写信告诉你他的近况。"
show leonie neutral with dissolve
Mum "你的学校？可我以为你只收女生？"
Al "是的，正是如此。"
show leonie frown with dissolve
Mum "那马塞尔怎么可能在那种地方入学？他会比以前更加扎眼！"
Al "嗯，问题就在这里……"
show al smile with dissolve
Al "严格来说，{i}马塞尔{/i}并不会在我学校注册入学。"
Marcel shock b "啊……"
"我想我能猜到事情会朝哪个方向发展，可姨妈的计划实在太过疯狂，我简直不敢相信。"
"话说回来，近来我身上已经发生了许多离奇之事。这不过是沧海一粟罢了。"
Al "我不是要冒犯你，马塞尔，但我认为你会很适合我学校。你只需要把头发编成辫子、穿上我们的校服就够了。"
Al "那样的话，我不明白有谁会把你跟我们任何一个学生分辨出来。你会完全融入其中！"
show leonie shock with dissolve
Mum "什么……？"
"母亲倒吸一口凉气。"
show leonie frown with dissolve
Mum "你不会是说——"
show al neutral with dissolve
Al "但我正是这个意思，莱奥妮。这是我能想到的唯一办法。"
Al "在一年时间里，马塞尔将在我学校、在我的照看下学习。他会打扮成我的一名女学生，举止也像我的一名女学生，没有人会发觉真相。"
Al "等到一年过去、他完成学业，围绕乔治的所有肮脏事应当都已经烟消云散。那时候，他就能在巴黎重拾旧日的生活。"
Al "不过，在那之前，我愿意照顾他。"
show al smile with dissolve
Al "我知道这听起来像个古怪的念头，但这是我能想到的最好的办法。相信我，莱奥妮，我也希望你的儿子好。"
Al "我会竭尽所能保护他。"
Al "那么，对这件事你怎么看？"

stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene train g:
    size (1920, 1080) crop (240, 40, 1440, 810)
with clockwipe
$ renpy.pause(0.5)
show overlay2
show message2 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message2
hide logo2
hide overlay2
with datetrans2

$ save_name = (__("{u}序章{/u}{vspace=1}  9月15日{vspace=1}  前往米耶讷") )

$ renpy.pause(0.5)

play ambience "sfx/train.ogg" fadein 1.0
play music "bgm/Casual_Day.ogg" fadein 1.0
scene train:
    size (1920, 1080) crop (240, 40, 1440, 810)
$ all_moves(x_express=Wiggle(freq=.5, amp=10), y_express=Wiggle(freq=.12, amp=15), z_express=Wiggle(freq=.4, amp=1))
with dissolve
window show dissolve

"我坐在火车上，茫然失神地凝望着窗外。"
"铁轨想必老旧且不平整，因为火车的车轮在冰冷坚硬的钢轨上发出刺耳的声响。"
"我的后脑勺撞到了座椅上。我不小心咬到了舌头，疼得直皱眉。"
show al sad2 at center with dissolve
Al "哎呀。"
"阿尔贝汀姨妈朝我投来同情的目光。"
Al "你没伤着自己吧？"
Marcel embarrassed c "没、呃……我没事……"
show al neutral2 with dissolve
Al "你确定吗？"
"我自然并不十分确定，可我无法对姨妈这样说。我不愿让她忧心。"
Marcel sigh c "我……唔，我尽可能地确定吧。"
show al sigh2 with dissolve
Al "可怜的孩子。这你一定很难受吧。"
Marcel ehe c "我能撑过去的。"
"我朝姨妈露出一个自以为能让她安心的微笑，可我怀疑那并不怎么管用。在这样的境况下，我实在没有心情笑。"

stop ambience fadeout 2.0
scene sky with wipeup_slow

"我这一生都在巴黎度过。我从未去过乡下——一辈子也没去过一次——而如今，突然间，我就要被从旧日世界推入一个全新的天地。"
"我几乎来不及与母亲道别，就被阿尔贝汀姨妈带着，乘一辆马车火速送往火车站。"
"坐火车对我来说是头一遭。外头比我预想的更嘈杂，人也比我预想的多，尽管他们都各自隔绝在自己的小隔间里。"
"我与阿尔贝汀姨妈独享一个隔间，可我仍能隐隐听到远处一个孩子尖利的哭喊声，夹杂着那位母亲拼命想要让她安静下来的声音。"
"火车沿着铁轨轰隆前行，像一个上了发条的玩具。每过去一秒，它便把我带离巴黎，带离我的母亲，带离我曾熟悉的一切。"
"我谈不上多么眷恋过去的生活，但至少那是我所熟悉的。"
"在学校里，我时常被同学们取笑戏弄，但我知道会这样，也已练就了躲进图书馆、不让人找到我的本事。"
"至少我曾这样认为，可尽管我竭尽所能，我还是被人从楼梯上推了下去。"
"也许我离开这里反倒是最好的。"
"倘若我在一群女孩当中求学，我应当就不必担心遭到欺负了；至少不会遭到身体上的欺负。"
"人们都说女孩是更娇弱的性别，而我大概会比她们全都高出许多。"
"我只希望自己不会太显眼。"
"我已经觉得自己显眼得可怕，穿着阿尔贝汀姨妈在一家小店里给我买的花裙，头发扎成两条辫子。"
"阿尔贝汀姨妈认为，既然我打算以女孩的身份生活，就该尽早试着习惯这一切。"
"我想她说的没错，可微风掠过双腿的感觉实在奇怪，一点也不自然。"
"在巴黎那座大车站，在喷吐着蒸汽的火车环绕下与母亲道别，本身已够令人黯然，更何况我还穿着一条裙子。"
"这并不是我愿意选择与母亲道别的方式，可如今，我的选择似乎已经不那么重要了。"
"我略略挪动身子，感到不自在，随手捻弄着裙摆。"

play ambience "sfx/train.ogg" fadein 2.0
scene train:
    size (1920, 1080) crop (240, 40, 1440, 810)
show al frown2 at center
$ all_moves(x_express=Wiggle(freq=.5, amp=10), y_express=Wiggle(freq=.12, amp=15), z_express=Wiggle(freq=.4, amp=1))
with wipedown_slow

Al "别坐立不安，马塞尔。"
"阿尔贝汀姨妈把手覆在我的手上，迫使它安分下来。"
"她的手指修长，指甲修剪得整整齐齐，干干净净，未施粉饰。那是一双十分能干的双手，一位女校长的双手。"
Al "坐立不安可不太像淑女。你表现得好像连自己这身皮囊都待不自在似的！"
Marcel sad c "可我不太确定这{i}究竟{/i}是不是我自己的皮囊。"
"我满腹狐疑地打量着那条花裙。它看起来并不像我的东西，尽管我能看见自己的膝盖在布料下隆起成一座座小岛。"
"当我挪动右腿、微微屈起膝盖时，我惊愕地看到裙子的布料也随之移动。"
"我那整洁的黑鞋上的黄铜鞋扣在阳光下闪闪发亮。"
"我对着它们皱了皱眉。"
"这双鞋不是我的。长袜不是，裙子也不是。"
"这一切没有一样是属于我的。没有一样能代表曾经的我……"
"但我想，这便是我如今的样子了。"
"我不再是马塞尔，不再是乔治·德·圣雷米和莱奥妮·布吕吉埃的儿子。我完全是另一个人了。"
"我真希望知道那人究竟是谁。"
show al neutral2 with dissolve
Al "我知道穿连衣裙和衬衣现在对你来说一定很奇怪，但你很快会习惯的！"
Marcel sigh c "我不知道自己是否想习惯这些……"
show al annoyed2 with dissolve
Al "你该庆幸自己不用穿束身衣！那玩意儿对脊背和肋骨可糟透了！勒得人腰部难受得要命。"
Al "我不让我的姑娘们穿那种衣服。她们还太小，而且那对她们也没好处。"
Al "依我看，乡下的姑娘应该穿得自然一些。"
Marcel neutral c "我不知道现在的我还有哪里自然可言。"
show al neutral2 with dissolve
Al "哦，马塞尔……"
"姨妈的眼神柔和了下来。"
show al sad2 with dissolve
Al "你在担心，对吧？我从你脸上看得出来。"
Marcel sigh c "我肯定没事的……"
"我嘴上虽这么说，心里却并不怎么信。阿尔贝汀姨妈也一样。我从来就不太擅长撒谎。"
"那么，我又怎么能让整所寄宿学校的女孩们都相信，我跟她们一模一样呢？"
"我会显得滑稽可笑，活像一只想混进天鹅群里的鸭子。就算我的个头不露馅儿，我的嗓音也会，抑或是我说话的样子也会。"
Marcel sad c "我尽量不去多想。"
"然而在这间火车包厢里，我如今也别无他法。"
Marcel neutral c "我知道您和我母亲做这些都是为了我好，我很感激。真的。"
Marcel "我母亲才是这辈子真正受苦的人。跟她吃的苦相比，这根本不算什么。"
show al neutral2 with dissolve
Al "嗯，你说得没错。自打你母亲碰上你那个不成器的父亲，她可没少吃苦头。"
show al smile2 with dissolve
Al "但愿在她那副容貌之外，你也承袭了她几分不服输的骨气！"
Marcel embarrassed c "我也希望如此。只是我不晓得自己能不能习惯这一切。"
"我又去拨弄裙摆，阿尔贝汀姨妈轻轻拍开我的手指。"
show al neutral2 with dissolve
Al "若你想和我的姑娘们打成一片，那你最好能习惯。"
Marcel sigh c "唉，我也从未真正和哪个男孩子合得来。我不晓得自己究竟能融入哪里。"
show al frown2 with dissolve
Al "抱着这种心态，你自然是融不进去的。"
show al neutral2 with dissolve
Al "试着积极一点儿吧。我敢肯定你会过得如鱼得水！"
Marcel neutral c "您确定吗……？"
show al smile2 with dissolve
Al "我确定。你是个非常乖巧的男孩子。我真想不出我的哪个姑娘会不喜欢你，毕竟你礼貌周全、无可挑剔！"
Marcel sigh c "若只要彬彬有礼就能交到朋友，我怕是早就被友谊淹没了……"

show image "border" onlayer border
scene countryside_d:
    subpixel True
    size (1920, 1080) crop (0, 100, 1280, 720)
    linear 20.0 crop (350, 100, 1280, 720)
with wiperight_slow

"我叹了口气，眉头紧锁，望着窗外。"
"我能看见乡野在我眼前飞掠而过：无垠的田野、碧绿的树木、树篱与小小的农舍。"
"草甸里有绵羊在吃草，看上去宛如云朵；还有的牛小得如同瓷器摆件；还有鬃毛与尾巴灰白的小马驹。"
"万物都显得那么渺小、那么遥远，令我生出一种巨人的错觉。"
"这与巴黎全然不同。"
"窗外的景致与巴黎竟是如此迥异，令人心绪不宁。"

hide image "border" onlayer border
scene train:
    size (1920, 1080) crop (240, 40, 1440, 810)
show al neutral2 at center
$ all_moves(x_express=Wiggle(freq=.5, amp=10), y_express=Wiggle(freq=.12, amp=15), z_express=Wiggle(freq=.4, amp=1))
with wipeleft_slow

Al "好了，马塞尔，接下来这一整年你要在我的学校里就读。等你完成学业、满了十六岁，就回巴黎去，与你母亲重逢。"
Al "不过在那之前，你得和我一起住在这所寄宿学校里。"
Marcel neutral c "可是，既然是寄宿学校，我岂不是得和其他姑娘们同住一间寝室？"
Marcel "那样一来，她们定会识破我的秘密。"
show al smile2 with dissolve
Al "哦，你不必为此担心。我早已做好了一切必要的安排。你不会和其他姑娘们住同一间宿舍。"
Al "你可以住进专门留给老师们用的私人房间。"
show al frown2 with dissolve
Al "今年早些时候，我们的音乐女教师离开了我们。她跟一位政界部长私奔，跑去了兰斯。"
"阿尔贝汀姨妈哼了一声，仿佛兰斯是什么为非作歹的聚集地……不过，据我所知，也说不定当真是。我从没去过那里。"
"不过我更愿意相信，阿尔贝汀姨妈的不悦源于那位音乐女教师的背叛，而非兰斯本身。"
show al sigh2 with dissolve
Al "多亏她走得仓促，我们才空出一间房间，正好给你用。"
Al "你将彻底独处一间——虽说它算不上好看，可总比跟所有姑娘们挤在一间宿舍里强得多！"
show al smile2 with dissolve
Al "你会有自己的衣柜{i}，还有{/i}你自己专属的洗脸盆。听起来不是很称心吗？"
Marcel neutral c "听上去倒有几分……"
"与我和母亲同住的那间巴黎宽敞公寓相比，这里确实逼仄，但我不会说出口。考虑到阿尔贝汀姨妈为我所做的一切，那样说未免太刻薄了。"
Marcel sad c "……不错，可其他姑娘们会怎么说呢？她们难道不会纳闷，为何独独我受到特别照顾？"
show al smile2 with dissolve
Al "她们没空去琢磨这些闲事。她们的功课已经够让她们忙得团团转了，而且她们个个都谈不上有什么想象力。她们可当不成什么像样的侦探！"
Al "我会编个什么谎话来搪塞——也许就说你夜里惊悸难眠——她们就足够安心地去相信了。"
Marcel embarrassed c "但愿您说得对……"
"我轻轻咬着下唇。这不是个好习惯，却是我从母亲那里学来的。"
"如果非要继承我父母的某些缺点，我很庆幸继承的是那些无伤大雅的。我才不想像父亲那样，做个醉醺醺的浪荡子。"
show al frown2 with dissolve
Al "别这么忧心忡忡的，马塞尔！我敢肯定我的姑娘们会立刻喜欢你——不过你得学着把自己收拾得干干净净、整整齐齐！"
Al "若说我有哪桩最不待见的事，那就是邋遢马虎！"

$ achievement.grant("to_myennes")
scene cg27
$ all_moves(x_express=Wiggle(freq=.5, amp=10), y_express=Wiggle(freq=.12, amp=15), z_express=Wiggle(freq=.4, amp=1))
with wiperight_slow

"阿尔贝汀姨妈俯下身，将几缕发丝替我拢到耳后。"
"她虽然是我的姨妈，可她一碰我，我仍不免浑身僵硬。"
"我已多年不曾见过她。她于我而言无异于陌生人，而且纵使是我母亲的姐妹，她也没有母亲的金发与蓝眼。"
"阿尔贝汀姨妈看上去与母亲简直完全是另一种人：更结实、更强壮，前臂粗壮，一头铜色头发绾成利落而得体的发髻。"
"她活脱脱就是那种刻板印象里的女学监……"
"但也许，要当一名女学监，就非得生得这般模样。或许这是这一行当的必备条件。"
"我不禁思忖……"
Al "现在，仔细听好了，马塞尔。我的学校也许地处乡间，论陈设和经费，远不如你那些体面的城里学校，可我治校严谨。我要求严苛，对我的姑娘们寄望甚高。"
Al "你也许是我的亲外甥，可你若在课上掉了队，我会像责罚其他任何学生那样责罚你。你明白了吗？"
Marcel "我明白了……"
Al "不不不！这可不行。"
Marcel "您这话是什么意思？"
Al "从今往后，你就是我的学生，正因如此，你理应带着该有的恭敬来称呼我。来，从头再说一遍。"
Marcel "好、好的，嗯……抱歉，夫人？"
Al "很好。"
Al "听着，在学校里，我不能让旁人知道你其实是我的外甥。这个秘密我会替你守好，但只要有机会，我会尽量照看你。我欠莱奥妮这份情。"
Al "那么多年前，我未能帮上她。虽曾努力，她却把我拒之门外。她总以为自己最懂……"
Al "如今她终于放下身段，来征求我的意见，我可不想让她失望。"
Al "我不会让你失望的。"
Al "马塞尔，你终将在米耶纳享受那本就是你该得的那份宁静、惬意的求学时光：我向你保证。"
Al "你会结识那么多新朋友，学到那么多新本事，等到这一学年结束时，我敢说你将变得判若两人！"
"我知道姨妈是想让我振作起来，可她那股永不枯竭的精力，反倒让我觉得更加疲惫。"
"我不知道自己是否想成为一个新的人。我又怎么能呢？"
"我几乎都认不清现在的自己了——穿着贴身衬裙、连衣裙，还有那双带扣的黑皮鞋。"
"我觉得自己不像是平日的我，可我又不知道平日的我究竟是何模样。"
"我不知道自己该做些什么……{w}可我已没有多少时间去想明白了。"
"这铁轨总不会无止境地延伸下去。"

stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
play music "bgm/Mysterious.ogg" fadein 1.0
scene sky with wiperight_slow
window show dissolve

"大约两小时后，我和姨妈抵达了讷韦尔的火车站。"
"我提出替阿尔贝汀姨妈提旅行包，她却不耐烦地把我赶开。"
Al smile_side "没事的，亲爱的。你不必为我这行李费心！"
Marcel neutral c "可是——"
Al annoyed_side "也许你素来习惯帮衬莱奥妮，可{i}我{/i}料理自己的事情绰绰有余。说实在的，这正是我引以为傲的一点。我可不是什么柔弱的花朵。"
"于是，我只好空着手走出车站，而阿尔贝汀姨妈却吃力地拎着三个对她来说实在太沉的行李袋。"
"我想帮她一把，可我又能做什么呢？她已经拒绝了我的心意。"
"被好好训斥了一番后，我开始打量起这座城市，倘若它真配得上这一称呼的话。"
"讷韦尔远不及巴黎那么大。行人更稀少，房屋更矮小，就连在地上啄食的鸽子也似乎透着几分懒洋洋。"
"巴黎的鸽子又大又肥，却会为了最微不足道的残羹剩饭彼此恶斗。而讷韦尔的鸽子则毫无生气得多。它们饿得几乎连翅膀都拍不动，也抬不起那毛茸茸的脑袋。"
"姨妈站在路旁等候，我便陪在她身边一同等着。"
"终于，一辆公共马车沿着道路缓缓驶来。那是一辆笨重庞大的马车，能坐下十五个人，由三匹看着倦怠的马拉着。"
"公共马车在姨妈和我面前停下，我们俩便攀了上去。"
"阿尔贝汀姨妈与她的行李袋较着劲，直到那时她才允许我帮她一把。"
"我担心她一个人想把行李拖上公共马车，结果会弄掉在鹅卵石路面上。那样扣子可能就会散开，她的衣裳会散落得到处都是。那可实在太丢人了。"

play ambience "sfx/carriage.ogg" fadein 2.0
scene omnibus:
    size (1920, 1080) crop (240, 40, 1440, 810)
show al neutral2 at center
$ all_moves(x_express=Wiggle(freq=.5, amp=10), y_express=Wiggle(freq=.12, amp=15), z_express=Wiggle(freq=.4, amp=1))
with wipedown_slow

"从讷韦尔到勃艮第乡间的这段路十分颠簸，沿途布满了无数坑洼与低洼处。"
"公共马车摇摇晃晃。我跟着来回摆动，脑袋磕在车窗上，次数多到数不清。"
"我能听见在木轮嘎吱作响之上，马匹的喷鼻声。它们的蹄子踏在不平的路面上，发出参差不齐的嗒嗒回响；这声音又被车夫偶尔甩出的鞭声所打断。"
"这趟旅程着实谈不上舒适；跟巴黎的电车相比更是如此。"
"巴黎的电车也是由马拉动，与这辆公共马车颇为相似，但车内的座垫更为舒适，也不那么拥挤，更不那么颠簸。"
"同车的乘客围着我叽叽喳喳地交谈，嗡嗡的话音灌满我的耳朵。我也能闻见周遭这些来自不同阶层的男男女女，混杂着马匹的气味。"
"这些彼此争斗的感官冲击如此强烈，我不得不紧紧闭上双眼。"

stop ambience fadeout 2.0
window hide dissolve
scene black with eyeclose
$ renpy.pause(0.8)
play ambience "sfx/carriage.ogg" fadein 2.0
scene omnibus:
    size (1920, 1080) crop (240, 40, 1440, 810)
show al neutral2 at center
$ all_moves(x_express=Wiggle(freq=.5, amp=10), y_express=Wiggle(freq=.12, amp=15), z_express=Wiggle(freq=.4, amp=1))
with eyeopen
window show dissolve

"当我终于再次睁开眼时，唉，我发现周遭的环境竟丝毫没有改变。"
"人们在不同地点下车，随着我们穿过一座座村庄，又有更多的人上车。"
"一位绅士上车时朝我点了点头致意，而另一个显然{i}并非{/i}绅士的男人（他的双手太过粗糙；衬衫被体力活磨得破烂又肮脏）竟朝我挤了挤眼。"
"我脸上一红，把头别向一边。"
"姨妈捕捉到了他那狡黠的眨眼，皱起眉头。她朝我凑近了些，一只手臂环住我的肩膀，然后低声耳语……"
show al frown2 with dissolve
Al "{size=-5}别看他，亲爱的，别去招惹他。{/size}"
Marcel sad c "{size=-5}我{i}才{/i}不想招惹他呢。{/size}"
"我也低声回应。"
Marcel frown c "{size=-5}我什么都没做。我只是坐在这儿罢了。{/size}"
show al annoyed2 with dissolve
Al "{size=-5}也许吧，可你还是得小心。别去招惹那种男人的目光。你得把头转开。{/size}"
Al "{size=-5}那种男人会把任何斜瞥都当作是邀请。还是谨慎些为好。{/size}"
"姨妈捏了捏我的肩膀。我想这该是一种安抚的动作，反倒让我打了个寒颤。"
"我不喜欢被男人以色眯眯的目光打量，更不喜欢为并非我错的事而被怪罪。"
"我不明白自己做了什么才招来那个眼色，也许是我太天真了。"
"难道这就是女人们时常要面对的事吗？"
"即便是那个并非绅士的男人下了车，留下姨妈和我成为最后两名乘客，我的不安也依旧挥之不去。"
show al sigh2 with dissolve
Al "这也好。你本就有操不完的心，哪还有闲工夫去应付那些不请自来的纠缠。"
show al frown2 with dissolve
Al "依我看，从某种意义上说，你当真像极了你母亲。她当年也常招惹来那些浪荡子和无赖。"
"姨妈咂了咂舌，摇了摇头。"
show al annoyed2 with dissolve
Al "我生得不如你母亲漂亮——咱们年轻时，我还为此怨恨过她呢！——也从来不像她那样，被男孩子争相献殷勤。我那时可真吃醋……"
show al sad2 with dissolve
Al "可是如今回想，我想那说不定反倒是件幸事。"
Al "可怜的莱奥妮。"
show al neutral2 with dissolve
Al "好了，你千万别担心。马塞尔，有我在你身边，你在米耶纳什么都不必怕。我的学校里不会有男人来骚扰你。"
Marcel sigh c "就只剩下姑娘们了……"
show al smile2 with dissolve
Al "啊，说得也是。光是她们，就足够让人头疼了！"
Al "再过个把钟头，我们应当就要到米耶纳了。打起精神，注意着点儿。"
Al "米耶纳的景致美极了。我想你这辈子恐怕还没见过这般景象吧！"
Marcel sad c "我这一生，也没见过多少世面……"
Al "那好，这一回你可要大饱眼福了！"
"姨妈听上去很乐观，我却并不完全确定。"
"我因这一路奔波而疲惫不堪，身上那身陌生新衣又把腰和胸口勒得发紧。"
"我的双脚酸疼，尽管我几乎没走过五步路；脑袋也被马蹄声震得突突直跳。"
"感觉我们仿佛连日赶路了一般，可事实上，不过才过了大约七个钟头。"
"阿尔贝汀姨妈和我在将近正午时到了巴黎那座大火车站。"
"天还没完全黑下来，可风已比先前凉了许多。等我们抵达米耶纳时，太阳想必已经落下山了。"

stop ambience fadeout 3.0
scene sky_n with wipeup_slow

"我靠回椅背，望向窗外。太阳缓缓沉入地平线下，将周围的景物染成粉色。随后，过了一些时候，星星便出来了。"
"我想在这乡间看星星，或许要比在巴黎看得更分明，可我从来不是个爱仰望天空的人。我到底是个十足的城里少爷。"
"我想，乡间是美的，可这份美并非我能真正懂得欣赏的那种。"
"我住过漂亮的公寓，随我那位昔日名流的父亲去过歌剧院、戏院和豪华咖啡馆，花草与牛群又怎会打动我的心呢……？"
"至少我当初是这么想的，然而……"
Al smile_side "瞧，马塞尔！快看！"
"我目瞪口呆地望着窗外，眼睛睁得像鹅蛋那么大。"

play ambience "sfx/carriage.ogg" fadein 3.0
show image "border" onlayer border
scene countryside_n:
    subpixel True
    size (1920, 1080) crop (0, 180, 1280, 720)
    linear 20.0 crop (350, 180, 1280, 720)
with dissolve

"我终于看见它了。"
"米耶纳。"
"村庄如同一张毯子般铺展在我眼前——啊，这实在{i}是{/i}一幅赏心悦目的美景！"
"缓坡上那一座座长满青草的小丘，随处可见点缀着的花朵。"
"这些房屋的排布与花朵一样随性，仿佛它们是从土里自己长出来的一般。它们由木头和石头筑成，屋顶倾斜，散落在山丘与山谷之间，其间夹杂着树木与树篱。"
"绿得简直刺痛了我的眼睛。"

hide image "border" onlayer border
scene countryside_n
with wipeleft_slow

"未来一年，我就要住在这里，穿上姨妈那所学院庄重的制服。"
"我将住进这些古朴的小屋之间，上一所同样古朴的小学校，一切都坐落在乡野深处。"
"我已不是马塞尔·德·圣雷米了。再也不是了。"
"接下来的一年，我将以一个女孩的身份住在这里，混在一群女孩中间，栖身于陌生的屋檐之下。"
"我不会回巴黎，也将见不到母亲。除了阿尔贝汀姨妈，我便只能孤身一人了。"

stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}序章{/u}{vspace=1}  9月15日{vspace=1}  白衣身影") )
play ambience "sfx/night_amb.ogg" fadein 1.0
play music "bgm/Luce.ogg" fadein 1.0
scene sky_n with wiperight_slow
window show dissolve

"当阿尔贝汀姨妈和我终于抵达她的学校时，天空已是一片深沉的午夜蓝。"
"这是一个无云的夜晚。我能看见每一颗星星，宛如挂毯上的针脚，在那天鹅绒般的蓝色中闪烁不休。"
"至于月亮，那是一弯纤细的新月，两端收成尖角。它看上去锋利，近乎致命。"
"倘若星星是根根针脚，那么月亮便形同一枚针。"
"我觉得自己从未如此真切地看清过月亮（就连星星也一样）。巴黎街头似乎永远弥漫着的那股呛人烟雾，如同一层额外的云翳遮蔽了天空。"
"或许正因如此，米耶纳的月亮和星星才显得这般尖利。"
"我的呼吸在胸口猛地一滞。"
"我的心仿佛成了一枚针垫。它已被那恶毒而危险的月亮彻底刺穿。"
"这片天空，某种意义上是美的，可它与我习以为常的一切相隔甚远。"
"米耶纳的一切于我而言都是未知，而我也为它所不识。"
"我几乎觉得天空像是在向我发出警告。它想让我远离……"
"可这是个愚蠢的念头……{w}不是吗？"

scene yard_n:
    size (1920, 1080) crop (240, 40, 1440, 810)
show al neutral2 n at center
with wipedown_slow

Al "那么，你觉得如何？"
"姨妈将一只手搁在我的肩上。"
show al smile2 n with dissolve
Al "这是所好学校，不是吗？也许边边角角有些破旧，可夜色倒正好把那些遮掩了！"

show image "border" onlayer border
scene yard_n:
    subpixel True
    size (1920, 1080) crop (0, 180, 1280, 720)
    linear 20.0 crop (350, 180, 1280, 720)
with wiperight_slow

"我费力地将目光从月亮上挪开（这比我预想的要难得多），转向那所学校。"
"这是一栋简陋的建筑，只有一层。它的窗户一片漆黑，里面所有的灯光都已熄灭。"
"那些漆黑的窗户使它看上去宛如一位失明的老妇人，虹膜上聚满了白内障。"
"这栋楼也有点歪斜，朝一边倾侧。铺着板岩的屋顶上还立着一根倾斜的烟囱，仿佛随时都会滑落砸到地上。"
"它看上去既不太结实，也不太安全——不过我觉得，它这种摇摇欲坠反倒正合我眼下的处境。这间破败的校舍里，竟透出几分近乎诗意的东西。"
"在它周围还散落着其他几栋建筑，或许是用作更年幼学生的教室（阿尔贝汀姨妈告诉我，这所学校招收三岁到十六岁的孩子）。"
"我想，那栋稍远一些、看起来比其他楼都要高的建筑，应该就是所有女孩的住处了。"

hide image "border" onlayer border
scene yard_n
with wipeleft_slow

"只有这栋楼似乎还涌动着勃勃生气。"
"楼上的窗户亮着灯，我仰起头往里张望，能看见一些白色的、轻纱般的朦胧轮廓。"
"这些就是我未来的新同学吗？"
"都这么晚了，她们想必已经换上睡衣。她们似乎毫不在意会有人从旁走过，瞥见她们披散的发丝或裸露的手臂。"

window hide dissolve
scene cg7 with wipeup_slow
$ renpy.pause(1.0)
window show dissolve

"我尤其注意到三楼第二扇窗户里的一个女孩；那正是位于倾斜屋顶正下方的一层。"
"她站在窗边，神情恍惚地眺望着校园的景致。"
"很难看清她，可她那份沉静，以及照亮她后脑的明亮灯光，却让她比同伴们更显眼。"
"她的脸庞柔和而苍白，宛如瓷娃娃，嘴唇微撅，噘成一个小小的弧度。而她的头发，对一个女孩来说短得反常，是金色的，服帖地勾勒着她的脸，犹如一只画框。"
"她身子前倾，手掌按在玻璃上，目光不安地游移着、搜寻着。"
"她在寻找什么呢？"
Marcel c shock "哦……"
"就在那时，那位神秘的女孩将目光投向了校园。我的视线与她相遇。她正直直地看着我。"
"她皱起了眉头，张开了嘴。"
"看起来她似乎要开口说些什么——或许是无声的问候，又或许是个问句？——可我看不清她的嘴唇。我没有这个机会了。"
"阿尔贝汀姨妈叹了口气，摇了摇头。"

scene yard_n:
    size (1920, 1080) crop (240, 40, 1440, 810)
show al frown2 n at center
with wipedown_slow

Al "老天！灯光怎么还亮着？都已经十点半了！"
show al annoyed2 n with dissolve
Al "杜布瓦夫人应该清楚，姑娘们十点钟就该上床睡觉。她在这儿已经够久了！"
Marcel neutral c "杜布瓦夫人……？"
show al neutral2 n with dissolve
Al "我的助手。她也教英文。"
Al "她是个好人——心地善良，富有同情心——可我担心她对姑娘们太过心软。"
show al sigh2 n with dissolve
Al "我不过离开她一个来星期，那些淘气鬼就把她摆弄得服服帖帖。"
"阿尔贝汀姨妈咂了咂舌。"
show al annoyed2 n with dissolve
Al "但愿我不在期间，姑娘们的学业达到了令人满意的水准，因为她们的宵禁分明没有好好执行！"
Al "我明天得去跟她谈一谈……"
show al smile2 n with dissolve
Al "好了，别管这些了。长途跋涉之后，你一定累坏了。"
Al "跟我来。我带你去你的房间，你就可以好好睡上一觉了。"
Al "明天你就要向同学们介绍自己，届时你在米耶纳的新生活才算真正开始。听上去是不是很令人兴奋？"
"我知道姨妈是一番好意，可我不知道该如何回答那个问题。"
"我想，从某种意义上说，这倒也令人兴奋。"
"也许我会想象自己是那位著名的德翁骑士，既非男人也非女人，在最适合自己的时候，于两种性别之间来回切换……"
"但我不是什么伟大的历史人物，也不是什么英雄。"
"我不过是个寻常的巴黎少年，只想安安静静、平淡无奇、毫不起眼地过完这一生……"
"而现在，我甚至不被允许做一个男孩。"
"既然如此，那我又是谁？"

scene sky_n with wipeup_slow

"我重新抬头望向三楼的第二扇窗户，想寻见那张面容甜美、留着金色短发的女孩，却再也找不到她了。"
"她大概是在阿尔贝汀姨妈同我说话的时候走开的。"
"这么一想，我不由得有些难过。"
"我曾希望，她有一天能成为我的盟友……"
"可她凭什么要那样做呢？"
"她根本不知道我是谁。"
"我自己也几乎不知道自己是谁。"

stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}序章{/u}{vspace=1}  9月15日{vspace=1}  风暴前夕") )
play ambience "sfx/night_amb2.ogg" fadein 1.0
play music "bgm/Night.ogg" fadein 1.0
scene cg28 with wiperight_slow
$ renpy.pause(0.8)
window show dissolve

"那一夜，我睡得很不安稳。"
"我的新房间，比我从前同母亲住的那间公寓里的卧室还要小。床也更简陋，被褥单薄。"
"不管我怎么翻来覆去，总是找不到一个舒服的姿势。"
"阿尔贝汀姨妈给我买的那件裙子被叠好，放在我房间角落的一张小木桌上。"
"这个房间里的几乎一切尽是木制：从每走一步就吱呀作响的地板，到墙壁、书桌，再到角落里的五斗柜。"
"这房间黯淡而阴郁，倒也正合我的心境。"
"我身上穿的并不是我平日的睡衣，而是阿尔贝汀姨妈给我买的睡裙，为的是让我的伪装更加天衣无缝。"
"这件睡裙长而端雅，垂落及踝。"
"我猜想，它算得上妩媚动人，可这并不是我愿意穿的东西。光滑的布料贴着裸露的双腿与胸膛，那触感令我一阵战栗。"
"心绪不宁的我在床上辗转反侧，散开的头发铺散在扎人的枕头上。"
"我这辈子从未觉得自己如此赤裸——可矛盾的是——这睡裙又显得太过厚实、太过沉重。"
"相比之下，我盖的毯子又薄得可怜。我冻得发僵。"
"我太想睡着了，于是把耳朵用力压进头颅与枕头之间，耳朵像一块手帕似的，被压得折了起来。"
"很疼，我在呼吸间低声呜咽，却没有一个人听见。"
"我孤身一人。"
"大半个夜晚我都无法入睡，只是一个劲儿地担忧：担忧远在巴黎的母亲，担忧即将到来的学校生活，担忧我那些新同学，担忧他们审视的目光，担忧他们会不会识破……"
"要是他们识破了，我该怎么办？"
"那时我的人生，就真的没有活头了。"
"那我就得远远逃离所有文明——不只是巴黎熙熙攘攘的街头，连乡间也要逃离——然后活下去……"
"我该去哪里落脚？"
"我会住在那片幽暗与阴郁之中；或许住进一个洞穴里。然后我靠苔藓果腹，喝下从洞穴崎岖石壁上滴落下来的水。"
"也许，若我在洞穴里待得足够久，一动不动，我的身体就会化作石头，我便不再是血肉之躯，而是成为这片大地的一部分。"
"我喜欢这个念头。"
"人死之后，躯体本该回归大地。那将是一种极为平静安详的离世方式……"
"不过，这只是我的一时妄想而已。我不会死的。"
"时间仍将不可抗拒地一路前行，而我终须醒来，去面对即将来临的清晨。"
"对此，我无能为力。"

stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene sky g
with clockwipe
$ renpy.pause(0.5)
show overlay2
show message3 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message3
hide logo2
hide overlay2
with datetrans2

$ save_name = (__("{u}序章{/u}{vspace=1}  9月16日{vspace=1}  早起的鸟儿") )

$ renpy.pause(0.3)

play ambience "sfx/birds.ogg" fadein 1.0
play music "bgm/Casual_Day.ogg" fadein 1.0
scene sky with dissolve
window show dissolve

"翌日清晨，太阳早早升起，明丽耀眼。"
"我几乎一夜不曾合眼，可卧室窗外鸟儿的啁啾声，仍旧将我唤醒。"
"至少{i}它们{/i}听起来很快活。我但愿也能分享它们的欢愉，可我的脑袋沉甸甸的，仿佛有人敲开了我的颅骨，把我的脑子换成了一块石头。"
"我从床上坐起，被褥滑落到膝盖四周，不由得皱起了眉。"
"我能感觉到额内有一条血管在怦怦跳动。这是紧张所致吗？"
"我想，或许也是长期睡眠不足的缘故，尽管我向来便不热衷早起。"
"当初住在巴黎时，醒来意味着我必须准备好去上学，而去上学意味着我会被同学们欺负和折磨……"
"如今我已不在巴黎，可往日的恐惧仍旧挥之不去；此刻更因境遇的转变而被放大。"
"如果巴黎的男生欺负我，是因为我这个男孩长得像女孩，那么米延的女生会不会因为我这个女孩举止像男孩，而欺负我？"
"女孩本应比男孩更温柔、更甜美，可她们却有锋利的肘子，和狠毒的舌头。"
"至少，我试图这样安慰自己——她们不会把同学推下楼梯，也不会对着人家的脸吐口水。那可不是淑女所为。"
"可万一她们得知，我并不是什么淑女呢？"
"然而我没有太多时间来琢磨这件事，因为我听到有人用指节敲响了我的房门。"

play sound "sfx/knock.ogg"
stop ambience fadeout 3.0
scene marcel_room with wipedown_slow

Al neutral_side "马塞尔？你醒了吗？"
Marcel shock n "啊，嗯……"
"我站起身来。"
"地板吱呀作响，我赤裸的脚趾抵着木面，屈伸颤抖。"
"有一根钉子从木板里突了出来，扎住了我右脚毫无防备的脚底。"
"我醒来不过五分钟，这一天却已经“一帆风顺”得过了头。"
Marcel embarrassed n "我醒了，阿尔贝汀姨妈……"
"尽管脚上疼痛，我还是努力让声音保持平稳。我不想让她担心——不是为这点小事。"
Marcel "您请进吧。"
Al annoyed_side "好。"
"房门吱呀一声打开，我的姨妈走了进来。"

play sound "sfx/door.ogg"
show al neutral:
    xpos -0.10 xanchor 0.5 ypos 0.5 yalign 0.5
    ease 1.5 xpos 0.45

"她照例收拾得一丝不苟：红发没有一丝凌乱。"
"浓烈的紫罗兰香气，从她周身每个毛孔里弥漫出来。"
"我的鼻子抽动了一下。我好像要打喷嚏了。"
"我的姨妈粗略地扫了一眼我的房间，然后打量起我来。我还穿着睡衣，这让她看得我满脸羞红。"
"阿尔贝汀姨妈{i}毕竟{/i}是我的亲戚，可我以这般模样被人端详，终究还是令人难堪。"
"若她是我的母亲，我倒不会这么在意，可我那位不苟言笑的姨妈，我已经多年未见了。"
Al "务必在七点半之前穿戴整齐，到食堂去。那是住校女生用早餐的时间。"
Al "你的校服收在衣柜里。下楼去食堂前把它换上，并且务必要拍打平整，别留一丝褶皱。我可容不下邋遢。"
show al annoyed with dissolve
Al "哦，还有一件事。你的长袜两只必须一般长短，刚好及到膝盖上方；凡留长发的姑娘，都得把头发束起来。你知道的，长发散着可不庄重。"
Marcel sad n "是、是的，阿尔贝汀姨妈……"
show al neutral with dissolve
Al "往后的早晨我都不会来查你的岗，所以你得自己起床。我不能让人看出我待你有特别之处。你明白吗？"
Marcel "是、是的，嗯……说得在理。"
show al sigh with dissolve
Al "好。"
show al neutral with dissolve
Al "倘若你吃早饭迟到，那就只能饿着。要到午饭才有的吃。另一方面，若你上课迟到，就要受罚。我说清楚了吗？"
Marcel "再清楚不过了。"
"我曾盼着姨妈能对我稍稍宽松一些，可我想，若对我格外优待，对那些女孩便不公平了。"
"我不想给同学们更多挑出我、把我当作异类的理由。"
show al annoyed with dissolve
Al "哦，还有一件事。你还记得我昨天跟你叮嘱的话吗？"
Marcel shock n "嗯……要当心男人？"
Al "嗯，对，可还不止这些。"
show al neutral with dissolve
Al "你在我的学校里，不能再叫我姨妈。我是这所学校的校长，你则是我的学生，你我之间就仅此一重关系。务必把这一点记在心里。"
Marcel sad n "哦，嗯……"
"我低头看向地板。受伤的脚仍在隐隐作痛。"
Marcel "我会更注意些的。姨——"
Marcel "我是说，布吕吉埃夫人。"
show al smile with dissolve
Bru "很好。"
show al neutral with dissolve
Bru "我想，既入校就读，你也别再把自己的名字写成‘马塞尔’了。你应当改用阴性写法：‘玛塞尔’。"
Bru "从今日起，你就是玛塞尔，而我是布吕吉埃夫人，你要牢牢记住才好。"
Bru "按时去上课，和其他姑娘们交朋友，别惹是生非……"
show al sigh with dissolve
Bru "还有，尽量让自己过得开心。"
"布吕吉埃夫人的声音，片刻前还刻意保持着疏离与公事公办，此刻却柔和了下来。"
show al neutral with dissolve
Bru "愿你在这米耶纳度过美好的一年——不只是为你自己，也是为了莱奥妮。她非常在乎你，别无所求，只盼你能快活。"
show al sad with dissolve
Bru "倘若你能在米耶纳寻得哪怕一丝安宁，或许她也就不必那般挂念了。"

play sound "sfx/footsteps3.ogg" fadein 1.0
show al:
    ease 2.5 xpos -0.20

"说完这番话，布吕吉埃夫人便转过身去，踩着吱呀作响的地板走了，每走一步都随之呻吟。"
"我想，这或许是如此古老建筑的好处之一——我暗自思忖，看着她的脚步声渐渐远去。以后早上我再也不必担心睡过头了。同窗们踩在这陈旧木地板上的嘈杂脚步声，必定能瞬间将我唤醒。"

stop sound fadeout 1.0

"布吕吉埃夫人走后，我叹了口气，伸手穿过自己的头发。"
"“要努力开心起来，”她这样说，仿佛我存心要痛苦似的！这算是什么建议？"
"我感激姨妈关心我，也知道她是一片好意，可她说的话，听来似乎并不特别有用。"
"唉，算了。"

show image "border" onlayer border
play sound "sfx/drawer.ogg"
scene marcel_room
$camera_move(-2500,800,400,0,0,'dissolve')
with wipeleft_slow

"我走到我的衣橱前，拉开它，抽屉因年岁久远而吱呀作响。"
"衣橱里放着一套校服，正如布吕吉埃夫人所说。那是一长块黑色衣料，让我想起了丧服。"
"我带戒心地打量了它好一会儿。我并不很想穿上它。那样做，总感觉像是承认了失败……"
"可我听见同学们在自己的宿舍里窸窸窣窣地活动起来。"
"胳膊穿进袖子、脚探进袜子的声响，透过我房间的墙壁渗透进来。"
"有轻盈娇俏的说话声，有哗哗的水声，还有咯咯的笑声。"
"我得赶紧了，否则开学第一天就要迟到。"
"我觉得姨妈不会高兴的；尤其是在她费心训诫了我一番之后。"

hide image "border" onlayer border
scene marcel_room
$camera_move(0,0,0,0,0,'dissolve')
with wiperight_slow

"我从抽屉里取出那件裙子，放在床上。"
"我小心翼翼地避开挂在洗脸盆上方那面有裂缝的镜子，脱下睡裙。"
"我往脸上泼了些水，用毛巾擦干。"
"然后，我穿上昨天穿的那件衬衣——隐约察觉到它带着火车烟味，和布吕吉埃夫人浓重的香水味——再把新校服套在外面。"
"校服十分合身。它在腰间收紧，又在臀围处蓬开，赋予我一个颇具欺骗性的女性身段。"
"我梳理头发，重新扎成昨天那样的两条辫子，不过这活儿既累赘又繁琐。"

play ambience "sfx/footsteps3.ogg" fadein 3.0

"我花了好一阵子才学会让双手配合无间，而且辫子也散了好几次。"
"就在我手忙脚乱之际，我听见走廊上传来笃笃的脚步声；与我相隔的，只有那扇单薄的木门。"
"每当听到有人走过，我都不由得绷紧神经。"
"我心中有一部分不禁好奇：他们是否知道我在屋里，又是否知道我能听见他们。"
"这些穿着如出一辙的黑色连身裙、把头发束在脑后的女孩，会不会在我门口驻足，揣想门后究竟是谁？"
"这个念头实在令人心神不宁，我的手指一滑，编了一半的辫子又散开了。"

stop ambience fadeout 3.0

"我咂了咂舌。为什么非得这么难？"

window hide dissolve
scene black with blinds2
$ renpy.pause(0.5)
$ achievement.grant("mirror_mirror")
scene cg29 with blinds2
$ renpy.pause(0.8)
window show dissolve

"终于，我压住了自己笨拙的手指，和令我失措的紧张。我用发绳扎好两条辫子，端详起镜中的自己。"
"我身上穿着一个货真价实的女学生的、端庄的长裙校服。"
"裙子大部分是深色的，袖子和衣领却是雪白的。"
"这套校服看起来并没有我担心的那般寒酸或阴沉，可那条长裙的确叫人觉得压抑。衣料粗糙而坚硬，勒进我的腰里，可——恰恰相反——胸前又空荡荡的，绰有余裕。"
"布吕吉埃夫人给我带的，一定是一件大一号的校服，好配得上我的身高——可我虽然个子高，胸膛却平板得像块木板。"
"我想，她是没料到这一点。"
"我左右转动着身子叹了口气，对自己的模样，比以往任何时候都更挑剔。"
"这裙子的剪裁虽不完美，可若没有一位熟练女裁缝的帮忙，这大概已经是我能得到的最好结果了。"
"我本该料到会是这样的。毕竟，这件裙子并不是为我做的。"
"感觉这世上真的没有一样东西，是为我而造的。"
"在巴黎那所糟糕的男校里，我觉得格格不入；可到了这里，我依然格格不入。"
"我真的能说服我的新同学，让我显得属于这里吗？"
"我毫无把握。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}序章{/u}{vspace=1}  9月16日{vspace=1}  赴汤蹈火") )
play music "bgm/Energetic.ogg" fadein 1.0
scene sky with wiperight_slow
window show dissolve

"虽然我在鸟鸣声中醒得还算早，可我在新卧室里花了大多时间，只顾着整理头发和裙子。"
"我大概盯着自己的倒影看了整整五分钟，既惊叹，又有些害怕。我就是忍不住。"
"这场蜕变看起来如此彻底——从巴黎少年到乡间女学生——这让我惊惧不已。"
"我在镜中那道左右颠倒的影像上久久审视着自己，远远超过了必要的时间，想要窥探那个旧日的马塞尔，在我体内是否还残留着些许痕迹。"
"当然，我的五官依旧如故；我蓝眼睛，短翘的鼻子，可当这些五官配上发辫和裙子时，它们在脸上的排布，不知怎的，看上去竟不一样了。"
"从前学校里的男生们，总爱取笑我这副模样太像个女子。"
"他们是对的。"
"我继承了父亲的个子，和母亲的五官。"
"那双眼睛、鼻子和嘴唇，长在我母亲身上如此姣好，搁在我身上却近乎滑稽——我是一个蹿得过快、又高又瘦又憨笨的男孩……"
"可这些我曾为之绝望的五官，一旦与更女性化的服饰相配，竟显得近乎动人。"
"这使得审视自己的脸，成了一种十分奇异的体验；事实上，奇异到我全然忘了时间。"

play ambience "sfx/crowd.ogg" fadein 3.0
scene diningroom with wipedown_slow

"当我终于走进餐厅，我愕然发现——令我沮丧的是——那里已经挤得水泄不通。"

show image "border" onlayer border
scene diningroom:
    subpixel True
    size (1920, 1080) crop (0, 180, 1280, 720)
    linear 20.0 crop (350, 180, 1280, 720)
with wiperight_slow

"梳着束发、身穿黑色长裙的女孩们，整齐地坐在环绕着长桌摆放的木椅上。"
"她们身子前倾，一边吃着早餐，一边彼此聊得起劲。"
"在这所学校，早餐似乎很是简单；几片抹了黄油和果酱的面包，外加一杯牛奶。"
"我看见刀光一闪，女孩们往面包片上抹着黄油，又听见牙齿磕到杯沿的声响。"
"能想象到的各色头发——淡金、艳红、灰棕、乌黑——来回晃动着，她们一模一样的辫子垂在背后。"
"这些女孩年纪各不相同。最小的大约只有五六岁，个子矮得双脚都够不到地面。至于年纪大些的，则与我不相上下。她们坐得更从容自信，脊背挺直，嘴角挂着轻松的笑意。"
"坐在这两张长桌旁的女孩究竟有多少，实在难以数清，但若要让我猜，我想大约有四十人。"
"女孩的人数并没有我担心的那么多，但她们凑在一起，绝对能闹出一片喧嚣。"
"我也确信，这些女孩并非这所学校的全部学生。"
"这些女孩想必住在米埃纳周边的村庄里。她们住在学校，是因为每天往返学校步行实在太远。"
"至于住在米埃纳本镇的女孩，多半与家人同住。她们不在学校寄宿，而是夜晚回家。"
"这所学校接纳的女学生总数，恐怕接近七八十人。"
"我在巴黎就读的那所学校学生要多得多，可她们全都是和我一样的男孩。我这一生，还从未见过这么多女孩，齐刷刷聚在一间屋子里。"

hide image "border" onlayer border
scene diningroom
with wipeleft_slow

"然而，当我出现在餐厅门口的一刹那，所有交谈似乎都静了下来。"
"女孩们纷纷抬起头，连最小的那些也不例外，好奇地打量着我。"
"我咽了口唾沫，垂下目光，盯着自己的脚。"
"我觉得自己像是个不受欢迎的闯入者；一场婚宴上不请自来的客人。"
"我羞涩地在桌间穿行，一路把目光钉在自己的脚上。"
"可有空位让我坐下？我又该去哪儿领取我的食物？"
"我往前走时，听见女孩们在窃窃私语，而且毫不遮掩。她们甚至根本没想压低声音。"
Cla "那是谁？"
Claa "我从没见过她……"
Claaa "她是新来的学生吗？"
Claa "有新学生？"
Claaa "这是杜布瓦夫人昨天说的！"
Cla "那么，她就是那个新学生咯……"
Claaaa "我听说她是从巴黎来的！"
Claaa "巴黎？真的吗？"
Cla "不知道她会不会摆出一副高高在上的架子……"
Claaaa "也许她会觉得自己高人一等，瞧不上我们这些乡下人！"
Claa "她都不看我们一眼。说不定她是个势利眼。"
Claaa "也许她只是害羞……"
Claaaa "不过她个子可真是高！"
Cla "你说得对！她简直像个巨人！"
Claaa "她比诺艾米还要高！"
"女孩们开始彼此咯咯地笑作一团。"
"她们的笑声让我的脸涨得通红，头垂得更低了。"
"她们的话算不上恶毒，可我不喜欢她们对我妄加揣测——尤其是在我听得见的场合。"
"难道她们就不在乎我的感受吗？"
"也许，作为她们这个小圈子里的外人，她们并不认可我也同样会有感受。"
"这个念头刺痛了我。"
W "打扰一下，新来的姑娘。你是想吃早饭吧？"
Marcel shock u "啊、哦……"
"我停下脚步，抬起头来。"
"餐厅后墙开着一扇木窗。我猜想，那扇窗户想必通向厨房。"
"倚在窗台上、小臂压着木头的，是一位身形纤瘦的女子。她脸颊上点缀着雀斑，棕色的头发在脑后绾成一个发髻。"
"她在衣服外系着一条白色围裙，这让我揣测她一定是厨师。"
Marcel sad u "是的，嗯……我正发愁该去哪儿呢……"
Cook "唉，你要是早点儿到，兴许还能跟着其他姑娘们学样呢……"
Cook "你算是勉强赶上了。我正打算开始做午饭呢。"
Marcel "是、嗯……对不起……"
Cook "别道歉了，孩子。不要紧的。看在今天是头一天的份上，迟到这么一小会儿，我可以原谅你。"
"厨师冲我甜甜地一笑。"
"我不禁揣测她究竟多大年纪。她看起来并不比我年长多少。"
"也许她过去曾是这里的学生，一直没能真正离开这所学校……？"
"无论她的过往如何，她的微笑都令我心安。胃里那团焦虑的结慢慢松开，我发觉自己比过去半小时以来都要平静。"
Cook "要吃的时候，你得在这儿跟别的姑娘们一道排队，然后我给大伙儿挨个盛，就像这样。"
"厨师递给我一只托盘。托盘里有一个盘子，盛着两片看起来有些单薄、蔫软的面包，还有一杯牛奶。"
Cook "好了，快去吧！我手头还有好多活儿要干呢！"
"她随意摆了摆手，像在打发我走，可脸上仍旧带着笑意，我想那不过是玩笑罢了。"
Cook "你得趁村里教堂的钟声还没响起，赶紧把它吃了。你总不想迟到吧，嗯？"
Marcel ehe u "不，嗯……我确实不想……留下个不好的第一印象总归不好……"
Cook "那是一定的！"
Cook "布吕吉埃夫人是个好老师——是最好的之一——可她严厉得很。你可不想跟她结仇吧！"
"一想到会把自己的姨妈变成敌人，实在令人沮丧。也只有彻头彻尾的失败者，才做得出这种事。"
"我真的得振作起来了。"
"我端着托盘，环顾房间，想找一个空位。"
"第二张长桌旁空着好几个位置，那儿坐的大多是五到十二岁的女孩，但我并不太想和这些小孩子坐在一起。"
"我并不讨厌孩子（其实我觉得他们挺可爱的），可那样只会招来年长女孩们的取笑。"
"我该跟同龄的人坐在一起——可该找谁呢？"
"我沿着长桌来回打量了片刻，随即停住目光。"

show image "border2" onlayer border
scene diningroom blur:
    subpixel True
    size (1920, 1080) crop (200, 0, 1280, 720)
    linear 19.0 crop (200, 220, 1280, 720)
show luce neutral2:
    subpixel True
    size (1920, 1080) crop (-130, 0, 1280, 720)
    linear 19.0 crop (-130, 220, 1280, 720)
with wiperight_slow

"在这一片无法辨认的脸庞中——她们穿着制服，模样惊人地相似——我瞥见了一张熟悉的面孔。"
"我只不过与她有过一面之缘，就在昨夜我们目光交汇的那一刻，可她的面容却始终留在我脑海里。"
"也许是因她那一脸憧憬的神情。"
"正是昨天坐在窗边的那个女孩，当时她凝望着米埃纳的丘峦群山，仿佛宁愿身在别处。"
"远看时我便觉得她生得漂亮，如今近了细看，才发现这并非我一时无端的臆想。"
"她的头发比绝大多数同龄同学都短，剪成齐整的波波头，垂到下颌线处。她有一双棕色的眼睛，头低垂着，看上去身材娇小纤弱。"
"有那么片刻，我差点把她当成了年纪很小的学生——也许十一二岁吧？——可她却是和年纪较大的女孩们坐一桌，尽管她并不与她们交谈。"
"说到底，她想必跟我的年纪差不多。"
"她虽与好些学生并排坐着，却不与她们交谈。她看上去与她们的嬉闹格格不入，仿佛活在自己的世界里。"
"她两旁各有一个空位。看样子，其他人都在与她保持距离。"
"她同窗们的冷淡或许自有缘由，但除非我亲自去和她攀谈，否则无从知晓。"
"我迟疑着，拖着步子往前挪了几步。"

hide image "border2" onlayer border
scene diningroom
show luce neutral:
    xpos 0.45 xanchor 0.5
with wipeleft_slow

Marcel u neutral "嗯……"
"我刚一开口，脸就泛起淡淡的粉红。"
"要是说话能不结巴就好了……！"
Marcel u ehe "我在想，嗯……我能坐在你旁边吗？"
"那女孩没有回答。至少没有开口。也许她觉得，犯不着在我身上浪费口舌吧？"
"与仍忙着闲谈的其他女孩不同，她一次也没有瞥向我。不过，她倒是点了点头，我把它当作默许。"

stop ambience fadeout 5.0
scene diningroom:
    size (1920, 1080) crop (240, 40, 1440, 810)
show luce neutral2:
    xpos 0.45 xanchor 0.5
with dissolve

"我挨着她坐下，然后放下托盘。"
Marcel u smile "谢、谢谢你。"
show luce sigh2 with dissolve
"女孩耸耸肩，仿佛在说这没什么。"
"我很快就发现，她并不怎么爱说话。"
"我寻思着是否冒犯了她……可若真冒犯了她，她又怎会让我坐在她旁边？"
show luce neutral2 with dissolve
Marcel u shy "嗯……你也许听说过我。看样子有些同学已经知道了。我叫玛塞尔，是这里的新学生。"
Marcel u ehe "我以前住在巴黎，嗯……乡下的这一切对我来说都很新鲜……不过我、我肯定会渐渐喜欢上这里的……！"
"说到那句话的末尾，我的声调扬了起来，我不禁皱了皱眉。"
"恐怕我听起来很绝望，可若真如此，那也是因为我确实如此。鉴于我在旧学校的种种经历，我实在拿不准将来会不会喜欢上米埃纳，不过无论如何，我仍竭力抓住哪怕几缕希望。"
"我不想在还没真正体验过米埃纳之前，就把它一笔勾销。"
"我觉得还是往好处想比较好，可……"
show luce sigh2 with dissolve
Girl "……你还挺乐观的。"
Marcel u neutral "哪里乐观了？"
"那位短发的女孩抬起头来，嘴唇抿着。"
show luce frown2 with dissolve
Girl "你为什么觉得自己会喜欢这儿呢？"
Marcel u sad "这、这个……我……"
"她带着挑衅的目光看我。我不得不垂下了视线。"
Marcel u ehe "我大半辈子——不，我这辈子——都住在城里……"
Marcel "我也喜欢那里，可它实在太喧闹了。人那么多，烟囱里冒出的烟那么多。到处都是灰蒙蒙的……"
Marcel "米耶讷就不是那样。这里绿意多得多。"
Girl "确实更绿，这点我承认……"
show luce sigh2 with dissolve
Girl "不过也更安静。"
Marcel u neutral "我倒没觉得有多安静。这些姑娘们吵得很……"
"那女孩审视了我片刻，仿佛在掂量着我，随后……"
show luce smile2 with dissolve
Girl "……呵。"
"她的唇角微微一翘。她居然真的笑了……！"
Girl "嗯，这话倒也没错。这些姑娘们聊天，是因为没别的事可做，好借此填补那份沉寂。"
Marcel u frown "那你就不说话……？"
show luce neutral2 with dissolve
Girl "不常说。"
Marcel "为什么？"
Girl "没那个兴致。太无聊了。"
show luce sigh2 with dissolve
Girl "米耶讷这儿的一切……{w}都那么、那么无聊。"
show luce neutral2 with dissolve
Girl "要是你一辈子都住在城里，兴许会觉得这儿挺有意思，可不出一个月，你就会一门心思想回去了。"
Girl "我真想去城里，可是……"
show luce sad2 with dissolve
"这时，女孩摇了摇头。也许她觉得自己的话说得太多？"
show luce sigh2 with dissolve
Girl "……算了，当我没说。"
"她叹了口气。"
show luce neutral2 with dissolve
Girl "你该把早饭吃了。再过五分钟钟声就要响了。"
Marcel u shock "对、对……！谢、谢谢你……！"
"我并不怎么饿，可昨天没吃多少东西，肚子正咕咕作响。"
"我可不想它在课堂上叫唤。那会难堪极了。"
"我至今给人留下的第一印象已经够糟了，可别让同窗们再觉得我是个贪得无厌的饕餮。"
"我往面包上抹果酱时，女孩面无表情地看着。她没有笑，但看起来比刚才更有兴致了。"
Girl "……顺便说一下，我叫露丝。"
Marcel u neutral "你的名字……？"
"她点了点头。"
Luce "其实叫什么也无所谓啦。等你回了城，多半就把我忘了，我也不怪你。"
show luce sigh2 with dissolve
Luce "这个可怜巴巴的小村子，真是一点意思都没有。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}序章{/u}{vspace=1}  9月16日{vspace=1}  众目睽睽") )
play music "bgm/Classroom.ogg" fadein 1.0
scene cg1 with wiperight_slow
$ achievement.grant("centre_of_attention")
$ renpy.pause(1.0)
window show dissolve

Bru al annoyed_side "好了，同学们，安静下来。"
"布吕吉埃夫人站在教室前方，双手交叠。"
"我站在她身旁，目光低垂，望着木地板。我无法直视任何一位同窗的眼睛。"
"年级较大的女孩们的教室相当狭小；也许是因为在米埃纳能继续学业的年长女孩并没有多少。"
"我想，米埃纳像我这个年纪的女孩，大多已经去干活了；要么在农场帮衬家里，要么缝补袜子，要么学着做帮厨女仆。"
"能继续来上学的女孩算是幸运的。就乡村的标准而言，她们的家境想必还算宽裕。"
"这间屋子里大约有二十名十三到十六岁的女孩。"
"我想，年纪更小的学生想必需要在各自独立的班里上课：一个是幼儿园年纪的女孩，另一个则是稍大一些的学童？"
"我也不能十分确定。我在这所学校待的时间还不够久，还没弄清这一切究竟是如何运作的。"
"需要打交道的同窗比我想象的少，这让我松了口气，可这间教室却拥挤得让人幽闭发慌。"
"教室里塞满了木桌，几乎连绕着它们穿行的余地都没有。"
"空气中弥漫着粉笔灰和鞋油的气味，熏得我有些头晕。"
"如今新同窗们的窃窃私语被局限在一方空间里，听来更觉被放大了。"
"在餐厅里，想避开她们的目光还容易些，可现在我被推到她们面前展示，便再也躲不开了。"
"我仿佛成了一只吊在集市摊位上死兔子。"
Bru al neutral_side "今天，我要向大家介绍一位新同学。"
Bru "米耶讷很少来新生——尤其还是年纪大些的！——不过我相信你们会以礼相待。"
"女孩们都梳着一模一样的辫子——唯有留波波头的露丝例外——她们头凑着头，窃窃私语。"

# sfx here?
show image "border" onlayer border
scene classroom:
    subpixel True
    size (1920, 1080) crop (0, 300, 1280, 720)
    linear 25.0 crop (350, 300, 1280, 720)
with wiperight_slow

Cla "这么说，我们终于能近距离瞧瞧她了……"
Claa "没想到她这么高！"
Claaa "可不是嘛！她可得当心，不然脑袋要撞到天花板了！"
Claa "我真是羡慕死啦！跟她一比，我又矮又胖！"
Claaa "瞧瞧她那漂亮的长腿……"
Cla "她长个儿是往上长，可横着却一点没长，对吧？"
Claaa "我倒觉得她看着挺纤细的……"
Cla "她是纤细，可纤细错了地方！她的胸脯简直像男孩子一样平！"
"像个男孩的……"
"这句话在我脑海中反复回荡，仿佛某种咒语。"
"倘若我在新同窗眼里看起来像个男孩，那也是因为我本来就是——可我还指望我的伪装不至于这么轻易被看穿。"
"我知道自己的胸是平的（若不是，那才真叫人惊骇），可它真就看上去那么可笑吗？"
"突然，我愚蠢地感到局促不安起来。我的脸发烫。"
"同窗们窃笑起来，被我这份羞涩逗乐了。"
Cla "一个巴黎来的姑娘，竟这么安静。"
Claaa "说不定她是个娇滴滴的淑女？"
Claa "好一副自命不凡的样子！"
Claaaa "可要真是个淑女，怎么偏偏跑到米耶讷这种地方来？"
Claa "说不定是她家道中落了！"
Claaa "那样倒好！省得她再也别想瞧不起咱们！"
"{i}我{/i}是在瞧不起她们吗？"
"除了露丝，我至今没跟任何人说过一句话，可也许她们已把我的沉默当成了傲慢？"
"我自认并非傲慢之人，可旧学校里有些男生似乎也觉得我是。若这些女孩也这么想，那想必是我的过错。"

hide image "border" onlayer border
scene cg1
with wipeleft_slow

"我好奇地低头打量自己。我左右转了转身子，裙摆飘飘，却仍旧看不出自己的外表有什么异样之处。"
Bru al frown_side "姑娘们，请回想一下：我不是告诉过你们，要{i}尊重{/i}你们这位新同学吗。你们不是幼儿园里的小娃娃。你们都是大姑娘了，我希望你们拿出与之相称的举止来。"
Bru al annoyed_side "请你们注意点体统。"
"布吕吉埃夫人拍拍手，窃窃私语随之停了下来——尽管停得很慢。"
"女孩们的目光仍在我身上来回扫视。"
"她们如今是在心里对我评头论足，即便没有用嘴把看法说出来。"
"不知怎的，这种无从知晓反倒让我更加局促不安。"
Bru al neutral_side "好啦，这位新来的姑娘来自巴黎，想必你们都清楚。"
"布吕吉埃夫人叹了口气。"
Bru al sigh_side "你们这些姑娘家长舌得很，活像一群椋鸟。只要肯下功夫，你们怕是连石头里的秘密都能给撬出来……"
"女孩们被这句玩笑逗得咯咯直笑，气氛也因此缓和了些。"
"我怯生生地抬起头，透过睫毛打量着我的同窗们。"
"我想她们并不像我最初想象的那般可怕。她们不过是些普通的女生。我并不觉得她们存心要害我，可那句关于我胸部（或者说平坦的胸部）的话，仍叫我隐隐作痛。"
Bru smile_side "现在，玛塞尔，你愿意自我介绍一下吗？"
Marcel "哦，嗯……是、是的……我叫玛塞尔·雷诺……"
"那不是我的本名，可那正是布吕吉埃夫人在昨天漫长的火车旅途中反复向我灌输的名字。"
"她还替我编了一段身世，此刻我正像背诵一首诗那样，流利地向这群毫无戒心的女生复述。"
Marcel "……我生在巴黎。我这一生大半都在巴黎度过，直到——"
"可我终究没能说完这层精心编织的谎言。"

play sound "sfx/door.ogg"
stop music fadeout 1.0
scene classroom
show claudine smile:
    xzoom -1 xpos 1.20 xanchor 0.5
    ease 1.2 xpos 0.80
with dissolve

"教室的门突然、猝不及防地被推开了，伴着一声嘎吱、一声闷响，以及一声惊呼……"

play music "bgm/Comedy.ogg" fadein 1.0

Girll "哦，您好，夫人！我{i}非常、非常{/i}抱歉来晚了！"

scene classroom:
    size (1920, 1080) crop (300, 40, 1440, 810)
show claudine smile2:
    xzoom -1 xpos 0.75 xanchor 0.5
with dissolve

"一个女孩站在门口。她穿着和其余同窗一样的黑色制服，长而端庄的裙摆，却在白色衣领下系了一截红丝带，给这身装扮添上一抹亮色。"
"她的头发又长又松散，不像同窗们那种辫子，一路垂到背心中央。她的发丝大半是直的，只在发梢微微卷起。"
"她一手叉腰，腼腆地笑了笑。"
show claudine laugh2 with dissolve
Girll "哎呀！我还偏偏挑这么个日子迟到，嗯？这就是那个我听过好多传闻的新姑娘吧？"

scene classroom
show claudine smile:
    xzoom -1 xpos 0.75 xanchor 0.5
show al annoyed at left2
with dissolve

"布吕吉埃夫人抿紧嘴唇，眯起双眼。"
Bru "克洛蒂娜，我看你还没有资格问东问西！你可不是寻常的“迟到”。你是相当、{i}相当{/i}迟到了。"
show claudine laugh at bounce
Claudine "哎呀！我倒不知道原来这么讲究区别呢！"
show al frown with dissolve
Bru "当然讲究！你要是只迟到个几秒钟，我兴许还能睁一只眼闭一只眼，可整整五分钟——"
show claudine shock at bounce
Claudine "哎呀，夫人，五分钟又不是多长的时间——再说我迟到是有原因的。"
show al sigh with dissolve
Bru "克洛蒂娜，你总能找出个理由来替你的恶劣行径搪塞——只不过你的理由究竟有几分可信，我可从来都拿不准。"
Claudine "可是夫人，我说的{i}千真万确{/i}，我摸着良心！您{i}真的{/i}以为我会在新姑娘进校的同一天迟到吗？我早就眼巴巴地想看看她了！"
show claudine smile with dissolve
Claudine "您看，今早我不得不在家多待了几分钟，都是因为我那亲爱的让内特。"
show al frown with dissolve
Bru "哦，别又拿你那{i}傻猫{/i}说事了。"
show claudine shock at bounce
Claudine "{i}是{/i}，我的猫，{i}又是{/i}——而且让内特{i}才不{/i}傻！不是我自己夸口，她是最漂亮的猫儿，毛色美极了！"
show claudine smile with dissolve
Claudine "今早，我家让内特她——"
Bru "够了，克洛蒂娜。我已经容你唠叨得够久了。"
show al sigh with dissolve
Bru "你还不快坐下，安静点？等会儿我再以合适的方式跟你算账。"
show claudine neutral with dissolve
Claudine "您不想听听我为什么迟到这么久吗？"
show al annoyed with dissolve
Bru "姑娘，你的借口我听一辈子都嫌多。"
show claudine laugh with dissolve
Claudine "那好吧。我会规矩的！"
"尽管克洛蒂娜没有说出口，我却几乎听出了那句尾端悄悄缀上的、带着促狭意味的“暂且如此”。"

stop music fadeout 3.0
play sound "sfx/footsteps3.ogg" fadein 0.5
scene classroom:
    size (1920, 1080) crop (0, 40, 1440, 810)
show claudine smile2:
    xzoom -1 xpos 1.10 xanchor 0.5 ypos 0.5 yanchor 0.5
    ease 1.4 xpos 0.35
with wipeleft_slow

"克洛蒂娜在教室前排落座，一条腿叠在另一条腿上。"

stop sound fadeout 1.0

show claudine smile2:
    xzoom 1.0
with dissolve

$ renpy.pause(0.3)

show claudine:
    ease 0.8 ypos 0.55

"随后，她靠在椅背上，用半阖的眼睛打量着我。"
"我注意到，她的眼睛显得颇为深暗，眼角四周带着些模糊的晕痕，或许是睡眠不足的缘故。"
"她的皮肤也很苍白，尤其是眼睑一带。那里的皮肤白得近乎透明，隐隐透出蜿蜒的蓝紫色血管……"

play music "bgm/Claudine.ogg" fadein 1.0

Claudine "嗯？"
"克洛蒂娜忸怩地笑了笑。"
Claudine "你可是盯着我看个不停呢，新来的姑娘。"
Marcel u shock "没有……这个，我……"
show claudine laugh2 with dissolve
Claudine "我原以为，作为闪闪发光的新生，盯着你看是我的本分，可也许并非如此！"
show claudine smile2 with dissolve
Claudine "有瞧见什么合你心意的吗？"
Marcel u shy "我……这、这个，嗯——"

scene classroom:
    size (1920, 1080) crop (350, 40, 1440, 810)
show al frown2:
    xpos 0.70 xanchor 0.5
with dissolve

Bru "克洛蒂娜。"
"布吕吉埃夫人向克洛蒂娜投去一记警告的眼神。"
Bru "再耍嘴皮子，课间休息你就去劈柴火。"
Claudine u annoyed "那多没意思！我手指头会扎刺的！"
show al sigh2 with dissolve
Bru "那就请你安静下来，让玛塞尔把自我介绍说完。"
Claudine u smile "玛塞尔，是吧……？"
"克洛蒂娜上下打量着我。她淡淡地笑了一下，活像一只准备扑向肥美老鼠的猫。"
Claudine "那好吧，你继续。别让我这张漂亮的脸蛋分了你心神！"

scene cg1 with wipeup_slow

Marcel "这个，嗯……我……"
"我能感觉到同学们的目光都落在我身上，唯独露丝没有。她正望着窗外，神情漠然。"
"而克洛蒂娜则目光灼灼地盯着我，依旧微笑着。"
"她的目光令我心神不宁。那感觉简直像是在用眼睛剥我的衣服；不仅剥去我裙子的布料，甚至连我的皮肤也要一并剥下……"
Marcel "我叫玛塞尔·雷诺，来自巴黎。"
Marcel "我一直在巴黎生活，直到最近身体开始不适。"
Marcel "医生说我受了烟尘雾霾的不良影响，若能离开城市到乡下来，身子就会好些。"
Marcel "我来米耶讷完成最后一年的学业。我希望身子能好起来，也希望与大家和睦相处。"
"我匆匆结束自我介绍，向同学们行了一个笨拙的屈膝礼。"

scene classroom:
    size (1920, 1080) crop (350, 40, 1440, 810)
show al neutral2:
    xpos 0.70 xanchor 0.5
with dissolve

Bru "玛塞尔体质相当纤弱，所以夜里必须独自睡一间房，也不允许参加任何剧烈的体育活动。"
Bru "希望你们姑娘家够懂事，体谅她的特殊情况，尽量让她感到受人欢迎。"
Claudine u laugh "您说{i}她{/i}体弱？"
"克洛蒂娜难以置信地哼了一声。"
Claudine "我从没见过像她这么高的姑娘！她能把校园里的白杨树都比下去！"

scene cg1
with wipeup_slow

"新同学们开始窃笑，我羞愧地低下了头。我的脸颊滚烫。"
"即使在巴黎的寄宿学校，我也出奇地高，可如今被一群女同学围在中间，我必定显得比以往任何时候都要更像个巨人。"
"我就像一棵被娇小的花朵环绕的树。"
Bru al frown_side "克洛蒂娜！别胡闹了，否则我可真要罚你了。"
Bru al neutral_side "好了，教室里只空着一个座位，我想你恐怕得坐前排了，玛塞尔——不过我确实挺同情你的。"

show image "border2" onlayer border
scene classroom blur:
    subpixel True
    size (1920, 1080) crop (400, 80, 1280, 720)
    linear 15.0 crop (0, 80, 1280, 720)
show claudine smile2:
    subpixel True
    size (1920, 1080) crop (350, 20, 1280, 720)
    linear 15.0 crop (-50, 20, 1280, 720)
with wipeleft_slow

"我琢磨了整整三秒钟这是为什么，直到我的目光落在那张唯一的空课桌上。"
"结果正巧，它偏偏就设在克洛蒂娜旁边。"
play sound "sfx/chair.ogg"
"我忍住一声叹息，在她身边坐下，椅腿刮过木地板的咯吱作响。"

hide image "border2" onlayer border
scene classroom blur:
    size (1920, 1080) crop (0, 120, 1152, 648)
show claudine smile3:
    xpos 0.40 xanchor 0.5 ypos 0.55 yanchor 0.5
with dissolve

"克洛蒂娜倾身向我，微笑着，把一缕散落的头发绕在手指上。"
Claudine "你好啊，生面孔。"
Marcel shy u "哦，嗯……你、你好？"
show claudine laugh3 with dissolve
"克洛蒂娜咯咯地笑了起来。"
Claudine "你这人还挺别扭的，是不是？"
Marcel shock u "你、你这是什么意思？"
show claudine smile3 with dissolve
Claudine "起先你一直盯着我看，现在却又装出一副受不了我的样子！"
Claudine "你宁愿对着书桌说话，也不肯理我这张迷人的脸蛋，我可真是伤心呢！"
Marcel shy u "我，嗯……这个，我……"

scene classroom:
    size (1920, 1080) crop (120, 40, 1440, 810)
show claudine smile2:
    xpos 0.25 xanchor 0.5 ypos 0.55 yanchor 0.5
show celine annoyed2:
    xpos 1.10 xanchor 0.5 ypos 0.55 yanchor 0.5
    ease 1.2 xpos 0.75 ypos 0.55 xanchor 0.5 yanchor 0.5
with dissolve

Girllll "其实，你们本就不该在课堂上说话……"
show celine sigh2 with dissolve
Girllll "而且，自夸自家脸蛋漂亮，可一点也不淑女。你若还有半点羞耻心，就该把这种话留给异性去说。"
show claudine laugh2 with dissolve
Claudine "哦，塞琳，你总是这么一本正经。真稀奇，你居然肯屈尊跟我们这些渺小的人物说话！"
Marcel frown u "嗯？"
"我的好奇心战胜了焦虑，我发现自己转过头去。"

show image "border" onlayer border
scene classroom blur:
    subpixel True
    size (1920, 1080) crop (500, 0, 1280, 720)
    linear 19.0 crop (500, 220, 1280, 720)
show celine frown2:
    subpixel True
    size (1920, 1080) crop (-130, -50, 1280, 720)
    linear 19.0 crop (-130, 170, 1280, 720)
with wiperight_slow

"原来，塞琳坐在克洛蒂娜和我身后。她有一头深色的头发，在脑后编成一条复杂的辫子，还留着厚厚的刘海。"
"她看向克洛蒂娜，显然不以为然，双臂交叠在胸前。"
"她坐在椅子上的姿态，似乎将她与同学们区分开来，尽管她不过是众多穿着相同制服、头发一丝不苟地向后梳去的女孩之一。"
"她看起来骄傲而高傲，双眼因鄙夷而微微眯起。"
"她说话的方式，也不同于克洛蒂娜那轻快的声调。不知怎的，她的语气更为从容有度，也听不出丝毫明显的乡土口音。"
"那么，我想她大概不是出生在米耶纳的吧。她看起来不像。"

hide image "border" onlayer border
scene classroom:
    size (1920, 1080) crop (120, 40, 1440, 810)
show claudine smile2:
    xpos 0.25 xanchor 0.5 ypos 0.55 yanchor 0.5
show celine frown2:
    xpos 0.75 xanchor 0.5 ypos 0.55 yanchor 0.5
with wipeleft_slow

Claudine "难怪你会急着替新姑娘说话。你们俩真是一路货色，对不对？"
show celine annoyed2 with dissolve
Celine "我不明白你在说什么。"
Claudine "哦，我看你心里明白得很！你们这些城里姑娘自会抱成一团，好把我们这些可怜的乡下小民踩在脚下，是不是？"
show celine sigh2:
    xzoom -1
with dissolve
Celine "你现在纯粹是在胡思乱想。"
"塞琳嗤之以鼻，把鼻尖扬得高高的。"
show celine frown2 with dissolve
Celine "我出生在哪里无关紧要。我叫你闭嘴，仅仅是因为你惹我心烦。"
show claudine laugh2 with dissolve
Claudine "可你这样样都看不顺眼，亲爱的塞琳！你的脾气跟醉汉一样反复无常！"
show celine sigh2 with dissolve
Celine "也许我的脾气是反复无常，克洛蒂娜，就因为非得坐在你后面。"
show claudine shock2 at bounce
Claudine "噢，天哪……"
"克洛蒂娜甜甜地向塞琳眨着眼睛。"
show claudine smile2 with dissolve
Claudine "我让你分心了吗，塞琳？日复一日地对着我美丽的后脑勺，你的心可承受得住吗？"
show claudine laugh2 with dissolve
Claudine "你是不是想让双手穿过我的发间，感受它有多么柔顺丝滑？是这样吗？"
show celine annoyed2:
    xzoom 1
with dissolve
Celine "才没有。"
"值得称赞的是，塞琳对克洛蒂娜的指责丝毫不为所动。她只是哼了一声。"
Celine "你把自己看得太高了。"
show claudine smile2 with dissolve
Claudine "那总比把自己看得太低要强，对吧？"
Celine "就你而言，你的自尊心被滋养得过头了。当心别撑破了。"
Claudine "噢，我向你保证，我可小心着呢！"
show celine frown2 with dissolve
Celine "我对此表示怀疑……"
"塞琳皱起眉头。她似乎想再说些什么，但随即那念头一闪而过，她又打消了主意。"
show celine sigh2 with dissolve
"她叹了口气，摇了摇头，然后看向我。"
show celine neutral2 with dissolve
Celine "你是玛塞尔，对吧？"
Marcel shy u "是、是的，唔……我是。"
"我暗自庆幸，姨妈给我取的假女性名字恰好与我自己的名字相同，否则恐怕我一时间都记不起该答应别人的呼唤。"
show celine frown2 with dissolve
Celine "我真不羡慕你，非得挨着这个……{w} {i}丫头{/i}。"
show claudine shock2 at bounce
Claudine "你什么意思，亲爱的塞琳？你说“丫头”的时候停顿得那么久，仿佛想暗示我根本不是个女孩似的！"
Celine "你的{i}举止{/i}可一点也不像姑娘家。你是我认识的姑娘里嘴最没有把门的，你的规矩实在不成体统。"
show celine sigh2 with dissolve
Celine "坐在你后面已经够让我受的了，可偏还要坐在你{i}旁边{/i}……"
show celine neutral2 with dissolve
Celine "我真同情你，玛塞尔。"
show claudine annoyed2 with dissolve
Claudine "噢，收起你的同情吧！玛塞尔才不需要！她就喜欢坐在我旁边！谁不喜欢呢？"
show claudine laugh2 with dissolve
Claudine "毕竟，我可是聪明绝顶，又美貌，又有天分，又迷人——"
show celine sigh2 with dissolve
Celine "还招人烦。"
show claudine neutral2 with dissolve
Claudine "我只在别人先惹我的时候，才让他们烦！"
Claudine "我倒想不搭理你，亲爱的塞琳，可你偏要在玛塞尔第一天上学的时候，就散布关于我的狠毒谣言，我{i}真的{/i}很生气……"
show claudine shock2 with dissolve
Claudine "怎么，简直就像你不希望我交到朋友一样！"
show celine frown2 with dissolve
Celine "我看你{i}才{/i}不想要朋友吧。你宁可要一群跟班、一群信徒，好让她们来围观你的小把戏。"
Celine "你要是这么爱演戏，就去当个演员，别想把这间教室变成你的舞台。那可真够烦人的。"
show claudine annoyed2 with dissolve
Claudine "这屋里招人烦的可不止我一个……"
"克洛蒂娜固执地向塞琳吐了吐舌头，而塞琳没有回嘴。"
show celine sigh2:
    xzoom -1
with dissolve
"相反，她叹了口气，移开了目光。"
"看来大多数人都是这样对付克洛蒂娜的。他们别过头去，装作她不存在。"
"这对塞琳来说或许是个可行的办法，但……"

scene classroom blur:
    size (1920, 1080) crop (0, 120, 1152, 648)
show claudine smile3:
    xpos 0.40 xanchor 0.5 ypos 0.55 yanchor 0.5
with dissolve

Claudine "那么，玛塞尔！"
"克洛蒂娜又把全部注意力转回我身上，始终灿烂地微笑着。"
Claudine "认识一位从城里来的姑娘可真有意思。你知道吗，我一直想去巴黎？改天我可要让你好好给我讲讲那边的事！"
Claudine "还有，让你知道一下……"
"克洛蒂娜用手指甲轻轻地敲着她的课桌。"
show claudine laugh3 with dissolve
Claudine "……我可是{i}相当{/i}会说服人的。"
"我感到一阵寒意顺着脊背袭来。"
"克洛蒂娜不过是个女孩。她比我矮，而且身形纤细。"
"她的皮肤苍白，近乎毫无血色，眼下那圈暗沉的晕痕让她看起来仿佛许多天没睡过觉了。"
"我在巴黎上学时，总被同学们殴打、推搡、辱骂，可那毕竟是一所全是男孩的学校。"
"我还从未被一个有着克洛蒂娜这般纤弱身躯的男孩欺凌过，可她绿色眼眸里的那一丝光芒，却预示着危险。"
"我想别过头去，却很快发现自己做不到。那种感觉仿佛我中了魔法一般。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
play music "bgm/Energetic.ogg" fadein 1.0
play ambience "sfx/footsteps2.ogg" fadein 1.0
$ save_name = (__("{u}序章{/u}{vspace=1}  9月16日{vspace=1}  操场上的政治") )
scene sky with wiperight_slow
window show dissolve

"那天晚些时候，我们这二十来个女孩的班级，在布吕吉埃夫人的命令下，被带到音乐教室。那间教室设在另一栋楼里，与主教室分开。"
"我们步入校园，途经那栋七到十二岁孩子们上课的建筑。"
"门关着，我看不见里面，可声音还是一样传了出来。我听见一声低沉而模糊的呜咽。听起来像是其中某个女孩正被她的老师责骂。"

stop ambience fadeout 2.0
scene yard
show claudine laugh at center
with wipedown_slow

Claudine "小孩子。"
"克洛蒂娜轻蔑地笑着，摇了摇头。"
Claudine "他们吵得要命。"

show claudine:
    ease 1.0 xpos 0.30

$ renpy.pause(0.5)

show celine annoyed:
    xpos 0.75 ypos 0.53 xanchor 0.5 yanchor 0.5
with dissolve

Celine "你应该庆幸，那些年纪小的孩子是在另一栋楼里上课。"
show claudine smile with dissolve
Claudine "我{i}当然{/i}庆幸，简直庆幸极了！我每天感谢我的幸运星，他们也该好好感谢。可每回碰上哭闹的小孩，我就忍不住想捏他一把！"

show celine:
    ease 0.85 xpos 0.85

$ renpy.pause(0.5)

show mirabel shock:
    xpos 0.65 ypos 0.5 xanchor 0.5 yalign 0.5
with dissolve

Girlll "什么……？"
"一个跟在克洛蒂娜身后的女孩倒抽一口凉气，眼睛瞪得滑稽地大。"
"我不知道这位同学是谁，但这大概也在意料之中。我来这里还不到一天，同学们一模一样的黑裙子和编起来的发型几乎令人难以分辨。"
"我之后得加倍用心去记住她们的名字。"
show mirabel sad with dissolve
Girlll "你不是认真的吧，克洛蒂娜？你真的会对一个小孩子做那种事吗？！"
Claudine "要是他们把我惹烦了，那我可能真会。我最擅长把人捏得服服帖帖。要不要给你演示一下，米拉贝尔？"
"克洛蒂娜摊开她的手指，指尖是修剪得整齐匀称的指甲，咧嘴一笑。"
"那个我猜想应是米拉贝尔的女孩向后缩了缩，脸色苍白。"
show mirabel shock at twirl
Mirabel "天哪！我、我还以为你在开玩笑，可你居然这么坏！"
Mirabel "我得提醒我亲爱的玛丽-诺埃尔，让她离你远点！"
show claudine laugh with dissolve
Claudine "对，你就去说吧！让她知道，要是她不小心，大坏蛋克洛蒂娜会趁夜里去找她，在她全身留下一道道红印子！"
play sound "sfx/footstep.ogg"
show mirabel sad:
    ease 0.4 xpos 0.69
Mirabel "呀啊啊……！"
"米拉贝尔吱地一声，慌乱地向后退了一步。"
Mirabel "可、可怜的玛丽-诺埃尔！我可不想她被捏！"
show mirabel shy with dissolve
Mirabel "你、你也一样，玛塞尔。唔……"
"米拉贝尔怯生生地瞥了我一眼，眼睑半垂，睫毛是榛子色的。"
"米拉贝尔的头发也是榛子色的。它被扎成两条略微歪斜的辫子，一条比另一条粗些。而她的脸颊上则散布着雀斑，使她看起来有点像林间的小鹿——虽说住在巴黎的我从未见过鹿。"
Mirabel "我、我，唔……我知道咱们还算不上认识，或、或许你也不想听我说，可、可你在克洛蒂娜身边得小心点。有时候她是挺好，可、可有时候她又很吓人，而且，唔……这个嘛……"
show mirabel shock at bounce
Mirabel "请、请多保重。你看起来是个好姑娘，我可不想看到你受伤！"
show claudine shock with dissolve
Claudine "喂，米拉贝尔！"
play sound "sfx/footstep.ogg"
show mirabel sad at twirl
"克洛蒂娜一把抓住米拉贝尔一条凌乱的辫子，用力一扯，引得她的猎物叫出声来。"
show claudine annoyed with dissolve
Claudine "你要是真那么怕我，为什么还要当着我的面说我坏话？你以为我不会还击吗？你准是太天真，不然就是蠢透了！"

show claudine:
    ease 0.5 xpos 0.20

$ renpy.pause(0.5)

show noemie sigh:
    xpos 0.44 ypos 0.5 xanchor 0.5 yalign 0.5
with dissolve

GirlT "噢，得了吧。"
"另一个女孩（这个高而瘦长）哼了一声。"
GirlT "咱们{i}全都{/i}知道米拉贝尔很蠢。她那么迟钝，有时候连自己的名字都写不好！"
show claudine neutral with dissolve
Claudine "我清楚得很，谢谢你，诺艾米。那句话，照我们的话说，是反问。"
show noemie frown with dissolve
Noémie "你知道大家还怎么说吗？要是你问了蠢问题——"
show claudine laugh with dissolve
Claudine "你的名字大概是米拉贝尔·拉克斯吧！"
show noemie smile with dissolve
"女孩们开始笑作一团，克洛蒂娜也在其中。"
show mirabel shy with dissolve
"而米拉贝尔却没有笑。她的脸涨得通红，棕色的眼眶里开始涌满泪水。"
"我心想，这是否经常发生。米拉贝尔是不是常常被捉弄？"
"我这样想或许有些残忍，但她确实像是个容易下手的对象。她把情绪全写在脸上，又太过真诚，根本无力抵挡克洛蒂娜那恶毒的冷嘲热讽。"
show celine frown with dissolve
Celine "噢，得了吧。"
"塞琳皱起眉头。与其他女孩不同——她们似乎对克洛蒂娜那点卑劣的残忍津津乐道——她看上去一点也不以为然。"
show celine annoyed with dissolve
Celine "你该放过米拉贝尔。她又没得罪你。你能不能学着善良一点，像你的朋友特蕾莎那样？"
show claudine neutral with dissolve
Claudine "我不明白特蕾莎跟这有什么关系。她都不再上这所学校了。她已经继续过自己的生活了……"
show claudine smirk with dissolve
Claudine "而且，说实在的，米拉贝尔也该那么做！她到底为什么还要费力来上学，真是个谜！"
show mirabel scared at bounce
"米拉贝尔的下唇微微颤抖。看来她真的快要哭出来了。"
"我不禁为她感到难过。有那么一瞬，我犹豫着是否该出面替她解围，但……"

scene yard:
    size (1920, 1080) crop (350, 40, 1440, 810)
show al frown2 at center
with wiperight_slow

Bru "走吧，姑娘们！打起精神来！"
"布吕吉埃夫人终于注意到我们明显缺乏纪律，在校舍中间停下脚步，朝我们唤道。"
Bru "你们要是继续这样交头接耳，天黑前都到不了音乐教室。这可是个坏习惯，一点也不像大家闺秀。"

play sound "sfx/footsteps2.ogg" fadein 0.5
show al frown2:
    ease 1.0 xpos 0.75 ypos 0.5 xanchor 0.5 yalign 0.5

show mirabel shock2:
    xzoom -1 xpos -0.20 ypos 0.5 xanchor 0.5 yalign 0.5
    ease 1.8 xpos 0.25

$ renpy.pause(1.0)

stop sound fadeout 0.5

Mirabel "是、是的，夫人！我、我非常抱歉！"
"米拉贝尔快步跟上周吕吉埃夫人，如同一只小鸭子追着母亲跑，而克洛蒂娜则没那么积极。"

scene yard
show claudine neutral at left
show noemie neutral at center
show celine frown:
    xpos 0.82 ypos 0.54 yanchor 0.5 xanchor 0.5
with wipeleft_slow

Claudine "真是个笨蛋。她是不是以为，装出那副乖乖女的样子，就能让布吕吉埃夫人喜欢她，可她脑子里装的全是浆糊。"
Noémie "像她那样的姑娘{i}只好{/i}装出一副好模样。她本来就没有别的长处。她既不聪明，也不漂亮，相貌实在太过平庸。"
show noemie smirk with dissolve
Noémie "她要不是脾气好，就什么也没有了！"
show claudine shock with dissolve
Claudine "噢，这念头多可怕！我光是想想就浑身发抖！"
show claudine smirk with dissolve
Claudine "想象一下，就因为只配做个好人、才不得不装出好样子！我倒宁可去死！"
show celine annoyed with dissolve
Celine "别这么小题大做了。讲礼貌又不费一分钱。我觉得学着谦逊一点对你有好处。"

play sound "sfx/footsteps2.ogg" fadein 0.5
show celine:
    xzoom -1
with dissolve

$ renpy.pause(0.3)

show celine:
    ease 1.2 xpos 1.40

$ renpy.pause(0.8)

show claudine:
    ease 1.2 xpos 0.15

show noemie:
    ease 1.2 xpos 0.72

$ renpy.pause(0.5)

stop sound fadeout 0.5

"塞琳从克洛蒂娜和诺艾米身旁掠过，两人在她身后吹着口哨。"
Claudine "瞧瞧她！她可真是自命不凡！"
show noemie frown with dissolve
Noémie "真没想到她竟肯屈尊来跟我们这些下等人说话。"
show claudine laugh with dissolve
Claudine "真的，能得见她的芳容是我们的福分！我睡前一定记得去塞琳圣女的祭坛前拜一拜！"

play ambience "sfx/footsteps2.ogg" fadein 1.0
show image "border" onlayer border
scene yard:
    subpixel True
    size (1920, 1080) crop (0, 100, 1280, 720)
    linear 15.0 crop (350, 100, 1280, 720)
with wiperight_slow

"克洛蒂娜和诺艾米跟在班级的队尾。"
"我还不清楚自己该在这些陌生面孔中占什么位置，便不自觉地随着她们一起被裹挟着向前。"
"很快，我们来到音乐教室所在的那栋独立建筑。布吕吉埃夫人打开门锁，领着我们走了进去。"

stop music fadeout 1.0
stop ambience fadeout 1.0
window hide dissolve
hide image "border" onlayer border
scene black
with dissolve
$ save_name = (__("{u}序章{/u}{vspace=1}  9月16日{vspace=1}  谱曲") )
play sound "sfx/door.ogg"
play music "bgm/Celine.ogg" fadein 1.0
scene musicroom with dooropen
window show dissolve

"这间房间比我们的教室还要小，而且没有课桌和椅子。它实在相当空荡，只有几个木抽屉、几个柜子，以及一架靠着一扇窄窗的木制钢琴。"
"那么，我想这间就是音乐教室了。"

play sound "sfx/footsteps3.ogg" fadein 0.5
show al neutral:
    xpos -0.10 ypos 0.5 xanchor 0.5 yalign 0.5
    ease 1.5 xpos 0.5

Bru "好了，姑娘们，安静下来。"
stop sound fadeout 0.5
"等所有女孩都鱼贯而入后，布吕吉埃夫人拍了拍手，高个子诺艾米（最后进来的那一个）随手带上了门。"
Bru "现在，排好队形。"
"作为一名新生，我不知道布吕吉埃夫人所说的“列队”是什么，可别的女孩都知道。"

show image "border" onlayer border
scene musicroom:
    subpixel True
    size (1920, 1080) crop (0, 100, 1280, 720)
    linear 20.0 crop (350, 100, 1280, 720)
with wiperight_slow

"她们排成整齐的两列，每列十二人；高个子的女孩在后排，矮个子的靠近前面。"
"诺艾米是班里最高的几人之一，正站在后排。露丝则因为最矮，站在前排正中央，而克洛蒂娜那张咧嘴笑的脸在她身后浮现。"
"与此同时，塞琳从人群中脱身而出，在钢琴旁的小凳上坐了下来。"
"现在回想起来，我想起布吕吉埃夫人昨天在从巴黎到米耶纳的车程中告诉我，原先那位音乐女教师已经私奔去了兰斯。"
"布吕吉埃夫人想必暂时顶替着这门课，由塞琳弹奏钢琴，直到她能雇到别人来接替这个职位。"

hide image "border" onlayer border
scene musicroom
show al neutral at center
with wipeleft_slow

Bru "咳咳。"
"布吕吉埃夫人清了清嗓子，然后向我投来一记严厉的目光。"
Bru "我知道你是新来的学生，玛塞尔，不过当我让姑娘们排队形时，也包括你在内。"
Marcel shock "哦……！非常抱歉，夫人！"
"我的脸涨红了，新同学们都嘲笑我。"
Cla "她好像老是走神……"
Claa "她的魂都飘到云里去了！"
Claaa "那还用说！我的意思是，她那么高……"
"当我匆匆到第二排、在诺艾米和克洛蒂娜之间站定自己的位置时，窃窃私语和咯咯笑声充满了整个房间。"
show al sigh with dissolve
Bru "谢谢你，雷诺小姐。我欣赏你的配合。那么，现在。"
show al neutral with dissolve
Bru "我们要好好练一整小时的音阶。"
"这一群聚集起来的女孩中响起一阵齐声的叹息。"
show al frown with dissolve
"布吕吉埃夫人咳了一声，举起一只手示意安静。"
Bru "音阶很重要，姑娘们。你们永远都得回到基本功上来。只有当基础牢固时，你们才能在上面构筑技巧。"

show al:
    ease 1.0 xpos 0.70 ypos 0.5 xanchor 0.5 yalign 0.5

show claudine smile at left2 with dissolve

Claudine "夫人，我总觉得，有些人生来就有音乐天赋——"
"克洛蒂娜侧目瞥了塞琳一眼。"
show claudine smirk with dissolve
Claudine "——而另一些人，无论怎么努力，也{i}永远{/i}达不到水准，可怜的羔羊们。"
"此刻，克洛蒂娜把头朝米拉贝尔的方向偏了偏。"
"米拉贝尔一言不发，只是局促地盯着自己的脚。"
show al annoyed with dissolve
Bru "好了，克洛蒂娜，你不该这么刻薄。你们这些姑娘，谁也不会成为专业的歌剧演员，也不会去巴黎的音乐学院深造。我的要求并不严苛。我只想往你们的生活里注入一点文化气息。"
show claudine smile with dissolve
Claudine "夫人，凭我父亲的营生，我的生活已经有足够的文化了。"
show al frown with dissolve
Bru "我不知道你父亲让你接触的那种所谓“文化”，对一个年轻小姐来说是不是合适。而音乐，对任何女性来说都是值得追求的东西。"
show claudine annoyed with dissolve
Claudine "既然你说了我们谁都不会成为歌剧演员，那在我看来就是浪费时间。比起练音阶，我宁愿做些更有意思的事。"
Bru "很遗憾，克洛蒂娜，你又不是老师：{i}我{/i}才是。"
show claudine neutral with dissolve
Claudine "那为什么坐在钢琴凳上的是塞琳？"
"布吕吉埃夫人怒视了一瞬，但她尽力维持着自己的镇定。"
show al neutral with dissolve
Bru "塞琳是这里唯一会弹钢琴的姑娘。我在给她一个磨练技巧的机会。"
Claudine "是这样吗……？"
show al sigh with dissolve
Bru "确实就是如此。"
show claudine smirk with dissolve
Claudine "这么说，你并没有因为勒梅尔小姐私奔了、而你自己又不懂音乐、因此没资格教我们，就想占塞琳的便宜咯？"
show al mad with dissolve
Bru "克洛蒂娜，真是的！你今天太过分了！我理解你对我们新来的学生很兴奋，可你也用不着这么卖弄！你顶嘴的样子让人很不愉快，我不信玛塞尔会觉得你有多出色！"
Marcel shy u "唔，我……"
show claudine smile with dissolve
Claudine "噢，我怀疑玛塞尔在这地方可没对多少东西留下印象。她毕竟是城里来的。"
Claudine "我本想来点挑衅的、好引起她的注意，可她似乎铁了心一直避开我的目光！"
show al annoyed with dissolve
Bru "就我而言，我可不怪她。"
Bru "那么，我们开始练音阶吧……除非你还想给这段对话添点什么，克洛蒂娜？"
show claudine laugh with dissolve
Claudine "我想说的都说完了。"
show al neutral with dissolve
Bru "很好。那么，塞琳，你可以开始了。"
Celine huh "是，夫人。"

stop music fadeout 1.0
window hide dissolve
scene cg19 with wipeleft_slow
play ambience "sfx/scales.ogg" fadein 3.0
$ renpy.pause(1.0)
window show dissolve

"塞琳修长纤细的手指落在钢琴的琴键上。"
"我对钢琴所知甚少（我自己也没什么音乐天分），但这架钢琴看起来相当陈旧且磨损。它的声音不如父亲带我去巴黎听过的那些音乐会上所闻的琴声那般清亮动听，但塞琳仍毫不介意地继续弹奏。"
"她用指尖弹出的音阶颇为简单，可当我站在那里凝视时，却发生了一种奇妙的转变。"

scene cg19_2 with dissolve

"塞琳那总是撇成一副讥讽皱眉模样的双唇，此刻嘴角却微微抽动起来。她的表情不知怎的，显得柔和了许多。想必是因为她在微笑。"
"那是如此甜美的一抹微笑，她看起来几乎宛如天使。"

stop ambience fadeout 3.0
scene musicroom:
    size (1920, 1080) crop (350, 40, 1440, 810)
show noemie neutral2 at center
with wiperight_slow

Noémie "喂，新来的。"
"诺艾米用尖尖的胳膊肘戳了戳我的侧腰。"
show noemie smirk2 with dissolve
Noémie "你应该跟着音阶一起唱，而不是像条金鱼那样张着嘴站在那儿。"
Marcel shy u "啊，唔……对不起？"

play music "bgm/Claudine.ogg" fadein 1.0

show noemie:
    ease 1.0 xpos 0.70

$ renpy.pause(0.5)

show claudine smirk2:
    xpos 0.30 ypos 0.5 xanchor 0.5 yalign 0.5
with dissolve

Claudine "你为什么偏偏跟诺艾米道歉？"
"克洛蒂娜想必偷听到了我们低声的交谈，发出窃笑。"
Claudine "她又不是布吕吉埃夫人。你什么都不欠她的。"
show noemie frown2 with dissolve
Noémie "哼，我好心帮忙，倒成我的不是了。"
"诺艾米气呼呼地别过头去，而我则涨红了脸。"

show noemie:
    xzoom -1
with dissolve

$ renpy.pause(0.3)

show noemie:
    ease 1.2 xpos 1.20

$ renpy.pause(0.5)

show claudine:
    ease 1.0 xpos 0.5

Marcel sad u "我……我很抱歉……"
"我又在道歉了，尽管克洛蒂娜叫我别这样。我控制不住自己。道歉已成为我应对生命中每一次挑衅的惯常反应，无论那挑衅多么微不足道。"
"在巴黎那所旧学校，我总是在道歉。我因为上课走神而向老师道歉；因为惹恼了同学而向他们道歉；我甚至还因为自己成为那么多欺凌的对象而向校长道歉。"
"我才是那个被欺凌的人，总是在走廊里被人用墨丸砸中、被人绊倒，可他们却告诉我，这些“事件”是我自己的问题。"
"按校长的说法，是我性格中某些根本的东西让同学们与我为敌。就是因为我表现得太过像个女孩。"
"我也不想让新同学们与我为敌……"
"但令我宽慰的是，克洛蒂娜似乎并不因我那些过分的道歉而怪我。相反，她笑了起来。"
show claudine laugh2 with dissolve
Claudine "哦，你可真是个温吞性子！我原以为你不理我，是因为你觉得自己高贵得懒得跟我说话——城里人常常那么自命不凡！——可也许……"
show claudine smile2 with dissolve
Claudine "会不会你只是害羞呢？"
Marcel shy u "我……我一直都很安静……"
"我或许会说那是我遗传自母亲的性情，但我并不确定是否如此。母亲或许在父亲手中受过苦，可她绝不会默默承受。她常常咒骂他。"
"她比我更有血性——不过话又说回来，大多数人都比我更有血性。"
show claudine annoyed2 with dissolve
Claudine "那你跟塞琳可真不一样。她也来自城里——不是巴黎，而是奥尔良——还总让大伙儿记着这一点。她就喜欢在我们面前炫耀她那高人一等的学问。"
Claudine "你看她，弹着钢琴，活像布吕吉埃夫人的小哈巴狗。她真是个马屁精！"
Marcel neutral u "可她弹得确实不错，不是吗？"
show claudine shock2 with dissolve
Claudine "哦，你可别跟塞琳这么说。"
Marcel neutral u "为什么？"
show claudine annoyed2 with dissolve
Claudine "她早就自命不凡得过头了。可别再火上浇油了！你要是一味夸她，她会真把自己当成法国正牌女王了！"

scene musicroom
show claudine neutral:
    xpos 0.30 xanchor 0.5
show al frown:
    xpos 0.70 xanchor 0.5
with wipeleft_slow

Bru "克洛蒂娜！"
"布吕吉埃夫人的声音打断了塞琳的音阶，而她的眼睛则用一记足以令狮子的鬃毛变白的可怕瞪视牢牢钉住克洛蒂娜。"
Bru "我不会再提醒你第二遍。请专心些。"
show claudine neutral with dissolve
Claudine "是，夫人……"
"克洛蒂娜拖着腔调，明显没什么热忱，然后朝我微微一笑。"
show claudine smile with dissolve
Claudine "我们索性也跟着练吧。我也想听听你唱。"

show image "border" onlayer border
scene musicroom:
    subpixel True
    size (1920, 1080) crop (0, 100, 1280, 720)
    linear 20.0 crop (350, 100, 1280, 720)
with wiperight_slow

"克洛蒂娜张开嘴，开始跟着其他女孩一起唱起音阶。"
"混合在一起的歌声并不协调。"
"有些女孩声音轻柔得几乎听不见，而另一些则有着响亮有力的嗓门，毫不羞涩地充斥着整个房间。"
"当然，克洛蒂娜属于后一类。她也是位相当出色的歌手。她的嗓音清澈纯净，让我想起潺潺的流水。"
"我真希望自己也能这么说。"
"我不会唱歌；我确信我不会。我根本不知道该怎么唱。"
"我担心，只要我一开口，我的嗓音就会破音，然后所有人都会知道我不是我自称的那个人。我其实并不是个女孩。"
"我本想保持沉默，但……"

hide image "border" onlayer border
scene musicroom:
    size (1920, 1080) crop (120, 40, 1440, 810)
show claudine smile2:
    xpos 0.50 xanchor 0.5
with wipeleft_slow

Claudine "怎么？你不想一起唱吗？"
"我想我没有别的选择。"
"我试着开口唱（真的，我试了），可从嘴里发出的与其说是音乐，不如说是一种含糊不清的咕哝。"
"我竭力压低声音，可克洛蒂娜一定是长了老鹰般的耳朵，因为她还是照样窃笑起来。她居然还能听见我！"
"真丢人……"
"当塞琳弹完一连串音阶、同学们纷纷休息时，克洛蒂娜不怀好意地朝我微微一笑。"
show claudine smirk2 with dissolve
Claudine "你唱得可不怎么样，是不是？"
Marcel shy u "不、不怎么会，没……"
show claudine laugh2 with dissolve
Claudine "哎呀，哎呀。你简直快跟可怜的米拉贝尔一样糟了！这可真是了不起的成就呢！"

show mirabel shock:
    xpos 1.10 ypos 0.5 xanchor 0.5 yalign 0.5
    ease 1.0 xpos 0.90

"闻听此言，米拉贝尔的脸涨得通红。我为她感到难过，可我还没来得及问她是否安好，克洛蒂娜便继续向我发问。"

show mirabel:
    ease 1.0 xpos 1.10

$ renpy.pause(0.5)

hide mirabel
show claudine neutral2
with dissolve

Claudine "难道巴黎的学校不教音乐吗？我还以为他们一定教的。我以为你会每天至少练上那么一个钟头，伴奏也比这架旧钢琴体面得多呢！"
Marcel neutral u "嗯……"
"我在以前的学校从未受过音乐教育。老师们过分偏重于他们认为实用的科目，比如数学、科学和古典文学。相比之下，音乐被视作女性才钻研的玩意儿；简直一文不值。"
"我这辈子从未唱过歌。"
"即便我拥有一副像克洛蒂娜那样清亮甜美的嗓子，我也因为毫无经验而完全找不着调。"
"不过，我实在难以对克洛蒂娜坦承这些。"
Marcel sad u "我们确实学过音乐，可我从来就不怎么在行。我以前的音乐老师说我嗓子又粗又笨。她说要是我在别的姑娘上头乱哼，对她们可不公平。"
"至少，这番话有一部分是实情。从前那些老师，即便明知我答得上来，课堂上也不再向我提问，因为我的嗓音常常引得同窗们踢我的椅背，或是朝我丢东西。"
"若是大家索性假装我不存在，对谁都要省心得多。"
Claudine "唔……所以是有人叫你别唱喽？"
Marcel sad u "或者干脆别开口说话。"
show claudine annoyed2 with dissolve
Claudine "真不公平！我知道淑女应当只被看见、不被听见，可这也太过分了……！"
show claudine neutral2 with dissolve
Claudine "也许巴黎的学校说到底也没有那么好吧。"
Marcel "我其实并不喜欢那儿，没有……"
Claudine "可你别的科目呢？缝纫呢？神学呢？礼仪呢？还有芭蕾呢？"
show claudine shock2 at bounce
Claudine "你{i}肯定{/i}学过芭蕾的吧，对不对？你一定学过！"
"一想到像我这样的人竟要去学跳舞，我便窘迫得无地自容，脸颊也涨得通红。"
Marcel shy u "我芭蕾也一直不太行。我太高了，又笨手笨脚……"
show claudine neutral2 with dissolve
Claudine "噢，真可惜。我可是很想去跳芭蕾呢！"

stop music fadeout 1.0

show claudine neutral2:
    ease 1.0 xpos 0.25 xanchor 0.5

show luce frown2:
    xzoom -1 xpos 1.20 ypos 0.5 xanchor 0.5 yalign 0.5
    ease 1.4 xpos 0.75

$ renpy.pause(0.8)

play music "bgm/Comedy.ogg" fadein 1.0

Luce "那是因为你受不了自己不是众人瞩目的焦点。"
"整节课都沉默不语的露丝——我不确定她是否费心唱过一句——突然开口，声音是冷冷平平的语调。"
"她的神情冷若冰霜，可克洛蒂娜依旧笑了起来。"
show claudine laugh2 with dissolve
Claudine "那当然喽！你可真懂我，露丝！"
show luce sigh2 with dissolve
Luce "可惜是呀……"
show claudine shock2 with dissolve
Claudine "天哪，你可{i}真{/i}冷淡！你从来不肯跟我多说两句，除非有什么刻薄话要说！"
show luce frown2 with dissolve
Luce "你对米拉贝尔很刻薄。你糟蹋了她的歌声……"
Luce "刚才你还说她蠢。"
show claudine smile2 with dissolve
Claudine "哎呀，哎呀。那些话你都听见了？"
Luce "我想不听都不行，你实在太吵了。"

scene musicroom
show claudine smile:
    xpos 0.25 xanchor 0.5

show luce frown:
    xzoom -1 xpos 0.70 xanchor 0.5

show mirabel shock:
    xpos 1.10 ypos 0.5 xanchor 0.5 yalign 0.5
    ease 1.4 xpos 0.85
with dissolve

Mirabel "露、露丝……！"
"米拉贝尔急忙插嘴，脸颊泛起鲜艳的粉色。"
show mirabel shy with dissolve
Mirabel "你不用替我出头。我、我很感激，可我是全班年纪最大的。我应当能照顾好自己的！"
show luce neutral with dissolve
Luce "你应当是能，没错，可你做不到。"
show luce sigh with dissolve
Luce "你就是没救了。"
show mirabel shock with dissolve
Mirabel "没救了，她这么说……"
"米拉贝尔往后一缩，肩膀耷拉了下来。"
show mirabel sad with dissolve
Mirabel "我、我猜你这话说得没错。我还有很多要学的呢。"
show claudine neutral with dissolve
Claudine "哟，这又是怎么了？"
"克洛蒂娜挑起一根眉毛。"
Claudine "你这是在替米拉贝尔说话呢，露丝，还是也想损她两句？我真是看不透你！"
show luce neutral with dissolve
Luce "我只是在说最近一直盘桓在我心头的话罢了。米拉贝尔有她的毛病，可你也有。"
show luce frown with dissolve
Luce "你老是欺负比你弱的人。我真希望你别这样。这让人很不舒服。"
show claudine laugh with dissolve
Claudine "要是换了别人，我兴许还会被这句话惹恼，可你那话实在让人严肃不起来。你又小又可爱，露丝！"
"克洛蒂娜笑着，揉乱了露丝那头金色小脑袋上的头发。"
show luce annoyed with dissolve
"露丝撅起嘴，想推开克洛蒂娜的手，可克洛蒂娜比她力气大，纹丝不动。"
"露丝咬紧牙关，眉头紧锁。"
Luce "你难道不懂得怎样真心实意地夸人吗？"
show claudine smile with dissolve
Claudine "我更爱在话里掺上几分刻薄，这样才免得人们得意忘形。"
Claudine "不过说句实话，我倒觉得玛塞尔真该跟我们米拉贝尔学个一两手，哪怕她唱得五音不全！"
show mirabel shock at bounce
Mirabel "学什么呀？！"
Claudine "那就是，哪怕你在某件事上缺了天分，也不该就那么轻易放弃。"
Claudine "你唱歌是真差，米拉贝尔。你是我这辈子听过最糟的女歌手，可就算你有那么多、{i}那么多{/i}毛病，你还是不肯放弃。从某种角度说，这几乎让人佩服。"
"克洛蒂娜把手从露丝头上移开——露丝皱着脸，重新整理头发——然后看向我。"
show claudine neutral with dissolve
Claudine "有些人无论怎么努力，有些事就是做不好，可如果你不{i}一直{/i}试下去，你永远不会知道自己到底有没有长进的本事。"
Claudine "学学米拉贝尔的样子，别这么放不开。"
show claudine smile with dissolve
Claudine "你才刚来米延，玛塞尔。这正是你全新人生的开端，你不该糟蹋了它。别在城里那副模样在这里行事。"
show claudine laugh with dissolve
Claudine "就算唱得不好也要唱！就算摔跤也要试着练你的芭蕾！"
Claudine "顶撞一下老师，被狼狈地赶出教室，怎么样？那可真有意思得很！"
show luce neutral with dissolve
Luce "这可真是糟糕的建议。"
show luce sigh with dissolve
Luce "你今天就够顽劣的了，克洛蒂娜，我倒吃惊你怎么还没被赶出教室。"
show claudine smirk with dissolve
Claudine "那一定是因为我长得好看！"

show claudine:
    ease 0.8 xpos 0.35

show noemie frown:
    xpos -0.18 xanchor 0.5
    ease 1.6 xpos 0.13 ypos 0.5 xanchor 0.5 yalign 0.5

$ renpy.pause(0.6)

Noémie "那肯定不是因为你谦虚。你从来就没有过那种东西。"
"诺艾米翻了个白眼，克洛蒂娜笑了起来。"
show claudine smile with dissolve
Claudine "你就尽情地活吧，玛塞尔。去做那些你一直想做、却从没机会做的事。这样一来，你的人生就一定会变得非常特别！"
show claudine laugh with dissolve
Claudine "就算是米延也能很美。你只需要有正确的心境！"
"而克洛蒂娜的笑灿烂到连我都几乎要信了她。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
play music "bgm/Classroom.ogg" fadein 1.0
$ save_name = (__("{u}序章{/u}{vspace=1}  9月16日{vspace=1}  选择搭档") )
scene classroom
show paulette neutral at center
with wiperight_slow
window show dissolve

"我们今日的最后一门课是英语。这堂课在大教室上进行，可老师并非布吕吉埃夫人，而是一位个子娇小、身材纤细、留着浅金色头发的女子。"
"她看起来更像学生，而非老师。这位女子与我们这帮学生唯一的区别，便是她的衣着。"
Te "打扰一下……"
"她站在教室前方，紧张地打量着我的同窗们。"
show paulette sad at twirl
Te "呃，打扰一下……？"
"全班无人理会她。她们依旧轻松地谈笑；女孩们转过身坐在椅上，回头瞥着身后的人。"
"我困惑地看向坐在身旁的克洛蒂娜。"

scene classroom:
    size (1920, 1080) crop (0, 40, 1440, 810)
show claudine smile2:
    xpos 0.30 xanchor 0.5 ypos 0.55 yanchor 0.5
with wipeleft_slow

Marcel neutral u "那是谁？"
Claudine "哦，对了。你还不认识她吧？那是杜布瓦夫人！"
Marcel "杜布瓦……"
"布吕吉埃夫人昨天跟我说起过那位不幸的杜布瓦夫人。她说她不在时把学校交给了杜布瓦夫人打理，而她本人则到巴黎来与我和母亲谈话。"
"我记得布吕吉埃夫人说过，杜布瓦夫人并不擅长管束课堂。她还提到过这位夫人说话轻声细语。"
"现在我总算是亲眼见识到了。"
Marcel frown u "她的课一直是这样吗？"
show claudine laugh2 with dissolve
Claudine "一直如此。没人肯理会她半分。她的存在感比教堂里的老鼠还不如！"
show claudine neutral2 with dissolve
Claudine "有时候，我简直有点可怜那位可怜的人儿……"

show celine frown2:
    xpos 1.10 xanchor 0.5 ypos 0.55 yanchor 0.5
    ease 1.5 xpos 0.70

Celine "你要是真觉得她可怜，克洛蒂娜，就不会总是把局面弄得这么难堪。"
show claudine shock2 with dissolve
"克洛蒂娜眨了眨睫毛，装出一副全然不解的模样。"
Claudine "谁，我吗？"
show celine sigh2 with dissolve
Celine "{i}就是{/i}你。你总在她的课上讲话，从来不肯记笔记！你连试都不试。"
show claudine neutral2 with dissolve
Claudine "我或许可怜那位可怜的女人管不住一个班，塞琳，可那并不意味着我就得低声下气地去讨好她。"
Celine "你当然不会。你压根儿就不肯弯一弯腰。你这人倔得很……"
show claudine laugh2 with dissolve
Claudine "我准是从我那位可敬的爸爸那儿遗传来的！"
show celine frown2 with dissolve
Celine "请别在一群正经淑女面前提起你的爸爸。"
show claudine shock2 at bounce
Claudine "哼？真有意思。我是很想听你的劝，塞琳，可我在这屋里看不到哪个正经淑女值得我操心呀！"
show celine annoyed2 with dissolve
Celine "你、你好大的胆子……？！"
show claudine laugh2 with dissolve
Claudine "我胆子是大着呢——说实话，大得很。好啦，还是放松点吧，塞琳，要不你那漂亮脸蛋就要起皱纹了！"

scene classroom
show paulette sad at center
with wiperight_slow

Dubois "同学们，请安静一下……"
"与此同时，杜布瓦夫人仍在恳求全班安静下来。"
"她不似布吕吉埃夫人那样发号施令。她的声音里没有果决，也没有相信自己真能让所有人静下来的底气。她听起来像是走投无路。"
"说实话，这叫人不免得有些难安。看她手足无措、焦急地忙碌，我替她感到难堪。"
"我想，倘若我也当老师——我可不想当，这听起来是个吃力不讨好、薪水又低得可怜的差事——那我大概也会像杜布瓦夫人一样：安静、羞涩、不敢坚持己见。"

scene classroom:
    size (1920, 1080) crop (0, 40, 1440, 810)
show claudine smile2:
    xpos 0.30 xanchor 0.5 ypos 0.55 yanchor 0.5
show celine sigh2:
    xpos 0.70 xanchor 0.5 ypos 0.55 yanchor 0.5
with wipeleft_slow

Celine "你们这些乡下丫头为什么非要嚷得这么大声？上课五分钟前就该开始了，我都开始头疼了。"
show claudine smirk2 with dissolve
Claudine "你管我们叫乡下丫头，塞琳，可你如今在乡下也住得够久了。你那宝贝的奥尔良早就远在你身后啦！"
show celine sad2 with dissolve
Celine "而我每天都在懊悔这件事。"
show celine neutral2 with dissolve
Celine "奥尔良也许吵嚷了些，可那里的人起码懂得基本的规矩。他们不会这样打断长辈和体面人说话。"
show claudine annoyed2 with dissolve
Claudine "噢，得了吧。你难道真以为杜布瓦夫人就比我们强，仅仅因为她比我们多活了那么几岁？"
Claudine "要是她管不住自己的班，那也就没有理由让我敬重她——不过我也承认，我确实可怜她。"
show claudine neutral2 with dissolve
Claudine "她简直就像个长不大的女学生——不过这个词恐怕用得不妥，毕竟我比她还高呢！"
Claudine "一个如此苍白、乏味、无趣的人，怎能指望指使我该做什么呢？"
show celine frown2 with dissolve
Celine "你是{i}谁{/i}的话都不爱听。你就像一头还没驯服的小马驹。我可爱的埃托瓦勒在受过充分调教之前，也是这副德性。"
show claudine smirk2 with dissolve
Claudine "哎呀！这么说你是打算驯服我喽，塞琳？"
show celine sigh2 with dissolve
Celine "有时候我倒是想，可那多半是自找麻烦，得不偿失。"
Claudine "哈！我倒要看看你试试看！"
Celine "别来招惹我。"
"塞琳叹了口气，用指尖揉按着头皮。"

# chatter?
show image "border" onlayer border
scene classroom:
    subpixel True
    size (1920, 1080) crop (0, 300, 1280, 720)
    linear 25.0 crop (350, 300, 1280, 720)
with wiperight_slow

"喧闹声铺天盖地地涌来，其间夹杂着杜布瓦夫人那悲戚的整顿纪律的呼喝。"
Cla "不知道我们什么时候才会有新的音乐老师……"
Claa "我们好久都没有一位真正的老师了！"
Claaa "塞琳钢琴弹得不错，可她毕竟比不上勒梅尔小姐。"
"塞琳朝那些闲聊说笑的女生方向瞪了一眼。"
Celine frown "因为我和勒梅尔小姐不同，绝不会跟一个政客私奔，逃到兰斯去？"
"那帮叽叽喳喳的女孩脸红了。她们低下头，看着交叠在课桌上或膝头的手，局促地咯咯直笑。"
Cla "噢，我们可不是要冒犯你，塞琳！"
Claa "我们觉得你的钢琴弹得很好，真的！"
Claaa "我们只是盼着布吕吉埃夫人能请一位造诣深厚的音乐老师，一位真正有经验的！"
Cla "没错！自从勒梅尔小姐走了，我们的音乐课可就落下好多了。"
Cla "要是学校合唱团能重新组建起来就好了。"
Claa "噢，是啊！我好喜欢跟勒梅尔小姐一起在合唱团唱歌！"
Claa "我们甚至在圣诞期间到当地的教堂里演出过呢！"
Claaa "我真希望合唱团没有被解散……"
Cla "你不能去请布吕吉埃夫人把合唱团恢复起来吗，塞琳？我们这么多人可都那么喜欢它！"
Celine huh "我可以试试，可布吕吉埃夫人对音乐一窍不通，我又不知道该怎么指挥你们。我只会弹钢琴。"
Claaa "那我们只好等着新的音乐女教师了……也许是一位男教师……？"

hide image "border" onlayer border
scene classroom:
    size (1920, 1080) crop (350, 40, 1440, 810)
show mirabel shock2:
    xpos 0.70 xanchor 0.5 ypos 0.55 yanchor 0.5
with wipeleft_slow

Mirabel "什么？"
"米拉贝尔瞪大眼睛，盯着那个刚开口的女生——一个一头赤红头发的姑娘。"
Mirabel "你真觉得布吕吉埃夫人会请一位先生吗？"
Cla "凡事都有可能，不是吗？"
show mirabel at bounce
Mirabel "可这所学校从来不许男人进来，只有政府官员例外，而且一年才一次！"
show mirabel shy2 with dissolve
Mirabel "我们从来没见过男老师……"
Cla "凡事都有头一回嘛！"
Claa "要是布吕吉埃夫人找不到一位还算像样的女士来当我们音乐老师，她就只好退而求其次，请位先生来喽！"
Claaa "你能想象吗？我们学校里有位先生？！"
"我的同窗们兴奋地尖叫起来。与此同时，米拉贝尔的脸色变得苍白。"
show mirabel scared2 with dissolve
Mirabel "我可不想去想象那种事。我甚至不知道自己能不能想象！男人好可怕……"

show noemie smirk2:
    xzoom -1 xpos -0.20 ypos 0.55 yanchor 0.5 xanchor 0.5
    ease 1.8 xpos 0.35

Noémie "你嘴上这么说，可我们都知道你有多黏你爸爸，米拉贝尔。"
show mirabel shock2 at bounce
Mirabel "那、那不一样！我爸爸就是我爸爸！他是个善良的好人，我的小弟弟也是……"
Mirabel "虽说他还算不上是个男人吧。"
show mirabel sad2 with dissolve
Mirabel "不过别的男人，我可就不敢这么说了。"
Noémie "那是因为你根本不认识别的男人，傻瓜。"
show noemie frown2 with dissolve
"坐在教室最末排的诺艾米，朝米拉贝尔的后脑勺弹出一枚墨团——不出所料，米拉贝尔尖叫一声，举起双手护住自己的头发。"
Noémie "你要是跟我父母雇的那些男人说过话，就不会这么说了。就拿费利克斯来说吧，他可是位十足的绅士。"

play sound "sfx/footsteps3.ogg" fadein 0.5
show mirabel:
    ease 0.8 xpos 0.80
show noemie:
    ease 1.2 xpos 0.55
show claudine smirk2:
    xpos -0.20 xanchor 0.5 ypos 0.54 yanchor 0.5
    ease 1.6 xpos 0.20

$ renpy.pause(0.6)
stop sound fadeout 0.5

Claudine "一位对你毫无兴趣的十足绅士，对吧，诺艾米？"
show noemie mad2 with dissolve
Noémie "闭、闭嘴。"
"这一次，诺艾米把墨团弹向了克洛蒂娜。"
"然而，克洛蒂娜的反应远比米拉贝尔敏捷，她及时抬起英语书，将那墨团挡了下来。"
show noemie frown2 with dissolve
Noémie "这跟你没关系，克洛蒂娜。你根本不知道自己在说什么。"
show claudine laugh2 with dissolve
Claudine "这么说，你是想说你还不是仍旧为你那位英俊王子抛弃了你而耿耿于怀喽？"
show noemie shock2 with dissolve
Noémie "我、我才{i}没有{/i}被抛弃！"
"一股愤怒的红晕在诺艾米苍白的脸上蔓延开来。我不太明白这是为什么，可也没机会发问——即便有，我也不会问。我的同窗们仍在为她们幻想中的钢琴家而神魂颠倒。"
Cla "噢，我真希望布吕吉埃夫人请一位男音乐老师！那该是多么新鲜的变化呀！"
Claa "你觉得他会是个英俊的男人吗，方方的下巴，眼神严肃？"
Claaa "也许深色头发，神情忧郁，仿佛藏着什么秘密似的……"
Cla "噢，对！玩音乐的男人总有些不可告人的秘密！"
show mirabel shock2 at bounce
Mirabel "真、真的是这样吗？"
Cla "当然啦！懂音乐的男人总是那种沉默寡言、又爱沉思的类型！那种男人比谁都更需要疼爱，不过他们迟早都会敞开心扉，展现出甜蜜的内心！"
show noemie frown2 with dissolve
Noémie "“敞开心扉”？"
"诺艾米稍稍恢复了镇定，嗤之以鼻。"
Noémie "你这是在说男人，还是在说牡蛎？"
show claudine laugh2 with dissolve
Claudine "我敢说米拉贝尔对这两样都很有经验！"
"我的同窗们笑得前仰后合，全都沉浸在自己的遐想里，激动不已。"

show image "border" onlayer border
scene classroom:
    subpixel True
    size (1920, 1080) crop (0, 300, 1280, 720)
    linear 25.0 crop (350, 300, 1280, 720)
with wiperight_slow

"看到一群女孩如此沉迷于她们的幻想，我觉得颇为古怪。"
"我大半辈子都与男人为伴，从未觉得他们有什么值得兴奋的地方。"
"事实上，对我来说，他们是我拼命想要逃离的存在。"
"我在寄宿学校所遇见的男人——包括老师和校长在内——身上没有一丝一毫的柔情。"
"宿舍里那些安静、阴郁、满怀愁绪的男孩，总是格外被其他人挑出来欺弄，我自己也在其中。"
"这些女孩说起话来，仿佛这辈子从未见过男人似的——不过我想，这或许也差不了多少。"
"这些女孩大多在米耶纳的这座乡村小校读了多年书。她们从没有过男老师，也没有过男同学。"
"她们所交谈过的男人，恐怕也只有自己的父亲、叔伯舅舅，或是表亲。"
"或许这就是为何一想到能见到异性，她们便如此兴奋。"
"我不禁好奇，若她们知道自己身边已有一位男子，会说些什么？她们会眼放光芒地围住我问个不停，还是嫌恶地退避三舍？"
"我全然不像她们那位头发乌黑、眼神忧郁的梦幻音乐老师。我的下颌线条并不硬朗，头发是浅色的，而我的双手虽然纤细，却连救命的调子也哼不出来。"
"我敢肯定，若她们得知真相，必定会大失所望。"

hide image "border" onlayer border
scene classroom:
    size (1920, 1080) crop (0, 40, 1440, 810)
show claudine smile2:
    xpos 0.30 xanchor 0.5 ypos 0.55 yanchor 0.5
with wipeleft_slow

Claudine "哎呀，你们这些姑娘呀。"
"我正在琢磨这些事时，克洛蒂娜了然于胸地啧了一声。"
Claudine "你们把男人说得好像多稀罕似的，像钻石珍珠一样，可他们占了全世界整整一半的人口！他们也没那么特别。"
Cla "你说得倒轻巧，谁让你是在你那个古怪的家庭里长大的。"
Claa "你一定又在读你父亲那些古怪的书了。它们把你的男人观都带坏了，克洛蒂娜！"
"什么书？我很好奇，可是……"
show claudine neutral2 with dissolve
Claudine "我看是你们这些姑娘的想法才扭了。"
Claudine "我可是读过许多关于男人的东西，你们知道吗——那些故事里，既有写男人的，也有男人自己写的。"
show claudine smirk2 with dissolve
Claudine "有几段故事，我亲眼读过……！那内容简直要吓得你们头发都竖起来！"
Cla "别这么粗俗，克洛蒂娜。真正的男人才不会写那种故事。"
Claa "说得对！真正的男人温柔、善良，又体贴……"
Claaa "尤其是懂音乐的那种！"
show claudine heh2 with dissolve
Claudine "哦，你们会吓一跳的。男人可以比你们敢想象的还要放荡不羁——而他们对我们这样端庄规矩的姑娘的某些幻想……！"
show claudine smirk2 with dissolve
Claudine "哎呀，连我都差点要脸红了呢！"
"可克洛蒂娜没有脸红。我不确定她是否会脸红，也许是她脸皮太厚了。相反，她咯咯一笑，朝椅背靠去，一条腿叠在另一条腿上。"
"我们的同学都看着她，兴致被勾了起来，不过我怀疑她们并不想承认这一点。"
"我也忍不住好奇地打量着她。她对男人的幻想究竟了解多少……？"
Cla "我不信。你是在编故事。"
Claaa "你总是在编故事，克洛蒂娜。"
Claa "都是因为你父亲！"
show claudine smile2 with dissolve
Claudine "{i}我{/i}才不是编故事的那个人，姑娘们；我只是读故事罢了。"
Claudine "我真的读过很多故事。我能讲些极其不知羞耻的事给你们听！"
show claudine neutral2 with dissolve
Claudine "总之，我觉得男人还是离这所学校远一点的好——尤其是这里的学生有那么多都这么傻。你们啊，简直是送上门去让人摘的果子！"
Claudine "我们需要的音乐老师，有塞琳一位就足够了。"

play sound "sfx/footsteps3.ogg" fadein 0.5
show celine frown2:
    xpos 1.14 ypos 0.55 yanchor 0.5 xanchor 0.5
    ease 1.6 xpos 0.70

$ renpy.pause(0.5)
stop sound fadeout 0.5

Celine "你真的是这么想的吗？"
show claudine laugh2 with dissolve
Claudine "当然是真的！你的钢琴弹得一流，亲爱的塞琳，而且你的嗓音宛如天使！论起音乐，我不信哪个男人能胜过你。"
show claudine smile2 with dissolve
Claudine "如果由你来当我们的老师，而不是哪个手指纤细的登徒子，对姑娘们来说也更安全！"

play sound "sfx/footsteps3.ogg" fadein 0.5
show mirabel neutral:
    xpos 1.10 ypos 0.5 xanchor 0.50 yanchor 0.5
    ease 1.2 xpos 0.90

$ renpy.pause(0.5)
stop sound fadeout 0.5

Mirabel "我、我同意克洛蒂娜的话。这、这所学校是供年轻女子学习的地方。男人不该待在这里！"
Cla "安静点吧，米拉贝尔。没人想听你的意见。除了糕点，你什么都不懂！"
Mirabel "哦，嗯……好、好吧……对、对不起……"

show mirabel sad:
    xzoom -1
with dissolve

$ renpy.pause(0.3)

play sound "sfx/footsteps3.ogg" fadein 0.5
show mirabel:
    ease 1.2 xpos 1.10
$ renpy.pause(0.5)
hide mirabel with dissolve
$ renpy.pause(0.5)
stop sound fadeout 0.5

Claa "我也不见得总乐意听克洛蒂娜的想法！"
Claaa "她把我们说得好象小孩子一样！"
Cla "你觉得我们管不住自己吗？"
show claudine smirk2 with dissolve
Claudine "没错，我正是这么想的。你们都那么渴望被关注，一转眼就会任由别人占了便宜！"
Cla "你、你在说什么？"
Claa "我才没有那么天真！"
Claaa "想、想要经历一场甜蜜而动人的爱情，有什么错吗？"
Claudine "和那位音乐老师……？"
Claa "那又怎么样？！只要他喜欢我，其他的都不重要！"
show claudine laugh2 with dissolve
Claudine "哦，我敢说他当然会喜欢你啦，埃莱娜，谁叫你那么容易轻信别人，又那么笨手笨脚！"
show claudine smirk2 with dissolve
Claudine "幻想老男人的年轻姑娘，跟幻想年轻姑娘的老男人一样可悲，不过我想我也不必对你太苛刻。"
Claudine "{i}他们{/i}本该更自重一些，可你们一个个都被保护得太好，连自己到底想要什么都不知道。"
Claudine "只要别一见到哪个男人敲门就往上扑——也千万别被他们的甜言蜜语哄住了，看在老天爷的份上。你总不想成为他们床头上又一道刻痕吧。"
show celine sad2 with dissolve
Celine "嗯……"
"在克洛蒂娜那番得意洋洋、自鸣得意的话里，塞琳的脸色一点点变白。如今她白得几乎没了血色。"
Marcel frown u "塞琳？"
"我转过头，越过肩膀瞥了她一眼，声音因焦虑而紧绷。"
Marcel sad u "你还好吗……？"
show celine sigh2 with dissolve
Celine "我……我只是有点头晕……"
Marcel "要不要出去透透气？也许我可以去告诉杜布瓦夫人——"
show celine sad2 with dissolve
Celine "哦，不用。你真好心，不过……"
show celine frown2 with dissolve
"塞琳严厉地看了克洛蒂娜一眼。"
Celine "……我想，只要这位卖弄风情的夫人别再炫耀她的学识，我就会觉得好受些。"
show claudine annoyed2 with dissolve
Claudine "哦？"
"克洛蒂娜挺起胸膛。"
Claudine "你说我是卖弄风情的夫人？"
show celine annoyed2 with dissolve
Celine "没错，你就是。才读了一两本书，就以为自己懂得爱情的全部了！"
Celine "你自己根本没谈过恋爱。你只是想炫耀罢了。好吧，我看腻了你这份故作老成的模样。"
Celine "你要是有你装出来的那一半聪明，就该停下这场煽动大家的闹腾，好让我们专心学英语课。照这样下去，可怜的杜布瓦夫人嗓子都会喊哑的，而你们谁都没有在认真听。"
Cla "可是聊男人比英语课有意思多了！"
Claa "多有意思啊！"
Claaa "反正我永远也不会去英国。我才不需要学他们那种蠢话！"
show celine frown2 with dissolve
Celine "所以你们宁愿做个无知的蠢人？"
Celine "或许克洛蒂娜说得对，你们就是这样。"

play sound "sfx/stamp.ogg"
scene classroom
show celine frown:
    xpos 0.5 xanchor 0.5 ypos 0.60 yanchor 0.5
    ease 0.8 ypos 0.54
with dissolve

"于是，带着一副当真叫人无地自容的神情，塞琳站起身来，手掌猛地拍在桌面上。课桌摇摇欲坠地嘎嘎作响，有那么一会儿，我真担心它会散架。"
Celine "大家都请听我说。我们理应是一群姑娘，而不是一群农场的牲口。都别说话了，专心上课吧。"
"塞琳环视教室，目光冷若冰霜。"
"尽管她与学生无异，可她看起来比杜布瓦夫人本人还要像位老师。"
"听了塞琳的话，全班安静了下来。就连克洛蒂娜也噤了声，不过她在闭嘴前还是嘟囔了一句……"
Claudine u annoyed "{size=-5}她还说{i}我{/i}在炫耀！{/size}"

show celine:
    ease 1.0 xpos 0.70

show paulette smile:
    xpos -0.10 xanchor 0.5 ypos 0.5 yanchor 0.5
    ease 1.6 xpos 0.30

$ renpy.pause(0.6)

"杜布瓦夫人感激地望向塞琳，双手交叠在身前。"
Dubois "是、是的，说得对。塞琳说得非常对。谢谢你让大家安静下来。我很感激。"
show celine frown with dissolve
Celine "您不必谢我。您是老师，不是吗？"
show paulette sad at bounce
Dubois "是、是的，那个……"
"听到这番话，杜布瓦夫人的脸泛起红晕。"

show image "border2" onlayer border
scene classroom:
    size (1920, 1080) crop (0, 40, 1440, 810)
show luce smirk2:
    xzoom -1 xpos 0.30 xanchor 0.5 ypos 0.55 yanchor 0.5
with wipeleft_slow

Luce "……呵。"
"我发誓，我能听见教室后方传来一声压抑的、含着笑意的轻哼。"
"我好奇地转过头，寻找那出声的人。我的目光很快落在露丝身上。她坐在教室最右侧，紧挨着窗户。"
"尽管她的目光并没有落在杜布瓦夫人身上——她正望着窗外，看着校园——我还是能看到一丝浅笑牵动她的嘴角。"
"她是因杜布瓦夫人当着自己学生的面出丑而感到高兴吗？"
"我不明白这是为何。"
"我从不觉得露丝有几分施虐的癖好……可话又说回来，关于露丝，我不了解的事情太多了。"
"我在这所学校连一整天都还没待满，这些同学对我来说仍是谜一般的人物。回头我应该试着多了解她们一些。那样的话，说不定我还能交到几个朋友。"

hide image "border2" onlayer border
scene classroom
show paulette neutral at center
with wiperight_slow

Dubois "那么，同学们，我们今天要学习助动词。请大家把注意力集中到教室前方……"
"被塞琳训斥得噤了声，全班温顺地听从杜布瓦夫人的吩咐。我们齐刷刷望向黑板，杜布瓦夫人正用大而圆润的字迹在上面写着几个单词。"
"{i}能。{/i}"
"{i}会。{/i}"
"{i}将。{/i}"
"我认得这些词，尽管它们是外文。我在以前的学校专门钻研过英语。"
"虽然我学业上从不擅长——上课时我紧张又紧绷，满心只担心纸团或是乱伸的脚踢到我的椅背，根本没法专心——但助动词应该难不倒我……"
show paulette smile with dissolve
Dubois "那么，请姑娘们试着用这些词来造句……"
"事实上，这课对这一群十几岁的姑娘来说，似乎太简单了些。她们难道不该早就学会了吗？"
"克洛蒂娜似乎也这么认为，因为她响亮地打了个哈欠，甚至懒得用手掩一下。"
"杜布瓦夫人的肩膀僵住了。"
show paulette frown with dissolve
Dubois "怎么了，克洛蒂娜？有什么问题吗？"
Claudine u annoyed "哦，没有，夫人，{i}没有{/i}什么困扰我。问题恰恰就在这里。这堂课实在是太简单了！"
Claudine "如果您想让我认真听讲，就该给我一些更难的题目。不然的话，我可能会趴在桌上睡着，那样我可就要把我这一头漂亮的头发弄乱啦！"
"我们的同学们在克洛蒂娜那句大胆的宣告后窃笑起来。与此同时，染在杜布瓦夫人脸上的红晕越发深了。"
show paulette sad with dissolve
Dubois "如果你真这么累，克洛蒂娜，也许出去活动活动腿脚比较妥当。我可不想你昏倒。"
Claudine u smile "哦？那么您有什么建议呢，夫人？"
show paulette frown with dissolve
Dubois "你何不到外面的柴棚去，给我们拿些柴火来？天色已晚，天也开始变冷了。"
Claudine u annoyed "哦，不要，夫人，我{i}一点{/i}兴趣都没有！要是我得搬木头，我手指头一定会扎进木刺！那样的话，我就再也弹不了钢琴啦！"
Mirabel shock "什、什么？我都不知道你会弹钢琴！"
Celine sigh "她当然不会。这又是她那些瞎编的蠢话。"
Claudine u smile "哎呀，你好爱挑刺啊！"
Claudine "我想我已经说过了，塞琳，我不编故事，我只是读故事而已。"
Celine "我倒觉得你读的故事未免太多了……"
show paulette mad at bounce
Dubois "要、要是你扎了木刺，那也是你抱怨太多的咎由自取。至少那能让你清醒清醒！"
"杜布瓦夫人竭力让自己的语气显得笃定，可当她的目光碰上克洛蒂娜的视线时，声音还是发颤了。"
"而克洛蒂娜则一副完全不在意的模样。相反，她朝椅背靠去，骄傲地微笑着，漫不经心地卷着一缕发丝绕在指间。"
Claudine "可是夫人，我{i}实在{/i}没法一个人搬回足够生火的柴火。我至少得跑上两趟，那会更耽误您的课的！"
Claudine "如果您非要让我承担这么麻烦的差事，那至少总该允许我找个同伴吧？"
show paulette neutral with dissolve
Dubois "嗯……"
"杜布瓦夫人犹豫了片刻。也许她认为附和克洛蒂娜会削弱自己的威信，可她想必也该明白，在这间教室里，她本就没什么威信可言。"
"无论如何，克洛蒂娜确实言之有理。尽管她这番逻辑是出于私心，却也让人难以反驳。"
Dubois "好吧。你可以带个同伴。带上露丝。"
Luce frown "什么……？"
"一直望着窗外的露丝抬起头来，皱了皱眉。"
Luce "为什么要我？"
show paulette frown with dissolve
Dubois "你要是刚才用心听讲，我就用不着跟你解释这些了，露丝。克洛蒂娜要去柴棚。你必须跟她去。"
Luce "可我为什么非去不可？"
Dubois "因为是我说的。"
Luce "可我又没做错什么。"
show paulette mad with dissolve
Dubois "别提什么做错事；你根本什么事都不做！上我的课时，你总是望着窗外出神，呆头呆脑的！"
Dubois "好吧，或许这能让你学会稍微专心一点。"
Luce neutral "可是——"
Claudine u smile "冒昧地说一句，夫人，我想这次跑腿或许让那位新来的姑娘陪我去更好。"
show paulette neutral with dissolve
Dubois "什么新来的姑娘？"
Marcel shy u "嗯……"
"我尴尬地在椅子上动了动身子。"
"杜布瓦夫人难道没注意到我吗？以我的身高，我真想不通她怎会没看见。也许她是太忙于试图管住她那班学生——又管不住——才把我给忘了。"
Marcel neutral u "我是新来的学生，夫人。我叫玛塞尔·雷诺。"
show paulette frown with dissolve
Dubois "玛塞尔……？"
Claudine u laugh "您为何一脸困惑？难道您不知道今天会有位新学生来吗？您是我们的老师，总该知道的呀！我真不敢相信，像您这样有身份的人，居然会犯下这么大的疏忽！"
show paulette sad at bounce
Dubois "不，不是那个……"
"杜布瓦夫人的脸又一次涨红了，她连忙否认克洛蒂娜那番刻薄话里任何真实的成分。接着她上下打量着我，脸上是茫然不解的神情。过了好一会儿，她才终于恍然大悟。"
"等她明白过来，她眨了眨眼。"
show paulette neutral with dissolve
Dubois "啊。我想我现在记起你了。你就是布吕吉埃夫人提起的那位新学生，对吧？"
Marcel neutral u "是的，没错。"
show paulette frown with dissolve
Dubois "真奇怪。她写信给我的时候，我还以为你会比现在更年轻些。"
Dubois "像你这样年纪的姑娘转学可不多见；尤其是在接受正规教育的最后一年。这难道不会影响你的学业吗？"
Marcel sad u "确实有些影响，但医生让我为了健康搬到米耶讷去。除此之外别无他法。"
show paulette neutral with dissolve
Dubois "为了健康，是吗……？"
show paulette sigh with dissolve
Dubois "嗯，那与我无关。"
Luce frown "身为所谓的教育者，我想学生的福祉{i}就是{/i}您该关心的事。"
show paulette frown with dissolve
Dubois "住口，露丝。我不许你顶嘴。"
Luce "可是别的姑娘也顶撞您，您从不责罚她们。"
show paulette mad at bounce
Dubois "那、那是另一码事！"
"杜布瓦夫人怒目而视。她整个身子从头到脚都在颤抖，压抑着未说出口的怒火。"
"我不明白为什么偏偏是露丝让杜布瓦夫人如此恼火。与我们其他同学不同，她压根儿就没说话。我想不出她被单独挑出来的理由，除非我们这位英语老师与她有什么仇怨。"
show paulette neutral with dissolve
Dubois "那么，我想我接受克洛蒂娜的提议吧。"
Dubois "既然是位新来的姑娘，让玛塞尔小姐去取柴火，也许比你去更合适。这确实能帮她熟悉一下学校的环境，也能打消她在巴黎生活养出的那股娇气。"
show paulette frown with dissolve
Dubois "在这所学校，无论我们来自何处，都必须辛勤努力。没有谁高贵到可以不用弄脏手、弄脏裙子。你可记住了，玛塞尔小姐？"
Marcel shy u "是的，我明白了，夫人。"
Claudine u smile "如果您愿意，我可以带玛塞尔四处看看，不过我想，或许让她自己挑个同伴会更好。要是能跟一个她信任的人配合，她取柴火大概会更快吧！"
show paulette neutral with dissolve
Dubois "这确实有道理，嗯。你说得很有道理，克洛蒂娜。"
"就这样，克洛蒂娜轻而易举地摆脱了本应因抱怨而受到的惩罚。"
"杜布瓦夫人似乎压根儿没意识到自己是被如何作弄的。"
"克洛蒂娜说她弹过几年钢琴。我不确定她说的是不是实话，可即便她不会演奏任何乐器，她也深知如何操纵人心。"
show paulette frown with dissolve
Dubois "那么，玛塞尔，你去柴棚取些柴火来。然后我们就可以生火了，兴许这股暖意能让我的姑娘们更专心听讲。有谁是你想请来作伴的吗？"
Marcel frown u "嗯……"
"我疑惑地环视教室，可除了米拉贝尔，我的同窗们似乎都巴不得避开我的目光。"
"交朋友的事算是泡汤了。她们仿佛根本不愿与我扯上任何关系。"
"可我还是得挑一个人。我总不能叫杜布瓦夫人一直等着。"
"我该选谁呢？"

$ achievement.grant("picking_a_partner")

window hide dissolve

menu:
    with dissolve

    "克洛蒂娜":
        jump Claudine_route
    "露丝":
        jump Luce_route
    "米拉贝尔":
        jump Mirabel_route
    "塞琳":
        jump Celine_route

label luce_credits:

# change this to romance theme, probably...
play music "bgm/Luce.ogg" fadein 2.0
$ renpy.pause(1.0)

scene countryside_n
show overlay2
with slow_dissolve

$ renpy.pause(0.5)

show logo:
    subpixel True
    size (1920, 1080) crop (0, 50, 1920, 1080)
    linear 12.0 crop (0, -350, 1920, 1080)
with slow_dissolve

$ renpy.pause(5.0)

hide logo with slow_dissolve

$ renpy.pause(0.5)

show cg1_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}剧本{/u}{/font}{/size}{vspace=1}{size=+10}ebi-hime{/size}{vspace=20}{size=+30}{u}{font=fonts/NotoSansSC-VF.ttf}程序{/font}{/u}{/size}{vspace=1}{size=+10}ebi-hime{/size}{/color}")):
    size (1920, 1080) crop (-1150, -220, 1920, 1080)
    linear 10.5 crop (-1150, -500, 1920, 1080)
with slow_dissolve

$ renpy.pause(8.0)

hide cg1_cred
show cg8_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}角色立绘{/u}{/font}{/size}{vspace=1}{size=+10}Drulle11{/size}{vspace=20}{size=+30}{u}{font=fonts/NotoSansSC-VF.ttf}背景美术{/u}{/size}{/font}{vspace=1}{size=+10}Background TK{/size}{/color}")):
    size (1920, 1080) crop (-1150, -220, 1920, 1080)
    linear 10.5 crop (-1150, -500, 1920, 1080)
with dissolve

$ renpy.pause(8.0)

hide cg8_cred
show cg9_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}界面{/u}{/font}{/size}{vspace=1}{size=+10}ds sans{/size}{vspace=20}{size=+30}{u}{font=fonts/NotoSansSC-VF.ttf}字体{/font}{/u}{/size}{vspace=1}{size=+10}Lato{vspace=1}Magnolia{vspace=1}Raleway{/size}{/color}")):
    size (1920, 1080) crop (-1240, -180, 1920, 1080)
    linear 10.5 crop (-1240, -450, 1920, 1080)
with dissolve

$ renpy.pause(8.0)

hide cg9_cred
show cg10_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}音乐{/u}{/size}{/font}{vspace=1}{size=+10}CrysetBase{/size}{vspace=20}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}音效{/u}{/font}{/size}{vspace=1}{size=+10}Pond5{vspace=1}Sounddogs{/size}{/color}")):
    size (1920, 1080) crop (-1180, -220, 1920, 1080)
    linear 10.5 crop (-1180, -500, 1920, 1080)
with dissolve

$ renpy.pause(8.0)

hide cg10_cred
show cg11_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}校对{/u}{/font}{/size}{vspace=1}{size=+10}Kuroneko{vspace=1}Marantana{vspace=1}Saryana{vspace=1}Xolf{/size}{/color}")):
    size (1920, 1080) crop (-1180, -280, 1920, 1080)
    linear 10.5 crop (-1180, -600, 1920, 1080)
with dissolve

$ renpy.pause(8.0)

hide cg11_cred
show cg12_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}引擎{/u}{/size}{/font}{vspace=1}{size=+10}Ren’py{/size}{/color}")):
    size (1920, 1080) crop (-1270, -340, 1920, 1080)
    linear 10.5 crop (-1270, -640, 1920, 1080)
with dissolve

$ renpy.pause(6.5)
hide text
hide cg12_cred
show text (_("{color=#ffffff}{size=+40}{font=fonts/NotoSansSC-VF.ttf}感谢您的阅读！{/font}{/color}")) at truecenter
with dissolve

$ renpy.pause(10.0)

hide text
with slow_dissolve

$ renpy.pause(1.0)

stop music fadeout 2.0
scene white
with slow_dissolve

return

#######################################################

label mira_credits:

# change this to romance theme, probably...
play music "bgm/Night.ogg" fadein 2.0
$ renpy.pause(1.0)

scene countryside_n
show overlay2
with slow_dissolve

$ renpy.pause(0.5)

show logo:
    subpixel True
    size (1920, 1080) crop (0, 50, 1920, 1080)
    linear 12.0 crop (0, -350, 1920, 1080)
with slow_dissolve

$ renpy.pause(5.0)

hide logo with slow_dissolve

$ renpy.pause(0.5)

show cg32_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}剧本{/u}{/font}{/size}{vspace=1}{size=+10}ebi-hime{/size}{vspace=20}{size=+30}{u}{font=fonts/NotoSansSC-VF.ttf}程序{/font}{/u}{/size}{vspace=1}{size=+10}ebi-hime{/size}{/color}")):
    size (1920, 1080) crop (-1150, -220, 1920, 1080)
    linear 10.5 crop (-1150, -500, 1920, 1080)
with slow_dissolve

$ renpy.pause(8.0)

hide cg32_cred
show cg14_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}角色立绘{/u}{/font}{/size}{vspace=1}{size=+10}Drulle11{/size}{vspace=20}{size=+30}{u}{font=fonts/NotoSansSC-VF.ttf}背景美术{/u}{/size}{/font}{vspace=1}{size=+10}Background TK{/size}{/color}")):
    size (1920, 1080) crop (-1150, -220, 1920, 1080)
    linear 10.5 crop (-1150, -500, 1920, 1080)
with dissolve

$ renpy.pause(8.0)

hide cg14_cred
show cg15_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}界面{/u}{/font}{/size}{vspace=1}{size=+10}ds sans{/size}{vspace=20}{size=+30}{u}{font=fonts/NotoSansSC-VF.ttf}字体{/font}{/u}{/size}{vspace=1}{size=+10}Lato{vspace=1}Magnolia{vspace=1}Raleway{/size}{/color}")):
    size (1920, 1080) crop (-1240, -180, 1920, 1080)
    linear 10.5 crop (-1240, -450, 1920, 1080)
with dissolve

$ renpy.pause(8.0)

hide cg15_cred
show cg16_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}音乐{/u}{/size}{/font}{vspace=1}{size=+10}CrysetBase{/size}{vspace=20}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}音效{/u}{/font}{/size}{vspace=1}{size=+10}Pond5{vspace=1}Sounddogs{/size}{/color}")):
    size (1920, 1080) crop (-1180, -220, 1920, 1080)
    linear 10.5 crop (-1180, -500, 1920, 1080)
with dissolve

$ renpy.pause(8.0)

hide cg16_cred
show cg17_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}校对{/u}{/font}{/size}{vspace=1}{size=+10}Kuroneko{vspace=1}Marantana{vspace=1}Saryana{vspace=1}Xolf{/size}{/color}")):
    size (1920, 1080) crop (-1180, -280, 1920, 1080)
    linear 10.5 crop (-1180, -600, 1920, 1080)
with dissolve

$ renpy.pause(8.0)

hide cg17_cred
show cg18_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}引擎{/u}{/size}{/font}{vspace=1}{size=+10}Ren’py{/size}{/color}")):
    size (1920, 1080) crop (-1270, -340, 1920, 1080)
    linear 10.5 crop (-1270, -640, 1920, 1080)
with dissolve

$ renpy.pause(6.5)
hide text
hide cg18_cred
show text (_("{color=#ffffff}{size=+40}{font=fonts/NotoSansSC-VF.ttf}感谢您的阅读！{/font}{/color}")) at truecenter
with dissolve

$ renpy.pause(10.0)

hide text
with slow_dissolve

$ renpy.pause(1.0)

stop music fadeout 2.0
scene white
with slow_dissolve

return

########################################################

label celine_credits:

play music "bgm/Oh Holy Night.mp3" fadein 2.0
$ renpy.pause(1.0)

scene countryside_n
show overlay2
with slow_dissolve

$ renpy.pause(0.5)

show logo:
    subpixel True
    size (1920, 1080) crop (0, 50, 1920, 1080)
    linear 12.0 crop (0, -350, 1920, 1080)
with slow_dissolve

$ renpy.pause(5.0)

hide logo with slow_dissolve

$ renpy.pause(0.5)

show cg19_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}剧本{/u}{/font}{/size}{vspace=1}{size=+10}ebi-hime{/size}{vspace=20}{size=+30}{u}{font=fonts/NotoSansSC-VF.ttf}程序{/font}{/u}{/size}{vspace=1}{size=+10}ebi-hime{/size}{/color}")):
    size (1920, 1080) crop (-1150, -220, 1920, 1080)
    linear 10.5 crop (-1150, -500, 1920, 1080)
with slow_dissolve

$ renpy.pause(8.0)

hide cg19_cred
show cg20_2_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}角色立绘{/u}{/font}{/size}{vspace=1}{size=+10}Drulle11{/size}{vspace=20}{size=+30}{u}{font=fonts/NotoSansSC-VF.ttf}背景美术{/u}{/size}{/font}{vspace=1}{size=+10}Background TK{/size}{/color}")):
    size (1920, 1080) crop (-1150, -220, 1920, 1080)
    linear 10.5 crop (-1150, -500, 1920, 1080)
with dissolve

$ renpy.pause(8.0)

hide cg20_2_cred
show cg21_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}界面{/u}{/font}{/size}{vspace=1}{size=+10}ds sans{/size}{vspace=20}{size=+30}{u}{font=fonts/NotoSansSC-VF.ttf}字体{/font}{/u}{/size}{vspace=1}{size=+10}Lato{vspace=1}Magnolia{vspace=1}Raleway{/size}{/color}")):
    size (1920, 1080) crop (-1240, -180, 1920, 1080)
    linear 10.5 crop (-1240, -450, 1920, 1080)
with dissolve

$ renpy.pause(8.0)

hide cg21_cred
show cg23_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}音乐{/u}{/size}{/font}{vspace=1}{size=+10}CrysetBase{/size}{vspace=20}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}音效{/u}{/font}{/size}{vspace=1}{size=+10}Pond5{vspace=1}Sounddogs{/size}{/color}")):
    size (1920, 1080) crop (-1180, -220, 1920, 1080)
    linear 10.5 crop (-1180, -500, 1920, 1080)
with dissolve

$ renpy.pause(8.0)

hide cg23_cred
show cg24_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}校对{/u}{/font}{/size}{vspace=1}{size=+10}Kuroneko{vspace=1}Marantana{vspace=1}Saryana{vspace=1}Xolf{/size}{/color}")):
    size (1920, 1080) crop (-1180, -280, 1920, 1080)
    linear 10.5 crop (-1180, -600, 1920, 1080)
with dissolve

$ renpy.pause(8.0)

hide cg24_cred
show cg25_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}引擎{/u}{/size}{/font}{vspace=1}{size=+10}Ren’py{/size}{/color}")):
    size (1920, 1080) crop (-1270, -340, 1920, 1080)
    linear 10.5 crop (-1270, -640, 1920, 1080)
with dissolve

$ renpy.pause(6.5)
hide text
hide cg25_cred
show text (_("{color=#ffffff}{size=+40}{font=fonts/NotoSansSC-VF.ttf}感谢您的阅读！{/font}{/color}")) at truecenter
with dissolve

$ renpy.pause(10.0)

hide text
with slow_dissolve

$ renpy.pause(1.0)

stop music fadeout 2.0
scene white
with slow_dissolve

return


########################################################

label claudine_credits:

# change this to romance theme, probably...
play music "bgm/Claudine.ogg" fadein 2.0
$ renpy.pause(1.0)

scene countryside_n
show overlay2
with slow_dissolve

$ renpy.pause(0.5)

show logo:
    subpixel True
    size (1920, 1080) crop (0, 50, 1920, 1080)
    linear 12.0 crop (0, -350, 1920, 1080)
with slow_dissolve

$ renpy.pause(5.0)

hide logo with slow_dissolve

$ renpy.pause(0.5)

show cg2_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}剧本{/u}{/font}{/size}{vspace=1}{size=+10}ebi-hime{/size}{vspace=20}{size=+30}{u}{font=fonts/NotoSansSC-VF.ttf}程序{/font}{/u}{/size}{vspace=1}{size=+10}ebi-hime{/size}{/color}")):
    size (1920, 1080) crop (-1150, -220, 1920, 1080)
    linear 10.5 crop (-1150, -500, 1920, 1080)
with slow_dissolve

$ renpy.pause(8.0)

hide cg2_cred
show cg26_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}角色立绘{/u}{/font}{/size}{vspace=1}{size=+10}Drulle11{/size}{vspace=20}{size=+30}{u}{font=fonts/NotoSansSC-VF.ttf}背景美术{/u}{/size}{/font}{vspace=1}{size=+10}Background TK{/size}{/color}")):
    size (1920, 1080) crop (-1150, -220, 1920, 1080)
    linear 10.5 crop (-1150, -500, 1920, 1080)
with dissolve

$ renpy.pause(8.0)

hide cg26_cred
show cg4_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}界面{/u}{/font}{/size}{vspace=1}{size=+10}ds sans{/size}{vspace=20}{size=+30}{u}{font=fonts/NotoSansSC-VF.ttf}字体{/font}{/u}{/size}{vspace=1}{size=+10}Lato{vspace=1}Magnolia{vspace=1}Raleway{/size}{/color}")):
    size (1920, 1080) crop (-1240, -180, 1920, 1080)
    linear 10.5 crop (-1240, -450, 1920, 1080)
with dissolve

$ renpy.pause(8.0)

hide cg4_cred
show cg5_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}音乐{/u}{/size}{/font}{vspace=1}{size=+10}CrysetBase{/size}{vspace=20}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}音效{/u}{/font}{/size}{vspace=1}{size=+10}Pond5{vspace=1}Sounddogs{/size}{/color}")):
    size (1920, 1080) crop (-1180, -220, 1920, 1080)
    linear 10.5 crop (-1180, -500, 1920, 1080)
with dissolve

$ renpy.pause(8.0)

hide cg5_cred
show cg6_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}校对{/u}{/font}{/size}{vspace=1}{size=+10}Kuroneko{vspace=1}Marantana{vspace=1}Saryana{vspace=1}Xolf{/size}{/color}")):
    size (1920, 1080) crop (-1180, -280, 1920, 1080)
    linear 10.5 crop (-1180, -600, 1920, 1080)
with dissolve

$ renpy.pause(8.0)

hide cg6_cred
show cg3_cred:
    linear 0.0 xalign 0.10 yalign 0.5
show text (_("{color=#ffffff}{size=+30}{font=fonts/NotoSansSC-VF.ttf}{u}引擎{/u}{/size}{/font}{vspace=1}{size=+10}Ren’py{/size}{/color}")):
    size (1920, 1080) crop (-1270, -340, 1920, 1080)
    linear 10.5 crop (-1270, -640, 1920, 1080)
with dissolve

$ renpy.pause(6.5)
hide text
hide cg3_cred
show text (_("{color=#ffffff}{size=+40}{font=fonts/NotoSansSC-VF.ttf}感谢您的阅读！{/font}{/color}")) at truecenter
with dissolve

$ renpy.pause(10.0)

hide text
with slow_dissolve

$ renpy.pause(1.0)

stop music fadeout 2.0
scene white
with slow_dissolve

return


########################################################

image cg1_cred = im.FactorScale("cgs/cg1.jpg", 0.40)
image cg2_cred = im.FactorScale("cgs/cg2.jpg", 0.40)
image cg3_cred = im.FactorScale("cgs/cg3.jpg", 0.40)
image cg4_cred = im.FactorScale("cgs/cg4.jpg", 0.40)
image cg5_cred = im.FactorScale("cgs/cg5.jpg", 0.40)
image cg6_cred = im.FactorScale("cgs/cg6_2.jpg", 0.40)
image cg8_cred = im.FactorScale("cgs/cg8.jpg", 0.40)
image cg9_cred = im.FactorScale("cgs/cg9.jpg", 0.40)
image cg10_cred = im.FactorScale("cgs/cg10.jpg", 0.40)
image cg11_cred = im.FactorScale("cgs/cg11.jpg", 0.40)
image cg12_cred = im.FactorScale("cgs/cg12.jpg", 0.40)
image cg13_cred = im.FactorScale("cgs/cg13.jpg", 0.40)
image cg14_cred = im.FactorScale("cgs/cg14.jpg", 0.40)
image cg15_cred = im.FactorScale("cgs/cg15.jpg", 0.40)
image cg16_cred = im.FactorScale("cgs/cg16.jpg", 0.40)
image cg17_cred = im.FactorScale("cgs/cg17.jpg", 0.40)
image cg18_cred = im.FactorScale("cgs/cg18.jpg", 0.40)
image cg19_cred = im.FactorScale("cgs/cg19.jpg", 0.40)
image cg20_2_cred = im.FactorScale("cgs/cg20_2.jpg", 0.40)
image cg21_cred = im.FactorScale("cgs/cg21.jpg", 0.40)
image cg23_cred = im.FactorScale("cgs/cg23.jpg", 0.40)
image cg24_cred = im.FactorScale("cgs/cg24.jpg", 0.40)
image cg25_cred = im.FactorScale("cgs/cg25.jpg", 0.40)
image cg26_cred = im.FactorScale("cgs/cg26.jpg", 0.40)
image cg32_cred = im.FactorScale("cgs/cg32.jpg", 0.40)

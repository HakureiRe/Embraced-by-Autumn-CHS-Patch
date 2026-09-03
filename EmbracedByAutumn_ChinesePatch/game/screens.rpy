################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


################################################################################


transform appear:

    on show:
        xalign .5 yalign .5
        linear 1.0 alpha 1.0
    on replace:
        xalign .5 yalign .5
        linear 1.0 alpha 1.0
    on hide:
        linear 1.0 alpha 0.0

transform h_smooth(p=0, t=.5, x=0, y=0): ##transform with horizontal hover
    alpha .0 xoffset x yoffset y
    pause p
    easein t  alpha 1.0 xoffset 0 yoffset 0
    on replaced:
        easeout t alpha 0
    on hide:
        easeout t alpha 0
    on hover:
        easein .2 xoffset -6
    on idle:
        easeout .2 xoffset 0
    on selected_idle:
        easeout .2 xoffset 0
    on selected_hover:
        easein .2 xoffset -6

transform v_smooth(p=0, t=.5, x=0, y=0): ##transform with vertical hover
    alpha 1.0 xoffset 0 yoffset 0
    on replaced:
        easeout t alpha 0
    on hide:
        easeout t alpha 0
    on hover:
        easein .2 yoffset -6
    on idle:
        easeout .2 yoffset 0
    on selected_idle:
        easeout .2 yoffset 0
    on selected_hover:
        easein .2 yoffset -6


################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    default side_image = None
    default two_window = False

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what:
            id "what"
            xsize 1380
            line_spacing 1

    use quick_menu


    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign -0.02 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    #background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    #padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    ypos gui.dialogue_ypos

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize 1100
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum 1100


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        at appear

        vbox:
            style "menu"
            spacing 20

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear


##################################################################################

transform appear:

    on show:
        xalign .5 yalign .5
        linear 1.0 alpha 1.0
    on replace:
        xalign .5 yalign .5
        linear 1.0 alpha 1.0
    on hide:
        linear 1.0 alpha 0.0

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu:

        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 0.955

            textbutton _("返回") action Rollback()
            textbutton _("跳过") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("存档") action ShowMenu('save')
            textbutton _("设置") action ShowMenu('preferences')

screen quick_menu2:

        hbox:
            style_prefix "quick2"
            xalign 0.5
            yalign 0.925

            textbutton _("返回") action Rollback()
            textbutton _("跳过") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("存档") action ShowMenu('save')
            textbutton _("设置") action ShowMenu('preferences')

init -2:
    style quick_button:
        #size_group "notes_nav"
        background None
        xpadding 30

    style quick_button_text:
        size 20
        font "fonts/NotoSansSC-VF.ttf"
        idle_color "#5c3e27"
        hover_color "#a2846d"
        selected_idle_color "#a2846d"
        selected_hover_color "#a2846d"
        insensitive_color "#8e857f"

    style quick2_button:
        #size_group "notes_nav"
        background None
        xpadding 30

    style quick2_button_text:
        size 20
        font "fonts/NotoSansSC-VF.ttf"
        idle_color "#5c3e27"
        hover_color "#a2846d"
        selected_idle_color "#a2846d"
        selected_hover_color "#a2846d"
        insensitive_color "#8e857f"

##############################################################################

# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation

screen navigation:

    hbox:
        style_group "nav"
        xalign 0.5
        yalign 0.89

        textbutton _("返回") action Return()
        textbutton _("设置") action ShowMenu("preferences")
        textbutton _("读取") action ShowMenu("load")
        textbutton _("保存") action ShowMenu("save")
        textbutton _("标题") action MainMenu()
        textbutton _("退出") action Quit()

screen extras_navigation:

    hbox:
        style_group "nav"
        xalign 0.5
        yalign 0.89

        textbutton _("画廊") action ShowMenu("gallery")
        textbutton _("音乐") action ShowMenu("music")
        if persistent.end == "on":
            textbutton _("制作手记") action ShowMenu("notes")
        else:
            textbutton _("未解锁")
        textbutton _("返回") action ShowMenu("extras")
        textbutton _("标题") action ShowMenu("main_menu")

init -2:

    style nav_button:
        background None
        xpadding 40

    style nav_button_text:
        size 44
        font "fonts/NotoSansSC-VF.ttf"
        idle_color "#facf8d"
        hover_color "#ffffff"
        selected_idle_color "#a38962"
        selected_hover_color "#a38962"
        insensitive_color "#a38962"
        xalign 0.5
        xcenter 0.5

style main_header:
    font "fonts/NotoSansSC-VF.ttf"
    size 76
    color "5c3e27"
    xanchor 0.0
    xpos 0.0
    xalign 0.0
    text_align 0.0

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    tag menu

    add "gui/mm.png"
    add "gui/logo.png"

    vbox:
        style_group "mm"
        xalign .50
        yalign .820

        textbutton _("开始") at v_smooth(0,0.6,0,0) action Start()
        textbutton _("继续") at v_smooth(0,0.6,0,0) action ShowMenu("load")
        textbutton _("设置") at v_smooth(0,0.6,0,0) action ShowMenu("preferences")
        textbutton _("附加内容") at v_smooth(0,0.6,0,0) action ShowMenu("extras")
        textbutton _("退出") at v_smooth(0,0.6,0,0) action Quit(confirm=False)


init -2:

    style mm_button:
        size_group "mm_button"
        background None
        ypadding -6

    style mm_button_text:
        size 72
        font "fonts/NotoSansSC-VF.ttf"
        outlines [(2, "#5c3e27", 0, 0)]
        idle_color "#f8e1a7"
        hover_color "#de6743"
        selected_idle_color "#f2c582"
        selected_hover_color "#f2c582"
        insensitive_color "#a38962"
        drop_shadow [(1, 1)]
        xcenter 0.5

#################################################################################

screen extras():
    tag menu

    add "gui/extra_mm.png"
    add "gui/logo.png"

    vbox:
        style_group "mm2"
        xalign .50
        yalign .86

        textbutton _("画廊") at v_smooth(0,0.6,0,0) action ShowMenu("gallery")
        textbutton _("音乐盒") at v_smooth(0,0.6,0,0) action ShowMenu("music")
        if persistent.end == "on":
            textbutton _("制作手记") at v_smooth(0,0.6,0,0) action ShowMenu("notes")
        else:
            textbutton _("未解锁")
        textbutton _("返回") at v_smooth(0,0.6,0,0) action ShowMenu("main_menu")

init -2:

    style mm2_button:
        size_group "mm2_button"
        background None
        ypadding -4

    style mm2_button_text:
        size 72
        font "fonts/NotoSansSC-VF.ttf"
        outlines [(2, "#5c3e27", 0, 0)]
        idle_color "#f8e1a7"
        hover_color "#de6743"
        selected_idle_color "#f2c582"
        selected_hover_color "#f2c582"
        insensitive_color "#a38962"
        drop_shadow [(1, 1)]
        xcenter 0.5


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("返回"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("版本 [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("由 {a=https://www.renpy.org/}Ren'Py{/a} 驱动（版本 [renpy.version_only]）。\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen load_save_slot:
    $ file_text = "%2s. %s\n  %s" % (
                        FileSlotName(number, 6),
                        FileTime(number, empty=__ ("Empty Slot.")),
                        FileSaveName(number))

    add FileScreenshot(number) xpos 43 ypos 11
    text file_text:
        style "slot_name_text"
        xpos 380 ypos 94

    key "save_delete" action FileDelete(number)

screen file_picker:

    imagemap:
            ground "gui/sl_ground.png"
            idle "gui/sl_idle.png"
            hover "gui/sl_hover.png"
            selected_idle "gui/sl_hover.png"
            insensitive "gui/sl_idle.png"

            hotspot (160, 220, 720, 203) at v_smooth(0,0.6,0,0) clicked FileAction(1):
                use load_save_slot(number=1)
            hotspot (907, 220, 720, 203) at v_smooth(0,0.6,0,0) clicked FileAction(2):
                use load_save_slot(number=2)
            hotspot (160, 440, 720, 203) at v_smooth(0,0.6,0,0) clicked FileAction(3):
                use load_save_slot(number=3)
            hotspot (907, 440, 720, 203) at v_smooth(0,0.6,0,0) clicked FileAction(4):
                use load_save_slot(number=4)
            hotspot (160, 660, 720, 203) at v_smooth(0,0.6,0,0) clicked FileAction(5):
                use load_save_slot(number=5)
            hotspot (907, 660, 720, 203) at v_smooth(0,0.6,0,0) clicked FileAction(6):
                use load_save_slot(number=6)

    vbox:
        style_group "pages"
        xalign .925
        yalign .5

        textbutton _("1") clicked FilePage(1)
        textbutton _("2") clicked FilePage(2)
        textbutton _("3") clicked FilePage(3)
        textbutton _("4") clicked FilePage(4)
        textbutton _("5") clicked FilePage(5)
        textbutton _("6") clicked FilePage(6)
        textbutton _("7") clicked FilePage(7)
        textbutton _("8") clicked FilePage(8)
        textbutton _("9") clicked FilePage(9)

    use navigation


screen save:
    key "s" action Return()
    # This ensures that any other menu screen is replaced.
    tag menu
    if main_menu:
        add "bgs/countryside_d.jpg"

    use file_picker
    text "保存游戏":
        xalign 0.11
        yalign 0.09
        text_align 0.5
        style "main_header"

screen load:
    key "l" action Return()
    # This ensures that any other menu screen is replaced.
    tag menu
    if main_menu:
        add "bgs/countryside_d.jpg"

    use file_picker
    text "读取游戏":
        xalign 0.11
        yalign 0.09
        text_align 0.5
        style "main_header"

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)
    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)
    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)
    config.thumbnail_width = 312
    config.thumbnail_height = 175

    style.slot_name_text = Style(style.slot_button_text)

style slot_button_text:
    xanchor 0.0
    xpos 0.0
    xalign 0.0
    text_align 0.0

style pages_button:
    size_group "pages"
    background None
    ypadding 5

style pages_button_text:
    font "fonts/NotoSansSC-VF.ttf"
    idle_color "#facf8d"
    hover_color "#ffffff"
    selected_idle_color "#ffffff"
    selected_hover_color "#ffffff"
    insensitive_color "#a38962"
    size 48
    xcenter 0.0
    xpos 0.0
    text_align 0.0


translate None style slot_button_text:
    font "fonts/NotoSansSC-VF.ttf"
    size 25
    color "#5c3e27"
    line_spacing 0

## Preferences screen ##########################################################

# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:

    tag menu

    if main_menu:
        add "bgs/countryside_d.jpg"

    add "gui/config_ground.png"
    use navigation

    text "设置":
        xalign 0.11
        yalign 0.09
        text_align 0.5
        style "main_header"

    grid 1 1:
        style_group "prefs"
        xalign 0.23
        yalign 0.40
        xmaximum 1200

        vbox:

            text _("显示"):
                style "pref_header"

            frame:
                style_group "pref"
                has hbox

                textbutton _("窗口模式") at h_smooth(0,0.6,0,0) action Preference("display", "any window")
                textbutton _("全屏") at h_smooth(0,0.6,0,0) action Preference("display", "fullscreen")

            text _("转场效果"):
                style "pref_header"

            frame:
                style_group "pref"
                has hbox

                textbutton _("全部开启") at h_smooth(0,0.6,0,0) action Preference("transitions", "all")
                textbutton _("全部关闭") at h_smooth(0,0.6,0,0) action Preference("transitions", "none")

            text _("快进"):
                style "pref_header"

            frame:
                style_group "pref"
                has hbox

                textbutton _("仅已读文本") at h_smooth(0,0.6,0,0) action Preference("skip", "seen")
                textbutton _("全部文本") at h_smooth(0,0.6,0,0) action Preference("skip", "all")

            #text _("Language"):
            #    style "pref_header"

            #frame:
            #    style_group "pref"
            #    has vbox

            #    textbutton _("English") at h_smooth(0,0.6,0,0) action Language(None)
                #textbutton _("{font=gui/fonts/simkai.ttf}简体中文{/font}") at h_smooth(0,0.6,0,0) action Language("chinese")


    grid 1 1:
        style_group "prefs"
        xalign 0.80
        yalign 0.53
        #xmaximum 650

        vbox:
            frame:
                style_group "pref3"
                has vbox

                text _("文本速度"):
                    style "pref_header"
                    #ypos -0.40
                  # drop_shadow [(2, 2)]
                #text _("    slower                                                                                faster"):
                 #   color "#689a6d"
                 #   font "fonts/NotoSansSC-VF.ttf"
                 #   size 20
                  # drop_shadow [(2, 2)]
                bar value Preference("text speed")

            frame:
                style_group "pref3"
                has vbox
                text _("自动前进延迟"):
                    style "pref_header"

                    #ypos -0.40
                 #  drop_shadow [(2, 2)]
              #  text _("    faster                                                                                slower"):
               #     color "#689a6d"
                #    font "fonts/NotoSansSC-VF.ttf"
                 #   size 20
                 #  drop_shadow [(2, 2)]
                bar value Preference("auto-forward time")

            frame:
                style_group "pref3"
                has vbox

                text _("音乐音量"):
                    style "pref_header"
                    #ypos -0.40
                  # drop_shadow [(2, 2)]

                #text _("    softer                                                                                louder"):
               #     color "#689a6d"
                #    font "fonts/NotoSansSC-VF.ttf"
                 #   size 20
                  # drop_shadow [(2, 2)]
                bar value Preference("music volume")

            frame:
                style_group "pref3"
                has vbox
                text _("音效音量"):
                    style "pref_header"
                    #ypos -0.40
                  # drop_shadow [(2, 2)]
               # text _("    softer                                                                                louder"):
                #    color "#689a6d"
                #    font "fonts/NotoSansSC-VF.ttf"
                #    size 20
                 # drop_shadow [(2, 2)]

                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("测试"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"



init -2:
    style pref_frame:
        xmargin 0
        top_margin 0
        background None

    style pref_hbox:
        xfill False

    style pref_vbox:
        xfill False

    style pref_button:
        size_group "pref"
        background "gui/pref_butt.png"
        hover_background "gui/pref_butt.png"
        xpadding 90
        ypadding 20

    style pref_button_text:
        size 34
        font "fonts/NotoSansSC-VF.ttf"
        idle_color "#a38962"
        hover_color "#ffffff"
        selected_idle_color "#facf8d"
        selected_hover_color "#ffffff"
        insensitive_color "#a38962"
        xalign 0.5
        xcenter 0.5

    style pref_header:
        size_group "pref_header"
        background None
        size 38
        font "fonts/NotoSansSC-VF.ttf"
        idle_color "#5c3e27"
        xalign 0.0

    style pref3_frame:
        xfill False
        xmargin 3
        top_margin 0
        ypadding -2
        background None

    style pref3_hbox:
        xfill False

    style pref3_vbox:
        xfill False

    style soundtest_button:
        xalign 1.0

init -2 python:

    style.pref3_slider.left_bar = "gui/bar_full.png"
    style.pref3_slider.right_bar = "gui/bar_empty.png"
    style.pref3_slider.hover_left_bar = "gui/bar_full.png"
    style.pref3_slider.thumb = "gui/thumb.png"
    style.pref3_slider.thumb_shadow = None
    style.pref3_slider.thumb_offset = 15
    style.pref3_slider.ymaximum = 96
    style.pref3_slider.xmaximum = 548
    style.pref3_slider.left_gutter = 10
    style.pref3_slider.right_gutter = -5


    style.vscrollbar.left_bar = "gui/scrollbar/vertical_idle_bar.png"
    style.vscrollbar.right_bar = "gui/scrollbar/vertical_hover_bar.png"
    style.vscrollbar.hover_left_bar = "gui/scrollbar/vertical_idle_bar.png"
    style.vscrollbar.thumb = "gui/scrollbar/vertical_hover_thumb.png"
    style.vscrollbar.thumb_shadow = None
    style.vscrollbar.thumb_offset = 15
    style.vscrollbar.ymaximum = 1050
    style.vscrollbar.xmaximum = 50
    style.vscrollbar.left_gutter = 0
    style.vscrollbar.right_gutter = 0


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("对话记录为空。")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("键盘") action SetScreenVariable("device", "keyboard")
                textbutton _("鼠标") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("手柄") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("回车")
        text _("推进对话并激活界面。")

    hbox:
        label _("空格")
        text _("推进对话（不选择选项）。")

    hbox:
        label _("方向键")
        text _("在界面中导航。")

    hbox:
        label _("退出键")
        text _("进入游戏菜单。")

    hbox:
        label _("控制键")
        text _("按住时快进对话。")

    hbox:
        label _("制表键")
        text _("切换快进对话模式。")

    hbox:
        label _("上翻页")
        text _("回退到更早的对话。")

    hbox:
        label _("下翻页")
        text _("前进到更晚的对话。")

    hbox:
        label "H"
        text _("隐藏用户界面。")

    hbox:
        label "S"
        text _("截取屏幕截图。")

    hbox:
        label "V"
        text _("切换辅助功能{a=https://www.renpy.org/l/voicing}朗读{/a}。")


screen mouse_help():

    hbox:
        label _("左键单击")
        text _("推进对话并激活界面。")

    hbox:
        label _("中键单击")
        text _("隐藏用户界面。")

    hbox:
        label _("右键单击")
        text _("进入游戏菜单。")

    hbox:
        label _("滚轮向上\n点击回退侧边栏")
        text _("回退到更早的对话。")

    hbox:
        label _("滚轮向下")
        text _("前进到更晚的对话。")


screen gamepad_help():

    hbox:
        label _("右扳机键\nA/底端按钮")
        text _("推进对话并激活界面。")

    hbox:
        label _("左扳机键\n左肩键")
        text _("回退到更早的对话。")

    hbox:
        label _("右肩键")
        text _("前进到更晚的对话。")


    hbox:
        label _("方向键、摇杆")
        text _("在界面中导航。")

    hbox:
        label _("开始键、导航键")
        text _("进入游戏菜单。")

    hbox:
        label _("Y/顶端按钮")
        text _("隐藏用户界面。")

    textbutton _("校准") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################

screen yesno_prompt:

    modal True

    add "gui/yn.png"

    hbox:
        style_group "yn"
        xalign 0.55
        yalign 0.56

        textbutton _("是") at v_smooth(0,0.6,0,0) action yes_action
        textbutton _("否") at v_smooth(0,0.6,0,0) action no_action

    text _(message):
            style "yn_popup"


init -2:

    style yn_button:
        size_group "yn"
        background "gui/yn_button.png"
        hover_background "gui/yn_button.png"
        xpadding 140

    style yn_button_text:
        size 40
        font "fonts/NotoSansSC-VF.ttf"
        idle_color "#efc081"
        hover_color "#ffffff"
        selected_idle_color "#ffffff"
        selected_hover_color "#ffffff"
        insensitive_color "#ffffff"
        xalign 0.5

    style yn_popup:
        color "#5f412a"
        font "fonts/NotoSansSC-VF.ttf"
        size 34
        #drop_shadow [(2, 2)]
        xalign 0.50
        yalign 0.44
        text_align 0.5

###############################################################################

translate None style yn_button_text:
    font "fonts/NotoSansSC-VF.ttf"
    size 40
    xpos -0.25
    ypos 0.63
    xalign 0.5

translate chinese style yn_button_text:
    font "gui/fonts/simkai.ttf"
    size 46
    xpos -0.40
    ypos 0.60
    xalign 0.5

translate chinese style yn_popup:
    font "gui/fonts/simkai.ttf"
    size 36

translate None style yn_popup:
    font "fonts/NotoSansSC-VF.ttf"
    size 36

################################################################################

screen indicator():
    zorder 9999

    ##debug functions

    #if config.developer:
       # $ctd=renpy.call_stack_depth()
       # text _("Call stack (debugger) [ctd]") align (.01,1.0)

    if _rollback:
        if _preferences.afm_enable:
            image "GUI/auto.png"
        if config.skipping == "slow":
            image "GUI/skip.png"
        if config.skipping == "fast":
            image "GUI/skip.png"

init python:
    config.skip_indicator = None
    config.overlay_screens.append("indicator")

## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png")
    yminimum 56
    xminimum 1180

style notify_text:
    properties gui.text_properties("notify")
    xpos 40
    ypos 5
    color "facf8d"
    outlines [(2, "#4e321b")]
    font "fonts/NotoSansSC-VF.ttf"

###############################################################################

translate chinese style notify_text:
    font "gui/fonts/simkai.ttf"

translate None style notify_text:
    font "fonts/NotoSansSC-VF.ttf"

## NVL screen ##################################################################

# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what:
                    id what_id
                    line_spacing 10

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu2




################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("返回") action Rollback()
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("菜单") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900

#################################

#######################################

init python:

    # Step 1. Create the gallery object.
    g = Gallery()

    # Step 2. Add buttons and images to the gallery.

    g.button       ("cg1")
    g.unlock_image ("cg1")

    g.button       ("cg2")
    g.unlock_image ("cg2")

    g.button       ("cg3")
    g.unlock_image ("cg3")
    g.unlock_image ("cg3_2")

    g.button       ("cg4")
    g.unlock_image ("cg4")

    g.button       ("cg5")
    g.unlock_image ("cg5")

    g.button       ("cg6")
    g.unlock_image ("cg6")
    g.unlock_image ("cg6_2")

    g.button       ("cg7")
    g.unlock_image ("cg7")

    g.button       ("cg8")
    g.unlock_image ("cg8")

    g.button       ("cg9")
    g.unlock_image ("cg9")
    g.unlock_image ("cg9_2")

    g.button       ("cg10")
    g.unlock_image ("cg10")

    g.button       ("cg11")
    g.unlock_image ("cg11")

    g.button       ("cg12")
    g.unlock_image ("cg12")

    g.button       ("cg13")
    g.unlock_image ("cg13")
    g.unlock_image ("cg13_2")

    g.button       ("cg14")
    g.unlock_image ("cg14")

    g.button       ("cg15")
    g.unlock_image ("cg15")
    g.unlock_image ("cg15_2")

    g.button       ("cg16")
    g.unlock_image ("cg16")

    g.button       ("cg17")
    g.unlock_image ("cg17")
    g.unlock_image ("cg17_2")

    g.button       ("cg18")
    g.unlock_image ("cg18")

    g.button       ("cg19")
    g.unlock_image ("cg19")
    g.unlock_image ("cg19_2")

    g.button       ("cg20")
    g.unlock_image ("cg20")
    g.unlock_image ("cg20_2")

    g.button       ("cg21")
    g.unlock_image ("cg21")

    g.button       ("cg22")
    g.unlock_image ("cg22")
    g.unlock_image ("cg22_2")

    g.button       ("cg23")
    g.unlock_image ("cg23")

    g.button       ("cg24")
    g.unlock_image ("cg24")

    g.button       ("cg25")
    g.unlock_image ("cg25")

    g.button       ("cg26")
    g.unlock_image ("cg26")
    g.unlock_image ("cg26_2")
    g.unlock_image ("cg26_3")

    g.button       ("cg27")
    g.unlock_image ("cg27")

    g.button       ("cg28")
    g.unlock_image ("cg28")

    g.button       ("cg29")
    g.unlock_image ("cg29")

    g.button       ("cg30")
    g.unlock_image ("cg30")

    g.button       ("cg31")
    g.unlock_image ("cg31")

    g.button       ("cg32")
    g.unlock_image ("cg32")

    g.locked_button = "gui/locked.png"


    # The transition used when switching images.
    g.transition = dissolve

    bg_page=1


########################################

screen gallery:

    tag menu

    add "bgs/countryside_d.jpg"

    add "gui/sl_ground.png"
    use extras_navigation

    $ next_bg_page = bg_page + 1
    $ prev_bg_page = bg_page - 1

    text "画廊":
        xalign 0.11
        yalign 0.09
        text_align 0.5
        style "main_header"

    grid 3 2:

        xoffset 240
        xspacing 70
        yspacing 70
        yoffset 280

        add g.make_button("cg27", im.Scale("cgs/CG27.jpg", 384, 216, xpos =0,ypos=0))
        add g.make_button("cg7", im.Scale("cgs/CG7.jpg", 384, 216, xpos =0,ypos=0))
        add g.make_button("cg28", im.Scale("cgs/CG28.jpg", 384, 216, xpos =0,ypos=0))

        add g.make_button("cg29", im.Scale("cgs/CG29.jpg", 384, 216, xpos =0,ypos=0))
        add g.make_button("cg1", im.Scale("cgs/CG1.jpg", 384, 216, xpos =0,ypos=0))
        add g.make_button("cg19", im.Scale("cgs/CG19.jpg", 384, 216, xpos =0,ypos=0))

    vbox:
        style_group "pages"
        xalign .925
        yalign .5

        textbutton _("1") #clicked FilePage(1)
        textbutton _("2") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery2')  ]
        textbutton _("3") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery3')  ]
        textbutton _("4") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery4')  ]
        textbutton _("5") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery5')  ]
        textbutton _("6") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery6')  ]

#######################

screen gallery2:

    tag menu

    add "bgs/countryside_d.jpg"

    add "gui/sl_ground.png"
    use extras_navigation

    $ next_bg_page = bg_page + 1
    $ prev_bg_page = bg_page - 1

    text "画廊":
        xalign 0.11
        yalign 0.09
        text_align 0.5
        style "main_header"

    grid 3 2:

        xoffset 240
        xspacing 70
        yspacing 70
        yoffset 280

        add g.make_button("cg2", im.Scale("cgs/CG2.jpg", 384, 216, xpos =0,ypos=0))
        add g.make_button("cg3", im.Scale("cgs/CG3.jpg", 384, 216, xpos =0,ypos=0))
        add g.make_button("cg26", im.Scale("cgs/CG26.jpg", 384, 216, xpos =0,ypos=0))

        add g.make_button("cg4", im.Scale("cgs/CG4.jpg", 384, 216, xpos =0,ypos=0))
        add g.make_button("cg30", im.Scale("cgs/CG30.jpg", 384, 216, xpos =0,ypos=0))
        add g.make_button("cg5", im.Scale("cgs/CG5.jpg", 384, 216, xpos =0,ypos=0))

    vbox:
        style_group "pages"
        xalign .925
        yalign .5

        textbutton _("1") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery')  ]
        textbutton _("2") #action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery2')  ]
        textbutton _("3") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery3')  ]
        textbutton _("4") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery4')  ]
        textbutton _("5") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery5')  ]
        textbutton _("6") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery6')  ]

#################################

screen gallery3:

    tag menu

    add "bgs/countryside_d.jpg"

    add "gui/sl_ground.png"
    use extras_navigation

    $ next_bg_page = bg_page + 1
    $ prev_bg_page = bg_page - 1

    text "画廊":
        xalign 0.11
        yalign 0.09
        text_align 0.5
        style "main_header"

    grid 3 2:

        xoffset 240
        xspacing 70
        yspacing 70
        yoffset 280

        add g.make_button("cg6", im.Scale("cgs/CG6.jpg", 384, 216, xpos =0,ypos=0))
        add g.make_button("cg31", im.Scale("cgs/CG31.jpg", 384, 216, xpos =0,ypos=0))
        add g.make_button("cg8", im.Scale("cgs/CG8.jpg", 384, 216, xpos =0,ypos=0))

        add g.make_button("cg9", im.Scale("cgs/CG9.jpg", 384, 216, xpos =0,ypos=0))
        add g.make_button("cg10", im.Scale("cgs/CG10.jpg", 384, 216, xpos =0,ypos=0))
        add g.make_button("cg11", im.Scale("cgs/CG11.jpg", 384, 216, xpos =0,ypos=0))

    vbox:
        style_group "pages"
        xalign .925
        yalign .5

        textbutton _("1") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery')  ]
        textbutton _("2") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery2')  ]
        textbutton _("3") #action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery3')  ]
        textbutton _("4") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery4')  ]
        textbutton _("5") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery5')  ]
        textbutton _("6") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery6')  ]

##########################################################################

screen gallery4:

    tag menu

    add "bgs/countryside_d.jpg"

    add "gui/sl_ground.png"
    use extras_navigation

    $ next_bg_page = bg_page + 1
    $ prev_bg_page = bg_page - 1

    text "画廊":
        xalign 0.11
        yalign 0.09
        text_align 0.5
        style "main_header"

    grid 3 2:

        xoffset 240
        xspacing 70
        yspacing 70
        yoffset 280

        add g.make_button("cg12", im.Scale("cgs/CG12.jpg", 384, 216, xpos =0,ypos=0))
        add g.make_button("cg13", im.Scale("cgs/CG13.jpg", 384, 216, xpos =0,ypos=0))
        add g.make_button("cg32", im.Scale("cgs/CG32.jpg", 384, 216, xpos =0,ypos=0))

        add g.make_button("cg14", im.Scale("cgs/CG14.jpg", 384, 216, xpos =0,ypos=0))
        add g.make_button("cg15", im.Scale("cgs/CG15.jpg", 384, 216, xpos =0,ypos=0))
        add g.make_button("cg16", im.Scale("cgs/CG16.jpg", 384, 216, xpos =0,ypos=0))

    vbox:
        style_group "pages"
        xalign .925
        yalign .5

        textbutton _("1") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery')  ]
        textbutton _("2") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery2')  ]
        textbutton _("3") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery3')  ]
        textbutton _("4") #action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery4')  ]
        textbutton _("5") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery5')  ]
        textbutton _("6") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery6')  ]

###################################################################################

screen gallery5:

    tag menu

    add "bgs/countryside_d.jpg"

    add "gui/sl_ground.png"
    use extras_navigation

    $ next_bg_page = bg_page + 1
    $ prev_bg_page = bg_page - 1

    text "画廊":
        xalign 0.11
        yalign 0.09
        text_align 0.5
        style "main_header"

    grid 3 2:

        xoffset 240
        xspacing 70
        yspacing 70
        yoffset 280

        add g.make_button("cg17", im.Scale("cgs/CG17.jpg", 384, 216, xpos =0,ypos=0))
        add g.make_button("cg18", im.Scale("cgs/CG18.jpg", 384, 216, xpos =0,ypos=0))
        add g.make_button("cg20", im.Scale("cgs/CG20.jpg", 384, 216, xpos =0,ypos=0))

        add g.make_button("cg21", im.Scale("cgs/CG21.jpg", 384, 216, xpos =0,ypos=0))
        add g.make_button("cg22", im.Scale("cgs/CG22.jpg", 384, 216, xpos =0,ypos=0))
        add g.make_button("cg23", im.Scale("cgs/CG23.jpg", 384, 216, xpos =0,ypos=0))

    vbox:
        style_group "pages"
        xalign .925
        yalign .5

        textbutton _("1") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery')  ]
        textbutton _("2") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery2')  ]
        textbutton _("3") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery3')  ]
        textbutton _("4") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery4')  ]
        textbutton _("5") #action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery5')  ]
        textbutton _("6") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery6')  ]

###################################################################################

screen gallery6:

    tag menu

    add "bgs/countryside_d.jpg"

    add "gui/sl_ground.png"
    use extras_navigation

    $ next_bg_page = bg_page + 1
    $ prev_bg_page = bg_page - 1

    text "画廊":
        xalign 0.11
        yalign 0.09
        text_align 0.5
        style "main_header"

    grid 3 2:

        xoffset 240
        xspacing 70
        yspacing 70
        yoffset 280

        add g.make_button("cg24", im.Scale("cgs/CG24.jpg", 384, 216, xpos =0,ypos=0))
        add g.make_button("cg25", im.Scale("cgs/CG25.jpg", 384, 216, xpos =0,ypos=0))
        label _(" ")

        label _(" ")
        label _(" ")
        label _(" ")

    vbox:
        style_group "pages"
        xalign .925
        yalign .5

        textbutton _("1") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery')  ]
        textbutton _("2") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery2')  ]
        textbutton _("3") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery3')  ]
        textbutton _("4") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery4')  ]
        textbutton _("5") action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery5')  ]
        textbutton _("6") #action [SetVariable('bg_page', next_bg_page), ShowMenu('gallery6')  ]

#################################################################################

init -2:

    style gal_button:
        size_group "gal_button"
        background None
        hover_background None
        xpadding 20
        ypadding 5

    style gal_button_text:
        size 36
        font "fonts/NotoSansSC-VF.ttf"
        #drop_shadow [(1, 1)]
        #outlines [(1, "#000000")]
        idle_color "#689a6d"
        hover_color "#56815a"
        selected_idle_color "#487766"
        selected_hover_color "#487766"
        insensitive_color "#3b3c3f"
        #xalign 0.60
        xcenter 0.5
        #yanchor 0.10

#####################################

translate chinese style gal_button_text:
    font "gui/fonts/simkai.ttf"
    size 36

translate None style gal_button_text:
    font "fonts/NotoSansSC-VF.ttf"
    size 36

#####################################

init python:

    # Step 1. Create a MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)

    mr.add("bgm/Casual_Day.ogg", always_unlocked=True)
    mr.add("bgm/Celine.ogg")
    mr.add("bgm/Night.ogg")
    mr.add("bgm/Sad.ogg")
    mr.add("bgm/Mysterious.ogg")
    mr.add("bgm/Energetic.ogg")
    mr.add("bgm/Comedy.ogg")
    mr.add("bgm/Luce.ogg")
    mr.add("bgm/Claudine.ogg")
    mr.add("bgm/Friendship.ogg")
    mr.add("bgm/Confession.ogg")
    mr.add("bgm/Mirabel.ogg")
    mr.add("bgm/Classroom.ogg")
    mr.add("bgm/Oh Holy Night.mp3")

#######################################

screen music:

    tag menu

    add "bgs/countryside_d.jpg"

    add "gui/config_ground.png"
    use extras_navigation

    text "音乐盒":
        xalign 0.11
        yalign 0.09
        text_align 0.5
        style "main_header"

    grid 1 1:
        style_group "music"
        xalign 0.35
        yalign 0.50
        xmaximum 500

        vbox:
            frame:
                style_group "music"
                has vbox

                textbutton _("秋叶") action mr.Play("bgm/Casual_Day.ogg")
                textbutton _("心情舒畅") action mr.Play("bgm/Energetic.ogg")
                textbutton _("寒意渐浓") action mr.Play("bgm/Mysterious.ogg")
                textbutton _("敞开心扉") action mr.Play("bgm/Friendship.ogg")
                textbutton _("云开雾散") action mr.Play("bgm/Luce.ogg")
                textbutton _("星空") action mr.Play("bgm/Night.ogg")
                textbutton _("携手共进") action mr.Play("bgm/Classroom.ogg")
                textbutton _("恶名夫人") action mr.Play("bgm/Claudine.ogg")
                textbutton _("轻若游丝") action mr.Play("bgm/Celine.ogg")


    grid 1 1:
        style_group "music"
        xalign 0.80
        yalign 0.50
        xmaximum 500

        vbox:
            frame:
                style_group "music"
                has vbox

                textbutton _("手忙脚乱") action mr.Play("bgm/Comedy.ogg")
                textbutton _("愁眉苦脸") action mr.Play("bgm/Sad.ogg")
                textbutton _("笑靥如花") action mr.Play("bgm/Mirabel.ogg")
                textbutton _("发自肺腑") action mr.Play("bgm/Confession.ogg")
                textbutton _("哦，圣善夜") action mr.Play("bgm/Oh Holy Night.mp3")


    #grid 1 1:
    #    style_group "music"
    #    xalign 0.80
    #    yalign 0.33
    #    xmaximum 500

    #    vbox:
    #        frame:
    #            style_group "music"
    #            has vbox

    #            textbutton _("Ashes to ashes") action mr.Play("bgm/Track_09.ogg")
    #            textbutton _("You and me") action mr.Play("bgm/Track_10.ogg")
    #            textbutton _("Days gone by") action mr.Play("bgm/Track_11.ogg")

    # Start the music playing on entry to the music room.
    on "replace" action mr.Play()
    on "replace" action Stop("ambience")

    # Restore the main menu music upon leaving.
    on "replaced" action Play("music", "bgm/Casual_Day.ogg")
    on "replaced" action Play("ambience", "sfx/birds.ogg")

init -2:

    style music_button:
        size_group "music"
        background None
        #hover_background "gui/underline.png"
        #selected_background "gui/underline.png"
        ypadding 4

    style music_button_text:
        size 42
        font "fonts/NotoSansSC-VF.ttf"
        idle_color "#8b7460"
        hover_color "#de6743"
        selected_idle_color "5c3e27"
        selected_hover_color "5c3e27"
        insensitive_color "#a38962"

    style music_frame:
        xfill True
        xmargin 2
        ymargin 5
        background None
        top_margin 5
        xpadding 10

##################################

screen notes:

    tag menu

    add "bgs/countryside_d.jpg"

    add "gui/config_ground.png"
    use extras_navigation

    text "制作手记":
        xalign 0.11
        yalign 0.09
        text_align 0.5
        style "main_header"

    viewport:
        mousewheel True
        draggable True
        scrollbars "vertical"
        area (371, 261, 1309, 564)

        vbox:
                text (_("大家好！感谢阅读{i}Embraced By Autumn{/i}，希望你们喜欢！{vspace=20}简单来说，这个故事……是把柯莱特1900-1904年的小说系列{i}《克洛蒂娜》{/i}（尤其是{i}《在学校的克洛蒂娜》{/i}），与Caramel Box 2005年的视觉小说{i}《処女はお姉さまに恋してる》{/i}（Otoboku）揉在一起的产物。我想这就是整部作品与其创作过程的最好概括！哇，这部VN背后的渊源可真深，不是吗？{vspace=20}{i}《Otoboku》{/i}其实是我早年在{i}《Shuffle!》{/i}、{i}《Grisaia》{/i}之类之后接触VN时，最早读过的一部。我很喜欢它的大体设定（一个女性化的男生就读于精致的女校），也很中意那位主角。读到一个男主人公不是被刻画成色狼、对着每个遇到的女性角色流口水（呃，我想主要是因为{i}《Otoboku》{/i}的主角在故事大部分时间里都努力扮演一位有教养的小姐）的VN，实在令人耳目一新。{vspace=20}我太喜欢{i}《Otoboku》{/i}了，以至于想自己也写一部相似设定的VN。我在脑海里反复构思了好几年，也几次动笔尝试，但都在大约一万字左右夭折——我一直找不到一个我足够喜欢、能把角色安放进去的场景。{vspace=20}后来我读到了柯莱特的{i}《克洛蒂娜》{/i}系列，彻底爱上了其中对法国乡村的绝美描绘。故事发生在1890年代，柯莱特笔下的文字极为优美动人，克洛蒂娜则是一位活泼、充满生气的第一人称叙述者。她其实可能是我最喜欢的虚构角色之一；她伶牙俐齿、自信满满，虽然有点小霸王，但讲起话来妙趣横生。{vspace=20}我发觉{i}《克洛蒂娜》{/i}系列太迷人了，于是决定把它的场景与{i}《Otoboku》{/i}的大前提嫁接起来，{i}看吧{/i}——《Autumn》就这样诞生了！{vspace=20}我觉得主角马塞尔与{i}《Otoboku》{/i}的主角瑞穗有很多相似之处：腼腆、内敛，又相当有礼貌。不过考虑到马塞尔在性别表达上的困扰，我不确定称其为“男性”是否完全准确；也许“非二元性别”更贴切一些。所以{i}《Autumn》{/i}与其说是“伪娘故事”，不如说是一个关于角色从始至终对自己的性别有着模糊概念、并不严格男或女的故事。{vspace=20}与此同时，{i}《Autumn》{/i}的其他一些角色则从{i}《克洛蒂娜》{/i}的人物中汲取了灵感——最明显的就是克洛蒂娜本人（{i}意料之中{/i}）。{vspace=20}我太爱柯莱特笔下的克洛蒂娜了，以至于想如法炮制一个自己笔下的小恶魔法兰西学园少女。我的克洛蒂娜与柯莱特的有着相当多的共同点（包括名字、顽皮的性格，以及那位深居简出、醉心学术的父亲），但我觉得我创作的克洛蒂娜要比柯莱特的稍微可爱一些。克洛蒂娜线中的戏剧冲突同样不见于{i}《克洛蒂娜》{/i}系列——因为第一部小说讲的是柯莱特的克洛蒂娜试图追求（并且失败了）她那女性英语老师的芳心。{vspace=20}如果你读过{i}《克洛蒂娜》{/i}系列，或许还能在其他角色身上看到一些对应之处。马塞尔的姨母布吕吉埃夫人，大致受柯莱特的桑让小姐启发（她的形象设计还参考了1937年版法语电影中的桑让小姐）；杜布瓦夫人大致受柯莱特的艾梅·朗特奈启发（这个名字我用在了{i}《黑莓蜜》{/i}中康斯坦丝的教师身上）；米拉贝尔受柯莱特的玛丽启发；诺艾米受柯莱特的阿娜伊斯启发……{vspace=20}不过我想，只有克洛蒂娜与柯莱特的原创角色有大量相似之处；其他角色与各自的灵感原型相差甚远，各路线中的种种戏剧情节都是我自己构思的。{vspace=20}总而言之，我想说的是：如果你喜欢这部VN，请务必读一读柯莱特的{i}《克洛蒂娜》{/i}系列。我深爱{i}《克洛蒂娜》{/i}，也很乐意让更多的人与它相识！{vspace=20}顺带一提，我曾考虑过给诺艾米一条自己的路线，毕竟她是相当重要的配角。事实上她出现在共同线里的时间可能比米拉贝尔还多，哈哈;;{vspace=20}我对诺艾米的路线确实有一个模糊的构想，但还没坐下来动笔。写四条各具特色的女主路线已经够有挑战了，而且{i}《Autumn》{/i}的美术素材量也相当巨大——至少在我的作品里算是了。我以往的作品多倾向于{s}低成本的{/s}极简风格。{vspace=20}今后也许可以考虑给诺艾米一条路线，如果{i}《Autumn》{/i}销量足够好、大家也有兴趣的话。不过即便如此，我也不作出任何承诺。假如你有兴趣读诺艾米的路线，请务必告诉我！任何反馈我都求之不得！{vspace=20}再次感谢你阅读{i}《Autumn》{/i}！希望你喜欢！{vspace=20}- ebi x")) size 30

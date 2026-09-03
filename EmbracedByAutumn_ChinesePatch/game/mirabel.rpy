label Mirabel_route:

    stop music fadeout 1.0
    scene black with wiperight_slow
    $ renpy.pause(0.8)
    $ save_name = (__("{u}米拉贝尔篇{/u}{vspace=1}  9月16日{vspace=1}  物以类聚") )
    play music "bgm/Casual_Day.ogg" fadein 1.0
    show image "border" onlayer border
    scene woodshed:
        subpixel True
        size (1920, 1080) crop (0, 50, 1280, 720)
        linear 25.0 crop (350, 50, 1280, 720)
    with wiperight_slow
    window show dissolve

    "我很快便发现，那间柴房离学校主楼足足有五分钟的路程。"
"这座破败的小屋被树木环绕，看起来几乎像童话里巫婆的屋子。屋顶又低又斜，低到我不得不低下头，免得撞到脑袋。"
"柴房只有一扇小小的窗户，安在高处，透进来的光少得可怜。"
"墙边堆满了柴火，一直垛到天花板。那些木柴堆得摇摇欲坠，我担心只要稍有动作，整堆柴火就会轰然倒塌砸到我身上。"
"锯木屑的气味浓重地弥漫在空气中。它无处不在，浓得几乎令人窒息。"
"我从未待在过这么狭小逼仄的地方——除了那次在旧学校，同学们把我锁进扫帚柜里。"
"这是一种新的体验，但我不太确定它是否令人愉快。"
"这份安宁与寂静，与巴黎繁忙喧闹的街道相比固然是一大改变，可它却让人感到格外荒凉。"
"至少，原本会是如此……"

hide image "border" onlayer border
scene woodshed:
    size (1920, 1080) crop (240, 40, 1440, 810)
show mirabel scared2 w:
    xzoom -1 xpos 0.53 xanchor 0.5
with wipeleft_slow
window show dissolve

Mirabel "玛塞尔……？唔……你还好吗？"
"……要不是身边还有人在。"
"米拉贝尔站在我身旁，用那双灰褐色的眼睛焦灼地朝我眨着。"
"我也说不清，为什么在所有同学里我偏偏挑了米拉贝尔，陪我进行这次小小的冒险。也许是因为，她是唯一一个在听说要和我同去时没有撇嘴唇的女孩。"
"她看起来是个相当不错的女孩，尽管我还不怎么了解她；为人善良、尽责，总是乐于帮忙。"
"看来我的判断也正中要害。米拉贝尔正关切地望着我，十指在身前交叠着。"
show mirabel sad2 w with dissolve
Mirabel "你看起来脸色有点差，唔……而且你还没开始拾柴呢。"
Marcel neutral u "啊，抱歉。"
"我眨了眨眼，回过神来。我在眼前唤起的巴黎幻影——我那奢华的公寓、喧闹的街道、川流不息的马车声——都化作一团灰濛濛的烟雾消散了。"
Marcel "我刚刚在想事情……"
show mirabel neutral2 w with dissolve
Mirabel "那你方才一定想得很出神，才会这样恍惚走神！"
Marcel ehe u "大概是吧。"
Marcel "米耶讷与我从前的生活截然不同，仅此而已。我还需要些时日来习惯。"
show mirabel ehe2 w with dissolve
Mirabel "我可以想象得到——虽说我自己也没多少想象力。"
show mirabel smile2 w with dissolve
Mirabel "我从没去过城里。我想不出那会是什么样子，但想来一定比米耶讷气派得多吧！"
Marcel smile u "米耶讷自有它的迷人之处。"
"我用一个微笑回应了米拉贝尔那焦灼的笑。"
"连我自己都惊讶，原来对着她微笑竟是这般容易。我很少能与人相处得这样融洽；尤其是陌生人。"
"这一定是因为米拉贝尔看起来如此甜美、又如此不设防。"
show mirabel neutral2 w with dissolve
Mirabel "巴黎是不是很喧闹嘈杂？"
show mirabel shy2 w with dissolve
Mirabel "克洛蒂娜几年前去过那儿——我记得她在那儿有亲戚——回来时她便给我们讲了些千奇百怪的故事。"
show mirabel neutral2 w with dissolve
Mirabel "她说马车白天里随时都会驶过街道，还有酒馆整夜开着门，挤满了喝醉的人！"
Mirabel "她说那里的女人穿着最奢华的衣裳，天空里的浓烟比星辰还要多，而歌剧、戏剧、音乐会更是无日不有、随时可去。"
show mirabel shock2 w with dissolve
Mirabel "她说得活灵活现、宛若仙境，简直像是故事里讲的那样！"
Mirabel "她说的该不会是真的吧？我真不敢相信世上竟有那样的地方！"
Marcel neutral u "我在巴黎生活了大半辈子，我可以证实，这座城市一天中大多数时候都相当繁忙，没错。"
Marcel "即便在夜深人静之时，酒馆的窗子里也总亮着灯火；我已不止一次被驶过的马车，或是街上传来的醉汉叫嚷声惊醒……"
show mirabel at bounce
Mirabel "天哪！听起来真不可思议，可也怪吓人的！这一点也不像米耶讷！"
Mirabel "在这里，所有店铺五点就打烊了，我父母十点就熄灯入睡！"
show mirabel shy2 w with dissolve
Mirabel "我上床睡觉时，屋里总是漆黑一片。"
Marcel "难道村民们晚上不留在酒馆里喝酒吗？"
show mirabel neutral2 w with dissolve
Mirabel "有时会的，若是碰上什么节庆的话；可大多数村民第二天还得早起上工呢。"
Mirabel "住在米耶讷的人，大多在农场里劳作。"
Marcel smile u "说得通。巴黎可没有那么多可耕种的农田……"
show mirabel shock2 w with dissolve
Mirabel "我想也是吧！"
"米拉贝尔朝我眨了眨眼，仿佛她从未想过要在鹅卵石道路上耕种庄稼、饲养羔羊有多难。"
show mirabel neutral2 w with dissolve
Mirabel "既然种不了庄稼，巴黎人靠什么挣钱呢？"
Marcel neutral u "他们大多是做小生意的；至于开不起自家店铺的人，便在店里当伙计，或是去富人家中当仆役……"
"我回想起我的父亲：尽管上了年纪，却毋庸置疑地英俊，轻浮得无可救药，更是巴黎报纸源源不断的丑闻素材。"
Marcel "还有些人甚至靠当画家、演员或乐师谋生。"
Mirabel "你说演员？就是那些登台演戏的人吗？"
Marcel "是这样。"
Mirabel "真是稀奇……"
show mirabel shock2 w with dissolve
Mirabel "我还从没看过戏。我真不明白，怎么会有人靠扮演别人来谋生。"
Mirabel "光是做我自己，已然让我觉得艰难，更何况去当另一个女孩——甚至一个男孩！"
Mirabel "演员一定很了不起。"
Marcel smile u "有这种感受的，不止你一个。"
"我试图给米拉贝尔一个安慰的微笑。"
Marcel "有时，我也觉得做自己很难。"
"我不确定自己搬到米耶纳，是让这一切变得更难了，还是更容易了。"
Mirabel "可对你来说一定不一样吧！你可是从巴黎来的！你们巴黎人一个个都那么时髦又自信！"
Marcel neutral u "并非人人如此……"
show mirabel ehe2 w with dissolve
Mirabel "也许不是人人如此，可我得知这一切后，实在吃惊得很。"
show mirabel shy2 w with dissolve
Mirabel "我知道，这话从我这样已经长大的姑娘嘴里说出来或许显得很蠢，但……"
show mirabel ehe2 w with dissolve
Mirabel "我以前总以为整个法国——不，是全世界！——都跟我家乡米延一样。"
show mirabel neutral2 w with dissolve
Mirabel "克洛蒂娜跟我讲起她在巴黎的那些日子时，我惊讶得不得了，还以为她准是在说谎。"
show mirabel sad2 w with dissolve
Mirabel "她和诺艾米总爱捉弄我。她们觉得我是个蠢蛋。也许她们说得没错……"
Marcel neutral u "我不觉得你是个蠢蛋。你没去过巴黎，自然不知道那儿是什么样子，这很平常。"
Marcel smile u "我刚到米延的时候也很惊讶。我从没见过那样多的绿意。"
show mirabel laugh2 w with dissolve
Mirabel "呵呵……"
"米拉贝尔羞涩地轻声笑了。"
show mirabel smile2 w with dissolve
Mirabel "那么，谢谢你这么体贴。"
show mirabel neutral2 w with dissolve
Mirabel "别的女孩对我都不好。尤其是诺艾米，简直霸道得很——不过克洛蒂娜也差不了多少。"
show mirabel sad2 w with dissolve
Mirabel "我不肯相信她讲的巴黎那些故事时，她笑话我。她说我的想象力跟一块石头差不多。"
Mirabel "这点上她也许说得没错，就像她说巴黎时说对了一样。"
"米拉贝尔又摇了摇头。"
show mirabel shock2 w at bounce
Mirabel "演员！我真不敢相信。"
Mirabel "我永远、{i}永远{/i}也做不来那种事。"
show mirabel sad2 w with dissolve
"米拉贝尔看起来如此沮丧，我几乎为自己回答了她的问题而感到愧疚。"
"她似乎是那种只要有机会就会苛责自己的人，或许是因为同学们嘲弄的缘故。"
"她的自尊心想必很低。"
"如果真是这样，那我感同身受。生为这样一位光彩夺目、魅力非凡的父亲的孩子，我太了解那种滋味了。"
"出于对米拉贝尔心情的体恤，我试着转移话题。"
Marcel neutral u "如果不介意我多问一句，你家里人是靠什么过活的？"
show mirabel neutral2 w with dissolve
Mirabel "他们在村里开着一间小面包店。我偶尔会去帮帮忙。"
show mirabel ehe2 w with dissolve
Mirabel "其实我烤面包还挺拿手的。那是我少数几样还算擅长的事。"
"……可是，尽管我竭力周旋，米拉贝尔似乎铁了心要把话题拉回她自己的失败上。"
show mirabel sad2 w with dissolve
Mirabel "我不会穿针引线，唱歌怎么都找不准调，字也写得又大又幼稚……"
Mirabel "我很惊讶你会让我陪你去柴房，偏偏是挑了我这样的。"
Marcel "这有什么好惊讶的？"
show mirabel shock2 w with dissolve
Mirabel "因为你是个聪明的巴黎姑娘呀！你一定上过好些的学校！我敢说你懂好多我不懂的东西，比如芭蕾、弹琴，还有……我说不上来。拉丁文？"
"她说拉丁语说得没错（我学了好几年拉丁语，深恶痛绝），可我从未练过芭蕾，而要我演奏乐器，那和让我飞上月球一样不可能。"
"我试图宽慰她，但米拉贝尔不给我机会。她皱起额头，发出一声沮丧的轻叹。"
show mirabel shy2 w with dissolve
Mirabel "你怎么会愿意跟一个像我这样乏味无趣的姑娘待在一起？"
Marcel smile u "我想跟你待在一起，是因为你看起来人很好。我不觉得还需要比这更深的原因。"
show mirabel shock2 w with dissolve
Mirabel "可我在你眼里一定无聊透顶！我根本没什么特别的地方。"
show mirabel sad2 w with dissolve
Mirabel "你跟克洛蒂娜待在一起会更有意思。"
Marcel frown u "可我不{i}想{/i}跟克洛蒂娜待在一起。"
show mirabel shock2 w with dissolve
Mirabel "你……"
"米拉贝尔眨了眨眼。她被我的回答惊得目瞪口呆，我倒不如直接告诉她我喜欢吃铅笔芯算了。"
Mirabel "你不想……？"
Marcel sigh u "我相信她会是个有趣的同伴，不过……倒也谈不上特别想，不。"
Marcel neutral u "我太习惯被吵吵嚷嚷的人围着了，如今既然离开了巴黎，我想我宁可换换节奏。"
Mirabel "可克洛蒂娜又聪明又风趣又好笑！我觉得连布吕吉埃夫人都喜欢她，尽管克洛蒂娜总是跟她顶嘴。"
show mirabel neutral2 w with dissolve
Mirabel "没有人会不喜欢克洛蒂娜。至于我——"
show mirabel sad2 w with dissolve
Mirabel "我不过是个样样都不行的失败者。"
Marcel sad u "米拉贝尔……"
"我上上下下打量了米拉贝尔一番。"
"她这般自我苛责，就算在我看来也有些过分，但我也能理解她的心情。"
"米拉贝尔不敢与人目光相接，又总是自我轻贱，这让我想起了过去那个自己。"
"若她是个男孩，这些举止会让她被打上懦夫的标签……{w}可身为女孩，这份腼腆或许反会被视为可爱。"
"她并不算符合世俗标准的美人，圆脸，眼神迟钝而呈褐色，可她笑起来却很甜美。"
"我想成为她的朋友。"
"至少，我希望自己能做到。"
"在她那近乎粉碎的自我认知面前，此刻想要与她建立一段情谊或许并不可能，但……"

stop music fadeout 3.0

Marcel neutral u "我明白你的心情，可跟谁相处，该由我来决定。"
Marcel "我这一生大半都活在怕人的阴影里，躲着同窗，如今我已经厌倦了。"
Marcel frown u "我想主宰自己的人生。"

window hide dissolve
play sound "sfx/footsteps3.ogg" fadein 0.5
play music "bgm/Confession.ogg" fadein 1.0
scene cg32 with wiperight_slow
$ renpy.pause(0.8)
window show dissolve
stop sound fadeout 0.5

Mirabel "玛、玛塞尔……？"
"米拉贝尔焦虑地望着我。"
"在激情的冲动下，我一定向前迈了一步，因为我此刻离米拉贝尔比刚才近了许多。"
"我的手指搭在她的肩上，但我没有把指甲掐进她的肌肤。我不想伤害她。我只想让她明白我的感受。"
Marcel "你一直都在讲自己所谓的那些缺点，可那些我一点也不在乎。"
Marcel "不管你怎么看待你自己，我照样想跟你说话……"
Marcel "而且，日子久了，我还想成为你的朋友。"
Mirabel "我、我的朋友……？！"
Marcel "是这样。"
Mirabel "你真好……"
"米拉贝尔羞涩地移开目光，不敢与我对视。"
Mirabel "班上的女孩子没有一个人理会我。她们都觉得我是个可怜、愚蠢又迟钝的女孩……"
Mirabel "从来没有人说过想跟我待在一起。至少，好久都没有过了。"
Mirabel "我、我真的很荣幸，可我不晓得自己会不会是个好朋友。克洛蒂娜——"
Marcel "我已经跟你说过了，我没兴趣当克洛蒂娜的朋友。我更愿意跟你说话。"
Mirabel "好吧，要是你真不嫌弃……"
"米拉贝尔咬住了嘴唇。"
Mirabel "我不想让你失望……"
Marcel "不会的。别担心。"
Marcel "你不必做天底下最聪明的姑娘，也不必最风趣、最机智。"
Marcel "我过去的学校里尽是些聪明、风趣、机智的人，可我跟他们向来合不来。他们仗着自己的聪明来取笑我。"
Mirabel "你、你也被人取笑过？"
Marcel "被取笑得很惨。"
Marcel "这正是我搬到这儿来的原因之一。我在城里活不下去。"
Mirabel "可她们为什么要取笑你呢？你比我漂亮得多得多，看起来也聪明得多。真说不通……"
Marcel "也许说不通，可事情就是这样。"
Marcel "我知道被人欺负是什么滋味。所以我才想当你的朋友。不管你怎么说你自己，我觉得你是个好人。"
Marcel "我知道我们认识彼此的时间还不长，可是……"
Marcel "我喜欢你。"
Mirabel "玛、玛塞尔……"
"米拉贝尔的脸愈发通红。"
"我担心自己有点说得太过头了（我从未求过任何人做我的朋友，对这一切还很生疏），不过话又说回来，米拉贝尔在贬低自己时也毫不留情面。"
"她既如此极端地贬损自己，那我就得尽力把她重新扶起来。"
"倘若米拉贝尔在米延过得并不快乐，那我想帮帮她。我不愿她像我当年在巴黎那样，感到那般悲伤与孤独。"
"倘若我搬到乡下，也能对别人产生一些好的影响，那倒也不错。"
"幸运的是，我逗米拉贝尔开心的努力似乎奏效了。"
"米拉贝尔抬起头来，脸上仍因羞涩而泛着淡淡的粉红。她的目光与我的相遇。接着，在短暂的停顿之后……"
Mirabel "你竟然还说{i}我{/i}好！你肯定是我见过的心地最甜的姑娘了！"
"……米拉贝尔向我绽开一个明媚而温暖的笑容。"
Mirabel "谢谢你这么体贴，玛塞尔！我不晓得自己配不配得上……"
Mirabel "但我真的很高兴能遇见你！"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}米拉贝尔篇{/u}{vspace=1}  9月16日{vspace=1}  志同道合") )
play music "bgm/Night.ogg" fadein 1.0
play ambience "sfx/night_amb2.ogg" fadein 1.0
scene cg28 with wiperight_slow
window show dissolve

"那晚稍晚时分，我躺在床上，望着墙壁。"
"无论我怎样辗转反侧，都始终无法入睡。"
"这张床的被单远比巴黎家中那些要薄，而且太短，无法将我完全盖住。"
"我赤裸的脚从被单下露了出来，脚趾在卧室的寒意中蜷曲着。"
"这张床垫实在劣质，我能感觉到每一处凹凸不平。"
"在巴黎，无论何时街上都挤满了人。而在米延，却几乎静谧得有些诡异。"
"四下如此静止沉寂，没有什么能让我不去留意自己身体发出的声响。"
"我的心跳声听起来近乎不自然地响亮，我甚至发誓能听见自己的血液在血管中奔流。"
"我感到自己如此脆弱，就连盖在身上那薄薄的一层被单，都仿佛在将我压垮。"
"我一遍又一遍地在脑海里回放着今天发生的事，就像从前我入睡前，母亲常把发刷的鬃毛一遍遍梳过我的头发。"
"我认识了新同学，上了几堂课，还结识了一个我希望将来能日渐亲近的相识。"
"不，不只是相识，而是朋友。"
"米拉贝尔。"
"在我执拗地紧闭的眼睑之下，我在脑海中想象出一个幻影般的米拉贝尔。"
"她相当矮小——比我矮得多——有着并不出众的棕色头发、分得很开的棕色眼睛，以及一张柔软、近乎面团般的脸。"
"她并不特别迷人。无论多么宽厚的诗人，也绝不会把她的容貌比作女神，或是海中的仙女……"
"但是，当她笑起来时，却显得十分动人。"
"可惜的是，我觉得她并非那种经常微笑的女孩。"
"常年被自我怀疑压垮，米拉贝尔的肩膀总是耷拉着，这让她看起来比她本来的样子更矮小、更敦实。"
"我希望她能多些自信。"
"她的微笑几乎有脱胎换骨的力量，眼见着她皱眉，实在是一种浪费。"
"如果可能的话，我希望将来能让她多笑一笑。"
"除了母亲之外，我从未真正让谁快乐过，这是一种令人愉悦的感觉，让我觉得自己有了用处。"
"我想帮助米拉贝尔，或许她也能反过来帮到我。"
"也许我们能够一同克服各自的焦虑。我只能这样希望了。"

stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene sky g with clockwipe
$ renpy.pause(0.5)
show overlay2
show message18 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message18
hide logo2
hide overlay2
with datetrans2

$ renpy.pause(0.3)

$ save_name = (__("{u}米拉贝尔篇{/u}{vspace=1}  9月17日{vspace=1}  玛丽-诺埃尔") )
play ambience "sfx/birds.ogg" fadein 1.0
scene sky with dissolve
window show dissolve

"第二天，吃过早餐后，我在庭院里散步。"
"尽管已是深秋时节，今天却很温暖。"
"夏日阳光的最后几缕残辉执拗地透过云层洒落下来，仿佛迫不及待地想提醒我们所有人，太阳依然存在。"

stop ambience fadeout 1.0
play ambiencee "sfx/footsteps2.ogg" fadein 1.0
show image "border" onlayer border
scene yard:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

"树上的叶子呈现出令人惊叹的红、黄、棕诸般色彩。哪怕最轻微的风吹过，它们便沙沙作响，有几片叶子脱离枝头，懒洋洋地在空气中飘荡。"
"这是个宜人的日子，我想趁着还来得及，好好享受这晴朗的天气。"
"怀着这个念头，我漫无目的地徘徊着，心中没有既定的方向，如同一片浮云……"

play music "bgm/Comedy.ogg" fadein 1.0
stop ambiencee fadeout 1.0
hide image "border" onlayer border
scene yard:
    size (1920, 1080) crop (240, 40, 1440, 810)
show mirabel smile2:
    xzoom -1.0 xpos 0.30 xanchor 0.5
show marie smile2:
    xpos 0.70 xanchor 0.5
with wipeleft_slow

Mirabel "哎呀，玛丽-诺埃尔！你该小心些才是，你这小傻瓜！"
"……直到一个熟悉的声音将我从沉思中唤醒。"
"米拉贝尔站在校园中央的水泵旁。她的头发仍扎成那两条熟悉的短辫，嘴唇因忧虑而紧抿着。"
"她也不是独自一人。"

show image "border2" onlayer border
scene yard blur:
    subpixel True
    size (1920, 1080) crop (320, 0, 1280, 720)
    linear 19.0 crop (320, 200, 1280, 720)
show marie smile2:
    subpixel True
    size (1920, 1080) crop (-160, 140, 1280, 720)
    linear 19.0 crop (-160, 340, 1280, 720)
with dissolve

"米拉贝尔身旁站着一个小女孩——看模样年纪还很小——剪着短发，发丝像牧羊人的那样卷曲着环在脸旁。"
"这女孩身形十分娇小，眼睛又大又圆，镶着长长的睫毛。"
"我想她一定是幼儿班的学生；大概七八岁的样子。"
"小女孩的脸颊上沾着饼干屑，裙子的前襟上也有一小块果酱渍。"
"米拉贝尔打量着这女孩，发出啧啧的咂舌声，活像个无可奈何的母亲。"

hide image "border2" onlayer border
scene yard:
    size (1920, 1080) crop (240, 40, 1440, 810)
show mirabel smile2:
    xzoom -1.0 xpos 0.30 xanchor 0.5
show marie smile2:
    xpos 0.70 xanchor 0.5
with dissolve

Mirabel "来，过来。我们得把你收拾干净，好让你漂漂亮亮、干干净净的！"
show marie pout2 at twirl
Marie "唔……？我不要……"
"那女孩（我记得米拉贝尔叫她玛丽-诺埃尔）噘着嘴，想从米拉贝尔身边挣脱。"
"不过，米拉贝尔显然早有预料，她紧紧扣住了这个小小被托付者的手指。"
show mirabel neutral2 with dissolve
Mirabel "不管你愿不愿意都没用。你总不能顶着这副像是被人从树篱里拖出来的样子去上早课吧！你老师看见了会怎么说？"
show marie sad2 with dissolve
Marie "嗯……"
"玛丽-诺埃尔用黑皮鞋的鞋尖踢着一颗松动的石子。"
Marie "她会不高兴的……"
Mirabel "说得对，她会不高兴。说不定会让你丢人地站到外面去，说不定连指节都会被戒尺敲打！"
show marie shock2 at bounce
Marie "戒、戒尺……？"
"玛丽-诺埃尔抽了抽鼻子。她那湛蓝明亮的眼睛里开始盈满泪水。"
show marie scared2 with dissolve
Marie "我不想那样……"
Mirabel "而{i}我{/i}也不希望你落到那步田地。我太在乎你了，舍不得让你受罚！"
show mirabel smile2 with dissolve
Mirabel "所以我要把你嘴边的面包屑擦掉，然后再试着想办法对付那块污渍……"
"米拉贝尔看向那女孩裙前抹着的那一坨草莓果酱。"
show mirabel ehe2 with dissolve
Mirabel "还好咱们的校服是黑的，否则那块污渍就会显眼得要命。要是裙子是白的，那就怎么也弄不掉了！"
show marie shock2 at bounce
Marie "什么？可米拉贝尔你什么都会呀！"
show mirabel ehe2 with dissolve
Mirabel "别犯傻了，小傻瓜。我也不是什么都擅长。其实，大多数事我都不擅长……"
Marie "可你总是照顾我！你就像个大人一样！"
Mirabel "比起你来，我{i}确实{/i}是个大人了。"
show mirabel smile2 with dissolve
Mirabel "好了，站好别动。我来给你擦脸。"
show marie neutral2 with dissolve
Marie "好……"
play ambience "sfx/bath.ogg" fadein 1.0
"米拉贝尔把手帕放到水泵下，然后拉动水泵的摇柄。"
"手帕既已沾湿，她便把注意力转向玛丽-诺埃尔。"
stop ambience fadeout 1.0
"米拉贝尔蹲下身来，裙摆拖曳在地上，用手帕的边缘轻轻擦拭玛丽-诺埃尔沾着糕点屑的脸颊。"
show mirabel neutral2 with dissolve
Mirabel "我是不是擦得太重了？"
"玛丽-诺埃尔摇了摇头，米拉贝尔便啧啧地咂舌。"
Mirabel "好了，好了！我不是叫你别动嘛。"
show marie huh2 at bounce
Marie "哦……对不起……我忘了。"
show mirabel laugh2 with dissolve
Mirabel "你这姑娘记性可真差！难怪今早连自己的早餐都泼了一身！"
show marie sad2 with dissolve
Marie "别的姑娘都笑话我。她们说我老是白日做梦。"
show mirabel smile2 with dissolve
Mirabel "你的心思准是飘到老远去了，脸上才会沾了这么多面包屑！"
Marie "我不过是在想些事儿……"
show mirabel laugh2 with dissolve
Mirabel "要紧的事？"
Marie "也不算。就是些平常事。"
show marie pout2 with dissolve
"玛丽-诺埃尔噘起了嘴。"
Marie "我不是故意弄得这么脏的。是不知不觉就……"
show mirabel smile2 with dissolve
Mirabel "我知道。我不信你是故意的。"
show marie sad2 with dissolve
Marie "你没生我的气吧……？"
Mirabel "我为什么要生气呀，你这小古怪？对你，我可气不起来！"
Marie "可你总是关照我……我不想碍你的事……"
show mirabel laugh2 with dissolve
Mirabel "我关照你是因为我愿意，傻瓜！"
"米拉贝尔用食指指尖戳了戳玛丽-诺埃尔的鼻子。这个小同伴为了把目光牢牢盯在米拉贝尔的指头上，一时竟成了斗鸡眼。"
Mirabel "你没有碍我的事。能跟你待在一起，我很开心！"
show marie huh2 with dissolve
Marie "我让你开心吗？"
Mirabel "当然！"
show marie sad2 with dissolve
Marie "我不知道……"
"玛丽-诺埃尔垂下目光，望向地面。她盯着自己那双穿在磨损的黑皮鞋里的脚，皱起了眉头。"
Marie "我不觉得自己让{i}任何人{/i}开心。"
show mirabel neutral2 with dissolve
Mirabel "那你为什么这么说？"
Marie "我爸妈把我送到这所学校，已经好几个月没来看我了……"
Marie "因为我走神，老师冲我发火；同学们也都取笑我。"
show mirabel neutral2 with dissolve
Mirabel "哎，别理会他们。他们不过是嫉妒你。"
show marie shock2 with dissolve
Marie "他们为什么要嫉妒我……？"
Mirabel "因为你是个温柔善良的好姑娘，又可爱得不得了！"
show marie sad2 with dissolve
Marie "可、可爱？我才不……"
show mirabel shock2 with dissolve
Mirabel "你就是！"
"咦，为什么这番对话听来如此熟悉？"
"这简直就像昨天我与米拉贝尔在柴棚里的交谈，只不过角色对调了过来。"
"其实还挺有趣的。"
"遗憾的是，玛丽-诺埃尔和先前的米拉贝尔一样，似乎并不打算接受这一点。"
show marie neutral2 with dissolve
Marie "要是我真那么可爱，那我爸妈怎么还不来看我？！"
show mirabel neutral2 with dissolve
Mirabel "这个我可不敢装作知道，小宝贝。我没见过你父母，但我敢肯定，不得不离开你这么可爱的女儿，他们心里一定很难受。"
show marie huh2 with dissolve
Marie "你怎么知道……？"
Mirabel "他们每周都给你寄糖果和信来，对不对？"
show marie neutral2 with dissolve
Marie "嗯，那倒是真的……"
show mirabel laugh2 with dissolve
Mirabel "你不记得上个月收到的那几颗漂亮开心果软糖了吗？那可真好吃呀！"
show marie sad2 with dissolve
Marie "糖果是很好，可我更想见到我的妈妈和爸爸……"
show mirabel smile2 with dissolve
Mirabel "我相信你想，可他们一定太忙了。他们不是在国外工作吗？"
Marie "爸爸和妈妈在意大利。我想跟他们一起去，可他们说我必须留在法国……"
show mirabel laugh2 with dissolve
Mirabel "那等他们从意大利回来，我相信他们见了你一定会很高兴！"
show marie huh2 with dissolve
Marie "你真的这么觉得……？"
Mirabel "当然啦！他们会张开双臂，把你搂进怀里大大地抱一抱，然后你想吃多少开心果软糖，他们就喂你多少！"
"玛丽-诺埃尔露出怀疑的神情。"
show marie angry2 with dissolve
Marie "我要是吃那么多软糖，会吃坏肚子的。"
Mirabel "那你可以分一些给我呀！"
show marie shock2 with dissolve
Marie "哦，对呀！好主意！我会把所有的糖果都分给你！算是谢谢你对我这么好！"
show mirabel ehe2 with dissolve
Mirabel "我对你好，可不是图你拿糖果来谢我，傻孩子！"
"米拉贝尔笑了，用指节轻敲玛丽-诺埃尔的头顶。"
show mirabel smile2 with dissolve
Mirabel "不过，既然你愿意帮忙，我当然不会拒绝，只是我大概该多注意一下自己的体重……"
show mirabel ehe2 with dissolve
Mirabel "班上有几个女生说话真是刻薄……"
show marie huh2 with dissolve
Marie "像克洛蒂娜那样？"
show mirabel sad2 with dissolve
Mirabel "就跟克洛蒂娜一模一样。"
"玛丽-诺埃尔打了个寒颤。"
show marie scared2 with dissolve
Marie "我觉得你们这些大女孩比我老师还要吓人。"
show mirabel shock2 with dissolve
Mirabel "那么你是觉得{i}我{/i}很吓人喽？"
show marie shock2 at bounce
Marie "啊！才没有呢！"
show marie smile2 with dissolve
Marie "你是我认识的最善良、最亲切的女孩！"
show mirabel laugh2 with dissolve
Mirabel "哎呀，真是太谢谢你啦！这话对我来说很重要。"
show mirabel smile2 with dissolve
Mirabel "好了……"
"米拉贝尔把手帕从玛丽-诺埃尔的脸颊上移开。"
Mirabel "你的脸看起来光洁又明亮，就像镜面一样！"
show marie shock2 with dissolve
Marie "这么说，你能在我的脸上看到{i}你{/i}的脸吗？！"
show mirabel ehe2 with dissolve
Mirabel "这个么……倒也不全是……"
show mirabel laugh2 with dissolve
Mirabel "我只是说你看起来干干净净！你美得像幅画一样！"
show marie neutral2 with dissolve
Marie "一幅镜子的画……？"
show mirabel neutral2 with dissolve
Mirabel "谁会想买一幅镜子的画呀？在画里还能看见自己的倒影吗？"
Marie "我不知道。我以前从没见过镜子的画。"
Mirabel "我也没见过……"
"米拉贝尔的声音渐渐低了下去。她出神地凝望远方片刻，心不在焉，最终才回过神来。"
show mirabel laugh2 with dissolve
Mirabel "好啦，不说这个了！我们来看看你的裙子吧。"
"玛丽-诺埃尔带着几分怀疑，看着自己裙前那块惹眼的果酱渍。"
show marie huh2 with dissolve
Marie "你确定能洗干净吗？脏的地方好多啊……"
show mirabel smile2 with dissolve
Mirabel "我不知道能不能把它洗得像你的脸一样干净，但我会尽力试试。"
Mirabel "要是我用这块手帕，应该能把最脏的地方擦掉……"
show marie sad2 with dissolve
Marie "可是那样你的手帕也会弄脏呀。你不介意吗？"
Mirabel "我不介意。等我帮你清理干净后再洗手帕就是啦！现在别动，小鸭子。"
show marie huh2 with dissolve
Marie "好……"
"玛丽-诺埃尔点头应允。她的声音从唇间滑落，轻柔而甜美，宛如天使的嗓音。"
show marie neutral2 with dissolve
"她的声音太轻，我都有点听不清。"
"那风声虽轻，却几乎要把她的声音卷走，就仿佛地上散落的那些松脱的秋叶一般。"
"米拉贝尔把手帕按到玛丽-诺埃尔的裙前。她擦拭了好一会儿，专注间舌头从嘴角微微探出。"
"她如此专注于玛丽-诺埃尔，我都不确定她有没有察觉到，自己裙摆正拖在泵下积水的水洼里。"
"也许我该提醒她……？"
"然而，米拉贝尔看起来如此沉醉于她的差事，我不愿打扰她。"
"我想我以前从未见过她如此认真的模样。"
"尽管米拉贝尔昨天向我细数了种种所谓的缺点，但她应付小孩子却格外在行。"
show mirabel neutral2 with dissolve
Mirabel "嗯……"
"米拉贝尔终于从玛丽-诺埃尔的裙前退开，右手还攥着手帕。"
Mirabel "我已经把最重的污渍擦掉了，不过果酱很黏，很难全部弄干净。"
Mirabel "我想不会有人注意到的，不过要是你有干净制服的话，明天恐怕得换一件。"
"米拉贝尔用审视的目光打量着玛丽-诺埃尔。"
Mirabel "你有吗？"
show marie huh2 with dissolve
"玛丽-诺埃尔点了点头。"
show mirabel smile2 with dissolve
Mirabel "那以后就穿那件吧，等洗衣日到了再把这件洗干净。"
Marie "好……"
show mirabel neutral2 with dissolve
Mirabel "玛丽，你有几件校服？"
show marie neutral2 with dissolve
Marie "只有两件；这一件，还有另一件。"
Mirabel "那你可得小心别再把果酱沾到另一件裙子上，不然你这一整个星期都得穿着黏糊糊的衣服！"
show marie huh2 with dissolve
Marie "我、我会尽力的！"
show mirabel smile2 with dissolve
Mirabel "好孩子。你答应我会更小心吗？"
show marie sad2 with dissolve
Marie "我答应你……"
show mirabel laugh2 with dissolve
Mirabel "那我们就用一个吻来立下这个誓约吧！"
"米拉贝尔低下头，飞快地在玛丽-诺埃尔那已完全擦干净、透着粉红的脸颊上印下一吻。"

play sound "sfx/rustle.ogg"
scene yard
show mirabel smile:
    xzoom -1 xpos 0.3 xanchor 0.5
show marie smile:
    xpos 0.7 xanchor 0.5
with dissolve

"两人的约定一经缔结，米拉贝尔便站起身来。她用手拍了拍校服裙（我想她还没意识到裙子已经湿了），然后笑了。"
Mirabel "好啦，玛丽-诺埃尔。你的课马上就要开始了吧？"
show marie shock at bounce
Marie "哦，是啊，你说得对！"
Mirabel "那你该动身了。我可不想你迟到。"
show marie smile with dissolve
Marie "好、好的。我这就走！"
show marie laugh with dissolve
Marie "真是太谢谢你了，米拉贝尔！"

stop music fadeout 1.0
play sound "sfx/rustle.ogg"

show marie:
    xzoom -1
with dissolve

$ renpy.pause(0.3)

show marie:
    ease 1.2 xpos 1.3

$ renpy.pause(0.3)

show mirabel:
    ease 0.8 xpos 0.5

"说完这些轻柔的、带着口音的话语，玛丽-诺埃尔转身朝自己的教室奔去。"

play music "bgm/Friendship.ogg" fadein 1.0

"米拉贝尔目送她离去，脸上带着母亲般的微笑。"
"米拉贝尔似乎并不在意，我们的课程也像玛丽-诺埃尔的一样，很快就要开始了。"
"我时刻盼着远处教堂的钟声随时响起，宣告我们每日课程的开始。"
"然而，钟声却始终静默。寂静笼罩着庭院，只有风声和树上的沙沙叶响打破这份安宁。"
"几个穿着校服的女孩远远地从我们身旁走过（我想我能认出其中的露丝），但她们没有停下来和我们说话。"
"没有人在意我们。"
"离上课应该还有几分钟。"
"也许我该借此机会和米拉贝尔聊聊？"

play sound "sfx/rustle.ogg"
scene yard:
    size (1920, 1080) crop (240, 40, 1440, 810)
show mirabel smile2:
    xzoom -1 xpos 0.5 xalign 0.5
with dissolve

Marcel neutral u "那个，米拉贝尔……？"
"我终于向她走去，我那双朴素的校鞋把脚下的草叶踩得低伏。"
Marcel smile u "早安。很高兴又见到你。"
show mirabel shock2 at bounce
Mirabel "哦——玛塞尔！"
"米拉贝尔从出神中被拉了回来，转身看向我。她眨了眨眼，像是要驱散眼里的什么东西，然后迟疑地笑了。"
show mirabel ehe2 with dissolve
Mirabel "早、早安！我也很高兴见到你……"
"米拉贝尔同玛丽-诺埃尔说话时那份从容的自信不见了。如今，她看起来与昨天在柴棚里时一样：害羞、局促，并不完全清楚该拿自己的手怎么办。"
"她局促地把手放在身前，十指交握，随即又松开。"
"但愿我没有那么吓人。"
"我请求米拉贝尔做我的朋友，但我想她还不太信任我。"
"算了。还有时间来慢慢培养。我们不必立刻成为莫逆之交。"
Marcel huh u "我想很快就打上课铃了。我们该去上课了，不然布吕吉埃夫人会责骂我们的。"
show mirabel sad2 with dissolve
Mirabel "布吕吉埃夫人总是责骂我，不管我迟没迟到……"
show mirabel ehe2 with dissolve
Mirabel "不过你说得也有道理。"
"米拉贝尔勇敢地笑了笑。"
Mirabel "谢谢你为我操心。"
Marcel smile u "这没什么。我看你似乎想得出神，觉得该提醒你一声……"
show mirabel laugh2 with dissolve
Mirabel "哦，我哪有什么想得出神。我不是早就跟你说过，我根本没有那样的想象力吗！"
Marcel sad u "米拉贝尔……"
"我皱了皱眉。"
"我觉得她在开玩笑，但她对自己那个所谓的‘玩笑’信得太深，以至于一点也不显得好笑。"
Marcel "我觉得你不该这样贬低自己。这样对身体不好……"
show mirabel ehe2 with dissolve
Mirabel "哈哈哈……这个，嗯……"
Mirabel "算了，别提那个了。这没什么要紧的。"
play ambience "sfx/footsteps2.ogg" fadein 1.0
show mirabel:
    ease 3.0 xpos 1.10
"我对这一点不太确定，但还没来得及开口评论。米拉贝尔已经大步走在我前面，手臂像士兵一样摆动着。"
Mirabel "好、我们走吧，好吗？"

show image "border" onlayer border
scene yard:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

"我连忙跟上去，脚下的草叶和落叶沙沙作响。"
"我们走着的当儿，我心中涌起许多疑问。我不想打探，但是……"

stop ambience fadeout 2.0
hide image "border" onlayer border
scene yard:
    size (1920, 1080) crop (240, 40, 1440, 810)
show mirabel neutral2:
    xzoom -1 xpos 0.5 xalign 0.5
with wipeleft_slow

Marcel neutral u "我刚才恰好看到你和一个女孩在说话……"
Mirabel "一个女孩？你是说玛丽-诺埃尔？"
Marcel "没错，是叫这个名字。我不是故意偷听的，只是正好听到了一点点你们的谈话。"
Marcel smile u "你似乎很喜欢她。"
show mirabel ehe2 with dissolve
Mirabel "其实大多数孩子我都很喜欢。跟她们说话很轻松。至少比跟班上的同学轻松……"
"米拉贝尔的脸红了。"
show mirabel shy2 with dissolve
Mirabel "我、我知道这话听起来也许很傻，可我从来都不太擅长和同龄的女孩子相处。"
Marcel "我不觉得这听起来傻。"
show mirabel shock2 at bounce
Mirabel "你、你不觉得吗？"
Marcel neutral u "不觉得。"
"我一向也不怎么擅长与同龄男孩相处。"
"我就读的学校里，那些比我小的男孩远比我的同窗友善，仅仅是因为我比他们高出许多，他们敬畏我。"
"那些小男孩还没能弄明白，我是多么被人嫌弃、受人嘲讽。"
"他们不知道和我说话无异于社交自杀——即便知道，我怀疑五六岁的稚龄孩童也不会放在心上。"
"小孩子通常不像年长者那般恶毒，单单是因为他们天生对年长于自己的人怀有太多敬意。"
Marcel smile u "小孩子没那么爱评头论足，不是吗？她们不会取笑人，也不会说刻薄话。"
Marcel "别人对她们好，她们也对别人好。她们容易懂，也好相处。"
show mirabel laugh2 with dissolve
Mirabel "这正是我心里想的！真高兴你能懂我！"
show mirabel ehe2 with dissolve
Mirabel "班上的女生觉得我无聊、愚钝又迟钝。她们想，要是和我待在一起，也会被打上无聊、愚钝又迟钝的印记。"
Mirabel "那些小孩子就没那么刻薄了。我跟她们说话时，她们总是很感激的样子，也喜欢和我一起玩。"
show mirabel neutral2 with dissolve
Mirabel "也许是因为大一点的女孩都不理她们，老师们又把她们当成麻烦。"
show mirabel smile2 with dissolve
Mirabel "我想她们很珍惜这份关注。"
Marcel neutral u "那玛丽-诺埃尔是你最喜欢的一个吗？"
Mirabel "我不喜欢挑什么偏爱，不过我想她算是其中之一吧。"
show mirabel laugh2 with dissolve
Mirabel "她真的很可爱！"
show mirabel smile2 with dissolve
Mirabel "她的父母都住在意大利，为了让她接受法国教育，把她留在了这所学校。她非常想念他们，朋友也不多……"
Marcel huh u "所以你才去和她说话？"
show mirabel neutral2 with dissolve
Mirabel "我尽量陪在她身边。其他女孩老是欺负她。"
show mirabel sad2 with dissolve
Mirabel "我想她们一定是嫉妒，因为她父母总是寄来意大利的糖果和巧克力……"
"米拉贝尔摇了摇头。"
Mirabel "玛丽-诺埃尔功课也不太好。她在读写上有些困难，还总爱走神。"
Mirabel "其实我一直在试着帮她一点，不过我得承认我不是最好的老师……"
show mirabel shy2 with dissolve
"米拉贝尔的脸泛起淡淡粉红。她摆弄着一条辫子的末梢，这似乎是她每当尴尬时惯于做的小动作。"
Mirabel "尽管那是我梦想中的事之一。"
Marcel huh u "哪里乐观了？"
Mirabel "这话听起来大概会有点傻，嗯……"
show mirabel ehe2 with dissolve
Mirabel "我知道这算不上什么了不起的梦想，真的——跟那些渴望成为舞者、诗人或演员的人相比根本不算什么——可我想当一名老师。"
show mirabel shy2 with dissolve
Mirabel "我、我不知道自己能不能做到，也不知道够不够聪明，可我喜欢和年幼的孩子待在一起，我想她们也喜欢我。这让我觉得很放松。"
Mirabel "其他工作听起来都好吓人，可、可要是能跟像玛丽-诺埃尔这样的孩子一起工作，我想我不会害怕。我觉得那样会让我很幸福。"
show mirabel neutral2 with dissolve
Mirabel "不过现在这还只是个梦想罢了。我很想去做，可是……"
"米拉贝尔抬起头望向天空，双手交握在身前。"
"我很快发现，天空是淡淡的粉蓝色，缀满了洁白蓬松的云朵。"
"细弱的阳光透过云层洒落。光线穿过米拉贝尔那一头长长的棕色长发，让它闪耀起来，恰如打磨过的栗子表面。"
"一阵凉风吹动米拉贝尔的刘海。她搭在胸前的发辫微微颤动。"
show mirabel sad2 with dissolve
Mirabel "我不知道自己什么时候才能让它成真。"
Mirabel "恐怕我是不够聪明。"

stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene sky3 g with clockwipe
$ renpy.pause(0.5)
show overlay2
show message23 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message23
hide logo2
hide overlay2
with datetrans2

$ renpy.pause(0.3)

$ save_name = (__("{u}米拉贝尔篇{/u}{vspace=1}  10月26日{vspace=1}  冷若冰霜") )
play ambience "sfx/wind.ogg" fadein 1.0
play music "bgm/Classroom.ogg" fadein 1.0
scene sky3 with dissolve
window show dissolve

"日子一天天过去。"
"秋意渐深，天气也随之转冷。树梢依旧披着棕、红与金黄，可叶子却在最轻的微风里瑟瑟颤动。"
"阳光愈发稀薄，厚重的云层时常预示着雨意。"
"在米延度过的头几夜，我以为自己的卧室已经够冷了，如今却简直是冰窖一般。"

stop ambience fadeout 1.0
show image "border" onlayer border
scene classroom_r:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

"教室同样寒意逼人，火炉里多半时候都添得满满的柴火，烧得正旺。"
"每天早上，由学校里年纪较大的女生——包括我在内——负责走上一段长长的路去柴房，再抱着足够的柴火回来，好让三间教室一整天都暖和。"
"有的女孩对寒冷抱怨不已，甚至进了教室还把外套穿在身上。另一些女孩则干脆不去上缝纫课或是阅读理解课，只顾把时间都耗在把双手坐在身下取暖上。"
"就在这样一个寒冷的秋日，临近十月底，全班那副集体懈怠的模样，终于把布吕吉埃夫人的脾气逼到了爆发的临界点。"

hide image "border" onlayer border
scene classroom_r:
    size (1920, 1080) crop (350, 40, 1440, 810)
show al annoyed2:
    xpos 0.50 xanchor 0.5
with wipeleft_slow

Bru "各位同学，请你们认真作答黑板上的题目。拿起你们的铅笔——"
Claudine u annoyed "哦，夫人，我们{i}一定{/i}要做吗？天这么冷，我怕我的手指都要冻掉啦！"
Noémie frown "说得对！我的手指都冻成冰柱了，几乎弯都弯不了！"
Claudine "夫人，这种天气您就不该给我们布置阅读理解练习！"
show al frown2 with dissolve
Bru "哦，我不该，是吗……？"
"整整一星期都在听着类似抱怨的布吕吉埃夫人，挑起了一边的眉毛。"
Bru "克洛蒂娜和诺艾米，很遗憾要对你们二位说，这间教室{i}不是{/i}由你们做主，而是由我做主。既然是我的学生，你们除了服从我的命令之外别无选择。"
Claudine "可是夫人，我也不知道自己{i}能不能{/i}听您的命令呀，尽管我是那么愿意！我都冻了个半死啦！"
Bru "冻着了，是吗？那可真是可惜。"
Bru "你愿意绕着校园跑上三圈来暖和暖和身子吗？那样也许能帮你解冻，克洛蒂娜小姐。"
"克洛蒂娜在椅子里又往下缩了缩，无奈地叹了口气。"
Claudine "不了，夫人……"
Bru "那就坐直了专心听讲——看在老天爷份上，立刻把您的手从屁股底下拿出来。你都快十六岁了，不是六岁。我绝不允许在我的课堂上有这种不成体统的行为！"
Claudine "哦，夫人，我的年纪无关紧要！不管一个人在这世上活了多少年，还是会觉得冷的！"
Bru "你要是把心思放在功课上就不会冷了。你们{i}全都{/i}得集中精神！"
"布吕吉埃夫人本就耐心耗尽，目光扫过整间教室——如同往常一样，停在米拉贝尔身上，怒目而视。"
Bru "米拉贝尔·拉克！请你别再摆弄头发了，专心听讲！"
"米拉贝尔心虚地跳了一下，睁大了眼睛，从刘海底下怯怯地打量布吕吉埃夫人。"
Mirabel shock "是、是的，布吕吉埃夫人……"
"教室里另外几个女孩朝米拉贝尔瞥了一眼，克洛蒂娜也在其中。她们开始窃笑。"
"至于布吕吉埃夫人，则是一副全然无动于衷的模样。"
show al sigh2 with dissolve
Bru "真是的，你们这些姑娘……"
show al annoyed2 with dissolve
Bru "那边是克洛蒂娜小姐，尽管她整天抱怨天冷，却偏偏一肚子的火气；这边是米拉贝尔小姐，她的注意力还不如一只水蚤。"
Bru "你们这些姑娘难道连{i}装装{/i}样子、对我的课表现出一点兴趣都做不到吗？"
Mirabel "我……我很抱歉，布吕吉埃夫人……"
show al frown2 with dissolve
Bru "哦，你{i}会{/i}后悔的。"
Bru "我知道对你们这些姑娘来说，那似乎还早得很，可期末考试会用你意想不到的速度降临。"
show al annoyed2 with dissolve
Bru "到夏天的时候，你们这些年长一些的姑娘——也包括你，克洛蒂娜。请别再偷笑——要前往内韦尔，接受数学、理解力和英语的考试。"
Bru "我不知道你们这些姑娘将来想做什么，可要是你们当中有人打算以有意义的方式为社会做贡献，那就必须通过这些考试。"
show al frown2 with dissolve
Bru "如果你们不在乎自己的前途，那就尽管继续闹别扭、抱怨，或者望着窗外发呆吧。不过等你们步入工作的世界，那对找工作可毫无益处。"
Bru "要是你们通不过这些考试，就永远别想当上老师、家庭教师、护士，或者任何你们想成为的人。"
show al annoyed2 with dissolve
Bru "其实我根本不必再提醒你们这些考试有多重要。你们现在都该明白了——尤其是你，米拉贝尔。"
Bru "我本以为考试不及格足以给你动力，让你埋头苦读，可看来并非如此。"

stop music fadeout 2.0

show al sigh2 with dissolve
Bru "我很少这样评价我的学生，哪怕是那些最无可救药的，可你恐怕真的是教不会的了。"
Mirabel "哦……！"
"一声痛苦的小小呜咽从米拉贝尔唇间挤了出来。"
"她低下头，眼睛被刘海遮住，可我还是能看见她双颊泛起的绯红。"
"教室里几个女孩凑在一起交换着恶毒的私语，头靠着头，压低了声音。"

play music "bgm/Sad.ogg" fadein 1.0
show image "border" onlayer border
scene classroom_r:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

Cla "我还是没法相信，那个迟钝的老米拉贝尔去年考试竟然没通过。"
Claa "就是！她再考一次又有什么用？"
Claaa "谁都知道她肯定又要失望了！"
Claa "也许她就是喜欢品尝失败的滋味吧！"
Cla "监考老师们看到她再来，肯定都会惊讶，这一点是毫无悬念的！"
Claa "她就像一股臭味，不管你怎么想赶走她，她总是不断地回来！"
Cla "我几乎都要替监考老师们难过了。她只会白费他们的时间，到头来他们还不是毫无例外地让她不及格！"
Claaa "好啦，好啦，我们可不能一口咬定她就会不及格。距离考试还有六个月呢。她有足够的时间学习。"
Cla "哦，别傻了，她{i}当然{/i}会不及格。米拉贝尔样样都不及格！"
Claaaa "她就算学上{i}六年{/i}，也还是不够应付那些考试的！"
Claaa "她连穿针引线都不会！"
Claa "她连法国的首都是哪里都不知道！"
Cla "她甚至连自己的名字有时候都会写错！"
Cla "我不明白米拉贝尔为什么还没放弃。"
Claa "也许她是笨到了连自己已经无可救药都察觉不到的地步！"

hide image "border" onlayer border
scene classroom_r:
    size (1920, 1080) crop (250, 40, 1440, 810)
show mirabel shy2:
    xpos 0.75 xanchor 0.5 ypos 0.55 yanchor 0.5
    ease 1.0 ypos 0.60
with wipeleft_slow

"米拉贝尔的头越垂越低。她耷拉着肩膀，被这些残忍话语的重量压垮了。"
"布吕吉埃夫人拍了拍手，想压下同学们恶毒的话语，但已经太迟了。伤害早已造成。"
"米拉贝尔一定听见了那些扔向她的话，一个字都没漏。她不可能没听见。我们那些同学根本没打算压低嗓门。"
"事实上，我觉得他们是故意想让她听见。"
"课终于还是继续了下去，可米拉贝尔几乎没听进去。她僵坐着一动不动，眼神呆滞，甚至懒得去捡起自己的铅笔。"
"她看起来彻底被打败了。"
"我多希望能安慰她，可我该怎么开口呢？眼下我们正在上课，即便不是在上课，我也不确定自己是否和她熟到能说出什么有意义的慰藉之词。"
"我完全不知道米拉贝尔又重考过一回了。"
"若真是如此，她该比我们其余人都年长一岁才对。"
"既然她都已经十六岁了，为什么还留在这所学校？"
"真是个谜。"
"我不得不承认，关于米拉贝尔，还有很多我所不知道的事。"
"我很想成为她的朋友，非常想，可我们简直形同陌路。"

stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene sky3 g with clockwipe
$ renpy.pause(0.5)
show overlay2
show message24 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message24
hide logo2
hide overlay2
with datetrans2

$ renpy.pause(0.3)

$ save_name = (__("{u}米拉贝尔篇{/u}{vspace=1}  10月27日{vspace=1}  米拉贝尔的告白") )
play music "bgm/Mysterious.ogg" fadein 1.0
scene sky3 with dissolve
window show dissolve

"第二天，早上取柴并把它搬回教室的活儿，落到了米拉贝尔和我头上。"

show image "border" onlayer border
scene woodshed_w:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wipe

"在逼仄昏暗的柴房里埋头干活时，我停下来，越过肩膀朝米拉贝尔瞥了一眼。"
"昨天我没能找到机会问米拉贝尔考试的事。我当时觉得，既然那么多同学都在拿这事取笑她，问起来恐怕会显得不近人情。"
"然而如今我们独处了，我仍不完全确定该怎样开口去问她。"
"我有一部分念头觉得，或许我根本就不该费这个心去问。"
"我不愿让米拉贝尔难过，而这显然是件沉甸甸压在她心头的事——或许几乎像我怀里抱着的柴火一样沉。"
"我该跟她谈吗？我敢吗？"
"我总可以试一试，可我不知道该怎么开口。"
"我该说些什么……？"

hide image "border" onlayer border
scene woodshed_w:
    size (1920, 1080) crop (240, 40, 1440, 810)
show mirabel scared2 r:
    xzoom -1 xpos 0.53 xanchor 0.5
with wipeleft_slow

Mirabel "玛塞尔……？"
"到头来，是米拉贝尔先开了口。"
"她好奇地看着我，怀里紧紧抱着一捆柴火，贴在胸前。她抱得那样不稳当，我担心它随时会掉下来。"
Mirabel "你还好吧？"
Marcel ehe u "哦，嗯……我没事……"
show mirabel neutral2 r with dissolve
Mirabel "真的吗？你一直咬着下嘴唇，就像只小兔子似的……"
"有吗？我可没注意到。"
"看来，在我打量米拉贝尔的时候，她也在打量着我。"
Marcel ehe u "哦，嗯……若是害你担心了，我很抱歉。谢谢你这么关心我。"
Mirabel "别这么说。嗯……"
"米拉贝尔皱起眉头。"
Mirabel "也许是我多心了，不过……方才你似乎一直在看我。"
show mirabel huh2 r with dissolve
Mirabel "你可是有什么话想问我？"
"我方才一直在为该怎么跟米拉贝尔说话而纠结，可如今她主动提起了，我反倒忽然感到一阵紧张。"
"我有点想告诉她一切都好——就此终结这场对话——可那样的话，我就丝毫无法更接近了解米拉贝尔了。"
"我得鼓起勇气跟她说话。唯有如此，我们才有可能成为朋友。"
"正如父亲常喜欢说的那样，懦弱的心，永远赢不得美人的芳心……"
"虽说据报上所言，我父亲本就对女人——无论美丑——从来谈不上有多大兴趣。"
Marcel neutral u "嗯，我只是有件事觉得好奇罢了……"
Mirabel "是关于我的吗？"
Marcel "嗯。这个……"
Marcel "是几周前同学们说过的那件事。"
show mirabel neutral2 r with dissolve
Mirabel "他们说了什么？"
Marcel huh u "哦，你也知道的。他们谈的是夏天的考试。你还记得吗……？"
show mirabel shock2 r at bounce
Mirabel "哦，那个……！"
"终于，她恍然大悟了。米拉贝尔睁大了眼睛，嘴唇抿成了方才提到的那枚硬币的形状。"
"她抱在怀里的那堆柴火抱得更紧了。"
"我看见她指节因用力而泛白，死死撑着，拼命不让柴火散落一地，或砸到自己的脚上。"
"她被我的提问弄得如此不安，我立刻感到一阵愧疚。"
Marcel sad u "我、呃……若我提起不该提的事，我很抱歉。我不想让你难过……！"
show mirabel ehe2 r with dissolve
Mirabel "哦，不，那……没关系的……"
Marcel neutral u "你不介意谈谈这件事？"
show mirabel neutral2 r with dissolve
Mirabel "不介意。至少，我想我不介意……"
show mirabel sigh2 r with dissolve
Mirabel "我反倒惊讶你还没听说过这件事。其他人可都知道了。"
show mirabel sad2 r with dissolve
Mirabel "我原以为米延的人都晓得我那些失败……不过，也许是我太一厢情愿了吧？"
Mirabel "你才搬来不久，所以没听过也怪不得你。"
Mirabel "不过，这事也算不上多要紧——放在大局里不值一提。对我而言它很重要，可对你来说……"
"米拉贝尔皱起眉头。"
show mirabel sigh2 r with dissolve
Mirabel "我想不出你为何会在意。我这点烦恼，对你这样从城里来的姑娘来说，一定觉得很乏味吧！"
Marcel "可我{i}的确{/i}在意。所以我才问你这件事。"
show mirabel huh2 r with dissolve
Mirabel "你、你在意？"
Marcel smile u "嗯。我不是刚说了吗？"
Mirabel "是关于我的吗？"
"我点了点头。"
show mirabel ehe2 r with dissolve
Mirabel "哦……！我也不懂为什么，可是……我想，这让我很高兴……"
show mirabel shy2 r with dissolve
Mirabel "也许吧……？"
"但米拉贝尔的声音渐渐低了下去，听上去并不十分确定。"
"她轻轻叹了口气，把柴火又往怀里揽了揽，就像母亲抱着怀里的婴儿那样。"
Marcel huh u "若你不想对我说，也不必勉强。"
show mirabel neutral2 r with dissolve
Mirabel "哦，不是那样的。若我不告诉你去年发生的事，别人也会说，而且多半会说得比实情还要糟。"
show mirabel sad2 r with dissolve
Mirabel "嗯……"
"这一次，轮到米拉贝尔咬住她自己的下唇。"
Mirabel "我想，那{i}确实{/i}挺糟的。"
show mirabel sigh2 r with dissolve
Mirabel "事实上，那是件很丢人的事。"
"米拉贝尔的下唇微微颤动。"
"她把怀抱的那一捧柴放回柴堆。接着，她开始拨弄自己的发辫——每当她不知道双手该往哪儿放时，她常常如此。"
show mirabel neutral2 r with dissolve
Mirabel "说实话，我……其实比学校里其他姑娘大一岁。我今年十六，明年一月就要十七了。"
"她说出真实年龄时缩了一下，仿佛那是个见不得人的秘密。某种程度上，我想也确实是——或者说，要不是我们班所有人都早已知道这件事（在此之前唯独我还被蒙在鼓里），它本该是的。"
show mirabel sad2 r with dissolve
Mirabel "跟别的姑娘相比，我觉得自己{i}好老{/i}。"
Marcel huh u "你不老。一岁之差没那么大……"
show mirabel shock2 r with dissolve
Mirabel "可对我来说这差别{i}感觉{/i}很大，而且别的姑娘也不肯让我忘记这一点！"
show mirabel sad2 r with dissolve
Mirabel "她们总是取笑我，说我老姑娘，或说我是老婆婆。"
Mirabel "有时候，诺艾米会问我照镜子有没有找到白头发；而克洛蒂娜总在我俩清晨一起去捡柴火时，提醒我别闪了腰。"
show mirabel ehe2 r with dissolve
Mirabel "正因为如此，布吕吉埃夫人让我和你一起去柴房，我才很高兴。我知道你绝不会开那种玩笑。你人实在太好了。"
"米拉贝尔冲我露出一个浅浅的笑，可那笑容里几乎没有什么真正的喜悦。"
"可怜的米拉贝尔看起来彻底被打败了。"
show mirabel sad2 r with dissolve
Mirabel "我的同学们认为，因为我比她们年长，我就应当更聪明、更有魅力……"
show mirabel sigh2 r with dissolve
Mirabel "但，当然，我并不是。"
show mirabel sad2 r with dissolve
Mirabel "学校大多数科目我都比旁人差，这更叫她们笑话我。"
show mirabel huh2 r with dissolve
Mirabel "「都十六岁了，这么大一个姑娘，连穿针都不会？！」"
"米拉贝尔模仿起诺艾米的腔调；鼻音浓重，尖细尖细的，带着无可辩驳的幸灾乐祸。"
Mirabel "「这样你还怎么找得到丈夫？！你简直已经是个老姑娘了！」"
show mirabel sad2 r with dissolve
Mirabel "可这实在不公平。诺艾米的针线活跟我一样差。她没那份耐心，还老用针扎到自己的手指头……"
show mirabel sigh2 r with dissolve
Mirabel "可她才不在乎公不公平。她们谁都不在乎。她们只想让我难受。"
show mirabel sad2 r with dissolve
Mirabel "打从我记事起，就总被人取笑迟钝、迷糊，但去年还没这么糟。"
Mirabel "我那时十五岁，虽然已是学校最后一年，却还不是最年长的。"
Mirabel "我有几个同龄的朋友，诺艾米和克洛蒂娜也大多不来找我麻烦，直到……"

stop music fadeout 2.0

show mirabel sigh2 r with dissolve
"米拉贝尔停顿了一下。她转过身去，仿佛羞于与我对视。"
"我尽可能温和地引导她；把嗓音压得低低的，就像人对林间的小鹿说话时那样。"
Marcel huh u "直到……？"

play music "bgm/Confession.ogg" fadein 1.0

show mirabel sad2 r with dissolve
Mirabel "哦，就是夏天的考试！"
show mirabel neutral2 r with dissolve
Mirabel "当一名小学老师一直是我的梦想，可要当老师，就得通过那些考试。否则根本进不了师范学校。"
Mirabel "只要一有空，我就拼命用功，尽管在父母的面包店里帮忙让我忙得不可开交。我甚至还请了几个朋友来帮我，可是……"
show mirabel sad2 r with dissolve
"米拉贝尔的下唇颤抖着。"
show mirabel shock2 r with dissolve
Mirabel "我真的很努力——真的，我是认真做了，尽管没人相信我——可我的成绩实在糟透了！"
Mirabel "我把那篇关于法国文学的作文写得一塌糊涂，口试时又紧张得一开口就结巴。"
Mirabel "监考老师不得不让我重说三遍，后来索性放弃，挥手把我打发走了。"
show mirabel sigh2 r with dissolve
Mirabel "他连听都懒得听我说。我想，他早就把我当成无可救药的人了……"
show mirabel sad2 r with dissolve
Mirabel "最糟的是，我觉得他是对的。我{i}就是{/i}个无可救药的人。我是个失败者。"
show mirabel sigh2 r with dissolve
Mirabel "布吕吉埃夫人是这么想的。我其他同学也都这么想——我自己也一样。"
Mirabel "我{i}一无是处{/i}。"
"我望着米拉贝尔好一会儿，被她那股自我厌恶的力量震得说不出话来。"
"我拿不准该说些什么才能让她振作起来。我不知道自己的话究竟值多少分量。我那套老生常谈又有什么用？"
"它们改变不了已经发生的事。"
"安慰米拉贝尔也许做不到，但我想对她处境流露出关切。我想让她知道我在乎她。"
"正是出于这个念头，还有那股未了的求知欲，我向她抛出了又一个问题。"
Marcel huh u "那，你的朋友们后来怎么样了？她们通过考试了吗？"
show mirabel neutral2 r with dissolve
Mirabel "哦，是的。她们轻松就通过了，而且都离开了米延。"
Mirabel "她们中有两个去了讷韦尔的师范学校，还有一个给……好像是奥尔良的一个小女孩当家庭教师。"
Mirabel "她们说过会给我写信，起初确实也写了，可如今已经一个多月没收到她们的信了。"
show mirabel sigh2 r with dissolve
"米拉贝尔叹了口气。"
Mirabel "我想，我真怪不得她们。她们一定在忙着过新生活，而我写信又写得不好。"
Mirabel "我总是一慌起来就反复犹豫该写什么，结果信纸上净是墨渍，还涂涂改改。"
show mirabel sad2 r with dissolve
Mirabel "我拼写也不太好，尽管有满满一肚子话想告诉她们，却似乎总没法好好地写下来。"
Mirabel "我{i}什么{/i}都做不好。我是个失败者。"
Marcel "那你想念你的朋友们吗？"
show mirabel sigh2 r with dissolve
Mirabel "想念的。我常想起她们，总在想她们此刻在做什么。"
Mirabel "有时候，我甚至会嫉妒她们。"
show mirabel sad2 r with dissolve
Mirabel "当然，我不想嫉妒自己的朋友。我为她们通过考试而高兴，可话虽如此……"
"米拉贝尔的表情扭曲了。"
Mirabel "我也想去讷韦尔，和她们一道读书。"
Mirabel "我都快十七了，身边却净是些比我小的姑娘，而她们{i}个个{/i}都比我聪明。"
Mirabel "我觉得自己被人抛在了后头，无论我怎么跑都没用。我追不上！"
Mirabel "真是让人懊恼……！"

window hide dissolve
$ achievement.grant("damp_eyes")
scene cg14 with dissolve
$ renpy.pause(0.8)
window show dissolve

"米拉贝尔看着我。她的脸颊因窘迫而微微泛红，眼眶也湿润得可疑，尽管她极力在忍住那快要涌出的泪水。"
Mirabel "我若要成为老师，就必须通过这些考试。"
Mirabel "父母让我在学校多留一年，好再给我一次机会，可这是我最末一次机会了。"
Mirabel "若我{i}又{/i}没考过，便别无选择，只能一辈子留在米延了。"
Mirabel "我得一直帮父母在面包店里干活，直到我真{i}成{/i}了老姑娘，手指僵硬，再也揉不动面团。"
Mirabel "我只好眼看着同学们长大，离开米延，去经历种种冒险……"
Mirabel "而我，却只能困在这里。"
Mirabel "我要永远留在这里，孤零零的，又笨，又没人爱……"
"米拉贝尔抬起头。她的眼睛眯了起来，带着从自身绝望中崭新锻造出的决心。"
Mirabel "今年是我最后的机会。"
Mirabel "我不知道自己能否通过考试，可我必须尽力而为。"
Mirabel "我没有别的选择。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
play ambience "sfx/wind.ogg" fadein 1.0
$ save_name = (__("{u}米拉贝尔篇{/u}{vspace=1}  10月27日{vspace=1}  被点名") )
scene sky3 with wiperight_slow
window show dissolve

"那天早上英语课时，杜布瓦夫人比平时更加暴躁，或许是因为严寒的缘故。"
"尽管教室后头的炉火正欢快地燃烧，似乎也丝毫没能缓和空气中的寒意。"
"这堂课里，我的大多数同学都坐在自己双手上，拼命想让自己暖和些；尤其是那些不幸坐在教室前排、或是靠近窗边的女孩。"

play music "bgm/Sad.ogg" fadein 1.0
stop ambience fadeout 1.0
show image "border" onlayer border
scene classroom_r:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

"杜布瓦夫人又一次像往常那样，在这堂课里屡次刁难可怜的露丝——可让杜布瓦夫人恼火的是，露丝对她抛来的每一个问题都能不眨眼睛地答上来。"
"火气渐长，杜布瓦夫人在教室里搜寻起新的靶子。"
"我本能地在椅子里缩了下去，尽管或许根本没必要这么紧张。"
"尽管杜布瓦夫人在课上总是点露丝的名，为任何所谓的过失责骂她，可对于其他女孩，她却相当宽容。"
"她那种爱把错归到露丝身上的倾向，实在令人起疑。"
"这让我忍不住猜想她们之间是不是有什么过往。杜布瓦夫人如此恨露丝，必定有缘由，可我怎么也想象不出那会是什么。露丝并不是个惹麻烦的人；无论怎么想都不是。"
"她总是专心听讲，从不插嘴。"
"事实上，她几乎从不开口说话。"
"若是我们班里真有谁该时常受罚，那也该是克洛蒂娜，可杜布瓦夫人的目光却径直从她身上掠过。"
"也许是杜布瓦夫人不想承担试图惩罚机灵的克洛蒂娜所带来的后果吧。反正她也不会听。她显然从来不听布吕吉埃夫人的话。"
"取而代之的是，在漫长的停顿之后……"

hide image "border" onlayer border
scene classroom_r
show paulette frown:
    xpos 0.50 xanchor 0.5
with wipeleft_slow

Dubois "米拉贝尔。"
"……杜布瓦夫人终于选定了她的目标。"
"米拉贝尔——方才正心不在焉地咬着辫梢，出神地望着窗外——猛地惊醒过来。"
"她这一惊，手肘撞到了铅笔。铅笔从桌上滚落，掉在地上，发出一声沉闷得几乎听不见的轻响。"
"米拉贝尔圆润的脸涨得通红，杜布瓦夫人叹了口气。"
"与此同时，我们的同学们都咯咯笑了起来。"
show paulette neutral with dissolve
Dubois "看来我叫你起来是对的，米拉贝尔。显然你方才根本没在听讲，是不是？"
Mirabel shock "不、不是的，夫人……我很抱歉。"
show paulette frown with dissolve
Dubois "你想怎么道歉都行，可你辜负的唯有你自己。"
Dubois "你的英语水平还差得远，没资格在我讲课时那样张着嘴、望着虚空发呆。"
Mirabel "我……我很抱歉，夫人……"
show paulette sigh with dissolve
Dubois "是啊，这话你已经说过了。"
Mirabel sad "我、我道歉……"
show paulette frown with dissolve
Dubois "反复重复这番话，也不会对你的处境有任何帮助。"
show paulette sigh with dissolve
"杜布瓦夫人挑起一边眉毛，随后叹了口气。"
Dubois "我还以为我要教的是满屋子的姑娘，而不是一屋子学舌的鹦鹉。"
Mirabel "我、我很抱歉……"
"同学们开始为米拉贝尔的失态咯咯发笑，杜布瓦夫人则把双手往空中一摊，做了个假装投降的姿势。"
show paulette mad with dissolve
Dubois "哦，我认输！你当真教不会，是不是，米拉贝尔？"
Mirabel "是、是的，夫人……"
"米拉贝尔弯下腰，伸出手臂，试图把铅笔从地上捞起来。我想她只是想把那张绯红的脸藏到课桌底下，我祈祷杜布瓦夫人就此放过她，可……"
show paulette frown with dissolve
Dubois "哦，够了，米拉贝尔。我准许你捡起那支铅笔了吗？"
Mirabel "可、可是夫人……我不捡起铅笔，又怎么做笔记呢？"
show paulette neutral with dissolve
Dubois "你本来就一个字的笔记都没写。我倒怀疑这会不会妨碍你那所谓的『学习』。"
Mirabel "我……我很抱歉……"
show paulette mad with dissolve
Dubois "哦，你就消停会儿吧！你翻来覆去尽是这几句，都让我怀疑自己是不是疯了！"
"全班又开始哄笑起来，除了露丝——她依旧望着窗外。我想她不愿参与这场小小的闹剧。"
"露丝对杜布瓦夫人说话总是客客气气的，但语气里透着一股冷意。当杜布瓦夫人不点她起来回答问题时，露丝便执拗地不去看她；挺直了背，神情坚定。"
"这实在令人好奇……"
"但此刻我更担心的是米拉贝尔。"
show paulette neutral with dissolve
Dubois "那么，米拉贝尔，不如让我们看看这半个钟头里，你那颗笨脑瓜到底装进去了多少东西？"
show paulette frown with dissolve
Dubois "站起来，到黑板前面来。试着把这句英文译成法文——"
play sound "sfx/slap.ogg"
"杜布瓦夫人一巴掌拍在黑板上一记。"
Dubois "——当着全班同学的面。"
Mirabel shock "哦……"
"米拉贝尔盯着杜布瓦夫人，僵在原地，仿佛我们的英语老师刚才竟要她把自己从大炮里发射出去似的。"
"米拉贝尔脸上那种恐惧的神情如此真切，我简直觉得她说不定宁愿选择那个办法。"
Dubois "怎么？还等什么？"
Dubois "动作快点。我可没一整天的时间。趁我还没老掉牙，你赶紧到教室前面来。"
Mirabel sad "可您……我是说，嗯……"
"米拉贝尔在座位上不安地扭动。她的手指开始拨弄其中一条发辫的发梢——每当她感到不自在时，它们常常如此。"
Mirabel "您要我……当着大家的面……写答案……？"
Dubois "我当然要你当着大家的面写出来。我总不能为了你一个人，叫全体同学都把课桌转过去吧！"
Mirabel scared "可我，嗯……我……"
show paulette mad with dissolve
Dubois "哦，快去写吧，丫头。我等得不耐烦了。"

show image "border" onlayer border
scene classroom_r:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

Cla "她为什么看起来那么紧张？"
Claa "我们都知道她肯定答不对！"
Claa "反正也没人对她抱什么期望……"
"教室里满是残忍的窃窃私语。它们像玫瑰园里的毛虫一样繁衍；每一个音节都在啃噬着米拉贝尔本就脆弱的自尊。"
"若我是个更大胆、更勇敢的人，也许我会叫他们停下。我会请求——不，{i}要求{/i}——他们别再去纠缠米拉贝尔。"
"她究竟做过什么对不起他们的事？"
"米拉贝尔是个善良、温柔的女孩，或许她觉得功课有些吃力，但她仍每天都去上课。"
"她没有放弃。"
"她正拼尽全力去追寻自己的梦想，尽管身边所有人都在试图将她击倒。"
"我觉得这很了不起……"
"但遗憾的是，我并不是个大胆、勇敢的人，我发觉自己无力替她辩护。我只能坐在那里，默默地在心里盼着米拉贝尔竭尽全力，看着她站起身来。"

hide image "border" onlayer border
play ambience "sfx/footsteps3.ogg" fadein 0.5
scene classroom_r
show paulette frown:
    xpos 0.70 xanchor 0.5
show mirabel sad:
    xzoom -1 xpos -0.20 xanchor 0.5
    ease 2.0 xpos 0.28
with wipeleft_slow

$ renpy.pause(0.8)
stop ambience fadeout 0.5

"米拉贝尔迈着缓慢而沉重的步子，走向教室前面。"
"她踌躇地挪动着，十指在身前交握。她一直低着头，眼睛被刘海遮住。她的脸颊正慢慢泛起淡粉色。"
"看着她是件令人心疼的事。"
"再明白不过了，她宁愿待在任何地方，也不愿待在这间教室的四面墙之内，我不能说自己怪她。"
"所有人的目光都落在米拉贝尔身上。大家都在等着她出错。他们正满心期待地享受这个念头。"
show paulette sigh with dissolve
Dubois "真是费了老大的劲。你看上去活像是被押上断头台的样子，米拉贝尔！"
"杜布瓦夫人摇了摇头，然后把一支粉笔塞进米拉贝尔颤抖的手掌里。"
show paulette neutral with dissolve
Dubois "给。你拿着这个。"
show mirabel scared at bounce
"米拉贝尔接了过来，可她的手指抖得厉害，差点把它掉在地上。"
show paulette frown with dissolve
Dubois "那么，你还等什么？试着把答案写下来。把这个英语句子译回法语。"

scene classroom_r:
    size (1920, 1080) crop (100, 40, 1440, 810)
show mirabel scared2:
    xzoom -1 xpos 0.30 xanchor 0.5
with dissolve

"米拉贝尔盯着黑板。她把粉笔夹在指间，指头都染上了一层白色的粉灰，可她就是一动不动。"
"也许她根本写不出来。"
"或许光是走到教室前面，就已经耗尽了她最后一丝力气。"

scene classroom_r
show paulette frown:
    xpos 0.70 xanchor 0.5
show mirabel scared:
    xzoom -1 xpos 0.28 xanchor 0.5
with dissolve

Dubois "拜托，姑娘。别光杵在那儿！这不过是一个简单的句子。谁都能做。就连幼儿班的小丫头们都能答上来。"
show paulette mad with dissolve
Dubois "要不要我去请一个年幼的孩子来——也许是五六岁的小孩？——替你来回答这道题？"
show mirabel shock at bounce
Mirabel "啊——不……！我——我不想让您那样做。我——我不愿打搅他们的功课！"
show paulette frown with dissolve
Dubois "那就动手吧。写一个答案——{i}随便{/i}一个答案——就算不是对的也行。"
Cla "肯定不会是对的那个答案！"
Claa "我觉得杜布瓦夫人对那个连穿针都费劲的女孩，怕是期望太高了……"
Cla "还有连自己的名字都拼不对！"
"同学们中间响起一阵残忍的窃笑声。米拉贝尔的额头上开始冒汗。"

show image "border" onlayer border
scene classroom_r:
    subpixel True
    size (1920, 1080) crop (670, 180, 640, 360)
    linear 20.0 crop (670, 50, 640, 360)
with dissolve

"米拉贝尔用颤抖的手指把粉笔压到黑板上。她写得很慢，舌头从嘴角探出来，一副全神贯注的模样。"
"她看起来那么无助，我真担心她会哭出来。"
"几秒钟过去了。米拉贝尔仍然在写。"
"她迟疑地移动着粉笔，那姿态活像一个恨不得逃走的人。她按得太用力了些，粉笔的笔尖碎成了粉末。"

hide image "border" onlayer border
scene classroom_r
show paulette frown:
    xpos 0.70 xanchor 0.5
show mirabel scared:
    xzoom -1 xpos 0.28 xanchor 0.5
with dissolve

Dubois "当心点，米拉贝尔！你要是连这么简单的问题都答错，至少也该有点分寸，别顺手把教室里的东西也给砸了！"
show mirabel shock at bounce
Mirabel "是——是的，夫人！我会小心的！"
"又过去了几秒钟煎熬般的时光，感觉却远比实际漫长。"
show mirabel sad:
    ease 0.8 xpos 0.25
"当米拉贝尔终于从黑板前退开时，她带着焦虑又歉疚的神情抬头望向杜布瓦夫人。"
Mirabel "对不起，嗯……我已经尽力了，可是……"
show paulette frown with dissolve
Dubois "尽力。"
"杜布瓦夫人看着写在黑板上的答案——字迹很小、很淡，透着犹豫。"
"她挑起了一边眉毛。"
Dubois "{i}这{/i}就是你的尽力？"
show mirabel shy with dissolve
Mirabel "是的，嗯……那个……我试过了……"
show paulette sigh with dissolve
Dubois "如果{i}这{/i}就是你在尽力，米拉贝尔，那我可真不愿看到你一点力气都不出时写出的作业是什么样子。"
Dubois "这完全错了，而且你连这些法语单词都没拼对！"
show paulette frown with dissolve
Dubois "你本来{i}就是{/i}法国人，不是吗？你怎么能把自己的母语糟蹋成这样？！"
show mirabel scared with dissolve
Mirabel "我……我——我不知道，夫人……"
show paulette neutral with dissolve
Dubois "我也不知道。你真是世界一大奇观，米拉贝尔，我可不是说好话。"
show paulette sigh with dissolve
Dubois "行了，回去坐下，别再丢人现眼了。这情形连我都觉得太压抑。"
show mirabel shock at bounce
Mirabel "是——是的……！"
"米拉贝尔不用别人提第二遍。"

show mirabel:
    xzoom 1
with dissolve

$ renpy.pause(0.3)

show mirabel:
    ease 0.8 xpos 0.15

"她转过身，准备羞愧地溜回自己的座位，可是……"
show paulette neutral with dissolve
Dubois "噢，米拉贝尔。要是你不介意的话，能把我的粉笔还给我吗？它也许只有原来的一半大了，可这接下来的一堂课我还想用它。"

show mirabel shock:
    xzoom -1
with dissolve

$ renpy.pause(0.3)

show mirabel at bounce

Mirabel "啊——好的……！我——我很抱歉……"

show mirabel:
    ease 0.8 xpos 0.28

"米拉贝尔半压低着声音，脸因羞愧而涨得通红，还得忍受着额外的屈辱，转过身去把粉笔交还给我们的老师。"

play ambience "sfx/footsteps3.ogg" fadein 0.5
show mirabel sad:
    xzoom 1
with dissolve

$ renpy.pause(0.3)

show mirabel:
    ease 1.2 xpos -0.10

$ renpy.pause(1.2)

scene classroom_r:
    size (1920, 1080) crop (350, 40, 1440, 810)
show mirabel sad2:
    xzoom 1 xpos 1.0 xanchor 0.5 ypos 0.50 yanchor 0.5
    ease 1.5 xpos 0.75
with wipeleft_slow
stop ambience fadeout 0.5

"当米拉贝尔终于坐下时，她一直低着头，双肩耷拉着。"

show mirabel:
    ease 0.8 ypos 0.55

"也许她是在设法保护自己，避开同学们残忍的窃笑和恶毒的言语……可无论她怎样蜷缩起自己，那些话她一定还是听得见。"
"他们可一点也没有遮掩自己对米拉贝尔失败的幸灾乐祸。"
"我原以为男孩子才残忍。看来女孩子也一样能恶毒。"

scene classroom_r:
show paulette neutral:
    xpos 0.50 xanchor 0.5
with wipeleft_slow

Dubois "好了，我们把这堆胡言乱语从黑板上擦掉吧……"
"杜布瓦夫人捡起一块脏抹布，把米拉贝尔那犹豫、完全错误的答案从黑板上擦掉。"
Dubois "有哪位同学能把这个简单的英语词组译成法语？如果你们刚才留意听了，这应该是相当容易的……就算没听，也该比米拉贝尔做得好。"
"我真替米拉贝尔难过——她就那么低着头坐在那里——于是决定结束这场小小的表演。对于杜布瓦夫人的提问，我是第一个——也是唯一一个——举手的学生。"
"杜布瓦夫人打量了我一会儿，嘴唇抿得紧紧的。"
Dubois "是玛塞尔，对吗？从巴黎来的那个女孩？"
Marcel frown u "是这样。"
show paulette sigh with dissolve
Dubois "很好。让我们看看你在那所时髦的巴黎学校都学了些什么。请到教室前面来。"

scene classroom_r:
    size (1920, 1080) crop (240, 40, 1440, 810)
show paulette frown2:
    xpos 0.50 xanchor 0.5
with dissolve

"我照做了，尽管我的双腿在发抖。我并不特别喜欢成为众人瞩目的焦点，可如果这样能让杜布瓦夫人不再盯着米拉贝尔，那我也无所谓。"
"现在再去给米拉贝尔真正的帮助已经太迟了。伤害已经造成。"
"不过，我至少可以试着减轻她的痛苦。"
"我接过杜布瓦夫人递来的粉笔，它带着米拉贝尔手心里的温热，然后在黑板旁站定。"

show image "border" onlayer border
scene classroom_r:
    subpixel True
    size (1920, 1080) crop (670, 180, 640, 360)
    linear 20.0 crop (670, 50, 640, 360)
with dissolve

"我看了那句子文几秒钟，试着在脑子里把它分解成法语。"
"杜布瓦夫人说这句话不复杂，可我觉得她这么说，更多的是为了让米拉贝尔难堪。"
"这句话其实相当长，里面缀满了许多标点符号和复杂词汇。"
"我不记得杜布瓦夫人教过我们这上面写的哪怕一半的东西。"
"我敢打赌，教室里那些嘲笑米拉贝尔「无能」的女孩，多半也翻译不了这句话。"
"幸好我在巴黎学过其中一些词汇，所以对我来说并不算全然陌生。"
"我应该能把它译回法语……"
"我深吸一口气，祈祷自己的直觉是对的，然后把粉笔的断端压在黑板上。"
"我写了一会儿，粉笔刮过黑板的声音充满了整个房间，然后我才退开。"

hide image "border" onlayer border
scene classroom_r:
    size (1920, 1080) crop (240, 40, 1440, 810)
show paulette frown2:
    xpos 0.50 xanchor 0.5
with dissolve

Marcel neutral u "您觉得怎么样，夫人？这样可以吗？"
show paulette neutral2 with dissolve
Dubois "我想，也许有更优雅的写法，但你好歹把意思表达出来了，大体上没错。"
show paulette sigh2 with dissolve
Dubois "这个可以接受。"
Marcel sigh u "谢谢您，夫人。"
"我把粉笔递还给杜布瓦夫人，回到了自己桌前的座位上。"

scene classroom_r with dissolve

"整个过程里，我能看到一双双好奇的眼睛落在我身上。"
"我的同学们——除了露丝——都带着不小的兴趣看着我……"

scene classroom_r:
    size (1920, 1080) crop (350, 40, 1440, 810)
show mirabel shock2:
    xpos 0.75 xanchor 0.5 ypos 0.55 yanchor 0.5
with wiperight_slow

"可是最吸引我注意的那双大眼睛，是米拉贝尔的。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
play music "bgm/Casual_Day.ogg" fadein 1.0
$ save_name = (__("{u}米拉贝尔篇{/u}{vspace=1}  10月27日{vspace=1}  渐渐靠近") )
scene yard_r with wiperight_slow
window show dissolve

"当天最后一节课结束时，我随着一群女孩走出教室。可我还没来得及走远，就被一道紧张不安的声音叫住了。"

play sound "sfx/footsteps2.ogg" fadein 0.5
show mirabel shy r:
    xzoom -1 xpos -0.20 xanchor 0.5
    ease 2.0 xpos 0.50

$ renpy.pause(0.8)
stop sound fadeout 0.5

W "玛塞尔！嗯，玛塞尔？"
"是米拉贝尔。"
"明明是她先叫住我的，此刻她却羞怯地看着我。她的手指在身前交缠着，一如往常那样，她正低头看着地面。"
Marcel neutral u "怎么了……？"
"我期待地看着她。"
Marcel "你找我有什么事吗？"
show mirabel at twirl
Mirabel "那个，嗯……我在想……"
"米拉贝尔局促不安地看了看左边，又看了看右边，才走上前来。"

play sound "sfx/rustle.ogg"
scene yard_r:
    size (1920, 1080) crop (240, 40, 1440, 810)
show mirabel shy2 r:
    xzoom -1 xpos 0.5 xanchor 0.5
with dissolve

Mirabel "我想问你一个问题……可是当着这么多人问出来，有点不好意思。"
show mirabel neutral2 r with dissolve
Mirabel "我们能不能找个没人的地方谈谈？"
Marcel neutral u "如果你想要个清静的地方，我想那总归可以到我的房间去。"
show mirabel shock2 r at bounce
Mirabel "你有自己的房间？"
Marcel smile u "是这样。"
show mirabel neutral2 r with dissolve
Mirabel "这么说，你是不跟寄宿在这里的其他女生一起睡宿舍的吗？"
Marcel shy u "不。我，嗯……有时候睡不好，校长觉得那样可能会吵到别人。"
Mirabel "原来是这样……这么说，你有完全属于自己的一间卧室……"
show mirabel laugh2 r with dissolve
Mirabel "你可真走运！"
Marcel "这个嘛，房间其实挺小的，有时候会有点寂寞。"
"我正想安抚米拉贝尔，却又担心自己的话可能适得其反。"
"我想，在这样一所小学校里，能拥有一间自己的房间确实挺让人羡慕的。"
"其他女孩都合住宿舍，睡在同一屋檐下挤在一起的床铺上。"
"我不想显得像个娇生惯养的巴黎少爷，虽然受到了校长的特别照顾，却不懂得珍惜自己享有的这些优待。"
"不可否认，我在巴黎的旧公寓比我如今睡的这间卧室要大得多，可如果我这样告诉米拉贝尔，听起来就像在炫耀。"
"幸好，米拉贝尔一点也没有被冒犯的样子。她仍然笑着。"
"这下我倒好奇了……"
Marcel huh u "可你不是寄宿在这所学校里的吧，米拉贝尔？我以为你跟父母住在他们的面包店里。"
show mirabel neutral2 r with dissolve
Mirabel "是啊。不过我并没有自己的房间。我有个弟弟，我跟他合住一间。"
Mirabel "他还不到上学的年纪，所以我在家的时候都得照看他。"
Mirabel "哄他开心、晚上给他掖好被子、给他讲故事哄他入睡，都是我的活儿……"
show mirabel sigh2 r with dissolve
Mirabel "他年纪那么小，却那么吵、那么有精神！照看他可真够费心的！"
show mirabel sad2 r with dissolve
Mirabel "我想，要是我搬进学校的宿舍、住在这里，也许就能多睡一会儿……"
"米拉贝尔顿了顿，像是在重新考虑，然后羞怯地咯咯一笑。"
show mirabel ehe2 r with dissolve
Mirabel "唔，也许不会吧。"
show mirabel sad2 r with dissolve
Mirabel "其他女生大概会一直对我使坏捉弄我。她们会偷走我的衣服，冬天还会往我鞋里塞雪。"
Marcel huh u "你真觉得她们会那样做吗？"
Mirabel "她们干得出这种事。去年春天，在你来这所学校之前，有人往我课桌里头塞满了青蛙卵……"
Marcel frown u "呃……听起来真恶心。"
show mirabel shock2 r at bounce
Mirabel "可不是嘛！那东西又恶心又黏糊糊的，我的书都弄坏了……"
show mirabel sad2 r with dissolve
Mirabel "杜布瓦夫人还为这事怪罪我。"
Mirabel "我试着跟她解释，说我才不会往自己课桌里放青蛙卵——我为什么要那么做？——可我不太会替自己辩解，她根本就不听我的……"
Mirabel "她恼火我顶撞她，把我狼狈地赶出了教室。"
Marcel shock u "但那不公平……！"
show mirabel sigh2 r with dissolve
Mirabel "我知道这不公平，可生活本来就很少是公平的。"
show mirabel smile2 r with dissolve
Mirabel "我想，我得庆幸自己能跟父母住在一起，不用寄宿在学校楼里。我觉得那会相当压抑。"
show mirabel neutral2 r with dissolve
Mirabel "不过……"
"米拉贝尔打量着我，她的手指依旧在身前缠在一起。"
Mirabel "希望这话听起来不会太冒失，可是既然你提到了，我{i}确实{/i}对你的房间很好奇。我想看看它是什么样子。"
Marcel neutral u "嗯……"
"我沉思了片刻。"

scene sky3 with wipeup_slow

"我来这所学校已经一个多月了，却从没邀请过任何同学上我的房间。我觉得自己跟他们还没有熟到那个地步——况且，我也担心那会有失体统。"
"男人和女人当然可以往来，但社交礼仪规定，异性之间的青少年不该在没有陪伴的情况下独处太久；除非他们已经有了婚约。"
"可米拉贝尔并不知道我是个男孩——而且有时候，当我早晨在镜子里看到自己的时候，我自己也不确定自己是不是了。"
"每当我看到自己穿着连衣裙、头发扎成辫子时，总会感到一阵惊讶——毕竟穿了十几年的裤子，会让人如此——不过它已经不像从前那样让我觉得怪异了。"
"它已经成了我日常生活的一部分，就像写下我名字的阴性形式：玛塞尔。"
"我想，人只要有足够的时间，什么都能习惯，但我觉得自己从前穿男装时，从未像现在这般自在。"
"我不确定自己是否完全满意现在的生活和新的模样，但我已经足够安于这一切了。"
"和同学们相处很有意思，我也希望能交到更多的朋友。"
"我不愿拒绝米拉贝尔的亲近。要是我伤了她的心，我会很难受的。"
"我或许是以某种不实的名义邀她来我的房间，可明明是她先开口请求的。她要是知道我是个男孩，大概就不会开口了，但我也不是在欺骗她。"
"我没有任何不可告人的目的。我只是想聊聊天。"
"于是，在心里反复斟酌了一番之后，我终于下定了决心。"

scene yard_r:
    size (1920, 1080) crop (240, 40, 1440, 810)
show mirabel neutral2 r:
    xzoom -1 xpos 0.5 xanchor 0.5
with wipedown_slow

Marcel smile u "好吧。你可以来我房间。"
show mirabel laugh2 r at bounce
Mirabel "太好啦！"
"米拉贝尔把双手合在一起，脸上的神情明亮得简直在发光。"
"看着她那分明的欢喜，我忍不住微笑起来，虽然心里有点困惑。"
Marcel ehe u "说真的，那里真没什么好看的……"
show mirabel shock2 r with dissolve
Mirabel "可对我来说有啊！我已经……哦，很久很久没进过别的女生的卧室了；自从我那些老朋友离开米耶纳之后就没有过！"
show mirabel laugh2 r with dissolve
Mirabel "我觉得这很有趣！"
show mirabel smile2 r with dissolve
Mirabel "我终于有了一个愿意跟我说话的朋友……"
Marcel neutral u "那么，这是不是意味着我们正式成为朋友了？"
show mirabel shy2 r with dissolve
Mirabel "呃，嗯……"
"米拉贝尔从睫毛底下抬头看我，突然变得羞怯，手指拨弄着辫梢儿。"
Mirabel "那是我们第一次在柴房里说话时你讲的，我当时就在想，嗯……要是你愿意做我的朋友，我也不介意。"
show mirabel ehe2 r with dissolve
Mirabel "我{i}确实{/i}会感到孤单，有个能说说话的人会很好；我的意思是，一个不会老是取笑我的人……"
Marcel smile u "那我们可以做朋友。"
show mirabel shock2 r with dissolve
Mirabel "可——可你确定这样好吗？你是{i}真心{/i}想跟我做朋友吗？"
Marcel neutral u "当然是真的。是我先开口的，而且我还让你进我的卧室，不是吗？"
show mirabel laugh2 r with dissolve
Mirabel "噢，是的！我真的很感激！谢谢你……！"
Marcel laugh u "真傻。"
"我朝她笑笑，摇了摇头。"
Marcel smile "你知道吗，朋友之间不必这样热情过头地谢来谢去。"
show mirabel shock2 r with dissolve
Mirabel "啊——那个……我——我真抱歉……！"
Marcel "你也不用道歉。你又没做错什么。"
Mirabel "我——我吗？嗯，那……我会尽量不再这样了！"
Marcel ehe u "而且我并没有在责备你……"
show mirabel shy2 r with dissolve
"米拉贝尔是那种特别爱道歉的女孩，即使错并不在她。"
"也许她早已习惯了被老师责骂，以至于「对不起」成了她在任何情况下的默认反应？"
"若真是这样，那就有点令人难过了。"
"我希望她在我身边不会感到不自在。我不觉得自己有什么威胁性，尽管我个子很高。"
"也许等我们聊过之后，她会更放松些。至少我是这么希望的。"
"不过，首先，有件事我大概应该告诉她……"
Marcel "你也别对我的卧室抱太大期待。它其实挺阴沉的。"
show mirabel shock2 r at bounce
Mirabel "阴沉？我才不信呢！只要有你在，就什么都不可能阴沉！"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
play music "bgm/Friendship.ogg" fadein 1.0
$ save_name = (__("{u}米拉贝尔篇{/u}{vspace=1}  10月27日{vspace=1}  米拉贝尔的仙境") )
scene marcel_room_w:
    size (1920, 1080) crop (80, 40, 1440, 810)
show mirabel shock2 r:
    xzoom -1 xpos 0.35 xanchor 0.5
with wiperight_slow
window show dissolve

Mirabel "那么，这就是你睡觉的地方？！"
"米拉贝尔好奇地打量着我的房间，她的双手在身前握在一起，活像跌进仙境之后的爱丽丝……"
"倒不是说我的房间有什么奇妙之处。"

show image "border" onlayer border
scene marcel_room_w:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

"我这间屋子天花板相当低，墙壁也挨得紧紧的，给人一种狭窄逼仄、叫人透不过气的感觉。"
"只有一扇单薄的窗户，嵌着年久蒙尘的旧玻璃，微微一阵风就会哗啦作响。"
"地板踩上去吱吱作响，钉子钉进木头里也不齐整，只等着绊倒那些刚睡醒、迷迷糊糊、毫无防备的女学生（也就是我）。"
"我的床靠在一个角落里，被子叠得整整齐齐。铁床架常常在我翻身时吱嘎作响，而且对我而言有点太小了。"
"床边是一张木桌，桌上放着一面有裂纹的镜子，还有几本我从巴黎带来的书。"
"母亲写来的信都夹在我那本卷了边、又旧又破的《基督山伯爵》书页里。"
"房间里还有一个木制五斗柜，放着我的衣服，鞋子则在它旁边的地板上整整齐齐地排成一排。"
"除此之外，我的房间就空空荡荡的了。"
"实在没什么可看的……"

hide image "border" onlayer border
scene marcel_room_w:
    size (1920, 1080) crop (80, 40, 1440, 810)
show mirabel smile2 r:
    xzoom -1 xpos 0.35 xanchor 0.5
with wipeleft_slow

"可是，尽管我内心对它颇有微词，米拉贝尔却睁大眼睛惊喜地打量着四周。"
show mirabel laugh2 r with dissolve
Mirabel "哦，真雅致！"
Marcel ehe u "它跟牢房差不多“雅致”……不过你喜欢的，我很高兴。"
show mirabel smile2 r with dissolve
"米拉贝尔没有理会我的打趣之词，仍盯着看。"

show mirabel:
    ease 1.0 xpos 0.40

"她像一只精灵似的在房间里翩然穿梭，一会儿停在窗前，一会儿又去端详搁在床头柜上的那面镜子。"

show image "border" onlayer border
scene marcel_room_w:
    size (1920, 1080) crop (600, 200, 640, 360)
with dissolve

Mirabel shock "你知道，那是会招来厄运的。"
"她指着那面布满细小裂纹的玻璃。"
Marcel sigh u "我知道，可摔碎它的不是我。我来的时候它就这样了。"
Mirabel "你得当心。地上可能还留着一些碎玻璃碴。我不希望你割破脚……"
Marcel smile u "我{i}是{/i}很小心，不过谢谢你的关心。"

hide image "border" onlayer border
scene marcel_room_w:
    size (1920, 1080) crop (80, 40, 1440, 810)
show mirabel ehe2 r:
    xzoom -1 xpos 0.40 xanchor 0.5
with wipeleft_slow

Mirabel "我忍不住要担心你……你是我这么长时间以来交到的第一个朋友，我得确保你没事……"
show mirabel shy2 r with dissolve
"她这番坦率的坦白似乎让米拉贝尔有些不安，因为她的脸颊泛起了粉色，低下了头。"
"她长长未剪的刘海垂了下来，遮住了眼睛。"
"米拉贝尔的刘海又厚又蓬松，让我想起设得兰矮种马，不过我没说出口。我不确定她会把它当作夸奖还是别的什么。"
show mirabel neutral2 r with dissolve
Mirabel "哦……？这些又是什么……？"
"也许是想要推进话题，米拉贝尔停下来端详我床头柜上的书。"
"我偏爱那种又厚又长、页码很多的书的（我觉得长篇故事更容易让人沉浸其中），而我桌上的书，对不喜欢读书的人来说恐怕显得很吓人。"
"米拉贝尔好奇地端详着最上面那本书的封面，一只手托在下巴底下。"
Mirabel "{i}基督山伯爵{/i}……？"
Marcel smile u "是大仲马写的。你听说过吗？它非常有名。"
show mirabel shy2 r with dissolve
Mirabel "嗯……那个……"
show mirabel ehe2 r with dissolve
Mirabel "我想我大概是偶尔听说过一两次，可我不知道它讲的是什么。"
show mirabel neutral2 r with dissolve
Mirabel "是什么样的小说？"
Marcel happy u "哦，非常精彩！"
"我在床上坐直了一些，心里涌起一股新生的热情。"
"我喜爱这部小说，可从来没有能和我聊它的人。学校里的男孩没一个愿意和我说话，而母亲也向来不怎么喜欢冒险故事。"
"这还是头一次有人认真地问我关于我最心爱的书的问题。"
Marcel smile u "这故事讲一个年轻人——他叫唐泰斯——蒙冤入狱，在经受了经年累月的折磨之后，终于从监狱里逃了出来。"
show mirabel sad2 r at bounce
Mirabel "折磨……？我不知道自己会不会喜欢这种内容……"
Marcel "这个嘛，那只是在故事的前半段。就像我说的，他逃出了监狱，然后发现了一笔宝藏，变得富有。"
Marcel happy u "然后他利用自己的财富，向过去所有亏待过他的人们复仇！"
Marcel "里面人物众多，情节也十分曲折。很难不让人被它深深吸引！"
Marcel smile u "改天你想借去读读吗？你也许会喜欢它！"
show mirabel shy2 r with dissolve
Mirabel "那个，嗯……你——你真好，可我不怎么读书。我不太能专注地看那些密密麻麻的字，嗯……而且……"
show mirabel sigh2 r with dissolve
Mirabel "我——我在家实在太忙了，要在面包店里帮忙，还要照看我弟弟。我没有时间！"
Marcel u sigh "哦。我明白了……"
"我咽下一声叹息。"
"我本指望能跟米拉贝尔因为这本书而亲近起来，可那不过是我的痴心妄想罢了。"
"以后我该学着更体贴一些才是。"
Marcel u smile "没关系。别放在心上。我们各有所好。"
Marcel "你不想借的话，不必勉强。"
show mirabel sad2 r with dissolve
Mirabel "谢谢你。你说得对，我想是这样，不过……"
"米拉贝尔又瞥了一眼我床头柜上那本陈旧的厚书。也许是我多心，可她的神情看起来几乎带着一丝懊悔？"
Mirabel "有时候，我觉得自己应该比现在更喜欢读书。要是我想当老师，就得提高我的读写能力……"
show mirabel scared2 r with dissolve
Mirabel "可一看到像那样又厚又大的书，我就打退堂鼓了！"
Mirabel "像那样的书，得啃上好几个月才能读完吧！"
Marcel ehe u "不习惯的时候，读书{i}确实{/i}挺慢的，不过万事皆然。"
Marcel smile u "等你习惯了，就能读得快一些。那时候，那些故事才会真正活起来！"
show mirabel neutral2 r with dissolve
Mirabel "哦，这我可说不好……"
show mirabel sad2 r with dissolve
Mirabel "我不太会想象东西。就算我能看懂书里看到的词——大部分词吧——我的脑子也没法把它们变成词以外的东西。"
Mirabel "我脑海里看不到任何画面。我想象不出那些人物。"
show mirabel sigh2 r with dissolve
Mirabel "这类书里的故事，就只是纸上某个人编造的文字罢了。对我来说，它从不会变成真的。"
show mirabel ehe2 r with dissolve
Mirabel "再说……我每读完一个长句子，通常就把句首讲的东西忘掉了。"
Mirabel "我是个没救的笨蛋。"
Marcel neutral u "我不觉得你是笨蛋。就像我说的，我们各有所长。"
"如今我倒开始后悔把书留在桌上了。我并没有想炫耀自己的学识或是别的什么。我自己也算不上多爱读书的人。"
"只是有少数几个故事，我喜欢偶尔拿起来读一读。"
Marcel laugh u "不过，等你沉浸到故事里去的时候，它们是很过瘾的。要是你真正投入进去，故事就能把你带到一个从未去过的崭新天地。那多叫人兴奋啊！"
show mirabel neutral2 r with dissolve
Mirabel "那我就信你的话吧……"
"米拉贝尔看起来并不是完全相信。"
show mirabel shock2 r with dissolve
Mirabel "可是玛塞尔，你是真的很聪明！之前英语课上那道难题你都解出来了，你还把这么厚、这么长的书当作消遣来读！"
show mirabel smile2 r with dissolve
Mirabel "你上课总是全神贯注，布吕吉埃夫人似乎也很喜欢你，课堂上老师点你回答问题时，你大多都答得对。"
show mirabel laugh2 r at bounce
Mirabel "你真是太棒了！"
Marcel ehe u "哈哈哈……别把话说得那么满……"
"我不习惯收到这么热情的称赞，虽然并非全然不受用，可着实有点叫人难为情。"
"不管米拉贝尔怎么说，我知道自己不聪明；真的不聪明。"
"在以前的学校里，我在学业上从未出类拔萃。我既不是班上最差的学生，也不是最好的。我只是平庸：普普通通而已。"
"要是我在姨母的学校里显得比大多数人聪明，那只是因为我在巴黎的课业更严格，老师也更加严苛。"
show mirabel shy2 r with dissolve
Mirabel "我在想，唔……我不想给你添麻烦，可要是不会太叨扰的话……"
show mirabel neutral2 r with dissolve
Mirabel "你能不能抽空帮我补习一下？"
show mirabel shock2 r with dissolve
Mirabel "我知道自己不是学校里最聪明的姑娘，可我真的好希望有朝一日能当上老师！"
Mirabel "我想通过结业考试，然后想进师范学校，还想为这个世界带来一点改变！"
show mirabel shy2 r with dissolve
Mirabel "同学们都取笑我。他们觉得像我这样的笨蛋，这辈子都休想当老师，可我不想放弃我的梦想！"
show mirabel ehe2 r with dissolve
Mirabel "嗯……话虽这么说，可我一直在自学，却什么都没学进去。我没法集中精神。什么都能让我分心。"
show mirabel neutral2 r with dissolve
Mirabel "我差一点就要放弃自己了，可是……我想，要是有你来帮我，我说不定还能有所长进。"
Mirabel "那么，呃……"
show mirabel shy2 r with dissolve
Mirabel "你觉得呢？帮帮我，会不会让你太为难？"
Mirabel "你要是不愿意，我能理解，可是……要是你每周能匀出一小时左右给我，我真的会感激不尽。"
"米拉贝尔看起来那么痛苦、那么率真可爱，棕色的眼睛睁得大大的，脸颊因窘迫而泛起红晕，让我无法把目光从她身上移开。"
"尽管她羞怯又敏感，可她对于当老师这件事真的十分执着。"
"她比什么都更想让自己的梦想成真……而她决定来找我帮忙。"
"那一定意味着她信任我。"
"她把她这个朋友当成了寄托，我不愿辜负她。"
"这就是为什么我毫不犹豫地答应了。"
Marcel smile u "我当然会帮你。朋友不就是这样吗？"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
play music "bgm/Mirabel.ogg" fadein 1.0
play ambience "sfx/wind.ogg" fadein 1.0
$ save_name = (__("{u}米拉贝尔篇{/u}{vspace=1}  10月27日{vspace=1}  玛塞尔小姐") )
scene sky3 with wiperight_slow
window show dissolve

# CG here?
"那天傍晚，我最终还是辅导起了米拉贝尔。"
"我并不能确定自己是不是个好家教。事前没有任何征兆，我也没有机会准备。"
"我以前也从没辅导过任何人。在原先的学校里，从没有人会来向我求助；一部分是因为我平庸的头脑，但更主要的是因为没有人愿意被人看到和我沾上关系。"
"这样被人依赖，感觉倒也确实不错，我想……{w} 可这毕竟是一段全然陌生的经历，我不由得感到压力。"
"我不想让米拉贝尔失望。"
"她把信任托付给了我，作为她新交的朋友，我有责任去实现她的期望。"
"尽管我自己也疑虑重重，我还是尽力凑合着往下走。"
"我从床头柜旁存着的一叠纸中抽出几张——那是我用来给母亲写信的纸——递给米拉贝尔。"
"然后，我给她出了一道类似课堂上那类法语作文题：{i}请特别留意你自身的道德准则与品格，给一位多年未见的兄弟写一封信{/i}这类题目。"
"我自己也不太喜欢这类题目。我没有兄弟，把时间消磨在给并不存在的人写虚构的信上，似乎也没什么意义。"
"我更愿意写一封真正的信给母亲——她独自在巴黎郁郁度日——比起布吕吉埃夫人，她更能懂得我的文字……"
"但这并不是问题的关键。"
"给米拉贝尔出了这样一道题后，我靠回椅背，静静观察她。"
"我房间里有一张书桌，却没有椅子，于是米拉贝尔只好坐在我的床上，拿我的一本书垫着那张纸。"
"这并不理想，我也担心她会不会弄坏我珍爱的那本{i}基度山伯爵{/i}，不过她对它很小心；至少，当她埋头于一道荒唐的作文题、舌尖微微探出嘴角时，她已经尽可能小心了。"
"我安静地注视着米拉贝尔埋头书写，她弯着腰伏在横线纸上。辫子垂落到肩头，双眼微微眯起。"
"她的字写得相当大——近乎孩子气——那些字常常像探洞者一样沉到横线之下，有时又高高飞起，顶到上一行去。"
"她的手不太稳，尽管努力想把字母连起来，却常常写不下去，在思索时把铅笔从纸上提起。"
"即便如此，尽管有这些不足，米拉贝尔依旧很认真对待这件事。"
"她在努力。"
"大约过了半个钟头（这也是布吕吉埃夫人在课堂上允许我们写作文的时间），我把那张纸从米拉贝尔手中拿过来，匆匆浏览了一遍。"

stop ambience fadeout 1.0
scene marcel_room_w:
    size (1920, 1080) crop (140, 40, 1440, 810)
show mirabel ehe2 r:
    xzoom -1 xpos 0.50 xanchor 0.5
with wipedown_slow

Mirabel "唔，这样可以吗？"
"米拉贝尔怯生生地望着我，缩着身子，手指上沾着铅芯的印痕。"
"她的神情带着期待，却是那种消极意义上的期待。她那微微颤抖的下唇，活脱脱一个只等着挨批的女孩——我很快就明白其中缘由了。"
"米拉贝尔这封短信里有大量拼写错误，文笔也相当稚嫩。"
"这封假托的信也过于简短；远远不足以向可能的考官展现米拉贝尔对法语的掌握程度。"
"我想，若是作者只有七岁，这样的信也许还算可圈可点，可米拉贝尔比这大了整整十岁。"
"我不知道该说些什么才不至于伤了米拉贝尔的心，可是……"
Marcel ehe u "嗯，总算是个开始。"
show mirabel sigh2 r with dissolve
Mirabel "我明白了……"
"米拉贝尔的肩膀颓然垮了下来。"
Mirabel "那意思就是说还不行喽。"
show mirabel sad2 r with dissolve
Mirabel "嗯，我早就知道了……"
Marcel huh u "不，唔……倒不是说不行本身。只是，唔……"
show mirabel ehe2 r with dissolve
Mirabel "没关系。你不用费心照顾我的感受。我早就知道自己是个笨蛋。大家都费尽心思来提醒我。我一时半会儿可忘不了！"
Marcel sad u "米拉贝尔……"
"米拉贝尔的文笔确实差强人意，但现在我开始怀疑，这背后是否另有缘由。"
"米拉贝尔是不是害怕学问？会不会是因为这个？"
Marcel neutral u "大家开始叫你笨蛋的时候，你多大年纪？"
show mirabel shock2 r with dissolve
Mirabel "哦，打从我有记忆起，他们就一直这么说了！"
show mirabel sad2 r with dissolve
Mirabel "我五岁那年进了村里的学校。我跟别的姑娘们一起待在幼儿班，可我比她们块头大，反应也比她们慢，长得也不怎么好看。"
Mirabel "别的姑娘都不愿意跟我玩，至于那位老师……"
show mirabel sigh2 r with dissolve
Mirabel "她准是觉得我是个毫无可取之处的迟钝丫头，所以对我才那么苛刻。我每犯一点错，她都要训斥我！"
show mirabel sad2 r with dissolve
Mirabel "也许我要是有别的姑娘那样的金发、蓝眼睛和牛奶似的皮肤，她就会对我和蔼些……可惜我很平凡。"
Mirabel "我的眼睛和头发是棕色的，肤色也深，还有满脸的雀斑……"
"米拉贝尔沮丧地叹了口气，一边扯着自己的辫子。"
Mirabel "老师对别的姑娘都和颜悦色，却把我当作碍事的人。"
show mirabel shy2 r with dissolve
Mirabel "就好像谁都不愿意让我留在身边一样。"
Marcel sad u "我明白了。"

play ambience "sfx/wind.ogg" fadein 1.0
scene sky3 with wipeup_slow

"我想我渐渐明白，为什么米拉贝尔在专心学业上会如此吃力了。"
"自幼年起就被人说成不过是个头脑简单的蠢货，想必在她心上留下了深深的烙印。"
"难怪米拉贝尔会觉得写作和算术那么令人焦头烂额。她不敢相信自己是聪明的，因为她从小就被灌输相反的念头。"
"若真要帮到米拉贝尔，首先我得设法树立起她的自信——可我该怎么做呢？"
"多年来，米拉贝尔一直在外貌和所谓的愚笨上遭受接二连三的重击。"
"要抹平所有这些创伤谈何容易，我甚至妄想自己能帮上忙，都未免太过自大了……"
"但是，尽管我们父子如此不同，我毕竟是乔治·德·圣雷米的儿子，而他（据母亲说）是当今整个基督教世界里最傲慢自负的人之一。"
"他浑身上下每一处都散发着自信，夜复一夜地站在舞台上，面对成群的崇拜者，没有一丝一毫的紧张。"
"我的父亲没有理由焦虑，因为他相信——事实上，他{i}从来{/i}都相信——自己每一件事都会成功。"
"我一点也不像父亲。我既害羞又安静，厌恶成为众人瞩目的焦点，但除了我这一副令人发窘的高个子外，我必定还从他那儿继承了点什么。"
"也许我能把他那份从容自信引来一些，传达给米拉贝尔？"
"我说过要帮她，也准备好不惜一切代价。"
"作为她的朋友，我不想让她失望。"
"于是，在片刻的停顿之后，我开口道……"

stop ambience fadeout 2.0
scene marcel_room_w:
    size (1920, 1080) crop (140, 40, 1440, 810)
show mirabel sad2 r:
    xzoom -1 xpos 0.50 xanchor 0.5
with wipedown_slow

Marcel smile u "嗯，我倒不觉得你平凡。"
show mirabel shock2 r at bounce
Mirabel "你、你不觉得吗？"
Marcel "一点也不。"

window hide dissolve
play sound "sfx/fall.ogg"
scene cg15 with wiperight_slow
$ achievement.grant("shoulder_to_cry_on")
$ renpy.pause(0.8)
window show dissolve

"我朝米拉贝尔挪近了些，床在我的大腿下吱呀作响，然后握住她的手指。"
"我把我们的掌心紧紧贴在一起，全然不顾脑海里那个惊慌失措、叫我快退开的声音，对她报以一笑。"
"那正是我在晚宴和日场演出上见过的、父亲脸上那种微笑——当他想向那些不是我母亲的美貌青年男女调情时的那种笑容。"
"一部分的我憎恨自己使出如此卑劣的手段，可另一部分的我却按捺不住那种冒充另一个人所带来的令人眩晕的兴奋。"
Marcel "你不平凡。"
"我再次向米拉贝尔强调，目光紧紧锁住她的双眼。"
Marcel "你有自己独特的美。"
Mirabel "我……我不太相信……"
Marcel "别不信。我是真心这么想的。"
Marcel "你不是你的老师和同学们以为的那种迟钝、笨拙的姑娘。"
Marcel "他们之所以挑剔你，是因为你不符合他们那套狭隘的美丑标准……{w} 可美是主观的。它取决于看的人。"
Mirabel "漂、漂亮……？！可、可这我就说不好了……"
Mirabel "你真的那么认为吗？"
Marcel "我当然这么认为，不然我不会说出口。你没有必要自卑。你很漂亮。"
Mirabel "可、可这我就说不好了……！唔……"
Mirabel "你是城里的姑娘。你住在巴黎。你在街上随便走走，想必就见过好多漂亮又时髦的女人……"
Mirabel "你比我漂亮得多，漂亮太多了。"
Marcel "哎呀，谢谢你。听你这么说，我很高兴。"
"我像一位骑士那样微微颔首。"
Marcel "我倒不觉得自己特别好看，可我领你这份情……"
Marcel "我也希望你能认可我的看法。"
Marcel "你很漂亮，米拉贝尔，可你的价值远不止于此。你甜美、善良，又那么用功。"
Mirabel "也许是白费力气！同学们都觉得我考不上，我自己也有几分信了。"
Mirabel "有时候我真不明白自己干嘛还要白费劲去试。既然到头来我只会把事情搞砸，那又有什么意义呢？"
Marcel "米拉贝尔……"
"我感到自己的眼神变得柔和。我的心正在融化。"
"我如此心疼这个可怜的姑娘，她为了实现梦想付出了那么多努力，以至于我只想将她紧紧搂进怀里，把她的头按在我的胸前。"
"我想拭去她眼角已经开始聚起的泪珠；她既难过又气恼，却不是气那些取笑她的人，而是气她自己所谓的失败。"
"米拉贝尔太过善良，即使别人贬低她，她也无法真正迁怒于人。她的自信心是那么低，以至于总是用自我贬损来为他们残酷的话语开脱：{i}唉，我大概罪有应得吧……{/i}"
"可她错了。她并不该受这些，而我想让她明白这一点。"
"也许我无法用一个拥抱来传达我的感情（那或许太突兀，而且也不大得体），但我下定决心，要用我所掌握的一切言语来抚慰她。"
"说到底，我能用的也只有言语了。"
Marcel "我知道这会很难——"
"这一点，从亲身体验中我深有体会。"
Marcel "——可你得学着不去理会那些唱衰的人。别让他们摆布你的人生。"
Marcel "你要是能试着更乐观一些，对你会大有好处。"
Mirabel "可要是人人都觉得我一无是处，我又怎么能乐观得起来呢？"
Marcel "那不是真的，米拉贝尔。你自己也知道那不是真的。"
"我把握住米拉贝尔的手指轻轻收紧了一些。"
"透过她的指尖，我能感到她身体的温度。这是一种令人安心的感觉，让我平静下来——尽管卧室的木地板上正悄然爬着幽暗的影子。"
"我已经和米拉贝尔坐了有一阵子了，傍晚正迅速临近。太阳很快就要落山了。"
"一阵凉风从窗外吹来。它拂动秋树的树梢，让枝叶瑟瑟颤抖；把落叶撒向地面，就像一个农夫为喂鸡而撒下谷物。"
"外面很冷，我的房间里也常常一样寒冷……可是和米拉贝尔在一起时，我就不觉得那么冷了。"
Marcel "我不相信你会考不上，米拉贝尔。"
Mirabel "可、可你才认识我没多久啊！"
Marcel "我认识你够久了。我知道我想和你做朋友，也知道我想看你成功。"
Mirabel "可是我怕……我八成会让你失望……"
Marcel "不会的。我保证。"
Marcel "要是从一开始我就料到你会让我失望，我根本就不会答应给你补习……"
Marcel "还有，要是你真觉得会失败，你就不会来找我帮忙了。"
Marcel "你一定相信还有机会——哪怕这机会再渺茫——你相信自己能通过考试。"
Marcel "要是已经认定自己必败无疑，谁还会费这么大力气去做一件事呢。"
Marcel "你{i}就是{/i}乐观的。你只是不敢承认罢了。"
Mirabel "嗯，或、或许你说得对。我当然希望能通过考试，当上真正的老师，可我不知道光靠自己要怎么做。看上去……是不可能的……"
Marcel "所以我才要帮你——可你得先学会帮自己，我才帮得上忙。"
Marcel "你觉得学习难，是因为你一直被灌输一个念头：再怎么努力也注定会失败。这让你连着手都犹豫不决……"
Marcel "可要是你训练自己去相信，自己真的能实现目标，学习应该会容易得多。"
Marcel "别去想你可能会失败。试着把心思放在你一定会成功这个信念上。"
Mirabel "可是那样的话，万一我真的失败了，我只怕会对自己更加失望……"
Marcel "那样的话，我会在这儿安慰你。在你需要的时候，在你觉得撑不下去的时候，我都会安抚你。"
Marcel "你不是孤身一人。"
Marcel "我会尽力教你，所以你也要反过来为我尽力。"
Marcel "努力去建立你的自信吧。那之后，一切都会水到渠成。"
Marcel "我对你有信心。或许得花些时间，可我相信你一定能做到。"
Mirabel "玛塞尔……"
"米拉贝尔吸了吸鼻子。"
"尽管我的房间里寒意弥漫，米拉贝尔的双颊却泛着淡淡的粉色。"
"她眨着眼睛望向我，长长的睫毛湿漉漉的，又被泪水染得深了一两分。"
"她凝视着我的脸，目光搜寻着、带着几分怀疑，仿佛想分辨出这究竟是不是什么残酷的玩笑——可当她在我的神色中只看见一片真挚，她的肩膀便松弛了下来。"
"她眨了一次眼，又眨了一次，然后……"
Mirabel "哦，玛塞尔！这是头一次有人对我说，对我有信心！"
Marcel "那我真高兴，能成为头一个这样对你说的人。"
Mirabel "哦，你呀……我……"

scene cg15_2 with dissolve

"米拉贝尔吸了吸鼻子。她用空着的那只手擦了擦眼睛，羞赧地笑了，为自己这番强烈情感的流露而窘迫。"
Mirabel "我原以为巴黎来的姑娘都是傲慢又势利的，可你却是我见过最善良的人！你待人这样好，我都不知道自己配不配得上你！"
Marcel "米拉贝尔……"
"我尽最大胆量，用尽可能坚定的语气对米拉贝尔说，手指把她握得更紧了一些。"
Marcel "谈不上什么配不配得上 。我们是朋友，仅此而已。"
Marcel "我想帮你，是因为我在乎你。就这么简单。"
Mirabel "玛塞尔……哦，玛塞尔……！太谢谢你了！"
Mirabel "既然你愿意为我这么用心，那我也一定为你加倍努力！我不会放弃，也不会让你失望！我发誓！"

play ambience "sfx/wind.ogg" fadein 1.0
scene sky3 with wipeup_slow

"伴着这句欢快的呼喊，米拉贝尔张开双臂，紧紧而温暖地环抱住了我。"
"她的头靠在我的胸前。我能感到她的发丝摩挲着我的脸颊。"
"她的手臂紧紧地环住我的腰，把我定在原地动弹不得，可我不在乎。"
"我{i}不想{/i}动。"
"能让米拉贝尔这样抱我，我已是求之不得，一边细细品味着她的双手、她的胸膛和她的脸颊传来的温暖。"
"她离我这么近，我发誓我能听见她的心跳，像一只被困住的鹧鸪那样怦怦直跳，就那样紧紧依偎着我……"
"又或者，这样急速擂动的是我的心。很难分辨。"
"我们两人如此紧密地交缠在一起，我甚至无从分辨米拉贝尔的身体在哪里终结，而我的又在哪里开始。"

stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene sky3 g with clockwipe
$ renpy.pause(0.5)
show overlay2
show message20 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message20
hide logo2
hide overlay2
with datetrans2

$ renpy.pause(0.3)

$ save_name = (__("{u}米拉贝尔篇{/u}{vspace=1}  11月18日{vspace=1}  丑闻") )
play music "bgm/Classroom.ogg" fadein 1.0
play ambience "sfx/wind.ogg" fadein 1.0
scene sky3 with dissolve
window show dissolve

"几个星期悄然流逝。在这些日子里，我每天晚上都在房间里与米拉贝尔见面，一同复习她在课堂上吃力应付的各个科目。"
"原来米拉贝尔每一样科目都很吃力，从自然科学到拼写无一例外，但我努力不让自己因此却步。"
"我说过要帮米拉贝尔，那我就一定会帮她。"
"秋天已开始悄然转入冬季，距离米拉贝尔参加期末考试还有半年。这时间应当足够了——至少我这样希望——足以把通过考试所需的一切知识传授给她。"
"只要我继续支持她，我确信米拉贝尔的自信心会随之提升，她的成绩也会一同进步。"
"米拉贝尔对学业投入到了这样的地步，甚至休息时间也会到我房间里来，好让我辅导她。"
"我并不太介意她时刻相伴。事实上，我相当享受。"
"正如米拉贝尔这辈子从未有过谁如此尽心尽力地帮她进步，我也从未有过谁这样依赖我。"
"我们住在巴黎时，母亲也常常倚靠我寻求支撑，但那并不完全相同。"
"她是我的母亲，不是我的朋友，尽管她本该是我的监护人，却如此依赖我提供情感上的支撑，以至于我常常因为太过内疚，反而不愿把自己的烦忧告诉她。"
"母亲依赖着我，而我不愿把话题的焦点转向我自己的烦恼，去让她不安……"
"可是，当然，她最终还是发现了。"
"当我被人推下楼梯、伤到了腿时，她不可能不发现。"
"当母亲得知我一直在受人欺负时，她相当难过。她问我——不，是盘问我——为什么要一直瞒着她，在那场不幸的事故之后的好几个月里，她都用一种受伤的眼神看着我。"
"和米拉贝尔在一起则不同。"
"她与我年纪相仿——至少相差无几——而我们被系在一起的，并非血缘，而是友谊。"
"人们说血浓于水，我同意，但米拉贝尔对我的依赖，感觉并不像母亲那般沉重。"
"帮助米拉贝尔让我感到自己在这世上有了一种意义；某种目标。"
"我想给她希望。"

stop ambience fadeout 1.0
scene classroom_r:
    size (1920, 1080) crop (350, 40, 1440, 810)
show mirabel sad2:
    xpos 0.75 xanchor 0.5 ypos 0.55 yanchor 0.5
with wipedown_slow

"在某一日，第三次辅导开始之前，我把椅子拉到米拉贝尔的书桌旁，翻看她在上一堂课算术本上解出的（或者说，至少试着解出的）那些算式。"
"她好奇地打量着我，头像鸟儿那样歪向一侧。"
Mirabel "那，唔……怎么样呀，玛塞尔？我有进步了吗？"
Marcel neutral u "嗯，让我看看……"

scene classroom_r blur:
    size (1920, 1080) crop (400, 120, 1152, 648)
show mirabel shy3:
    xpos 0.80 xanchor 0.5 ypos 0.55 yanchor 0.5
with dissolve

"我稍稍向前倾身，直到额头几乎触到米拉贝尔的额头。"
"这所乡村学校的书桌相当狭小。一个女孩勉强坐得舒服，更何况两个人，而我的大腿紧紧贴着我的朋友。"
"我们的腿缩在米拉贝尔那张木书桌的桌面下，紧紧缠绕在一起。"
"我们如今亲密到几乎形影不离，以至于班上有些同学开始对我们说些刻薄话；尤其是诺艾米。"

scene classroom_r:
    size (1920, 1080) crop (0, 40, 1440, 810)
show noemie frown2:
    xzoom -1 xpos 0.30 xanchor 0.5
with wipeleft_slow

"她趴在教室另一头，单手撑着脑袋打量着我们。她的表情冷硬而带着挑衅。"
Noémie "哎呀，你们俩就歇歇吧？"
Marcel neutral u "恕我不明白你在说什么。"
show noemie mad2 with dissolve
Noémie "我才不信你不明白！你坐在那儿，装得一脸天真无辜，可你们俩在打什么主意，分明就摆在眼前！"
Marcel frown u "那究竟是什么？"
Noémie "得了吧！"
"诺艾米哼了一声。"
Noémie "非要我在教室里当着大家挑明了吗？"
Mirabel sad "玛塞尔，别……"
"米拉贝尔轻轻把手搭在我的肩上，指望这能让我闭嘴……可是，当然，肌肤拂过我衣领的那一触，反而起了相反的作用。"
show noemie frown2 with dissolve
"诺艾米像马一样嗤了一声，双臂抱在胸前。"
Noémie "我真受不了！你们俩成天腻在一起，手指也碰，腿也挨，天知道都蹭到哪儿去了！"
Noémie "你们简直就跟一对热恋中的情侣似的！"

play ambience "sfx/footsteps3.ogg" fadein 0.5
show claudine smirk2:
    xzoom -1 xpos 1.20 xanchor 0.5 ypos 0.53 yanchor 0.5
    ease 1.2 xpos 0.70

$ renpy.pause(0.6)

stop ambience fadeout 0.5

Claudine "情侣？哎呀呀！"
"克洛蒂娜对这类风波眼光敏锐，忍不住也掺和进了这场对话。"
Claudine "好下流呀，诺艾米！"
show noemie shock2 at bounce
Noémie "我、我说的可不下流！{i}她们{/i}才是毫无廉耻的那一个！"
show noemie frown2 with dissolve
Noémie "两个姑娘成天那样腻在一块，本来就不成体统；尤其还是那个呆头呆脑、迷迷糊糊的米拉贝尔！看着她们我就反胃！"
show claudine smirk2 with dissolve
Claudine "哦？那你是吃醋了？"
show noemie shock2 at bounce
Noémie "吃、吃醋……？当然不是！"
show claudine smile2 with dissolve
Claudine "真稀奇。我还以为你眼里只有费利克斯呢，没想到你近来却挺留心玛塞尔的……"
show claudine laugh2 with dissolve
Claudine "真让人忍不住胡思乱想呢！"
Noémie "胡、胡思乱想什么？！"
show claudine smirk2 with dissolve
Claudine "这个嘛，{i}你{/i}是不是很想知道呀？"
Noémie "是啊，我想知道！所以我才问！我不许你这样往我身上泼脏水！"
Claudine "哎哟哟！你好大的火气！这下我{i}更{/i}好奇了！"
"克洛蒂娜的笑容加深了。"
Claudine "你对女人与女人之间那种事了解得多吗，诺艾米？几个月前你来我家做客的时候，该不会偷偷翻过我父亲的书吧？"
show noemie madblush2 with dissolve
Noémie "当、当然没有！别胡说八道！{i}你{/i}才是这儿最下贱的人！"

show noemie mad2:
    xzoom 1
with dissolve

$ renpy.pause(0.3)

play ambience "sfx/footsteps3.ogg" fadein 0.5
show noemie:
    ease 1.8 xpos -1.20

show claudine:
    ease 1.2 xpos 0.5

$ renpy.pause(1.0)

stop ambience fadeout 0.5

show claudine:
    xzoom 1
with dissolve

"于是，伴随着一声不满的哼唧，诺艾米别过了头。"
"我让目光在克洛蒂娜那张笑得很漂亮的脸上停留了一会儿。"
"尽管克洛蒂娜常常取笑米拉贝尔，我却觉得，她的取笑并不像其他一些女孩那样带刺。"
"她的话里往往并无真正的恶意；只是一种戏谑、疏离的玩味，就像猫在戏弄老鼠那样……"
"话又说回来，克洛蒂娜似乎对所有人都一视同仁地保持着这种疏远的讥讽——甚至连我原以为是她朋友的诺艾米也不例外。"
"也许在那一点上，是我看错了。"
"克洛蒂娜是故意为我们解围，还是仅仅想给自己找点乐子？"
"我不知道，但我还是感激她。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}米拉贝尔篇{/u}{vspace=1}  11月18日{vspace=1}  贪婪之手") )
play ambience2 "sfx/birds.ogg" fadein 1.0
scene sky3 with wiperight_slow
window show dissolve

"剩下的课就在再无事端中过去了，等到午饭时间，米拉贝尔问我们能不能到我房间去，好让我更仔细地看看她的算式。"
"我像往常一样欣然答应，为自己能够帮上忙而感到高兴。"

stop ambience2 fadeout 0.5
play ambience "sfx/footsteps2.ogg" fadein 0.5
show image "border" onlayer border
scene yard_r:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

"米拉贝尔和我一起穿过庭院，绕着水泵走了过去。"
"这是个寒冷的日子，天空阴沉多云。庭院旁的一些树还在固执地守着它们的叶子，尽管风霜雨雪正竭力将它们吹落。"
"寒风相当刺骨，撩起裙摆缠绕着我的双腿。我的脸颊开始泛起粉色，一心盼着回到屋里——那里虽然也没暖和多少，但至少好一些。"
"然而，我和米拉贝尔才走了没几步，便停了下来。"

play music "bgm/Energetic.ogg" fadein 1.0
stop ambience fadeout 0.5
hide image "border" onlayer border
scene yard_r
show marie sad r:
    xpos 0.5 xanchor 0.5
with wipeleft_slow

"庭院里站着一个小姑娘，我认得她，虽然我从未亲自同她说过话。"
"是玛丽-诺埃尔。"
show marie smile r at bounce
"玛丽-诺埃尔一看到米拉贝尔，整个神情都变了。"
show marie laugh r with dissolve
"她笑得咧开了嘴，露出几处缺牙的缝隙，反倒让她愈发可爱。"
Marie "米拉贝尔！米拉贝尔！"

play sound "sfx/rustle.ogg"
show marie:
    ease 1.2 xpos -0.20

$ renpy.pause(0.5)

scene yard_r:
    size (1920, 1080) crop (240, 40, 1440, 810)
show mirabel smile2 r:
    xzoom -1.0 xpos 0.30 xanchor 0.5 ypos 0.5 yanchor 0.5
show marie smile2 r:
    xpos 1.2 xanchor 0.5
    ease 1.6 xpos 0.70 xanchor 0.5
with wipeleft_slow

"玛丽-诺埃尔高兴地尖叫着，张开双臂朝前扑了过来。"
show mirabel laugh2 r with dissolve
Mirabel "玛丽-诺埃尔……！"
"米拉贝尔跪下来，张开双臂，在玛丽-诺埃尔冲进来时将她拥入怀中。"

play sound "sfx/rustle.ogg"
show marie:
    ease 0.8 xpos 0.44

"玛丽-诺埃尔虽然身形如此娇小孱弱，方才必定跑得飞快，因为小姑娘撞进她胸口时，米拉贝尔痛得皱起了眉。"

play sound "sfx/slap.ogg"
with hpunch

show mirabel shock2 r:
    ease 0.4 xpos 0.25
Mirabel "唉呀……"
show marie shock2 r at bounce
Marie "哦，米拉贝尔……"
"此刻，被保护者的双臂护住的玛丽-诺埃尔，带着几分关切抬头望着她的脸。"
show marie sad2 r with dissolve
Marie "我没伤到你吧……？"
show mirabel ehe2 r with dissolve
Mirabel "哦，没有，呃……我、我没事……"
"米拉贝尔显然{i}不是{/i}没事，但她不愿让小姑娘担心，于是强挤出一个微笑。"
show mirabel laugh2 r with dissolve
Mirabel "我只是又见到你很高兴，我的小鸭子！"
show marie smile2 r at bounce
Marie "真的吗？你想我了吗？！"
show mirabel smile2 r with dissolve
Mirabel "没错。感觉都好几年没见到你了！"
show marie laugh2 r at twirl
Marie "米拉贝尔！哦，米拉贝尔！"
"玛丽-诺埃尔被这番话哄住了，于是像小猫似的，把脸颊贴在米拉贝尔怀里磨蹭。"
Marie "我也想你！我超级超级想你！我超想你的！"
Mirabel "超想，嗯？那到底有多想呢？"
show marie smile2 r at bounce
Marie "嗯……我觉得是一大堆！就像大象那么大！"
show mirabel neutral2 r with dissolve
Mirabel "大象？我还从没见过大象呢……"
Marie "我见过，我见过！它们真的好大好大，就像……"

play sound "sfx/rustle.ogg"
show marie:
    ease 0.8 xpos 0.65

"玛丽-诺埃尔退后一步，把两条手臂尽力张到最开，像一只振翅欲飞的鸟儿。"
Marie "{i}这么{/i}大！"

show mirabel laugh2 r:
    ease 0.8 xpos 0.35

Mirabel "天哪！那真的{i}是{/i}很大！"
"米拉贝尔笑了起来，拍了拍玛丽-诺埃尔的深色卷发。"
"玛丽-诺埃尔低头垂首地站了一会儿，心满意足地享受着米拉贝尔的抚弄……"

stop music fadeout 1.0

show marie angry2 r with dissolve
"可随后她便对上我的目光，恶狠狠地瞪了过来。"

play music "bgm/Mysterious.ogg" fadein 1.0

Marie "那{i}这{/i}位是谁？"
show mirabel smile2 r with dissolve
Mirabel "她吗？她是我的朋友，玛塞尔。"
Marie "玛塞尔……？"
"玛丽-诺埃尔皱起鼻子。"
Marie "我以前从没跟她说过话。"
Mirabel "她来这所学校不久。她是九月搬来的。她以前住在巴黎。"
show marie shock2 r with dissolve
Marie "你才认识她两个月，她就已经是你的朋友了……？"
show marie angry2 r with dissolve
"玛丽-诺埃尔双臂交叉，挑剔地上下打量着我。"
"旁人或许以为，这样一个小姑娘的不满可以轻易置之不理，但玛丽-诺埃尔的目光却相当具有穿透力。"
"她清澈的蓝眼睛镶着极长的睫毛，那神情只能用鄙夷来形容。"
"我的个头几乎是她的两倍，却有种被她居高临下俯视着的感觉。"
Marcel shy u "呃……你好？很高兴认识你。"
"我朝玛丽-诺埃尔挥了挥手，但她没有回应。相反，她翘起鼻子，摆出一副公主般的傲慢姿态。"
show marie pout2 r with dissolve
Marie "哼！我倒看不出她有什么特别的！"
show mirabel shock2 r at bounce
Mirabel "玛丽-诺埃尔！别这么没礼貌！你应该好好打个招呼！"
show marie shout2 r with dissolve
Marie "可是我{i}不{/i}想！"
show mirabel sigh2 r with dissolve
Mirabel "哎呀，玛丽-诺埃尔……"
"米拉贝尔难过地叹了口气。"
show mirabel sad2 r with dissolve
Mirabel "对不起，玛塞尔……她平时不是这样的。玛丽-诺埃尔平时是个很可爱的女孩……"
Marcel ehe u "没关系，呃……我明白。对她来说我是个完全陌生的人。她对我有所戒备也很自然。"
Mirabel "但我希望她至少试着跟你好好相处。毕竟你是我的朋友……"
show marie angry2 r with dissolve
Marie "那我呢？！我也是你的朋友啊，米拉贝尔，而且你认识我的时间比{i}她{/i}长多了！"
show mirabel ehe2 r with dissolve
Mirabel "你当然是我的朋友，可玛塞尔最近一直在帮我补习功课。她是个很善良的人，我欠她很多。"
show marie pout2 r with dissolve
Marie "功课……？"
"玛丽-诺埃尔不悦地皱着眉，眉头越皱越紧。"
Marie "这就是你最近一直这么忙的原因吗？"
show mirabel smile2 r with dissolve
Mirabel "没错。我非常想通过今年年底的考试，玛塞尔说她愿意帮我。她人真好吧？"
show marie shout2 r with dissolve
Marie "不，这一点也{i}不{/i}好！学习很无聊！这个女孩也很无聊！"
show mirabel shock2 r with dissolve
Mirabel "别这么说！你根本不认识她。我相信，只要你跟她聊聊——"
Marie "我{i}不{/i}想跟她说话！我讨厌她！我讨厌她，我要她走开！"
Mirabel "玛丽-诺埃尔，求你了……你不该那样说讨厌别人！"
show marie angry2 r with dissolve
Marie "为什么不行？"
show mirabel sad2 r with dissolve
Mirabel "讨厌是很重的字眼，玛塞尔没做什么值得你讨厌的事。"
show marie shout2 r with dissolve
Marie "她做了！她要把你从我身边抢走！"
show marie wah2 r with dissolve
Marie "自从你跟这个女孩做朋友，你就不理我了！"
show marie sad2 r with dissolve
Marie "你为什么不再跟我玩了？你为什么现在不跟我玩？！"
show mirabel:
    ease 0.8 ypos 0.60
Mirabel "小鸭子……"
"米拉贝尔跪在玛丽-诺埃尔面前，双手扶住她纤瘦的肩膀。"
show mirabel neutral2 r with dissolve
Mirabel "你这么喜欢和我一起玩，我很高兴。我也喜欢和你一起玩，但通过这些考试对我很重要。我得专心，否则我可能永远无法实现我的梦想。"
show marie huh2 r with dissolve
Marie "你的梦想……？"
Mirabel "没错。你也有梦想吧，玛丽-诺埃尔？"
show marie sad2 r with dissolve
Marie "嗯，有的……"
"玛丽-诺埃尔咽了咽口水。她低头看着自己的鞋子，深色的睫毛轻轻颤动。"
Marie "我想再见见我的父母……"
Mirabel "如果你的梦想没有实现，你会难过的，对吧？"
Marie "会非常难过……"
show mirabel sad2 r with dissolve
Mirabel "嗯，如果我的梦想没有实现，我也会那么难过。要是这次考试又不及格，我真不知道该怎么办！"
show marie scared2 r with dissolve
Marie "你也会难过……？"
show mirabel neutral2 r with dissolve
Mirabel "没错。所以我现在不能陪你玩，才会花更多时间跟玛塞尔在一起。我得专心学习。"
show mirabel smile2 r with dissolve
Mirabel "我知道你也许会觉得孤单，但或许你可以把这当成一个机会。为什么不试着跟班上的几个女孩交朋友呢？"
show marie sad2 r with dissolve
"玛丽-诺埃尔瑟缩了一下，仿佛米拉贝尔威胁要打她似的。"
play sound "sfx/rustle.ogg"
show marie:
    ease 0.6 xpos 0.80
"她先退了一步，又退了第二步，眼中燃着怒火。"
show marie shout2 r with dissolve
Marie "不要！我才不要！"
show mirabel sad2 r:
    ease 0.8 ypos 0.5
Mirabel "可是——"
show marie angry2 r with dissolve
Marie "我{i}才不管{/i}你说什么！我不想跟班上那些蠢女孩交朋友！她们不喜欢我，我也不喜欢她们！"
Mirabel "你总可以试试。在你没发脾气的时候，你是个很可爱的女孩。我相信——"
show marie shout2 r with dissolve
Marie "不要，不要，不要！"
"玛丽-诺埃尔摇摇头，用脚跺着地面。她气得两颊通红，小小的手握成拳头垂在身侧。"
Marie "我才不跟别的女孩交朋友！我绝不！"
Mirabel "可是当我和玛塞尔在一起的时候，你怎么办呢？"
show marie sad2 r with dissolve
Marie "我想我只能一个人待着了……"
show marie angry2 r with dissolve
Marie "不过没关系。我不在乎。我已经习惯一个人了。"
show marie shout2 r with dissolve
Marie "米拉贝尔，你如果不跟我玩，那我也不需要你了！"

show marie sad2 r:
    xzoom -1
with dissolve

"玛丽-诺埃尔抽了抽鼻子。她别过头去，大约是想证明自己对米拉贝尔有多么不在乎……可我敢发誓，我看见她眼里开始凝聚起泪光。"
Marie "这就像爸爸妈妈一样。他们把我丢下了。每个人都是这样。"
show mirabel shock2 r with dissolve
Mirabel "我不会丢下你的，玛丽-诺埃尔……！"

show marie scared2 r:
    xzoom 1
with dissolve

Marie "可是你不再跟我玩了，是吗？"
show mirabel sad2 r with dissolve
Mirabel "对不起，玛丽-诺埃尔，可是……我不能。我没有时间。"
show marie sad2 r with dissolve
Marie "所以，你没时间陪我。我明白了。"
Marie "那算了……"
show marie shout2 r with dissolve
Marie "但我真希望你没有选择跟这个女孩玩！"
Marie "我真希望你没有选她！"
"玛丽-诺埃尔伸出指责的手指，直直指向我，活像在指认一个罪犯。"
"我确实已经够愧疚了。"
"我主动去帮米拉贝尔，是想看她微笑；可如今……我担心自己也许在不经意间，把一切都弄得更糟了。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}米拉贝尔篇{/u}{vspace=1}  11月18日{vspace=1}  焦虑") )
play music "bgm/Mirabel.ogg" fadein 1.0
scene marcel_room_w:
    size (1920, 1080) crop (140, 40, 1440, 810)
show mirabel neutral2 r:
    xzoom -1 xpos 0.50 xanchor 0.5
with wiperight_slow
window show dissolve

"那天晚上，我和米拉贝尔一起温习几道简单的算术题。"
"嗯，我说它们简单，可米拉贝尔似乎有些吃力。她已经卡在其中一道题上整整十分钟了，但她仍咬牙坚持着。"
"她俯下身，手里拿着铅笔，眯起了眼睛。"
"我发现，米拉贝尔专注的时候，有个前后摇晃身体的小习惯。她的辫子随着这些细微的动作轻轻晃动，几缕散落的发丝蜷曲在她脸颊旁。"
"这模样实在很可爱；还有她那粉嫩的、猫儿般的舌头，正从嘴角探出来。"
"和米拉贝尔独处一室、两人单独待在一起，总能让我感到安心……{w}可今天，我的思绪却一再飘远。"
"我无法停止去想玛丽-诺埃尔。"

window hide dissolve
scene white with slow_dissolve
scene yard_r g:
    size (1920, 1080) crop (240, 40, 1440, 810)
show marie angry2 g:
    xpos 0.5 xanchor 0.5
with dissolve
window show dissolve

"玛丽-诺埃尔尽管年纪那么小，先前却朝我投来如此可怕的一瞥，那目光仿佛要把我的皮肉从骨头上生生剐下来。"
"她就这么厌恶我和米拉贝尔待在一起吗？"
"我想问题并不在于米拉贝尔是特地和我在一起，而是因为她实在太忙，抽不出一丝片刻来陪伴她这位小朋友。"
"玛丽-诺埃尔一定觉得很孤单吧……"
"尽管我竭力想帮米拉贝尔，可把米拉贝尔与她分开，我这样做是否会太残忍了？"
"不过，米拉贝尔似乎全神贯注于她的功课。是她主动求我指导的，我答应帮她，并不觉得自己做错了什么。"
"至少，我不愿意相信自己做错了……"

window hide dissolve
scene white with dissolve
show image "border" onlayer border
scene marcel_room_w:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with slow_dissolve
window show dissolve

"我满心愧疚地在床上挪了挪身子。床架吱嘎作响，却没有惊动埋头学习的米拉贝尔。"
"我究竟怎么做才是对的？"
"我要怎样才能让米拉贝尔和玛丽-诺埃尔都开心？"
"我不知道。"
"当然，我明白玛丽-诺埃尔的幸福并不由我负责。我几乎不认识这个女孩。我和她说过的话不到五个字，而她回给我的话，全都是一概的敌意。"
"玛丽-诺埃尔不是我的妹妹，不是我的女儿，也不是我的朋友。我们之间没有任何关系。"
"那么，我为何会如此愧疚？"
"大约过了半个钟头，我结束了这场临时的学习——不单是为了米拉贝尔（随着时间流逝，她的注意力开始涣散），也是为了我自己。"
"我查看米拉贝尔试着平衡的那些分数题，目光扫过纸面。"
"我本该在批阅米拉贝尔的作业，可我的眼睛却无法聚焦。我其实什么也没看清。我脑子里满满都是玛丽-诺埃尔那副气鼓鼓、受了背叛的神情。"

hide image "border" onlayer border
scene marcel_room_w:
    size (1920, 1080) crop (140, 40, 1440, 810)
show mirabel neutral2 r:
    xzoom -1 xpos 0.50 xanchor 0.5 ypos 0.5 yanchor 0.5
with wipeleft_slow

Mirabel "玛塞尔……？"
"米拉贝尔显然察觉到了我的恍惚，担忧地望着我。"
show mirabel huh2 r with dissolve
Mirabel "你还好吧？"
Marcel huh u "哦，嗯……"
"我确实状态不太好，但这不是米拉贝尔的错。"
"她已经有那么多操心事，我不想再让她担心，于是尽力用一个浅浅的微笑去宽慰她，可那笑容却一点也不像是真的。"
"我或许是我父亲的儿子，但连他一半的戏都演不到。"
Marcel ehe u "我没事。"
show mirabel neutral2 r with dissolve
"米拉贝尔丝毫没有安心的样子。她一眼就把我看穿了。"
"我们不少同学似乎都以为她笨，可他们错了。虽然米拉贝尔记忆新学的东西比较吃力，但她远比旁人所以为的更具洞察力，尤其是对他人情绪的感受。"
show mirabel sad2 r with dissolve
Mirabel "我看你一点也不像没事……呃……"
Mirabel "我的分数真的那么差吗？"
show mirabel sigh2 r with dissolve
Mirabel "我知道我不太聪明，可我一直都在努力……"
Marcel "别太担心。这不是分数的问题。"
show mirabel huh2 r with dissolve
Mirabel "不是吗……？"
Marcel neutral u "不是。我心里想着别的事，仅此而已。"
show mirabel neutral2 r with dissolve
Mirabel "我明白了。呃……"
Mirabel "那{i}到底{/i}是什么在困扰你？"
Marcel sad u "我……不知道能不能说。"
show mirabel huh2 r with dissolve
Mirabel "是和我有关吗？"
Marcel sigh u "间接上说，算是吧。"
show mirabel sad2 r with dissolve
Mirabel "是关于我的功课吗？"
Marcel neutral u "我已经告诉过你，不是的。"
show mirabel sigh2 r with dissolve
Mirabel "我知道你这么说，可过去几周你一直在教我，我不知道自己有没有进步。"
show mirabel sad2 r with dissolve
Mirabel "如果你对教我这件事有点犹豫，我也不会觉得意外。"
Mirabel "你真的肯一直陪着我教了我这么久，我真的非常感谢你！"
show mirabel shock2 r with dissolve
Mirabel "你不需要为了我勉强自己。我不想给你添负担！"
Marcel sigh u "米拉贝尔，拜托你。"
"我叹了口气。"
"我很高兴米拉贝尔如此体贴周到，但凡事总有个度，过分操心别人的福祉，有时反而会适得其反。"
Marcel "你说得好像是你强迫我给你补习似的。"
show mirabel sad2 r with dissolve
Mirabel "嗯，也许确实是这样……"
Mirabel "我开口问你愿不愿意教我，而且我知道，因为你是个好人，你很可能会答应。"
show mirabel sigh2 r with dissolve
Mirabel "也许是我太自私了。"
Marcel shock u "你才不自私！我帮你是因为我{i}想{/i}帮你！"
show mirabel shock2 r with dissolve
Mirabel "真的吗？"
Marcel huh u "{i}真的，{/i}真的。我没骗你。"
Marcel "我喜欢帮你，因为这让我觉得高兴。就是这样而已。"
show mirabel neutral2 r with dissolve
Mirabel "可这不无聊吗？"
Marcel smile u "我不觉得无聊。这对我也很有帮助。"
Marcel "教你让我能重新复习课堂上讲过的内容，这样我自己也不会忘……而且你{i}确实{/i}一直在进步。"
show mirabel huh2 r with dissolve
Mirabel "我真的进步了吗？"
"我点了点头。"
Marcel "嗯。是循序渐进，但总归是进步。"
Marcel "你专心听我讲，也很努力，就算我指出你的错误，你也坚持继续。这说明你很有毅力。"
show mirabel shy2 r with dissolve
Mirabel "嗯，我、我不知道是不是这样……"
"米拉贝尔在这番夸奖之下，像温室里的一朵冬日花朵般蔫了下去。她低下头，想用长长的刘海遮住眼睛，但我还是看见一抹粉色在她脸颊上绽放开来。"
"我想她其实很享受这番夸奖，只是良好的教养让她不便欣然接受罢了。"
"这又是米拉贝尔讨人喜欢的另一面。每当我夸她，她总是那么容易脸红，反倒让我更想多夸她几句。"
Marcel "给你补习让我很有成就感，我宁愿把时间花在你身上，也不想跟学校里其他任何女孩在一起。"
Marcel "我并不担心你运算分数的能力。"
show mirabel neutral2 r with dissolve
Mirabel "嗯，既然你这么说……呃……"
"米拉贝尔把双手放在膝上。她的手指交缠在一起，从睫毛下抬眸望向我。"
"她的眼睛或许只是那种平平无奇的、泥褐色的棕色，但当冬日阳光微弱的余晖透过我那扇小窗悄然洒入时，那光便照亮了她的脸庞，让她几乎像是在发光。"
"此刻，她的眼睛看起来并不那么平淡，也不那么棕了。事实上，它们几乎像是闪烁着光芒。"
show mirabel sad2 r with dissolve
Mirabel "如果有什么事困扰着你，你愿意告诉我就好了；尤其是和我有关的事。"
Mirabel "如果我做了什么让你不高兴或惹你烦的事，我希望你能告诉我，这样我以后可以改正。"
show mirabel shock2 r:
    ease 0.8 ypos 0.60
Mirabel "请千万别顾及我的感受……！"
"米拉贝尔朝我低下头，手指在膝上紧合，做出一个臣服的姿态。"
"她这样俯身向前时，我能看见她不均匀的发缝和颈后。几缕纤细的、榛色的发丝正从她的辫子里松脱开来，那些辫子因为整天被抚摸，变得越来越乱。"
"这些发丝贴在她裸露的颈上，软软地印在她粉嫩的脸颊上。"
"当她这样俯身时，我几乎觉得自己像一位神父。我是不是该为她洒上圣水，或降下祝福呢？"
"当然，就算我想做，我也做不到。"
show mirabel sigh2 r with dissolve
Mirabel "请把你对我的真实想法都告诉我……！"
"米拉贝尔紧闭着双眼，摆出一副等待接受某种责难的神情。"
"她对这件事看得如此郑重，我不禁莞尔。"
Marcel smile u "我已经告诉过你我对你的看法了。我觉得你是个好朋友，你很善良，而且你总是逗我笑……并不总是故意的。"
show mirabel neutral2 r with dissolve
Mirabel "你、你是说，你觉得我有趣？"
Marcel "有时候，是的……但我喜欢你这一点。"
show mirabel shy2 r:
    ease 0.8 ypos 0.5
Mirabel "那么，呃……"
"米拉贝尔又坐直了身子，理了理自己的辫子。"
show mirabel neutral2 r with dissolve
Mirabel "你对我没有意见吗？"
Marcel neutral u "你的性格里我唯一有意见的，就是你太自卑了。"
Marcel sigh u "我希望你不要总是对自己那么苛刻，也希望你不要老是胡思乱想，以为我陪着你只是因为觉得自己有义务……"
Marcel smile u "但除此之外，我没有别的意见。"
show mirabel huh2 r with dissolve
Mirabel "那你刚才为什么看起来那么闷闷不乐……？"
Marcel sigh u "这……说来复杂。"
"我叹了口气，拨弄起自己的一缕头发（米拉贝尔的坏毛病一定传染上我了）。"
"我本不想和米拉贝尔谈这件事，怕惹她不快；但我担心，若不告诉她我烦忧的根源，她会在自己心里把这一切越放大越大，把自己当成全人类种种痛苦的罪魁祸首。"
"对于一个自称毫无想象力的女孩而言，米拉贝尔编排起自己惹恼、惹哭所有人的白日梦，倒是格外的拿手。"
Marcel neutral u "如果你一定要知道……我其实是在想你的那个小朋友，玛丽-诺埃尔。"
show mirabel sad2 r with dissolve
Mirabel "哦，是啊……我早该想到的。她刚才对你实在太没礼貌了。"
show mirabel sigh2 r with dissolve
Mirabel "她一向有点……冷淡，我想，但我从未听过她以那样轻蔑的口吻对长辈说话。"
Mirabel "玛丽-诺埃尔肯听我的，我想她是敬重我的。我本该替你再训斥她几句才是。"
show mirabel sad2 r with dissolve
Mirabel "若是我让你难堪了，我很抱歉。"
Marcel huh u "啊，你不必道歉。我并未因她的所作所为而动怒……"
show mirabel huh2 r with dissolve
Mirabel "你不生气？"
show mirabel neutral2 r with dissolve
"米拉贝尔皱起了眉头。"
Mirabel "倘若玛丽-诺埃尔敢那样对克洛蒂娜或诺艾米说话，她们准会揪住她的耳朵！"
Marcel smile u "那么，幸好我不是克洛蒂娜，也不是诺艾米。"
show mirabel ehe2 r with dissolve
Mirabel "是啊……我也常常这么想。"
Mirabel "我决计不可能像这样和克洛蒂娜或诺艾米坐在一起。她们真是难缠得紧……"
"米拉贝尔朝我露出一个浅浅的微笑，仿佛在确认我们的友谊。我也回以她一个微笑，虽然我的神情仍若有所思。"
"我无法停止去想玛丽-诺埃尔。"
"我并没有因为她伤害了我的自尊而难过（我的自尊曾遭受过比这样一个瘦弱小姑娘所能造成的更沉重的打击），我也不觉得自己受了什么冒犯。"
"我想我能理解她为何如此恨我。"
"在玛丽-诺埃尔看来，我必然像是一个闯入她与她心爱的米拉贝尔之间的不速之客。我不过是个碍事的人，这便解释了她为何想除掉我。"
"以一种孩子气、近乎天真的方式，玛丽-诺埃尔一定把我当成了必须消灭的对手，就像童话里那个善妒的继姐。"
"我怎能因为这样一个小姑娘沉溺于这般天真的念头就去恨她呢？"
"孩子，无论表面上多么乖巧伶俐，有时候也会比大多数成年人更小心眼、更记仇。"
"不过，孩子并没有什么真正的力量。他们往往无法对冒犯自己的人施以小小的报复，于是只好转而骂人、发脾气。"
"玛丽-诺埃尔的坏脾气是可以理解的，我甚至能体谅。"
"我不恨她，也没有非要从她身上逼出一句道歉的强烈欲望。"
"我没有生气。"
"而是……"
Marcel sad u "我……我想，我是在担心她。"
show mirabel neutral2 r with dissolve
Mirabel "担心？"
"米拉贝尔眨了眨眼。"
Mirabel "她对你说过那么多恶毒的话，你居然还担心她？！"
Marcel "是这样。"
"我点头表示赞成。"
Marcel neutral u "她是生我的气，没错，可是……与此同时，她看来是那样地不快乐。她当时落了泪。"
Marcel "她说我把你从她身边抢走了……但她又说她并不在意，因为她早已习惯了孤独。"
Marcel sigh u "我不愿她以为我在把你带走……但我想，我确实一直在这样做。"
Marcel sad u "我想我多少有些愧疚。我答应过帮你备考，却从未料到一个诺言竟会让一位年轻姑娘落泪……"
show mirabel smile2 r with dissolve
Mirabel "玛塞尔……"
"米拉贝尔温柔地朝我微笑。逆着从卧室窗户悄然渗入的、微弱的落日余晖，她的神情看起来几乎像天使一般。"

scene marcel_room_w blur:
    size (1920, 1080) crop (280, 40, 1152, 648)
show mirabel smile3 r:
    xzoom -1 xpos 0.50 xanchor 0.5
with dissolve

"她把一只手轻轻搭在我肩上，然后说道……"
Mirabel "你真是善良。"
Marcel shock u "我……是吗？"
Mirabel "嗯。我原以为你会要我因她无礼而责罚玛丽-诺埃尔，谁知你反倒担心起她是否快乐来。"
show mirabel laugh3 r with dissolve
Mirabel "哎呀，听来你关心她，竟几乎和我一样多呢！"
Marcel neutral u "这我可说不上。说真的，我几乎不认识那姑娘……"
Marcel sad u "我只是不愿见她难过罢了。"
show mirabel smile3 r with dissolve
Mirabel "所以我才说{i}几乎{/i}嘛。"
"米拉贝尔听了这句纠正轻轻笑了，可她的笑声很快便消融在我房间的寂静里。"
show mirabel neutral3 r with dissolve
"她的嘴唇仍抿着，一声轻叹从她微启的双唇间挣脱而出。"
show mirabel sad3 r with dissolve
Mirabel "说真的，我自己也有点担心玛丽-诺埃尔。自她踏进这所学校那天起，我便一直陪在她身边，她也始终依恋着我……"
Mirabel "可我也想过，她或许依恋得有些{i}过{/i}头了。"
Mirabel "她从不费心去结交同龄的朋友。我试着劝她，她却拒绝了。她说她不需要别的朋友，因为她有我。"
show mirabel sigh3 r with dissolve
Mirabel "我想我大概是把她宠坏了。我本该对她严厉一点，可我实在见不得她哭。"
Mirabel "尽管我总告诫自己别再惯着她，可到头来总是心软。只要她开口，我便陪她玩耍。我不愿她孤独……"
show mirabel ehe3 r with dissolve
Mirabel "而且，说真的，我自己过去也曾有几分孤独。"
show mirabel sad3 r with dissolve
Mirabel "玛丽-诺埃尔愿意亲近我，我原是很欢喜的，可如今……"
Marcel neutral u "你以为她该试着去结交些别的朋友？"
show mirabel sigh3 r with dissolve
"米拉贝尔点了点头。"
show mirabel neutral3 r with dissolve
Mirabel "我不可能永远待在这所学校。无论期末考试过不过，夏天我都得走。到那时，玛丽-诺埃尔便只剩下自己了。"
show mirabel sad3 r with dissolve
Mirabel "我不愿那情形发生……所以我想，不如在我们之间拉开些距离，或许才是最好的。"
Mirabel "我曾指望，若她不能同我玩耍，也许会开始和别的同学搭话……"
Mirabel "可这似乎并不奏效。我担心，若她不能同我说话，她宁可独自一人！"
Marcel huh u "她倒是当真相当执拗……"
show mirabel neutral3 r with dissolve
Mirabel "可不是，执拗得惊人。她准是随了她母亲的性子。她母亲是歌剧演员，据我所知，性情十分热烈。"
Marcel sigh u "玛丽-诺埃尔看来确确实实满腔热忱地恨着我……"
show mirabel sigh3 r with dissolve
Mirabel "若不是我把你拖进这摊浑水，她本不会如此。我当时没想明白……"
show mirabel sad3 r with dissolve
Mirabel "唉，这也不算什么新鲜事。我向来不动脑子。"
Marcel neutral u "嘿……别对自己这么苛责。"
"我伸出手，轻轻将一缕从米拉贝尔凌乱辫子中散落的卷发拢到她的耳后。"
show mirabel shy3 r with dissolve
"我的肌肤触碰到她的肌肤，纵使不过短短一瞬，却几乎像闪电般噼啪作响。"
Marcel smile u "你是我认识的人里最体贴的一个。"
show mirabel shock3 r with dissolve
Mirabel "你、你真的这么觉得吗？"
Marcel "我确实这么认为。你如此珍视玛丽-诺埃尔，我觉得十分动人；我也知道，放任她独自一人，你一定满怀愧疚。"
show mirabel sad3 r with dissolve
Mirabel "非常愧疚……"
show mirabel sigh3 r with dissolve
Mirabel "我觉得自己像个抛弃亲生孩子的母亲，可我知道我非这样做不可。"
show mirabel sad3 r with dissolve
Mirabel "玛丽-诺埃尔不能一直这样缠着我。这对她不好，也无助于她结交新朋友。"
Mirabel "我只想她过得快乐。"
Marcel "我知道你确是这样想。我敢说，玛丽-诺埃尔迟早也会明白这一点的。"
show mirabel huh3 r with dissolve
Mirabel "这可未必！她那么倔强……"
show mirabel smile3 r with dissolve
Mirabel "不过，谢谢你，玛塞尔。"
Marcel huh u "你为何向我道谢？"
show mirabel ehe3 r with dissolve
Mirabel "谢谢你告诉我，我做的是对的。似乎再没有别人这么想，连我自己也不例外。"
Mirabel "我总觉得自己活得一团糟，净做着与理应所做之事截然相反的事。"
Mirabel "我感激你对我这份信心。它让我对自己也多了几分自信。"
Marcel smile u "你{i}本该{/i}有自信。你没有不去自信的理由。"
show mirabel shy3 r with dissolve
Mirabel "这可说不准。我不知道自己配不配得上像你这样的朋友，可是……"
show mirabel ehe3 r with dissolve
Mirabel "谢谢你这样支持我。"
show mirabel smile3 r with dissolve
Mirabel "我会继续尽力而为——为了你，为了玛丽-诺埃尔……也为了我自己。"
Mirabel "我不想让任何人失望。"

stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene sky3 g with clockwipe
$ renpy.pause(0.5)
show overlay2
show message21 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message21
hide logo2
hide overlay2
with datetrans2

$ renpy.pause(0.3)

$ save_name = (__("{u}米拉贝尔篇{/u}{vspace=1}  12月7日{vspace=1}  萧瑟的深冬") )
play ambience "sfx/wind.ogg" fadein 1.0
play music "bgm/Casual_Day.ogg" fadein 1.0
scene sky3 with dissolve
window show dissolve

"时光在一种惬意，却也冻得人发抖的模糊感觉中继续流逝。"
"这些随着天气转冷而愈变愈短的日子，很快汇聚成数周，又在一个月里仿佛河流般流淌而去。"
"不知不觉，十二月已经来临。天空是炮灰色般的铅灰，风也前所未有地愈发急迫。"
"虽然还不曾下雪（天气还没冷到那个地步，尽管感觉上已经像是了），灰蒙蒙的云层却一再倾泄下成片成片的雨。"
"那雨多半在夜里落下，敲得我窗玻璃哗哗作响，在庭院里留下一个个足以让低年级小女生陷进去的大水洼。"
"我们这些年纪大的女孩被布吕吉埃夫人严厉地训斥，要我们以身作则，不许——“看在老天份上，克洛蒂娜！”——去跳过那些较大的水洼，或是在里面趟水。"
"克洛蒂娜嘛，毕竟是克洛蒂娜，她完全没把布吕吉埃夫人放在眼里。她似乎在雨天里自得其乐，像一位海洋女神。她站在庭院中，张开双臂，几乎是欣然迎接着这场雨。"
"而我这边，可就没那么热衷了。"
"米耶纳的雨确实比巴黎的雨清新——巴黎的雨吮在舌尖带着烟味，顺着石街流下时被尘土染得乌黑——可我并不特别想被淋湿。"
"米拉贝尔和我绕着那些水洼走，远远地避开它们。"
"在这糟糕天气来临之际，我那间小屋比以往任何时候都更冷，不过米拉贝尔的陪伴帮着暖了暖它。"
"米拉贝尔每天放学后都会来我的卧室，准时得如同钟表。在那里，我们两人一起研读课上记下的笔记，把所学的内容再过一遍。"
"我已对米拉贝尔待在我房里这一点再习惯不过，她不在时，屋里便显得格外萧索。"
"米拉贝尔的缺席，再加上这风声、雨声与寒意，让我比以往任何时候都更难入睡。"
"米拉贝尔不在时，我对她的思念远比我想象的更深——这实在奇怪，因为我们几乎是形影不离；简直像一个女学生的幻影，与其说是两个人，不如说是同一个生命。"
"我想与她共度的时光，比以往任何时候都要多……"
"但有一桩区区小事，却萦绕在我心头，令我良心不安，即便是在我和米拉贝尔在一起时。"
"我无法停止为玛丽-诺埃尔担忧。"
"我想她还没有原谅我独占米拉贝尔的时光。事实上，我觉得她如今比以往任何时候都更恨我。"
"在我们难得相逢的场合里，玛丽-诺埃尔总像一只猫似的悄然溜走，眼里蓄满雷霆般的怒意。"
"如果她找到了一群同龄的伙伴一同闲逛，我也就不必为这位难以捉摸的小小姐如此操心了；可每当我见到她，她总是一个人。"
"我开始担心，除了米拉贝尔之外，玛丽-诺埃尔恐怕一个朋友也没有。"

stop music fadeout 2.0
stop ambience fadeout 2.0
scene marcel_room_w:
    size (1920, 1080) crop (140, 40, 1440, 810)
show mirabel neutral2 r:
    xzoom -1 xpos 0.50 xanchor 0.5
with wipedown_slow

"在又一次与米拉贝尔的自习时段里，我向她吐露了这些忧虑，她与我看法一致。"

play music "bgm/Friendship.ogg" fadein 1.0

show mirabel sad2 r with dissolve
Mirabel "这一个月来，我或许对她过于严厉了些。我早该料到，要她交朋友是件难事。"
show mirabel sigh2 r with dissolve
Mirabel "我原以为与她保持距离，会给她一点推力，让她更合群些，可也许并不奏效……"
Marcel neutral u "也许她以为，一旦和同学搭话，自己便是认输了？"
show mirabel shock2 r with dissolve
Mirabel "她会输掉什么呢？她只会赢得朋友……！"
Marcel sigh u "这我知道，可她似乎是那种不管什么事都不肯认错的人。"
Marcel neutral u "她早已认定自己不喜欢班上的姑娘们，因此不肯搭理她们。她宁可独自一人，也不肯低头认输。"
show mirabel sad2 r with dissolve
Mirabel "你或许说得对。那倒真像是玛丽-诺埃尔会做的事。"
"米拉贝尔叹了口气。"
show mirabel sad2 r with dissolve
Mirabel "我该试着去和她谈谈。或许我是这学校里唯一能说得动她的人。"
Marcel neutral u "我觉得这主意不错。无论如何，我们得试一试。"
show mirabel neutral2 r with dissolve
Mirabel "是啊，你说得对极了！"
"米拉贝尔点了点头，仿佛在对自己确认着什么，然后说道……"
Mirabel "明早我会去找玛丽-诺埃尔，把我心里牵挂的事告诉她。"
Mirabel "我要告诉她，我不是厌倦了她，我仍然在乎她，我躲着她并不是因为讨厌她。我只是想让她多交些朋友。"
show mirabel ehe2 r with dissolve
Mirabel "若运气好些，她应当能明白道理。"
show mirabel laugh2 r with dissolve
Mirabel "也许我还该从父母的烘焙坊带些东西给她，为我的疏远道个歉。带个葡萄干圆面包……？玛丽-诺埃尔最爱葡萄干圆面包了！"
Marcel huh u "你觉得那样管用吗？"
show mirabel smile2 r with dissolve
Mirabel "但愿如此。"
show mirabel laugh2 r with dissolve
Mirabel "她或许会有点生我的气，可只要我给她点吃的，她应该就会消气了！"
Marcel smile u "你是说像猫一样……？"
show mirabel huh2 r with dissolve
Mirabel "那怎么就像猫了？"
Marcel "猫在没吃到东西之前总摆出一副冷淡高傲的样子，一有吃的，便亲近起来。"
Marcel "它们只在自己能落着好处时才显得温顺乖巧。"
show mirabel smile2 r with dissolve
Mirabel "唉，我倒不觉得我的玛丽-诺埃尔有那么工于心计。事实上，一提到葡萄干圆面包，她可是相当单纯呢！"
show mirabel laugh2 r with dissolve
"米拉贝尔咯咯笑了起来。"
Mirabel "明天我会早早起床，专为她挑个最大、葡萄干最多的面包卷。我相信她会喜欢的。"
show mirabel neutral2 r with dissolve
Mirabel "至少，但愿她会喜欢。"
Mirabel "若这还不能让她开心，我也不知还有别的什么能哄好她了。"

stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene sky3 g with clockwipe
show overlay2
show message22 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message22
hide logo2
hide overlay2
with datetrans2

$ renpy.pause(0.3)

$ save_name = (__("{u}米拉贝尔篇{/u}{vspace=1}  12月8日{vspace=1}  甜蜜的点心") )
play ambience "sfx/wind.ogg" fadein 1.0
play music "bgm/Casual_Day.ogg" fadein 1.0
scene sky3 with dissolve
window show dissolve

"第二天清早，米拉贝尔早早便到了学校。我在院子里那口抽水泵旁与她碰面，从头到脚都冻得瑟瑟发抖。"
"又是一个阴冷的日子，天空灰蒙蒙的。"
"阳光透过一层薄薄的云幕洒落，虽然微弱，仿佛在试图驱散即将来临的雨意，可我的希望并不算高。"
"昨夜也下过雨，院子里散布着的一洼洼静止的积水，几乎像是在渴求着陪伴。"
"我打了个寒颤，伸手环抱住自己。由于头发被一分为二，编成两条辫子扎在脑后，我的后颈显得格外暴露在这天气里。"
"刚到这所学校时，我梳起头发来颇为费劲，可如今做起来已近乎习以为常。"
"人真的是什么都能习惯。"
"如今，即便是从卧室那面有裂痕的镜子里望见自己穿裙子的模样，也不再令我感到不安了。"
"这一切都如此自然，我简直不明白当初它为何会让我难堪。"

stop ambience fadeout 1.0
scene yard_r
show mirabel neutral r:
    xzoom -1 xpos 0.5 xanchor 0.5
with wipedown_slow

"见到米拉贝尔时，我看出她也同我一样在发抖。她的牙齿不住打颤，那张柔嫩的脸庞因寒冷而泛起了红晕。"
"她双手捧着一个牛皮纸袋，把它紧紧贴在胸口，那样子如同一位置身地抱着婴孩的母亲。"
"我好奇地向她走近。"

play sound "sfx/rustle.ogg"
scene yard_r:
    size (1920, 1080) crop (240, 40, 1440, 810)
show mirabel neutral2 r:
    xzoom -1.0 xpos 0.5 xanchor 0.5 ypos 0.5 yanchor 0.5
with dissolve

Marcel huh u "那是你父母烘焙坊做的……？"
show mirabel smile2 r with dissolve
"米拉贝尔点了点头。"
Mirabel "今天早上我挑了个最大、最可口的葡萄干圆面包，全是为玛丽-诺埃尔准备的！"
show mirabel neutral2 r with dissolve
Mirabel "但愿她会喜欢。往常我常在早上拿烘焙坊的面包和糕点给她，或者……唉。"
show mirabel sigh2 r with dissolve
Mirabel "以前常给的，可近来好些时候没给了；自打遇见你之后就没再给过……"
Marcel shy u "呃，嗯……"
"我抬手揉了揉后颈，有些局促地瞥了一眼地面。"
Marcel "抱歉……？"
show mirabel shock2 r at bounce
Mirabel "哎呀，你不必道歉！这些都不是你的错！"
show mirabel neutral2 r with dissolve
Mirabel "其实……"
"米拉贝尔用一只手伸进纸袋深处，从中取出一样东西。那是一个温热、焦褐色的布里欧修面包，上面这儿那儿地点缀着醋栗。"
show mirabel smile2 r with dissolve
Mirabel "我还给你多带了一个，谢谢你一直陪在我身边。"
Marcel huh u "啊，你不必谢我……"
Mirabel "这没什么。我想谢谢你——就像你想给我补习一样，还记得吗？"
"米拉贝尔的眼睛如教堂的彩绘玻璃窗般闪亮，她把我前不久才对她随口说过的这句小话原样重复了出来。"
"我初识米拉贝尔时，她做梦也不会想到这样打趣我，即便只是玩笑；可我想，她与我相处已更加自在了。"
"她甚至会拿我开玩笑——尽管都不是刻薄的那种——而且她笑起来时，总是发自内心的欢喜。"
"我很庆幸我们竟能变得如此亲近。"
"我从未有过像米拉贝尔这样的朋友——严格说来，我甚至从未有过任何朋友。"
"若是她想送我一件礼物，我有什么理由拒绝呢？我不想让她失望。"
Marcel smile u "你若当真不介意，那我就……"
"我接过她递来的那只醋栗面包，捧在手心。"
"它是温热的，那股暖意渗进我的掌心，将双手中凛冽的寒意化开。"
"醋栗面包闻起来很香。刚出炉的糕点香气几乎一点也没被冷风吹散，直钻进我的鼻腔。"
"这让我想起从前在巴黎时，常与母亲去的一家小面包店。那并不是什么知名铺子；只是一间由一对母子经营的小店。"
"我的母亲时不时会带我去那儿（也许那对店主让她想起了我们——在一个更幸福的、想象中的世界里，我们俩都面颊红润、麻利地忙碌着？），而我总会挑些布里欧修卷或玛德琳蛋糕来尝。"
"我已经很久没去过那家面包店了。我原以为自己不会想念它，可这只醋栗面包却让那些旧日回忆如潮水般涌回心头。"
"我不禁怀念起在巴黎的旧日生活，尽管那时我并未怎么珍惜它。"
"我离开巴黎已经三个月了，简直难以置信。"
"时光当真飞逝。"
show mirabel neutral2 r with dissolve
Mirabel "玛塞尔……？"
"米拉贝尔好奇地打量着我，把那牛皮纸袋抱在胸前。"
show mirabel huh2 r with dissolve
Mirabel "你不想尝尝吗？"
show mirabel sad2 r with dissolve
"她眉头微蹙。"
Mirabel "你不喜欢葡萄干吗？"
Marcel shock u "不，不，我可喜欢葡萄干了！问题不在这里。我只是想起了一些事，哈哈……"
Marcel ehe u "这个面包卷让我想起在巴黎时，我和母亲去过的一家烘焙坊做的面包卷。"
show mirabel huh2 r with dissolve
Mirabel "在巴黎，是吗？"
show mirabel ehe2 r with dissolve
Mirabel "呃、呃，我也不知我父母烘焙坊做的糕点能否和巴黎的烘焙坊相比，可、可我还是希望你一样喜欢！"
Marcel smile u "我一定会的。"
"这甜点的香气，连同那金黄酥脆的外皮，让我直流口水。"
"今早我没吃什么早餐，而昨晚的晚餐则仿佛已是很久很久以前的事了。"
"我低下头，抿紧嘴唇，一口咬下那只醋栗面包。"
Marcel "嗯……"
"就在咬下的那一刻，我的口中顿时充满了醋栗面包那股厚实而浓郁的果香。"
"它的味道与我从前在巴黎吃过的醋栗面包并无多大不同。事实上，甚至可能更好吃。"
"醋栗在我齿间满足地爆开，酸涩而明快。而面包本身，则柔软而富嚼劲。"
"正是这种风味与口感的结合，才让醋栗面包如此美味。"
"我一面咽下一口松软的褐色面团，一面不由得心想：这真是一种可靠扎实的糕点。"
"它们做起来相当简单，用料也只有寥寥几样。无论在哪里，味道几乎都一样——是在巴黎的面包店买的，还是在米耶讷这所乡村学校的院子里吃的……可这反而更增添了它们的魅力。"
"醋栗面包也许并不精致，但这正是它们如此美味的原因。"

scene yard_r blur:
    size (1920, 1080) crop (390, 40, 1152, 648)
show mirabel neutral3 r:
    xzoom -1 xpos 0.5 xanchor 0.5
with dissolve

Mirabel "那么，你觉得如何？"
"米拉贝尔挨到我身边，棕色的眼睛睁得大大的。"
show mirabel shy3 r with dissolve
Mirabel "好吃吗……？"
Marcel smile u "嗯……"
"我咽下那一口醋栗面包，向米拉贝尔投去一个微笑。"
Marcel happy u "好吃极了！"
show mirabel laugh3 r with dissolve
Mirabel "哦，我真高兴！我方才还担心来着……"
Marcel "你不必担心。你父母做得很好。"
show mirabel neutral3 r with dissolve
Mirabel "嗯，那个……其实……"
show mirabel shy3 r with dissolve
Mirabel "跟你说实话，那个面包卷不是我父母做的。"
Marcel neutral u "那是谁做的？"
show mirabel ehe3 r with dissolve
Mirabel "嘿嘿……"
"米拉贝尔一手把纸袋抱在胸前，另一只手羞怯地举了起来，那模样像是课堂上举手回答问题的人。"
Mirabel "是我。"
Marcel huh u "你睡过头了？"
show mirabel smile3 r with dissolve
"米拉贝尔点了点头，同时羞怯地笑了笑。"
Mirabel "我一大早就起床，赶做了一炉足可配得上玛丽-诺埃尔的葡萄干圆面包。"
Mirabel "我想这样一来，这些面包卷或许就尝得出我的一点特别心思了……况且我父母不喜欢我拿他们打算卖的食物。"
show mirabel neutral3 r with dissolve
Mirabel "我做得好吗？"
Marcel shock u "你做得棒极了！我可不知道你烘焙这么在行！"
show mirabel shy3 r with dissolve
Mirabel "我没有；真的没有。"
Mirabel "我烘焙只是一般水平……可我父母{i}确实{/i}开着家烘焙坊，我从小便帮着他们。"
show mirabel ehe3 r with dissolve
Mirabel "想来我也只能零零碎碎地学了些门道……嘿嘿。"
show mirabel smile3 r with dissolve
Mirabel "唉，你喜欢就好！那是我烤的第二炉葡萄干圆面包。"
show mirabel neutral3 r with dissolve
Mirabel "第一炉我烤得太久，所以有点焦了；这一炉我又觉得大约没烤够火候……"
Mirabel "我本来想再烤一炉的，可那样我上学就要迟到了，而且我父母已经骂过我浪费食材了。"
show mirabel sad3 r with dissolve
Mirabel "我一直担心它们不好吃……"
Marcel smile u "啊——我明白了。原来你是在拿我当试吃的小白鼠，之后才把面包送给玛丽-诺埃尔？"
show mirabel shock3 r at bounce
Mirabel "没、没有……！"
show mirabel shy3 r with dissolve
Mirabel "那个，怎么说呢……也许有一点点吧——但你不介意，对吧？"
Mirabel "玛丽-诺埃尔对吃的东西可挑剔了，我不想把不好吃的东西送给她。"
Marcel happy u "没关系。你能这么信任我，让我尝你烤的点心，我真的很高兴。我深感荣幸。"
show mirabel ehe3 r with dissolve
Mirabel "我、我觉得你夸大其词了……不过还是谢谢你。你那么喜欢我烤的葡萄干面包，我真的好开心！"
show mirabel sigh3 r with dissolve
Mirabel "希望玛丽-诺埃尔也能喜欢。"

stop music fadeout 1.0
window hide dissolve
scene black with blinds2
$ renpy.pause(0.8)
$ save_name = (__("{u}米拉贝尔篇{/u}{vspace=1}  12月8日{vspace=1}  玛丽-诺埃尔在哪里？") )
play music "bgm/Sad.ogg" fadein 1.0
scene sky3 with blinds2
window show dissolve

"可是，尽管我和米拉贝尔在学校里找了足足十五分钟……"

scene yard_r:
    size (1920, 1080) crop (240, 40, 1440, 810)
show mirabel neutral2 r:
    xzoom -1.0 xpos 0.5 xanchor 0.5 ypos 0.5 yanchor 0.5
with wipedown_slow

Mirabel "哎呀，我完全不知道{i}她会在哪儿{/i}！"
"……我们却连那固执、板着脸的玛丽-诺埃尔的影子也没瞧见。"
"与此同时，米拉贝尔手中纸袋里的那只醋栗面包，正一刻比一刻更冷下去。"
"米拉贝尔焦虑地咬着下唇。"
"我们已经搜遍了学校及其庭院的每一个角落——所有教室、饭堂，甚至连音乐室都找过了——却始终没有寻见她。"
"她究竟会在哪里呢？"
show mirabel sad2 r with dissolve
Mirabel "我希望她不是在躲我……"
Marcel shock u "她为什么要躲你？她那么喜欢你！"
show mirabel sigh2 r with dissolve
Mirabel "她{i}以前{/i}是喜欢我的，可我这阵子一直对她那么疏远。她说不定是在故意躲开我气我，好让我内疚……"
show mirabel sad2 r with dissolve
Mirabel "玛丽-诺埃尔长着一张甜美的脸，可这种事她也不是做不出来。"
Marcel frown u "不过，我倒不觉得她会躲着你。"
Marcel "你这么好的人，我想没有人会存心想让你难过。"
show mirabel ehe2 r with dissolve
Mirabel "诶、诶嘿嘿……那个，嗯……谢谢你，玛塞尔……不过我拿不准玛丽-诺埃尔是不是跟你一样的想法。"
Marcel neutral u "我觉得她是这么想的，我敢肯定。也许我们没看到她，只是因为她还在宿舍里。"
show mirabel neutral2 r with dissolve
Mirabel "可是都这么晚了，学生是不许在宿舍里逗留的。"
"米拉贝尔将信将疑地环顾着校园。当初我和她第一次在这里碰面时，这儿除了树木空无一人；如今却挤满了各年级、穿着校服的学生。"
show mirabel huh2 r with dissolve
Mirabel "要是被抓到，她会惹上麻烦的。"
Marcel sad u "说不定她有正当理由逗留在那儿。最近天一直很冷，而玛丽-诺埃尔就算照她的年纪来看也长得很小。她说不定是得了什么病。"
show mirabel shock2 r with dissolve
Mirabel "生、生病？你真的这么觉得吗？！"
Marcel sigh u "有可能。她随时可能染上肺炎……"
"可我刚一提出这个建议，便后悔自己说出口。"
"我觉得自己的提议完全在情理之中，可光是这句话就让米拉贝尔的脸一下子白了。"
show mirabel scared2 r with dissolve
Mirabel "天、天哪……！我可怜的玛丽-诺埃尔……"
Mirabel "要是她真的病了，一直在等我来看她，而我却从没来过呢？她一定又难过又孤单！"
Marcel huh u "呃，我们现在还不知道她是不是生病了……"
show mirabel sad2 r with dissolve
Mirabel "我、我想也是，可是……万一真是肺炎呢……"
Mirabel "朱贝尔家的小娃娃，前两年冬天就是染上肺炎走的。医生说她只要好好休息就能好起来，可是……"
show mirabel scared2 r with dissolve
Mirabel "{size=-5}她还是死了……{/size}"
"米拉贝尔轻声说道，仿佛再大声一点说出这个故事结局，就会招来一段续篇似的。"
"我把一只手搭在米拉贝尔肩上，想安慰安慰她。"
Marcel neutral u "我说过了，我们还不知道她是不是生病了。那只是种可能罢了。"
show mirabel neutral2 r with dissolve
Mirabel "一种可能……是啊……"
show mirabel ehe2 r with dissolve
Mirabel "我想我是想得太远了……"
"米拉贝尔苦笑了一下。"
Mirabel "我还以为自己没有想象力呢。为什么一到往最坏的方面想时，它倒是灵得很？"
show mirabel sad2 r with dissolve
Mirabel "真对不起，把你也卷进来，玛塞尔。你一定还有更要紧的事要做。"
Marcel huh u "不会，没事。我也想帮你找玛丽-诺埃尔。"
Marcel "你起那么早就是为了烤那些葡萄干面包。要是它们白白浪费，那就太可惜了。"
show mirabel shock2 r at bounce
Mirabel "你、你真这么觉得……？"
Marcel smile u "我要是没这么想就不会这么说了。你烤的点心很好吃。我可不想让玛丽-诺埃尔错过——而且我敢肯定她也不想错过！"
"我安抚地对米拉贝尔笑了笑。与此同时，我不禁暗自思忖：来到这所学校后，我竟也成了个颇为温柔体贴的护花使者。"
"我一直以为我与父亲的相似之处仅限于身高，也许我错了。我与女性打交道，或许并不如我原本想象的那般笨拙……"
"至少，在涉及米拉贝尔时是这样。玛丽-诺埃尔则是另一回事了。"
Marcel neutral u "要不我们去问问她们班里一个女生吧？她们说不定知道她在哪儿。"
show mirabel sad2 r with dissolve
Mirabel "可是玛丽-诺埃尔班里的女生，没有一个是真心喜欢她的……"
Marcel "她们也许不喜欢她，可既然她们跟她一起上课、睡同一间宿舍，那她们总该知道她大概去了哪儿。"
Marcel "要是她真的病了，她们也该能告诉我们。那样多少也能让你放下些心事。"
show mirabel neutral2 r with dissolve
Mirabel "你说得也有道理……"
show mirabel sad2 r with dissolve
Mirabel "不过，要是她真的{i}是{/i}病了，我想我会更担心她。"
Mirabel "不过站在这里也没多大用。"
show mirabel neutral2 r with dissolve
"米拉贝尔环顾着校园。几个看起来与玛丽-诺埃尔年纪相仿的年轻女孩正低着头，匆匆赶路。"
Mirabel "好，我去问问她们。"

play ambience "sfx/footsteps2.ogg" fadein 0.5
show mirabel:
    ease 1.2 xpos 1.2

$ renpy.pause(0.8)

scene yard_r
show mirabel neutral r:
    xzoom -1 xpos -0.20 xanchor 0.5 ypos 0.5 yanchor 0.5
    ease 1.5 xpos 0.5
with wiperight_slow
stop ambience fadeout 0.5

"米拉贝尔战战兢兢地朝那群女孩走去。她脚步缓慢而迟疑，脸色苍白如纸。"
"我从没见过像米拉贝尔这么大年纪的女孩，在即将与比自己小这么多的孩子打交道时，竟露出如此紧张的神情。"
"若不是米拉贝尔的神情如此认真，她的这份紧张几乎可说是颇为有趣。"
show mirabel neutral r with dissolve
Mirabel "那个，打扰一下……你们是玛丽-诺埃尔班上的吧？"
GirlR "玛丽-诺埃尔？那个讨厌鬼？"
"其中一个女孩走上前来，眯起了眼睛。她似乎是这群低年级小姑娘里实际上的领头人。"
"她深色的头发用两条红色发带扎在脑后，那模样让我略微想起一位西班牙舞者，双眼的轮廓被一抹夸张的黑色睫毛勾勒出来。"
GirlR "玛丽-诺埃尔是不是惹你生气了？要不要好好教训她一顿？"
show mirabel shock r at bounce
Mirabel "哎呀不是，完全不是那么回事！"
GirlR "哦，这么说她{i}没有{/i}惹你生气？那可真是头一遭。"
GirlR "我看你是唯一一个会陪她待在一起的人了，米拉贝尔。我总以为你是出于可怜才那么做的。"
Mirabel "当然不是！我愿意跟玛丽-诺埃尔说话是因为我喜欢她！"
GirlR "那你到底喜欢她哪一点呢？"
Mirabel "每一点！"
GirlR "好。"
"那女孩翻了个白眼。"
GirlR "那你找她又是为了什么？"
show mirabel neutral r with dissolve
Mirabel "玛丽-诺埃尔是我的朋友，我最近一直很担心她。"
Mirabel "我有一阵子没见到她了，我觉得她说不定是在生我的气。我带了个葡萄干面包来逗她开心，可连她的人影都没见着。"
show mirabel sad r with dissolve
Mirabel "你知道她可能去哪儿吗？"
GirlR "谁知道呢？谁又在乎呢？玛丽-诺埃尔这阵子尽说些荒唐话，真正是荒唐透顶。"
Marcel neutral u "比如说？"
GirlR "那种话我可不会{i}当真{/i}。她就是想要引人注意罢了。"
GirlR "她觉得凭她一对自己蓝眼睛和卷头发，全世界都该围着她转。我承认她是长得有几分好看，可她的性子太坏了！"
GirlR "哼，我可不关心，就算她真的跑掉了，我也巴不得呢！"
show mirabel scared r with dissolve
Mirabel "什么……？玛丽-诺埃尔说她要离家出走？"
GirlR "没错。昨天她净说这个了。她一直念叨着说迈恩没人关心她；说她父母从不来看她；还说她要躲到森林里去过游荡的日子。"
GirlR "全都是这种没头没脑的话。"
GirlR "我倒不觉得她真有勇气离家出走，不过我心里倒有点希望她那么做。"
GirlR "她要是走了，对大家都清净多了！她整天耷拉着脸！我可受不了她！"
"不过，米拉贝尔已经不再听这女孩那番轻蔑的说辞。她眯起眼睛，脸色惨白如鬼。"
show mirabel sad r with dissolve
Mirabel "玛丽-诺埃尔……你怎么能这样，你这个小傻瓜？"
Marcel sad u "你不会真相信她跑掉了，对吧？"
show mirabel scared r with dissolve
Mirabel "换作别的女生说这种话，我是不会信的，可你也知道玛丽-诺埃尔有多倔！"
Mirabel "她只要说要做什么，就非得做到不可。"
show mirabel sad r with dissolve
Mirabel "她会冲进森林，然后迷路迷得找不着北，然后……"
show mirabel scared r with dissolve
Mirabel "要、要是有狼可怎么办？！"
Marcel shock u "没、没事的，米拉贝尔。狼只在夜里才出来，我敢肯定……"
Mirabel "可、可要是她在那儿待得太久，又没人看见她，那就……哦……！"
"米拉贝尔的手指猛地抽搐了一下。慌乱之中，她的纸袋掉到了地上。袋子砸向地面，撒出了仅剩的那只醋栗面包。"
"那只原本看起来如此美味的面包，如今已经冰凉，不再适合入口——不过米拉贝尔似乎并不怎么在意。"
"比起一个点心的命运，她有更重要的事挂在心头。"
show mirabel sad r with dissolve
Mirabel "要不是我躲着她，玛丽-诺埃尔就不会觉得那么孤单了。"
Mirabel "这一切都是因为我。"
Mirabel "全都是我的错。"
show mirabel scared r with dissolve
Mirabel "我得去找她！"

play sound "sfx/rustle.ogg"
show mirabel:
    ease 1.2 xpos 1.2

$ renpy.pause(0.8)

show image "border" onlayer border
scene yard_r:
    subpixel True
    size (1920, 1080) crop (0, 120, 1280, 720)
    linear 20.0 crop (350, 120, 1280, 720)
with wiperight_slow

Marcel shock u "喂，米拉贝尔……！"
"我在米拉贝尔身后呼唤，却几乎无济于事。虽说她并非什么身手矫健的人，可听到这个消息后，她却爆发出惊人的一股力气。"
"她早已跑了出去，对昨夜那场雨在校园里留下的点点水洼毫不在意，径直踏过它们，身后溅起一串水珠。"
"若是布吕吉埃夫人或杜布瓦夫人在这里，她们定会责备米拉贝尔的失态，可米拉贝尔已经顾不得那么多了。"
"她的裙摆湿了，鞋底也湿了。"
"她的袜子恐怕已经湿透，可她仍不停下脚步。"
"望着她渐行渐远的背影，我知道自己必须跟上去。我不能让她一个人去。"

hide image "border" onlayer border
scene yard_r
with wipeleft_slow

GirlR "喂，玛塞尔……"
"那个刚才与米拉贝尔说话的年轻女孩看着我，然后皱起了眉头。"
"她似乎知道我的名字，可我并不知道她的。"
"是因为我作为来自巴黎的新生，身上那层光鲜的光环吗？"
"我想我已经不再是新生了——我在这儿已经待了三个月——可米耶讷是个几乎没有什么闲言碎语可传的小村庄。"
"这些女孩还能谈些什么呢？"
Marcel huh u "怎么了？"
GirlR "米拉贝尔怎么了？她怎么看起来那么害怕？"
GirlR "我觉得玛丽-诺埃尔{i}真的{/i}跑掉了。这又是她耍的什么蠢把戏——而且，就算不是，她跑掉了也怪不到米拉贝尔头上。"
GirlR "她对玛丽-诺埃尔真的很好。她是这所学校里唯一受得了她的人！"
Marcel sad u "我也不觉得这怪米拉贝尔……可要是玛丽-诺埃尔真出了什么事，她照样会把责任全揽到自己身上。"
Marcel "我不知道她会不会原谅自己。"
GirlR "我真搞不懂。别人做的事，我绝不会怪到自己头上。那也太蠢了。"
Marcel ehe u "也许等你再长大一点，你就明白了。"
GirlR "不可能！我可比那明智多了！"
"我冲那位扎着红色发带的女孩笑了笑，然后转身去找米拉贝尔。"
"村里的教堂钟声很快就要敲响。若是追上去，我今天的头一节课便要迟到——可那又有什么要紧呢？"
"米拉贝尔比那些重要得多。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
play ambience "sfx/night_amb.ogg" fadein 1.0
play music "bgm/Mysterious.ogg" fadein 1.0
$ save_name = (__("{u}米拉贝尔篇{/u}{vspace=1}  12月8日{vspace=1}  走进树林") )
scene forest:
    size (1920, 1080) crop (240, 40, 1440, 810)
show fog_bg:
    size (1920, 1080) crop (240, 40, 1440, 810)
show mirabel shy2 r:
    xzoom -1 xpos 0.5 xanchor 0.5
show fog_fg:
    size (1920, 1080) crop (240, 40, 1440, 810)
with wiperight_slow
window show dissolve

Mirabel "喂，玛塞尔……"
Marcel neutral u "怎么了？"
Mirabel "我只是想说，嗯……谢谢你陪我一起来。你本不必这样的，我很感激。"
Marcel ehe u "哎呀，别这样。你早就该知道，你不需要谢我。"
"我试图给米拉贝尔一个安慰的微笑，可连我自己都看得出那笑容有多么勉强。"
Marcel "我只是做了任何一个朋友都会做的事。我怎么能让你一个人在林子里乱闯呢！"
show mirabel shock2 r with dissolve
Mirabel "哦、噢……嗯……"
"米拉贝尔垂下目光，望向地面。在四周树木的阴影下，她那双比平日更显幽暗的棕色眼睛里，满是愧疚。"
show mirabel sad2 r with dissolve
Mirabel "我、我希望你不是勉强自己来的。"
Marcel smile u "做你的朋友不是一种负担。就像我已经说过的，这是一种荣幸。"
show mirabel shy2 r with dissolve
Mirabel "这、这我可说不上来……"
Marcel neutral u "{i}我{/i}知道。好了，别说了。我们得留意着点。"
"是为了玛丽-诺埃尔，还是为了那些潜藏在灌木丛间的可能的猛兽，我也说不准。我想，我们就等着看先遇上哪一样吧。"
"米拉贝尔紧挨着我走。我们的脚步踩碎脚下的枯枝，以及秋天残余下的零星落叶。"

play ambience2 "sfx/footsteps2.ogg" fadein 1.0
show image "border" onlayer border
scene forest:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
show fog_bg:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
show fog_fg:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

"每走一步，我的身体都绷得紧紧的。双肩僵硬；双眼眯起，警惕地张望着。"
"米耶讷是个紧邻一片茂密森林的小村庄。那些树木又高又瘦，光秃秃的枝杈几乎像长矛一般刺向天空。"
"这些树木大多是落叶乔木，它们早已因畏惧冬霜而落尽了叶子。"
"这里那儿点缀着几棵常青树，可由于林中如此幽暗，它们那生机勃勃的浓绿色泽也被蒙上了一层黯淡。"
"四周的树木都高高耸立在我们头顶，遮住了那淡淡的蓝天。"
"我以为校园里已经很冷了，可这里更要冷得多。"
"地面崎岖不平。我只得小心翼翼地在这泥地上落脚，尽力避开树根与倒下的枝条。"
"我很担心，在这林子里，我们真会撞上一处野兽的巢穴。"
"我们那长长的校裙和端庄的黑鞋，本就不是为了在森林里穿行而备的；我也从不知道有哪个女学生能跑得比狼还快。"
"若是真碰到潜藏在这儿的什么怪物，我们必然处于劣势。没有风，也帮不了我们。"
"我倒是想退回去，可又怎么能呢？"
"在找到玛丽-诺埃尔之前，我们不能离开——尽管我开始担忧，我们到底能不能找到她。"

stop ambience2 fadeout 1.0
hide image "border" onlayer border
scene forest:
    size (1920, 1080) crop (240, 40, 1440, 810)
show fog_bg:
    size (1920, 1080) crop (240, 40, 1440, 810)
show mirabel sad2 r:
    xzoom -1 xpos 0.5 xanchor 0.5
show fog_fg:
    size (1920, 1080) crop (240, 40, 1440, 810)
with wipeleft_slow

Mirabel "感觉我们好像已经走了好几个钟头了……"
"米拉贝尔也并没有夸大其词。我不确定我们俩在这森林里走了多久，可真说不定已经有几个钟头了。"
"在这片森林里，时间仿佛统统模糊成一团，辨不清彼此；这里暗得几乎像是海底深处。"
"我们也许只是待了几分钟，也许是几个钟头，甚至可能是好几天。"
show mirabel sigh2 r with dissolve
Mirabel "真希望能找到玛丽-诺埃尔……"
Marcel neutral u "我敢肯定我们会找到的。"
"我试着让自己听起来很乐观，可我的决心已开始动摇。我讲出来的语气，并不如我自己所希望的那样笃定。"
"如果连我自己都无法欺骗，我又怎么能指望安慰米拉贝尔呢？"
show mirabel sad2 r with dissolve
Mirabel "真抱歉把你拖进来，玛塞尔。你为了我连今天的课都逃了！"
Mirabel "等我们回去，布吕吉埃夫人一定会很生我的气。"
show mirabel sigh2 r with dissolve
Mirabel "她总生我的气，因为我做事太慢，可我觉得她喜欢你。要是你因为我而受罚，那就太可惜了……"
Marcel huh u "喂，等等。你说的“要是我们回去”是什么意思？我们当然要回去！"
show mirabel huh2 r with dissolve
Mirabel "当、当然要回去啦！我刚才只是在想，嗯……"
show mirabel sad2 r with dissolve
Mirabel "我们总归有这个可能碰上狼的。"
Marcel frown u "我们不会碰上狼的。它们白天不出来。我已经跟你说过了。"
"至少，这正是我试图让自己相信的——但我仍有一些疑虑。"
"别提布吕吉埃夫人可能会有的怒火了。她对我与米拉贝尔迟到的恼怒，比起一群狂躁、半饥半饱的恶狼的凶残暴怒，简直不值一提。"
"我不知道，当血肉还活着时就被从骨头上剥下来，那会是怎样一种感受……"
"我无法想象那会是什么好受的感觉。"
"我是个彻头彻尾的懦夫，光是撞到脚趾，或是被缝衣针刺到手指，都能惹得我落泪。"
"我觉得我无论如何也承受不了几十颗尖锐锋利的牙齿撕咬我毫无防备的身体……"
"不过，虽说这不算是多大的安慰，我怀疑没几个人能承受得了那种事；就连从前学校里那些嘲笑我意志薄弱的男孩们也不例外。"
"如果我真的意志薄弱，我就根本不会走进这片森林；哪怕是为了米拉贝尔。"
"待在米耶讷改变了我。"
"我依旧对疼痛避之不及，也算不上勇敢；不过也许，我已不像曾经那样是个懦夫了。"
"那一定是因为，我现在有了一个需要勇敢的理由。"
"米拉贝尔正依靠着我，这意味着我必须为了她而坚强。"
"我必须唤起自己仅有的那一点点勇气，把它化作继续前行的力量。只要专注于自己身体单调重复的动作，这并不算太难。"

play ambience2 "sfx/footsteps2.ogg" fadein 0.5
show image "border" onlayer border
scene forest:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
show fog_bg:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
show fog_fg:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

"右脚跨过左脚。"
"右脚跨过左脚。"
"右——"
Mirabel shock "啊……"

stop ambience2 fadeout 0.5
hide image "border" onlayer border
scene forest:
    size (1920, 1080) crop (240, 40, 1440, 810)
show fog_bg:
    size (1920, 1080) crop (240, 40, 1440, 810)
show mirabel shock2 r:
    xzoom -1 xpos 0.5 xanchor 0.5
show fog_fg:
    size (1920, 1080) crop (240, 40, 1440, 810)
with wipeleft_slow

"突然，米拉贝尔停了下来。她的身体僵住，仿佛生了根一般。"
"我也停了下来。我不得不如此，因为我的手臂还和米拉贝尔挽在一起。"
"我们正站在一道小峡谷的边缘，四周还有更多的树木环绕。"
"我顺着泥土的坡脊向下望去，看着谷底的地面。那并不算太远——这道峡谷大约一米来深——但光是看到大地骤然断裂的景象，就足以让我不寒而栗。"
"我把视线从那处落差上移开，然后看向米拉贝尔。"
"她的眼睛因惊恐而瞪大，目光像受惊的小鹿一般慌乱地四处扫视。"
"一定是什么东西吓到了她，可那会是什么呢？"
Marcel huh u "怎么了？"
show mirabel neutral2 r with dissolve
Mirabel "我、我好像听到什么动静了……"
Marcel frown u "你确定吗？也许只是风声，要么是我们自己的脚步声。"
show mirabel shock2 r with dissolve
Mirabel "不、不是的，绝对不是，我敢发誓！"
"米拉贝尔的声音压成了耳语。她惊恐地环顾着森林，试图揣测那神秘声响的来源。"
show mirabel neutral2 r with dissolve
Mirabel "我听到灌木丛里有动静。听起来像是某种动物……"
Marcel shock u "动物？"
Mirabel "对、对。而且好像离我们很近。我想——"
play sound "sfx/rustle.ogg"
"但我始终没能听到米拉贝尔的想法，因为她被一阵响亮的窸窣声打断了。"
"橡树根部的一小片绿丛开始颤动起来。"
"一根树枝咔嚓断裂。"
"我觉得那不是狼。狼不可能藏身于这么一小片绿丛之中。那声响的来源多半是某个娇小无害的东西——也许是一只兔子？——但还没等我来得及安慰米拉贝尔……"

scene forest blur:
    size (1920, 1080) crop (390, 40, 1152, 648)
show fog_bg:
    size (1920, 1080) crop (390, 40, 1152, 648)
show mirabel shock3 r:
    xzoom -1 xpos 0.5 xanchor 0.5
show fog_fg:
    size (1920, 1080) crop (390, 40, 1152, 648)
with dissolve

Mirabel "玛、玛塞尔……！！！"
"……她就惊慌失措地扑向了我。"
"她的胸口紧贴着我的，双臂则缠上了我的腰。"
"不幸的是，她扑到我身上时，力道似乎大了一些。"
Marcel shock u "啊、啊……"
"我踉跄着向后倒退，喘不过气来。"
"我的身体摇晃着，紧接着……"
Marcel "噢、噢……！"

scene sky3 with wipeup_slow

"……我脚下的地面消失了。"
"一定是米拉贝尔把我推下了峡谷的边缘！"
"那是我向后跌落之前，脑海中掠过的最后一个念头。"
"我什么也做不了，无法支撑住自己的身体。"
"我根本无法保护自己。"
"我能做的，只有绷紧身体，迎接这场坠落……"
Mirabel shock "玛塞尔……！"
"而我也确实坠了下去。"

play sound "sfx/collapse.ogg"
show image "border" onlayer border
scene forest2:
    size (1920, 1080) crop (300, 400, 640, 360)
show fog_fg:
    size (1920, 1080) crop (300, 400, 640, 360)
with vpunch

"我的后背砰然撞上地面，后脑勺也磕在了一棵树上。"
"有几秒钟的工夫，我难受得喘不过气来。"
"我用失神的双眼仰望天空，它已被高耸于头顶的树木遮得严严实实。我的脑袋晕眩起来，树木开始重影；两棵，继而三棵，继而四棵……"
"森林像旋转木马一般在我四周打着转。"
"我觉得一阵恶心。"
"我的头和后背都疼得阵阵抽痛。我一定是摔在了什么东西上面——几块石头或散落的枯枝——因为我想我划伤了自己。"
"我希望我没有撕破校服。布吕吉埃夫人对此可{i}不会{/i}高兴。"
"我试着坐起来，可浑身疼得厉害。每一个动作，无论多么轻微，都让我的胃里翻江倒海。"
"我为什么会这么难受……？"

play sound "sfx/rustle.ogg"
hide image "border" onlayer border
scene forest2
show fog_bg
show mirabel shock r:
    xzoom -1 xpos -0.20 xanchor 0.5 ypos 0.5 yanchor 0.5
    ease 1.2 xpos 0.30
show fog_fg
with wipeup_slow

Mirabel "玛塞尔！玛塞尔？！"
"米拉贝尔在我身后呼喊，她的声音尖利，因担忧而紧绷。"
"如果她还能冷静思考，她大概不会这样尖叫。她可能会引来比兔子更危险的生物。然而，显而易见的是，她{i}并没有{/i}在思考；至少没有在考虑常识层面的问题。"
"她太过担心我的安危了。"
"我想我对此还是心存感激的，尽管她的哭喊声让我头疼。"
show mirabel scared r with dissolve
Mirabel "玛塞尔？！"

play ambience2 "sfx/footsteps2.ogg" fadein 3.0

"米拉贝尔的哭喊声在我的颅骨里回荡。那声音震耳欲聋。"
"一切声响都太吵了。我能听见树枝在微风中吱嘎作响；我能听见心脏在胸中砰砰跳动；我发誓我甚至能听见虫子在我四周的泥土里钻动……"
"我还能听见别的什么。"
"脚步声。"
"也许是米拉贝尔……？"
"这脚步声太轻柔、太细碎，不像她的。"
"那会是谁呢？"
"我直起身子坐好，脑袋一直隐隐作痛，然后转过头去。"
"我眨了眨眼睛。"

scene forest2 blur:
    size (1920, 1080) crop (400, 220, 1152, 648)
show fog_bg:
    size (1920, 1080) crop (400, 220, 1152, 648)
show marie shock3 r:
    xpos 0.50 xanchor 0.5 ypos 0.50 yanchor 0.5
show fog_fg:
    size (1920, 1080) crop (400, 220, 1152, 648)
with wiperight_slow
stop ambience2 fadeout 1.0

"那边，在离我仅几步远的地方，站着一个穿着端庄校服的身影……"
Marie "玛塞尔……？是、是你吗……？"
"……是玛丽-诺埃尔。"

stop music fadeout 1.0
stop ambience fadeout 1.0
window hide dissolve
scene black with blinds2
$ renpy.pause(0.8)
play music "bgm/Confession.ogg" fadein 1.0
play ambience "sfx/night_amb.ogg" fadein 1.0
scene forest2
show fog_bg
show mirabel shock r:
    xzoom -1 xpos 0.20 xanchor 0.5
show marie neutral r:
    xpos 0.80 xanchor 0.5
show fog_fg
with blinds2
window show dissolve

Mirabel "玛丽-诺埃尔！原来你在这儿！我担心坏了！"
show marie huh r at bounce
Marie "米、米拉贝尔……？你怎么会在这里？"
show mirabel neutral r with dissolve
Mirabel "这句话该我问你才对，笨丫头！"
show mirabel scared r with dissolve
Mirabel "哦，玛丽-诺埃尔……我的小玛丽-诺埃尔！"

play sound "sfx/rustle.ogg"
show mirabel:
    ease 1.0 xpos 0.60

$ renpy.pause(0.4)

scene forest2:
    size (1920, 1080) crop (240, 40, 1440, 810)
show fog_bg:
    size (1920, 1080) crop (240, 40, 1440, 810)
show mirabel scared2 r:
    xzoom -1 xpos -0.20 xanchor 0.5 ypos 0.5 yanchor 0.5
    ease 1.2 xpos 0.35
show marie neutral2 r:
    xpos 0.65 xanchor 0.5
show fog_fg:
    size (1920, 1080) crop (240, 40, 1440, 810)
with wiperight_slow

"米拉贝尔冲向那个正站在橡树旁踌躇不前的小女孩，在她面前蹲下。"

show mirabel:
    ease 0.6 ypos 0.55

Mirabel "你这个小傻瓜……"
show mirabel sad2 r with dissolve
Mirabel "你在这里待了多久了？你是什么时候跑出来的？"
show marie sad2 r with dissolve
Marie "今天早上，吃早餐的时候。我从食堂溜出来，就跑了。"
show mirabel shock2 r with dissolve
Mirabel "那你应该没在这里待太久。至少这个还让人放心一点——可是天哪，你全身都冰凉了！"
Mirabel "我们得把你带回学校，好好暖和起来！"
show marie scared2 r with dissolve
Marie "你要带我回去？"
Mirabel "当然啦！我怎么能让你留在这林子里，你这个小傻瓜！我本来还怕你会被狼袭击呢！"
show marie neutral2 r with dissolve
Marie "狼白天是不会出来的。我没事。"
show mirabel sad2 r with dissolve
Mirabel "可万一你{i}不是{/i}没事呢？你可能会绊倒摔断腿，或者撞到头，或者划破膝盖！"
show marie huh2 r with dissolve
Marie "你是说，就像玛塞尔那样？"
Marcel sad u "嗯……"

show image "border" onlayer border
scene forest2:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
show fog_bg:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
show fog_fg:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

"我微微一缩，脸颊因窘迫而泛起红晕，垂眼看向地面。"
"尽管重重地摔了一跤，我倒觉得还算过得去。"
"我的脑袋已经不疼了，这算是件好事，我也能站起来了，不再感到疼痛；或者说，至少没有身体上的疼痛。"
"自尊心则是另一回事，不过我本就不觉得自己有太多那样的东西。"
"由于那次难受的着地，我裙子背面沾满了泥土，而那些替我垫了背、使我免于摔得更重的树枝和枝桠，也划破了我的腿。"
"我的校服破了好几处，裙背的丝带也松开了，但为了确保玛丽-诺埃尔的安全，这点代价算不了什么。"
"至少我不是唯一一个看起来狼狈不堪的人。"
"玛丽-诺埃尔也同样狼狈。她的鞋底沾满了泥土，裙子弄得脏兮兮的，头发里还缠着几片树叶，像缀着丝带一般。"

hide image "border" onlayer border
scene forest2
show fog_bg
show mirabel shock r:
    xzoom -1 xpos 0.35 xanchor 0.5 ypos 0.55 yanchor 0.5
    ease 0.8 ypos 0.50
show marie neutral r:
    xpos 0.65 xanchor 0.5
show fog_fg
with wipeleft_slow

Mirabel "哦，对了……！玛塞尔……！"
"米拉贝尔似乎突然想起我的存在，睁大眼睛看向我。"
show mirabel sad r with dissolve
Mirabel "你没事吧？你没伤着哪里，对吧？"
Marcel sigh u "我想我没事……"
show mirabel shock r with dissolve
Mirabel "你确定吗？你没有扭到哪儿吧？"
show mirabel sad r with dissolve
Mirabel "你能站起来吗？需要帮忙吗？"
Marcel ehe u "我真的没事，我保证。我没摔多远。"
show marie angry r with dissolve
Marie "你弄出了好大的声响。吓了我一跳。"
Marcel frown u "呃，抱歉打扰到你了……"
show mirabel sigh r with dissolve
"米拉贝尔，果真是米拉贝尔，依旧在焦躁不安，手上不停地绞着手指。"
Mirabel "都是我不好，你才会摔倒。要不是我推了你，就……"
Marcel smile u "那是个意外。别放在心上。"
show mirabel scared r with dissolve
Mirabel "可、可我怎么能{i}不{/i}担心呢？我真的弄伤你了！"
show mirabel sad r with dissolve
Mirabel "我真是又笨又冒失。你能受得了我，简直是个奇迹！"
Mirabel "我这个朋友真是太差劲了！"
Marcel huh u "那，我们换个角度想想好不好？你是故意推我的吗？"
show mirabel shock r at bounce
Mirabel "当然不是！我绝不会那么做！"
Marcel smile u "那就没什么好担心的了。"
Marcel "我还活着，也没摔断哪根骨头。一切都没事。"
"至少据我所见是这样。"
Marcel "你不用为我操心。你不是还在担心玛丽-诺埃尔吗？"
show mirabel sad r with dissolve
Mirabel "哦，对啊！没错！"

scene forest2:
    size (1920, 1080) crop (240, 40, 1440, 810)
show fog_bg:
    size (1920, 1080) crop (240, 40, 1440, 810)
show mirabel shock2 r:
    xzoom -1 xpos 0.35 xanchor 0.5
show marie neutral2 r:
    xpos 0.65 xanchor 0.5
show fog_fg:
    size (1920, 1080) crop (240, 40, 1440, 810)
with wiperight_slow

"米拉贝尔转回身，看向那个我们冒了生命危险去救的小女孩。"
"她站在一棵高大橡树旁，树干粗壮宽阔，相形之下，她显得比以往任何时候都更加娇小、纤弱。"
"我们头顶的橡树枝条在颤抖。树叶沙沙作响，汇成一曲轻柔而带着不祥之兆的交响。"
"听起来就像有数不清的、隐形不可见的人正在悄悄议论着我们。"
show mirabel sad2 r with dissolve
Mirabel "你这个小傻瓜，大傻瓜。你怎么一个人跑到这儿来了？你难道不怕吗？！"
show marie sad2 r with dissolve
Marie "我害怕，可是我告诉自己那不要紧。我以为不会有人惦记我。"
show mirabel shock2 r at bounce
Mirabel "我们当然会惦记你！玛塞尔和我都担心坏了！"
Mirabel "我们一知道你不见，就马上出来找你了——我们也很害怕！"
show marie huh2 r with dissolve
Marie "你吓着了？"
show mirabel scared2 r with dissolve
Mirabel "怕得要命！我担心你可能会伤着自己，担心得脑子都乱成一团了！"
Mirabel "要是你摔断了骨头、撞破了头，或者死掉了……"
Mirabel "哦，那我可承受不了！"
Mirabel "我们找了你好几个小时！玛塞尔在找你的路上还受了伤，全是为了你！"
show marie pout2 r with dissolve
Marie "哦，是吗？那又如何？"
"玛丽-诺埃尔撅起嘴，然后双手在胸前交叉。"
Marie "我从来没让你们来找我！是你们自己要找的！"
Mirabel "我知道你没有，可我们怎么能丢下你不管呢？那我心里会难受死的！"
show marie shout2 r with dissolve
Marie "哼，{i}那{/i}才好。你们{i}就该{/i}难受！"
Mirabel "什么……？"
play sound "sfx/rustle.ogg"
show mirabel huh2 r:
    ease 0.8 xpos 0.28
"米拉贝尔后退一步，一手捂住胸口，仿佛被刺痛了一般。"
Mirabel "你不是认真的，对吧？"
show marie wah2 r with dissolve
Marie "我是认真的！我说的每一句都是真心话！"
Marie "你{i}就该{/i}难受，米拉贝尔，我才不管玛塞尔是不是受了伤！你们俩都伤害了{i}我！{/i}"
Marie "你们伤了我的心，却根本不在乎！"
show mirabel shock2 r:
    ease 0.8 xpos 0.35
Mirabel "可我{i}真{/i}的在乎，玛丽-诺埃尔！我很在乎你！你对我来说很珍贵！"
show marie huh2 r with dissolve
Marie "这么说我很珍贵，是吗？"
"玛丽-诺埃尔抬起头来。她的蓝眼睛与米拉贝尔的棕色眼眸相遇，在高耸橡树的阴影下，显得深沉而充满挑衅。"
show marie angry2 r with dissolve
Marie "既然我这么珍贵，那你为什么一直不理我？"
Marie "你说了我是你的朋友！你说过会陪我玩，会对我好……"
show marie shout2 r with dissolve
Marie "可是这整整一个月，你几乎都没跟我说过话！这太不公平了！"

play sound "sfx/rustle.ogg"
scene forest2 blur:
    size (1920, 1080) crop (400, 220, 1152, 648)
show fog_bg:
    size (1920, 1080) crop (400, 220, 1152, 648)
show marie angry3 r:
    xpos 0.50 xanchor 0.5 ypos 0.50 yanchor 0.5
show fog_fg:
    size (1920, 1080) crop (400, 220, 1152, 648)
with dissolve

"玛丽-诺埃尔用小脚在地上一跺。她脚下的一根树枝咔嚓一声断成两截。"
"她的表情因愤怒与悲伤交织而扭曲，下唇微微颤抖。"
"最终，过了片刻，悲伤占了上风，因为她抽噎了一下，低下了头。"
"她的眼睛泛着泪光。"
show marie sad3 r with dissolve
Marie "我以为你厌倦我了，就像我妈妈和爸爸那样。"
Marie "我以为你再也不会、永远不会跟我说话了，我都不知道该怎么办……"
show marie angry3 r with dissolve
"苦涩而懊恼的泪水顺着玛丽-诺埃尔泛红的脸颊滑落。她的双手在身侧攥成拳头，双肩微微颤抖。"
"她咬紧了牙关。"
"我觉得她并不想哭，可她实在控制不住自己。"
"她一定已经难受了很长很长的时间。如今，这份情绪终于宣泄了出来。"

scene forest2:
    size (1920, 1080) crop (240, 40, 1440, 810)
show fog_bg:
    size (1920, 1080) crop (240, 40, 1440, 810)
show mirabel sad2 r:
    xzoom -1 xpos 0.35 xanchor 0.5
show marie angry2 r:
    xpos 0.65 xanchor 0.5
show fog_fg:
    size (1920, 1080) crop (240, 40, 1440, 810)
with dissolve

Mirabel "哦，玛丽-诺埃尔……我可怜的玛丽-诺埃尔。对不起。"
Mirabel "我从没想过要让你觉得自己是多余、不被爱的。那跟事实实在是相差太远了。"
show marie sad2 r with dissolve
Marie "那你为什么不陪我玩？！为什么一直不理我？！"
show mirabel scared2 r with dissolve
Mirabel "那是因为……哦，是我太傻了！"
show mirabel sad2 r with dissolve
Mirabel "我一直专心在学业上，我想着如果我们不黏在一起太久，也许对你反而是件好事。"
Mirabel "我心想，如果我不在，也许你就会被逼着去跟班上其他女孩交朋友。"
Mirabel "不管我期末考试及不及格，我很快都得离开这所学校了，我担心到那时你会孤零零一个人！"
show marie shock2 r at bounce
Marie "诶、诶？"
"玛丽-诺埃尔望着米拉贝尔，眼睛因震惊而瞪得大大的。"
Marie "你真的要离开我吗……？"
show mirabel sigh2 r with dissolve
Mirabel "当然会。说实话，我这个年纪还在上学，已经太大了。"
show marie angry2 r with dissolve
Marie "才不是！你才不老；不像布吕吉埃夫人那样！"
show mirabel shock2 r with dissolve
Mirabel "呃，但愿如此！"
show mirabel sad2 r with dissolve
Mirabel "我确实没有布吕吉埃夫人那么老，不过我一月就满十七岁了。我比班上其他女孩都大一岁。"
Mirabel "我本该去年就离校的，不过学校又给了我一次参加期末考试的机会。"
show mirabel sigh2 r with dissolve
Mirabel "我不想辜负给了我这次机会的父母，所以我一直在拼命用功……而且我走之后，也不想让你孤单。"
show marie shout2 r with dissolve
Marie "可、可我不想你走！这太不公平了！"
show mirabel sad2 r with dissolve
Mirabel "我知道这不公平，我也不想离开你，可我不得不走。"
show marie wah2 r with dissolve
Marie "不要！不要，不要，不要！"
"玛丽-诺埃尔试图抗议，眼睛因坚定而眯起……但她一定明白，尽管带着孩子气的倔强，却无法阻止时间的流逝。"
"无论发生什么，米拉贝尔总有一天不得不离开她。她根本别无选择。"
"玛丽-诺埃尔抽了抽鼻子，终于回过神来，摇了摇头。她用胳膊背擦了擦眼眶发红的眼睛。"
show marie sad2 r with dissolve
Marie "那……要是你真的通过了期末考试，你会去哪儿？"
show mirabel neutral2 r with dissolve
Mirabel "我想去讷韦尔的一所师范学校读书。"
Marie "那、那你连米耶讷都不待了？！"
show mirabel sigh2 r with dissolve
Mirabel "大概是吧。这附近没有什么师范学校。这个村子太小了。"
show marie huh2 r with dissolve
Marie "可我以为你很喜欢米耶讷！"
show mirabel huh2 r with dissolve
Mirabel "我{i}确实{/i}很喜欢米耶讷。我最爱这里的乡间风光——也爱在这里结识的人们。"
show mirabel sad2 r with dissolve
Mirabel "我其实不想走，可要是我想让梦想成真，我就不得不走。"
Mirabel "我害怕去大城市。一想到要离开家，比当初走进这片林子还要让人害怕……"
show mirabel huh2 r with dissolve
Mirabel "但只要是不得不做的事，我就会去做，就像我走进这里来找你一样。"
Mirabel "我不跟你说话，本是想帮你，请相信我，可我现在知道我做错了。"
Mirabel "我不该一声不吭就对你置之不理。相反，我应该把情况跟你说清楚才是。"
Mirabel "我从没想过要让你觉得自己被抛弃、被嫌弃。那跟事实简直大相径庭。"
show mirabel shock2 r with dissolve
Mirabel "我在乎你，玛丽-诺埃尔。就算我们天各一方，我也会一直在乎你。"
Mirabel "你永远是我最特别的朋友……这一点永远不会变。我真的很爱你！"
show marie shock2 r with dissolve
Marie "米拉贝尔……米、米拉贝尔……！"

window hide dissolve
$ achievement.grant("a_touching_reunion")
scene cg16:
    subpixel True
    size (1920, 1080) crop (380, 270, 960, 540)
    linear 5.0 crop (0, 0, 1920, 1080)
show fog_fg:
    subpixel True
    size (1920, 1080) crop (380, 270, 960, 540)
    linear 5.0 crop (0, 0, 1920, 1080)
with dissolve
$ renpy.pause(1.0)
window show dissolve

"说罢，玛丽-诺埃尔迈开步子，冲向了米拉贝尔，缩短了两人之间的距离。"
"她张开双臂，朝那个年长的女孩跑去。"
"米拉贝尔顺从地蹲下，接受了玛丽-诺埃尔的拥抱；她揽住小女孩的后背，两人的额头碰在了一起。"
"玛丽-诺埃尔抽噎着。她的胸口起伏不定，眼眶里噙满泪水。她的眼睛红红的，但玛丽-诺埃尔并没有低头躲闪，也没有遮掩自己的脸。"
"相反，她望着米拉贝尔，下唇抿出坚定的神情，然后说道……"
Marie "我也爱你。"
Mirabel "嘿嘿嘿……那，谢谢你。"
Mirabel "那我们算是重新做回朋友了吗？"
Marie "我们从来就没不是朋友过。我们{i}永远{/i}是朋友。"
Mirabel "就算你生我的气也是吗？"
Marie "我其实并没有真的生你的气。我永远不会生你的气。你是我在这世上最好的朋友。"
Marie "你走之后我会非常想你，我也不想让你走，可是……"
"玛丽-诺埃尔深吸一口气，然后大义凛然地说道……"
Marie "如果你愿意，讷韦尔你尽可以去，既然那是你的梦想。我不想拖你的后腿。"
Marie "我受够自己这么自私了。我不想做个坏女孩。"
Marie "我想让你开心。"
Mirabel "嗯，也许你是有点自私，可我觉得那样很可爱！"
Marie "我、我真的很可爱……？"
Mirabel "没错。你是最可爱的，玛丽-诺埃尔。"
Mirabel "我不想离开你，可是……"
Marie "那我们就不谈这个了！好不好？"
Mirabel "好。那就不谈我离开的事——至少现在先不谈。"
Mirabel "现在，只要你平安无事，我就放心了。"
"米拉贝尔把玛丽-诺埃尔搂得更紧了些，脸上浮现一抹温柔的笑容。"
Mirabel "你什么都不用担心。你想哭就哭个够吧。"
Mirabel "我现在就在你身边……我永远、永远不会再不理你了。我保证。"

stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
play music "bgm/Energetic.ogg" fadein 1.0
play ambience "sfx/night_amb.ogg" fadein 1.0
play ambience2 "sfx/footsteps2.ogg" fadein 1.0
$ save_name = (__("{u}米拉贝尔篇{/u}{vspace=1}  12月8日{vspace=1}  重逢") )
show image "border" onlayer border
scene forest:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
show fog_bg:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
show fog_fg:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow
window show dissolve

"在森林中重逢之后，我、米拉贝尔和玛丽-诺埃尔踏上了返回学校的漫长路途。"
"进入这片森林还算容易，可要走出去却是个更棘手的难题。"
"我和米拉贝尔都知道自己想去哪里，却不知道该怎么走。"
"我们没有像汉泽尔与格莱特那样在身后丢下石子来标记来路，也没有丢下任何面包碎屑——不过，即使我们丢下了，我也怀疑那能有多大用处。"
"森林的地面崎岖不平，满是腐殖土。面包屑很容易就湮没在丛生的灌木杂草之中，而且它们也太小了，根本看不见。"
"我们只能转而依靠直觉来为我们引路。"
"我们在一片融洽的沉默中走了大约半个小时，玛丽-诺埃尔的手指与米拉贝尔的十指相扣。"
"一路上，除了四周树叶的沙沙声、风声，以及远处看不见的鸟儿的啼鸣之外，我们什么也没听见。"
"我们的脚步几乎是以完美的同步落在地面上，踩得树枝和落叶咔嚓作响。"
"走了一会儿，玛丽-诺埃尔终于开始疲倦了。尽管我和米拉贝尔已经走得很慢，她的腿还是太短，跟不上我们的步伐，而且她好像也没有多少体力。"
"独自一人走这么深进入森林，想必已经够累的了，可如今还要再走回去，对她的身体来说实在太过勉强。"

stop ambience2 fadeout 1.0
hide image "border" onlayer border
scene forest
show fog_bg
show marie sad r:
    xpos 0.70 xanchor 0.5
show mirabel neutral r:
    xzoom -1 xpos 0.30 xanchor 0.5
show fog_fg
with wipeleft_slow

Marie "喂，米拉贝尔……"
"玛丽-诺埃尔拽了拽米拉贝尔的手。她的蓝眼睛因疲惫而半睁半闭，说话也含含糊糊的，声音轻柔。"
Marie "我有点累了……"
show mirabel sad r with dissolve
Mirabel "我知道你累了，小鸭子，可我们还得往前走。我相信我们……就快到了……？"
"可米拉贝尔却停住了。她听起来一点也不信服，而这也有充分的理由。"
"我根本不知道我们身处何处。"
"我们可能离森林入口只有五分钟，也可能还有五个小时的路程。当所有树木看上去都一样时，根本无法分辨，而且也没有任何东西能标示出我们的进展。"
show marie scared r with dissolve
Marie "我不知道我还能不能继续走下去……"
"玛丽-诺埃尔停了下来。她弯下腰，隔着袜子揉着小腿。"
show marie sad r with dissolve
Marie "我的脚好痛。"
show mirabel shock r at bounce
Mirabel "可你要是不接着走，我们就走不出这片林子了！"
Marcel smile u "米拉贝尔。别担心。我知道该怎么做。"

window hide dissolve
scene cg17
show fog_fg:
    size (1920, 1080) crop (0, -120, 1920, 1080)
show fog_fg2:
    size (1920, 1080) crop (0, -60, 1920, 1080)
with wiperight_slow
$ renpy.pause(0.8)
window show dissolve

"趁米拉贝尔还没来得及问我有什么打算，玛丽-诺埃尔也还没来得及抗议，我便走近小女孩，把她抱进了怀里。"
Marie "喂、喂……！"
"玛丽-诺埃尔猛地睁大了眼睛。如我所料，她开始扭动起来。双腿乱蹬，还成功踢中了我腰侧几脚。"
Marie "你在干什么？哪有这样对待一位淑女的！放我下来！"
Marcel "我只是想帮你……"
"我从紧紧咬合的齿缝间嘶声低语。"
Marcel "你要是走不动，我想那我干脆背你好了。这样我们还能继续赶路，你的脚也不会那么痛。"
Marcel "你不觉得这主意不错吗？"

show cg17_2 behind fog_fg, fog_fg2 with dissolve
with dissolve

Marie "嗯……"
"玛丽-诺埃尔皱起了眉头。她似乎正在仔细掂量我的提议。"
Marie "唔、唔，我想总比走着强……"
"令我松了口气的是，玛丽-诺埃尔终于不再踢腿、也不乱挥双臂了。"
"相反，就像一个个倔强又面无表情的小娃娃，她的身体忽然变得软绵绵的。她在我怀里放松下来，脑袋倚在我的胸口，双臂交叠在膝上。"
"我对她的配合心存感激，不过玛丽-诺埃尔个子虽小，分量却出奇地沉。我的手臂在她重量下微微下坠，我只得抿紧嘴唇，强忍下没龇牙。"
"也许抱着另一个人（哪怕只是个小不点）并非明智之举，毕竟我前不久才掉进峡谷、脑袋撞上树干——但确实是我主动提出要帮她的。"
"若此刻把她放下来，未免显得不够绅士。"
"玛丽-诺埃尔本就够不信任我了。我不想再给她更多恨我的理由。"
Mirabel shock "你确定你没事吗，玛塞尔？"
Marcel "我、我没事。别担心我。"
Mirabel "可是你的脸色变得苍白了。我不想你弄伤自己……"
Marie "哼。我早该料到会这样。"
"玛丽-诺埃尔把鼻子翘得老高。"
Marie "像你这样的巴黎女孩，这辈子从没干过一天的实在活儿。你的手也太嫩了！我又不重，你居然就已经累成这样了！"
"至于最后那一点，我可没那么确定……"
Marie "你根本不可能一路把我背回学校！"
Mirabel "玛丽-诺埃尔！你该更感恩一点！玛塞尔正在帮你呢！"
Marcel "不，没事。她说得对。我并不怎么强壮，但我会尽力的……"
Marcel "我在乡下住得够久了。不该怕这点体力活儿。"
"米拉贝尔和我继续往前走。我把玛丽-诺埃尔抱在怀里。因为怕她掉到地上，我搂得紧紧的（也许有点太紧了），她却抱怨说我弄疼了她。"
"我相应松了松力道，调整了一下手臂的姿势。"
Marcel "你现在感觉怎么样？这样还好吗？"
Marie "感觉……应该还行吧。只要别再掐我就行了，好吗？"
Marcel "我会尽量不的。"
Marie "你的指甲为什么这么长啊？你住在乡下，那不是会弄脏吗！"
Marcel "留长指甲穿针引线更方便——再说，我母亲也喜欢我的指甲。让我把头发留长的也是她。"
Marie "你的妈妈？"
"我点了点头。"
Marcel "她当然住在巴黎。我已经好几个月没见到她了……"
Marie "哦。我明白了。"
Marie "你想她吗？"
Marcel "我很想她。很长很长一段时间里，她是我唯一的朋友。"
Marcel "自从搬到米耶纳，我就一直给她写信，她也会回信，但那终究跟真正地谈话不一样。"
Marcel "我想再见到她，可我不确定什么时候能见到。"
Marie "哦……"
"玛丽-诺埃尔会意地点了点头。"
Marie "我也很久很久没见到我的妈妈了。我也很想她……"
Marcel "那我们就有共同点了。"
Marie "也许吧……"
"玛丽-诺埃尔对这个主意似乎并不满意。她撅起嘴，把头更深地埋进我的胸口。"

play ambience2 "sfx/footsteps2.ogg" fadein 0.5
show image "border" onlayer border
scene forest:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
show fog_bg:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
show fog_fg:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

"我继续往前走。我们穿行在幽暗、仿佛无边无际的森林里，我的脚步声与米拉贝尔的交织在一起。"
"玛丽-诺埃尔绝非轻盈的负担，但我开始渐渐习惯她的重量了。"
"在搬到米延之前，我从没想过自己会迷失在一片幽深黑暗的森林里，怀里还抱着一个小女孩。"
"搬到乡下的这段日子，我经历了许多意想不到的事，但总的说来，我觉得自己很享受这段经历。"
"在米延，我觉得自己能成为想要成为的那个人。"
"我不知道自己是否想成为一个女孩，可我从来也不怎么喜欢当男孩。"
"我只想做我自己。"
"不过，行走之间，我忍不住琢磨：倘若米拉贝尔知道了全部真相，她还会接纳我吗？"
"向她敞开心扉的想法令我忐忑不安，但我现在已足够了解米拉贝尔，相信她一定会接纳我的。"
"米拉贝尔是个甜美温柔的姑娘，宽容得近乎过分。她唯一的苛刻似乎是留给自己的。"
"忽然之间，我心头涌起一股冲动，想把一切都告诉米拉贝尔。我想让她知晓关于我的全部。"
"那样的话，我们或许能变得比现在更加亲密。"
"我想，我会喜欢那样的。"
"在米延，没有人比我更信任米拉贝尔了；放眼整个米延，也不曾有。"
"正当我这么想着——玛丽-诺埃尔如猫儿般蜷在我怀里，脚下咯吱作响地踩踏着枯枝——米拉贝尔忽然倒吸了一口凉气。"
"她睁大眼睛，指向前方。"

stop ambience2 fadeout 1.0
hide image "border" onlayer border
scene forest
show fog_bg
show mirabel shock r:
    xzoom -1 xpos 0.5 xanchor 0.5
show fog_fg
with wipeleft_slow

Mirabel "看那边！我认得那些冬青树！"
Marcel shock u "你愿意……？"
"那些冬青树在我看来并不特别。若不是米拉贝尔，我根本不会知道那原来是冬青树。"
"然而，经她这么一提，我看到了那独特的叶子，边缘俱是尖利的锯齿，还有缀在枝丫间鲜红的浆果。"
"这些树看起来就像圣诞卡上画的那种。它们相当惹眼。"
show mirabel smile r with dissolve
Mirabel "这些树就在森林入口附近！我们快要出去了！"
show mirabel laugh r with dissolve
Mirabel "来啊！我们走吧！"

play sound "sfx/rustle.ogg"
show mirabel:
    ease 1.2 xpos 1.20

Marcel shock u "等、等等……！我跑不了那么快！"
"我努力跟上米拉贝尔的步伐，可怀里抱着这个玛丽-诺埃尔形状的累赘，实在有点难——我可没胆量当着她的面这么称呼她。"
"我觉得玛丽-诺埃尔不会喜欢这种说法。"
"我仍确信她恨我，但出乎我意料的是……"

scene cg17_2
show fog_fg:
    size (1920, 1080) crop (0, -120, 1920, 1080)
show fog_fg2:
    size (1920, 1080) crop (0, -60, 1920, 1080)
with wipeleft_slow

Marie "喂……玛塞尔……"
Marcel "嗯？"
"我停下脚步，落在米拉贝尔身后几步，端详着那个仍被抱在怀中的小女孩。"
"这一路上她大多都把脑袋抵在我胸前，说什么也不肯看我的脸。"
"她也从不开口与我搭话，除非是想责骂我搂得太紧。"
"可现在，她居然屈尊像对待平辈一样跟我说话了。"
"她那双蓝眼睛对上了我的目光。"
"她长长的睫毛颤了颤，（只是我的错觉吗……？）她的脸颊泛起一抹极淡的、樱草般的粉色。"
"一阵长久的沉默，然后……"
Marie "我只是想告诉你，嗯……谢谢你来找我。"
Marcel "嗯？"
"我呆呆地注视着玛丽-诺埃尔，哑口无言。"
"是我听错了吗？"
"那个倔强又傲慢的玛丽-诺埃尔，绝无可能屈尊道歉——尤其不会向我这个她势不两立的仇人！"
"为了稳妥起见，我该再问清楚一些……"
Marcel "你刚才说什么？"
Marie "别、别让我再说一遍，你这个笨蛋！"
Marie "我说了……嗯……"
Marie "你本不必来找我的，可你还是来了。你为我担心，甚至帮了我，尽管我对你那么无礼。"
Marie "那让我……有点开心……"
"她的脸颊愈发绯红了。"
Marie "我以为我讨厌你，可……也许我错了。"
Marie "我不该对你说那些刻薄的话。你不该被那样对待，所以……"
Marie "我为给你添麻烦而抱歉……以后我会尽量对你更好的。"
Marcel "啊……"
"有好一会儿，我竟说不出话来。除了结结巴巴的一句……之外，我实在不知该如何回应她这番温暖的话语。"
Marcel "谢、谢谢你，玛丽-诺埃尔！我保证不会让你失望！"
"我把她搂得更贴近自己的胸口，给了她一个拥抱，然而，就在我这么做的刹那……"
Marie "喂、喂！别会错意……！我才不是想跟你做朋友什么的！"
Marcel "可你刚才明明说不讨厌我！"
Marie "我是不讨厌你，可那不表示我喜欢你！你还差得远，根本比不上米拉贝尔！"
"唔，她说的或许也有道理……"
Marie "真是的。"
"玛丽-诺埃尔沉下脸来，把鼻子翘得老高。"
Marie "我会忍着你，也不会对你无礼，但仅此而已。你明白吗？"
Marcel "我明白了，夫人。"
"我竟会幻想玛丽-诺埃尔有朝一日能把我当作朋友，真是蠢透了。"
"是我太心急了些——可是，话又说回来……"
"哪怕是勉强的接纳，也总好过彻头彻尾的厌恶。"
"我想，我与玛丽-诺埃尔之间已经有了一些真正的进展。"
"也许假以时日，她会像关心米拉贝尔那样关心我。"
"毕竟，比这更离奇的事也曾发生过。"
"过去，我无论如何也想象不到，自己竟也会慢慢喜欢上自己…… {w}但遇见米拉贝尔，帮我扭转了这一点。"
"我不知道过去的自己是否曾比此刻更满意于自己的身份、自己所做的事。"

stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}米拉贝尔篇{/u}{vspace=1}  12月8日{vspace=1}  严厉的训斥") )
play music "bgm/Casual_Day.ogg" fadein 1.0
scene office:
    size (1920, 1080) crop (460, 40, 1440, 810)
show al frown2 at center
with wiperight_slow
window show dissolve

Bru "那么，你们几个今天到底为什么没去上课？"
"布吕吉埃夫人双臂交叉，打量着狼狈不堪的我们三人。她坐在书桌后面，眯起眼睛；米拉贝尔、玛丽-诺埃尔和我则正面对着她。"
"米拉贝尔和我都局促地扭动着，两人坐的都是一把不舒服的木椅。"

scene office
show marie pout:
    xzoom -1 xpos 0.35 xanchor 0.5
show mirabel shy:
    xzoom -1 xpos 0.20 xanchor 0.5
show al frown:
    xpos 0.75 xanchor 0.5
with wipeleft_slow

Mirabel "抱歉，夫人，可我们不得不进森林——"
show al shock with dissolve
Bru "森林！"
"布吕吉埃夫人的眉毛几乎挑到了前额中央，仿佛正拼命想逃离她的脸。"
show al annoyed with dissolve
Bru "是啊，我听说了。据说你们三个到院子的时候狼狈得很；头发乱蓬蓬的，脸颊和手指都被荆棘划伤了……"
Bru "真是难以置信。我实在想不通。你们为什么要那样把自己置于危险之中？"
show marie angry with dissolve
Marie "不、不是米拉贝尔的错！"
show al neutral with dissolve
Bru "那就请你给我说清楚。那是谁的错？"
Marie "是我的！都是我的错！"
"玛丽-诺埃尔一如既往地冲动，毫不退缩地瞪着布吕吉埃夫人。她身侧的双手攥成拳头，眼中燃烧着炽烈的热忱。"
"这小姑娘的倔强实在令人佩服，尤其考虑到我们如今的情况有多么岌岌可危。"
"只要布吕吉埃夫人愿意，她大可以当场将我们逐出校门。以我们三人公然违反校规的行径而言，我们确实罪有应得。"
"玛丽-诺埃尔虽然年幼，想必也明白这一点，但她那股炽热的正义感却丝毫未减。我敢打赌，为了米拉贝尔，她甚至愿意去与狮子搏斗。"
show marie shout with dissolve
Marie "是我跑进森林的！米拉贝尔是来找我的！她不该受罚！她什么错都没有！"
Marie "你要是想罚谁，就罚我吧！"
show al annoyed with dissolve
Bru "哦，我会的，相信我。我会用配得上你这样不守规矩的淘气丫头的方式来惩罚你……但首先，我得跟米拉贝尔和玛塞尔谈谈。"
show al frown with dissolve
Bru "你说米拉贝尔没有错，可我倒是想问……"
"布吕吉埃夫人瞥了米拉贝尔和我一眼。"
"我咽了咽口水，别过脸去，紧张得不敢迎上她的目光。"

show image "border" onlayer border
scene office:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

"我一边竭尽全力躲避布吕吉埃夫人那锐利的视线，一边却忍不住好奇地打量起四周来。"
"我以前从未进过布吕吉埃夫人的办公室，它与我巴黎母校的校长办公室截然不同。"
"布吕吉埃夫人的办公室狭小而朴素。既没有摆满炫耀性奖杯的柜子，墙上也没有悬挂任何已故老者的画像。"
"布吕吉埃夫人的书桌颇小，是木头做的。上面摆着几张照片，旁边还放着几叠纸张和几本皮面装帧的书。"
"办公室的墙边排满了书架，上面同样塞满了书。空气中弥漫着薄荷、信纸与墨水的气息。"
"窗台上摆着几盆盆栽，正努力汲取冬日渐剩不多的阳光。"
"这里几乎算得上令人安心——至少，如果布吕吉埃夫人不是像嗅到什么恶臭那样打量米拉贝尔和我的话。"
"我们俩这回必定惹上大麻烦了。"

hide image "border" onlayer border
scene office
show marie pout:
    xzoom -1 xpos 0.35 xanchor 0.5
show mirabel shy:
    xzoom -1 xpos 0.20 xanchor 0.5
show al annoyed:
    xpos 0.75 xanchor 0.5
with wipeleft_slow

Bru "不得不说，我对你们俩很惊讶，而且绝不是好的那种。"
Bru "玛塞尔，我一直以为你是个用功的学生；米拉贝尔，虽然你的成绩还差得远，但你以前从没逃过课。"
show al frown with dissolve
Bru "这种行为从克洛蒂娜那儿我还能料到，可你们俩！"
Bru "你们的行为实在令人震惊——这还不够，你们居然还要把一个幼儿班的小姑娘也拖进你们这场荒唐里！"
show marie shout with dissolve
Marie "他们{i}没有{/i}拽我！我已经说过了！是我自己跑进森林的！"
show al annoyed with dissolve
Bru "那你真是太蠢了，幸好你没受伤，也没有走丢。"
show marie sad with dissolve
Marie "嗯……"
"玛丽-诺埃尔微微一缩。"
Marie "所以米拉贝尔才会来找我。她担心我……"
show al frown with dissolve
Bru "也确实该担心。要是这么小的姑娘一个人跑到野外去，谁都会担心——可要是不跟老师打招呼就胡乱追着你跑？{i}那{/i}才叫鲁莽。"
Bru "你们三个能毫发无伤地回来，简直是奇迹。"
Mirabel "我……我确实想过找老师，可、可我太担心了……"
show mirabel sigh with dissolve
Mirabel "我怕再耽搁下去，就来不及了……"
show al annoyed with dissolve
Bru "所以你以为不如告诉老师，而是像个歇斯底里的女学生那样自己一头扎进危险里更好？"
show mirabel sad with dissolve
Mirabel "这个嘛，我{i}本来就{/i}是个女学生……"
Bru "是吗？像你这样的十六岁？我个人觉得你早过了那个阶段。"
show mirabel shockblush with dissolve
"米拉贝尔羞得双颊滚烫绯红。像她平日紧张时那样，她羞怯地开始拨弄其中一根辫子的末端。"
show al neutral with dissolve
Bru "米拉贝尔，你应该把心思放在考试上，而不是去当什么游侠骑士。"
Bru "你一知道玛丽-诺埃尔不见了，就该立刻来告诉我。我可以替你们安排一支搜寻队，而你本该留在教室里——那才是你该待的地方。"
show al sigh with dissolve
Bru "你的功课本来就够差了，别再给自己添绊子了。"
show al annoyed with dissolve
Bru "还有你，玛塞尔……"
"布吕吉埃夫人转向我，神情严厉而毫不留情。"
Bru "我还以为你比这更聪明些。"
Bru "记住：你能在我的学校读书，全靠我的恩惠。是我顶着重重阻碍，才让你在这里有了一个位置。我本指望你会更感激我的付出。"
show al frown with dissolve
Bru "我从未想过，哪怕一刻，你会纵容我珍爱的学生做出这种愚蠢的荒唐事！"
"我缩了一下。"
"布吕吉埃夫人说得对。我能进入这所学校就读，全靠她对我格外通融。"
"她为我备下了这所学校端庄的校服，给了我一间属于自己的房间，并且在过去几个月里一直以她自己的方式关照着我。"
"我亏欠她太多了。"
"若不是布吕吉埃夫人，我绝不会来到米延。"
"我会留在巴黎，被呛人的烟尘所环绕，在那里日渐枯萎消沉。"
"正因为我来到了乡下，我才能蜕变成一个崭新的人。"
"我交到了朋友，尝到了欢乐，生平头一次真正地享受起生活……嗯，是从未有过的滋味。"
"所有这一切机会，我都欠布吕吉埃夫人……然而，即便如此，我竟公然违背了她的意愿。"
"我逃了整天的课，还把自己置于危险之中。"
"她当时必定为我担心坏了——不只是担心她这所受人敬重的乡村学校的学生，更是担心她的侄子：她挚爱的妹妹莱奥妮唯一的儿子。"
"也许我本不该踏入那座林子。正如我姨母所说，我很可能会迷路，或是遭到野兽的袭击。"
"我的举动丝毫谈不上理智，可我仍然认为它们是必要的。"
"我做了自己认定不得不做的事，也毫无悔意。"
Marcel neutral u "抱歉，夫人，我只是想帮玛丽-诺埃尔。我的行为绝无恶意，真的。"
show al annoyed with dissolve
Bru "可万一你受伤了怎么办，玛塞尔？你为什么不停下来想想这一点？"
Marcel "我确实想过一下下，可玛丽-诺埃尔的安危似乎比我自己的更重要。"
show mirabel sad with dissolve
Mirabel "啊、啊，请您别怪玛塞尔！这多半是我的错，夫人！"
Mirabel "我一听说玛丽-诺埃尔跑掉了，就冲了出去。玛塞尔别无选择，只能跟着我。"
show mirabel sigh with dissolve
Mirabel "她是想确认我平安……"
show al frown with dissolve
Bru "那玛塞尔自己呢？要是真出了事，谁来护她周全？！"
show mirabel neutral with dissolve
Mirabel "呃，嗯……"
"米拉贝尔慌乱得手足无措。她的嘴像胡桃夹子似地张开又合拢，却一个字也说不出来。"
"布吕吉埃夫人眉间的皱纹更深了。"
Bru "这正是我要说的。"
show al sigh with dissolve
Bru "你们三个都做得很蠢。我对你们都很失望——但对你们俩，玛塞尔和米拉贝尔，尤为失望。"
show al annoyed with dissolve
Bru "像玛丽-诺埃尔这样的小孩开个愚蠢的玩笑是一回事，可两个大姑娘却被卷进去，那又是另一回事了。"
Marcel sad u "我……我、我抱歉……"
show al frown with dissolve
Bru "「抱歉」改变不了过去！也弥补不了你犯下的错！"
Bru "要是我接受了你的道歉，你就什么也学不到；而作为你们的校长，育人正是我的职责！"
show al annoyed with dissolve
Bru "我要让你们明白，无论情况如何，都不能无视校规，哪怕你们自认为理由多么正当。"
Bru "无论如何，我都得让你们受到教训……"
"布吕吉埃夫人怒视着我。"
"有几刻，我担心她正蓄势待发地准备对我施以惩罚。她真的要为了我的鲁莽而将我开除吗？"
"她看起来不只是生气：她简直怒不可遏。她下颌的肌肉绷得紧紧的，双眼半拢，宛如蛇目。"
"用不了多久，她就会下令让我离开她的学校了。"
"她会把我送回巴黎，而我将在母亲身边度过余生。"
"像我这样公然违抗校规、自作主张跑掉的顽劣学生，根本不配待在这样的乡村学校里。"
"我本就不该在这里就读。我并非像同窗们那样的女孩，可我也从未真正融入过男孩之中。"
"我不知道自己究竟属于哪里。"
"我曾以为自己属于这里，然而，我那愚蠢而不合时宜的勇敢，在那一瞬毁掉了一切。"

stop music fadeout 1.0

"我低下头，等待着那柄传说中的利刃落下，就在此时……"

play music "bgm/Confession.ogg" fadein 1.0
scene office:
    size (1920, 1080) crop (460, 40, 1440, 810)
show al neutral2 at center
with dissolve

Bru "哦，玛塞尔……"
Marcel shock u "啊……？"
"我眨了眨眼。"
"我缓缓抬起头来。"
"布吕吉埃夫人仍在注视着我，可她神色间所有生硬的线条都柔和了下来。"
"她看来不再愤怒了。事实上，情况恰恰相反。"
"她的眼眶似乎可疑地湿润了，只得用棉手帕的边角轻轻拭去。"
show al sad2 with dissolve
Bru "我得知你们三个不见了的时候，真是担心坏了！"
Bru "我怕你们可能惹上了什么麻烦，甚至受了重伤！我问你，那会对我们学校的名誉造成什么影响？"
show al shock2 with dissolve
Bru "那作为你们的校长，我又会显得多难堪？"
Bru "你们这样鲁莽，我可能会丢掉工作——还有你们的父母呢？！"
show al sad2 with dissolve
Bru "若明知自己没能尽到保护你们的职责，我又怎么有脸去见他们？"
Bru "我又该怎么跟莱奥妮交代……？！"
"我姨母说得对。我本该在追着米拉贝尔跑出去、一心想充当英雄之前，先替母亲着想。"
"若我闯下什么祸，她该如何是好？"
"父亲多年前便弃母亲而去，而她也与自己的家人断绝了来往。"
"多年来，我都是母亲唯一的依靠。我既是她仅剩的亲人，又是她最好的朋友。"
"与我分别令她痛彻心扉。她在火车站送我时潸然泪下，尽管她试图把脸埋进我的胸口掩藏。"
"母亲爱我，我也爱她，可我太沉溺于米拉贝尔和玛丽-诺埃尔之间，竟没能想到她。"
"我本该更体贴些的。"
"也许我确实该被开除，终究还是如此。"
"正因如此，我对接下来要从布吕吉埃夫人口中说出的话，已做好了十足的准备……"
show al annoyed2 with dissolve
Bru "我要给你们父母写一封措辞严厉的信，把发生的事告诉他们。"
"我已做好了准备，但是……"
show al sigh2 with dissolve
Bru "他们会酌情惩罚你们。"
Marcel shock u "啊……"
"我瞪大了眼睛，凝视着布吕吉埃夫人。"
Marcel huh u "这么说，您不会开除我们？"
show al neutral2 with dissolve
Bru "开除你们？"
"布吕吉埃夫人皱起眉头。"
Bru "我为什么要那么做？"
Marcel sad u "我、我本以为您会的！我们违反了校规。我们让自己陷入危险，还——"
show al annoyed2 with dissolve
Bru "是啊，你们{i}确实{/i}违反了校规，我也很生你们的气。你们谁都一样不争气，都不值得同情，可是{i}说真的！{/i}"
Bru "你们担心我一位年幼学生的安全，我为什么要为这个开除你们？"
show al neutral2 with dissolve
Bru "你们是想救玛丽-诺埃尔，对吗？"

scene office
show marie shock:
    xzoom -1 xpos 0.35 xanchor 0.5
show mirabel neutral:
    xzoom -1 xpos 0.20 xanchor 0.5
show al annoyed:
    xpos 0.75 xanchor 0.5
with dissolve

Marie "没错！米拉贝尔是想帮我！她是！"
show marie pout with dissolve
"玛丽-诺埃尔顿了顿，用眼角瞥了我一眼。"
Marie "我想玛塞尔也帮了一点点忙。"
show al neutral with dissolve
Bru "那我找不到惩罚你们的理由。给你们父母写封信——没错，{i}你们{/i}的父母也一样，玛丽-诺埃尔——应该就够了。"
Bru "他们可以随意训斥你们，但我这一边，就免了。"
show al smile with dissolve
Bru "我因你们的行为而恼火，但我也不能否认，我心里有一丝是佩服的。"
Bru "你们那样不顾一切地追着玛丽-诺埃尔冲进森林，不管那里潜藏着怎样的危险，真是太勇敢了。"
Bru "我刚才和玛丽-诺埃尔的老师谈过，她也同样感谢你们找到了她。她一直为了这位淘气的小姐担心得要命。"
show marie shout with dissolve
Marie "哼，她就是{i}应该{/i}感激！米拉贝尔真的很棒！她是我最好的朋友，为了我她什么都肯做！"
show al annoyed with dissolve
Bru "是这样的吗……？"
show mirabel ehe with dissolve
Mirabel "这、这个，嗯……我、我也不确定我算不算「勇敢」，可我真的很在乎玛丽-诺埃尔。"
show mirabel neutral with dissolve
Mirabel "我很喜欢小孩子——我自己就有个弟弟——我受不了想到他们难过、害怕或孤单。"
Mirabel "无论发生什么，我都想守在他们身边。这是世界上我最想要的事。"
Bru "你说是「什么都」……？"
Mirabel "是、是的……"
show al sigh with dissolve
Bru "嗯，让我想想……"
"布吕吉埃夫人一手托着下巴，陷入沉吟。"
show al neutral with dissolve
Bru "我一直以为你想当老师的梦想不过是说说而已，可你的品性或许当真适合这个职业。"
show al smile with dissolve
Bru "也许我可以给你一个提议。"
show mirabel shock with dissolve
Mirabel "一、一个提议……？"
"姨母点了点头。"
Bru "贝尔奥姆小姐有了个有趣的想法。她似乎对此相当热衷。"
Bru "她想问问你，倘若你没有别的事忙，是否愿意偶尔帮她照料幼儿班的孩子？"
Bru "这会给你一些宝贵的教学经验，也能让你离实现梦想更近一步。"
show marie shock at bounce
Marie "欸？！"
"玛丽-诺埃尔的耳朵微微竖起。她在椅子上稍稍坐直了些，眼睛睁得圆圆的。"
show marie huh with dissolve
Marie "米拉贝尔要当我的新老师了吗？！是真的吗，是真的吗？！"
show al neutral with dissolve
Bru "如果她愿意的话，她将成为你们的助教老师。"
Bru "米拉贝尔，你意下如何？"
show marie smile with dissolve
Marie "米拉贝尔！！！"
"玛丽-诺埃尔握住米拉贝尔的手。她纤细的手指缠绕上米拉贝尔的指间，仰头望向她心目中偶像的眼睛，眼神里毫不掩饰着崇拜。"
"玛丽-诺埃尔睁着又大又圆的蓝眼睛，用甜甜的、咬字不清的腔调开口说……"
Marie "你来当我的老师好不好？我真的好喜欢这样！"
show mirabel scared with dissolve
Mirabel "我也很愿意，但是……这、这样真的可以吗？"
show al smile with dissolve
Bru "我看不出有什么问题。贝尔奥姆小姐一直很喜欢你，玛丽-诺埃尔更是迷上你了。"
show marie laugh with dissolve
Marie "我不懂那个大词是什么意思，但我超喜欢米拉贝尔！她是我全世界最好的朋友！"
Bru "你看？"
"布吕吉埃夫人露出微笑。"
Bru "我相信，如果你成为她的老师，那个小姑娘会非常高兴。"
Bru "米拉贝尔，我知道你近来有多用功。尽管你今天行事有些冒失，我想你也该得到某种回报。"
show mirabel shy with dissolve
Mirabel "那、那……如果您真的不介意的话……唔……"
show mirabel laugh with dissolve
Mirabel "我、我很愿意去贝尔奥姆小姐的班里帮忙！"
show marie smile with dissolve
Marie "太好啦！"
"玛丽-诺埃尔兴高采烈地拍着手。"
Marie "那意味着我每天都能见到米拉贝尔了！我们可以一直做最好的朋友！"
show mirabel neutral with dissolve
Mirabel "喂……"
"米拉贝尔朝着她这位小被监护人摇了摇手指，以示责备。"
Mirabel "玛丽-诺埃尔，如果我要做你的老师，我就得使唤你、给你下指令。在教室里，我不能再像朋友那样待你了。"
show marie laugh with dissolve
Marie "可我还是能常见到你，见好多好多回！那一定很有趣！"
show mirabel sigh with dissolve
Mirabel "当我逼你练字母的时候，可就不一定有趣了。你真是个固执的姑娘……"
show mirabel neutral with dissolve
Mirabel "而且我仍会推着你与别的同学说话。你总不能一直黏着我。那对你并不好。你明白吗？"
show marie pout with dissolve
Marie "哼……"
"玛丽-诺埃尔撅起了嘴。"
Marie "你已经像个老师的样子了！"
Mirabel "唔，我将来确实想当老师。我不能偏心谁。那样不对。"
show marie shout with dissolve
Marie "什么？那不公平！"
show mirabel sigh with dissolve
Mirabel "人生就是如此。"
show mirabel smile with dissolve
"不过，米拉贝尔或许是招架不住玛丽-诺埃尔那甜软可爱的、咬字不清的声音，到底还是在女孩的头顶上轻轻揉了揉。"
Bru "哈。说不定有一天，你真能成为一位好老师！"
"布吕吉埃夫人笑了起来。"
show al neutral with dissolve
Bru "我心里还有一个想法。"
Bru "倘若你未能通过期末考试、进不了师范学院，你也可以留在这里任教——不是当助教，而是一个更固定的职位。"
Bru "贝尔奥姆小姐今夏就要嫁人，她打算辞去工作，多陪陪她的丈夫。"
Bru "我迟早得为她物色一位接替者，而我认为你或许能胜任。"
Bru "你当然不必现在答复，但请务必好好考虑。"
show al smile with dissolve
"布吕吉埃夫人朝米拉贝尔露出一个温暖的微笑。"
Bru "拉克小姐，能与你共事，我会非常乐意。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
play music "bgm/Friendship.ogg" fadein 1.0
play ambience "sfx/night_amb.ogg" fadein 1.0
$ save_name = (__("{u}米拉贝尔篇{/u}{vspace=1}  12月8日{vspace=1}  冰释前嫌") )
scene sky_n with wiperight_slow
window show dissolve

"与布吕吉埃夫人谈完之后，米拉贝尔和我一同退回到我的卧室。"
"才不过六点左右，天色却已经暗了下来。阴影在我的书桌下和盥洗盆周围聚成一片，不过米拉贝尔和我在一起，倒都觉得很满足。"
"至于玛丽-诺埃尔，她去为让老师担心而道了歉，随后便回到了宿舍。"
"我知道玛丽-诺埃尔和同龄的姑娘们合不来，她自己也不怎么在意；不过她今天的这段冒险，应该能让她和同学们有些话题可聊了。"
"运气好的话，她或许能向她们敞开心扉，甚至交上几个朋友。"
"说起今天的冒险，我不禁好奇，自己班上的姑娘们是否已经听说了树林里发生的事。"
"诺艾米和克洛蒂娜知道米拉贝尔的英勇事迹吗？"
"到了明天早上，她们是会继续取笑她，还是也许会对她生出一种崭新的敬佩呢？"
"很少有姑娘——即便是那些在乡下土生土长的——愿意像米拉贝尔那样，深入到树林那么远的地方去。即便是在白天，那也太危险了。"
"然而米拉贝尔却出乎了所有人的意料。尽管内心畏惧，她仍毫不犹豫地寻去救玛丽-诺埃尔。"
"就算同学们会取笑米拉贝尔，至少也应当为她的勇敢而敬重她。"
"米拉贝尔做了她们从来不敢做的事，而且她这么做，仅仅是为了玛丽-诺埃尔。"
"我觉得这很了不起。"
"尽管训斥了她一番，布吕吉埃夫人想必也认为这很了不起，因为她向米拉贝尔提出了一个相当慷慨的提议。"
"我不知道她对这一切作何感想？"
"我想，要弄清楚答案，只有一个办法。"

stop ambience fadeout 1.0
play ambience2 "sfx/night_amb2.ogg" fadein 1.0
scene marcel_room_n:
    size (1920, 1080) crop (140, 40, 1440, 810)
show mirabel neutral2 n:
    xzoom -1 xpos 0.5 xanchor 0.5
with wipeleft_slow

Marcel smile u "米拉贝尔，你怎么想？你愿意像布吕吉埃夫人期望的那样，留在这所学校任教吗？"
show mirabel shy2 n with dissolve
Mirabel "我……还不确定……"
"我以为米拉贝尔会为这个前景而兴奋，可她却再一次出乎了我的意料。她的声音轻柔而迟疑，低着头望着膝盖。"
"她的手指交叠在一起，搁在膝头。"
show mirabel sigh2 n with dissolve
"她叹了口气。"
Mirabel "我当然愿意。布吕吉埃夫人如此器重我，我真的很高兴。我一直以为她把我当成无可救药的笨蛋……"
show mirabel sad2 n with dissolve
Mirabel "但我不确定自己配得上这个机会。"
Marcel huh u "你当然配得上！你可是为了救玛丽-诺埃尔才闯进森林的！"
show mirabel huh2 n with dissolve
Mirabel "可那不单是我一个人的功劳。玛塞尔，你也陪我一起去了，最后找到玛丽-诺埃尔的还是你。"
Marcel neutral u "只是碰巧。"
show mirabel sad2 n with dissolve
Mirabel "是碰巧，没错……但若不是有你，我不知道自己敢不敢深入森林那么远。"
show mirabel sigh2 n with dissolve
Mirabel "我太害怕了，每一点声响都让我的心仿佛要炸开。"
show mirabel scared2 n with dissolve
Mirabel "如果你没陪我一起来，我想我走进森林不到五步就会掉头回去了。"
Marcel smile u "你现在是这么说，可我不认为你真会那样。你当初冲出去时可是满怀决心。"
"我朝她温柔地笑了笑。"
Marcel "倒是我一路赶着才追上你。"
show mirabel sad2 n with dissolve
Mirabel "你真的不必追来的。我那时太傻了……"
show mirabel sigh2 n with dissolve
"米拉贝尔叹了口气。她用右手的食指，在我那单薄而又简陋的鸭绒被上漫无目的地画着图案。"
Mirabel "布吕吉埃夫人说得对。我本该先跟老师说的。我绝不该独自莽撞地冲出去。我把你和玛丽-诺埃尔都置于了险境。"
show mirabel sad2 n with dissolve
Mirabel "当你摔进那道峡谷、撞到头的时候，我真的很担心你会受伤。"
Marcel "只是磕了一下。我没事。"
Mirabel "你现在没事了，可是……我不知道……"
show mirabel scared2 n with dissolve
Mirabel "我那时怕极了……"
"米拉贝尔吸了吸鼻子。"
Mirabel "失去玛丽-诺埃尔已经够糟了，可要是你因为我的缘故受了伤，我真不知自己会怎么办。"
show mirabel sigh2 n with dissolve
Mirabel "我、我会愧疚死的！"
Marcel "你没有什么可愧疚的。"
"我把米拉贝尔的手握进我掌中，让我们的掌心紧紧相贴。"
Marcel neutral u "我已经说过了，我陪你进森林，是因为我自己想去。"
Marcel smile u "因为我是你的朋友。"
show mirabel shock2 n with dissolve
Mirabel "正因为我们是朋友，我才更该替人着想才对！"
show mirabel sad2 n with dissolve
Mirabel "玛塞尔，从没有人像你对我这么好；至少同辈之中从没有人这样待我。"
show mirabel sigh2 n with dissolve
Mirabel "我非常珍视你的友谊，也高兴你总是支持我，可是……"
"米拉贝尔又吸了吸鼻子。她的肩膀微微颤抖。"
show mirabel sad2 n with dissolve
Mirabel "你因为我受了伤——也因为我惹上了麻烦。我真是太不负责任了！"
Mirabel "如果我不能像个大人一样行事，就永远当不了一名合格的老师。"
show mirabel sigh2 n with dissolve
Mirabel "天哪，我都快十七岁了。我再也不是小孩子了……"
Mirabel "我该长大了。"
Marcel huh u "我觉得你不必长大。"
show mirabel huh2 n with dissolve
Mirabel "你、你不觉得吗？"
Marcel "不。我觉得你这样就很好，只要……"
Mirabel "只要什么？"
"米拉贝尔不安地望了我好一会儿。黑暗中，她的脸苍白得如同一张白纸。"
show mirabel sad2 n with dissolve
Mirabel "我是不是做错了什么，让你不开心了……？"
Marcel shock u "米拉贝尔，你做什么都不会让我不高兴，除了你总是不够自信！这我已经跟你说过了！"
Marcel "布吕吉埃夫人在办公室里称赞你了！她也许是责骂过你，可她也为你的勇敢折服！你就不能接受她的夸奖吗？"
Marcel sad u "你难道不肯接受她给你的这个机会吗？"
show mirabel neutral2 n with dissolve
Mirabel "可是，没能通过考试就在这所学校教书……"
show mirabel sad2 n with dissolve
Mirabel "总觉得这样不公平。"
Marcel neutral u "话说回来，考试究竟有何价值？除了证明一个人能记住并复述一堆事实与数字，它们还能证明什么？"
Marcel "考试只说明你擅长考试！它们证明不了一个人有多善良、多有同情心。"
Marcel shock u "米拉贝尔，即便你不是学业上最有天分的人，你依然具备这一切。我相信你一定会成为一位了不起的老师！"
Marcel "这不正是你的梦想吗？"
show mirabel huh2 n with dissolve
Mirabel "这、这是我的梦想，没错。我一直在为它努力，可是……"
show mirabel shy2 n with dissolve
Mirabel "我心想，也许我内心深处从没真正相信它会实现……"
Marcel frown u "所以你要让这个机会就此溜走吗？"
show mirabel shock2 n at bounce
Mirabel "不，不会的！我还不至于傻到那个地步！"
show mirabel sad2 n with dissolve
Mirabel "如果布吕吉埃夫人真的放心让我这样的女孩在她宝贵的学校里教书，那么……"
Marcel smile u "不只是布吕吉埃夫人。我相信低年级班的全体女孩都会喜欢你的。"
show mirabel huh2 n with dissolve
Mirabel "你、你真的这么想吗？"
Marcel "我确定无疑。她们怎么可能不喜欢你呢？你真的很棒。"
show mirabel ehe2 n with dissolve
Mirabel "很、很棒？这我可说不好……"
"米拉贝尔笑着摇了摇头。至少她听了我的夸奖，看上去更多是觉得好笑，而不是难为情。"
show mirabel shy2 n with dissolve
Mirabel "不过，如果你觉得我能成为一位好老师，那么也许我会接受布吕吉埃夫人的提议。"
show mirabel neutral2 n with dissolve
Mirabel "很长一段时间里，我以为自己想当老师的唯一正道，就是通过考试、进师范学院。"
Mirabel "那曾是我的目标……不过，说实话，我不太喜欢大城市。"
show mirabel sigh2 n with dissolve
Mirabel "我一直盼着能留在米耶讷教书，可我告诉自己那是不可能的。"
show mirabel neutral2 n with dissolve
Mirabel "如果我有机会留在这里、实现我的目标，那不妨就留下吧。"
Marcel neutral u "那么，这是否意味着你不再需要和我一起学习了？"
show mirabel huh2 n with dissolve
Mirabel "您这话是什么意思？"
"米拉贝尔困惑地朝我眨了眨眼。"
Mirabel "我为什么要停止和你一起学习？"
Marcel ehe u "唔……既然布吕吉埃夫人已经答应，不论你能否通过考试都在这所学校任用你，你就不必再为它们苦练了。"
Marcel sigh u "我们也不必再那么频繁地见面了……"
"我低下头。我能感觉到喉头开始涌起一股哽意。"
"如果米拉贝尔不必把那么多时间都扑在功课上，她也许会轻松些；可我想到自己大概会想念我们一起温习的时光。"
"我很享受和米拉贝尔相处的时光，但我知道自己不该贪心。"
"我不想占用她太多时间——但令我松了口气的是……"
show mirabel shock2 n at bounce
Mirabel "不，不要！"
"米拉贝尔用力地摇了摇头。"
Mirabel "我不会停止和你一起学习的，玛塞尔！"
Marcel shock u "你不会……？"
Mirabel "不会！"
show mirabel neutral2 n with dissolve
Mirabel "我或许不必通过考试，但我还是想通过。它们给了我第二次机会，所以我应当全力以赴。"
Mirabel "我想通过它们，让所有嘲笑、捉弄过我的人都看走眼。我要让他们看看，像我这样笨拙迟钝的女孩也能进步。"
show mirabel huh2 n with dissolve
Mirabel "我{i}一定{/i}会进步。"
show mirabel neutral2 n with dissolve
Mirabel "如果我要成为一名合格的老师，至少得掌握写字和算术的基础。"
Mirabel "仅仅对我的学生好是不够的。我必须足够聪慧，能恰当地教导他们，好让他们也能去争取光明的未来。"
Mirabel "如果我不坚持尽力，那对我未来的学生可不公平。"
Marcel shock u "哇。你比我想象的还要坚定！我从没听你对任何事如此充满热情！"
show mirabel ehe2 n with dissolve
Mirabel "嘿嘿……"
"米拉贝尔尴尬地咯咯一笑，随即开始摆弄起自己一根辫子的末端。"
Mirabel "我、我这真的是个挺傻的梦想，犯不着这么起劲。这世上的老师并不少。"
"我不禁回想起在巴黎的日子——尽管我身陷那样的困境，老师却要么责骂我，要么对我视而不见。"
"我皱起眉头。"
Marcel frown u "老师或许并不少，但好老师依然稀缺。"
Marcel "米拉贝尔，我相信你将来一定会成为一位出色的老师。"
show mirabel shy2 n with dissolve
Mirabel "不见得。我肯定比不上你在巴黎时的那些老师……"
Marcel smile u "不，你确实不像他们。你比他们好得多。"
show mirabel shock2 n with dissolve
Mirabel "我、我可不敢这么想……！"
show mirabel smile2 n with dissolve
"不过，米拉贝尔尽管仍然震惊，却很快又露出了微笑。"
Mirabel "但谢谢你安慰我，玛塞尔。每当我对自己没有把握的时候，你总是这样。"
show mirabel shy2 n with dissolve
Mirabel "说实话……"
"米拉贝尔低下头，脸颊泛起淡淡的粉色。"
Mirabel "这也是我想继续和你一起学习的另一个原因。"
Mirabel "我喜欢和你在一起，嗯……"
show mirabel huh2 n with dissolve
"她咽了咽口水。"
Mirabel "而且，我也想继续和你在一起，如果你不太介意的话。"
show mirabel neutral2 n with dissolve
Mirabel "我不想给你添麻烦，但是——"
Marcel shock u "你一点也不麻烦！恰恰相反！我也喜欢和你待在一起！"
show mirabel shock2 n with dissolve
Mirabel "你、你也喜欢……？"

stop music fadeout 1.0

Marcel "是呀！毕竟……"
"我朝米拉贝尔稍稍凑近了些，声音压成了耳语。"

play music "bgm/Mirabel.ogg" fadein 1.0

Marcel "我爱你。"
"我从未对哪个姑娘说过我爱她。"
"说实话，除了母亲之外，我从未和别的姑娘说过话（她与其说是女孩，不如说是一位夫人）；自从来到米耶讷遇到米拉贝尔之前，一次都没有。"
"在这些年里，我从未想过自己有朝一日会对一个异性说出那三个甜蜜的字……也从未想过，自己竟能如此轻易地说出口。"
"让我震惊的，并不是自己这番坦白的胆大，而是那三个字竟如此自然地脱口而出。"
"我的脸颊甚至都没有泛红，也没有结舌。相反，我平静地注视着米拉贝尔，手指仍与她交缠在一起。"
"原来我爱她。"
"嗯，我当然爱她。这似乎再自然不过了。"
"起初，我出于怜悯和米拉贝尔结交，因为她那么痛苦地让我想起过去的自己——那个我一直想要摆脱的自我。"
"她害羞、笨拙、容易紧张，自尊心很低，还常常被同学们欺负。"
"我想做她的朋友，因为我想帮助她。"
"我或许比任何人都更能切身体会到，孤身一人是多么痛苦。"
"然而随着时间的推移，我对米拉贝尔的感情开始发生变化。我钦佩她的坚定，也发现了一个我从未想象过、这样一个安静的女孩身上竟能拥有的了不起的勇气。"
"她与我过去的样子完全不同。"
"她意志坚定，勤奋努力，也从不会放弃自己的梦想。"
"我竟曾以为米拉贝尔和我一样，真是太傻了。"
"她和我一点都不像。"
"她比过去的我，要美好得多、得多。"
Marcel smile u "我{i}确实{/i}很爱你，你知道吗。"
show mirabel shy2 n with dissolve
Mirabel "啊、啊，玛塞尔……"
"米拉贝尔的脸颊泛起了红晕。我不确定那是出于羞涩，还是欣喜。也许两者兼而有之？"
show mirabel ehe2 n with dissolve
Mirabel "你真是善良。"
show mirabel huh2 n with dissolve
Mirabel "我不知道自己配不配得上你的爱，但是——"
Marcel huh u "你{i}确实{/i}配得上，而且还远不止如此。你配得上我能给你的全部。"
show mirabel scared2 n with dissolve
Mirabel "可、可我长得这么普通，人也平平无奇。我身上一点特别之处都没有……"
Marcel "我觉得你很特别。"
Mirabel "我、我也觉得你很特别，可是我……啊……"
show mirabel shy2 n with dissolve
Mirabel "每次和你待在一起，玛塞尔，我的心就怦怦直跳，脸颊发烫，整个人都不知道该怎么办才好！"
Mirabel "就好像我得了某种脑热病似的，可我并没有生病。"
Mirabel "我想，这或许就是爱吧，可我不确定。我从未谈过恋爱，尤、尤其是和一个女人……"
show mirabel sigh2 n with dissolve
Mirabel "不过，无论如何，我从没想过你会回应我的心意。"
Marcel neutral u "可我的心意是真的。"
Marcel shy u "和你在一起时，我简直不像自己了。"
Marcel "我原以为，朋友之间大概就是这样的感觉……可我想，我对你的感情，恐怕要比友情更深。"
show mirabel huh2 n with dissolve
Mirabel "啊，玛塞尔，听你这么说我真的很安心，可是……"
"米拉贝尔脉脉含愁地望着我。她的睫毛显得很长，圆润的脸颊几乎宛如天鹅绒般柔软。"
show mirabel sad2 n with dissolve
Mirabel "我们两个都是女孩——而我还是如此平凡、如此不起眼的那一个！"
Mirabel "我、我不反对那些违背世俗的人，可、可是，要和一个像我这样的人一起去违背世俗……？"
show mirabel shy2 n with dissolve
Mirabel "我真的值得吗？"
Marcel frown u "你对我而言，值得一切。"
show mirabel huh2 n with dissolve
Mirabel "那、那么，如果你真的不嫌弃像我这样平凡的女孩……"

scene marcel_room_n blur:
    size (1920, 1080) crop (280, 40, 1152, 648)
show mirabel shy3 n:
    xzoom -1 xpos 0.50 xanchor 0.5
with dissolve

"米拉贝尔朝我靠得更近了。就在我们的嘴唇即将相触的刹那……"
Marcel huh u "有些事，我或许该告诉你了……"
show mirabel neutral3 n with dissolve
Mirabel "哦？"

scene marcel_room_n:
    size (1920, 1080) crop (140, 40, 1440, 810)
show mirabel shy2 n:
    xzoom -1 xpos 0.5 xanchor 0.5
with dissolve

"米拉贝尔退了开来。她的眼睛泛着异样的湿润，宛如清晨时分雏菊花瓣潮湿的背面。"
"那不是眼泪吧……？"
"我希望不是。"
"我想把米拉贝尔拥进怀里，拭去她那些即将夺眶而出的泪水；但在我把真相告诉她之前，我不愿意这么做。"
"我想让她知道我的真实身份……"
"不过说实话，在过去的几个月里，我的“真实身份”已经变得如此模糊难辨，连我自己都不确定它究竟是什么了。"
show mirabel huh2 n with dissolve
Mirabel "怎么了，玛塞尔？你怎么突然这么安静……？"
"我紧闭双眼，深吸了一口气。"
"我不认为米拉贝尔会因此与我反目，但把秘密说出来，终究还是让人不安。"
Marcel sigh u "其实……"
Marcel neutral u "我不是女孩，我的名字也不是玛塞尔·雷诺。"
Marcel "我的真名是马塞尔·德·圣雷米。我是一个演员的私生子，从前在巴黎的一所男校读书。"
Marcel sad u "我在那所学校……被欺负得很惨。他们总说我不像个男孩。"
Marcel "许多同学都怀疑我到底是不是个男孩——连我自己也这样怀疑过。"
Marcel "有一次，我甚至被人从楼梯上推了下去。没有摔断骨头，可是很疼。"
"我不由得瑟缩了一下。"
"仅仅是回想起这些记忆，就让人痛苦不已。"
"身为马塞尔·德·圣雷米、在巴黎被同龄人嘲笑的日子，仿佛已经是很久很久以前的事了；可其实，那并没有过去多久。"
"那不过才四个月，甚至还不到半年。"
"不过，自那以后，我身边的环境已经变了很多；我想，我也随着一并改变了。"
"我比以前勇敢了；而如今既然和米拉贝尔成了朋友，我也更明白失去她这个念头有多么可怕。"
"尽管如此，我依旧是马塞尔；仍是那个一贯害羞、说话轻声细语的人。"
"我想，这一点永远不会改变，不论我穿成男孩还是女孩。"
"我不会改变……我望着米拉贝尔的眼睛，恳求她明白这一点。"
Marcel neutral u "为了逃避欺负，我搬到了米延。是布吕吉埃夫人——也就是我的阿尔贝汀姨妈——建议我打扮成女孩，去她执教的学校读书。"
Marcel "她的想法是，既然我作为男孩找不到幸福，那我至少可以试着作为一个女孩，找到属于自己的位置。"
Marcel "至于我自己，我也不确定自己更喜欢做女孩还是男孩……但我向你保证，我从没骗过你。至少不是有意的。"
Marcel sigh u "无论穿不穿裙子，我都是马塞尔。"
Marcel "我永远都是马塞尔……"
Marcel sad u "我只希望你不会觉得我背叛了你。"
show mirabel shock2 n with dissolve
Mirabel "男孩……？"
"米拉贝尔坐在那里，眨着眼睛。"
"她看起来并没有因我的坦白而太过震惊，不过这或许是因为她还没有完全回过神来。"
"几秒钟过去，然后……"
show mirabel neutral2 n with dissolve
Mirabel "你真的是个男孩？"
Marcel shy u "嗯，我是作为男孩出生的。我自己也从没觉得自己多像个男孩，可我也说不准自己是不是女孩。"
show mirabel huh2 n with dissolve
Mirabel "这么说，你两者都不算？"
Marcel sigh u "我不知道。我想，我只是马塞尔。"
show mirabel neutral2 n with dissolve
Mirabel "马塞尔……"
"米拉贝尔试探地念出我的名字，脸上带着一丝浅浅的困惑，不过这个名字和我用女孩身份时所用的几乎一模一样。"
"念出声来并没有任何不同；只是写在纸上看得出差别罢了。"
"也许这正是米拉贝尔这么快就接受了这件事的原因。"
show mirabel smile2 n with dissolve
"她笑了，然后……"
show mirabel laugh2 n with dissolve
Mirabel "对我来说，你永远都是马塞尔，不管你是男孩还是女孩，还是两者皆是，又或者都不是。我都会一样喜欢你。这什么都改变不了！"
Marcel shy u "这么说，你不生我的气了？"
show mirabel huh2 n with dissolve
Mirabel "当然不生呀！我为什么要生你的气？"
Marcel "我原以为这会很让人困惑。这段时间我一直让你以为我是个女孩，可实际上我是别的东西。"
show mirabel smile2 n with dissolve
Mirabel "唔，你这么说来，是有点复杂……我不太擅长思考那些难懂的事，但我觉得，这件事不必那么难懂。"
show mirabel laugh2 n with dissolve
Mirabel "就像你说的，你就只是马塞尔！"
Marcel huh u "只是马塞尔……？"
show mirabel smile2 n with dissolve
Mirabel "没错！你就只是马塞尔，而我喜欢你，和五分钟前一模一样。"
Mirabel "我想，我大概永远不会停止喜欢你。"
Marcel shock u "你、你不会……？"
show mirabel laugh2 n with dissolve
Mirabel "可不是！"
Marcel "可是，你怎么知道……？"
show mirabel smile2 n with dissolve
Mirabel "嗯……就跟你说的那样。"

scene marcel_room_n blur:
    size (1920, 1080) crop (280, 40, 1152, 648)
show mirabel smile3 n:
    xzoom -1 xpos 0.50 xanchor 0.5
with dissolve

"米拉贝尔朝我稍稍靠拢了些，脸上挂着一丝浅浅的微笑。"
Mirabel "我想，我爱你。"
"就这样……"

window hide dissolve
scene cg18 with wiperight_slow
$ achievement.grant("mirabel")
$ renpy.pause(1.0)
window show dissolve

Marcel "啊……"
"……米拉贝尔的唇贴上了我的唇，落下一个轻柔而温存的吻。"
"说来真有意思。"
"我一直想象着，会是我先吻米拉贝尔；可她又找到了一个方式让我吃惊。"
"她远比我一开始所认为的更有主见。她也更大胆、更坚强、更明亮……"
"无论未来带来什么，只要能和她在一起，我都将感到荣幸。"
"我真的爱她。"

$ persistent.end = "on"
stop ambience2 fadeout 1.0
stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with slow_dissolve

jump mira_credits

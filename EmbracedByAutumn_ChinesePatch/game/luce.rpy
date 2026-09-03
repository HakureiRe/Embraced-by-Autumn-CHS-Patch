label Luce_route:

    stop music fadeout 1.0
    scene black with wiperight_slow
    $ renpy.pause(0.8)
    play music "bgm/Casual_Day.ogg" fadein 1.0
    $ save_name = (__("{u}露丝篇{/u}{vspace=1}  9月16日{vspace=1}  这就是人生") )
    scene woodshed:
        size (1920, 1080) crop (240, 40, 1440, 810)
    show luce frown2 w at center
    with wiperight_slow
    window show dissolve

    Luce "真是麻烦……"
show luce sigh2 w with dissolve
"露丝叹了口气。"
"她的声音那么轻，仿佛开口说话这件事本身就令她不安。"
"我想这是我的错。毕竟，是我把她拽到柴房来的。我本可以让她留在教室里，我相信她更愿意那样，我实在怪不得她。"

show image "border" onlayer border
scene woodshed:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

"柴房是一座与学校其他部分相隔绝的小屋子。我和露丝足足走了五分钟才到这里。"
"若不是露丝带路，我恐怕会在来的路上迷失在这片树林里，再也找不着方向。"
"柴房如此狭小，屋顶又那么低矮，我根本站不直身子。即便露丝不在我身边，这里也挤得够呛。"
"幸好，露丝自己身材娇小，占不了太多地方。"
"正如这屋子名字所暗示的那样，里面装满了木柴（{i}那可真叫人意外{/i}）。劈好的柴火一层叠着一层，权当是货架。"
"沿墙堆放的巨大柴垛看上去相当危险。我怕一个失足，或是一阵地面的颤动，就会让最顶端的木柴脱堆滚落，然后砸到我们。"
"我们得小心些才行。"
"木屑那股浓郁而带土腥味的香气弥漫在空气中。味道太过浓烈，熏得我眼睛都泛泪了。"
"我不禁想，柴房之所以离校舍这么远，是不是就是因为这个……？"
"一定是因为这个，也或许是因为：一旦这座小屋着了火，它就会卷着周围的建筑，一同葬身于赤红的烈焰之中。"
"尽管我知道露丝并不想来这里，尽管我为自己单独挑中她而感到愧疚，但我不后悔自己选定了她作同伴。我本以为，这或许是个了解她的好机会。"
"早餐时我只与露丝简短地交谈了几句，她看上去相当和善——只是颇为神秘。"
"我想和她多聊几句……{w}而且，我也有件事想问她。"

hide image "border" onlayer border
scene woodshed:
    size (1920, 1080) crop (240, 40, 1440, 810)
show luce frown2 w at center
with wipeleft_slow

Marcel neutral u "杜布瓦夫人是想让你跟克洛蒂娜一起去柴棚，对吧？"
show luce sigh2 w with dissolve
Luce "哦，是的，没错。我原本还盼着这回能溜掉一次呢，直到你决定把我一起拖进来。"
Luce "人生可以如此残酷。"
Marcel "抱歉……但有几件事一直让我心里放不下。"
show luce frown2 w with dissolve
Luce "什么事？"
Marcel frown u "杜布瓦夫人为什么执意要让你第一个到这儿来？你个头相当小，我怀疑你根本搬不了那么多木柴回去。"
show luce annoyed2 w with dissolve
Luce "你问得真好，玛塞尔。正如你不可能没注意到的，我是班上个子最小的。连十三岁的孩子都比我高大。"
Luce "既然如此，你选我做搭档实在没有任何理由，除非你是存心要跟我作对。"
Luce "你本该去问别的女孩；{i}任何{/i}一个别的女孩。"
Luce "诺艾米本是个不错的选择。她几乎和你一样高呢！"
show luce neutral2 w with dissolve
Luce "要是你和她搭档，三两下就能把这活儿干完。"
Marcel ehe u "我确实考虑过，没错……{w}但我有时候挺别扭的。有时，我喜欢给自己找罪受。"
Marcel "我想这一定是从我母亲那儿遗传来的。"
Luce "嗯……"
"露丝抿着嘴唇，打量了我片刻——直到最后，她抱起了双臂，转过身去。"
Luce "我就知道你有点古怪。"
Marcel "啊哈哈……也许你说得对。"
show luce sigh2 w with dissolve
Luce "而你甚至没有试图反驳这句话。大多数女孩被人骂了都会难过的，你知道吗？"
Marcel smile u "我不觉得那是骂人。在你陈述事实的时候，就更不是了。"
"我{i}的确{/i}很奇怪。这一点我心知肚明。"
"我不像我的新同学，这不仅是因为我来自巴黎，或是因为我的身高，甚至不仅是因为我是个男孩。正是所有这些因素交织在一起，才把我与米延的女学生们隔离开来。"
"我与众不同，可我一直都是如此。也许我已经习惯了。"
Marcel neutral u "那么……"
show luce neutral2 w with dissolve
"我斜眼打量着我这娇小的同伴。"
Marcel "杜布瓦夫人为什么这么恨你？你知道吗？"
"短暂的沉默。"
show luce sigh2 w with dissolve
"露丝叹了口气。她小小的肩膀在校服布料下微微起伏。"
Luce "看来，你注意到了。"
Marcel sad u "想不注意到都难。杜布瓦夫人毫不掩饰地轻蔑你，尽管你什么都没做错。"
Marcel "克洛蒂娜才是那个捣乱的人，可她完全躲过了惩罚。"
show luce neutral2 w with dissolve
Luce "是啊，唔，克洛蒂娜就是那样。她常常能设法逃过惩罚；尤其是在杜布瓦夫人面前。我想那是因为她太会说话了。"
show luce sad2 w with dissolve
Luce "可惜，我就没那么幸运了。"
Luce "就算我说到脸色发青，也帮不了我的处境。"
Marcel neutral u "那是为什么？"
show luce frown2 w with dissolve
Luce "杜布瓦夫人恨我。"
Marcel "真的是这样？"
"露丝点点头。"
Luce "从她第一眼看到我起，她就恨我。"
Luce "这其中毫无道理可言。我并没有做过什么招致它的事。事情就是如此。"
show luce sad2 w with dissolve
Luce "我可以安静得如同死亡本身，也可以妙语连珠、八面玲珑，但她总能找出点事来数落我。"
Luce "我的指甲长短……不齐的袜子……裙摆上松脱的线头……"
show luce sigh2 w with dissolve
Luce "有时候，我想只要她办得到，她甚至会数落我呼吸声太大，或是数落我在呼吸这回事本身。"
Luce "她为最微不足道的失当就惩罚我；而当我根本没做任何该受罚的事时，她便编造出些冒犯来数落我。"
Marcel sad u "我明白了……"
"事实上，我看得太清楚了。露丝的苦楚，让我想起自己从前在旧学校里所承受的那些。"
"我的同学们会取笑我，朝我扔东西，踹我椅子的背面，而我总是替他们受罚。"
"多年来，我忍受着这样的折磨，除了咬牙默默承受之外别无选择，但我无法容忍听到露丝也受到如此虐待。"
Marcel shock u "但那不公平！你不该被这样对待！根本没有这个必要！"
show luce neutral2 w with dissolve
Luce "你说得很对。这种小家子气的刻薄确实毫无必要，但人生本就不公平。"
show luce frown2 w with dissolve
Luce "它对杜布瓦夫人也并不仁慈。她讨厌自己的工作，这一点显而易见得令人心痛。"
Luce "我觉得她也不喜欢孩子，{i}或者说{/i}青少年。"
Marcel neutral u "她似乎不太擅长管束班级……"
show luce neutral2 w with dissolve
Luce "她确实不擅长。"
Luce "当她叫女孩们安静下来时，她们照样说话，而且常常拒绝做任何笔记。"
Luce "要不是有塞琳，什么事都办不成。"
Marcel "她把每个人都管得服服帖帖吗？"
"露丝点点头。"
show luce frown2 w with dissolve
Luce "塞琳以前在奥尔良的一所女子学校上学。我想，她在那里被教导要如何安静、如何敬重长辈。"
Luce "她主动代杜布瓦夫人管教那些不守规矩的女孩。"
Marcel "而那些女孩肯听她的？"
show luce neutral2 w with dissolve
Luce "也许她们觉得有义务听她的。她确实表现得非常气派、威严。我想她们是想让她另眼相看。"
Luce "杜布瓦夫人感激塞琳的帮忙，但她讨厌自己没有半分威信。她清楚自己多么无能为力，这让她怒火中烧。"
Luce "我想这就是她欺负我的原因。因为我是班上个子最小的，也是最虚弱的。"
Luce "她这么做，是因为她知道我无力还手。我哪里比得上克洛蒂娜或诺艾米，更不用说塞琳了。"
Marcel frown u "真糟糕……"
"我咬紧牙关，为露丝感到愤懑不平。"
Marcel neutral u "也许你该把这件事告诉布吕吉埃夫人。她是个善良的人，我相信她会对你的处境感兴趣的。"
show luce sigh2 w with dissolve
Luce "也许她会吧，但那也无济于事。"
Marcel "可是——"
show luce neutral2 w with dissolve
Luce "这里的老师本来就太少。音乐教师勒梅尔小姐四月就跑了，至今我们还没等到一位替补老师。"
Luce "没人愿意来这样偏僻又沉闷的小村庄工作，我不怪他们。"
show luce frown2 w with dissolve
Luce "布吕吉埃夫人没法赶走杜布瓦夫人。那样就没人能接替她了。"
Marcel shock u "但她至少可以找她谈谈呀！"
show luce neutral2 w with dissolve
Luce "那又能有什么用呢？"
show luce frown2 w with dissolve
Luce "杜布瓦夫人会知道我说了她坏话。到那时，她只会比以往更加凶狠地对待我。"
Luce "这不值得。"
show luce sigh2 w with dissolve
Luce "我对这一切都厌倦了。"
Luce "住在米延……{w}真是太累了。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  9月16日{vspace=1}  陷入沉思") )
scene sky_n with wiperight_slow
play ambience "sfx/night_amb2.ogg" fadein 1.0
play music "bgm/Night.ogg" fadein 1.0
window show dissolve

"那天夜里，我躺在床上休养，望着天花板出神。"
"我的头发如今摆脱了紧紧束缚的辫子，在枕头上铺散开来。我一动，便能感觉到它在移动。几缕松散的头发卡在我的脑袋与枕头之间，我一动，它们便拉扯着头皮。"
"其他女孩想必都已经睡着了。她们的宿舍里听不到一丝动静。"
"我能听到的，唯有风敲打窗棂的声音、我自己的呼吸，以及我那怯生生跳动的心。"
"无论我在床上怎么翻来覆去，就是没法让自己舒坦。"
"我的毯子相当单薄，而这间小屋又很冷。现在已是秋天，很快就要入冬了。"
"到了十二月，积雪会在校园里堆积起来，树叶也会从树上落尽。"
"我不禁想，米延的冬天会是什么样子。会比巴黎更冷吗？那里有着湿滑的鹅卵石街道，和蒙上霜花的窗子。"
"我想，这里会更暗。巴黎的街道一年四季都亮着煤气灯，可米延却没有这样的灯。这里只有山丘和花朵，它们可驱散不了多少黑暗。"

scene cg28 with wipedown_slow

"我再次在床上翻身，铁架床在我的重量下吱呀作响。"
"有那么片刻，我担心这张床会在我身下散架。它显然是给比我矮的人做的。毯子也是，它盖不满我的脚趾。"
"我试着把自己蜷成一团，就像个胎儿。这并没有让我觉得更安全或更暖和，但至少我的脚趾不再受冷了。"
"我躺在那里，难以入眠，便在这脑海中把今天发生的事又过了一遍。"
"这真是累人的一天。"
"从早到晚都扮演着另一个自己，比我预想的还要艰难。"
"我必须做出合乎情理的女性化举止，用合乎情理的女性口吻说话，结果我几乎一言不发，只因生怕自己最终露了馅。"
"也罢。反正我向来都不是个话多的人。我更愿意倾听。"
"至少那是我一贯的态度……{w}可是一到露丝身上，情况就有些不同了。"
"尽管我总在哀叹自己的命运（虽然只是在心里），我却觉得露丝或许比我更糟；她成了倒霉的杜布瓦夫人的替罪羊，每一桩小小的过失都要受罚。"
"这实在不太公平……"
"可是，正如露丝告诉我的那样，生活本就不公平。"
"父亲抛弃母亲，这不公平；从前在旧学校里，其他男孩欺负我，这不公平；我从来都格格不入，这也不公平……"
"但说来奇怪，我觉得自己扮成女孩时给人留下的印象，恐怕比以男孩身份示人时留下的更好。"
"我的同学们似乎喜欢我——或者至少，他们对我不加理会。"
"尽管有人对我身高窃窃私语，但似乎没有人觉得我特别古怪。"
"在我从前的巴黎学校里，我是颗被老师们拼命想嵌进圆孔里的方钉：偏偏还是个演员的私生子。"
"然而在米延，没人能凭我父亲的风流韵事来评判我，因为他们不知道他是谁。"
"他们也不知道我是谁——而在这一点上，他们并不孤单。我自己也不知道。"
"我是谁，我又想要什么？"
"我一无所知。"

stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene sky3 g
with clockwipe
$ renpy.pause(0.5)
show overlay2
show message4 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message4
hide logo2
hide overlay2
with datetrans2

$ renpy.pause(0.3)
play music "bgm/Energetic.ogg" fadein 1.0
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  10月2日{vspace=1}  少女间的私语") )
scene sky3 with dissolve
window show dissolve

"在我度过的这第一天仿佛以蜗牛般的速度缓缓爬过之后，我在米延的时间突然开始以令人目眩的速度飞逝。"
"我尽可能地和同学们搞好关系，而尽管我不怎么说话，同学们似乎也把这当作我性格的一部分来接受了。"

show image "border" onlayer border
scene yard_r:
    subpixel True
    size (1920, 1080) crop (0, 100, 1280, 720)
    linear 20.0 crop (350, 100, 1280, 720)
with wiperight_slow

"十月一个阴沉的早晨，我碰巧听到同学们围在水泵旁议论我。"
"校园里的那台水泵，在清晨时分算是个相当热闹的活动中心——至少我是这么发现的。女孩们常在开课前到这里来洗手洗脸，免得因仪容不整而挨布吕吉埃夫人的责骂。"
"据我观察，克洛蒂娜常在课堂中间故意把墨水或石墨蹭到手指上，好借机离开课程，在感到无聊时到那台水泵旁逗留。"
"……总之，今天早晨我碰到的那些在水泵旁闲聊的女孩中间，并没有克洛蒂娜。"
"一共三个女孩。我全都面熟，却叫不出名字（我这方面记性差得很）。不过我知道，这群人里最高的那个叫诺艾米。"

hide image "border" onlayer border
scene yard_r
show noemie frown r at center
with wipeleft_slow

Noémie "那么，你觉得新来的那个女孩怎么样？"
Marcel shock u "……！"
"一听这话，我便把背贴到附近一棵橡树上，低着头，想尽量不被人发现。"
"我心里有一部分觉得，明智的做法是昂首挺胸地走过这个闲聊的三人组，装出一副对她们的看法毫不在乎的样子。我想克洛蒂娜就会这么做，可我并不像她那样自信。"
"克洛蒂娜似乎不在乎别人怎么看她，可我却抑制不住自己的好奇。"
"我竖起耳朵，试图在泵水的溅落声中捕捉她们低声交谈的嗡嗡响动。"
Cla "她话很少，是不是？"
show noemie neutral r with dissolve
Noémie "起初我还以为她很没礼貌——好像她觉得跟我们说话有失身份似的——但现在我又不太确定了……"
Claa "她看起来不像势利眼，是不是？"
show noemie sigh r with dissolve
Noémie "她每次见到我都冲我微笑。"
Cla "数学课上她还把尺子借给我用呢。"
Claa "她甚至把历史笔记也借给我了！"
show noemie neutral r with dissolve
Noémie "她的字写得很工整，是不是？"
Claa "真优雅。她一定上过书法课！"
Cla "也许她是照着真正的淑女标准培养出来的，就像塞琳一样！"
show noemie frown r with dissolve
Noémie "我听说绅士们喜欢她那样端庄文静的类型。"
Claa "也许她这么安静是因为想隐没在人群之中。一个女孩长得这么高，一定很不好受……"
Cla "不过她确实有一种优雅的气质，是不是？"
Claa "你觉得像她这样的女孩真会受男人欢迎吗？"
show noemie sigh r with dissolve
Noémie "嗯，这个我倒也好奇……"
"诺艾米身量和我相仿，她叹了口气。她似乎为此感到不安，可她的交谈对象们似乎并没有注意到她的烦扰。"
Cla "如果我是男人，跟一个比我高出哪怕两厘米的女孩一起出现在人前，我都会觉得丢脸！这总有点让人威风扫地，你不觉得吗？"
Claa "娇小的女孩肯定更讨人喜欢……不过我倒不觉得玛塞尔会完全不受欢迎。"
Cla "我想她{i}确实{/i}有她自己的一份美。"
Claa "噢，我真希望她别把本地那些男孩子迷住！那就太不公平了！我可是先看上他们的！"
Cla "没错，没错！要是这个从巴黎来的插足者跑来抢走所有合适的男人的目光，那可不公平！"
"一个“闯入者”……？到了这么多星期之后，这些女孩竟还这样看待我吗？"
"这个念头刺痛了我，但我想自己也不便为此太过介怀。尽管我已竭尽全力，却仍未交到任何真正的朋友。"
show noemie neutral r with dissolve
Noémie "我倒不担心。她太安静了，根本不会主动去追求谁。"
show noemie smirk r with dissolve
Noémie "我敢打赌，要是有哪个男人敢接近她，她准会泪眼汪汪地跑开！"
"要是他们知道就好了……"
show noemie smile r with dissolve
Noémie "我们{i}绝对{/i}是更具吸引力的对象，哪怕我们不会写连笔字！我相信我们没什么好担心的！"
show noemie smirk r with dissolve
Noémie "玛塞尔或许长得漂亮，可要是她连一句完整的话都说不利索，那又有什么用呢？"
Noémie "男人是喜欢温顺柔和的姑娘，不错，可也得有个限度！像克洛蒂娜那样话太多的女孩不讨人喜欢，可像玛塞尔那样说话含含糊糊、柔弱单薄的姑娘同样不讨人喜欢！"
Noémie "一个男人又能拿她怎么样，除了打量她之外？她又从来都不开口说话！"
Cla "说得有道理！"
Claa "不管她长什么样，她永远不会像我们这么讨人喜欢；只要她不开口说话就不会！"
Marcel sigh u "……唉，我还在期待什么呢？"
"我叹了口气。"
"我想我能从这段谈话中听出来的也就这么多了。我可没兴趣留下来，听诺艾米和她的同伴们诽谤我。"

stop music fadeout 1.0

"我正准备悄悄溜回教室，去上早晨的第一节课，这时……"

play sound "sfx/footsteps2.ogg" fadein 1.0
show noemie shock r:
    ease 1.2 xpos 0.70

show al frown r:
    xpos -0.10 xanchor 0.5
    ease 1.6 xpos 0.30

$ renpy.pause(1.0)

play music "bgm/Comedy.ogg" fadein 1.0
stop sound fadeout 1.0

Bru "姑娘们，你们好。"
Noémie "噢，呃……啊、啊……"
"我的同学们瞪圆了眼睛，那模样几乎滑稽可笑。她们涨红了脸，愧疚地瞥向地面。"
Noémie "呃……早、早上好，夫人……！"
show al neutral r with dissolve
Bru "早上好，诺艾米。听你们这么兴高采烈的调子，我猜你们姑娘们今早心情不错？"
show noemie neutral r with dissolve
Noémie "噢，呃……是、是的……"
show al annoyed r with dissolve
Bru "那你们这么兴致勃勃地在聊什么呢，嗯？"
show noemie shock r at bounce
Noémie "我们，呃，在聊天气！"
show al neutral r with dissolve
Bru "聊天气，是吗？"
Noémie "没错！"
show al frown r with dissolve
Bru "嗯。"
"布吕吉埃夫人皱起了眉。她看上去并不被这番脆弱的借口所蒙蔽，但似乎也并不因这些女孩对她撒谎而特别恼怒。也许是因为她们的谎言实在太明显了。"
show al neutral r with dissolve
Bru "好吧，我很高兴姑娘们一大早就这么有精神。这是健康与快乐的征兆。"
show noemie smile r at bounce
Noémie "噢，是的，夫人！我们非常健康！"
show al annoyed r with dissolve
Bru "我只想提醒你们几句。"
Bru "我理解你们到了对异性感兴趣的年纪，但你们不应该让这样的闲话占据你们今后的谈话。"
show al frown r with dissolve
Bru "你们现在寻找人生伴侣还太年幼。与其那样，不如把心思放在学业上更有益处。学校是让你们求知的地方，不是用来议论男孩的。请记住这一点。"
show noemie shock r at bounce
Noémie "是、是的，夫人！我明白了！"
show al neutral r with dissolve
Bru "好。"
show al annoyed r with dissolve
Bru "另外，还有一句劝告……"
Claa "什么？"
Bru "我觉得，你们在校园里还是不要那么公开地议论玛塞尔小姐为好。你们永远不知道谁可能正在听。"
show al smile r with dissolve
"布吕吉埃夫人把头偏向一侧。她的目光与我短暂相遇，我看见一抹浅笑掠过她的嘴角。"
show al neutral r with dissolve
Bru "……要是你们碰巧惹恼了，或孤立了你们的新同学，那就太遗憾了。"
Bru "请你们说话再谨慎一些。"
Marcel shock u "哦……"
"我仍躲在橡树的树荫下，别开了目光。"
"布吕吉埃夫人一定看见我躲在这棵树旁了，哪怕我的同学们没有。"
"她是在设法保护我吗？"
"也许，是知道我太害羞、太安静，不敢独自去面对那些女孩，她才决定替我出面。"
"她说过，尽管我是她的侄儿，她也不会给我任何特殊优待，可布吕吉埃夫人或许比看上去要心软得多。"

stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene sky g
with clockwipe
$ renpy.pause(0.5)
show overlay2
show message13 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message13
hide logo2
hide overlay2
with datetrans2

$ renpy.pause(0.3)
play ambience "sfx/birds.ogg" fadein 1.0
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  10月14日{vspace=1}  没安好心") )
scene sky with dissolve
window show dissolve

"时间仍在缓缓流逝。"
"我按时上课，与同学们闲聊些无关紧要的话，夜晚则在自己那间房里入睡。"
"起初我以为自己永远无法适应这样的生活，可如今我已陷入一种惬意的日常节奏。"
"我甚至已经能毫不在意地为自己编好辫子。从前要花上十五分钟的活儿，如今用不了五分钟。"
"我对自己愈发有信心，也愈发习惯在米延这个地方生活了。"
"村庄街道两旁的所有店铺我都已熟悉，我也能借助教堂的钟楼作为参照来辨别方向。"
"当我想要放松时，有一处地方我格外喜欢流连，那就是一座被树木环抱的小湖。"

play music "bgm/Claudine.ogg" fadein 1.0
show image "border" onlayer border
scene lake:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

"这座湖离我上课的那群校舍不过十分钟步行之遥，但环绕四周的天然树篱却使它宛如一个独立的小世界。"
"说来，我最初发现这座湖，纯属偶然。"
"几周前，我在前往柴房的路上迷了路，一路漫无目的地乱走，才偶然闯进了这片林间空地。"
"那时我没什么机会仔细探索它，但后来我又回来过好几次。"
"环绕这座镜面般小湖的树木，披满了秋日的色彩。叶子是红的、棕的、黄的，薄而干脆，宛如纸张。"
"铺着草皮的地面上散落着这些零星的落叶与枯枝，而每阵风起，便有更多的叶子自空中飘落。"
"隐约可以听见鸟鸣声，我能看到细腿的知更鸟在树间蹦跳穿梭。"
"我不认识所有这些树，也叫不出那些鸟的名字。我骨子里是个城里孩子，哪懂得这些。鸽子大约是我唯一认得出的鸟，或许还要算上寒鸦——因为有一次，其中一只顺着母亲公寓的烟囱飞下来，弄翻了壁炉台上的一瓶花。"
"然而，米延这里的鸟，色彩斑斓的胸脯，轻柔甜美的歌喉，对我而言却是个谜。"
"近来，我已习惯于就这么坐在湖边，享受那份相对的宁静。"
"当我被大自然环绕时，我几乎能忘却一切。"
"我能感到所有的压力正从身体里流走。那种感觉几乎就像……"

stop ambience fadeout 2.0
hide image "border" onlayer border
scene lake
show claudine smile at center
with wipeleft_slow

Claudine "玛塞尔！"
Marcel shock u "啊！"
"我猛地一惊，转过头去。"
"是克洛蒂娜。"
"她的脸因用力而泛红，但眼下的黑圈却依旧那么显眼。"
"克洛蒂娜说她每晚至少睡满八个小时（“对正在长个儿的姑娘来说，美容觉很重要！”），而她的眼睛生来就是那般模样，无论她怎么做都改不了。"
"那对黑眼圈给她添了一抹病恹恹的气色，却也让她那双绿眼睛显得格外迷人。"
"我忍不住猜想，她是否化了妆才弄成那副样子？"
Marcel "呃……你好，克洛蒂娜。你在这儿做什么？"
show claudine laugh with dissolve
Claudine "我倒想问你同样的问题呢！"
show claudine smirk with dissolve
Claudine "马上就要上课了！我以为像你这种老师的乖宝贝可不想迟到呢！"
Marcel u frown "我可不是老师的乖宝贝……"
show claudine laugh with dissolve
Claudine "我可不敢苟同！"
show claudine smirk with dissolve
Claudine "你总是比所有人都先做完功课，还尽情享受布吕吉埃夫人给你的夸奖！如果那还不叫老师的乖宝贝，我就不知道什么才叫了！"
Claudine "你那么爱布吕吉埃夫人，她索性给你套上项圈、拴上链子得了！"
Marcel neutral u "我觉得事情不是那样的。"
Marcel shy u "我只是……还不习惯被老师们夸奖。"
Marcel "事实上，我的老师们常常无视我——至于其他人，则干脆讨厌我。"
show claudine neutral with dissolve
Claudine "哦？"
"克洛蒂娜挑起一道眉毛，神情饶有兴味。"
Claudine "你住在巴黎的时候是个坏女孩吗？你是不是顶撞过老师，或是跟别的女孩打过架？别告诉我你扯过别人头发，或是抓破过她们的脸？！"
"我觉得克洛蒂娜对那个前景显得有些过于兴奋了。为什么这个女孩对流血这样的念头如此着迷？"
Marcel sigh u "很抱歉让你失望，但我没做过那些事。"
show claudine laugh with dissolve
Claudine "不，我想象不出你会做那些事。尽管你长得这么高，你看起来也不是那种人！"
show claudine neutral with dissolve
Claudine "真可惜。"
Marcel neutral u "什么可惜？"
show claudine annoyed with dissolve
Claudine "如果我有你那么高，我可是会好好利用它！"
Claudine "要是我能把那个可恶的诺艾米扔出窗外，她就再也不敢背后议论我了！"
Marcel shock u "诺艾米自己就挺高的，而且我觉得你不该把任何人扔出窗外！那听起来太危险了！"
show claudine neutral with dissolve
Claudine "哎呀，这不是明摆着的嘛。这正是{i}关键{/i}所在呀，我亲爱的、迟钝的玛塞尔。"
show claudine smile with dissolve
Claudine "那么，你在以前的学校为什么那么不受欢迎？我想象不出有什么理由能让哪个老师去痛骂一个像你这样的女孩！"
"他们之所以讨厌我，是因为我表现得实在太像个女孩了——但当然，这话我没法对克洛蒂娜说。"
Marcel shy u "呃……这个，我的老师们说我白日做梦做太多了……"
show claudine neutral with dissolve
Claudine "就这样？"
Marcel sigh u "就这些。"
Claudine "嗯……"
show claudine shock with dissolve
Claudine "我不知道这算不算值得这样责骂你的理由，不过也许巴黎的学校比我以为的还要严格！"
Marcel sad u "它们{i}确实{/i}相当严格。我不止一次被用尺子打在手背上。"
show claudine annoyed with dissolve
Claudine "噢，是的。布吕吉埃夫人也这样。"
Marcel neutral u "这么说，你对这种特殊的惩罚方式有切身体会？"
Claudine "你怎么知道的？"
"克洛蒂娜做了个鬼脸。"
Claudine "不知为什么，她总是专门挑我！"
Marcel frown u "我倒是好奇为什么呢……"
Claudine "这真是个谜！"
Marcel u neutral "但体罚也没让你少惹麻烦。"
show claudine heh with dissolve
Claudine "可不是！"
Marcel huh u "你就不怕挨骂吗？"
show claudine smile with dissolve
Claudine "唔，我不喜欢挨骂——我想谁都不喜欢——但这样日子会更有意思一些，你不觉得吗？"
Marcel sigh u "我觉得生活有时候可能{i}太{/i}有意思了。"
Claudine "你{i}当然会{/i}这么想，毕竟你是城里姑娘。在我们乡下，得靠自己找乐子。"
Marcel u neutral "我还以为你喜欢住在乡下呢？"
show claudine laugh with dissolve
Claudine "我是喜欢！我喜欢这里！这是我必须让自己忙起来的原因之一！"
show claudine neutral with dissolve
Claudine "要是我也像你们巴黎人那样有那么多娱乐可以选择，我真不知道自己要该怎么办才好！"
show claudine shock with dissolve
Claudine "我会被那些戏剧和歌剧彻底迷住，以至于连自己都忘了，然后我的一部分就会永远死去！"
Claudine "像我这样的女孩，只有身处亲爱的老米延的山峦与树木之间，才能活得自在！"
show claudine neutral with dissolve
Claudine "不过，像你这样喜欢静坐沉思的女孩……"
Claudine "也许当你远远地、隔着一段安全的距离看着别人的生活发生，才会觉得日子更有意思？"
show claudine laugh with dissolve
Claudine "我相信那样过日子会轻松得多！至少你不必担心惹上麻烦！"
Claudine "而我，幸而没有这样的顾虑！"

scene lake:
    size (1920, 1080) crop (240, 40, 1440, 810)
show claudine smile2:
    xpos 0.5 xanchor 0.5 ypos 0.5 yanchor 0.5
with dissolve

"克洛蒂娜从裙袋里掏出一样东西，一边掏一边坏笑。"
"瞧她那副恶魔般的表情，我几乎以为那东西一定十分见不得人：也许是一盒香烟，或是一瓶杜松子酒……"
"但出乎我意料的是——让我松了口气（还是失望？）——那不过是一个小小的玻璃罐。"
Marcel neutral u "那个罐子是做什么用的？"
show claudine smile2 with dissolve
Claudine "它确实有个非常特别的用途。这一点你得相信我，玛塞尔！"
show claudine laugh2 with dissolve
Claudine "今天必将载入史册！会非常有趣！"
Marcel frown u "……我暂且相信你吧。"
"我已经在这湖畔站了太久，与克洛蒂娜说了太多话。"
"她是个有趣的同伴，我倒不介意多逗留片刻，看看她究竟要用那个玻璃罐做什么。我确信那一定会很好玩——但附近教堂的钟声很快就要敲响了。到那时，我必须回到教室里。"
"布吕吉埃夫人对迟到一事的态度，已经向我表达得很清楚了，我绝不想让她失望。"
Marcel neutral u "那么，我想我待会儿在课堂上见你吧。"
show claudine neutral2 with dissolve
Claudine "噢？你现在就要走了吗，亲爱的玛塞尔？"
Marcel sigh u "是的，我该走了。"
show claudine shock2 with dissolve
Claudine "可是，{i}为什么{/i}我们非得因为别人说我们应该，就去做自己不愿做的事，这样过完一生？要是想幸福，我们就该去做自己真正想做的事！你难道不同意吗？"
Marcel frown u "我认为规则的存在自有其道理。如果每个人都随心所欲、不顾他人，那就成了无政府状态。"
show claudine smile2 with dissolve
Claudine "那又怎样？"
show claudine laugh2 with dissolve
"克洛蒂娜咯咯笑了起来。"
Claudine "你说得好像那是什么坏事似的！"
show claudine smile2 with dissolve
Claudine "你确定我就不能劝你再待一会儿吗？你会错过大好机会的，知道吗！"
Marcel "我敢肯定，今天晚些时候在上课时，我就能看出你在打什么主意。"
show claudine shock2 with dissolve
Claudine "「打主意」！"
"克洛蒂娜咂了咂舌。"
Claudine "你说得我好像没安好心似的！"
Marcel frown u "我{i}知道{/i}你没安好心。"
Marcel neutral u "好了，我真的该走了，你也该走了。不然你就要迟到了。"
show claudine smirk2 with dissolve
Claudine "可是迟到才时髦呢，我可是听说的！这叫娇媚。让男人等上一等，他们反而会兴奋起来！"
Marcel u frown "那又有什么关系？我们教室里可没有男人。"
show claudine neutral2 with dissolve
Claudine "哦，天哪。你可真是太{i}认真{/i}了，我亲爱的玛塞尔。你可没有我期望中的前城里人那么大胆！"
show claudine laugh2 with dissolve
Claudine "真是可惜，不过你要是担心自己老师宠儿的名声，最好还是快走吧。别让我玷污了你！我可真是个糟糕的影响，真的！"
Marcel u neutral "那你呢？"
show claudine smile2 with dissolve
Claudine "我稍后再追上你。"
"我一度动了与她争辩的念头，但很快又打消了。"
"我不知道克洛蒂娜在打什么主意，但我很怀疑她会听我的。"
"她谁也不听。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
play music "bgm/Classroom.ogg" fadein 1.0
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  10月14日{vspace=1}  兴风作浪") )
scene sky with wiperight_slow
window show dissolve

"正如我所料，克洛蒂娜优哉游哉地迟到十分钟走进教室，随即被布吕吉埃夫人当场责罚。"
"布吕吉埃夫人命令克洛蒂娜到学校的操场去，站在教室窗边那棵大橡树旁，直到这堂课结束。"
"这惩罚听起来并不算太残忍，可一旦想到眼下已是十月中旬，而近来风又冷得厉害，那便另当别论了。"
"即便在教室里，壁炉的火烧得正旺，也依然冷得让人不舒服。"
"我看到班里有些女孩在勤勉书写的间隙，干脆坐到了自己手上，只是为了让手指不至于冻僵。"
"然而克洛蒂娜却从容地承受了这惩罚。她只是微微一笑，提起裙摆，朝布吕吉埃夫人行了一个足以媲美公主的屈膝礼。"

scene classroom
show claudine laugh at left2
show al annoyed at right2
with wipedown_slow

Claudine "当然，布吕吉埃夫人。我这就立刻遵从您的命令。我明白迟到进教室实在不该，我为打扰了各位同学宝贵的学习而道歉。"
"克洛蒂娜以一种矫揉造作的上流社会腔调说出这番话，和塞琳的腔调颇有几分相似，把所有元音都念得圆润饱满。"
"有些女孩面面相觑，一脸困惑，另一些则吃吃地笑。"
show al frown with dissolve
"布吕吉埃夫人则怒目而视。"
Bru "话说得真动听，克洛蒂娜。可惜我一个字都不信。"
show claudine shock at bounce
Claudine "哦，夫人！您这是在说我撒谎吗？"
show al sigh with dissolve
Bru "要是我想宽厚一点，或许我倒更倾向于把你那一套称作「做戏」。"
show claudine neutral with dissolve
Claudine "可我已经洗心革面了，布吕吉埃夫人！真的，我已经认识到自己的错了！"
show al annoyed with dissolve
Bru "你每隔一周就这么说，克洛蒂娜。请原谅，我对你的这些小把戏已经厌倦了。"
Bru "我知道少女总归是少女，我也明白你正处在叛逆的年纪，但作为老师，我的职责就是要压一压你那股子火爆劲儿。"
show al frown with dissolve
Bru "现在，出去站着。到冷风里去待一会儿，应该能让你冷静下来。"
show claudine smile with dissolve
Claudine "我感觉完全冷静得很呢，布吕吉埃夫人……但既然您这么希望，我自当毫无怨言地照办！"
show claudine laugh with dissolve
Claudine "再会了，朋友们！我们后会有期！"

play ambience "sfx/footsteps3.ogg" fadein 0.5
show claudine:
    ease 1.3 xpos -0.20

show al annoyed:
    ease 1.0 xpos 0.33

$ renpy.pause(1.2)

play sound "sfx/door.ogg"
stop ambience fadeout 0.5

"同学们看到这番公然反抗，又忍不住咯咯笑了起来；即便克洛蒂娜走出教室，那笑声也迟迟没有消散。"
"布吕吉埃夫人叹了口气，对克洛蒂娜的这出把戏显然不甚满意。"
Bru "好了，姑娘们，咱们回到正题吧……"
"可惜，即便克洛蒂娜（似乎）已被赶出局，全班还是不肯回到正事上来。"

show image "border" onlayer border
scene yard
show claudine smile at left2
with wipeleft_slow

"克洛蒂娜或许是被赶出了教室，颜面尽失，但命令她站的那棵橡树，却恰好紧挨着教室。"
"我的同学们忍不住向窗外张望——而每当他们看过去，克洛蒂娜便做出种种滑稽的鬼脸，逗得他们笑呛出声。"

hide image "border" onlayer border
scene classroom:
    size (1920, 1080) crop (350, 40, 1440, 810)
show mirabel neutral2:
    xpos 0.70 ypos 0.55 xanchor 0.5 yalign 0.5
with wiperight_slow

"至于露丝，她似乎对克洛蒂娜毫无兴趣；可当可怜的米拉贝尔与这位坏心眼同学对上目光——后者正把双手交叠在身前，活像一位基督教殉道者——她便忍不住咯咯笑了起来。"
show mirabel laugh2 with dissolve
Bru frown_side "拉克小姐！请你克制一下自己！"
"布吕吉埃夫人当即反手把黑板擦朝米拉贝尔掷去，吓得她猛地一跳。"
play sound "sfx/stamp.ogg"
show mirabel shock2 at bounce
"她的屁股一下子离开了椅子足有一厘米，一边呜咽着，一边伸手捂住脑袋。"
"隔了三个座位，我都能听见黑板擦砸在她脑袋上的闷响。听声音就知道一定很疼。"

scene classroom
show al frown at center
with wipeup_slow

Bru "好了，要是大家能把克洛蒂娜小姐的胡闹先放到一边，我想开始上课了……"
"这一下，全班总算彻底安静了下来。"

play sound "sfx/footsteps3.ogg" fadein 0.5
show al:
    ease 1.0 xpos 0.75

show mirabel sad:
    xzoom -1 xpos -0.15 ypos 0.55 xanchor 0.5 yalign 0.5
    ease 1.5 xpos 0.35

$ renpy.pause(0.8)
stop sound fadeout 0.5

"米拉贝尔羞怯地离开座位，把黑板擦送回给布吕吉埃夫人，一路上始终用一只手按着太阳穴；布吕吉埃夫人则重新在黑板上书写起来。"

show image "border" onlayer border
scene classroom:
    subpixel True
    size (1920, 1080) crop (300, 100, 1280, 720)
    linear 20.0 crop (300, 300, 1280, 720)
with wipedown_slow

"我和同学们都低下头伏在课桌上，认认真真地把布吕吉埃夫人工整的笔记抄进练习册里。"
"在接下来的历史课里，能听见的只有铅笔尖划过纸张的沙沙声，以及诺艾米咬着铅笔头时发出的牙齿咬合声。"

hide image "border" onlayer border
scene sky
with wipeup_slow

"然而，我们接下来的那一堂课，就完全是另一回事了。"
"每逢周三，上午排在历史课之前的课总是英语课，而英语课不由布吕吉埃夫人讲授，而是由杜布瓦夫人讲授。"
"克洛蒂娜在寒风中站了（也瑟瑟发抖了）将近一个小时后，才被放回教室。她苍白的脸颊比平时更红，双手也在发抖。"
"当杜布瓦夫人吩咐我们在练习本上写下各种过去分词时，克洛蒂娜的手指冻得发麻，铅笔一下子掉在了地上。"

scene classroom:
    size (1920, 1080) crop (0, 40, 1440, 810)
show claudine neutral2:
    xpos 0.30 xanchor 0.5 ypos 0.55 yanchor 0.5
with dissolve

Marcel u huh "哦……"
"克洛蒂娜的铅笔落在地上，发出轻微得几乎听不见的嗒声，随后滚到了我的课桌底下。"
Marcel u neutral "{size=-5}要不要我帮你把它捡起来……？{/size}"
"我压低声音，好让杜布瓦夫人听不见——其实她也并没怎么留意我们。她背对着我们，正忙着用细密的小字在黑板上写下例句。"
"我显然不是唯一一个违背课堂常规的女孩。"
"几个同学正偷偷传着纸条，另一些则把课桌靠得比平常更近，压低声音窃窃私语。"
"与此同时，诺艾米正咬着铅笔芯，低声向同伴念叨着些有的没的（多半是男生的事）。"
show claudine smile2 with dissolve
Claudine "你真好心，玛塞尔，不过我自己来就行了。"
"她的手指看起来简直像是冻伤了，可克洛蒂娜的眼里却闪烁着一丝顽皮。"
"她弯下腰，散落的长发垂拂在地板上，开始摸索——但她的手指并没有像蜘蛛一样在我的课桌下扒拉。相反，她看起来像是在自己的口袋里寻找什么。"
Marcel u frown "嗯，克洛蒂娜？你的铅笔就在这儿。"
show claudine laugh2 with dissolve
Claudine "我知道我的铅笔在哪儿，傻瓜，没事的；我又不是在找它。"
Marcel "那这些过去分词你要怎么抄下来？"
show claudine neutral2 with dissolve
Claudine "说真的，这事儿我还想过，信不信由你。我想我可以用缝衣针扎破指头，用我自己的血来写那些字！那会相当戏剧性，还带点政治意味！"
Claudine "你看，那会是一种抗议，抗议这堂课实在无聊得让人受不了！"
Marcel u shock "别、别那样……！那听起来太危险了——更别说还疼得很！"
show claudine smirk2 with dissolve
Claudine "哎哟，哎哟。"
"克洛蒂娜会意地得意一笑。"
Claudine "你该不会是那种一见到血就头晕的可怜虫吧，玛塞尔？"
Marcel "呃，我……其实更多是那个气味……"
show claudine laugh2 with dissolve
Claudine "哦，天哪！真有意思，一想到你这么大个姑娘，竟会被几滴血吓得退缩！"
show claudine smile2 with dissolve
Claudine "不过别担心。我知道怎么抗议而不伤到我这副漂亮的躯体。"
show claudine smirk2 with dissolve
Marcel "你在说什么啊？"
Claudine "我倒想知道……"
"克洛蒂娜从裙袋里掏出一样东西。那是圆形的，质地为玻璃，刚好妥帖地握在掌心。"
show claudine smile2 with dissolve
Claudine "想看看我在湖边弄到了什么东西吗？"
Marcel u huh "我是有点好奇，不过……"
"我咽了口唾沫。"
Marcel u frown "你真的要在课堂上把它拿出来吗？"
show claudine smirk2 with dissolve
Claudine "这正是这场演练的全部意义所在啊，玛塞尔！拜托，用用脑子！"
show claudine smile2 with dissolve
Claudine "我在一堆树叶底下发现了这个小家伙。我想他一定是在冬眠。"
Claudine "外面冷得要命，可教室里暖和得多。说不定这股热气能把他唤醒！"
Marcel u frown "「他」……？"
"我忐忑不安地盯着那个玻璃罐。"
"因为有克洛蒂娜的手指挡着，我看不清罐子里的东西——但我已经开始猜想到里面装的是什么了。"
Marcel u shock "里面该不会有一只{i}活物{/i}吧？"
show claudine smirk2 with dissolve
Claudine "也许我们该打开看看，一探究竟！这可是重大的科学趣事……"
show claudine laugh2 with dissolve
Claudine "而且我敢肯定，我的同学们会很乐意认识我的新朋友！"
Claudine "他至少也该让这堂课变得有趣一些！"
show claudine smile2 with dissolve
"克洛蒂娜在桌面底下拧开玻璃罐的盖子，然后将罐口凑向地面。"
Claudine "来呀，小朋友。醒醒。来吧。这可是你的大登场。"

stop music fadeout 1.0

Claudine "别被这么多大姑娘吓着。我敢肯定她们会喜欢你的！"

play music "bgm/Comedy.ogg" fadein 1.0
show image "border" onlayer border
scene classroom:
    subpixel True
    size (1920, 1080) crop (300, 100, 1280, 720)
    linear 25.0 crop (300, 300, 1280, 720)
with wipedown_slow

"慢慢地，极其缓慢地，一个斑驳的绿色脑袋从罐子里探了出来。"
"那个斑驳的绿色脑袋连着一个斑驳的绿色身体，身体上长着两对斑驳的绿色腿，每条腿的末端都带着蹼状的脚趾。"
"那是一只蟾蜍。"
"那只蟾蜍因为秋寒而仍处于半睡半醒之间，落在地板上，困惑地四下张望。"
"被一个淘气的女学生抓起来塞进罐子，又被带到一个满是陌生人的陌生教室里，想必是一次令人晕头转向的经历。"
"我想我能体会那种感受。那只蟾蜍赢得了我的同情。"
Marcel u shock "……"
"至少，假如它不长得那么狰狞，我本该{i}会{/i}同情它的！"
"我想我以前从没见过蟾蜍，但我从没想过它们的眼睛会这么鼓凸，身体会这么矮胖。"
"万一它朝我爬过来呢？"
"如果……如果它碰到我呢？"
"它的皮肤摸起来是黏滑的吗？它身上的气味又如何？"
"它不是那种会喷毒的蟾蜍，对吧……？"

hide image "border" onlayer border
scene classroom:
    size (1920, 1080) crop (0, 40, 1440, 810)
show claudine neutral2:
    xpos 0.30 xanchor 0.5 ypos 0.55 yanchor 0.5
with wipeup_slow

Claudine "玛塞尔？"
"克洛蒂娜朝我这边歪了歪头，带着甜美的困惑神情。"
Claudine "你怎么了？脸色有点苍白。"
Marcel u shy "哦，嗯，我、我没事。"
Claudine "你不会害怕一只蟾蜍吧？他只是个小小的小宝贝！"
Marcel u huh "{i}这{/i}是小宝贝？都快有我手掌那么大了！"
show claudine smile2 with dissolve
Claudine "正是！他就是个小不点儿！"
show claudine smirk2 with dissolve
Claudine "你该看看夏天聚集在湖边的一些真正的大家伙蟾蜍。它们可大得吓人！"
Marcel u sigh "大、大得吓人，你说……？"
show claudine laugh2 with dissolve
Claudine "嘿嘿嘿。"
"克洛蒂娜坏笑起来。"
Claudine "你们这些城里姑娘真有趣。表现得好像从没见过蟾蜍似的。"
Marcel u huh "唔、唔——"
show claudine shock2 at bounce
Claudine "我的天哪！不会是真的吧！你不是在逗我玩吧？"
Marcel u frown "我……我、我不知道巴黎是不是抓蟾蜍的好地方，不——我想，除非你去公园里。"
show claudine smile2 with dissolve
Claudine "那这对你来说该是一次增长见识的经历！"
show claudine laugh2 with dissolve
Claudine "去吧，我的小朋友。摧毁。吞噬。剿灭！"
"克洛蒂娜用鞋尖轻轻碰了碰那只蟾蜍。她动作很轻，并无意伤害这位同类，但我看那只蟾蜍并不领情。"
"蟾蜍困惑地抽动了一下，在它蹼状的脚掌上挪了挪身子。"
"它迟缓地向前跳去，在那一大片椅子腿与桌腿组成的“森林”下蜿蜒前行。尽管动作缓慢，它看起来却几乎带着某种目的，仿佛在寻找着什么；也许是在寻找它原来的家？"
"可惜，它在这儿可找不到多少水。"
"过了好一会儿，看来其他女孩终于注意到她们有“伙伴”了。"
"窃窃私语如燎原之火般在教室里蔓延开来，人人转头张望，眼中满是惊恐。"

show image "border" onlayer border
scene classroom:
    subpixel True
    size (1920, 1080) crop (0, 230, 1280, 720)
    linear 25.0 crop (350, 230, 1280, 720)
with wiperight_slow

Cla "那、那是什么？"
Claa "那是只{i}蟾蜍{/i}吗？"
Cla "它、它是什么时候进来的？"
Claaa "它{i}怎么{/i}进来的？"
Cla "是不是有人把它带进来开玩笑的？"
Claa "我是说，它总不会是自己爬进来的吧……"
Claaa "它、它在盯着我看……！"
Claaaa "嘿！我觉得它还挺可爱的！"
Claa "你、你觉得{i}那{/i}可爱？"
Cla "它、它看起来好黏糊！"
Claa "小心，露丝！它朝你这边来了！"
Luce neutral "哦？这是什么？"

play sound "sfx/slap.ogg"
hide image "border" onlayer border
scene classroom:
    size (1920, 1080) crop (350, 40, 1440, 810)
show mirabel shock2:
    xpos 0.70 xanchor 0.5 ypos 0.55 yanchor 0.5
    ease 1.0 ypos 0.5
with wipeleft_slow

Mirabel "{size=+5}呀啊啊啊！！！{/size}"
"坐在露丝身后的米拉贝尔突然尖叫一声，猛地站了起来。她的椅子向后倒去，重重砸在地上，发出一声巨响。"
"当然，这只会让局面愈演愈烈。"
"杜布瓦夫人吓了一跳，手中的粉笔从指间滑落，她猛地转过身来。"

scene classroom
show mirabel shock:
    xpos 0.70 xanchor 0.5 ypos 0.5 yanchor 0.5
show paulette frown:
    xpos 0.30 xanchor 0.5 ypos 0.5 yanchor 0.5
with wiperight_slow

Dubois "你、你到底是叫唤什么呀，米拉贝尔？你伤着了吗？"
show mirabel scared with dissolve
Mirabel "没、没有，我只是……我、我……"
show mirabel:
    ease 0.8 xpos 0.75
"米拉贝尔把背紧贴在墙上，惊慌地睁大了眼睛，整个身子都在发抖。"
"她那样子几乎像是想直接穿过这堵墙，整个人逃进操场里去——但当然，那是不可能的。"
"她被自己和露丝的课桌夹在中间，动弹不得，只能死死盯着前方，用手指着地面。"
show mirabel sad with dissolve
"她那发抖的手指正径直指向——"
show paulette sad at bounce
Dubois "啊、啊啊……！"
"当杜布瓦夫人一眼看到那只蟾蜍时，她也发出了一声尖叫。"
Dubois "那、那……那……"
"杜布瓦夫人的脸一下子变得煞白。"
show paulette mad at bounce
Dubois "那、那到底是什么……{w}那……{w}那{i}东西{/i}在我的教室里干什么……？！"

show noemie neutral:
    xpos 1.20 xanchor 0.5 ypos 0.5 yanchor 0.5
    ease 1.2 xpos 0.88
with dissolve

Noémie "一定是有人把它带进教室的，夫人。"
show paulette sad with dissolve
Dubois "带、带进来的？从哪儿？"
show noemie shock with dissolve
Noémie "从湖边！"
Cla "它肯定是在冬眠！"
Claa "这一定是某种恶作剧……"
show mirabel scared at twirl
Mirabel "啊、啊……！它、它又动了！它在动！"
Claaa "快，谁来抓住它！"
show noemie sad with dissolve
Noémie "我可不敢碰它！"
show paulette frown with dissolve
Dubois "塞琳，你不行……？"

show mirabel:
    ease 0.8 xpos 0.62

show noemie:
    ease 1.0 xpos 0.74

show celine frown:
    xpos 1.15 xanchor 0.5 ypos 0.54 yanchor 0.5
    ease 1.4 xpos 0.88

Celine "我……我、我可不想靠近它！"
show noemie frown with dissolve
Noémie "呃，我也不想！"
show mirabel sad with dissolve
Mirabel "好、好可怕……"
show paulette sad with dissolve
Dubois "它、它朝我这边来了！"
show paulette:
    ease 0.8 xpos 0.20
"杜布瓦夫人惊恐地后退了几步，睁大了眼睛。"
show paulette mad with dissolve
Dubois "我可没法在这可怕怪物蹦来蹦去的时候上课！你们之中总得有个人去把它弄走不可！"

scene classroom:
    size (1920, 1080) crop (0, 40, 1440, 810)
show claudine smile2:
    xpos 0.30 xanchor 0.5 ypos 0.55 yanchor 0.5
with wipeleft_slow

Claudine "让我来！我{i}可{/i}不怕一只蠢蟾蜍！"

play sound "sfx/footsteps3.ogg" fadein 0.5
scene classroom
show claudine smile:
    xpos -0.20 xanchor 0.5 ypos 0.5 yanchor 0.5
    ease 10.0 xpos 0.35
with wiperight_slow

"克洛蒂娜卷起袖子，缓缓地向那只蟾蜍逼近。"
"蟾蜍茫然地看着她，喉咙一阵痉挛，发出咕咕的叫声。"
"它那双大大的黄眼睛朝门口瞥去，也许是盼着能逃出去，但克洛蒂娜动作快得让它来不及。"

show claudine:
    ease 1.0 xpos 0.50

Claudine "抓住你了！"
stop sound fadeout 1.0
"她以近乎非人的速度把手划过半空，将手指箍住了蟾蜍肥圆的身躯。"
"蟾蜍扭动着身子，蹼状的腿乱踢着，想要挣脱克洛蒂娜的手，却收效甚微。"
show claudine laugh with dissolve
Claudine "你不会再打扰我们了！"

show image "border" onlayer border
scene classroom:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

"教室里安静了片刻。"
"同学们面面相觑地眨着眼睛，而杜布瓦夫人看着克洛蒂娜，克洛蒂娜则看着那只蟾蜍。"
"随后，在一阵如释重负、仿佛是众人齐声发出的叹息之后……"
Cla "克洛蒂娜抓住了！"
Claa "她真是个英雄！"
Claaa "我真不敢相信！她徒手就把那只蟾蜍拎了起来！"
Cla "我妈妈跟我说过，那样做会起疹子的。"
Claa "什么样的姑娘碰蟾蜍会连眉头都不皱一下？"
Cla "可克洛蒂娜一点都没犹豫！"
Claaa "她真是太了不起了！"
"克洛蒂娜微笑着，以一个夸张的屈膝礼接受了她应得的赞美。"
"她表现得活像一位把全班从不可名状的威胁下拯救出来的英勇战士——尽管正是她把那“威胁”带进教室的！"
"我真不敢相信，我这辈子竟从没遇见过比她更不知羞耻的女孩！"

hide image "border" onlayer border
scene classroom
show paulette neutral:
    xpos 0.75 xanchor 0.5 ypos 0.5 yanchor 0.5
show claudine smile at left2
with wipeleft_slow

Dubois "干、干得好，克洛蒂娜。你省了我们不少麻烦。"
Dubois "你真是太好了。"
Claudine "不客气！我一向乐意效劳！"
show claudine neutral with dissolve
Claudine "那么，您想让我怎么处置他？"
Dubois "{i}处置{/i}……？"
Claudine "我总得把他放到什么地方去吧，总不能把他藏进我的课桌里！他会爬得我满课本都是！"
Dubois "不行……"
"杜布瓦夫人的脸刷地一下白了。"
Dubois "你绝对{i}不能{/i}那样做。"
Claudine "那我又{i}该{/i}怎么做呢，夫人？"
Dubois "去把他放回外面。那儿才是他该待的地方。"
Claudine "要把他送回湖边吗？"
Dubois "是的，我……我想那样最好。"
show claudine laugh with dissolve
Claudine "您说得对，夫人！我一会儿就回来！"
"克洛蒂娜朝杜布瓦夫人行了个礼，手里还攥着那只蟾蜍，便径直走出了教室。"

play ambience "sfx/footsteps3.ogg" fadein 0.5
show claudine:
    xzoom -1
with dissolve

$ renpy.pause(0.2)

show claudine:
    ease 1.2 xpos -0.20

show paulette:
    ease 1.2 xpos 0.55

$ renpy.pause(0.8)

play sound "sfx/door.ogg"
stop ambience fadeout 0.5

"门在克洛蒂娜身后砰的一声关上了，她一走，杜布瓦夫人便回过头来看向全班。"
"此刻她皱起了眉，声音里透着一股凝重说道……"

scene classroom:
    size (1920, 1080) crop (350, 40, 1440, 810)
show paulette frown2 at center
with dissolve

Dubois "把蟾蜍带进来的肯定是你们其中一个人，可谁会做出这么残忍的事呢？"
Claa "不是我，夫人！"
Cla "也不是我！"
Mirabel shock "我、我绝不会碰蟾蜍的……它、它们好可怕……"
Cla "谁会{i}想{/i}去碰蟾蜍啊？！我是说，真的！除非你疯了！"
Claaaa "我觉得蟾蜍很可爱，但在秋天打扰它们就很残忍了，毕竟那时它们本该在冬眠。"
Claaa "这可不是什么有趣的玩笑。"
Claa "不过，{i}肯定有人{/i}把它带进来的。它不可能自己爬进来！"
Noémie smile "哦，哦！我知道是谁干的，夫人！"
show paulette neutral2 with dissolve
Dubois "你知道？那是谁，诺艾米？你看见了吗？"
Noémie "不算看见……{w}但我想一定是露丝干的！"

stop music fadeout 1.0

show paulette frown2 with dissolve
Dubois "露丝？"
Noémie "没错！那只蟾蜍当时就在她课桌旁跳着，而她是唯一一个看见却没尖叫的人！"
Cla "嘿，诺艾米说得对！露丝看起来一点都不害怕！"
Claa "她看起来一点都不惊讶！"
Claaa "她甚至毫无反应！"
Claa "她{i}一定{/i}是干的！"

play music "bgm/Mysterious.ogg" fadein 2.0

scene classroom:
    size (1920, 1080) crop (0, 40, 1440, 810)
show luce neutral2:
    xpos 0.25 xanchor 0.55 ypos 0.50 yanchor 0.5
with wipeleft_slow

Luce "什么？"
"露丝在椅子上稍稍坐直了些，随即定定地望着杜布瓦夫人。"
show luce sad2 with dissolve
Luce "不，我没有——"
"她刚开口，杜布瓦夫人便立刻打断了她。"

scene classroom:
    size (1920, 1080) crop (350, 40, 1440, 810)
show paulette frown2 at center
with wiperight_slow

Dubois "啊，是啊。{i}露丝。{/i}"
"杜布瓦夫人的声音压低了，化作一声低沉、骇人的耳语。"
Dubois "准是你干的，对吧？你{i}总是{/i}想让我难堪。"
Luce sad "不、不，我没有——"
show paulette mad2 with dissolve
Dubois "住口！"

play sound "sfx/slap.ogg"
with vpunch

"杜布瓦夫人拿起一把木直尺——那东西名义上用来指点黑板上的要点，实则多半被用作惩戒的工具——重重地敲在讲台上。"
Dubois "我不允许你跟我顶嘴，露丝！"
Dubois "我知道你怨恨我，但你也不必把活物带进教室！要是有人踩到它怎么办？要是它被踩死了怎么办？"
"我的同学们一想到那个念头，都因共通的嫌恶而打了个寒颤。"
show paulette frown2 with dissolve
Dubois "我对你本就不抱任何期望，你这个懒丫头，但这已经忍无可忍了。"
Dubois "我不能让你就这么安然无恙地坐着。不拿你做个榜样，谁知道你下次还会做出什么事来？"
Dubois "现在，站到教室前面来。"
Luce "可、可是——"
show paulette mad2 with dissolve
Dubois "{i}立刻！{/i}"

scene classroom:
    size (1920, 1080) crop (0, 40, 1440, 810)
show luce sad2:
    xpos 0.25 xanchor 0.5 ypos 0.55 yanchor 0.5
with wipeleft_slow

"露丝咬住下唇。她的脸几乎看不到一丝血色。"
"她显然不想站到全班前面去，可她又有什么选择呢？"
"要是她继续违抗杜布瓦夫人，说不定会招来更严厉的惩罚。"

play sound "sfx/chair.ogg"
show luce:
    ease 0.8 ypos 0.5

"露丝迟疑地站起身来。椅腿刮过木地板，那声音响得让人难受。"

scene classroom
show paulette frown at center
with wiperight_slow

Dubois "来吧，快点儿。你越快听话，惩罚就来得越快。"

play sound "sfx/footsteps3.ogg" fadein 0.5
show paulette:
    ease 1.4 xpos 0.75

show luce sad:
    xpos -0.15 xanchor 0.5 ypos 0.5 yanchor 0.5
    ease 2.4 xpos 0.25

$ renpy.pause(1.8)
stop sound fadeout 0.5

"露丝垂着头，拖着缓慢的步子挪到教室前面。我看见她试图平复自己的表情，可她的下唇还是止不住地颤抖。"
"这一整段时间里，我的血都在沸腾。"
"这不公平！这不是露丝的错！不是她把蟾蜍带进教室的，她也绝不该受这样的惩罚！"
Marcel shock u "杜布瓦夫人！请别责怪露丝！"
"我还没能克制住自己，人就已经站了起来，用尽平生从未有过的大声喊了出来。"
Marcel "把蟾蜍带进教室的不是她！"
show paulette frown with dissolve
Dubois "什么？"
"杜布瓦夫人皱起了眉头。"
show paulette neutral with dissolve
Dubois "那会是谁？"
Marcel neutral u "是……呃……"
"我顿住了。"
"我本可以把真正的罪魁祸首供出来，可我不想让克洛蒂娜对我怀恨在心。她看起来还算友好，可她要是藏着什么恶意，我也丝毫不会觉得意外。"
"要是我向老师告发她，她肯定会知道是我做的。我可是唯一一个在湖边看见她的人。"
"我得想个说辞才行。"
"既然没法把克洛蒂娜牵连进来，那我就只能认下这件事了。"
Marcel u huh "{i}我{/i}才是把蟾蜍带进教室的人！"
show paulette frown with dissolve
Dubois "{i}你？{/i}"
"杜布瓦夫人皱起了眉头。"
Dubois "你为什么要这么做？你是我最好的学生之一。在我的课上你从不捣乱。"
Marcel u sad "我知道，但是……真的是我。"
Dubois "真的吗？你有什么证据？"
Marcel frown u "嗯……"
"我朝克洛蒂娜的课桌下瞥了一眼，想找那个空罐子，可它并不在那里。想必她又把它放回口袋里带走了。"
Marcel neutral u "我没有证据，但是——"
show paulette sigh with dissolve
Dubois "那就坐下。你在浪费我的时间。"
Marcel u shock "可是——"
show paulette neutral with dissolve
Dubois "我知道你想为同学辩护，玛塞尔，我也觉得这值得称赞，但露丝不值得你为她浪费口舌。她是个阴郁又脾气暴躁的女孩，需要被教训一顿。"
Marcel shock u "但那不公平……！"
show paulette frown with dissolve
Dubois "在这间教室里，{i}由我{/i}来决定什么是公平、什么是不公平。现在，露丝，伸出手来。"
"露丝默默地伸出双手，掌心朝下。"
show paulette neutral with dissolve
Dubois "会有点儿疼，但我只是在给你应得的惩罚。"
Dubois "露丝，你真是该谢谢我，我竟然还想着把你这样一个无可救药的女孩塑造成一个像样的成年人。"

play sound "sfx/slap.ogg"
scene sky with wipeup_slow

"说着，杜布瓦夫人便抡起那把木直尺，啪的一声脆响，狠狠打在露丝的指节上。"

play sound "sfx/slap.ogg"
with vpunch

$ renpy.pause(0.3)

play sound "sfx/slap.ogg"
with hpunch

$ renpy.pause(0.3)

play sound "sfx/slap.ogg"
with vpunch

"她打了一下、两下、三下；一下又一下，直到那鞭打声在整间教室里回荡。"
"从头到尾，露丝都挺直着背。她的眼眶盈满了泪水，却始终没有哭出来。"
"每一声木尺落下的脆响，她的身子都会微微一颤，可她不退缩，也不躲闪。她的表情始终是那样坚硬、锈铁般冰冷。"
"而我，这一刻能做的惟有旁观。"
Marcel sad u "嗯……"
"我咬紧了牙关，被这满腔的不公刺痛着。"
"为什么露丝要为一件她根本没做过的事受罚？"
"我多希望能帮上她的忙……"
"可现在已经太迟了。"
"我真是彻头彻尾的没用。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
play ambience "sfx/footsteps2.ogg" fadein 1.0
play music "bgm/Sad.ogg" fadein 1.0
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  10月14日{vspace=1}  问心无愧") )
show image "border" onlayer border
scene yard:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 30.0 crop (350, 50, 1280, 720)
with wiperight_slow
window show dissolve

"那天午后，趁着午休，我在操场上找到了露丝。"
"她坐在一棵老橡树的枝叶下，低着头，脸大半隐在阴影里，鼻子深深埋进一本书中。"
"操场上差不多空无一人。我的大多数同学都还待在里面，在餐厅里叽叽喳喳地说个不停。"
"我并不觉得特别饿，所以决定不吃午饭了——很显然，有这种感觉的不只我一个。"
"我犹犹豫豫地朝露丝走去，就像一个追踪猎物鹿儿的猎人。我有点担心，怕一步踩错或是一片草叶的沙沙声会吓到她，可这想法实在可笑。"
"露丝方才能在教室前面站得笔直，挨了木尺那一下下狠打而毫不退缩。她想必极为坚忍。"
"又或者，她早已是承受过无数次这等野蛮刑罚的老手了。"

stop ambience fadeout 2.0
hide image "border" onlayer border
scene yard:
    size (1920, 1080) crop (480, 140, 1440, 810)
show luce neutral2:
    xpos 0.5 xanchor 0.5 ypos 0.55 yanchor 0.5
with wipeleft_slow

Marcel u sad "嗯……你还好吗，露丝……？"
"露丝的肩膀绷紧了。她放下书，用满含戒备的眼神看着我。"
show luce frown2 with dissolve
Luce "玛塞尔……"
Marcel u shy "是我。希望没打扰到你？我只是想知道你怎么样了。"
show luce sigh2 with dissolve
Luce "我冷。"
Marcel u neutral "确实是挺冷的，不过——"
show luce neutral2 with dissolve
Luce "那么，如果你只是想知道这个……"
"露丝又拾起书来，盯着书页。那是一本薄薄的小册子，四角看上去有些磨损，有几页还皱巴巴的。"
"这一定是一本她反复翻阅、爱不释手的书。露丝想必从前读过它很多很多遍了。"
Marcel u huh "你在读什么？"
show luce frown2 with dissolve
"露丝皱起了眉。她思量了片刻，然后把书的封面举起来给我看。"
"我满腹狐疑地看了过去。"
Marcel u neutral "{i}Poésies{/i}？马拉美的？"
show luce neutral2 with dissolve
"露丝点了点头。"
Marcel "所以，那些是诗？"
show luce sigh2 with dissolve
Luce "恭喜你，你会读书。"
Marcel u shy "嗯……谢谢？"
show luce frown2 with dissolve
"露丝翻了个白眼。"
Luce "我不是在称赞你。"
Marcel u sigh "我知道你不是。"
"我知道露丝此刻心情很差，但我并不怪她。她的手想必还在为杜布瓦夫人的惩罚而隐隐作痛——她的自尊想必也痛着。"
"我自己对那种为莫须有之事蒙冤受责的滋味，实在是再熟悉不过了。"
Marcel u neutral "那么，你喜欢诗？"
show luce neutral2 with dissolve
Luce "一点点。"
Marcel u smile "看来你已经把这书读了很多遍了。"
Luce "也许吧。"
"露丝耸了耸肩。"
Luce "在我来这里之前，父亲把它送给了我。他也喜欢这些诗。"
show luce sigh2 with dissolve
Luce "我觉得它们有点儿忧郁。"
Marcel u ehe "我听说马拉美有点儿晦涩难懂。"
show luce neutral2 with dissolve
Luce "也许吧，如果你从未悲伤过的话。"
Marcel u neutral "你有最喜欢的他的诗吗？"
show luce huh2 with dissolve
Luce "……也许是{i}The Windows{/i}。"
Marcel "它讲的是什么？"
show luce frown2 with dissolve
Luce "难道我要向你解释每一件小事吗？"
Marcel u sigh "嗯……不用，我想不必了。"
Marcel u sad "我没有打扰到你吧？如果打扰了，很抱歉。我只是担心你。"
Luce "哦？"
"露丝挑了挑眉毛。"
Luce "这倒是新鲜。我还以为你是来幸灾乐祸的。"
Marcel shock u "别、别这么说！我绝不会做那么残忍的事！"
show luce sigh2 with dissolve
Luce "……我知道。"
"露丝垂下头，然后朝着清冷的空气轻轻呼出一口气。"
Luce "你不是那样的人。别人或许会那样，但你不会。"
Luce "你不一样。"
play sound "sfx/bookclose.ogg"
show luce neutral2 with dissolve
"露丝合上书，把它放在膝上，接着用右手掌心平平地按在书的封面上。"
"这个动作虽然再寻常不过，却让我清清楚楚地看见她那只可怜的手红成了什么样。她的指节上交错着一道道红肿的隆起，皮肤看来又起了水泡、又红肿发炎。"
Marcel u sad "疼吗……？"
show luce frown2 with dissolve
Luce "{i}你{/i}觉得呢？"
Marcel u sigh "抱、抱歉。我想这应该很明显。"
Marcel u sad "不过说真的，你的手都红得破皮了。"
"我这辈子也挨过不止几次木直尺的责罚，可我想不起来有哪一位老师打得这么狠过，何况他们还是男人。"
"像杜布瓦夫人这样一个瘦小的女人，怎么能造成这么大的伤害——而且，或许更迫切的是，她为什么要这么做？"
Marcel u shock "杜布瓦夫人这次太过分了！"
show luce sigh2 with dissolve
Luce "我已经习惯了。"
Marcel "但是你{i}不该{/i}习惯这样的对待！你不该站在那里默默忍受！"
"这话由我说出来可真够虚伪的——毕竟有那么多回，我就是那样温顺地低下头、默默承受着自己的遭遇——可我实在压不住心头那股愤懑。"
"看到露丝那双可怜、红肿、磨破了皮的手，我的心猛地揪紧了。"
"可露丝自己却似乎对她这份处境毫不在意。她的脸被小心翼翼地抹平了，像一张面具。"
show luce neutral2 with dissolve
Luce "我想我已经告诉过你了。我除了接受，别无选择。"
Marcel u sad "不过你一定很疼吧。"
show luce frown2 with dissolve
Luce "那又怎样？怎么了？"
Luce "我没法回到过去，阻止杜布瓦夫人伤害我。"
Marcel u neutral "确实，那可能已经来不及了，但你应该试着照顾好你的手。"
Marcel "不如把手放到冷水下冲冲？这应该能缓解疼痛。"
show luce sigh2 with dissolve
Luce "你太担心了。这点苦算不了什么，我应付得来。"
Marcel u shock "不，这不算不了什么！你在流血，露丝！"
show luce neutral2 with dissolve
Luce "流得不多，伤口也不大。其实并不疼，真的。"
Marcel "但还是可能感染的。我不想看到那样！"
show luce sigh2 with dissolve
Luce "……那{i}确实{/i}会很麻烦，是的。"
Luce "我不想发烧。我的父母会担心的。"
Marcel u sad "我觉得你更应该多关心关心你自己。"
show luce neutral2 with dissolve
Luce "你这么想吗？"
"露丝眨了眨眼。"
Luce "但没必要。"
Marcel u huh "那你为什么要这么说呢？"

play sound "sfx/rustle.ogg"
scene yard
show luce frown:
    xpos 0.5 xanchor 0.5 ypos 0.60 yanchor 0.5
    ease 0.8 ypos 0.5
with dissolve

"露丝站起身来，裙摆在她腿边轻轻飘动，然后看着我。"
stop sound fadeout 1.0
show luce frown with dissolve
"她的目光那样锐利，让我觉得自己的皮肤仿佛正被一根针穿来刺去。"
Marcel u shockblush "什、怎么了？我脸上有什么东西吗？"
Luce "没有。我只是在想……"
Marcel "想什么？"
show luce neutral with dissolve
Luce "我从来都不怎么担心自己……"
show luce smile with dissolve
Luce "而现在，我也不需要了。"
"而露丝笑了。"
"那是一个非常小的笑，细薄如同横贯她指节的伤痕，却终究是一个笑容；即便如此含蓄，也丝毫不减其美。"
Luce "因为现在，有你替我担心了。"

stop music fadeout 1.0
window hide dissolve
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  10月14日{vspace=1}  患难见真情") )
scene black with blinds2
$ renpy.pause(0.8)
play ambience "sfx/bath.ogg" fadein 1.0
scene yard:
    size (1920, 1080) crop (300, 40, 1440, 810)
show luce neutral2 at center
with blinds2
window show dissolve

Marcel u neutral "这话怎么说？"
Luce "……没事。"
Marcel u sad "你确定吗？"
show luce sigh2 with dissolve
Luce "嗯。"

play music "bgm/Friendship.ogg" fadein 1.0
show image "border" onlayer border
scene yard:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

"我和露丝正站在操场上的水井旁边。水从生锈的水龙头里汩汩流出，在黯淡的秋日阳光里泛着彩虹般的光泽。"
"零落的水珠溅落在地上。我的鞋子和裙摆都湿了，可我毫不在意。我全部的心神都放在露丝身上。"
"当水流冲刷过她那双手受尽摧残的手时，她身子颤抖着——先是手背，然后是掌心——可她连一声疼痛的哼声都没有发出。"
"我猜想，她或许会把这当作是承认软弱吧。"
"露丝身形虽小，可她必定有着士兵一般的坚毅决心。"
"流水的声音，与那些已经在饭厅用完餐的同学们的闲谈声交织在一起。"
"几个和我们在杜布瓦夫人英语课上同班的女孩停下脚步，朝我和露丝投来好奇的目光。其中一些人似乎怜悯露丝和她那份处境，另一些人则看得兴致勃勃。"
"我真希望她们别这么直勾勾地围观我们。我费尽了全部意志力，才忍住没去呵斥她们冷酷无情。"
"说真的，想到自己从来没怎么懂得自保，这还挺可笑的。我默默地承受了所有对我的虐待，可换作露丝，我却做不到同样的事。"
"我不明白，为什么我对她所受之苦的反应，会跟我对自己所受之苦的反应如此不同？"
"这想必是我那点正义感在作祟吧。我无法保护自己，可我不喜欢看到别人受到伤害。"
"说到这个……"

hide image "border" onlayer border
scene yard:
    size (1920, 1080) crop (300, 40, 1440, 810)
show luce neutral2 at center
with wipeleft_slow

Marcel u sad "你的手怎么样了，露丝？希望它们别太疼。"
show luce sigh2 with dissolve
Luce "我会没事的。杀不死我的，只会让我更强。"
Marcel "你不必故意装得这么坚强，你知道的。"
Marcel "像你说的，我想为你担心。你可以告诉我你真实的感受。"
show luce neutral2 with dissolve
Luce "……可你对我来说还是个陌生人。"
show luce frown2 with dissolve
Luce "把所有的秘密都托付给你，也许很危险。"
Marcel u shock "我才不会拿你的秘密做什么呢，傻瓜！你把我当成什么人了？"
show luce huh2 with dissolve
Luce "我还不确定我该把你当成什么人。我还不怎么了解你。人再怎么小心也不为过。"
Marcel u ehe "好吧……你说得可能有些道理。"
"除了早餐桌上几次偶然的交谈，还有好几周前在柴房里那次尴尬的单独谈话之外，我和露丝其实并没有说过多少话。"
"至少在这方面我不是孤身一人。我其他的同学也都没跟露丝说过话。"
"她们似乎都避着她，而我想我知道是为什么。"
"她像刺猬一样浑身是刺，想从她嘴里多套出几句话来都难。"
"不过她现在正跟我说话呢。这总该算点什么吧？"
"她也许还没把我当成朋友，但我想她并不讨厌我。"
Marcel u neutral "那我希望我们以后能多谈一谈。"
show luce neutral2 with dissolve
Luce "你为什么愿意和我这样一个女孩说话？别人都不愿意。"
Marcel "也许正因为如此吧。我不喜欢总看见你一个人独自坐着。"
show luce frown2 with dissolve
Luce "所以，你是在可怜我？"
Marcel u huh "有一点，也许……？"
Marcel u sad "在杜布瓦夫人那样对你之后，不怜惜你都难。不过我不明白，这有什么不好的。"
show luce neutral2 with dissolve
Luce "这就是你想替我出头的原因吗？"
Marcel u neutral "是那样，也因为这一切太不公平了。"
Marcel u frown "我知道那只蟾蜍不是你带进教室的。谁都清楚。我敢说就连诺艾米也知道。她只是把罪名推到你头上，因为她知道杜布瓦夫人会大发雷霆。"
Marcel "她大概觉得那样会很滑稽吧。"
show luce sigh2 with dissolve
Luce "这……听起来倒也不是没可能。比起真相，诺艾米更在乎场面热闹。"
Marcel "可这实在不公平……"
show luce neutral2 with dissolve
Luce "我说过了，人生本就不公平。"
show luce frown2 with dissolve
Luce "况且。"
"露丝皱起了眉。"
Luce "既然你这么在意公平，为什么又要替我承受罪责呢？"
Luce "很显然，你根本不是蟾蜍事件背后的人。"
Marcel u huh "你是怎么知道的？"
show luce sigh2 with dissolve
Luce "拜托。"
"露丝翻了个白眼。"
Luce "别小看我。我可不是蠢货。"
show luce frown2 with dissolve
Luce "我知道你不是那种会玩这种把戏的人。你是个好女孩，好得过头了。你也许会坐在克洛蒂娜身边，可她还没本事把你带坏。"
Luce "你试图把自己推举成罪魁祸首，说真的，那实在好笑。"
Marcel u ehe "也许你说得对。我确实没把自己的盘算过好，啊哈哈……"
show luce neutral2 with dissolve
Luce "不过，你当时说我不该受责备时，口气倒是相当笃定。"
Marcel u shock "我、我当然确定！我知道你不会做这么孩子气的事！"
Luce "你是怎么知道的？为什么这么信得过我？"
Marcel u frown "因为我知道真正的元凶是谁。"
show luce huh2 with dissolve
Luce "哦……？"
"露丝挑了挑眉毛。她看起来被勾起了兴致。"
show luce neutral2 with dissolve
Luce "是谁？"
Marcel u sigh "当然是克洛蒂娜。"
show luce frown2 with dissolve
Luce "哦……原来如此。我早该想到的。"
Marcel u neutral "我想她经常开这种玩笑吧？"
show luce sigh2 with dissolve
Luce "是相当经常。"
Marcel u frown "那你是不是总替她背黑锅？"
show luce neutral2 with dissolve
Luce "通常不是。"
Luce "克洛蒂娜更爱去惹布吕吉埃夫人，而夫人对她是咱们班真正捣蛋鬼这一点，心里可清楚得很。"
Marcel u huh "她害你惹上麻烦，你不生她的气吗？"
show luce frown2 with dissolve
Luce "我不是不能生气，只是生气也改变不了什么。没有意义。"
Luce "我也不信克洛蒂娜是想牵连我。她并不恶毒——至少不全是。她只是没动脑子。"
Marcel u frown "要是当初我{i}再多{/i}想想，也许那时候就能帮上你了。"
show luce smile2 with dissolve
Luce "嗯。你也尽力了。"
"露丝笑了。"
Luce "不过你可真是个蹩脚的骗子，玛塞尔。"
Marcel sigh u "求求你，别提了……"
Luce "不过你的心意我心领了。你想为我辩护，这份好意真的很难得。"
show luce neutral2 with dissolve
Luce "只是往后你要是再撒谎，记得编得可信一些。"
Marcel u ehe "我会尽力……"
show luce huh2 with dissolve
Luce "你知道吗？"
"露丝朝我眨了眨眼。"
Luce "听你这么说，我相信你。我觉得你说真心想照看我，是真的，尽管这确实有些古怪。"
show luce neutral2 with dissolve
Luce "我实在不习惯别人对我这样温柔……"
show luce happy2 with dissolve
Luce "不过，那确实让我开心，我想。"
show luce smile2 with dissolve
Luce "我还说不上能不能称你为朋友，但你是个体贴的女孩。"
Luce "你半点也没有我听说城里女孩那样傲慢自负。"
Marcel u sigh "我倒不觉得自己特别傲慢，不过我确实相当无能。"
show luce neutral2 with dissolve
Luce "我不介意。无能总好过残忍或者睚眦必报。"
Luce "我的父母就挺无能的，可他们都是好人。我很爱他们。"
show luce sigh2 with dissolve
"露丝顿了一下。她回头看了看那仍在滴着水的水井，叹了口气。"
Luce "我真希望还能和他们住在一起……"
Marcel u sad "露丝……"
"我不知道该说什么来安慰她。我对露丝还不够了解，而我想说的话又怎么也说不出口。"
"我本可以告诉露丝，我明白她的感受：我思念远在巴黎的母亲，我为父亲担忧，我虽恨他拆散了这个家，却还是放不下他……"
"可这些话我一句也不能说。"
show luce neutral2 with dissolve
"我不能让她知道我父亲是谁。那会毁了我这一场伪装。"
"我所能做的，反倒只能是说些空洞的套话来敷衍她。"
"我不禁想，如果我不能对别人完全坦诚，那要交到朋友可真是难事——可话说回来，要是我真的坦诚相待，我最初就不会遇见露丝，这会儿我们也就不会在一起说话了。"
"而这，最起码，是一件值得庆幸的事。"
"我真的很庆幸能遇见她。"

stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
play music "bgm/Casual_Day.ogg" fadein 1.0
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  10月14日{vspace=1}  殉道者露丝") )
$ renpy.pause(0.8)
scene classroom:
    size (1920, 1080) crop (0, 40, 1440, 810)
show claudine annoyed2:
    xpos 0.30 xanchor 0.5 ypos 0.55 yanchor 0.5
with wiperight_slow
window show dissolve

Claudine "唉，真不敢相信！"
"那天稍晚，最后一节课结束后，我发现自己在迅速空下来的教室里跟克洛蒂娜说着话。"
"我们是最后留下的两个人，这对克洛蒂娜来说可不多见。"
"往常钟声一响，克洛蒂娜总是头一个冲出教室的人，急着要去看她心爱的那只猫，让娜特。"
"可今天却不一样了。"
"教室里正流传着关于露丝受杜布瓦夫人严厉惩戒的闲话。"
"人们——尤其是诺艾米——悄悄议论着、嘟囔着，一整堂缝纫课里都不停地伸长脖子去瞟露丝几眼。"
"克洛蒂娜想必也看到了露丝那双手的惨状，因为她整个下午都出奇地安静。"
"等到终于放学时，克洛蒂娜看向我，表情带着一丝哀怨，开口说道……"
show claudine sad2 with dissolve
Claudine "哦，玛塞尔，我闯了这么大的祸！"
Claudine "我真没想到杜布瓦夫人会怪到露丝头上，你知道的。这念头我压根就没动过！"
Marcel neutral u "我相信你，可也许你不该那么急着去实施你那缺德的诡计。"
Marcel sigh u "我还以为杜布瓦夫人什么事都怪露丝，这是人尽皆知的事。"
Claudine "啊，是啊，这倒确实没错。"
show claudine shock2 with dissolve
Claudine "可我没想到她下得了手把露丝打得那么狠！"
show claudine neutral2 with dissolve
Claudine "不管她怎么罚我，我总是能说会道地脱身。没人把杜布瓦夫人当回事，所以我就想……"
show claudine sad2 with dissolve
"克洛蒂娜叹了口气。"
Claudine "现在我觉得愧疚了。"
Marcel frown u "你也许应该愧疚。要不是你把那只蟾蜍带进学校，这整件事本来可以避免。"
show claudine shock2 with dissolve
Claudine "喂！我可没想闹出这么大动静！"
"我意味深长地久久注视着克洛蒂娜。克洛蒂娜也毫不眨眼地迎着我的目光，好一会儿，才终于移开视线。"
show claudine sigh2 with dissolve
Claudine "好啦，好啦。也许我{i}确实{/i}想闹出点动静来——可这能怪我吗？"
show claudine shock2 with dissolve
Claudine "英语课太无聊了，我的人生需要一点刺激！"
Marcel "可你本该想到受责罚的会是露丝，只要你肯停下来想一想。"
show claudine annoyed2 with dissolve
Claudine "呃……"
"克洛蒂娜的肩膀垮了下来。"
show claudine sad2 with dissolve
Claudine "也许我{i}这次{/i}是做得太过分了。"
Claudine "我不介意挨骂，可我不喜欢别人替我的过错背黑锅。"
"至少她还有一点正义感……"
show claudine neutral2 with dissolve
Claudine "我是说，那就把什么都变得没意思了！"
Claudine "我可是费了好大劲才找到那只蟾蜍的，跟你说，那可不是件容易事！这功劳该由我一个人来领才对！"
show claudine annoyed2 with dissolve
Claudine "我可不想让小露丝抢了我的风头！"
"……也许并不。"
Marcel neutral u "下次，你该把你的恶作剧留到布吕吉埃夫人的课堂上去。至少她毫不费力就能查出真正的元凶是谁。"
show claudine neutral2 with dissolve
Claudine "她是个精明的女人，尽管上了年纪。她那双眼睛可跟鹰一样锐利！"
Claudine "要说谁配当我的宿敌，那就是她！杜布瓦夫人跟她还差得远呢！"
show claudine heh2 with dissolve
Claudine "让布吕吉埃夫人尖叫起来，那可真叫人痛快！哦吼吼吼！"
Marcel frown u "你不会又在打什么主意吧？"
show claudine neutral2 with dissolve
Claudine "谁，{i}我{/i}吗？"
show claudine heh2 with dissolve
"克洛蒂娜指了指自己，摆出一副无辜的样子，随后笑了出来，摇了摇头。"
Claudine "当然没有！"
Marcel frown u "……好吧。"
"不管克洛蒂娜怎么说，我都没法完全信服……"
show claudine neutral2 with dissolve
Claudine "不过我不会再捉弄杜布瓦夫人了……{w}至少暂时不动。她显然应付不来。"
show claudine sad2 with dissolve
Claudine "可怜的小露丝已经够受罪了，我不该再火上浇油。"
Marcel neutral u "你真觉得她过得很苦吗？"
show claudine neutral2 with dissolve
Claudine "我想是吧。她又安静又阴郁又沉默寡言，我倒更难相信她不是那样。"
Claudine "还有她读的那些沉闷的书，都是些死去的老诗人写的！"
Marcel neutral u "马拉美？"
show claudine shock2 with dissolve
Claudine "还有别的呢！"
"克洛蒂娜哼了一声。"
show claudine neutral2 with dissolve
Claudine "她读的书全都那么感伤。难怪她看起来一副苦相！"
show claudine laugh2 with dissolve
Claudine "她该找个时间让我给她推荐几本书。我正知道什么能让她开心起来……"
show claudine neutral2 with dissolve
Claudine "至少我但愿自己知道，可我跟露丝其实一点都不熟。我几乎没跟她说过话。"
Marcel "那倒出人意料。你不是跟谁都说话吗？"
show claudine annoyed2 with dissolve
Claudine "哦，我跟她说过话，别误会，可我们从来没有好好聊过。她从不回话。她太情绪化了！"
show claudine shock2 with dissolve
Claudine "哦，要是她是个男孩子就好了。那这学校的姑娘们准会迷上她！"
Marcel "您真的这么觉得吗？"
show claudine smile2 with dissolve
Claudine "当然。这儿的姑娘对那种强壮又沉默的类型简直发疯。男人总在他们闭嘴的时候最迷人……"
show claudine neutral2 with dissolve
Claudine "可像可怜的小露丝这样独来独往的姑娘，却常常被扣上傲慢或阴沉的名声。"
Claudine "这大概就是诺艾米告发露丝的原因。她知道没人会替她出头。"
show claudine sad2 with dissolve
Claudine "杜布瓦夫人不太喜欢露丝，班上的其他人也是一样。"
Marcel sad u "她没在被欺负吧？"
show claudine neutral2 with dissolve
Claudine "我倒不会把它叫作欺凌，可她确实被冷落了。露丝不跟任何人说话，所以也没人试着跟她说话。也许他们都觉得她已经无可救药了……？"
show claudine shock2 with dissolve
Claudine "也许露丝更喜欢这样，我不得而知，可在我眼里这总归有点可悲——而且也太没必要了！"
Claudine "她也许读很多无聊的书，可她有张相当甜美的脸！"
show claudine neutral2 with dissolve
"克洛蒂娜靠在椅背上，翘起一条腿，陷入了沉思。"
Claudine "我以前试过跟她交朋友，可我最好的努力都很快被一口回绝了。"
show claudine annoyed2 with dissolve
Claudine "我早就不再做那个在小露丝面前当好心人的尝试了。既然她那么明显地不感兴趣，我何必费劲去搭话。"
show claudine smile2 with dissolve
Claudine "不过露丝似乎真的挺喜欢你。"
Marcel shockblush u "你、你真这么觉得……？"
show claudine laugh2 with dissolve
Claudine "她一定是的。你不是跟她好好聊过一回吗？"
Claudine "诺艾米说她看见你们俩站在水泵旁，亲密得像同伙一样！"
Marcel shy u "我不知道该不该说有那么夸张……不过露丝确实跟我说了会儿话，是的。"
show claudine smile2 with dissolve
Claudine "在你看来那也许只是‘一点点’，我亲爱的玛塞尔，可要是搁在露丝身上，那简直是了不起的进展！"
Marcel sad u "不过她说她不把我当朋友。"
show claudine neutral2 with dissolve
Claudine "可她也没排除将来有那么一天吧？"
Marcel neutral u "嗯，那倒没有……"
show claudine laugh2 with dissolve
Claudine "哦，天哪！那可{i}真{/i}是了不得！也许你和小露丝真的会成为朋友！我简直难以想象！"
show claudine smile2 with dissolve
Claudine "我都不信露丝在这读了三年书，竟能交成一个朋友！"
Marcel shock u "一个都没有……？"
Claudine "一个都没有！至少在你来之前是这样！"
show claudine heh2 with dissolve
Claudine "你做得真好！继续加油！"
"克洛蒂娜咧嘴一笑，然后伸出手揉乱了我的头顶。她那尖利的指甲刮过我的头皮，那种滋味实在称不上好受。"
"我倒抽一口气，然后把她推开了。"
Marcel sad u "别这样。你会弄坏我头发的。"
"我可是花了数不清的工夫学会编辫子的，怎么能让克洛蒂娜毁了我的一番心血。"
Marcel frown u "而且我从不知道你这么关心露丝。我以为你没那么无私。"
show claudine shock2 at bounce
Claudine "多无情呀！我关心这所学校里所有的学生，我不希望他们当中任何一个人不快乐！"
Claudine "那该是多么可惜的浪费，因为学生时代——我爸爸就常这么说——本该是少女一生中最幸福的时光！"
"最快乐的时光，嗯？"
"我的母亲和姨母也这样对我说过。"
"以前住在巴黎时，我对此并不太相信，但如今我身在米延，或许那也并非不可能。我也只能这样期望了。"
show claudine smile2 with dissolve
Claudine "要是咱们班有谁能成为露丝的朋友，我想那就是你了。加油！别让我失望，否则我会非常、非常失望的！"
"对于这个变化，克洛蒂娜听起来足够热切，但我的心中却多了几分犹豫。"
"我当真能让露丝走出她那冰冷、自我封闭的沉默吗？"
"听起来这是不小的责任，但我仍想尽我所能。"
"我不愿任何人再像我从前那样不幸。"

stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene sky g with clockwipe
$ renpy.pause(0.5)
show overlay2
show message17 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message17
hide logo2
hide overlay2
with datetrans2

$ renpy.pause(0.3)
play ambience "sfx/birds.ogg" fadein 1.0
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  10月19日{vspace=1}  空虚的时光") )
scene sky with dissolve
window show dissolve

"在米延的新学校里，日子一天天过去。树叶渐渐枯黄，从枝头飘落，风也开始转凉。"
"每到夜里，当我试图入睡时，总会发现自己裹在被子里瑟瑟发抖。我不得不蜷缩成一团，好让脚趾不致从被单下露出来。"
"不过，既然日子过得如此惬意，这也算不上什么要紧的事。"
"在米延，时间似乎比在城里过得慢一些。也许是因为这里的一切都静谧得多。"
"这里没有繁忙的道路，也没有拥挤的街巷；只有绵延的丘陵、树木与湖泊，尽收眼底。"
"无论天气多么寒冷，鸟儿总在林间啁啾；一些更顽强的花朵，仍在湖畔倔强地生长。"
"这里的空气闻起来比在巴黎时更为清新，而风，纵然寒冷，却似乎能让我焕然一新。"
"我这一生还不曾如此真切地觉得自己活着，也不曾如此真切地觉得那是我自己。"
"唯一的问题是，我仍不完全知道自己是谁，或者说“自我”究竟意味着什么。以女孩的身份生活，用着一个与我的名字几乎相同、却又并不相同的名字，让我的每一次交往都蒙上一层微妙的虚幻感。"
"一切都好像有点不对劲……"
"但即便心中困惑，时间依旧滴答流逝，一如它历来那样，无可避免。"

stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene classroom g with clockwipe
$ renpy.pause(0.5)
show overlay2
show message14 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message14
hide logo2
hide overlay2
with datetrans2

$ renpy.pause(0.3)
play ambience "sfx/wind.ogg" fadein 1.0
play music "bgm/Classroom.ogg" fadein 1.0
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  10月28日{vspace=1}  少了点什么") )
scene classroom with dissolve
window show dissolve

"事情发生在十月底，也就是教室里那只蟾蜍事件的两周之后。"
"我正坐在教室的书桌前，等候远处教堂的钟声响起。"
"教室里变得十分寒冷。风把窗玻璃刮得格格作响，像是无形鬼魂的手在摇晃它们；寒意顺着地板和天花板的缝隙溜进来。"
"这栋校舍已有些年头，吱呀作响的地板和漏水的屋顶无不显露着它的岁数。"
"尽管教室后方生着熊熊炉火，却不足以驱散侵袭我们的深秋寒意。我们这些同学尽管有火，仍不住地打颤。"

stop ambience fadeout 3.0
play sound "sfx/footsteps3.ogg" fadein 0.5

show al frown:
    xpos -0.10 ypos 0.5 xanchor 0.5 yanchor 0.5
    ease 1.5 xpos 0.50

$ renpy.pause(0.8)

stop sound fadeout 0.5

Bru "好了，姑娘们。安静下来。"
"布吕吉埃夫人走进教室时下达了这道命令，其实并无必要。今天几乎没人说话，我想她们是想保存体力。"
Bru "好了，我来点名吧。"
"布吕吉埃夫人按字母顺序点名班上的女孩们。她念到我们的名字时，我们便顺从地应声，像椋鸟一样叽叽喳喳地作答。"
Bru "拉尔克？"
Mirabel shock "到、到，夫人！"
Bru "拉罗什？"
Claudine u smile "到。"
Bru "梅西耶？"
Noémie smile "到。"
Bru "雷诺？"
Marcel neutral u "到，夫人。"
Bru "圣科尔？"
Celine sigh "是，夫人。"
"就这样一一点下去，直到布吕吉埃夫人念到名单上的最后一个名字。"
Bru "瓦莱特？"
"没有应答。"
Bru "瓦莱特？"
"布吕吉埃夫人又喊了一遍。"
Bru "露丝·瓦莱特？"
"依旧没有回应。"

show image "border" onlayer border
scene classroom:
    size (1920, 1080) crop (0, 80, 1440, 810)
with wipeleft_slow

"露丝常坐的那扇窗边的座位空着。她不在这里。"
"露丝向来不会上课迟到。她住在学校的宿舍里，不像克洛蒂娜、米拉贝尔那样的米延本地学生，家离校本部不过短短五分钟的路程。"
"露丝实在没有迟到的理由。她看起来也不像是会睡过头的那种人。"
"她该不会是生病了吧？"
"露丝个头那么娇小，而且近来确实很冷。"
"连我自己的寝室都冷得厉害，女孩们的宿舍条件想来也好不到哪里去。"
"万一她是染上咳嗽——更糟的，是流感呢？"
"那时露丝会怎样呢？"

hide image "border" onlayer border
scene classroom
show al neutral at center
with wiperight_slow

"然而，布吕吉埃夫人似乎并不太担心露丝的缺席。她只是咂了咂嘴，摇了摇头。"
Bru "我想她没在这儿吧……"
"布吕吉埃夫人在点名册上把露丝记作缺席，然后将其放到一旁。"
Bru "好了，同学们。今天，我们开始上地理课。"
"教室里响起一阵低低的哀叹。"
"至少，我的同学们还有力气表达她们对地理课的不满。"
show al frown with dissolve
Bru "好了，好了，别这样。你们这些姑娘应该庆幸自己有开阔眼界的机会。"
Bru "许多像你们这般年纪的女孩没有机会上学读书。她们不得不在农场上帮父母干活，或是到城里当女佣。你们得到了接受良好教育的机会，所以至少也该做出点感恩的样子——"
show al annoyed with dissolve
Bru "没错，说的就是你，克洛蒂娜。别冲我翻白眼了，年轻的小姐。"
Claudine annoyed u "天哪！真是个大唠叨鬼！"
"克洛蒂娜撅起嘴，往椅背上一靠，但这便是她全部的任性回应了。"
"我想，就连克洛蒂娜的兴致也被这寒天冷雨磨去了几分。"
show al neutral with dissolve
Bru "那么，姑娘们，把练习册翻开吧——"

stop music fadeout 0.5
play sound "sfx/door.ogg"

"然而就在那时，传来一声重重的闷响。"

play ambience "sfx/footsteps3.ogg" fadein 0.5
scene classroom:
    size (1920, 1080) crop (240, 40, 1440, 810)
show luce neutral2:
    xpos -0.10 ypos 0.5 xanchor 0.5 yanchor 0.5
    ease 2.5 xpos 0.35
with wipeleft_slow

$ renpy.pause(1.2)
stop ambience fadeout 1.0

"教室的门被推开，露丝就站在那里。"
"见她无恙，我松了口气……{w}可她真的无恙吗？"

play music "bgm/Mysterious.ogg" fadein 1.5

"露丝并非病到不能上课的地步，但她看起来实在称不上健康。"
"她的肤色比往常更苍白——近乎透明——双颊却因奔波而泛着红晕。"
"她那头金黄短发显得凌乱不堪。像豪猪背上的硬刺一样竖着，即便她用手去拨，也不肯服帖地垂下。"
"她的校服也皱得不成样子。衣领歪斜着，而且她没穿袜子。双腿完全暴露在寒风之中——两条百合般白皙的细茎，瘦弱得仿佛撑不起她整个身子。"
"她穿着规定的校鞋（黑色，配着一条端端正正的搭扣带子以固定），腿上却光着。"
"她为什么不穿袜子呢？是想表明什么态度吗？也许她是想叫布吕吉埃夫人难堪——但，不，那像是克洛蒂娜会做的事；何况就连克洛蒂娜也不会蠢到在外头这么冷的时候不穿袜子。"
"露丝一定是出了什么事，可究竟是什么？"

scene classroom
show al annoyed at right2
show luce neutral at left2
with wiperight_slow

Bru "啊，瓦莱特小姐。你可算{i}终于{/i}肯来加入我们了，真是难得。"
show luce sigh with dissolve
Luce "是，嗯……对不起，我迟到了……"
Bru "你可不是只迟了一点点。铃声响过之后五分钟，你才走进我的教室。"
Bru "你有什么借口？"
show luce neutral with dissolve
Luce "我……我……"
show al frown with dissolve
Bru "说啊，姑娘。你这副糟糕的行为到底是什么意思？你的衣着也实在不像话，看看你那光着的两条腿！你的袜子呢？"
show luce sad with dissolve
Luce "我……我只是忘了穿……"
show al annoyed with dissolve
Bru "你忘了穿？"
show luce neutral with dissolve
Luce "是的……"
Luce "我起晚了，又找不到袜子。我没有别的借口。非常抱歉。"
"我的一些同学——想必是与露丝同寝的寄宿生——开始好奇地窃窃私语。"
Cla "可是露丝并没有起晚。"
Claa "她总是比我先起床。"
Cla "那她为什么不早点来教室？"
Cla "吃早餐的时候我也没有看到她。"
Claaa "我好像看到杜布瓦夫人把她叫到一边去了。她说想跟她谈一谈。"
Cla "谈一谈……？"
Claa "露丝又惹祸了吗？"
Claaa "也许她是在受罚呢！"
show al mad with dissolve
Bru "姑娘们，请安静。够了。"
play sound "sfx/slap.ogg"
with vpunch
"布吕吉埃夫人一掌拍在讲台上。那沉闷的声响在整个教室里回荡，宣告着寂静的来临。"
show al frown with dissolve
Bru "要是我对无聊的闲言碎语感兴趣，我会问你们的。好了，露丝。"
"布吕吉埃夫人重新转向露丝，眯起了眼睛。"
Bru "你说，今天早上尽管天寒地冻，你还是没有穿袜子，是因为不想上课迟到？"
show luce neutral with dissolve
"露丝点了点头。"
show al neutral with dissolve
Bru "嗯，我想你努力准时赶到这里的用心值得称赞，尽管你还是没达到目标。"
show al annoyed with dissolve
Bru "尽管如此，我还是不能原谅你穿成那样来上我的课。"
show al frown with dissolve
Bru "你不是流民，露丝。你是我学校的学生，你应该为此感到自豪。"
show al annoyed with dissolve
Bru "在你进来打断我之前，我正在告诉我的学生们，许多像你这么大的女孩甚至连上学的机会都没有。"
Bru "她们必须靠做工来挣得身上的衣服和桌上的食物。"
Bru "你处于一个极其优越的位置。我不允许你玷污它！"
show al frown with dissolve
Bru "我绝不会让一个光着腿的女孩进我的教室，除非地狱结冰！太不成体统了！"
Bru "以你现在的样子，你只会分散其他姑娘的注意力！"
"我的同学们（以诺艾米为首）又开始了窃窃私语。"
Noémie smile "可你瞧瞧她那两条腿！"
Claa "她的袜子去哪儿了？"
Cla "也许她觉得穿袜子配不上她呢！"
Noémie "我{i}绝不{/i}会那样招摇地露出大腿；在这种天气里更不会！"
Claaa "她的皮肤会冻得发青的！"
Claa "她的脚趾会冻掉的！"
Noémie "真是个荡妇！"
show luce sigh with dissolve
"同学们那恶意的窃笑越来越响。它不安地蔓延开来，传遍整个教室，直到几乎所有的女孩都笑了起来——就连米拉贝尔也不例外，尽管她似乎压根不明白众人究竟在笑什么。"
"露丝没有任何反应。她只是继续站在那里，低垂着头。"
"我想她一定是习惯了。"
"她时常被杜布瓦夫人单独挑出来，被全班戏弄于她而言想必不过是沧海一粟。"
"可这仍然让我耿耿于怀。这不公平……！"

show al annoyed
show luce neutral
with dissolve

Bru "姑娘们，真是的。耍嘴皮子或许能帮你冬天取暖，但那可不怎么像个淑女。哎呀，你们简直快跟露丝一样糟了！"
show al neutral with dissolve
Bru "你看，明白了吧？"
"布吕吉埃夫人蹙眉看着露丝。"
Bru "正如我所说的。你呆在这教室里，只会分散别人的注意力。"
Bru "你没穿袜子，我不能让你坐下。"
show al frown with dissolve
Bru "我要你在剩下的课时里到操场上去站着——而且你最好给我站直。我不允许你坐下、靠着，或者倚在什么东西上！你听明白了吗？"
Bru "这本来应当是惩罚！"
show luce frown with dissolve
"露丝抬起头。她半睁着双眼望向布吕吉埃夫人。"
"短暂的停顿之后……"
show luce sigh with dissolve
Luce "是，夫人。"
"露丝低下头，彻底而完全地顺从了。"
show luce neutral with dissolve
"露丝那种自卑维诺的姿态，我再熟悉不过。我从前也和她一模一样；被人责骂、被人嘲弄，却无法为自己辩护。"
"我深知那毫无意义。"
"为自己挺身而出，只会让事情变得更糟。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
play music "bgm/Sad.ogg" fadein 1.0
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  10月28日{vspace=1}  失宠的露丝") )
scene yard
show luce frown:
    xpos 0.35 xanchor 0.5
with wiperight_slow
window show dissolve

"午餐开始时，我没有和同学们一同前往食堂。相反，我留在了校园里。"
"露丝仍站在那棵橡树的树荫下，羞愧地低着头。她那白皙的双腿在绿草衬托下格外醒目，草地上散落着星星点点的秋叶。"
"中级班的女孩们经过时，都停下脚步，好奇地多看露丝几眼，但露丝并没有以同样的目光回敬。"
"她仍然一动不动地站着，双臂僵硬地垂在身侧。"
"她没听见钟声响吗？"

scene yard:
    size (1920, 1080) crop (100, 40, 1440, 810)
show luce frown2:
    xpos 0.35 xanchor 0.5
with dissolve

Marcel u shy "打扰一下，露丝……？"
"我迟疑地走向她。"
Marcel u neutral "课暂时结束了。我想你大概可以走了。"
"露丝没有看我。她仍旧凝视着地面——又或许，从她那毫无焦点的眼神看来，她只是在望着虚空。"
"有那么一瞬间，我担心露丝根本懒得回答，可是……"
show luce sigh2 with dissolve
Luce "……我知道。"
"她轻声说道。"
Luce "我听到铃声了。"
"原来，她并没有无视我。"
"至少这让我松了口气，可露丝那平板而毫无感情的回应，着实令人在意。"
"她的声音如此平淡，仿佛在背诵台词（而且背得很糟）。"
Marcel u huh "你不想去吃午饭吗？既然你起晚了，我猜你大概也没吃早餐。"
Marcel "你不饿吗？"
show luce frown2 with dissolve
Luce "我当然饿。跟其他人一样，我需要进食才能活下去。"
Marcel "那你为什么还站在外面？"
show luce sigh2 with dissolve
Luce "……因为我没有别的地方可去。"
Marcel "你这是什么意思？"
show luce neutral2 with dissolve
Luce "没穿袜子，我不能进餐厅。我只是又会被训斥一顿，别的姑娘还会对我指指点点、笑话我。"
Marcel "我还以为你不在乎别人怎么看你呢。"
show luce huh2 with dissolve
Luce "我不在乎。一般情况下是这样。不过，要是那样会让我成为众矢之的，我就在乎了。"
Luce "我不想惹上更多的麻烦。"
Marcel "那你怎么不回宿舍找一双袜子穿上呢？"
"可话一出口，我便知道自己说错了话。"
show luce frown2 with dissolve
Luce "玛塞尔。"
"露丝怒视着我，双手攥成了拳头。"
"我想我该庆幸能引发她的情绪反应，但愤怒并不是我所期待的那种情绪。"
"我这张嘴真是会说话，对女人更是如此。"
Luce "你真是个白痴吗？"
Marcel sad u "嗯……我想不是吧。我不是班里最聪明的女孩，但我觉得我也不算太差——"
show luce sigh2 with dissolve
Luce "我不是在说你的成绩，笨蛋。"
Marcel shock u "那……那你指的又是什么呢……？"
show luce frown2 with dissolve
Luce "我真的要为你把话说得那么明白吗？"
"露丝嗤笑了一声。"
Luce "如果我有多余的一双袜子，我刚才就穿上了。"
Luce "我不喜欢让自己出丑。我早知道，要是光着腿进教室，我会惹上麻烦的。"
show luce sigh2 with dissolve
Luce "我这么做是因为别无选择。要么那样，要么干脆连来都不来。"
Marcel "那么，这是不是说你没有袜子？"
show luce neutral2 with dissolve
Luce "正是如此。"
Marcel neutral u "可它们到底怎么了？是破了个洞吗？还是……"
"露丝和其他女孩一起住在宿舍里。说不定是有人无意中错拿了露丝的袜子……{w}又或者是故意藏了起来，当作一个残忍的玩笑。"
Marcel sad u "是被谁拿走了吗？"
show luce sad2 with dissolve
Luce "是的。"
"露丝再次垂下头，方才那片刻的怒气已然熄灭，她叹了口气。"
show luce sigh2 with dissolve
Luce "有人偷走了它们。"
Marcel "你看到是谁了吗？"
show luce neutral2 with dissolve
Luce "看到了。就在别人都没注意的时候，他们当着我的面把袜子拿走了。"
Marcel huh u "那你为什么不把这件事告诉布吕吉埃夫人呢？！"
show luce sad2 with dissolve
Luce "……我不能说。"
Marcel sad u "为什么？"
Luce "我觉得她不会相信我的……"
show luce sigh2 with dissolve
Luce "而且，就算她信了，那也只会让我的处境更加复杂。"
Luce "不值得那么麻烦。"
Marcel shock u "可是，如果你没有袜子，在可预见的将来你就上不了任何课了！没有袜子，布吕吉埃夫人不会让你进教室！"
show luce neutral2 with dissolve
Luce "看起来确实如此，是啊。"
Marcel "那你打算怎么办？"
Luce "放学后我得去村里买一双新的。"
show luce sad2 with dissolve
Luce "我没有多少钱，但应该还够应付这笔开销……"
Luce "至少，我希望够用。"
show luce sigh2 with dissolve
Marcel sad u "可你今天剩下的时间里不就上不了任何课了？"
Luce "不觉得。"
Marcel shock u "也不能去餐厅？"
show luce neutral2 with dissolve
"露丝摇了摇头。"
Marcel frown u "可这不对啊！你在为一件不是你的错的事受罚！"
show luce sad2 with dissolve
Luce "我已经习惯了。这真的只是件小小的不便。"
Marcel "你怎么能把一整天没法吃东西叫作‘小小的不便’呢？"
show luce neutral2 with dissolve
Luce "我以前也挨过饿。不要紧。反正我吃得也不多。"
Marcel huh u "也许你应该多吃点。你瘦得像根树枝似的……"

stop music fadeout 1.0

show luce smirk2 with dissolve
Luce "呵……"

play music "bgm/Friendship.ogg" fadein 1.0

"一丝微笑浮上露丝的唇间。就微笑而言，它看来并不算多真诚，但比起她那紧抿双唇的愁容，已是令人眼前一亮的转变。"
Luce "现在你听起来像我母亲。"
Marcel neutral u "这是好事吗？"
show luce neutral2 with dissolve
Luce "我倒想知道……"
Luce "我母亲也喜欢多管闲事。"
show luce frown2 with dissolve
Luce "你可真爱多管闲事。"
Marcel shock u "我、我{i}才不{/i}是多管闲事的人……！"
show luce smile2 with dissolve
Luce "……不过，尽管她有不少缺点，我还是很爱我的母亲。"
Marcel shockblush u "啊……"
show luce sigh2 with dissolve
"露丝那浅浅的笑意消失了。她叹了口气，噘起嘴唇，双臂环抱在胸前。"
Luce "……好冷。"
Marcel sad u "一点也不意外。没穿袜子肯定冻坏了！"
show luce neutral2 with dissolve
Luce "是啊，嗯，所以我才打算去买一双。"
Marcel neutral u "如果你买得起的话。"
Luce "如果我买得起的话，是啊。"
Marcel frown u "可你本不该非得给自己买双新的；要是你的旧袜子是被人偷走的。"
show luce huh2 with dissolve
Luce "我知道本不该如此，可我又能怎么办呢？我没有别的法子；除非有哪位好心的袜子精灵愿意施舍我一双不要钱的。"
Marcel huh u "你尽可嗤笑，可那也许并非全无可能。"
"露丝那番关于袜子仙子的说法，让我有了一个主意。"
"我的袜子已经多得用不完。布吕吉埃夫人在巴黎给我买了六双，全是又厚又好的料子。"
"我并不需要那么多袜子。"
"我若捐出一两双去作件好事，布吕吉埃夫人想必不会介意吧？"
Marcel smile u "露丝，不如你上我的房间来吧？我有件礼物想送给你。"
show luce neutral2 with dissolve
Luce "今天又不是我的生日。"
Marcel "我知道，那也不要紧。无论怎样我都想送你点东西。"
show luce frown2 with dissolve
Luce "我母亲叮嘱过我，不该独自进陌生人的房间。"
Marcel neutral u "我们哪算什么陌生人。我们都在同一个班待了快两个月了。"
Marcel huh u "况且，你不是说我很像你母亲吗？"
show luce neutral2 with dissolve
Luce "我原本只是说着玩的，可如今我开始觉得，那倒是个颇为敏锐的观察。"
show luce smile2 with dissolve
Luce "我母亲也固执得很。她从不接受别人说‘不’。"
"又是一丝微笑（尽管微小而迟疑）浮上了露丝的唇间。"
Luce "……那好吧。我想我可以去你房间待上三十分钟左右。至少总比在这冷风里站着强。"
Luce "好了，我们走吧？"
"露丝把头歪向一边，短短的头发在脸颊边轻轻飘动。"
show luce happy2 with dissolve
Luce "我正急着想看看你这间房，况且让一位女士久等也不礼貌。"
Marcel shockblush u "当、当然！跟我来就行。"
"不知为何，我感觉心在胸腔里怦怦直跳，像一只雏鸟的心那样。"
"是因为露丝的微笑吗？她那戏弄的神情？还是因为想到她来到我的房间——就我们两个人，独处一室？"
"我一无所知，但有一件事我很确定。"
"我一直觉得露丝很漂亮，但当她笑起来时，就显得更加动人了。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  10月28日{vspace=1}  袜子精灵") )
$ renpy.pause(0.8)
play music "bgm/Luce.ogg" fadein 1.5
scene marcel_room
show luce neutral:
    xpos 0.35 xanchor 0.5
with wiperight_slow
window show dissolve

Luce "你的房间很不错，玛塞尔。"
Marcel smile u "谢谢你。不过这其实算不上是我的。布吕吉埃夫人说这原本是你们那位旧音乐老师的。"
show luce huh with dissolve
Luce "啊。那就说得通了。"

show luce:
    ease 1.2 xpos 0.50

"露丝拢起裙摆，在床边坐了下来。"

play sound "sfx/fall.ogg"
scene marcel_room:
    size (1920, 1080) crop (480, 0, 1440, 810)
show luce neutral2:
    xpos 0.5 ypos 0.50 yanchor 0.5 xanchor 0.5
    ease 1.0 ypos 0.55
with wipedown_slow

"她在进我房间之前脱下了鞋子，露出光着的脚趾。我能看见它们在微微蜷动，白得近乎鬼魅。"
show luce sad2 with dissolve
Luce "不过你说这里冷，倒是对的。"
show luce sigh2 with dissolve
Luce "话又说回来，宿舍里也冷得很——不过别的女孩们能让那地方暖和起来。"
Marcel neutral u "到底有多少女孩睡在宿舍里？"
show luce neutral2 with dissolve
Luce "我和那些大一点的女孩睡一起。我们一共十五个人。"
Luce "小一些的女孩睡在她们自己的宿舍，就在我们下面那层。"
Marcel huh u "听起来，和别的女孩挤在一间房里睡会很有家的感觉。"
show luce frown2 with dissolve
Luce "我可不太这么觉得。"
"露丝的神情阴沉了下来。"
Luce "别的女孩整夜交头接耳、说闲话，我换衣服时她们还会冷嘲热讽。"
Marcel sad u "她们都说些什么？"
Luce "说我太矮太瘦，不像个十几岁的姑娘，还说我该到楼下跟小孩子们一起睡。"
show luce sigh2 with dissolve
Luce "这一切真是蠢透了……"
"露丝叹了口气，摇了摇头。"
show luce neutral2 with dissolve
Luce "我倒宁愿能睡在像这样的房间里，就我一个人，可那永远都不可能。我父母没有钱。"
Marcel ehe u "呃，嗯……我不知道这会不会有用，可你随时都可以来我的房间。"
show luce huh2 with dissolve
Luce "真的可以吗？"
Marcel u smile "当然。这里就只有我一个人，有时候难免有点孤单。要是有个人作伴，我会很高兴的。"
show luce neutral2 with dissolve
Luce "要是你当真不介意，我或许就不客气地接受这个提议了。"
Marcel u smile "你若肯来，我求之不得！好啦，至于那双袜子……"
play sound "sfx/drawer.ogg"
"我从抽屉里取出一两双袜子，然后递给了露丝。"
Marcel "给你。好好收着吧。"
show luce neutral2 with dissolve
Luce "这么说，你把我叫到这儿来，就是打的这个主意？"
"露丝眨了眨眼睛。"
Luce "你当真确定我可以拿走它们吗？"
Marcel "没关系。我既然开口相赠，就不会反悔。"
show luce huh2 with dissolve
Luce "你真是太好了，可这是你的袜子呀。你自己不穿吗？"
Marcel "我的袜子多得够穿。你也不必担心要还给我。你就留着吧。"
Luce "你说的是真的吗？！"
Marcel u ehe2 "当然。这毕竟是件礼物。若是袜子精灵还要讨回送出去的东西，那可就太失礼了。"
show luce smile2 with dissolve
Luce "哦……"
"露丝的眼神柔和下来。她接过我手中的袜子，指尖在上面轻轻抚过。"
Luce "这料子真好！"
Marcel u huh "是吗？"
show luce huh2 with dissolve
Luce "可不是嘛！我原来的袜子是用又便宜又扎人的莱尔棉线织的，可这一双好多了，还更厚实！"
Luce "一定很贵吧。"
Marcel u ehe2 "这可说不好。我对钱财的事一窍不通，嘿嘿。"
show luce frown2 with dissolve
"露丝扬了扬眉毛。"
Luce "这么说，你家是不是阔绰得很，根本不用为钱发愁？"
Marcel u ehe "差、差不多吧……"
show luce huh2 with dissolve
Luce "哎呀呀，你真是好福气。我想象不出有人会这样随手送人礼物。"
Luce "当你没有多少钱的时候，一双袜子就能价值连城。"
show luce neutral2 with dissolve
Luce "我还从未收到过这样的礼物。"
"露丝把那双丝袜放在膝上，任由它们静静躺在那里，袜子在彼此交叠；纯白醒目的色泽，衬着她黑色的裙子。"
Luce "我得把这双袜子看得紧些，否则一转眼就会被人从我抽屉里偷走。"
Marcel u huh "经常有人偷你的东西吗……？"
show luce frown2 with dissolve
Luce "这事儿可不能叫作‘人们’干的。往往只有一个人作案。"
Marcel u frown "那是谁？"
"我的胸口因愤怒而发紧。"
Marcel "是谁一直在拿走你的东西，害你日子这么难过？"
show luce neutral2 with dissolve
"露丝顿住了。她先用指尖抚过那双新袜子，仿佛在细细品味那触感，然后才开口回答。"
"她抬起头，与我目光相接，轻声说道……"
show luce sad2 with dissolve
Luce "杜布瓦夫人。"
Marcel u shock "杜布瓦夫人？"
show luce sigh2 with dissolve
Luce "没错。她总爱刁难我。从我还是个小女孩起，她就一直这样，已经好久了。"
Luce "她其实是我姐姐。"
"我沉默地注视着露丝好一会儿，嘴微微张开。"
"杜布瓦夫人一直拿走露丝的东西，而她竟然还是露丝的姐姐？"
"我一直觉得她们长得很像——同样的金发，同样的棕色眼睛——但我从没想过她们竟有亲缘关系！"
Marcel u huh "你们俩的姓氏不是不一样吗？"
show luce neutral2 with dissolve
"露丝含糊地点了点头。"
Luce "我姐姐几年前结过一次婚。那是在她当老师之前的事。"
Luce "她丈夫不是个好人。他嗜酒如命，还爱打架。"
show luce frown2 with dissolve
Luce "有一天，他喝得太多，然后……"
"露丝没有再多说，但我想我能明白这故事会如何收场。"
Marcel u frown "所以杜布瓦夫人保留了丈夫的姓氏？"
show luce neutral2 with dissolve
"露丝点了点头。"
Luce "我们姓氏不同，可我们是同一对父母生的。我们在同一屋檐下出生、长大，只不过她比我大上好几岁。"
Luce "我们确实是亲姐妹没错……"
show luce sigh2 with dissolve
Luce "可我不想让任何人知道这件事。"
Luce "我想她也不想让任何人知道。"
Marcel u huh "可你们既然是姐妹，她为什么老在班上罚你呢？"
show luce neutral2 with dissolve
Luce "我觉得她罚我，正是{i}因为{/i}我们是姐妹。"
show luce frown2 with dissolve
Luce "她若罚别的女孩会于心不安……{w}可是，因为我们是一起长大的，她对我‘管教’起来却毫不手软。"
Luce "我们两个都还是孩子时，她就常掐我、踢我、揪我头发。如今她已是大人，却仍旧这么干，我并不觉得意外。"
Marcel u frown "她还拿你的东西……？"
show luce neutral2 with dissolve
"露丝点了点头。"
Luce "她认为，既然我们是姐妹，我所有的东西都归她……"
show luce frown2 with dissolve
Luce "可当然，反过来就不行了。她绝不会让我用她的任何东西。"
Marcel u huh "可她为什么偏偏拿走你的袜子呢？"
show luce neutral2 with dissolve
Luce "她自己那双的脚跟破了个洞，她又不想再买新的。"
Luce "于是她就拿了我的，我本想争辩，她却掐我，还说要告诉父亲母亲我有多不听话。"
show luce huh2 with dissolve
Luce "你要知道，我姐姐觉得我欠她的。"
Luce "我父母太穷，供不起我上学。因为我姐姐在这里做事，布吕吉埃夫人才让我免费住在这儿。"
show luce neutral2 with dissolve
Luce "要不是她，我早就在我父母的农场里住着，帮他们喂鸡、接生小牛犊了……"
show luce sad2 with dissolve
Luce "可我常常想，我或许倒宁愿那样。"
show luce sigh2 with dissolve
"露丝幽幽地叹了口气，把双腿蜷到胸前。她光着的脚趾抵在我的床边，膝盖收近下巴，头枕在上面。"
Luce "我受够了这所学校。"
show luce neutral2 with dissolve
Luce "若不是因为我姐姐，这里本不至于这么糟；可她一有机会就要把我的日子搅得痛苦不堪。"
Marcel u neutral "你不能告诉别人吗？"
show luce frown2 with dissolve
Luce "这话我们说过。要是我说了，她会比以往任何时候都更狠地对待我。"
Luce "我所能做的，只有忍着。"
Marcel u sad "露丝……"
"我真希望能为她做点什么，可除了把袜子给她，再奉上一张（但愿是）友善的脸供她倾诉之外，我实在不知还能做什么。"
"也许我不该太过追问这些事。这情况很复杂，我多半只会把事情弄得更糟。"
"我能做的，只有试着给露丝一点值得期待的东西。比如……"
Marcel u neutral "露丝……我有个主意。"
show luce huh2 with dissolve
Luce "什么？"
Marcel u smile "离这儿不远有一片很美的湖。我有时喜欢去那里，因为那里让人放松。"
Marcel "我在想，要是这个周末你没什么别的事，我们或许可以一起去？"
Marcel "我们可以去野餐！"
Luce "野餐？"
Marcel u ehe2 "对。我从来没做过这样的事——更没和同学一起过——不过我想那应该会很有趣。"
Marcel u smile "我知道最近天气很冷，可要是能暖和一点，赶在冬天来临前去那里，该是件惬意的事。"
Marcel "你觉得呢？"
show luce neutral2 with dissolve
Luce "我……说不准。我想象不出你为什么会想和我一起去。我不会把一切都搞砸了吗？"
Marcel u shock "你当然不会！你为什么会这么说？"
show luce sad2 with dissolve
Luce "因为我似乎总是惹出麻烦；就是为此。"
show luce sigh2 with dissolve
Luce "我沉默寡言，郁郁寡欢，话也不多。有时候我觉得，光是活着我就能惹人厌。"
Marcel u neutral "你并没有惹我厌。"
show luce huhblush2 with dissolve
Luce "我、我没有？"
Marcel u smile "一点也不。一次都没有。"
show luce neutral2 with dissolve
Luce "好吧，既然你这么肯定……"
"露丝狐疑地看了我几秒……{w}直到一抹我从未见过的、明亮至极的笑容点亮了她的脸庞。"
show luce happy2 with dissolve
Luce "我很愿意。"

stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene sky g with clockwipe
$ renpy.pause(0.5)
show overlay2
show message15 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message15
hide logo2
hide overlay2
with datetrans2

$ renpy.pause(0.3)

scene sky with dissolve
play ambience "sfx/birds.ogg" fadein 1.0
play music "bgm/Energetic.ogg" fadein 1.0
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  10月31日{vspace=1}  甜如蜜糖") )
window show dissolve

"到了周末，我同露丝一起到村里，为我们的野餐买些吃食。"
"露丝告诉我，草莓是她最喜欢的食物之一，可时近冬日，任何一家店铺都找不到草莓。我们只好改买些全年都有的东西：肉馅派、羊角面包，还有甜点。"
"我把买来的东西放进我的藤篮里，挎在臂弯。"
"这些食物、篮子，还有野餐毯，都是用母亲每月月初寄给我的那笔可观的零花钱买来的。"
"我以前从没用过母亲的钱，所以倒也攒下了一些硬币。"
"买好了食物，露丝和我便朝湖边走去。"

play ambiencee "sfx/footsteps2.ogg" fadein 1.0
show image "border" onlayer border
scene lake:
    subpixel True
    size (1920, 1080) crop (0, 120, 1280, 720)
    linear 25.0 crop (350, 120, 1280, 720)
with wiperight_slow

"湖水一如我记忆中的那般平静安详。只有一阵轻柔的微风，拂动着水面。"
"我能看见几条鱼银色的脊背，在暗淡的日光下闪闪发亮。"
"我想，在夏天，这片湖想必是一处热闹的地方；蜻蜓贴着水面低飞，轻吻湖水，蝴蝶在空中翩跹，而青蛙正产下卵……"
"可眼下时令已晚，周围并没有多少昆虫或两栖动物。"
"湖边十分安静，惟有几声婉转的鸟鸣。"
"幸好今天比本周早些时候暖和些。太阳隔着云幕淡淡地照着。风也不怎么刺骨，不穿外套在外面散步也足够舒适。"

stop ambiencee fadeout 2.0
stop ambience fadeout 2.0
hide image "border" onlayer border
scene lake
show luce neutral at center
with wipeleft_slow

"露丝望着湖面出神了片刻，双臂松松地垂在身侧。"
"尽管今天周末，她却仍穿着校服。我想她大概没有别的衣裳可穿。"
"她睁大了眼睛，微启着唇，凝望着水面。"
"片刻过去了，她始终沉默着，然后……"
show luce huh with dissolve
Luce "哦，这里的确{i}是{/i}很美！"
Marcel c smile "确实很美，对吧？我早跟你说过了。"
show luce frown with dissolve
Luce "我知道你说过，可我原本还有些怀疑。"
Luce "我在Myennes住了很久，可我从来没觉得它有多么美。"
show luce sigh with dissolve
Luce "它实在太像一座监狱了。"
Marcel c neutral "这座湖可不像监狱，对吧……？"
"湖的三面都被树木环抱，把露丝和我围在湖畔；将我们困在属于我们自己的小小世界里。"
"若有人想逃离尘世和那些窥探的目光，这片湖正是绝佳的藏身之所……{w}但我想，它也可能让人感到像一间牢笼。"
"这里真的是{i}很{/i}安静；事实上，静得令人心悸。"
show luce smile with dissolve
"露丝却只是对我的问话回以微笑，摇了摇头。"
Luce "不，它不是监狱。它太美了，不像是监狱。"
Marcel "可你不喜欢Myennes的其余地方吗？"
show luce frown with dissolve
Luce "我以前不喜欢。"
Luce "我觉得这座村子小得可怜，又沉闷乏味，我也讨厌人人都认识彼此。"
Luce "我不喜欢人们在街上跟我打招呼，尤其讨厌不得不同样回礼。"
show luce sigh with dissolve
Luce "这一切我全都厌恶。"
Marcel "那现在呢？"
show luce neutral with dissolve
Luce "我也许会被说服，改变看法。"
show luce smile with dissolve
Luce "和你在一起时，Myennes看起来都更美了。"
Marcel shockblush c "啊……"
"我不由自主地脸颊泛红。跟露丝在一起时，这似乎发生得格外频繁，叫人不安。"
Marcel ehe c "呃，嗯……"
"我从露丝身上别开脸（看太久会让我的心怦怦直跳），把目光投向地面。"
Marcel smile c "那，我们这就准备吃吧？"
show luce happy with dissolve
Luce "好主意。我今天早上什么都没吃。"
Marcel neutral c "我{i}刚才{/i}还在纳闷怎么没在餐厅见到你。是你姐姐又来数落你了吗？"
show luce frown with dissolve
Luce "我姐姐确实经常数落我，不过周末她还算体贴，会放我清静——至少大多数时候是这样。"
show luce neutral with dissolve
Luce "我没去餐厅的原因是……唉，这个……"
show luce shy with dissolve
"露丝羞怯地摆弄着她那条长而朴素的裙摆。"
Luce "我睡过头了。"
Marcel "你睡过头了？"
"露丝点了点头。"
Luce "我醒来时，早餐已经结束了。我只好匆匆赶去校园跟你见面。"
show luce huhblush with dissolve
Luce "我怕你会以为我把你抛下了。"
"露丝确实晚了几分钟，可我那时并没在意。如今，我却好奇起来。"
Marcel huh c "你怎么会睡过头呢？这可不像你。"
Marcel neutral c "你昨晚不会熬夜了吧？"
show luce sigh with dissolve
Luce "是啊，确实熬了，可不是有意为之的。"
Luce "我只是……"
show luce shy with dissolve
Luce "大概是……兴奋过头了吧。"
Luce "以前从来没有同学邀请我出去过；在这所学校读的三年里，一次也没有。"
show luce sigh with dissolve
Luce "我不知道那会是怎样的情形，也不知道我们会做些什么。"
Luce "我告诉自己，今天不过是又一个平淡无聊的日子，不该抱什么期望，可是……"
show luce shy with dissolve
Luce "我就是忍不住去想它。"
Luce "昨晚我试着入睡，却怎么也睡不着。我翻来覆去，满脑子都是今天……"
"露丝咽了咽口水。"
Luce "想、想着你。"
Marcel shockblush c "我……？"
show luce annoyed with dissolve
Luce "对，就是你！"
"露丝抬起头，随即皱起眉头，怒瞪着我。"
Luce "害得我睡不着都是{i}你{/i}的错，所以要你尽全力逗我开心。要是现在让我失望的话，我会非常伤心的……！"
Marcel shock c "我现在没有让你失望吧？"
show luce neutral with dissolve
"片刻的停顿。"
"露丝似乎在脑海里反复斟酌着可能的回答，挑拣着最佳的措辞，直到……"
show luce huh with dissolve
Luce "……没有。"
"她迟疑了片刻，坦言道。"
Luce "我没有失望。"
show luce smile with dissolve
Luce "你让我用全新的眼光看待 Myennes。"
Luce "和你在一起的时候，这个平淡无聊的地方……{w}看起来{i}几乎{/i}很美。"
Marcel smile c "只是几乎而已，是吗？"
"我微微一笑。"
Marcel "唔，总比没有强吧。"
Marcel "殿下，我会尽力让这一天对得起您。"
"我双手拎起裙摆，向露丝行了个利落的屈膝礼。"
Marcel "那么，你愿意帮我铺一下野餐垫吗？"
show luce annoyed with dissolve
Luce "先是把我当公主捧，现在又要我当苦力？这前后一致的道理在哪里？"
Luce "你那所高大上的巴黎学校没教过你礼仪吗？"
Luce "这种杂活就该你自己全包了！"
Marcel "好了好了，别这样。出点力对你有好处，还能让饭菜更香呢！"
show luce sigh with dissolve
Luce "……哼。好吧。"
show luce neutral with dissolve
"露丝撅着嘴，帮我从藤篮里取出野餐毯。"
"这是条很大的毯子，摆弄起来着实费了不少力气，但露丝和我还是把它铺开了；褶痕也全都抚平。"
"弄好之后，我后退一步端详起我们的成果，不禁笑了。"
Marcel "我觉得这样就很好了。"
show luce annoyed with dissolve
Luce "最好是。我们为那个费劲的东西至少折腾了五分钟……"
Marcel "这不是很好吗！正好让你的血活络起来！"
show luce frown with dissolve
Luce "血再这么活络下去，我怕鼻子会流出血来。"

play sound "sfx/rustle.ogg"
scene lake:
    size (1920, 1080) crop (240, 140, 1440, 810)
show luce frown2:
    xpos 0.5 xanchor 0.5 ypos 0.5 yanchor 0.5
    ease 0.8 ypos 0.55
with dissolve

"露丝叹了口气，往毯子上一倒，力气仿佛都用尽了。"
"她也懒得脱下那双沾了土的校鞋，但我没有责备她。我不是露丝的姐姐，训斥她并非我的本分。她平日想必已经听得够多了——更何况，她{i}确实{/i}帮了我不少忙。"
"若没有她，我都不知自己能否把这毯子给制服。"
"我在露丝身旁的毯子上坐下。我能感觉到布料下的落叶和零星的断枝，可这总比直接坐在地上舒服，也免去了裙子沾上泥土。"
Marcel c smile "那么……"
"我把野餐篮放在身边，开始在里面翻找起来。"
Marcel "你想吃点什么？"
show luce neutral2 with dissolve
Luce "甜的东西。"
Marcel "我不知道你喜欢吃甜的。"
Luce "有谁不喜欢呢？"
Marcel c ehe "说得也是，嘿嘿……"
show luce huh2 with dissolve
Luce "在学校我们吃不到多少甜食。餐厅里提供的多半是朴素又营养的东西，比如面包和汤。"
Luce "我一直喜欢蛋糕和饼干，可我没钱花在这种奢侈品上。"
show luce sad2 with dissolve
Luce "我自己买的零食，多半也会被我姐姐偷走。我太了解她了。"
Luce "她比喜鹊还会钻空子。"
Marcel c neutral "她也爱吃甜食吗？"
show luce sigh2 with dissolve
Luce "她比我还要厉害。"
Luce "要是能行，她恨不得天天只吃糖粉和凝脂奶油。"
Marcel c frown "听起来可不太健康……"
Marcel c smile "不过，偶尔吃一次这样的东西，我想也没什么问题。"
"我伸手探进篮子，取出那装满玛德琳蛋糕的纸袋。那是些小巧的黄油海绵蛋糕，上面撒着糖霜，虽然路上有些磕碰坏了，却丝毫不减它们的诱人。"
"我把纸袋递给露丝，她眯起眼睛打量着。"
show luce huh2 with dissolve
Luce "这些……都是给我的吗？"
Marcel c huh "唔，也许你不该把它们{i}全{/i}吃掉……"
Marcel "不过你可以吃一两个……或许三四五个也行！"
show luce neutral2 with dissolve
Luce "或者五个？"
Marcel c smile "你要是真想吃也行。只是记得给肉馅饼留点肚子。"
show luce shy2 with dissolve
Luce "嗯。"
"露丝伸出手指。它们迟疑地触了触纸袋，随即又缩了回去，仿佛有些害怕。"
Luce "你确定这样可以吗？"
Marcel c neutral "有什么不可以的？"
Luce "这是你自己花钱买的。让我吃的话，可不太合适。"
Marcel c shock "可我就是买来让你享用的呀！你要是一个都不尝，那才叫浪费呢！"

stop music fadeout 1.0

"我咧嘴一笑，接着用食指轻轻戳了戳露丝的脸颊。"
Marcel c smile "别害臊啦。我可是看见你在糕点铺橱窗前盯着这些玛德琳蛋糕直看。"

play music "bgm/Comedy.ogg" fadein 0.5

show luce annoyedblush2 with dissolve
Luce "我、我才没有看……！"
Marcel c laugh "你明明就看了。"
"露丝撅着嘴、鼓起腮帮子的时候，简直不像她自己，我按捺不住那股越来越强的念头，想要逗弄她。"
"既然我已经用手指戳过她了，那用言语再逗她一逗也无妨。"
Marcel c smile "你简直是馋得流口水。"
show luce huhblush2 with dissolve
Luce "流、流口水……？！"
Marcel "嗯哼。你表现得可一点都不含蓄。"
show luce annoyed2 at bounce
Luce "不、不是那样的……！"
Marcel c huh "可是露丝，我从不说假话。我当袜子精灵那天发过誓，要永远诚实坦率。"
Marcel "一想到你会说我撒谎，我就受不了！"
Luce "哼，这件事上你就是在撒谎！你编故事，好把我塑造成一个大馋鬼！"
show luce frown2 with dissolve
Luce "我确实喜欢玛德琳蛋糕，可我很多年都没吃过了。就算它们看起来再美味，我也绝不会在公共场合对着它们流口水的……"
Marcel c smile "也不会管它们烤得多么金黄，多么松软，多么绵软呢？"
show luce shy2 with dissolve
Luce "嗯……"
"露丝盯着那袋玛德琳蛋糕，脸颊绯红。"
"显然她很想拿一个，可她又不愿证实我的话。"
"她话语与神色间的矛盾可爱极了——而我在学校里见到的露丝，与眼前这个露丝之间的反差，则更是如此。"
"露丝被关在学校走廊里时，总是安静寡言，几乎不带一丝情绪。"
"可一旦走出校门，在秋日的树下与淡蓝色的天空下，她就像完全变了个人；一个更快乐的女孩。"
"我只希望这份快乐能一直持续下去。"
Marcel smile c "听我说，我不会笑话你的，我保证。我又不是你姐姐。"
show luce sigh2 with dissolve
Luce "谢天谢地……"
Marcel "吃一块玛德琳蛋糕吧。吃好几块也行。你要是不吃，我就忍不住把它们全吃光了。"
show luce huh2 with dissolve
Luce "那、那怎么行！既然是你买给我的，要是不尝几块，那才叫浪费……"

stop music fadeout 1.0

Luce "那我就不客气啦！"

window hide dissolve
$ achievement.grant("sweeter_than_sugar")
play music "bgm/Friendship.ogg" fadein 1.0
scene cg8 with dissolve
$ renpy.pause(1.0)
window show dissolve

"露丝拿起一个贝壳形状的玛德琳蛋糕，咬了一口。"
"糖霜从那甜点上纷纷落下。有些落在她膝上，像雪一样覆在膝盖的弧面上，可露丝并不在意。"
Luce "嗯……"
"她闭上眼睛，睫毛黏合在一起，细细品味着那玛德琳蛋糕。"
"我看得出她很享受，可我还是想听她亲口确认。"
Marcel smile c "好吃吗？"
Luce "简直像天堂一样！"
"露丝又咬了一口她的糕点，轻轻地叹了口气，心满意足。"
Luce "这块玛德琳蛋糕好松软、好甜。"
Luce "距离上次吃它已经太久，我几乎都忘了它们有多美味。"
"她把剩下的糕点一口塞进嘴里，咀嚼了好一会儿，脸上带着若有所思的神情。"
"她叹了口气，手里又拿起一块饼干，身子向后靠去，仰望那片凉爽的蓝天。"
Luce "我小时候，母亲常给我做这种蛋糕，当作一种犒赏。"
Luce "我们家没什么钱，不能常吃这样的东西，可母亲做的玛德琳蛋糕真的很好吃。"
"露丝的脸色沉了下来。"
Luce "当然，我姐姐往往先下手为强。有时候，她会在我还来不及尝上一口的时候，就把它们全吃光了。"
Luce "你或许以为，作为姐姐她会懂事些，可她从来都不怎么成熟。"
Luce "有一回发生这种事，母亲责骂了姐姐，还罚她不吃晚饭就上床睡觉。"
"露丝摇了摇头。她浅色的短发被风扬起，一缕缕发丝随风舞动。"
Luce "天哪，这勾起了不少回忆。"
Marcel neutral c "是美好的回忆吗？"
Luce "有些是美好的，可并不全是。"
Marcel smile c "那这些玛德琳蛋糕怎么样？有你母亲做的那么好吃吗？"
Luce "它们{i}确实{/i}好吃，只是方式不同。"
Luce "我母亲很清楚我喜欢什么样的玛德琳蛋糕。她会照着我的喜好调整配料。"
Luce "而这些玛德琳蛋糕，却是为任何付得起钱的顾客做的，只是摆在店铺的橱窗里。我想，它们大概少了点人情味吧……"
Luce "但美味丝毫不减。"
"露丝皱起眉头。她把双膝收近下巴，双臂环抱住双腿。"
Luce "现在我真想再尝尝母亲做的玛德琳蛋糕。那真的已经是很久以前的事了。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
play ambience "sfx/footsteps2.ogg" fadein 1.0
play music "bgm/Mysterious.ogg" fadein 1.0
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  10月31日{vspace=1}  回到现实") )
show image "border" onlayer border
scene village:
    subpixel True
    size (1920, 1080) crop (0, 200, 1280, 720)
    linear 20.0 crop (350, 200, 1280, 720)
with wiperight_slow
window show dissolve

"湖畔那场惬意的野餐之后，露丝和我回到了学校。"
"我们越靠近校舍，露丝的步子就越慢，直到她几乎是拖着脚在走。"

scene yard:
    subpixel True
    size (1920, 1080) crop (0, 200, 1280, 720)
    linear 20.0 crop (350, 200, 1280, 720)
with wiperight_slow

"在湖边时，我见过露丝各种各样的神情，可当我们回到学校操场，她的唇又抿成那道熟悉的、一线般的模样。"
"她双臂抱着胸，带着一丝不信任地打量着那栋老旧、歪斜的校舍。"

stop ambience fadeout 1.0
hide image "border" onlayer border
scene yard
show luce neutral at center
with wipeleft_slow

Luce "现在我们回到这里，几乎感觉今天就像没发生过一样……"
"露丝的声音轻得几乎要被秋风吞没。"
"散落在地的枯叶在我们脚边被风卷起，化作一片红黄交织的迷蒙。"
"我瞥了露丝一眼，忍不住皱起了眉头。"
Marcel frown c "你难道玩得不开心吗？"
show luce sad with dissolve
Luce "我玩得很开心。这才是最糟糕的地方……"
Luce "和你在一起的时候，我几乎可以假装自己不必回到这个可恨的地方；假装周一不用去上课，姐姐不会责罚我，同学们也不会在旁边看热闹、笑话我……"
show luce sigh with dissolve
Luce "有那么一阵子，仿佛只有你我二人……"
"露丝的声音渐渐低了下去。她是不是觉得自己说得太多了？"
"当初在柴房里，我第一次真正与她交谈时，情形也是如此。"
"我几乎没怎么引导，她那满腔的苦涩便如决堤般倾泻而出，可吐露完之后，她又重新板起了脸。"
"在那之后，她好几个星期都不肯跟我说话。"
"也许她不喜欢让自己显得脆弱。"
"这就是她的神情总是如此戒备的原因吗？"
"可若露丝从不让人走进她的心，那她将永远不会像我们身在湖畔时那样笑了。"
"我不想她再把我当成陌生人。"
Marcel neutral c "我倒不觉得这有什么不好。哪怕它终究要结束，你能好好开心一场，难道不该感到高兴吗？"
show luce neutral with dissolve
Luce "大概是吧……"
show luce sad with dissolve
Luce "我知道自己听起来一定像个被宠坏的孩子，可是……"
"露丝把几缕浅色的发丝别到同样白皙的耳后。"
Luce "我实在太不习惯能够……好好地活着，纯粹地享受一番，所以每当我遇到这样的机会……"
Marcel "你不希望它们结束？"
"露丝点了点头。"
show luce huh with dissolve
Luce "我当然很高兴你能带我出来。我很感激。湖泊很美，玛德琳蛋糕也很好吃。"
Luce "你为我做了那么多，本不必如此。这让我很开心。可是……"
show luce sad with dissolve
Luce "我真希望那些快乐的时光能再停留得久一点。"
"露丝吸了吸鼻子。"
show luce sigh with dissolve
Luce "真奇怪……"
Luce "这些年来，我一直忍受着同学们的嘲笑和姐姐的责罚。我知道这不公平，可我告诉自己，我无力去阻止这一切。"
show luce sad with dissolve
Luce "我曾认定，此生注定不幸。我以为自己没有抱怨的资格。"
Luce "毕竟，还有许多人过得比我更糟。"
Luce "可是，当你开始对我友善时……我才意识到，我不必独自承受这一切。"
show luce huh with dissolve
Luce "那么，我为什么忍了这么久？"
Luce "我为什么还要继续忍下去？"
show luce sad with dissolve
Luce "我{i}不想{/i}再忍了，可我一回到宿舍，就又要被欺负；我心里清楚得很。"
Marcel neutral c "那就别回宿舍去。至少现在别回去。"
show luce huh with dissolve
Luce "可我又能去哪儿呢？"
Marcel smile c "你可以回我房间来。"
show luce frown with dissolve
Luce "那不会打扰到你吗？"
Marcel "你并不打扰。若不然，我也不会陪你待上一整天。"
show luce neutral with dissolve
Luce "这倒是真的，可我还是担心你只是在可怜我。"
show luce sad with dissolve
Luce "我是个阴郁的人。大家都这么说。所以同学们都躲着我。"
Luce "我觉得自己算不上一个有趣的朋友。克洛蒂娜的陪伴，可比我有趣多了。"
Marcel huh c "可我不想和克洛蒂娜待在一起。她是有趣，可有时候也让人累得慌……"
Marcel smile c "而且我觉得，比起她，我跟你更有共同之处。"
Marcel "或许你没注意到，我也很安静。我也不喜欢引人注目。"
Marcel "况且，我也觉得你没有{i}那么{/i}安静。至少我们还能聊上几句。"
show luce huh with dissolve
Luce "那只是跟你在一起的时候。有你在，我就成了个话匣子。我也不知道为什么。"
Luce "我最近简直不像我自己了。"
"露丝摇了摇头。她似乎对自己的坦率感到惊讶，但至少她方才的悲伤仿佛已经消散。"
show luce neutral with dissolve
Luce "好吧，既然你真的不介意我作伴，那我就领你这个情。我不愿这美好的一天就这么仓促结束。"
Luce "如果可以，我想把这份记忆留得再久一点……"
show luce sigh with dissolve
Luce "在一切回到从前那样之前。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
play ambience "sfx/hairbrush.ogg" fadein 1.0
play music "bgm/Luce.ogg" fadein 1.0
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  10月31日{vspace=1}  温柔时刻") )
$ renpy.pause(0.8)
scene cg9 with wiperight_slow
$ renpy.pause(1.0)
window show dissolve

Marcel "这样怎么样？痛吗？"
Luce "不痛，没事。"
Marcel "好，我会轻一些。可要是扯疼了，要告诉我，好吗？"
Luce "我会的。不过我倒不担心这个。我相信你会小心。"
"这句坦白从露丝唇间轻轻逸出，比一片叶子落在地上的声音还要轻柔。"
"我看不见露丝的脸，但我猜想她的脸颊正泛红，就如同我的一般。"
"我胸腔里有东西在悸动。我能感到蝴蝶在我腹中翩然起舞。"
"是因为我们之间这份新的亲近吗？"
"露丝坐在我床沿，而我盘腿坐在她身后。"
"我手里握着那把镶金的梳子（它曾是母亲的），慢慢将梳齿滑过露丝那短短的浅金色头发。"
"露丝的发丝堪堪触及下颌，可里面却缠着多得惊人的结。我不禁纳闷怎么会这样。她的姐姐是不是偷走了她的发梳，就像偷走她的袜子一样？"
"我想一直替露丝梳头，直到头发梳得发亮噼啪作响，哪怕手臂酸痛也不在乎。"
"我想，在经历过这一切之后，她需要一个能对她呵护备至的人。"
"这或许能让她暂时忘掉——哪怕只是几个偷来的、隐秘的片刻——她的姐姐，这所学校，还有学校里所有的学生。"
"然而，当我的胸膛莫名发紧、指尖又不停颤抖时，实在很难专注于手头的事。"
"我试着告诉自己，露丝无非是一具玩偶，可她的发这么柔软，她的头皮这么温暖，叫我如何能相信这显而易见的谎言？"
"我用力过猛地挑开一个发结，露丝疼得轻轻叫了一声。"
Luce "啊……！"
Marcel "啊——对不起！我没留神……"
Luce "没关系。总比我姐姐温柔。"
Marcel "她从前也替你梳头吗？"
Luce "在我还小的时候，是的。"
Luce "那时候我的头发长得多——几乎垂到腰际——又那么容易打结。"
Luce "我想姐姐是嫉妒我的头发，因为她总是用力拽着梳子硬生生刷下去，都能梳下一把一把的头发来。"
Luce "有时候，她甚至还故意拿梳子在我的头发里搅出结来，好让她再慢慢去解开……"
"露丝在我的触碰下微微一颤。似乎只是提及这些回忆，就让她重温起某些不快的事。"
Luce "也只有像我姐姐这样小气的人，才能把梳头变成一种惩罚——而且她还总是乐在其中。"
Luce "再也没有什么比伤害我更能让她高兴的了。"
Marcel "可她为什么{i}想{/i}伤害你？我实在想不通。"
Luce "你还是别去弄明白为好。她是个恶毒的人，却也是个懦夫，就爱拿比她弱小的人撒气。"
Luce "你若是有一分像我姐姐，你也会伤害我。"
Marcel "不会的！我不会！我也办不到！"

scene cg9_2 with dissolve

Luce "噗……呵呵呵……"
"露丝的肩膀开始抽搐。我看不见她的脸，但……"
Marcel "你是……在笑我吗？"
Luce "抱歉，抱歉。你方才听起来可真是委屈！"
Marcel "我{i}是{/i}委屈。我绝没有伤害你的念头，一丝一毫都没有。"
Marcel "我提出替你梳头，是因为想帮你。朋友不就是这样吗？"
"对于女性之间的关系，我知之甚少（尽管我正一点点学着），可我一直以为梳头发是相当寻常的女子举动。"

scene cg9 with dissolve

Luce "嗯……"
"露丝在床上动了动。她的发丝轻扬，露出一小片光滑的后颈。"
Luce "你是有点笨手笨脚，但你没有坏心眼。"
Luce "我很难交到朋友——或许根本交不到——你肯费这么大的心思，我很意外，可是……"
Luce "我想，我并不介意把你称作朋友。"
Marcel "露丝……"
"我的心在胸腔里怦怦直跳，脸却愈发红了。"
"听露丝称我作她的朋友，我由衷高兴，可她的话语又让我的心颤抖不已。"
"我能勉强握紧那把梳子——它突然间莫名地滑腻起来——已是不易。"
"我的掌心开始冒汗。"
Marcel "嗯，那个……谢谢你。我会继续努力的——也谢谢你让我替你梳头。"
Luce "那你不必谢我。那算不上什么恩典。"
Luce "真要谢的话，{i}我{/i}才该谢{i}你{/i}。"
"露丝叹了口气。"
"我们俩沉默了片刻；只有梳齿穿过露丝发丝的声音打破了这份寂静。"
"我机械地上下移动着手臂。"
"如果我无法说服自己露丝只是一具玩偶，那我至少可以试着假装自己是件由发条零件做成的物什。"
"我的手在动，靠的不是骨骼与肌肉，而是齿轮与滑轮。"
"只要我假装自己是黄铜或钢铁所铸，我就不会那样手足无措……"
"几分钟过去了，随着时间流逝，我的知觉也渐渐恢复。如今，我几乎觉得一切如常。"
"这番反复梳头的动作让我手臂开始酸痛，但我没有停下。"
"我想，我希望这一刻永远延续下去。"
Luce "你知道吗……"
"露丝终于开口，她轻柔的声音在空气中荡漾开来。"
Luce "我一直都很喜欢长发。花了很多年才留起来，等它终于垂到腰际的时候，我高兴极了。"
Luce "小时候，我常假装自己是个公主。那头发是我的骄傲与快乐……"
"说到这里，露丝叹了口气。"
Luce "可自从我被送到这所学校，一切就变了。"
Marcel "出了什么事吗？"
Luce "可以这么说。"
Luce "姐姐在这里谋到差事后，我就被送来了这所学校。我来的时候，她已经教了半年书，地位也稳了。"
Luce "布吕吉埃夫人信任她，也听她的话。"
Luce "所以当姐姐告诉她说，我在她的课上一直挠头皮，她也就毫不怀疑地信了。"
Luce "姐姐说我是长了虱子，该把头发剃掉，免得传染给别的姑娘。"
Marcel "那么……"
"我的手指穿过露丝那浅淡、近乎灰白的发丝。"
"露丝的头发真的很美。它颇为纤细，也不算特别亮泽，却自有一种含蓄的韵味。"
"如果那头长发垂到她的腰际，我想露丝也许真的会像一位公主——或许是安徒生童话里住在冰封雪山上的那位雪之公主。"
"我咽了口唾沫。"
Marcel "你的头发被剃掉了？"
Luce "没错。是布吕吉埃夫人让姐姐动手的。"
"露丝的身体紧贴着我绷紧了，尽管我已尽可能轻柔地为她梳理着头发。"
"我觉得她脊背僵硬，并非因为我带给她的不适，而是因为她过往的痛苦。"
Luce "姐姐剃掉我头发的时候，我差点哭出来。我那么珍惜它，却只能坐在那儿任她糟蹋。"
Luce "等她弄完，剪刀都钝了，我的膝上落满了那些长长的、金黄的、我珍爱着的发丝……"
"露丝顿了顿。她低垂着头，深吸一口气，然后继续说道。"
Luce "别的姑娘当然都笑话我。那时候的头发比现在还短。她们说我看上去像个男孩子。"
Luce "没了头发，我不知道该怎么办。那让我觉得自己赤裸裸的——好像我都不像自己了。"
Luce "我留了那么久的长发，然后……"
"露丝摇了摇头。"
Luce "也许是我傻，可是……就好像我身体的一部分，连同头发一起被剪去了。"
Luce "那之后，我不知道自己是谁；就连看着镜中的倒影，也认不出自己。"
Luce "我身处一所陌生的新学校，四周都是陌生的新人，就连我自己看起来也像个陌生人……"
Marcel "不行……"

stop ambience fadeout 1.0
scene marcel_room blur:
    size (1920, 1080) crop (650, 60, 1152, 648)
show luce sad3 at center
with wipeleft_slow

"我让手指从露丝的发间滑落，又从床上起身站到她面前。"
"我与露丝的目光相遇，随即吃惊地发现，她的眸子水光潋滟，苍白的睫毛全都粘成了一簇簇。"
"她一定哭过了。"
Marcel neutral c "我不觉得你傻。"
show luce neutral3 with dissolve
Luce "你、你不觉得吗？"
Marcel sad c "不觉得。我明白你的感受。"
"对露丝的处境，我比她所能想象到的还要感同身受。"
"和她一样，我也被迫离开了故家。我把母亲抛在身后，来到这个陌生的环境，穿着陌生的衣裳。"
"虽然已经过去几个月了，可每次看到镜中的自己，我仍会惊讶地一怔。"
Marcel neutral c "有时候，我也不知道自己是谁。我不知道自己想成为什么人——可有一点我很清楚。"
"我把露丝的手握在掌心里。我的手指与她交缠在一起，如同常春藤一般。"
show luce huhblush3 at bounce
Luce "啊……！"
"露丝猛地一颤。她的脸颊泛起粉色，却并没有挣脱我的意思。"
"短暂的停顿之后，她的手指反握住我的……然后她靠了过来，直到我们的鼻尖几乎相触。"
show luce neutral3 with dissolve
Luce "你知道什么，玛塞尔？"
Marcel "听了你说的这一切，也知道了你所经历的一切，我知道，我想留在你身边。"
Marcel "我不会丢下你；永远不会。我太在乎你了，舍不得那样做。"
Marcel smile c "你真是个可亲的朋友。"

stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene sky3 g with clockwipe
$ renpy.pause(0.5)
show overlay2
show message16 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message16
hide logo2
hide overlay2
with datetrans2

$ renpy.pause(0.3)

play ambience "sfx/rain.ogg" fadein 1.0
play ambience2 "sfx/wind.ogg" fadein 1.0
play music "bgm/Casual_Day.ogg" fadein 1.0
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  11月9日{vspace=1}  雨天难开心") )
scene sky3
show rain2
with dissolve
window show dissolve

"几天平静无事地过去，直到某个周一清晨，我被雨滴敲打窗棂的声音唤醒。"
"我用早餐时雨势不减，前往教室上今天第一节课时也同样如此。"
"我不得不用手护住头顶，一路跑进教室以免浑身湿透，同学们也都一样。"
"可怜的米拉贝尔，唉，实在太过笨拙，没法毫发无损地穿过泥泞的校园。她刚在校舍入口外绊了一跤，一头栽进了水洼里。"
"冰冷的水花四处溅开，弄脏了米拉贝尔的手、胸口和裙摆。"
"布吕吉埃夫人看到浑身湿透、瑟瑟发抖的米拉贝尔，叹了口气，吩咐她去宿舍擦洗身子，换上一套备用的制服。"
"米拉贝尔乖乖照做，一言不发地离开了教室。"
"上课期间，雨仍旧拍打着窗户，与风声交织在一起。它执拗地敲击着玻璃，水流顺着光洁的窗面滑落。"
"我望向窗外，出神地盯着那雨。"
"风的呼啸几乎盖过了布吕吉埃夫人的讲课声，她不得不提高嗓门，好让自己被听见。"

play sound "sfx/churchbells.ogg" fadein 1.0

"雨仍旧不肯停歇，但除此之外，我们的第一节课总算安然无恙地过去了。随着远处教堂钟声的响起，这一小时宣告结束，也预示着我们的下一节课——英语。"

stop sound fadeout 2.0

"杜布瓦夫人走进教室，一副风尘仆仆的模样。几缕碎发散落在她紧绷的发辫之外，裙摆上溅满了水渍。"
"难道她也像可怜的米拉贝尔一样，在雨中摔了一跤？"
"布吕吉埃夫人打量了一番杜布瓦夫人那副邋遢模样，轻哼了一声，却没有开口说什么。或许在学生面前指责自己的下属，看起来会不够专业吧。"
"我不禁好奇，放学后她会不会把杜布瓦夫人拉到一旁，对她的仪表教训一番。"
"杜布瓦夫人或许也在担心同样的事，但她上英语课时比平时更显得心神不宁。当米拉贝尔在课上了一半时走进教室，已经洗净身子、换上了干净的制服，杜布瓦夫人惊讶地眨了眨眼。"
"米拉贝尔道了声歉，匆匆溜回座位，恹恹地低着头。"

stop ambience fadeout 1.0
stop ambience2 fadeout 1.0
play ambiencee "sfx/rain2.ogg" fadein 1.0
scene classroom_r:
    size (1920, 1080) crop (200, 40, 1440, 810)
show paulette neutral2:
    xpos 0.5 xanchor 0.5
with wipedown_slow

Dubois "好了，我们刚才讲到哪儿了……？"
"杜布瓦夫人沉吟着，思路全被打乱，直到塞琳开口插话。"
Celine sigh "您刚才在讲代词，夫人。"
show paulette smile2 at bounce
Dubois "啊，对！代词。你分毫不差。"
show paulette neutral2 with dissolve
Dubois "那么，姑娘们，把目光都移到黑板上……"
"课就这般进行着。除了窗外持续不断的雨声，一切相对安静而平淡——直到同学们满腹牢骚地开始窃窃私语。"

show image "border" onlayer border
scene classroom_r:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

Cla "这里可真冷……"
Claa "冻得我手都要掉下来了！"
Cla "这样我可没法做笔记！"
Claaa "反正这课我也不想做笔记，可这也太离谱了。"
Cla "炉火灭了吗？"
Claa "看样子是熄了。"
Claaa "什么时候的事？"
Claa "冷得我都感觉不到自己的手指了！"

hide image "border" onlayer border
scene classroom_r:
    size (1920, 1080) crop (200, 40, 1440, 810)
show paulette frown2:
    xpos 0.50 xanchor 0.5
with wipeleft_slow

Dubois "姑娘们？"
"杜布瓦夫人察觉到躁动，转身望向面前那一张张苍白、绷紧着的脸。"
Dubois "姑娘们，怎么了？怎么都不好好听课？"
Claudine smile u "我们是想听的，夫人，可炉子里的火好像已经灭了。"
show paulette neutral2 at bounce
Dubois "啊……"
"杜布瓦夫人望向炉栅。里面堆满了煤与柴烧尽后发黑的灰烬，早已燃尽，连一点火星也不剩。"
show paulette sigh2 with dissolve
Dubois "原来如此。难怪这里这么冷！"
show paulette neutral2 with dissolve
Dubois "火是什么时候熄灭的？克洛蒂娜，你看见了吗？"
Claudine "我也不太清楚，夫人。也许五分钟前吧？"
show paulette frown2 with dissolve
Dubois "这可不行。照这样下去，我们都要冻出病来了！"
Cla "说得对！"
Claa "尤其是米拉贝尔！"
Claaa "就是。米拉贝尔来上课的路上掉进水坑里了。"
Cla "要是火灭了，她怕是要寒气入骨了。"
Claa "她会得肺炎的！"

scene classroom_r:
    size (1920, 1080) crop (350, 40, 1440, 810)
show mirabel shock2:
    xpos 0.70 xanchor 0.5 ypos 0.55 yanchor 0.5
with wiperight_slow

Mirabel "肺、肺炎？"
"米拉贝尔眨着她那双鹿般的大眼睛，不安地环顾着教室。"
show mirabel sad2 with dissolve
Mirabel "我真的会……？"
Cla "总是有这个可能的。"
Claa "你还坐在窗户旁边，冷风都会扑到你身上！"
Claaa "米拉贝尔，你不觉得冷吗？"
show mirabel scared2 with dissolve
Mirabel "有、有一点点……"

play sound "sfx/chair.ogg"
show mirabel:
    ease 0.8 xpos 0.75
show noemie smile2:
    xzoom -1 xpos -0.10 xanchor 0.5 ypos 0.55 yanchor 0.5
    ease 1.6 xpos 0.30

Noémie "你可得当心，米拉贝尔。我姨妈阿涅丝去年冬天得了肺炎，到现在还没好利索。"
show noemie neutral2 with dissolve
Noémie "她总抱怨浑身酸痛，有些日子连床都下不来！"
show mirabel shock2 at bounce
Mirabel "哦、哦不……我、我不想生病……"
show noemie smirk2 with dissolve
Noémie "你要是不当心，那可比单纯生病更糟。你是真的会死的。"
show mirabel scared2 at bounce
Mirabel "死、死？！"
"米拉贝尔的声音发出紧绷的尖响。与此同时，她的脸色变得惨白。"
Mirabel "可、可是……我、我不想死……"
Mirabel "我、我不能死！"

scene classroom_r:
    size (1920, 1080) crop (200, 40, 1440, 810)
show paulette frown2:
    xpos 0.50 xanchor 0.5
with wipeleft_slow

Dubois "别犯傻了，米拉贝尔。你不会死的。"
Mirabel shock "可是诺艾米说——"
show paulette sigh2 with dissolve
Dubois "诺艾米只是在逗你——而且这个玩笑也开得太刻薄了。"
show paulette frown2 with dissolve
"杜布瓦夫人向诺艾米投去责备的目光，诺艾米却似乎毫不在意。她脸上那抹得意的笑容没有半分动摇。"
Dubois "诺艾米，向米拉贝尔道歉。"
Noémie smile "是，夫人。"
"诺艾米拖长了腔调说。"
"她转头看向米拉贝尔，仍带着那副得意洋洋的笑容。"
Noémie "抱歉，我说了实话。"
"然后，她吐了吐舌头。"
"可想而知，这点举动并不能缓解米拉贝尔的忧虑。她此刻抖得比先前更厉害了，像暴风雨中的一纸飘带。"
show paulette sigh2 with dissolve
Dubois "不过，诺艾米，你或许说得也有道理。"
show paulette neutral2 with dissolve
Dubois "这里{i}的确{/i}冷得厉害。我怕这样的温度对你们的身体不好。得把火点起来，不然你们谁都没法集中精神。"
Dubois "你们当中得派一个人去柴房再取些柴火来。"
"听到这话，教室里开始涌动起一种可以预见的愤慨。"
Cla "去柴房？这种天气？"
Claa "那地方远得很呢！"
Cla "那地方甚至都不在学校范围里！"
Claaa "我才不想去那儿！会把我的头发弄坏的！"
Claa "会把我的鞋子弄坏的！"
Cla "会把我的裙子弄脏的！"
Claaa "还管什么米拉贝尔！我要是在那儿出去，非冻出病来不可！"
Claa "鞋子可不便宜，你懂吗？！"
show paulette frown2 with dissolve
Dubois "好了，姑娘们。安静下来。"
"杜布瓦夫人想用与布吕吉埃夫人同样的方式来维持课堂秩序——一个严厉的眼神加上一拍手——但杜布瓦夫人终究不是布吕吉埃夫人。"
"尽管她把布吕吉埃夫人的语气和神情模仿得几乎惟妙惟肖，姑娘们却根本不听，更谈不上安静下来。"
"相反，那些义愤填膺的窃窃私语声反倒越来越大。"
Cla "这种天气谁会想出去啊？"
Claa "那是去找死！"
Cla "现在还下着雨呢！"
Claaa "而且整整下了一夜！"
Claa "肯定不能是留长发的人。风会把头发吹得不成样子！"
Claaa "可这教室里谁留短发来着？"
Cla "嗯，倒是有一个人……"
Claaa "可她那么瘦小！要是病倒了怎么办？"
Cla "那也不是我们的错。"
Claa "要是没人出去多搬点柴火，咱们{i}全都{/i}会生病的！"
show paulette neutral2 with dissolve
Dubois "嗯……你们说得倒也有道理。"
"杜布瓦夫人环顾教室片刻，目光最终落定在她打算派往柴房的那个不幸的牺牲品身上。"
"不出任何人所料，她的目光落在了……"

stop music fadeout 1.0
show paulette frown2 with dissolve

Dubois "露丝。你就不能让自己派上点用场吗？"

play music "bgm/Mysterious.ogg" fadein 1.0

"露丝本正带着淡淡兴味凝视着雨水斑驳的窗玻璃，此刻转过头来。"
"她那头银金色的短发拂过脸颊，她蹙着眉说道……"
Luce neutral "您要我去柴房？"
show paulette neutral2 with dissolve
Dubois "是这样。"
Dubois "其他姑娘都有一头漂亮的长发。她们要是出去，风雨会把头发弄坏，可你只有一头短发。"
show paulette smile2 with dissolve
Dubois "你要是出去待上几分钟，倒也不至于太损伤你的容貌。"
Cla "说得对！你去吧，露丝！"
Claa "行行好，给我们弄点柴火来吧！"
Claaa "你要是不肯为我们去，就为了米拉贝尔去一趟吧！"
Claa "是啊，想想可怜的米拉贝尔！要是咱们生不起火，她怕是要不行了！"
Luce "我觉得米拉贝尔不会死……"
Luce frown "而且我也不确定自己是不是做这件事最合适的人选。"
show paulette frown2 with dissolve
Dubois "你这么说又是为什么呢，露丝？"
Luce neutral "我比大多数同学都矮小，恐怕搬不回来那么多柴火。"
Luce "派个个子高一点的人去，比如诺艾米，不是更合理吗？"
Noémie frown "哦？所以你是想把我一块儿扯进来，是吧？"
Luce frown "你们都想着把我弄出去。我就不能回敬一下吗？"
Noémie "当然不行！我不能出去！我还得帮母亲打扫屋子、做晚饭，手指要是冻伤了，我还怎么干这些活！"
show paulette frown2 with dissolve
Dubois "诺艾米说得对。她还有别的事要做，可你没有。你住在学校，不是和家人住在一起。"
Dubois "请别这么固执。我已经让你去做这件事了，我希望你去办。"
Luce sad "可是……"

stop ambiencee fadeout 1.0
play ambience2 "sfx/wind.ogg" fadein 1.0
play ambience "sfx/rain.ogg" fadein 1.0
scene sky3
show rain2
with wipeup_slow

"露丝瞥了一眼窗外。外面的雨还在下，比刚才更密、更急。"
"风似乎也大了起来。我能听见它在外面呜咽，一路把零落的叶子吹得四散纷飞。"
Luce sad "我不确定这种天气能不能出去……"
"我不怪露丝不愿去。外面的天气实在糟透了。"
"露丝身形娇小纤弱，我担心她一旦踏出校舍的安全范围，就会被风给吹走。"
"我想不会再有人自告奋勇了，所以……"

stop ambience2 fadeout 1.0
stop ambience fadeout 1.0
play ambiencee "sfx/rain2.ogg" fadein 1.0
scene classroom_r:
    size (1920, 1080) crop (200, 40, 1440, 810)
show paulette neutral2:
    xpos 0.50 xanchor 0.5
with wipedown_slow

Marcel frown u "打扰一下，夫人……"
"我举起一只手。"
Marcel "我觉得露丝在这件事上说得对。我比她高，应当能搬更多柴火。要不，还是换成我去吧？"
show paulette frown2 with dissolve
Dubois "你这……真是高尚，玛塞尔……"
"杜布瓦夫人皱起眉头，那神情表明，她一点都不觉得我的提议有多高尚。"
show paulette sigh2 with dissolve
Dubois "……可我是让露丝去办这件事，不是叫你。"
Marcel shock u "可是——"
show paulette frown2 with dissolve
Dubois "身为老师，我的话在这间教室里应当优先，而不是听凭学生的心血来潮。"
show paulette neutral2 with dissolve
Dubois "你想帮露丝，心意是好的，可你不能一直替她挡着责任。"
Dubois "你要是这样一直惯着她，她将来就成不了一个勤恳自立的人。你明白吗？"
"杜布瓦夫人话里的真实用意，我实在再清楚不过了。"
"她不希望我——其实也不希望任何人——去帮露丝，因为她{i}就是{/i}想让露丝受苦。"
"她又想惩罚她的妹妹了，就为了『仅仅存在』这条罪名。"
"我咬住口中的软肉。我的手指蜷成了拳头。"
"这些年来，杜布瓦夫人折磨露丝难道还不够吗？"
"我想为露丝辩护，却又怕再替她说话只会让事情变得更糟。"
"我不知如何是好，只好垂下头，认命地退让了。"
Marcel sad u "我明白了。抱歉，夫人。"
show paulette smile2 with dissolve
Dubois "很好。"
show paulette neutral2 with dissolve
Dubois "好了，露丝。你到底是要出去，还是不出去？"
"露丝迎上杜布瓦夫人的目光。她的神情坚毅如铁。"
Luce frown "既然您给了我选择，那我想我还是宁可待在这里。"
show paulette frown2 with dissolve
Dubois "所以你不在乎同学们会不会生病？"
Luce neutral "这个，我——"
Dubois "哦，你这丫头真是没心没肺。你也太自私了！我还以为你父母会把你教得更好些！"

scene classroom_r:
    size (1920, 1080) crop (0, 40, 1440, 810)
show luce frown2:
    xpos 0.35 xanchor 0.5 ypos 0.55 yanchor 0.5
with wipeleft_slow

"露丝直直地望着杜布瓦夫人的眼睛，神情毫不退缩，说道……"
Luce "我也可以这样回敬您一句。"
"露丝的话很轻，对班上其他人来说多半难以捉摸，但我明白其中的含义。"

scene classroom_r:
    size (1920, 1080) crop (200, 40, 1440, 810)
show paulette mad2:
    xpos 0.50 xanchor 0.5
with wiperight_slow

"杜布瓦夫人想必也听懂了，因为她的脸涨得通红，布满红斑。"
"有那么几秒钟，我担心她会把黑板擦砸向露丝的头，或是更重的东西。"
"不过，那几秒很快就过去了，杜布瓦夫人脸上的怒红也随之褪去。"
show paulette sigh2 with dissolve
"她的肩膀垮了下来，长长地呼出一口气。"
show paulette frown2 with dissolve
"当她再次开口时，声音低沉而致命，甚至比校园里呜咽呼啸的风还要冰冷。"
Dubois "你刚才说什么，露丝？"
Luce frown "没什么，夫人。"
show paulette mad2 with dissolve
Dubois "别跟我装傻，丫头！你{i}分明{/i}说了什么。我听见了！"
show paulette frown2 with dissolve
Dubois "你何不走到讲台前面，把这话当着我的面再说一遍，你这个放肆的小东西？"
Luce frown "……那好吧。既然这是您想要的，{i}夫人{/i}，那正是我的荣幸。"

play sound "sfx/footsteps3.ogg" fadein 0.5
scene classroom_r
show paulette mad:
    xpos 0.50 xanchor 0.5
    ease 1.0 xpos 0.70
show luce frown:
    xpos -0.2 xanchor 0.5
    ease 2.0 xpos 0.30 xanchor 0.5
with wiperight_slow

$ renpy.pause(1.2)

stop sound fadeout 0.5

"露丝站起身，然后用无比清晰的声音说道……"
Luce "我{i}说了{/i}，这话我也可以原样奉还给您。"
show paulette mad:
    ease 0.7 xpos 0.75
Dubois "你——你这个……"
play sound "sfx/slap.ogg"
"杜布瓦夫人后退了一步。她的后背撞上黑板，激起一股淡淡弥漫在空气中的粉笔灰。"
show paulette frown with dissolve
Dubois "你这个心肠歹毒、忤逆顶撞的小丫头！"
Dubois "你尽管羞辱我好了，可你连我的教养也要扯进来！哎呀，这实在叫我难以忍受！"
Luce "真可笑。我也常有同感呢。"
show paulette mad with dissolve
Dubois "够了。安静！给我住口！"
show paulette frown with dissolve
Dubois "露丝！你这就给我出去，到柴房去取柴火，立刻！"
show paulette mad with dissolve
Dubois "然后，生好火之后，你就给我离开这间教室，站到外面那棵橡树下去！"
Dubois "我的教室里容不下你这种没规矩的丫头，不懂得尊敬师长，还满嘴无礼言语！"
show luce neutral with dissolve
Luce "那要是我拒绝呢？"
show paulette frown with dissolve
Dubois "那我就把你的恶劣行径禀告布吕吉埃夫人，让她把你从这所德高望重的学府开除！"
show paulette mad with dissolve
Dubois "像你这样无法无天的丫头根本不需要再受教育！这间教室对你来说太好了！你连一张书桌、一把椅子都不配用！"
Dubois "你这年轻的小姐，唯一配得上的就是站到倾盆大雨里去！也许那样能让你清醒清醒！"
show luce huh with dissolve
Luce "噢，天哪……"
"露丝挑了挑眉。"
show luce frown with dissolve
Luce "经过刚才那一番发作，夫人，我倒觉得需要冷静一下的不是我。"
Dubois "露丝！"
"杜布瓦夫人的脸扭曲起来。阴影聚拢在她眼底和嘴角周围，让她看起来几乎如同恶魔。"
"我从未想过人的脸能扭曲到那种地步。真是令人毛骨悚然。"
"如果我是露丝，此刻一定浑身发抖，可她连一丝颤动都没有。"
show luce sigh with dissolve
Luce "好吧。我去。"
"她没有太多选择的余地。"
show luce frown with dissolve
"露丝的脸再度恢复了毫无表情。"
"她站在那里，双臂僵直地垂在身侧，看起来就像一具人偶……"
"但人偶是由瓷器做成的，而瓷器看似坚固，却极易碎裂。"
"她真的会没事吗？"

stop ambiencee fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  11月9日{vspace=1}  冷落") )
play ambience "sfx/rain.ogg" fadein 1.0
play ambience2 "sfx/wind.ogg" fadein 1.0
play music "bgm/Sad.ogg" fadein 1.0
scene sky3
show rain2
with wiperight_slow
window show dissolve

"大约十五分钟后，露丝回到教室，怀里紧紧抱着一捆柴火。"
"木柴被雨水浸得湿透了，露丝试了好几次才把火点着。"
"当火终于烧起来（尽管微弱）时，露丝朝杜布瓦夫人僵硬地行了个屈膝礼，便走出了教室。"
"露丝一丝不苟地服从命令，走到外面的校园里，站到老橡树所能提供的那点可怜遮蔽之下。"
"可惜对露丝而言，这棵橡树几乎已落尽了叶子。仅剩的几片——红的、金的、褐的——战战兢兢地攀附在光秃秃的枝干上，仿佛在拼命求生。"
"它们在连绵不绝的雨水冲刷下瑟瑟发抖，露丝也一样。"
"我本该专心听英语课，可杜布瓦夫人的话左耳进、右耳出。"
"我无法集中精神。"
"我的身体或许还在教室里，可我的心却早已飘到很远很远的地方，与露丝一同被困在那湿冷阴郁的校园里。"

show image "border2" onlayer border
scene yard_r
show luce w frown r:
    xpos 0.30 xanchor 0.5
show rain
with wipedown_slow

"我每隔五分钟左右就向窗外瞥一眼去看露丝；我害怕，每次转头时都会发现露丝已经不在了。"
"万一她被风吹走了怎么办？"
"外面风这么大，就算风把她卷走了我也不会觉得意外……"
"但，令我宽慰（如果这也算宽慰的话）的是，整节课剩下的时间里露丝始终待在外面；她的脸色苍白，双臂僵直地垂在身侧。"
"她甚至没有用手去遮住头部以避雨。她一定明白，那样做毫无意义。"
"反正她都会被淋得透湿。"
show luce w sigh r with dissolve
"这实在太不公平了，气得我血脉偾张。"
"露丝什么都没做错，不该承受这一切。这不公正。这不合理。这——"

stop ambience2 fadeout 1.0
stop ambience fadeout 1.0
play ambiencee "sfx/rain2.ogg" fadein 1.0
hide image "border2" onlayer border
scene classroom_r
show paulette neutral at center
with wiperight_slow

Dubois "玛塞尔。"
"杜布瓦夫人的声音打断了我的思绪。"
"我猛地一颤，抬起头来，心怀愧疚地瞥了一眼我那面无表情的老师。"
Marcel u shock "是，夫人？"
show paulette frown with dissolve
Dubois "你能不能别老盯着露丝，把心思放回到你的功课上？她已经受到的关注够多了，你不必再给她添一分。"
Marcel "是，夫人。"
show paulette sigh with dissolve
"杜布瓦夫人叹了口气。"
show paulette neutral with dissolve
Dubois "我希望你不要对露丝那么心软。你应当清楚，她受罚是因为她是个执拗的小丫头，不懂得敬重长辈。"
show paulette frown with dissolve
Dubois "而你，倒是个出身教养良好的姑娘。据我所知，你的家境相当殷实。"
Dubois "你不想变成另一个露丝吧？"
Marcel sad u "不想，夫人。"
"这话也确确实实没错。我当然不愿像露丝那样被单独拎出来。那样的人生想必十分可悲——时刻提防着新的责备与训斥。"
show paulette neutral with dissolve
Dubois "那很好。那就请你把目光放到黑板上，别去看外面那个顽皮的姑娘。"
Marcel frown u "是，夫人……"
"但尽管有杜布瓦夫人的警告，我的目光还是不由自主地被露丝吸引过去，仿佛被某种强大的磁力牵引着。"

stop ambiencee fadeout 1.0
play ambience "sfx/rain.ogg" fadein 1.0
show image "border2" onlayer border
scene yard_r
show luce w frown r:
    xpos 0.30 xanchor 0.5
show rain
with wipeleft_slow

"露丝仍旧站在橡树下，低着头承受着落下的雨水。"
"她会没事吗？"
"我只能这样希望了。"

stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
hide image "border2" onlayer border
scene black
with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  11月9日{vspace=1}  雨落") )
play ambience "sfx/rain.ogg" fadein 1.0
play ambience2 "sfx/wind.ogg" fadein 1.0
play sound "sfx/churchbells.ogg" fadein 1.0
play music "bgm/Luce.ogg" fadein 1.0
$ achievement.grant("out_in_the_cold")
scene cg10 with wiperight_slow
$ renpy.pause(1.0)
window show dissolve

"教堂的钟声终于响起，宣告我这节难熬的英语课结束了，我立刻冲出校舍去看露丝。"
"雨还没有停，但似乎比刚才小了些。雨滴落得不那么急了，凛冽的风也减弱了，可这并没有让我稍稍安心。"

stop sound fadeout 1.0

"露丝已经在外面站了将近一个钟头，此刻想必早已冻彻骨髓。"
"她那头金发贴黏在脸颊和额头上，制服紧紧裹在身上，如同第二层皮肤。"
"水珠像泪珠一样凝在她的睫毛上，又有更多的水珠顺着她的鼻梁和脸颊滚落。"
"她看起来像是在哭泣，可那是虚幻的泪水。露丝的脸一片空白，即便我走近她，她的眼神也空洞而凝滞。"
Marcel sad u "哦，露丝。你……{w}还好吗？"
Luce "……"
"露丝没有回答我的问题，也许是因为那毫无意义。一眼就能看出，她根本没有一丝安好。"
Marcel "露丝……"
"我把露丝的手指握在手里，希望这能让她从恍惚中回过神来。"
"她的手摸起来冰冷刺骨，我的皮肤触到她时，不由得惊讶地倒吸一口气，几乎松手放开。"
Marcel shock u "你都冻僵了！"
"我把露丝的右手合在双掌之间搓着。也许摩擦能让她眼底重新焕发出一点生气……？"
Marcel "露丝……求你了，说句话吧。让我知道你还安好。"
"我的悉心照料，再加上我关切的言语，似乎起了一些作用。"

scene yard_r:
    size (1920, 1080) crop (240, 40, 1440, 810)
show luce w huh2 r:
    xpos 0.50 xanchor 0.5
show rain:
    size (1920, 1080) crop (240, 40, 1440, 810)
with dissolve

"露丝眨了几下眼睛，甩落睫毛上的雨珠，然后瞥了我一眼。"
"她的动作非常迟缓而僵硬，像一具自动机械。想必是因为寒冷吧。难道它已冻得她神志不清了？"
Luce "哦，玛塞尔……谢天谢地。真高兴是你。"
show luce w neutral2 r with dissolve
Luce "我还担心，等她那堂可恨的课一结束，我姐姐会来找我……"
show luce w sad2 r with dissolve
Luce "可当然，那永远不会发生。我姐姐绝不会为了我走进雨里。就算我着了火，她也不会朝我吐口唾沫。"
Luce "她恨我……"
"我不知道该如何反驳那句话。我想我也无话可说。"
"或许从前的我会对“有人竟会真正憎恨自己的骨肉至亲”这样的想法感到畏缩。"
"尽管母亲总在抱怨父亲，尽管凭他轻浮而无能的本性给我带来了种种艰辛，我却不恨他。他是我的父亲，也是我唯一拥有的父亲，而且我知道，他以他自己那种奇怪的方式在乎着我。"
"杜布瓦夫人却另当别论。"
"从她与露丝的相处来看，若说她真的{i}确实{/i}憎恶自己的妹妹，我也不会感到意外。"
"我不禁好奇，除了一股怨气之外，是否还另有原因。"
"怨恨足以推动人做出真正可怕的事，但我想，杜布瓦夫人的行径背后，恐怕远不止于此。"
show luce w sigh2 r with dissolve
Luce "要是她想杀了我，我都不会觉得意外。"
Marcel shock u "她为什么要杀你？"
show luce w frown2 r with dissolve
Luce "因为她心眼小，又孩子气。"
show luce w neutral2 r with dissolve
Luce "从我出生的那一刻起，她就恨我。就因为是我抢走了父母所有的关注。"
Luce "她比我大十一岁。我出生的时候，父母本以为他们不会再添孩子了。他们说我是个出乎意料的奇迹……"
show luce w sigh2 r with dissolve
Luce "可我姐姐却因此嫌弃我。"
Luce "她嫌弃我，因为我把父母对她的关注都夺走了。"
show luce w sad2 r with dissolve
Luce "她明明是个大人了，却还是没法接纳我。从这个意义上说，她就跟个孩子一样。"
"露丝抽了抽鼻子。"
"她抬手掩住嘴，往掌心里咳嗽。那咳声又响又干涩，就算弄疼了她的喉咙，我也不觉得意外。"
Marcel sad u "你在外面待得太久了。你抖得这样厉害，手也冰凉。"
Marcel "我们回屋里去吧。你需要暖和暖和。"
Luce "我觉得自己再也不会暖和过来了……"
Marcel "你会没事的。跟我来就是了。"
show luce w neutral2 r with dissolve
Luce "可我能去哪儿呢？要是进餐厅，我会因为拖着水走了一路被责骂——而且我也不想见到同学们。"
Luce "我不想被他们笑话。"
Marcel neutral u "那我们就不去餐厅了。去我房间吧。"
show luce w huh2 r with dissolve
Luce "你的房间……？可我都湿透了……"
show luce w frown2 r with dissolve
"露丝低头看了看自己。她的裙子被雨水浸得湿滑发亮，袜子也一样。"
"她又抽了抽鼻子。"
Luce "我还把你送我的那双漂亮袜子也弄坏了。那一定很贵吧。"
show luce w sigh2 r with dissolve
Luce "对不起。"
Marcel huh u "不过是点水罢了。没什么好担心的，而且这都不是你的错。"
show luce w huh2 r with dissolve
Luce "可是——"
Marcel frown u "别光是可是了。比起你那双袜子，{i}或者{/i}我卧室的地板，我更在乎的是你。"
Marcel "我不能再让你在外面多待一刻了。"
Marcel smile u "走吧。"

play sound "sfx/footsteps2.ogg" fadein 1.0
scene yard_r blur:
    size (1920, 1080) crop (390, 40, 1152, 648)
show luce w neutral3 r:
    xpos 0.50 xanchor 0.5
show rain:
    size (1920, 1080) crop (390, 40, 1152, 648)
with dissolve

"我握紧露丝的手，像拖着一个木制小玩偶似的把她拽在身后。"
"露丝试图稳住脚跟，却是徒劳。她比我矮小，而那一场倾盆大雨早已使她愈发柔弱。"
"她象征性地推拒了几句——"
show luce w sad3 r with dissolve
Luce "哎呀，真的，我不行。我不想给人添麻烦……"
"——但就连她也看得出这是徒劳的。我不愿再让她在这棵老橡树下多受一秒钟的罪。"
"我担心，露丝在这里待得越久，就会越苍白、越寒冷、越瘦削，直至她彻底从世间消逝。"

stop sound fadeout 1.0
stop ambience2 fadeout 1.0
stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  11月9日{vspace=1}  冰冷的手") )
play ambience "sfx/rain2.ogg" fadein 1.0
play music "bgm/Friendship.ogg" fadein 1.0
scene marcel_room_r
show luce w sad r:
    xpos 0.30 xanchor 0.5 ypos 0.5 yanchor 0.5
with wiperight_slow
window show dissolve

Luce "对不起，把这儿弄得一团糟……"
"露丝站在我卧室的门槛上，仍在瑟瑟发抖。"
"她的鞋袜已经脱去，此刻光着脚站着，苍白的小脚趾在木地板上蜷曲着。"
"她的脚趾白得吓人，与她的手指如出一辙。"
"露丝一向苍白，可如今她的皮肤简直毫无血色。"
"她仍穿着校服。水珠顺着裙摆滴落，在她脚边的地板上凝成一颗颗水珠。"
"露丝站立的地方正聚起一小滩水。待会儿我得收拾干净，不过现在……"
Marcel neutral u "就算你弄得一团糟，我也不介意。没关系的。你比我的房间重要多了。"
show luce w huh r with dissolve
Luce "你现在是这么说，可是……"
show luce w sigh r with dissolve
"露丝又抬手掩嘴咳嗽起来。她已经咳了相当多次；那低沉沙哑的咳声听起来很是痛苦。"
show luce w sad r with dissolve
Luce "要是你总得一次次跑来救我，你迟早会腻烦我的……"
Luce "我从没求你当我的骑士。"
Marcel smile u "你确实没求，可也许是我{i}自己{/i}想当呢。"
show luce w huh r with dissolve
Luce "可这不是在给你添麻烦吗？"
Marcel "你永远不会给我添麻烦的。"
"露丝从湿漉漉、散乱的刘海底下，狐疑地望着我。"
Luce "你当真吗？"
Marcel neutral u "我确定。无论发生什么，我都会一直这么说下去。"
Marcel frown u "你姐姐这样单单针对你，实在太不公平，我也没法袖手旁观，看着全班都任其发生。"
show luce w sigh r with dissolve
Luce "一直是这样子的……"
Marcel "唉，本{i}不该{/i}是这样的！"
show luce w huh r with dissolve
Luce "而你就要骑着你那高贵的战马，冲进来力挽狂澜啦？"
Marcel sad u "我试过了，可杜布瓦夫人根本不听我的。"
show luce w sad r with dissolve
Luce "她从来不听。我这位姐姐，固执得惊人。"
Marcel smile u "这怕是家传的。"
show luce w smile r with dissolve
Luce "呵……"
"露丝的唇角微微向上翘，露出一丝浅笑。那笑意太淡，不足以真正令人安心，但那终究是一个微笑。"
Luce "嗯，也许吧……"
Marcel neutral u "你敢那样当面顶撞杜布瓦夫人，真了不起。换作我，怕是做不到。"
Luce "这都是练出来的。你已经尽力了，玛塞尔。"
Marcel sad u "我猜你是锻炼得太多了。"
show luce w sad r with dissolve
Luce "我也这么觉得。我真的好厌倦这一切了。"
show luce w sigh r at twirl
Luce "我……好累……"
"露丝抽了抽鼻子。她的身体摇晃了一下，然后向前颓然倾倒。"

stop music fadeout 1.0

window hide dissolve
scene cg11 with wiperight_slow
play music "bgm/Confession.ogg" fadein 1.0
$ renpy.pause(1.0)
window show dissolve

"我冲上前去，赶在她瘫倒在地之前将她接住。"
"露丝的裙子是湿的，把我的制服也弄潮了，可我太过担心露丝，无暇顾念这些。"
Marcel "露丝！你还好吗？"
Luce "玛塞尔……？"
"露丝朝我眨了眨眼。她的金色睫毛显得比以往任何时候都要苍白。那双棕色的眼眸看上去雾蒙蒙的，难以聚焦。"
Luce "你又救了我一次。"
Marcel "可我却没能守护真正需要我的你。我真没用……"
Luce "你不是没用的。你是教室里唯一一个肯替我出头的人，这对我意义重大。"
Luce "我真的很感激。"
"露丝把头靠在我的胸口。她竟不曾试图从我怀里挣脱出去，可见她实在累得厉害。"
"我想我从未见过露丝如此彻底地依赖我。"
"若不是我如此担惊受怕地挂念着她，我或许会觉得这一幕颇为动人。"
"在风雨里站了将近一个钟头，想必已令她损耗不小。"
"露丝本就相当纤弱，而那样恶劣的天气，想必已把她仅存的那点儿力气也榨干了。"
Luce "你或许不是最出色的骑士，却是个好朋友。"
Marcel "你当真把我当成朋友吗？"
"露丝点了点头。"
Luce "在这座烂透了的学校里，你是唯一关心我的人；而我也只在乎你一个。"
Luce "我以为自己一辈子都不会想念这鬼地方的任何人，可也许，我会想念你。"
Luce "如果我让你失望了，我很抱歉……"
"我看着露丝那头灰白金色头发的头顶，皱起了眉头。"
"我不确定她在说些什么。也许她自己也不确定。她的声音沉重，近乎含混，说话时磕磕绊绊。"
Marcel "你不能穿着那身湿衣服。那样你永远也暖和不起来。"
Luce "可你抱着我的时候，我觉得很暖和。"
Luce "你并不想我离开，对吧？"
Marcel "当、当然不想！我绝不会把你赶出去！我说过要照看你，就一定要做到！"
Marcel "我太在乎你了，舍不得把你赶进寒夜里。"
Luce "那就好，真是松了口气。我都不记得以前有没有人跟我说过这样的话了……"
Marcel "「在乎你」？"
"露丝点了点头。"
Luce "上一个对我说这话的人，是我母亲。我已经三年没见过她了。"
Luce "我回家已经是很久以前的事了。我想念母亲的玛德琳蛋糕，想念她说笑话，也想念她的拥抱。"
Luce "我好想念她……"
"露丝抽了抽鼻子。我担心她正在哭。"
Marcel "哦，露丝……"
"我叹了口气。她听起来如此心神不宁，我能感到自己的心在同情之中随之碎裂。"
Marcel "我当不了你的母亲，但至少可以试着照顾照顾你。让我替你换身衣服，好不好？"
Luce "可我换什么呢？我总不能就这样光着身子留在你房间里吧……"
Marcel "不、不是那样……当然不是……"
"想都别想。"
Marcel "我有几件睡袍。你穿其中一件吧。"
Luce "几件睡袍……？"
"露丝挑了挑眉。"
Luce "你一定是出身富贵人家吧。我只买得起一件，还是法兰绒的。"
Luce "我干脆嫁进你家户口本子里算了。那样我就能买得起想要的好东西，还能住进巴黎呢！"
Luce "我总算能摆脱我姐姐了！"
Marcel "嗯……"
"我眨了眨眼，脸颊泛红。"
Marcel "你、你刚刚是说……结婚……？"
Luce "是的……"
"露丝虚弱地笑了笑。"
Luce "可我是在开玩笑啦。我知道那永远行不通。我们俩都是女子。"
Marcel "是啊。我们都是……女子……"
Luce "真可惜。"
Luce "你有没有兄弟可以介绍给我呀，玛塞尔？"
Marcel "没有，抱歉。我是独生子女。"
Luce "哼，问一问总不吃亏……"
Luce "当然啦，要是我真能遇上一位像你一样善良的男士，那未免太顺心了。我都不知道这世上到底有没有这样的人。"
"我不得不咽下喉头涌起的那团哽意。"
"要是露丝知道就好了……"
"可若是她当真发现我是个男孩，我想她不会允许我这样搂着她。"
"她绝不会容许我成为她的朋友，而我那些试图（却未能）保护她的举动，她也不会领情。"
"她想必会像我旧日学校里的同学们一样，对我嗤之以鼻，骂我是个怪物。"
"我没什么传统意义上的男子气概，称不上一个“真正的男人”，可我也不是女人。"
"我究竟是什么？"
"……也许这一切并不重要。至少眼下并不重要。露丝仍在发抖。"
Marcel "来吧，我给你换身衣服。你也该好好歇一歇。"
Luce "歇一歇……？太好了。我真的很累了……"
Marcel "看得出来。你说话就像喝醉了似的。"
Marcel "先在我床上坐下，我去给你拿件换的衣服。"

show image "border" onlayer border
scene marcel_room_r
$camera_move(-2500,800,400,0,0,'dissolve')
with wipeleft_slow

"我轻轻地把露丝放到床上，然后翻找抽屉，想找一件合适的睡袍。"
"我想我的衣服对露丝来说大多会太大，但这会儿想来也无所谓。眼下的当务之急，是为她找一件暖和干燥的衣物穿上；至于合不合身，倒在其次。"
"最终我选定了一件朴素的纯棉长袖睡袍，递给露丝。"

hide image "border" onlayer border
scene marcel_room_r:
    size (1920, 1080) crop (450, 0, 1440, 810)
show luce w neutral2 r:
    xpos 0.50 xanchor 0.5 ypos 0.50 yanchor 0.5
with wiperight_slow

Marcel u neutral "你要是愿意，就换这件吧。我发誓不看。"

show image "border" onlayer border
scene marcel_room_r
$camera_move(-2500,200,400,0,0,'dissolve')
with wipeleft_slow

"我再次背过身去，双臂交叠，执拗地凝望着卧室的一个角落——那儿搁着那面破裂的镜子和脸盆。"
"我看不见露丝的脸，却能感到她那带着询问的目光落在我背上。"
Luce neutral "你干嘛非要这样刻意别过脸去？"
Marcel u shock "我、我是想保全你的体面，所以才那样！"
Luce "有那么重要吗？我猜衣服底下我俩也没多大差别。我们俩都是女子。"
"那正是我一直让露丝信以为真的事，但真相远比这复杂。"
Luce "好吧，我想我自己也能把裙子脱下来……"
"我能听到身后露丝走动的声响。她站起身来，脚趾在地板上蜷缩着。指尖在布料上滑动，露丝伸手到背后去解开她那件黑色礼服背后的缎带。"
"露丝脱下身上的衣物，然后套上我为她备好的那件朴素睡袍。"
Luce n smile "啊，现在舒服多了。"

hide image "border" onlayer border
scene marcel_room_r:
    size (1920, 1080) crop (450, 0, 1440, 810)
show luce n neutral2 r:
    xpos 0.50 xanchor 0.5 ypos 0.50 yanchor 0.5
with wiperight_slow

"我回头看向露丝，脸颊发烫，只见她正坐在我的床沿，身上穿着我的睡袍。"
show luce n shy2 r with dissolve
Luce "那个……我躺下歇会儿，可以吗？"
Marcel u smile "当然可以。你爱待多久都行，殿下。"
show luce n happy2 r with dissolve
"我朝她鞠了一躬，逗得露丝咯咯笑了起来。"
show luce n smile2 r with dissolve
Luce "你像那样说话的时候，真像个骑士。"
"露丝在我的床上往后靠了靠，把被子拉到身上。她那头短短的浅金色头发在枕头四散铺开。"
show luce n sad2 r with dissolve
Luce "我多希望有一位英俊的王子，能这样对我屈膝行礼。"
Luce "要是他还能翻过学校的围墙来救我，那该多好。"
Marcel u sad "我倒希望不会有王子来救你。真要有那一天，我会想念你的。"
show luce n sigh2 r with dissolve
Luce "哦，你大可不必担心。不会有王子为一个我这样的姑娘而来的。我名下一枚杜卡特都没有。"
"露丝叹了口气。"
show luce n sad2 r with dissolve
Luce "我虽然看起来像个孩子，但我不是。我明白，要想改变命运，只能靠我自己。"
Luce "我可耗不起时间去做那些永远不会来的王子的梦。"
Luce "我得行动起来……"
Marcel u neutral "你这话说得不对。"

scene marcel_room_r blur:
    size (1920, 1080) crop (600, 60, 1152, 648)
show luce n huh3 r:
    xpos 0.50 xanchor 0.5
with dissolve

Luce "玛塞尔……？"
"我在床边、也就是露丝身旁坐下，然后斜眼看向她。"
Marcel u smile "你并不是孤身一人。你还有我呢。"
Marcel u ehe "我知道自己大多事情都不太在行，可我会尽我所能帮你；我保证。"
show luce n neutral3 r with dissolve
Luce "你是认真的吗？"
Marcel u smile "我说的是真的。"
Marcel "你要是愿意，今天剩下的时间都可以在这儿睡。我会跟布吕吉埃夫人说明你为什么没去上课。"
Marcel "你要是愿意，我甚至可以去跟她提一提杜布瓦夫人的所作所为。"
Marcel u sad "我不能任由这种事再继续下去了。"
Marcel u sigh "这样实在不对劲。"
show luce n sad3 r with dissolve
Luce "是不对，可这世上有太多事都不对了。"
show luce n sigh3 r with dissolve
Luce "我很高兴你这么在意我，但是……"
show luce n neutral3 r with dissolve
"露丝从她苍白的睫毛底下瞥向我，那睫毛羞怯地扇动着。"
Luce "谢谢你，玛塞尔。我很感激。"
show luce n smile3 r with dissolve
Luce "我真的很喜欢……你……"
show luce n sigh3 r with dissolve
"露丝闭上了眼睛。她的睫毛软软地、灰扑扑地合拢在一起。"
"没过多久，她的胸口便缓缓起伏起来。她已沉沉睡去。"

stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  11月9日{vspace=1}  思念") )
$ renpy.pause(0.8)
play music "bgm/Mysterious.ogg" fadein 1.0
scene sky3 with wiperight_slow
window show dissolve

"我安顿露丝睡下，然后独自匆匆赶去上剩下的课。"
"即便同学们鱼贯走进教室，露丝靠窗的那个座位仍旧空着。"
"布吕吉埃夫人点着名，念到露丝的名字时却顿住了。"

scene classroom_r
show al frown at center
with wipedown_slow

Bru "有谁知道露丝在哪儿吗？"
Noémie smile "夫人，她早上的课还在呢！"
Cla "你们说她是不是逃课了？"
Claa "不过，露丝平常不会这样呀……"
Mirabel shock "也许她身体不太舒服吧……"
"女孩子们把头凑到一处，开始窃窃私语——这正是她们素来如此的事。"
"在宁静而慵懒的米耶纳，除了嚼舌根，实在没有多少可供人消遣的活动。我的许多同学都沉迷于此道，我甚至可以说他们是此中行家。"
show al sigh with dissolve
"布吕吉埃夫人叹了口气，拍了拍手，示意大家安静。"
show al annoyed with dissolve
Bru "姑娘们，拜托，我只是问了个简单的问题。你们没理由就此叽叽喳喳说个不停。"
show al frown with dissolve
Bru "我再问一遍。有谁知道露丝可能在哪里？"
Marcel neutral u "嗯……"
"我低着头，怯怯地举起手。"
Marcel "夫人，我知道露丝在哪儿。"
show al neutral with dissolve
Bru "你真这么觉得？"
Marcel shy u "是、是的，那个……嗯……"
"尽管空气里弥漫着寒意，我仍能感到脸颊泛起了粉红。"
"我敢告诉同学们，露丝此刻正裹着我的睡袍，安安稳稳、暖烘烘地躺在我床上吗？"
"那十有八九要引起一阵骚动，即便我的同学们{i}确实{/i}误以为我们俩都是女孩。"
"我的姨妈知晓真相，哪怕旁人都不知情；我敢肯定，她会就“把别的女孩带进自己房间、还任由她们在我面前更衣”这件事，严厉地训诫我一两句。"
"露丝换衣服的时候，我并没有看她，但我终究还是听见了她的制服落到地板上的声响。"
"回想起那一幕，我的脸越发红了起来。"
"但愿我没有在自证其罪……"
show al annoyed with dissolve
Bru "怎么了，玛塞尔？你一下子变得好安静。你不是有话想跟我说吗？"
Marcel "哦，对、对，是这样。抱歉，夫人！"
"我结结巴巴地道歉，而正如意料之中的那样，惹得同学们笑出了声。"

show image "border" onlayer border
scene classroom_r:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

Cla "玛塞尔怎么了？"
Claa "她的眼神都发直了……"
Cla "她老是在走神做白日梦！"
Claaa "也许是因为她长得太高了！"
Claa "你这是什么意思？"
Claaa "你也可以说她的脑袋都飘到云端里去啦！"
Claa "这个笑话可真够烂的……"
Cla "我听了都觉得浑身难受。"
Cla "这种谐音双关语应该定为大罪。"
Claaa "喂！哪有那么差劲吧？！"
"所幸我的同学们并不知晓我这副窘态背后的真正缘由，而我但愿这份无知能一直保持下去。"
"倘若他们知道了，每当我谈起、甚至只是想起露丝时，就会在心底翻涌而起的那种奇异、朦胧又焦躁的情绪，他们的笑声便会戛然而止。"
"到那时，他们会鄙弃我。"
"他们会认为我有什么毛病，而说不定我确实如此。"
"我曾对任何旁人都没有过这样的感觉；我这一生中从未有过。"

hide image "border" onlayer border
scene classroom_r
show al annoyed at center
with wipeleft_slow

Marcel neutral u "露丝今天剩下的课都不会来上了。"
"顿了一顿之后，我终于开口说出话来。"
Marcel "她生病了。"
show al annoyed with dissolve
Bru "生病？"
"布吕吉埃夫人挑起了眉。"
Bru "这到底是怎么回事？"
Marcel sad u "都是下雨闹的，夫人。她，呃……"
"我再一次顿住，心中一阵不安。"
"我是否该提一提杜布瓦夫人与这整件事的牵连？"
"我倒是想提，可眼下或许不是合适的时机；不该在课堂上、在众人目光齐刷刷落在我身上的时候说。"
"我只能稍后再把这件事告诉布吕吉埃夫人了。"
Marcel neutral u "是因为雨水和寒气，夫人才弄成这样的。"
Marcel "露丝坐在窗边，窗玻璃太薄，寒气都钻了进来。再加上下雨，她就病倒了。"
show al neutral with dissolve
Bru "我明白了。"
show al frown with dissolve
Bru "好吧，既然露丝要为这么个荒唐理由错过功课，那就随她去吧。不过要是明年考试她挂了科，那可就是她自己的责任了。"
show al annoyed with dissolve
Bru "好了，姑娘们，今天下午我们要练一练你们的作文能力。"
"教室里响起一片齐刷刷的哀叹，其间夹杂着翻开簿册的声响。"
"我伸手拿起自己的课本和铅笔，然后顺从地低头做起笔记。"
"看样子所有人都把露丝忘了；每一个人都不例外，除了……"

scene classroom_r:
    size (1920, 1080) crop (0, 40, 1440, 810)
show claudine neutral2:
    xpos 0.35 xanchor 0.5 ypos 0.55 yanchor 0.5
with dissolve

Claudine "玛塞尔？"
"克洛蒂娜瞥了我一眼，那双碧绿的眼睛闪烁着好奇的光芒。"
show claudine neutral2 with dissolve
Claudine "你为什么不对布吕吉埃夫人说实话？"
Claudine "人人都知道露丝不是为了一点风雨才病的。"
Marcel sad u "我知道，可我觉得现在不是跟她说这事的好时机。"
show claudine huh2 with dissolve
Claudine "那，什么时{i}候{/i}才算好时机？"
Marcel neutral u "我说不准。我想也许等今天结束，去她的办公室再跟布吕吉埃夫人谈。那时候她更有空听我说，也不会有人在场打断。"
Claudine "这么说，你是打算去告杜布瓦夫人的状喽？"
Marcel "严格来说，我不觉得那叫告状。就像你说的，我只是说出实情——但绝不是为了制造戏剧性。"
Marcel huh u "我只是想为露丝好。"
show claudine neutral2 with dissolve
Claudine "那你觉得露丝会赞成你这么做吗？"
Marcel "是的，我愿意。她答应过我。"
show claudine huh2 with dissolve
Claudine "真的吗？呵，那可真是令人意外！"
show claudine neutral2 with dissolve
Claudine "露丝向来不爱兴风作浪。她不喜欢出风头。"
Marcel neutral u "正因为如此，我打算避开同学们窥探的目光——和耳朵——悄悄地护着她。"
show claudine smile2 with dissolve
Claudine "哎呀呀。你可真是思虑周全！"
show claudine neutral2 with dissolve
Claudine "那么，你为什么这般执着地要帮助小露丝呢，嗯？"
Marcel frown u "总得有人站出来。我不能眼睁睁看着杜布瓦夫人虐待她而坐视不管。倘若没有别人愿意挺身而出，那就由我来。"
Marcel "这不对……！"
show claudine laugh2 with dissolve
"克洛蒂娜咯咯笑了起来。"
Claudine "你可真是变得大胆了，玛塞尔！"
Marcel huh u "您真的这么觉得吗？"
"这一点我可不敢确定。"
show claudine smile2 with dissolve
"“大胆”这个形容词，是我最不会用来形容自己的词之一。"
"在巴黎的时候，我从未替自己说过话；不曾对我的同学们，更不曾对我的老师们。"
"我安静得像教堂里的一只老鼠，任凭同龄人肆意践踏我。"
"我甚至从未尝试过为自己辩护。和露丝一样，我也觉得那不值得费心。"
"不过，为了照看露丝，我已准备好不惜一切代价。"
Marcel neutral u "我也不知自己算不算‘大胆’……可露丝她……"
"她{i}究竟{/i}是什么？"
Marcel shy u "露丝她……对我很特别，我想要守护她。"
Marcel "若连试着去做都做不到，我又怎配自称是她的朋友。"
show claudine neutral2 with dissolve
Claudine "嗯。"
"克洛蒂娜合上课桌，手里拿着簿册，向后靠在椅背上。"
show claudine smile2 with dissolve
"她翘起一条腿叠在另一条腿上，然后朝我露出一个狡黠的微笑。"
Claudine "这么说，她只是朋友咯，嗯？"
Marcel "是、是的……不然还能是什么呢？"
show claudine laugh2 with dissolve
Claudine "这嘛，我{i}可{/i}不知道呢！不过我确实很好奇……"
show claudine smirk2 with dissolve
Claudine "每次你提起她，眼睛总是亮晶晶的。脸还红了呢！"
Marcel shockblush u "真、真的吗？"
show claudine laugh2 with dissolve
Claudine "就是！我眼光可尖了，这些事都逃不过我的眼睛。现在想低下头躲到头发后面去，可来不及啦！"
Marcel shy u "呃……"
"我的脊背一僵。"
"这么说，克洛蒂娜注意到我在做什么了。"
"我该对她多加小心才是。她是个鬼灵精，又非常敏锐。"
show claudine smile2 with dissolve
Claudine "嘛，你那么关心露丝，我觉得很好。我一直担忧着那个姑娘，我也觉得杜布瓦夫人的行径实在太不公平。"
show claudine sigh2 with dissolve
Claudine "我常常想着，要去把杜布瓦夫人那些见不得人的品行禀告布吕吉埃夫人，可我知道她绝不会相信我。"
Marcel neutral u "你喊‘狼来了’喊太多次了。"
show claudine huh2 with dissolve
Claudine "就是嘛！如今夫人却把我当成捣蛋鬼？这像话吗？！"
Marcel frown u "你{i}确实{/i}把那只蟾蜍带进了杜布瓦夫人的课堂……"
show claudine annoyed2 with dissolve
Claudine "那是很久以前的事了！"
Marcel shock u "那只不过是一个月前的事！"
show claudine laugh2 with dissolve
Claudine "就是嘛！已经很长时间了！"
show claudine smile2 with dissolve
Claudine "那么，我在想……"
Marcel neutral u "什么？"
Claudine "既然你那么执着地要帮你的小露丝，那或许我该跟你一起去。"
Claudine "我可以为你作证。毕竟我也在课堂上，我亲眼看到杜布瓦夫人当时有多过分。"
show claudine huh2 with dissolve
Claudine "单靠我们中的哪一个，布吕吉埃夫人或许都不会当真……可若我们一同去对她讲，她便会更愿意相信我们。"
Marcel shock u "嗯？"
"这可真是一个出人意料的进展。"
Marcel "你真的愿意帮我吗？"
show claudine smile2 with dissolve
Claudine "我没理由不帮。我自己也爱逗弄人，可我受不了看着弱小无助的人被这般没完没了地欺负。"
show claudine annoyed2 with dissolve
Claudine "我尤其受不了诺艾米为小露丝的不幸幸灾乐祸。真叫人恶心。"
Claudine "我真想让她出尽洋相！"
Marcel neutral u "那么，我们要一起行动？"
show claudine smile2 with dissolve
Claudine "是啊，一起！我喜欢这个说法！听着多顺耳。"
"克洛蒂娜咧嘴一笑，冲我露出满口珍珠般的白牙。"
show claudine laugh2 with dissolve
Claudine "你可要明白，玛塞尔，小露丝并不是你在学校里唯一的朋友。我也挺喜欢你的呢！"
show claudine smirk2 with dissolve
Claudine "再说……"
"克洛蒂娜的眼里亮起一簇顽皮的光。"
Claudine "我觉得这一切听起来相当有趣，你说是不是？"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
play ambience "sfx/birds.ogg" fadein 1.0
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  11月9日{vspace=1}  云开月明") )
scene sky with wiperight_slow
window show dissolve

"白昼渐渐流逝，雨云散去了。如今，天空澄澈而明蓝；散落在校园各处的积水，成了今天早些时候那场倾盆大雨唯一的印记。"
"最后一节课结束了，布吕吉埃夫人同其余的同班同学们一道走出了教室。"
"不过，克洛蒂娜如她所承诺的那样，留在了后面。"
"待所有人离去后，她转过身来看向我，唇边一抹会意的笑意若隐若现。"

stop ambience fadeout 3.0
play music "bgm/Claudine.ogg" fadein 1.0
scene classroom:
    size (1920, 1080) crop (0, 40, 1440, 810)
show claudine smile2:
    xpos 0.35 xanchor 0.5 ypos 0.55 yanchor 0.5
with wipedown_slow

Claudine "好了，玛塞尔。我们走吧。"
Marcel neutral u "去校长室？"
Claudine "正是。我希望你事先准备好说辞了！"
Marcel shock u "我、我还要准备说辞……？"
"我父亲或许是个演员，可我一向不擅长言辞。我总是在话语上绊倒，像一匹跛足的马……"
show claudine laugh2 with dissolve
"但令我宽慰的是，克洛蒂娜那张俏丽的脸很快便漾开了笑意。"
Claudine "傻瓜，你当然不需要说辞。又不是要你在歌剧院前表演。"
"谢天谢地。"
show claudine smile2 with dissolve
Claudine "你只需把事实告诉布吕吉埃夫人，让她知道你有多为露丝担忧。这就足以打动她的心了。"
Claudine "布吕吉埃夫人看似严厉，其实心软得很。"
"我想到我的三件睡袍、我的衬裙、我的厚袜子和我的印花裙，都整整齐齐地叠放在卧房的抽屉里。"
"是布吕吉埃夫人——我的阿尔贝汀姨妈——带我在巴黎四处奔走，买下这些昂贵的物件，连眼皮也不眨一下。"
"诚然，她是用我母亲的钱来购买那些东西的，可她还是抽出时间，帮我张罗齐崭新的生活所需的一切。"
"没有她，我真不知该怎么办。"
"我在米延逗留的这段时间，她待我颇有距离，可我知道她是关心我的。这一点她早已表露得再清楚不过。"
Marcel smile u "这不必你告诉我。"
"我也回以克洛蒂娜一个微笑。"
Marcel "我知道布吕吉埃夫人是位好人。"
show claudine laugh2 with dissolve
Claudine "那你就没什么好怕的了！"
show claudine smile2 with dissolve
Claudine "我们就去打动她的心吧。满怀深情、发自肺腑地讲讲亲爱的露丝的处境，她很快就会心软的。"
show claudine at twirl
"克洛蒂娜用她那尖尖的胳膊肘捅了捅我的腰侧。"
Claudine "当然，对你来说，满怀深情地谈论露丝应当不难。"
Marcel shy u "你、你在说些什么……？"
show claudine smirk2 with dissolve
Claudine "无非是说你在乎她呀！我看你脸上写得清清楚楚，一目了然，嘿嘿。"
Marcel "真、真的有这么明显吗？"
Claudine "再明显不过了！玛塞尔，若你愿听一句劝，千万别去玩牌；至少别赌钱。你很快就会输个倾家荡产！"
Claudine "你压根儿就没有什么扑克脸可言！"
Marcel sigh u "多谢你的忠告……咳。"
"我清了清嗓子，随即站起身来。"
Marcel neutral u "我们现在就去跟布吕吉埃夫人谈吧。"
show claudine laugh2 with dissolve
Claudine "嘿嘿嘿。你害羞了？"
Marcel shockblush u "没、没有……！"
show claudine smile2 with dissolve
Claudine "好了，我刚才跟你说什么来着？"
"克洛蒂娜咯咯地笑了起来。"
Claudine "你真是不擅长说谎。真不明白你何苦费那个劲。"
Marcel sigh u "你怕是要吃惊的。"
Marcel neutral u "总、总之……赶紧把这事了结吧。"
show claudine laugh2 with dissolve
Claudine "好。我来带路。我闭着眼都能摸到校长室。我去得够频繁了！"
Marcel sigh u "我觉得你不该为此这么得意。"
Claudine "我得意什么，由我自己做主！"
show claudine smile2 with dissolve
Claudine "屡屡受罚，却仍能留下来读书，这也算是件了不起的本事！"

play ambience "sfx/footsteps3.ogg" fadein 0.3
show claudine:
    ease 2.0 xpos 1.20

$ renpy.pause(0.8)

play sound "sfx/door.ogg"
stop ambience fadeout 0.5

"说罢，克洛蒂娜走出了教室，而我则亦步亦趋地跟在她的身后。"

play ambience "sfx/footsteps2.ogg"
scene yard
show claudine smile2:
    xpos -0.20 xanchor 0.5
    ease 5.0 xpos 1.2
with wiperight_slow

"我们穿过布满水洼的校园。"
"克洛蒂娜带我走进一栋我从未有机会进入的楼，领着我穿过一条狭窄的走廊，直到我们在一扇木门前停下。"

stop ambience fadeout 2.0
scene sky with wipeup_slow

"这扇门看起来并不起眼。"
"门上连一块说明这间屋子属于校长的黄铜铭牌都没有，不过我猜想，米延的风气与巴黎毕竟不同。"
"这里的一切都随意得多。"
play sound "sfx/knock.ogg"
"克洛蒂娜用指节轻快地叩了叩门。"
Claudine u smile "打扰了，布吕吉埃夫人？您在吗？"
"我听见门的那一侧传来纸张翻动的细微声响，还有一声咳嗽。"
Bru neutral_side "克洛蒂娜？是你吗？"
Claudine "是我！我来是为了谈一件要紧事。"
Bru "你又闯祸了，还是又要搞你那些愚蠢的恶作剧？"
"我听见布吕吉埃夫人重重地叹了口气。"
Bru "我现在没心情应付你的胡闹，顽皮的丫头。天已经不早，我想趁这功夫理一理学校的账目。你明天再来不行吗？"
Claudine "我倒也想这样，夫人，可是不行啊！我有非常重要的事要谈呢！这事十万火急，等不到明天！"
Bru "除非是生死攸关的大事，否则我不感兴趣。"
Claudine "可这有可能就是啊，夫人！很有可能呢！"
Claudine "我也不是一个人来的。我还带了别人来，她也想跟您谈谈！"
"我想，这该轮到我开口了……"
Marcel neutral u "那个……布、布吕吉埃夫人？那个……"
"对着一扇木门说话，而非对着人的脸，实在有些古怪。"
Marcel "我是玛塞尔。我也有话想说。"
Bru "玛塞尔，是吧……？"
"门那侧的纸张翻动声停了下来。"
play sound "sfx/chair.ogg"
"我听见一声吱呀，接着是脚步声。"
"门把手向右转动，随即门被向外拉开——几乎砸到我的头侧——露出了布吕吉埃夫人高大的身影。"

play sound "sfx/door.ogg"
scene office:
    size (1920, 1080) crop (240, 40, 1440, 810)
show al annoyed2 at center
with wipedown_slow

Claudine u annoyed "哼，她死活不肯给我开门，可一听到你的声音，不到一眨眼的功夫就放你进去了……"
Claudine "这还有公道吗？！"
show al frown2 with dissolve
Bru "原谅我，克洛蒂娜，可你素来以爱搞愚蠢恶作剧闻名，我实在难以把你的这些要求当真。"
Claudine "愚蠢的恶作剧？我吗？我才没有！"
show al sigh2 with dissolve
Bru "你还惯于夸大事实，如今便是明证。"
"布吕吉埃夫人翻了翻白眼。"
show al annoyed2 with dissolve
Bru "而玛塞尔就可靠得多了。既然她想见我，我没有异议。"
Claudine "哼。看来你是布吕吉埃夫人的宠儿呢，玛塞尔——真想不到！你还说自己不是老师的马屁精！"
"克洛蒂娜又用她那尖尖的胳膊肘捅了捅我的腰侧。我疼得直咧嘴。她可比看上去强壮得多。"
show al neutral2 with dissolve
Bru "那么，你们两个……"
"布吕吉埃夫人站在她办公室的门槛处，在克洛蒂娜和我之间来回打量了片刻。"
show al annoyed2 with dissolve
"她皱起了眉头。"
Bru "你们不进来吗？"
"我连忙照她的话去做，克洛蒂娜也是如此。我们并肩走进她的办公室，随即停住脚步；克洛蒂娜泰然自若，而我则局促不安。"

stop music fadeout 2.0

show image "border" onlayer border
scene office:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow
play music "bgm/Casual_day.ogg" fadein 1.0

"布吕吉埃夫人的办公室，与我在原来学校见过的校长办公室截然不同。"
"她的办公室是间相当狭小、朴素的屋子，墙上没有气派的肖像，也没有摆满奖杯的玻璃柜。"
"事实上，她的这处幽居一切都很务实，从那简朴的书桌到贴墙而立的书架，莫不如此。"
"布吕吉埃夫人的办公室远没有我最初担心的那样威严。事实上，它相当温馨。"
"布吕吉埃夫人让克洛蒂娜和我坐下；我们俩都听从了这道命令。"
"布吕吉埃夫人也坐了下来，隔着她的木桌面对着我们。"
"她好奇地打量着我们，十指交握，手肘撑在桌面上。"

hide image "border" onlayer border
scene office
show al frown:
    xpos 0.70 xanchor 0.5
show claudine smile:
    xpos 0.30 xanchor 0.5
with wipeleft_slow

Bru "你来找我，实在稀奇，玛塞尔。我想这还是头一回吧？"
Marcel neutral u "是、是的……"
show al annoyed with dissolve
Bru "我倒希望也能对你说同样的话，克洛蒂娜小姐。你进出我的办公室如此频繁，都快成这里的常驻物件了。"
show al sigh with dissolve
"我的姨妈叹了口气。"
show al neutral with dissolve
Bru "那么，出什么事了？你们两个之间闹了什么吗？"
Marcel u huh "哦，不是的，夫人，这事与克洛蒂娜和我无关。"
show al annoyed with dissolve
Bru "那么，这到底{i}是{/i}怎么回事……？"
Marcel "其实是为了露丝的事。你瞧……"
"我低下头，仍有些忐忑（我的头脑总把这样的办公室与惩罚联系在一起），随后开始解释起来。"
"我向布吕吉埃夫人说明了露丝今天下午缺课的真实原因，杜布瓦夫人如何命令她站在外面的雨里，以及可怜的露丝因此病得多么厉害。"
"我向她讲了那只蟾蜍的事，如何明明是露丝替人背了罪过、错不在她，她却因此被鞭挞得双手红肿破皮。"
"我还向她讲了杜布瓦夫人总是刻意针对露丝，以及那些不公的惩罚与刻薄的言语。"
"我说话时，布吕吉埃夫人静静地听着，等我说完，她又沉默了好一会儿。"
"她皱着眉，往后靠进椅背，十指交缠在一起，然后说道……"
show al frown with dissolve
Bru "那么，你是说杜布瓦夫人一直在亏待露丝？"
Marcel huh u "是的，正是如此。"
show al sigh with dissolve
Bru "嗯……"
show al neutral with dissolve
Bru "我也听说过杜布瓦夫人待露丝不好的传闻，可我总以为那是我那些傻丫头在闲言碎语。你也知道她们那德性。"
Marcel frown u "我知道她们那德性，夫人，可这不是无中生有的闲谈。全都是真的。"
show al annoyed with dissolve
Bru "那你对此又有什么要说的，克洛蒂娜……？虽说你的话往往不怎么顶用。"
show claudine shock at bounce
Claudine "那你那句话{i}又{/i}是什么意思？"
show al sigh with dissolve
Bru "只是我奇怪，你那张舌头说了那么多谎，怎么还没黑得像煤一样。"
show claudine huh with dissolve
Claudine "我知道自己算不上最可信的学生，夫人，可我绝不会在这类事上说谎！"
show claudine sad with dissolve
Claudine "杜布瓦夫人待可怜的小露丝{i}真{/i}是狠毒。哎呀，叫我实在看不过去！"
show al neutral with dissolve
Bru "你亲眼见过玛塞尔所说的那些不公正的惩罚吗？"
show claudine neutral with dissolve
Claudine "想{i}不{/i}看见都难。杜布瓦夫人对可怜的露丝的厌恶，简直毫不掩饰。"
Claudine "蟾蜍那件事露丝挨打时，我并不在课堂，但今天早晨我是在的。"
show claudine huh with dissolve
Claudine "你瞧，炉火灭了，杜布瓦夫人要露丝去拿些柴火来。不巧雨下得正大，露丝委实不太想去。"
Claudine "玛塞尔提议由她替露丝去，杜布瓦夫人却不肯。"
show claudine neutral with dissolve
Claudine "她一直命令露丝去柴房，我想无非是为了折磨她罢了。"
Claudine "露丝想要推辞，这一来，杜布瓦夫人便罚她站到倾盆大雨中去！"
show claudine shock with dissolve
Claudine "露丝就在校园里那棵老橡树下站了将近一个钟头！可怜她浑身湿透，肯定染上重感冒了。"
show claudine annoyed with dissolve
Claudine "天哪，说不定还要得肺炎呢！"
show al annoyed with dissolve
Bru "我明白了……"
show claudine neutral with dissolve
"布吕吉埃夫人一只手托住下巴，看起来陷入了沉思。"
show al sigh with dissolve
Bru "这确实比我料想的要严重得多。"
show al neutral with dissolve
Bru "虽然我也听过一些说法，可本以为或许是被夸大其词了。"
show al annoyed with dissolve
Bru "你们知道露丝与杜布瓦夫人的关系吧？"
Marcel neutral u "露丝告诉过我。她说她们是姐妹……"
show al neutral with dissolve
Bru "不错。"
"布吕吉埃夫人点了点头。"
show al annoyed with dissolve
Bru "我自己也有个妹妹。小时候我们常常争吵，可我心里始终是为她好的。"
Bru "我原以为，杜布瓦夫人对露丝严厉，许是出于想帮她的心。"
show al sigh with dissolve
Bru "我担心仅凭猜测便如此打探人家的家事，未免有失礼数。"
show al sad with dissolve
Bru "毕竟，露丝自己从未站出来说过这些事……"
Marcel neutral u "露丝担心，如果她出面作证反对杜布瓦夫人，日后杜布瓦夫人会对她更加狠毒。"
Marcel "我求了她好几回，她才答应我把这件事告诉您，夫人——不过，即便她不肯答应，我或许也会照实说出来。"
Marcel frown u "杜布瓦夫人太过分了。再这样下去，露丝恐怕真有危险。"
show al smile with dissolve
Bru "我能理解。谢谢你这样照顾你的同学，玛塞尔——克洛蒂娜，也谢谢你。"
Marcel shy u "啊、啊……呃……那、那没什么……"
Bru "你这么说，可我相信把这件事告诉我，一定需要很大的勇气。我不确定当初那个玛塞尔做不做得到。"
Marcel "嗯，或、或许吧……"
show claudine neutral with dissolve
Claudine "哦……？"
"克洛蒂娜在布吕吉埃夫人和我之间来回瞟着，眉头紧锁。"
Claudine "您说的『从前的玛塞尔』是什么意思？"
Claudine "布吕吉埃夫人，您是不是知道一些关于玛塞尔的事，而我还不知道？"
show al neutral with dissolve
Bru "这不是你该操心的事，克洛蒂娜。"
show claudine shock at bounce
Claudine "可我{i}就是{/i}担心！我想知道你们到底在说什么！"
show al annoyed with dissolve
Bru "其实也没什么大不了的。真相恐怕会让你失望——不过你若是执意要知道……"
"布吕吉埃夫人清了清嗓子，然后给了克洛蒂娜一个我明白是半真半假的回答。"
Bru "我认识玛塞尔的母亲有些年头了——当然也认识玛塞尔。我是这家人的朋友，也是一心为玛塞尔好。"
Bru "她的母亲托我照看她。"
show claudine huh with dissolve
Claudine "哦，原来是这样。我一点儿都不知道。"
show claudine annoyed with dissolve
"克洛蒂娜看了看我，随即撅起了嘴。"
Claudine "玛塞尔！你为什么不告诉我你认识布吕吉埃夫人？！为什么要瞒得密不透风？！"
Marcel shy u "我真的不是有心要保密……"
"我无力地撒了个谎。"
Marcel "我只是……觉得没必要让你知道这件事。"
show claudine shock with dissolve
Claudine "可我{i}就是喜欢{/i}知道事情！我{i}受不了{/i}被蒙在鼓里！"
show al annoyed with dissolve
Bru "那么克洛蒂娜，你这一生就必须准备好承受许许多多的失望。要一个人无所不知，既不可能——也不可取。"
Claudine "可我至少想多了解一点我自己的朋友！"
show al neutral with dissolve
Bru "这么说，你是玛塞尔的朋友了？"
show claudine annoyed with dissolve
Claudine "我以为我们是朋友，结果她居然瞒着我那么多事！"
"要是克洛蒂娜知道我还在瞒着她多少别的事，她还会这么热切地要与我结为朋友吗？"
show al smile with dissolve
Bru "玛塞尔，不得不说，我没想到你会与克洛蒂娜交好，偏偏是她……不过，如果你们俩能彼此谅解，我也很欣慰。"
Bru "想必你母亲看到你与同学们相处融洽，也会很高兴。"
show claudine neutral with dissolve
"布吕吉埃夫人温和地朝我笑了笑。"
Bru "你不仅交了新朋友，还来同我谈露丝的安危。这显示出你新长出的几分自信。"
Marcel neutral u "那您打算怎么处置露丝的事？您能帮帮她吗？"
show al neutral with dissolve
Bru "我会尽我所能。"
show al annoyed with dissolve
Bru "等露丝好一些，我会就这些事同她谈谈。无论这会让她有多难堪，她若能亲口证实，自然是再好不过。"
Bru "在那之后，我会去同杜布瓦夫人谈。"
show al frown with dissolve
Bru "如果你们所说属实——而我也没理由怀疑你——那这确实是一件非常严重的事。"
Bru "我是这所学校的校长，我不能坐视我自己的老师欺凌我的学生。这是极不道德的。"
Bru "既然我已得知露丝的遭遇，我会竭尽全力将它纠正过来。"
Bru "我向你保证。"
Marcel sigh u "哦，谢天谢地……！"
"我靠进椅背，低低地舒出一口气，如释重负。"
"我很庆幸这次来布吕吉埃夫人的办公室没有白费。她打算去和露丝谈谈，然后她再去找杜布瓦夫人。"
"希望她会狠狠地教训杜布瓦夫人一顿。"
"我还没天真到以为这就能解决露丝所有的难题，但至少这是一个开始。"
"也许露丝终于能在这么多年之后，于米延过上平静的生活。这就是我对她唯一的期盼。"
"倘若世上有人配得上幸福，那便是露丝。"
"我只想让她展露笑颜。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  11月9日{vspace=1}  消失的身影") )
play music "bgm/Night.ogg" fadein 1.0
scene marcel_room with wiperight_slow
window show dissolve

"晚些时候，我回到自己的房间，为与布吕吉埃夫人谈话后的成功而精神振奋。"
"我迫不及待地想把这条好消息告诉露丝，只可惜……"
Marcel shock u "露丝！露丝，你还在这里吗？"
"我的呼唤只换来一片沉寂。露丝没有回应，这我本应该料到的。"
"她人不在这儿，又怎能回应呢？"
"我的房间空无一人。"
"床铺的被子已经铺好，枕头也拍松了，可枕上却没有那颗熟悉的、灰金色头发的脑袋。"
"与此同时，借给露丝的那件睡袍已被整齐叠好，如今静静躺在我的床上，长长的袖子交叠在一起。"
"至于露丝去了哪里，我却毫无头绪。"
Marcel sad u "露丝……？"
"我又唤了一声她的名字——照如今的情形看，注定是徒劳的——然后叹了口气。"
"露丝一定是回了学校宿舍，或者去了餐厅。"
"我想她今天没吃多少东西。她一定是饿了。"
"也许，要是我动作快，我也可以亲自去一趟餐厅，赶在它打烊前弄点吃的……"
"可现在，食物是我最无暇顾及的东西。"
"我的脑子被露丝占据得满满的，无暇理会胃里那阵揪心的饥饿。"
"我本想告诉露丝我与布吕吉埃夫人会面的成功，可我现在根本没法这么做。"
"我只得等到下次见到她，可那又会是什么时候呢？"
"距我上次见到她还不到五个小时，我却已经开始想她了。"
"我不明白为什么会这样。"
"我为何这样黏人？"
"……好吧，我试着安慰自己，倘若我赖在这儿，像个愁眉苦脸、哀哀戚戚的幽灵一般，那我是找不到露丝的。"
"我转过身，准备再次离开卧室——可有什么东西吸引了我的目光。"

show image "border" onlayer border
scene marcel_room:
    size (1920, 1080) crop (550, 250, 640, 360)
with wipeleft_slow

"在我的床头柜上，一摞书的上头，放着一样貌似便条的东西。它叠得仔细而齐整，很像我的那件睡袍，这让我心生疑惑。"
"这是露丝留的吗？"
"我拿起那张便条，险些带乱了我的书，小心翼翼地将其展平。自始至终，我的双手都在颤抖。"

window hide dissolve
scene black with wipedown_slow
nvl show dissolve

nv "{i}亲爱的玛塞尔：{/i}"
nv "{i}非常感谢你让我觉得自己被人这样珍爱着。说真的，在这所学校里，我从未有过像你这样的朋友——事实上，我从来就没有过任何朋友。{/i}"
nv "{i}你一次又一次地竭力维护我，尽管我们初次交谈时我对你那样冷淡。你本没有理由来帮我，可你还是这样做了，我感激不尽。{/i}"
nv "{i}这一切对我真的非常重要，正因如此，写下这些话才让我如此痛心。{/i}"
nvl clear
nv "{i}我已尽力在这里苦苦支撑，但我再也无法忍受待在这所学校了。我的姐姐一直折磨我，而今天的事正是压垮我的最后一根稻草。{/i}"
nv "{i}我很倔强，也不肯认输，但姐姐已经把我拖垮了。我担心，若我留在这里，她只会继续伤害我——那到那时我该怎么办？{/i}"
nv "{i}我很害怕。{/i}"
nvl clear
nv "{i}我想念父母，想念从前的家。我已经好几年没见过他们了，我怕若再在这里待下去，会忘记他们可亲的面容。{/i}"
nv "{i}所以，今晚我就要回家去。{/i}"
nv "{i}我本打算一声不响地离开，心想反正也不会有人想念我，可你却把事情搅得复杂了许多。{/i}"
nv "{i}我知道至少得让你知道，我不能就这样悄悄溜走，所以才写了这封信。{/i}"
nv "{i}请你不要慌张，也不要来找我。你已经为我做了那么多，我实在不忍让你再为我担忧。我只希望你知道，我的决定并不是因为你做得不够好。你能帮的，终究是有限的。{/i}"
nv "{i}现在我必须自己拿主意了。我恐怕，这是我能真正快乐的唯一办法。{/i}"
nvl clear
nv "{i}谢谢你，玛塞尔，谢谢你一直做我的朋友，直到最后。等我回到父母身边，我仍会想着你，我想我会想念你的……{/i}"
nv "{i}可这所可悲的学校里的其他一切，我丝毫不怀念，更绝不会怀念我的姐姐。{/i}"
nv "{i}爱你的露丝{/i}"
nvl clear

nvl hide dissolve
scene marcel_room:
    size (1920, 1080) crop (550, 250, 640, 360)
with wipeup_slow
window show dissolve

"我凝视着这张便条，上面是露丝工整的手写草书。她一定是撕下一本习字簿的纸页来写的，因为纸面上布满了淡蓝色的横线，正如露丝自己的血管一般。"
"露丝那苍白如纸的皮肤下，青筋隐隐浮现，颇为惊人。今天在我把她从倾盆大雨中迎进屋里之后，它们比以往任何时候都更清晰可见。"
"我从未见过她如此苍白、如此纤弱。她就像一个素瓷娃娃……"
"而现在她竟打算逃走。"
"那个仿佛会被发间雨珠压垮的露丝，已经离开了。"
"她这副模样怎么逃得走？她连米延都出不去！"
"露丝自己都说她身无分文。她连坐公共马车的钱都出不起，更别说火车了……！"
"露丝是打算穿着她那身潮漉漉的校服，顶着这无情的天气，就这么一路徒步走去吗？"
"假如杜布瓦夫人今早没能要了她的命，那么一路跋涉回她家去，想必也一定会！"
"我的脑海里骤然涌上一幅幅骇人的景象：露丝躺在某条路沟里，天色越来越暗。她把行囊紧抱在胸前，那里面装着她姐姐还没来得及抢走的寥寥几件微薄家当，竭力抵御着寒冷……"
"可到头来，她还是撑不住。"
"这念头太可怕了。我决不能让它发生！"

hide image "border" onlayer border
scene marcel_room
with wipeup_slow

"露丝也许叮嘱过我不要去找她，可我怎能照办？抛下她，无异于判她死刑！"
"露丝不可能走得太远。她留在我床上、叠得整整齐齐的那件睡袍，摸上去还带着暖意，这说明她脱下它必定还不到半个钟头。"
"只要我动作够快，也许还能找到她。"
"我不确定她究竟去了哪里，不过这不要紧。我会一直找下去，无论要花多久，直到我们重逢。"
"露丝是我第一个、也是最珍视的朋友。我一直设法保护她免受她姐姐所害，收效甚微，但至少我还能试着保护她，免于伤害她自己。"
play sound "sfx/door.ogg"
"我把露丝的信塞进口袋，猛地推开卧室的门，一路祈祷着我能尽快找到她，少出些波折。"
"{i}求您了，上帝，{/i}我恳求着，{i}让我及时赶到露丝身边。让我帮她，趁她还来不及做出任何傻事。倘若她受了伤，我真不知该怎么办——我也不想知道。{/i}"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  11月9日{vspace=1}  绝望") )
play ambience "sfx/run.ogg" fadein 1.0
play ambience2 "sfx/night_amb.ogg" fadein 1.0
play music "bgm/Mysterious.ogg" fadein 1.0
scene village_n with wiperight_slow
window show dissolve

Marcel u sad "哈……哈……哈……"
"我大口喘息，每一次呼气，胸口都窜起一阵刺痛。"
"我把一只手按在胸口，疼得直皱眉头。"
"过去一个钟头，我一直像个着了魔的女人般在米延的街道上飞奔，四处寻找露丝，却连她的一丝踪影也没见着。"
"我问了几位一脸茫然的旁观者，是否看见一个穿着我校服、提着行囊的姑娘沿街走过，可他们都摇了摇头。"
"在村里搜寻时，我不禁寻思，明天布吕吉埃夫人会不会为我的失仪责骂我。她学校里的姑娘本该时时端庄得体，可我却几乎没有照这些规矩去做。"
"我穿着她学校的制服在村里飞奔，鞋上沾满泥点，脸因劳累而涨红，这对她那所古老学府的名声恐怕没什么好处。"
"我此刻的举止没有一点淑女的样子——可如今，淑女风范是我最无暇顾及的事。"
"我只想找到露丝。其他一切都无关紧要。"
"我也不知道自己找了多久，只觉得好像已过了好几个钟头。鞋子开始磨脚了，我还扭伤了右脚踝。疼得很，可我没有停下。"
"我想，如今除了死亡，没有什么能让我停下。"

scene sky_n with wipeup_slow

"天空缀满繁星，米延街道两旁那些古雅的店铺早已打烊。"
"我在米延的头一夜，月亮还瘦瘦的、如一弯钩月，如今却低悬在天际，圆润如一颗珍珠。"
"夜空很美，我却无心欣赏。我还没找到露丝，又怎能顾得上这些？"
"我试着保持乐观，可如今我却开始担心，自己怕是永远也找不到她了。"
"若她不在村里，她又能在哪儿呢……？"
"她该不会已经回学校去了吧？这也说不定，毕竟她已无处可去——但不，我不信她会这么做。"
"露丝很固执。她在信里也是这么说的。她绝不会这么轻易认输。"
"她终归没能挤上那班公共马车吧？"

scene village_n with wipedown_slow

"就在我穿梭于米安街巷、四处搜寻她的当口，她或许已经踏上前往讷韦尔的路了。"
"倘若她已经把米安甩在身后，我就再也找不到她了……！"

stop ambience fadeout 1.0

"我在面包房旁停下脚步——仿佛已是许久以前，我曾在这里为露丝买下那些玛德琳蛋糕——而后蹲下身子。隔着鞋袜，我揉捏着阵阵作痛的脚趾，不由皱起了眉。"
"露丝会去哪儿呢？她身上分文没有，此刻当真会坐在某辆公共马车上吗？"
"除非露丝去学了扒窃——这似乎又与她的性情大不相符——否则她绝无离弃米安的钱财手段。"
"我确信她仍在这里。她{i}一定{/i}还在这里——可究竟在何处？"
"我已把各地都寻遍了……"
Marcel shock u "哦……！"
"蓦地，一个念头涌上心头。在我搜寻那难以捉摸的露丝的过程中，还有一处地方未曾踏足；那地方离学校不算太远。"
"她一定在那里。她{i}一定{/i}在那里。"
"若她不在，我真不知该如何是好。"

stop ambience2 fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  11月9日{vspace=1}  失而复得") )
play music "bgm/Sad.ogg" fadein 1.0
play ambience "sfx/night_amb.ogg" fadein 1.0
scene lake_n with wiperight_slow
window show dissolve

Marcel shock u "露丝……！"
"我透过凉薄的空气呼唤她。一阵猛烈的风正开始刮起，它撩起我校服裙的裙摆。"
"我仓皇寻觅，鞋子和长袜上已沾满尘土，可眼下这些都无关紧要了。"
"哦……我想我能看见她了。"
Marcel "露丝……！"
Luce sad "啊？"

scene lake_n:
    size (1920, 1080) crop (400, 160, 1440, 810)
show luce sad2 n:
    xpos 0.5 xanchor 0.5 ypos 0.5 yanchor 0.5
with wiperight_slow

"露丝果然在这里。她正坐在湖边一棵树下。"
"她的旅行包就搁在身旁，一角微微凹陷，双膝蜷起，抵在下颏之下。"
"她双臂缠着瘦削的腿，宛如藤蔓一般，头枕在膝上——至少在我到来之前一直如此。"
show luce huh2 n with dissolve
"听到我的声音，露丝抬起头来，苍白的眼眸在渐渐逼近的黑暗里眨动。"
"此刻的湖畔十分幽暗，两旁树木高耸。大多数树已卸尽了秋叶，嶙峋的枝桠直刺向天，然而它们遮挡月光却绰绰有余。"
"只有几缕银光能够蜿蜒穿过枝桠之间。"
"湖面此刻望去几乎黑透了。在那凝滞如柏油的水面上，我几乎看不清倒映的星光。"
"我打了个寒颤。"
"风比先前刮得更猛了，可此刻我怎能去担忧这些呢？"
"除了露丝，我什么都不愿去想。"
play sound "sfx/rustle.ogg"
"我朝她奔去，险些被一段外露的树根绊倒。"

scene lake_n blur:
    size (1920, 1080) crop (420, 200, 1152, 648)
show luce huh3 n:
    xpos 0.5 xanchor 0.5
with dissolve

"我在露丝面前跪下，握住她的双手。我把自己的手指紧紧缠上她的，心里惶恐——我想，若是松开手，她便会化为一缕烟消散。"
"我仍无法完全确定这不是幻象……"
"可是幻象绝不会有露丝那可怜的指尖这样冰凉。"
Marcel sad u "露丝……噢，露丝……"
"我抽了抽鼻子。胸口痛苦地起伏着。"
"好一会儿我才察觉，双眼正被咸涩的泪水刺得发疼。"
Marcel shock u "露丝，你在这里待了多久了？"
show luce sad3 n with dissolve
"露丝别过头去，双颊泛起红晕。"
Luce "没、没多久……"
Marcel u frown "『没多久』是多久？"
show luce neutral3 n with dissolve
Luce "我想，大概一个多小时？我说不准。"
show luce sad3 n with dissolve
Luce "我觉得自己好像在这儿待了不知多久，可从另一头说，或许也并没有那么久。"
"我把露丝额前的刘海拨开，手掌贴在她裸露的额头上。烫得惊人；着实令人心惊。"
Marcel u sad "露丝，你的手指冻得冰凉，可额头却烫得厉害。你一定是病了！你这个样子，哪儿也去不了！"
"我瞥向搁在露丝身侧、依偎着树根的那只旅行包。"
Marcel u huh "你原来真的打算逃跑吗？"
show luce neutral3 n with dissolve
Luce "原本是这么想的……"
show luce sad3 n with dissolve
Luce "为了这个，我连我姐姐的包都偷来了。逃跑这件事，我已经谋划了一阵子。"
Marcel "那你身无分文，又打算怎么赶路呢？"
show luce neutral3 n with dissolve
Luce "我拿了一些我姐姐的钱。"
Marcel shock u "所以，你是偷了她的钱？！"
Luce "这个嘛……我本可以说我打算还回去，可说实话，我从没打算再回那所学校。"
Luce "我想这确实算是『偷』，可{i}她{/i}这些年从我这里偷走的东西太多了，我一点也不觉得愧疚。"
show luce sigh3 n with dissolve
"露丝抽了一下鼻子。我分不清那究竟是由于落泪（在黑暗里实在难以辨明），还是她正染上感冒的初兆。"
show luce sad3 n with dissolve
Luce "不过，我失算了。"
Marcel sad u "什么意思？发生什么事了？"
show luce neutral3 n with dissolve
Luce "我在等公共马车。车来了，我让车夫看了我的钱，可他不肯收。"
show luce sad3 n with dissolve
Luce "他只看了我一眼校服，就推断出我是从村里的学校逃出来的。"
Luce "他说他不能收我的钱——他不知道这钱是从哪儿来的——而且他也不肯让这么小的姑娘深夜里独自搭车。"
Luce "我想，他也是用他自己的方式在为我担心……"
show luce sigh3 n with dissolve
Luce "可我倒宁愿他没有这样。"
Marcel shock u "可我，我倒是庆幸他这么做了。换作是我，也会做同样的事！"
show luce neutral3 n with dissolve
Luce "我知道你会，玛塞尔。你总是为我操心。"
Marcel frown u "我当然该操心！这么冷的天，随时都可能下雨，你竟打算从学校里逃跑……"
"我顿了顿，随即深吸一口气。我得让自己冷静下来。"
"我来这儿是为了安慰露丝，而不是苛责她。她已经受过太多责备了，而且多半并非出于她自己的过错。"
Marcel sad u "我好害怕。我生怕你真的已经走了！"
show luce sad3 n with dissolve
Luce "可我不是叫你别怕吗。我信上写了呀。我不希望你为我担心……"
Marcel shock u "我当然会为你担心，你这个傻丫头！你是我最好的朋友！"
Marcel "你在纸上写什么都可以——就算你写草是粉色的，我也不在乎——可那并不能让它变成真的！"
show luce smile3 n with dissolve
Luce "……呵。"
"露丝轻轻笑了。就笑意而言，这实在算不上多么令人信服。那笑声听来苍凉、疲惫、空落落的。"
Luce "或许你说得也有道理。"
show luce sad3 n with dissolve
Luce "自从我踏进这所可怕的学校起，我就一直盼着逃跑。只是我没想到，事情会变成这样。"
show luce sigh3 n with dissolve
Luce "我真是个傻瓜……"
"露丝可怜兮兮地打了个喷嚏。倘若她先前没有着凉，那么在冷风里坐了这么久之后，此刻也必定染上风寒了。"
Marcel sad u "你不是傻瓜，露丝。"
show luce neutral3 n with dissolve
Luce "可公共马车的车夫就是不肯收我的钱。要是穿了姐姐的衣服，说不定我就能骗过他……"
Marcel smile u "我看杜布瓦夫人的衣服你也穿不下。你比她矮。"
show luce frown3 n with dissolve
Luce "嗯，唔，倒也是。"
show luce sigh3 n with dissolve
Luce "我比谁都矮一截。真不公平。"
"露丝又打了个喷嚏。我感觉到她的身子在我指下微微颤抖。"
Marcel neutral u "喂，你浑身都冻透了。"
Marcel "不如我们回学校去吧？我把你姐姐的包和钱还回去，你就蜷在我床上歇着。就当什么都没发生过。"
show luce neutral3 n with dissolve
Luce "就当什么都没发生过……"
Marcel smile u "没错！我们把这一切都抛到脑后吧，好不好？"
show luce huh3 n with dissolve
Luce "玛塞尔……"
play sound "sfx/rustle.ogg"
"我听见露丝在挪动。"
"在黑暗里很难看清她的神情，但我仍能辨认出她的五官：双目微眯，双唇紧抿。"
show luce frown3 n with dissolve
"她为何那样冷冷地看着我……？"
Luce "你叫我回去，说得倒轻巧，可我做不到。现在不行。"
Marcel shock u "那你又能去哪儿呢？！"
Luce "我不知道。这个我还得再想想。可{i}我{/i}确实知道，我不想回那所学校。"
Luce "我再也不想靠近我姐姐半步。我不想任她折磨我——等她发现我拿了她的钱，她一定会折磨我的。"
Luce "我的日子就再也过不下去了。她现在就已经在拼命把我的生活变成活生生的地狱。"
show luce neutral3 n with dissolve
Luce "我做不到……"
"露丝的脸上已褪尽一切情绪，可她的肢体语言却泄露了真实的心绪。"
"我坐得离露丝那么近，跪在她身侧，近到能感觉到她在发抖，而那寒冷绝不是罪魁祸首。"
"她这样颤抖，是因为害怕；甚至是惊恐。"
"她就那么怕她的姐姐吗，宁可一直这样守在湖边，活活冻死，也不愿回去面对她？"
"或许露丝觉得，冻死总比死在姐姐手里来得平静，可是……"
Marcel frown u "不是这样的。"
show luce huh3 n with dissolve
Luce "玛塞尔……？"
"露丝朝我眨眨眼，褐色的眼眸下聚拢着阴影。"
show luce neutral3 n with dissolve
Luce "你在说什么啊？"
Marcel "你姐姐不会惩罚你的。我不会让她得逞！"
Luce "这话……你这么说真的很体贴，可是——"
Marcel "露丝，我知道我到目前为止没能好好保护你，可我真的是在努力！"
Marcel "今天早些时候，我和克洛蒂娜去见了校长。"
show luce huh3 n with dissolve
Luce "你们跟布吕吉埃夫人谈了……？"
Marcel neutral u "没错。我们把你和姐姐之间发生的一切都告诉了她。"
Marcel "她说她会让事情回到正轨，这样杜布瓦夫人就不能再虐待你了——可你要是逃跑，这一切就永远不会实现！"
Marcel frown u "你若真想解决这个问题，就得正面去面对它！"
"我明白，这番话由我说出口，实在虚伪至极。"
"我难道不也同样逃避过自己的难题，正如露丝此刻这般吗？"
"我把母亲留在巴黎，独自来到米安，为的是开始一段新的生活，摆脱与父亲牵连所带来的社会污名。"
"也许我确实做得懦弱，可我不愿让露丝重蹈同样的覆辙。"
show luce frown3 n with dissolve
"不过，露丝似乎并未被我的说辞打动。她望着我，眉头紧锁。"
Luce "你说得倒轻巧，玛塞尔。"
show luce annoyed3 n with dissolve
Luce "你一直给我讲这些金玉良言，可你自己根本不用去践行其中任何一条！"
Luce "你不知道我过的是什么样的日子——我永远活在恐惧里，生怕姐姐又捏造出我什么新的错处来责罚我！"
Luce "这三年来我一直痛苦不堪，却从来没有人试图帮我！"
Marcel shock u "不是这样的！{i}我{/i}就在帮你，露丝！"
show luce frown3 n with dissolve
Luce "我知道你在帮我，可已经太迟了！我已经受够了，我好累！"
show luce sad3 n with dissolve
Luce "我真的……好累……"
"露丝凝望着湖面。湖水在面前铺展开来，水面幽暗而平展，宛如黑曜石。"
show luce neutral3 n with dissolve
Luce "你知道吗……"
"露丝咽了口唾沫。"
show luce sad3 n with dissolve
Luce "我坐在这里，努力抵御寒气的时候，竟开始想，若是我跳进那片湖里，是不是也不会太糟糕。"
Marcel neutral u "可你为什么要——"
"那句话才吐出一半，尚不成句，我便猛然领悟了露丝话语背后全部的含义。"
"我倒抽一口凉气。"
Marcel u shock "你不会是说……"
show luce frown3 n with dissolve
Luce "不，我是认真的。"
show luce sad3 n with dissolve
Luce "我想，若是我就这样……任凭湖水带我走，也许会更容易些，我猜。"
Luce "若我乘公共马车逃不出米耶纳，我心想，至少我也能用另一种更为彻底的方式逃离它。"
show luce sigh3 n with dissolve
Luce "那样，我就永远不必再回到那所可怕的学校了。"
Luce "也永远不必再见到我姐姐了……"
show luce neutral3 n with dissolve
Luce "也许，等到我的尸体从湖里被打捞上来、早已腐烂不堪时，姐姐会听说这件事，然后明白这全是她的错，或许还会觉得愧疚。"
show luce frown3 n with dissolve
Luce "我想，那样一来，这个计划便算值得了。"
Luce "哪怕只有一次，我也想像她伤害我那样，去伤害她……"

stop music fadeout 1.0

Marcel huh u "露丝……"

window hide dissolve
$ achievement.grant("reassurance")
play music "bgm/Confession.ogg" fadein 1.0
scene cg12 with wiperight_slow
$ renpy.pause(1.0)
window show dissolve

"我握住露丝的双肩，指尖深陷进她校服的布料里。"
"露丝的身子轻得令人不安，骨瘦如柴。有那么片刻，我生怕自己若抱得太紧，会把她弄折了——可我想，露丝心底某处必定早已碎裂了。"
"若非如此，她又怎会想着要跳进湖里去呢。"
"她怎么会生出如此凄绝的念头？我实在无法理解！"
Marcel "我不想假装自己懂得你的感受，露丝，因为我确实不懂。你是你，我是我，我无法知晓你心里在想些什么……"
Marcel "但我真的、真的很庆幸你没有跳进那座湖。"
Marcel "如、如果你死了，我会……"
"我的声音哽在喉咙里。我得强忍住泪水，眼皮不住地颤动。"
Marcel "我、我会不知道该怎么办。"
Marcel "这话听起来也许自私，但……我、我会难过得不行的……"
Luce "起初你也许会难过，但我相信过些时候你总会恢复过来的。"
Luce "你不像我这样冷淡、笨拙、难以相处，所以我肯定你能交到许多朋友。"
Luce "我不明白你为何如此看重我们之间的关系。"
Marcel "因为我在乎你呀！"
Marcel "你是我有生以来交到的第一个朋友！你对我来说无比珍贵！"
Marcel "所以我才会替你辩护，所以我才会向布吕吉埃夫人吐露心事，所以读完你的信后我才会四处去找你！"
Marcel "我会不惜一切代价，把你姐姐从你身边赶走——若那样行不通，我再试着想别的办法！"
Marcel "我会竭尽所能让你快乐，所以求求你，露丝！"
"我凝视着露丝的双眼，声音因绝望而颤抖。"
Marcel "别走！别消失！我想留在你身边！"
Luce "玛塞尔……"
"露丝回望着我，她的眼睛在黑暗里睁得老大；瞳孔迷失在一片乳白之中。"
Luce "你为什么要说这些？"
Marcel "我自己也说不清楚，但我……唔。"
"我咽了口唾沫。"
Marcel "这几天我做了些思索，总算得出了一个结论，姑且算是吧……"
Luce "那究竟是什么样的一种结论呢……？"
"露丝的声音异样地轻柔。她打量着我，仿佛一只兔子，羞怯又警觉。"
"我不想把这件事逼得太紧。我怕操之过急，反倒会把露丝吓跑。"
"我或许有些做得过火了，可我想让她知道我有多么在乎她。"
"我不能让露丝怀有寻死的念头，也不愿她以为，倘若她消失，会没有人想念她。"
"事实远非如此。若她死去，我会痛不欲生。我想让她明白这一点——不，我{i}必须{/i}让她明白。"
"我对自己心绪仍不甚确定，也害怕被拒绝，可我更怕失去露丝。"
"正因如此，我必须告诉她我的感受，而且要趁现在、趁我仍有机会的时候。"
"趁我仍怀有勇气的时候。"
Marcel "我在乎你，露丝。我那么、那么在乎你。其实，我……我……"
"我咽了口唾沫，双眼紧闭，随即朝着夜空呼喊……"
Marcel "我想，我或许是爱上你了！"

stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}露丝篇{/u}{vspace=1}  11月9日{vspace=1}  安然无恙") )
play ambience "sfx/night_amb2.ogg" fadein 1.0
play music "bgm/Night.ogg" fadein 1.0
scene marcel_room_n:
    size (1920, 1080) crop (450, 0, 1440, 810)
show luce neutral2 n:
    xpos 0.50 xanchor 0.5 ypos 0.50 yanchor 0.5
with wiperight_slow
window show dissolve

"露丝坐在我的床沿，一条腿交叠在另一条上。"
"我坐在她身旁，十指在膝上交握，目光凝在木地板上。"
"露丝的旅行包——不，应当说是她姐姐的那只——搁在我卧室的角落里；一团幽暗的影子，望去几乎有些不祥。"
"回到学校后，再要归还杜布瓦夫人的包和她的钱，已经实在太迟了，尽管我本有此意。"
"我本打算趁杜布瓦夫人还来得及发觉东西不见之前，悄然把这些物件归还，可如今恐怕是不可能了。"
"已经太迟了。"
"回程的路上，我一路安慰着露丝，告诉她明天一早我会替她把这些物件归还，可——这一次——露丝的心事似乎并不全系于她的姐姐身上。"
"她好奇地望着我，褐色的眼眸镶着一圈浅色的睫毛。"
show luce huh2 n with dissolve
Luce "我照你所说，陪你走回了学校，所以……"
"她眨了眨眼。"
show luce frown2 n with dissolve
Luce "你能否解释一下自己，玛塞尔？"
Marcel neutral u "我可以试试，但恐怕得花些时间。"
show luce neutral2 n with dissolve
Luce "我不介意。你想用多久时间都可以。"
show luce sigh2 n with dissolve
Luce "和你在一起时，我常常巴望着时间能整个儿静止才好。它流逝得未免太被高看了。"
Marcel shock u "你、你真是这么想的吗？"
show luce neutral2 n with dissolve
Luce "唔，我喜欢和你在一起，胜过和任何人在一起，尽管你{i}确实{/i}常常让我困惑。"
Luce "我以前从没遇见过像你这样的女孩……"
show luce sigh2 n with dissolve
Luce "不过我倒也并没认识多少个女孩。"
Marcel neutral u "你认识在这所学校念书的女孩们呀。"
show luce neutral2 n with dissolve
Luce "我大概只是{i}听说过{/i}她们，也许吧，却并不真正认识她们，算不上认识。她们不是取笑我，就是无视我，而我也同样无视她们。"
show luce sad2 n with dissolve
Luce "我向来不怎么在意交朋友。"
Marcel huh u "可你和我却是朋友……？"
show luce neutral2 n with dissolve
Luce "只因为你在这件事上太过执着了。"
Marcel sigh u "那么，请原谅我成了你的累赘。"
show luce huh2 n with dissolve
Luce "你不是累赘。"
show luce sad2 n with dissolve
Luce "我心底有一部分很高兴你今晚追了出来，尽管你若没这么做，事情会更省事些。"
Marcel shock u "不找你是绝不可能的！我{i}非得{/i}找到你不可。我都不敢想若没找到你该怎么办！"
show luce neutral2 n with dissolve
Luce "我知道。你已说过了。"
Luce "我猜你追出来，是因为我们是朋友，对吗……？"
Marcel shy u "是、是的。"
"我的声音哽在喉咙里。我向来不擅言辞，可当独处露丝身旁时，我那本就贫乏的社交能力似乎愈发捉襟见肘了。"
"我的心跳得如此剧烈，我生怕露丝会听见。"
"那可就太丢人了——可我在湖畔的那场告白，或许更甚。"
Marcel "我们{i}就是{/i}朋友，而我……真的很庆幸能遇见你。"
show luce huh2 n with dissolve
Luce "我也很高兴遇见你，但是……"
show luce neutral2 n with dissolve
Luce "当你说你爱我的时候……"
"我的身体绷紧了。我能感到自己的脸涨得通红。"
show luce huh2 n with dissolve
Luce "你那是出自朋友之情、以一个女孩对另一个女孩说的，还是……{w}其中另有深意？"
Marcel sad u "我……"
"我打了个寒颤。"
"露丝看去宛如天使，浅淡的头发在床边煤气灯的光晕里闪亮，让我难以与她保持对视。局促之下，我只好移开目光。"
Marcel sigh u "我……{w}自己也不太确定。"
show luce sigh2 n with dissolve
Luce "哦。"
"露丝叹了口气。她失望了吗？"
show luce neutral2 n with dissolve
Luce "那么，你对我的爱只是朋友之情，就是如此吗？"
Marcel shy u "我确实爱你，是作为朋友，但也可能不止于此。"
show luce huh2 n with dissolve
Luce "不止于此？"
show luce shy2 n with dissolve
Luce "你这话，嗯……是说你希望把我拥入怀中，或是亲吻我吗……？"
Marcel embarrassed u "呃、呃那个……我……我……"
"我的声音渐渐低了下去，被自己的窘迫紧紧扼住。"
"我从未吻过女孩。在从前那所学校里，我从不曾有过这样的机会——可即便那机会{i}当真{/i}出现过，我也怀疑不会有哪个女孩愿意回应。"
"就男孩而言，我并不算俊朗。"
"可若是作为女孩呢……"
show luce sighblush2 n with dissolve
Luce "我……我很抱歉问出这么令人难为情的问题……"
"至少脸红的不止我一个。露丝也现出了不寻常的局促。"
show luce neutral2 n with dissolve
Luce "你要知道，除了父母，以往从没有人对我说过爱我。"
show luce shy2 n with dissolve
Luce "我不太确定自己该如何回应。"
Luce "我不知道你对我这份『爱』，是否和童话里王子对公主的相同，还是女孩子之间彼此『相爱』本也寻常。"
show luce sigh2 n with dissolve
Luce "我不习惯去爱，也不习惯被爱，所以我说不准……"
Marcel shy u "我也是。这一切对我而言同样陌生。"
show luce neutral2 n with dissolve
Luce "但你认为自己爱我？"
Marcel u neutral "我想是的。"
show luce huh2 n with dissolve
Luce "胜过朋友之情？"
Marcel shy u "很有可能……"
"在米安的这段日子，我对女孩子间的友谊略知一二，可我从未见过班上的女孩们牵着手，或在走廊里偷偷亲吻，或彼此相拥。"
"我从未见过我的同学们做出那些我曾想象着要与露丝一道做的事。"
show luce neutral2 n with dissolve
Luce "我感激你的心意，可我……不太确定自己是什么感觉。这一切真让人困惑。"
show luce sad2 n with dissolve
Luce "你为什么爱我，玛塞尔？我不明白。"
Marcel huh u "你不明白什么……？"
show luce sigh2 n with dissolve
Luce "我觉得自己并不可爱。"
show luce sad2 n with dissolve
Luce "我姐姐显然也不这么认为。"
Luce "她只爱折磨我。可她并不爱{i}我{/i}。我从没想过，竟会有人爱上我。"

stop music fadeout 1.0

Marcel shy u "露丝……"

play music "bgm/Luce.ogg" fadein 1.0
scene marcel_room_n blur:
    size (1920, 1080) crop (600, 60, 1152, 648)
show luce neutral3 n:
    xpos 0.50 xanchor 0.5
with dissolve

"我朝她挨近了一些，握起她的双手，把我们的手指交缠在一起。"
"有那么一阵子，我担心自己太过冒进。我心里隐隐怕露丝会抽回手，可令我宽慰的是，她并没有。"
"恰恰相反，她反而挨得更近，双唇紧抿。那神情几乎就像在邀我吻她——不过或许只是我一厢情愿的臆想罢了。"
Marcel neutral u "你也许看轻了自己——这大概还得谢谢你姐姐——但这并不会改变我对你的看法。"
Marcel "我认为你是个坚强的人，这些年来承受了许多磨难。我不知道还有多少人能像你这样忍耐过来。"
Marcel smile u "我知道自己就做不到。"
Marcel "你真的很了不起，露丝。"
show luce huh3 n with dissolve
Luce "所以，你爱我是因为怜悯我？"
Marcel shock u "不、不是这样的！我不是怜悯你——或者说，唔……"
Marcel huh u "我想我心底确实有一部分是怜悯，但那只是因为你让我看到了太多自己的影子！"
Marcel neutral u "你就如同过去的我……可你比我过去任何时候都坚强，因为你没有逃跑。"
Marcel "你动过逃跑的念头，却终究没有逃。你随我回来了，如今我比以往任何时候都更爱你！"
show luce neutral3 n with dissolve
Luce "您这话是什么意思？"
"露丝打量着我。在煤气灯的光线下，她苍白的眼睛显得比任何时候都更硕大，仿佛要将我吞没。"
show luce frown3 n with dissolve
Luce "我怎么会像你……？"
Marcel neutral u "事情是这样的……"
"我握住露丝的手指，攥得更紧了。"
"我知道，纵使心跳如擂、喉咙干得难受，自己也必须告诉她。"
"若我不肯向她吐露我的过往——我真实的过往，而非布吕吉埃夫人为我编造的那缕虚影——露丝便永远不会明白，她对我究竟有多么重要。"
"我得让她知晓真相。"
Marcel shy u "我并非你以为的那个人。"
show luce huh3 n with dissolve
Luce "你这话是什么意思……？"
Marcel "首先，我……"
"我的声音渐渐消散，湮没在黑暗之中。"
"我能感到那颗被囚在肋骨之间心脏，正剧烈地撞击着……"
"我此生似乎从未这样惶然过：就连从前在旧校里被同学推下楼梯，我在稀薄的空气中飘飞、眩晕，直到重力攫住我开始下坠都不曾如此……"
"我仿佛又在坠落，可这一次，我看不见地板。我不知道自己会在何时、何处落地。"
"正因如此，这场告白才如此令人恐惧。"
"我无从推知这会有多痛，因为我并不清楚露丝会作何反应。她或许会震惊、恐惧，甚至对我的秘密心生厌恶——但我已走得这么远，此刻无法回头了。"
"露丝尽管惧怕她的姐姐，却依然有勇气回到这所学校。"
"我该试着跟随她的榜样。我会把一切都告诉她，然后看她是否还愿意做我的朋友。"
"我深深吸了口气，竭力稳住心神……{w} 然后，我便开口了。"

scene sky_n with wipeup_slow

"我告诉露丝，我不叫玛塞尔·雷诺，而是马塞尔·德·圣雷米。"
"我向她讲起我的父亲，他曾是巴黎一位著名的演员；也讲起我的母亲，她在我们奢华公寓里百无聊赖地度日，满心悔恨与怨怼，却仍深爱着我。"
"我告诉她我在旧校的种种经历，我如何始终难以融入；我仅仅因为存在，便时常遭受欺凌。"
"我告诉她那些刻薄的评语；朝我头顶弹来的墨团；那些绰号；那些殴打；被推搡、绊倒、踢踹；还有我滚落楼梯的那一跤。"
"我告诉她阿尔贝汀姨妈，以及她的计划——让我在一个人人都不认识我的小村庄里重新开始生活。"
"我告诉她前往米安的旅途，以及我多么担心自己会被识破，又是多么害怕自己无论作为女孩还是男孩都无法融入。"
"我告诉她，即便是现在，我也仍不完全确定自己究竟是什么，或想成为怎样的人。"
Marcel neutral u "我自己也曾受尽欺凌，全因我父亲。他的名字常出现在报纸上，总惹出各式各样的丑事。"
Marcel "我的同学们常把这些写我父亲事迹的文章用滑稽的腔调念给我听，好让我难堪退缩。"
Marcel "我想他们之所以恨我，也许是嫌我父亲太有钱……"
Marcel "但也可能是我弄错了。也许他们之所以恨我，是因为我从来都融不进人群。即便我出生在一个普通人家，也许依然融不进去。"
Marcel "可我毕竟不属于普通人家，而这让我成了一个容易下手的靶子。"
Marcel "我每天都被嘲笑和欺辱。有时候同学们只是骂我几句，可另一些时候，他们会朝我扔东西，推我，甚至做出更过分的事。"
Marcel sad u "母亲曾去投诉，可校长将她的忧虑置之一旁。他说我该学着硬气起来。"
Marcel "老师们也都作如是想。在有人欺凌我时，他们视而不见。"
Marcel "我从没试过为自己挺身而出。我知道那样只会让事情更糟——何况在体格上我本就比欺负我的人弱小，我从来都不可能打得过他们。"
Marcel sigh u "我只好认命，任由自己受人欺凌。我也没有多少选择。"
Marcel neutral u "所以当我见到你时，才会那么同情你，也才会想要帮你。"
Marcel sad u "很抱歉我向你隐瞒了自己的身份，露丝，但是……"

scene marcel_room_n blur:
    size (1920, 1080) crop (600, 60, 1152, 648)
show luce neutral3 n:
    xpos 0.50 xanchor 0.5
with wipedown_slow

"我凝视着露丝的双眼，下唇因难以抑制的情感而微微颤抖。"
Marcel neutral u "我真的在乎你，我不愿误导你。"
Marcel sad u "问题在于……我自己也不清楚自己究竟是什么人。"
Marcel "作为男孩，我从没能融入；可要当作女孩活着，我也觉得不自在。"
Marcel sigh u "也许无论我身在何处、是何身份，都永远没法真正融入……"
Marcel neutral u "但我确实知道，待在你身边令我感到安心，我也真的很珍视你的友谊。"
Marcel "至于你是否还愿意做我的朋友，那是另一回事了；但我很高兴我们得以共度这一段时光。"
Marcel u shy "谢谢你听我说这些。我所能祈求的，便仅止于此了。"
Marcel "你……{w}对我太好心了，或许好得过了头。我很感激。"
show luce huh3 n with dissolve
Luce "哦……"
"露丝凝视了我片刻，仿佛被惊得说不出话来。"
"我不能说怪她。这种事对任何人来说都太难以承受了。"
"我满心以为，露丝回过神来便会将她的手指从我手中抽开。我料想会有一场对峙——真正的愤怒——或者，至少是震惊、困惑与不信任。"
"厌恶。"
"我几乎觉得自己活该如此，毕竟我对露丝隐瞒了太多，瞒了这么久……"
"可是，尽管我心中忐忑，露丝却没有从我身边抽身退开。"
"她朝我眨了眨眼，仿佛第一次见到我一般，怔怔地凝视着。"
show luce neutral3 n with dissolve
Luce "马塞尔……德·圣雷米？"
"她终于开口说话，声音轻柔，带着一丝探寻。"
Marcel neutral u "是这样。"
show luce frown3 n with dissolve
Luce "那么你与乔治·德·圣雷米有亲缘关系？"
Marcel "是的，正是。"
"我点了点头。"
Marcel "那么，我想你是听说过他了？"
show luce sigh3 n with dissolve
Luce "略有耳闻。我知道他是个名演员。不过我从未见过他，连照片也没见过。我不知道他生得什么模样。"
show luce neutral3 n with dissolve
Luce "这名字在我心里没多大分量……"
Luce "但你是说，你是他的……{w}儿子？不是女儿？"
Marcel sigh u "就我所知，乔治没有女儿。我是个男孩。"
show luce huh3 n with dissolve
Luce "我不信……"
show luce neutral3 n with dissolve
Luce "我确实觉得你有些特别，可没想到你竟然是个男孩……！"
Luce "你倒不太像男孩——不过我这辈子也没见过多少男孩就是了。"
Marcel u neutral "我也不知道自己像不像个女孩。"
show luce huh3 n with dissolve
Luce "啊——不是的！我觉得你挺有女性气质的！"
Marcel shy u "可我比所有人都高出一大截……"
show luce neutral3 n with dissolve
Luce "诺艾米也很高，可她分明就是个女孩！"
Marcel neutral u "唔，话是这么说。"
show luce frown3 n with dissolve
Luce "我还是有点不敢相信……"
"露丝审视着我，眯起眼睛，或许是想从我的眉眼轮廓或鼻梁之间，窥出任何潜伏的男子气概。"
Luce "我可以……吗？"
"她把她的手指从我手中抽出，不等我回应，便按在我脸颊的两侧。"
"她的掌心还带着从外面带来的一丝凉意，我不由得打了个寒颤。"
"我能感觉到自己的脸颊正泛起淡淡的粉晕。"
show luce neutral3 n with dissolve
Luce "真稀奇。我没想到男孩的皮肤会这么柔软……"
Marcel sad u "我又不是石头做的，你知道吧。"
show luce huh3 n with dissolve
Luce "啊——我知道。对不起……！只是……"
show luce frown3 n with dissolve
Luce "男孩，嗯？"
Luce "可你的睫毛这么长，嘴唇看起来又软又丰满！"
Luce "就一个男孩来说，你长得挺漂亮的……"
Marcel shy u "嗯……"
"我不自在地挪动了一下身子。"
"与露丝靠得这么近，让我的心跳得更快了。我的脸颊越涨越红。"
"我为她没有立刻厌恶地抽身离开而感到欣慰，可我也不太喜欢被人像市集上的马匹那样东戳西戳的。那感觉实在有点不把人当人看。"
Marcel u huh "你检查完了吗……？"
show luce huh3 n with dissolve
Luce "啊——对不起！"
"露丝满脸窘迫地慌忙从我身边退开。"
show luce shy3 n with dissolve
Luce "我不是有意冒犯的。这一切实在太突然、太古怪了，我一时难以接受，但……"
"露丝看向自己的膝盖，手指蜷曲在大腿之上。"
show luce neutral3 n with dissolve
Luce "既然你说你是男孩，我也没有理由不信你。撒这种谎对你没有任何好处——至少据我所知是没有的。"
show luce huh3 n with dissolve
Luce "不过，这{i}确实{/i}很奇怪。我不知道该作何感想。哎呀，这简直就像莎士比亚戏剧里的一幕！"
Marcel neutral u "也许是{i}《第十二夜》{/i}吧？"
Luce "对，我想的就是它——不过那是写一个女孩扮成男孩。到了你这儿，正好反了过来。"
Luce "真稀奇。"
Marcel huh u "那么，呃……"
"我垂下眼帘，羞涩地看向露丝。"
Marcel "你难道不生气吗？竟和一个男孩单独相处了这么久。"
show luce huh3 n with dissolve
Luce "什么？不会啊？"
show luce frown3 n with dissolve
"露丝皱起了眉头。"
Luce "我为什么要为这种蠢事生气？"
Marcel shy u "这可是所女子学校。我算是个异类……"
Marcel "我原想，你若知道了真相，就不愿再和我独处了。我怕会让你觉得不自在，甚至惹你生气……"
Marcel sad u "我怕你会觉得我一直都在骗你。"
show luce neutral3 n with dissolve
Luce "唔，也许你没有完全说实话，可我也绝不会因此恨你。"
show luce smile3 n with dissolve
Luce "你也是我的第一个朋友。我不想因为这种事就和你反目。"
Luce "你是女孩还是男孩，或者既是两者，又或者两者皆非，我都不在乎。在没人肯为我出头的时候，你站出来护着我不受我姐姐欺负；我离家出走后，又是你去找我。"
Luce "你比这个凄惨地方里的任何人都待我要好。"
Luce "我又怎么会因此恨你呢？"
show luce huh3 n with dissolve
Luce "我也不认为你对我说的每一句都是假话。"
show luce neutral3 n with dissolve
Luce "你说我是你的第一个朋友，那是真心话，对吧？"
Marcel shy u "是——是的……这种事我不会撒谎的。"
show luce shy3 n with dissolve
Luce "那么……"
"露丝猛地吸了口气。她的脸颊染上了一层淡淡的粉色。"
Luce "还有你说爱我的时候……"
Luce "我不觉得那是谎话——还是说，那是假的？"
Marcel neutral u "……不，不是假的。至少我觉得不是。"
Marcel "我对自己的心意也说不准，可我知道我{i}确实{/i}在乎你。我不愿你受伤。"
Marcel huh u "我只想让你开心。这就是我唯一的愿望。"
show luce smile3 n with dissolve
Luce "马塞尔……"
"露丝的眼神柔和了下来。"
"她再次将我的手指握进她手中，又凑近了些。"
"她的嘴唇与我的近得令人心惊。"
"我能感觉到她的呼吸拂在我的脸颊上，那气息轻柔而清甜，让我的皮肤微微发麻。"
"我的心在胸腔里擂鼓般急促地跳个不停。"
"我深深沉溺在露丝的双眼、她的触碰、她的气息之中，简直难以安稳地坐着。"
Luce "你{i}确实{/i}让我开心。"
Marcel shockblush u "我——我真的吗？"
Luce "没错。你比任何人都更让我开心……"
show luce happy3 n with dissolve
Luce "如果这就是爱的话，那我想，我也一定是爱你的。"
Luce "我爱你，胜过爱这世上其他任何人……而且我想，无论你是谁、是什么，这份心意都不会改变。"
Luce "你永远都会是我的骑士。"

stop ambience fadeout 1.0
window hide dissolve
scene cg13 with dissolve
$ renpy.pause(1.0)
window show dissolve

"说着，露丝用自己的唇，在我唇上落下一个轻轻的吻；那是我有生以来的第一个吻。"
"年少时，我有时会想象亲吻一个女孩会是怎样的滋味。这些念头不过是白日梦罢了，一个个像肥皂泡般转瞬即逝，因为我确信，不会有哪个女孩会爱上我。"
"然而，我从不曾想象过，我的初吻会发生在女子学校里一间光线昏暗的卧室中。"
"我的想象力从来不敢延伸得那样远。"
"这个吻与我曾设想过的完全不同，可是……"
Luce "嗯……马塞尔……"
Marcel "哈……嗯……"
"……无论如何，我都不愿拿它去交换全世界。"
"我想我这辈子从未这般快乐过，也从未这样被接纳过。"
"当我亲吻露丝、她的唇柔软地贴在我的唇上时，我不禁暗自思忖。"
"这就是幸福的感觉吗？"

stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene sky g with clockwipe
$ renpy.pause(0.5)
show overlay2
show message11 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message11
hide logo2
hide overlay2
with datetrans2

$ renpy.pause(0.3)

$ save_name = (__("{u}露丝篇{/u}{vspace=1}  11月15日{vspace=1}  幸福结局") )
play music "bgm/Casual_Day.ogg" fadein 1.0
scene sky with dissolve
window show dissolve

"布吕吉埃夫人果然是言出必行。周末，她把杜布瓦夫人和露丝召到办公室谈了一次话；这件事到了周日我才知晓——露丝约我到湖边见面。"
"我们两人坐在清澈如镜的水边，临近的冬日让湖水显得比往日更添凉意，露丝终于开口谈起了整件事。"

scene lake:
    size (1920, 1080) crop (240, 140, 1440, 810)
show luce neutral2:
    xpos 0.5 xanchor 0.5 ypos 0.5 yanchor 0.5
with wipedown_slow

Luce "我们几个一起聊了聊。嗯……"
show luce huh2 with dissolve
Luce "话虽这么说，布吕吉埃夫人却没怎么开口。我主要是和我姐姐说的。我们聊了……"
Marcel neutral c "想什么？"
show luce neutral2 with dissolve
Luce "哦，天南地北什么都聊。挺有意思的。"
Luce "我们打小就是姐妹，可这么多年，这还是头一回感觉像是在真正地交谈。"
show luce sigh2 with dissolve
Luce "我们也许是姐妹，可这么多年却一直像陌生人一样相处。"
show luce sad2 with dissolve
Luce "和她说话，我才发觉自己对她了解得实在太少了。"
Marcel huh c "那你们都聊了些什么？"
show luce neutral2 with dissolve
Luce "真的是什么都聊，多得说不完。不过一开始还挺尴尬的。我们俩谁都不愿多说，只好由布吕吉埃夫人主持局面。"
show luce sad2 with dissolve
Luce "我姐姐不愿看我，我也不愿看她……"
show luce huh2 with dissolve
Luce "可布吕吉埃夫人不让我们走，非要我们开诚布公地谈一次。"
Luce "到最后，我们{i}只好{/i}开口谈。除此之外，我们别无他法。"
"露丝低下头去，双臂环抱着双腿。"
"这周断断续续地下了好几场雨，尽管今天天气晴好，河岸却仍潮湿泥泞。"
"为免弄脏了衣裳，露丝和我坐在一条陈旧的野餐毯上。那正是上次我们到湖边野餐时我带去的同一条毯子；上面是鲜亮的格纹图案，衬得露丝的脸比以往更加苍白。"
"我关切地望向她，问道……"
Marcel sad c "你是不是没怎么睡？"
show luce sigh2 with dissolve
"露丝摇了摇头。几缕短促的碎发在她脸颊旁飘动，她抬手将它们拢到耳后。"
Luce "我和姐姐的谈话在离开布吕吉埃夫人办公室后，还持续了很久。"
show luce neutral2 with dissolve
Luce "回宿舍的路上我们一直在聊，之后又在她房里聊了大半夜。"
Luce "我以前从不爱和她说话——说实话，对别人也一样——可她向我敞开心扉的时候……我不知道该怎么说。"
Luce "我想，如今我或许能以新的眼光来看她了。"
Marcel smile c "那么，我猜事情进展得还不错？"
show luce huh2 with dissolve
Luce "嗯……？"
"露丝把头歪向一侧。"
show luce neutral2 with dissolve
Luce "我想是吧。我不像从前那么厌恶我姐姐了，这大概也算是一种进展……"
show luce sigh2 with dissolve
Luce "可我们以往的关系压根就不存在。要说有所改善，也不值得夸耀什么。"
Marcel "可我觉得你还是该为此自豪。和她谈这些，想必很难吧。"
show luce neutral2 with dissolve
Luce "一开始的确很难。我想做什么都是如此——我是说，去做那些你不习惯的事。"
Luce "比起和人说话，我一向更喜欢读书。"
show luce huh2 with dissolve
Luce "书是……可靠的。它们不会做出或说出伤人的事——就算有，也只是因为你允许它们这样。它们没有自己的意志。"
Luce "书是人写的，却与人隔绝。它们只是一叠纸。无论你读多少遍，那些字词都不会变，哪怕你每次都能读出不同的意味来。"
show luce sigh2 with dissolve
Luce "人就要复杂得多了……"
"露丝叹了口气。"
show luce neutral2 with dissolve
Luce "尤其是我姐姐，她更是复杂。我以前不知道她竟过得这么苦。"
show luce huh2 with dissolve
Luce "……不，这么说也不对。我隐约是知道的，只是不愿去细想罢了。"
show luce sad2 with dissolve
Luce "她待我那么刻薄，所以我从没想过要体谅她。把她想成恶魔，我反而更自在。"
Luce "也许她也这么看我吧。"
Marcel huh c "那她的过往呢……？"
"我稍稍挺直了身子。"
"我无意过多打探，但我实在好奇——而且，为自己辩白一句，这事可{i}是{/i}露丝自己先提起的。若非她先开口，我根本不会知道她与姐姐有过那场长谈。"
Marcel c neutral "她那样狠心地待你，有什么缘由吗？"
show luce neutral2 with dissolve
Luce "我想，在她看来……那是够充分的理由，虽说我也不认为它完全合乎道理。"
Luce "话说回来，人本来就不是讲道理的东西。"
show luce sigh2 with dissolve
Luce "你听我说……"

stop music fadeout 1.0

"露丝拨弄着河岸边生的细草。她把草茎缠绕在苍白的指间，脆利的指甲尖锐的边缘在淡淡的阳光下如同猫爪般闪烁。"

play music "bgm/Sad.ogg" fadein 1.0

show luce neutral2 with dissolve
Luce "我姐姐以前结过一次婚，那时她才十五岁。她丈夫二十五岁。一切发生得非常快。"
Marcel sad c "你是提过一次她结过婚的，没错。"
"这就是为什么杜布瓦夫人与她妹妹露丝姓氏不同——也因为如此，尽管杜布瓦夫人还算年轻，却已是「夫人」而非「小姐」。"
"露丝提起过这个话题，但只是寥寥数语带过。"
"我不知道杜布瓦夫人和她前夫之间竟有这么大的年龄差距。我在想，这是否正是他们婚姻破裂的原因呢？"
"我自己的父亲就比当年年轻、痴迷、热恋中的母亲年长好几岁，看看他们最终的结局吧。"
Luce "我家以前住在离讷韦尔半个钟头路程的一个小村子里。我姐姐在讷韦尔上学，她每天都步行去。"
show luce frown2 with dissolve
Luce "她的丈夫——名叫艾蒂安——就住在城里。他父亲是木匠，有自己的铺子。艾蒂安就在他身边帮工。"
Luce "我姐姐上学路上会经过他的铺子。她那时候长得很漂亮——大家都这么说！——想必是入了艾蒂安的眼，所以他爱上了她。"
show luce neutral2 with dissolve
Luce "偶尔他会叫住她，和她攀谈起来——至少我听说的是这样……"
show luce huh2 with dissolve
Luce "后来有一天，他向她求了婚。"
Marcel shock c "就这么突然？"
"露丝点了点头。"
show luce neutral2 with dissolve
Luce "那是在我姐姐七月要参加考试前不久。"
Luce "艾蒂安想必清楚，那时才十五岁的姐姐很快就将完成学业。到时候，她就没有理由再去讷韦尔了。"
Luce "上学本来就够贵了，我父母为了供我姐姐念更高的学府，已经十分吃力。"
Luce "我姐姐本想去讷韦尔的师范学院就读，将来当一名教师，可那根本不可能。我父母太穷了。"
show luce huh2 with dissolve
Luce "无论如何，艾蒂安求了婚，我姐姐也答应了。"
show luce neutral2 with dissolve
Luce "我父母对这门婚事颇为犹疑，可我姐姐却异常坚决。她告诉他们，艾蒂安是个可靠的男人——还是位生意人！——定能养得起她。"
Luce "单从实际着眼，我想这门亲事看起来倒也诱人。"
Marcel c neutral "所以，他们就成婚了？"
"露丝点了点头。"
show luce huh2 with dissolve
Luce "是的，的确如此。就在我姐姐考完试几个月之后。"
show luce neutral2 with dissolve
Luce "婚礼是在讷韦尔举行的。那是一场小规模、不张扬的仪式，没什么排场。我记得不太清楚了。那时我才五岁。"
Luce "之后，我姐姐就去和艾蒂安一家住在铺子楼上。"
Marcel huh c "那她愿意那么做吗？我是说，她几乎还不认识他……"
show luce frown2 with dissolve
Luce "她一直说自己是愿意的……"
show luce sigh2 with dissolve
Luce "可昨天我和姐姐谈话时，才知道事情并不完全如此。"
show luce neutral2 with dissolve
Luce "她绝不是因为爱他才嫁给他的。他们那段关系以那样的动荡收场，至少就证明了这一点。"
Luce "我想，她嫁给他，是因为觉得自己别无选择。"
show luce sad2 with dissolve
"露丝继续拨弄着河岸上的草。她整洁的指甲缝里已沾上了泥土，掌心也被染成了绿色。"
show luce neutral2 with dissolve
Luce "她想读书，好当一名教师。可我父母太穷，供不起；除非他们不打算让我也像姐姐那样受教育。"
Luce "你瞧，他们认为，若不能给我同样的机会，却让姐姐去上学，那是不公平的。"
show luce huh2 with dissolve
Luce "若没有我出生，也许我父母还能勉强凑出些钱，去成全姐姐的志向……"
show luce sigh2 with dissolve
Luce "可要同时照顾我们两个，就无论如何也办不到了。"
Luce "嫁给一个有钱人，是我姐姐实现自己梦想的唯一出路。"
Marcel frown c "我明白了……"
"我的眉头皱了起来。"
"我想我现在能明白，为什么杜布瓦夫人似乎那么憎恨自己的妹妹了。她是不是在为自己不幸的婚姻怪罪露丝……？"
show luce neutral2 with dissolve
Luce "正如你所想的那样。"
"露丝注意到我脸上阴郁的神情，点了点头。"
show luce huh2 with dissolve
Luce "我姐姐并不喜欢和艾蒂安生活在一起。他把她当作女学生时，对她温柔体贴；可一旦结了婚，就大不如前了。"
show luce sad2 with dissolve
Luce "他是个暴躁的恶人，总能从我姐姐身上挑出毛病来。"
Luce "无论她做什么，他都要责难，从做饭到刺绣。"
Luce "我姐姐偶尔想要反抗——这很少见，因为她一向不喜与人起冲突——他便说，训斥妻子是丈夫的权利，好让她有所长进。"
show luce sigh2 with dissolve
Luce "听起来，他简直把她当成一个顽劣的小女孩；根本不像待妻子。"
show luce neutral2 with dissolve
Luce "他从不让姐姐忘记，正是他出钱供她受训成为教师的。他刻意张扬自己为她花费了多少金钱，好借机愈发肆意地嘲笑与羞辱她的过错。"
Luce "他凌辱她的兴致，似乎丝毫不亚于当初初遇时调戏她的那份劲头。他不断地苛责她，直到她彻底失去了对自身的全部信心。"
Luce "她险些精神崩溃。"
show luce sigh2 with dissolve
Luce "想到这一切，她能通过考试简直是奇迹……"
"露丝朝着寒冷的冬日空气里呼出一口温热的气息。"
show luce neutral2 with dissolve
Luce "我早知道她并不怎么喜欢自己的丈夫，却不曾料想他待她如此刻薄。"
show luce sigh2 with dissolve
Luce "她忍受了太多……"
show luce neutral2 with dissolve
Luce "而在这段岁月里，她常常会想：『唉……要是露丝没出世就好了。那样的话，我就从不必向男人求助，也从不会接受艾蒂安的求婚，这一切便都不会发生。』"
Marcel shock c "什么？这太不公平了……！"
"听露丝讲述时，我一直对杜布瓦夫人颇为同情，可这句话却让我心头一阵刺痛。"
Marcel c frown "来到这世上不是谁的错，这根本不是人能够左右的呀！"
show luce huh2 with dissolve
Luce "这我知道……而且我想，姐姐理智上也明白这一点。她明知迁怒于我是错的，却终究无法克制自己。"
Luce "我成了最完美的替罪羊，只因我当时并不在场。"
show luce sigh2 with dissolve
Luce "我无法替自己辩解，于是姐姐尽可以随心所欲地揣度于我。"
Marcel frown c "这点我能够理解，可她的丈夫呢？真正的祸首分明是{i}他{/i}呀！"
show luce neutral2 with dissolve
Luce "她当然也知道……{w}可她太怕他了，不敢作声。"
show luce sad2 with dissolve
Luce "姐姐向来是个沉默寡言的人。一遇到对抗，她便退缩回避，不会为自己据理力争。"
Luce "她一向如此……但我以为，嫁给艾蒂安这样的男人，使情况愈发糟了。"
Luce "她与他共同生活了八年，从十五岁直到二十三岁。她日日受辱，直到曾经可能拥有的一切自信都被剥夺殆尽。"
show luce sigh2 with dissolve
Luce "我自己实在无法想象……"
"露丝叹了口气，又摇了摇头。"
show luce neutral2 with dissolve
Luce "嗯，至少如今她总算摆脱了那个恶棍。"
Marcel c huh "发生了什么事？难道他……？"
"我没有把问题问完，也不需要问完。露丝轻易便猜中了我想说的话，并对我的猜想报以微笑。"
Luce "死？没有，无论他喝了多少酒都死不了。他是个体格健壮的人。一点酒——甚至很多酒——也要不了他的命。"
Luce "姐姐离婚了。"
Marcel neutral c "离婚……？那不是挺稀罕的事吗？"
"在法国，离婚合法化其实为时并不算久。我自己对离婚的程序所知甚少，但我记得母亲有位朋友曾苦苦争取与她那个软弱无能、不负责任的丈夫离婚。"
"从我听来她抱怨的内容看，那似乎是个艰难的过程。"
Marcel huh c "你姐姐是如何得到准许的？"
show luce huh2 with dissolve
Luce "这比她想象中的容易得多。她查出他有了外遇，而他竟迫不及待地证实了她的说法。"
show luce sigh2 with dissolve
Luce "我想艾蒂安本人也厌倦了姐姐。在被这般摧折之后，她失了几分姿色，也不再回应他的挑拨了。"
show luce neutral2 with dissolve
Luce "他早已准备好另寻新欢，而姐姐从新婚那天起就想离开他了。"
Luce "两人都赞成离婚，所以法庭也没多费周折便予以准许。"
Marcel neutral c "那之后呢……？"
show luce huh2 with dissolve
Luce "姐姐四处寻觅工作。她曾在讷韦尔断断续续当了几年的教师——毕竟她有这个资格——只是与艾蒂安这样的男人同住的压力，使她无法全心全意投入其中。"
Luce "离婚一经敲定、姐姐重获自由后，她便决心到更远的地方去。我想她是想逃离讷韦尔，连同那座城市所牵连的种种苦涩回忆。"
show luce neutral2 with dissolve
Luce "她向涅夫勒全省的学校递出了申请……"
Marcel c huh "那么到头来，是布吕吉埃夫人给了她一份职位？"
show luce sigh2 with dissolve
Luce "是这样。"
"露丝点了点头。"
show luce neutral2 with dissolve
Luce "我想布吕吉埃夫人或许是同情她吧。我不清楚她对姐姐的过往知道多少，但姐姐受过苦这一点，想必是瞒不过人的。"
Luce "布吕吉埃夫人虽看似冷淡疏离，却是个心地善良的女人，我确信她是有意相帮的。"
Marcel c smile "我姨母确实是个善良的女子。"
"尽管露丝对我讲述的这个故事如此沉重，我却发现自己不禁露出了微笑。"
Marcel "正因为有她，我才能留在这里。"
show luce smile2 with dissolve
Luce "也正因为有她，我姐姐才寻到一处可称作家的地方。"
Luce "她把新职位的消息写信告诉了父母，他们为她高兴。同样令他们欣喜的，是能为当时十二岁的最小的女儿换来一份免费教育。"
Luce "布吕吉埃夫人提出免除我的学费，于是我便被送到了这里。"
show luce neutral2 with dissolve
Luce "从那以后，我便一直住在米耶讷……"
show luce sigh2 with dissolve
Luce "而姐姐也从没有停止过对我的怨恨。"
"露丝叹了口气。"
show luce neutral2 with dissolve
Luce "我知道她并不想我来这里。我会让她想起过去，想起她的那段婚姻。"
Luce "她仍把她那段不幸的婚姻归咎于我，尽管明知这样很荒唐。"
Luce "后来，当她管不住班上的学生时，她连这个也开始怪罪到我头上。"
show luce sigh2 with dissolve
Luce "很久以来，我一直是姐姐的替罪羊。"
show luce sad2 with dissolve
Luce "我想她是在借我树立自己的威信，哪怕这威信摇摇欲坠。这伎俩想必是从她丈夫那儿学来的。"
Luce "当我告诉她，她待我的方式与他待她的如出一辙时，她愣住了。她说她从未那样想过，也从未想过要变成他那样的人……"
Luce "然后，她哭了起来。"
"露丝顿了顿。她的呼吸哽在喉间，眉头也皱了起来。"
show luce huh2 with dissolve
Luce "我从没见过姐姐哭泣。一时间我不知所措，只觉茫然无措……"
Luce "但布吕吉埃夫人劝我坚持下去。她说，我应当把这当作一次修复我们姐妹关系的机会。"
Luce "她让我去安慰姐姐……"
show luce sigh2 with dissolve
Luce "于是我便那样做了。我竭尽了全力。"
show luce sad2 with dissolve
Luce "我拥抱了她，她也回抱了我。她靠在我肩头哭泣，随后向我道了歉。"
Luce "她说她很抱歉，说她这个做姐姐的太糟糕了。我当然赞同她的话。"
Luce "她说她会设法弥补，又问我是否愿意打从心底原谅她。"
show luce neutral2 with dissolve
"露丝在毯子上舒展开身体。她仰头望向天空，脑袋向后仰起，浅褐色的眼眸半阖着。"
Luce "我说我不确定自己能否做到，但我愿意一试。"
Marcel huh c "那后来呢？"
show luce huh2 with dissolve
Luce "布吕吉埃夫人让我们先退下了。她说我们可以自行找时间慢慢谈。我想她是想体贴我们。"
Luce "姐姐和我回到她的房间，我们继续谈着。我们坦诚相待、毫无保留……{w}我想，经过这一切，我们终于能够彼此理解了。"
show luce neutral2 with dissolve
Luce "至少，我希望是如此。"
Marcel smile c "我也希望如此。"

stop music fadeout 1.0

scene lake blur:
    size (1920, 1080) crop (420, 200, 1152, 648)
show luce huh3:
    xpos 0.5 xanchor 0.5
with dissolve

"我握住露丝的手，轻轻捏了捏。"
"露丝偏过头来，微笑着，然后说道……"

play music "bgm/Confession.ogg" fadein 1.0

show luce shy3 with dissolve
Luce "谢谢你听我说这些，马塞尔。但愿没有让你觉得太乏味。"
Marcel ehe c "一点也不。我很乐意倾听……不过其实我也没帮上什么忙。"
Marcel "这一切之所以能够实现，全靠我姨母。"
show luce neutral3 with dissolve
Luce "是啊，确实如此。尽管在课堂上那般严厉，她却是个非常和善的人。"
show luce sad3 with dissolve
Luce "我几乎要羡慕你了，能有这么一位可亲的姨母……"
show luce neutral3 with dissolve
Luce "不过我想自己也算幸运。我还有姐姐。我们从不曾亲近，可我总觉得，修复这段关系或许是可能的。"
Luce "我不喜欢与人交谈。独处对我来说来得更容易些……"
show luce smile3 with dissolve
Luce "但这一次，我倒想尽力一试。毕竟，她也曾对我做出过努力。"
Marcel smile c "你能做到的，露丝。我确信你可以。"
Marcel "起初与她相处，你或许会觉得不自在——上天知道，在她让你受了那么多苦之后，我绝不会怪你——但倘若她真如自己所说那般心存歉意，那么一切应该会顺利的。"
Marcel "无论你何时需要我，我都会在这里，所以别担心。你不是孤身一人。"
Marcel "若事情变得艰难，你随时都可以向我倾诉。"
show luce happy3 with dissolve
Luce "或许我真会那么做。"
"露丝笑了。"
show luce neutral3 with dissolve
Luce "说来奇怪。波莱特一直是我的姐姐，可她却从不像个姐姐。我设法躲着她，她也设法躲着我。"
Luce "就好像，经由与她的交谈，我觅得了一位新的家人……"
show luce smile3 with dissolve
Luce "这还不止于此。"
"露丝朝我倾过身来。微风拂得她淡色的头发轻轻飘动，几缕松散的发丝搔着我的脸颊。"
Luce "我还寻到了一位出色的伴侣。"
show luce happy3 with dissolve
Luce "谢谢你陪着我，马塞尔。"
Luce "无论发生什么，我都希望我们能永远这样相守相依……"

window hide dissolve
scene cg13_2 with dissolve
$ renpy.pause(0.8)
window show dissolve

"说着，露丝低下头，在我唇上落下一个吻。那是一个非常轻柔、温存的吻，满含着对未来的犹疑与希冀。"
"我不知道明天会带来些什么。近来天这般寒冷，就算再下雨我也不意外。这一个星期，天空总是灰暗阴郁、乌云密布，但这还不足以败了我的兴致。"
"我很爱露丝……"
"而且，和她在一起的时候，我想我从未觉得如此幸福过。"

$ achievement.grant("luce")

$ persistent.end = "on"
stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with slow_dissolve
jump luce_credits

label Celine_route:

    stop music fadeout 1.0
    scene black with wiperight_slow
    $ renpy.pause(0.8)
    $ save_name = (__("{u}塞琳篇{/u}{vspace=1}  9月16日{vspace=1}  淑女的约定") )
    play music "bgm/Casual_Day.ogg" fadein 1.0
    scene woodshed:
        size (1920, 1080) crop (240, 40, 1440, 810)
    show celine frown2 w at center
    with wiperight_slow
    window show dissolve

    Celine "天哪！这地方比我上次来的时候还要破败不堪。简直是个健康隐患！"
"塞琳带着鄙夷环顾着这间柴房，这完全可以理解。"

show image "border" onlayer border
scene woodshed:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

"与我从前的巴黎学校相比，阿尔贝汀姨妈的乡下学校或许确实有几分乡土气，可这间柴房却实在破败不堪。"
"就像塞琳说的，这是一场随时会降临的灾祸。"
"我竖起耳朵，几乎能听见这间柴房变形的墙壁在屋顶的重压下呻吟作响。"
"万一整座屋子在我们身边塌下来怎么办？！"
"那可会是我在米延度过的第一个完整日子多么不吉利的结局。"
"这间柴房又小又逼仄，就坐落在离学校本体不远处的一小段步程之遥。"
"它的屋顶倾斜得危险，我总担心自己会撞到结满蛛网的屋檐，而那本就不多的地面空间又被一垛垛木柴占满了。"
"这间狭小的棚屋里只有一扇窗户，上面覆着一层尘埃与无人照管的岁月痕迹。唯有最明亮的光线才能穿透那厚积的积尘。"
"没有光亮替我取暖，屋内感觉格外寒冷，我不禁打了个寒颤。"

hide image "border" onlayer border
scene woodshed:
    size (1920, 1080) crop (240, 40, 1440, 810)
show celine frown2 w at center
with wipeleft_slow

Marcel u frown "说起来，我也并不喜欢这个地方。"
"我长叹一口气。"
Marcel u sigh "我可弄不明白，为什么非得让我大老远跑到这儿来。{i}我{/i}又不是那个顶撞杜布瓦夫人的人。"
Marcel "克洛蒂娜本就该受罚，那是她罪有应得。"
show celine sigh2 w with dissolve
Celine "克洛蒂娜从不为自己做过的错事负责，尽管她本该如此。"
show celine annoyed2 w with dissolve
Celine "你刚来这儿，可能还没意识到——可逃避惩罚正是她的一贯伎俩。就这一点而言，她像条蛇。"
Celine "我劝你跟她相处时小心些。谁也说不准她心里在盘算什么。"
Marcel u ehe "记下了，我会把这话记在心里。"
show celine sigh2 w with dissolve
Celine "不过说真的……"
"塞琳叹了口气。"
show celine frown2 w with dissolve
Celine "既然你明白这一切的罪魁祸首是克洛蒂娜，却还选我做你的搭档，而不是选她，这不是毫无道理吗。"
show celine annoyed2 w with dissolve
Celine "我讨厌来这儿。这地方又老旧，走起路来吱呀作响，还一股锯木屑的味儿。"
Celine "我也不想把沉重的木头拖回教室。手掌会扎进木刺，而我要继续弹钢琴的话，就得让这双手好好的。"
show celine frown2 w with dissolve
Celine "我不确定你是否知道这件事——布吕吉埃夫人相当倚重我。"
"塞琳伸出手让我细看，虽然她本无必要这么做。今天早些时候我曾见过她弹钢琴，我知道她那纤细的手指有多优雅。"
"她弹钢琴时，仿佛整个人都沉醉在音乐中。她的神情温柔恬静，宛如一个内心已获致宁静的人。"
"然而此刻，塞琳却是一副再恼怒不过的模样——而这一切都怪我。"
Marcel u sad "抱歉，我没考虑到这一点。"
show celine sigh2 w with dissolve
Celine "哦，也许你本该想到的。"
show celine frown2 w with dissolve
Celine "我并不想针对你，玛塞尔，可你确实该多体谅别人一点。"
"塞琳的话语比屋外凉爽的秋风还要刺人。"
"我被教训得哑口无言，垂下了头。"
Marcel "对不起，塞琳。我知道我太欠考虑了。我不是存心惹你不高兴。只是……"
Marcel u huh "在所有同学里，我想，如果我跟你一起去柴房，我会觉得最自在。"
Marcel "克洛蒂娜太闹腾，露丝几乎不开口，米拉贝尔又那么羞怯，我真不知道该怎么跟她单独说话。"
Marcel "我想，至少我还能跟你客客气气地聊上几句。"
Marcel u ehe "毕竟，我们之间确实有不少共同之处。"
show celine annoyed2 w with dissolve
Celine "是吗？"
"塞琳哼了一声，双臂交叉抱在胸前。"
show celine frown2 w with dissolve
Celine "那是什么呢，愿闻其详？"
Marcel u huh "这个嘛……也许是我自作多情，不过……我们俩都不是Myennes本地人。我们都来自更大的城市。"
Marcel "我来自巴黎，而你来自……奥尔良，我记得克洛蒂娜是这么说的？"
show celine annoyed2 w with dissolve
Celine "克洛蒂娜话太多了。她早该知道，别去打听不该打听的事——你也一样。"
show celine frown2 w with dissolve
Celine "我不太喜欢提起我从前的老家，不过……"
show celine sigh2 w with dissolve
"塞琳叹了口气。"
Celine "这一点你说得没错。我确实不是Myennes本地人。"
show celine sad2 w with dissolve
Celine "这所学校里许多女孩就住在这儿，或者住在这附近，打从她们出生起就是了；可我到这里才一年。"
Marcel u smile "那也比我多一年。我今天才第一天来！"
Marcel "咱们两个人当中，我觉得你对这里的了解最多。"
"我朝塞琳微微一笑。起初她并没有回应（也许是因为这里太昏暗，她看不见我的笑容）……"
show celine neutral2 w with dissolve
"但片刻停顿之后，她的嘴角微微上扬。"
"她在回以微笑。"
"有那么一瞬间，我担心自己得罪了塞琳，可幸好看来我的担忧只是多余的。"
"塞琳或许看似冷淡疏离，但我认为那并非她性格的全部面貌。"
"倘若她真如外表那般傲慢，就不会费心去斥责克洛蒂娜的刻薄，也不会在我们那堂倒霉的英语课上替杜布瓦夫人辩护。"
"说到底，她想必是个善良的人。"
Marcel u sad "这话听起来也许很傻，甚至有点戏剧化，可……自从我到了这儿，我就觉得自己格格不入。你知道吗……"
"我深吸了一口气。"
Marcel u huh "直到昨天为止，我一辈子都住在巴黎。我对乡村，或者对这里的行事方式，几乎一无所知。"
Marcel "我曾希望，既然你也有过和我相似的处境，或许你能体会我的感受。"
Marcel "无论如何，那都会让我觉得自己没那么孤单。"
show celine frown2 w with dissolve
Celine "你{i}真的{/i}感到孤单吗？"
Marcel u shy "倒也谈不上孤单，只是有点让人喘不过气来。"
Marcel "你当初来这里的时候，也是这样吗？你不担心吗？"
show celine sad2 w with dissolve
Celine "我不愿回想那段日子。那是我人生中相当黑暗的一段时光，不过……"
show celine frown2 w with dissolve
Celine "你并不孤单，玛塞尔。"
show celine sigh2 w with dissolve
Celine "我承认，起初我也很不安。我想，要是谁突然被告知要搬去那么远的地方，都会这样吧。"
Celine "我不想离开奥尔良，不想离开我的姐姐们，也不想离开那幢漂亮的房子，可在这件事上我几乎没有选择。我父亲想摆脱我，而我无力反抗。"
Marcel frown u "你父亲？"
"我皱起了眉头。"
"我觉得这一切背后另有隐情，可还没等我开口询问（说实话，我也不确定自己会问什么），塞琳就先开了口。"
show celine sad2 w with dissolve
Celine "不过，我能体会你的心情。我懂得做一个局外人是什么滋味。"
Celine "已经一年了，这里或多或少开始让我觉得像个家了，可我常常在想，同学们究竟是否真的接纳我。"
show celine annoyed2 w with dissolve
Celine "那些愚蠢又爱嚼舌根的女孩们，似乎仍把我当作外来者，而那个克洛蒂娜是她们当中最过分的！"
Celine "她总是问些多管闲事、冒犯无礼的问题，仿佛我有义务一定要回答她似的！"
Celine "我来这里不是为了回想过去的。我宁可活在当下。可是，当一个人不断被唠叨纠缠时，这就不那么容易了。"
Marcel huh u "我不太确定自己喜欢这种说法。"
Marcel sad u "我不想被人盘问；尤其是被克洛蒂娜盘问。那听起来有点吓人。"
show celine neutral2 w with dissolve
Celine "哦，你不必为此担心。克洛蒂娜也许很缠人，但你没什么好怕的。你若不想跟她说话，随时可以不搭理她。"
Marcel sigh u "那说起来容易，做起来可就难了……"
show celine frown2 w with dissolve
Celine "这有个诀窍。你只需学会如何装出毫不在意的样子。"
show celine sigh2 w with dissolve
Celine "若想在这里过上安宁的日子，你最好学会无视克洛蒂娜的挑衅。"
Marcel huh u "我会记住的……"
Marcel sigh u "不过，要消化的东西实在太多了。"
show celine sad2 w with dissolve
Celine "你觉得很难吗？"
Marcel neutral u "有一点。认识所有新同学，可真是一番经历……"
Marcel sad u "不过，要是昨晚我能多睡一会儿，也许我的表现会好一些。"
Celine "你当时是躺在床上睡不着，担心得无法安歇吗？"
Marcel sigh u "是这样。"
"塞琳轻而易举地看穿了我，尽管这柴房里如此昏暗。我要么是一本摊开的书，要么就是她也曾在搬到乡下之后熬过相似的难眠之夜——尽管黑暗已将我们紧紧围拢。"
Marcel sad u "我担心所有同学都会排挤我。我一直为融入大家而苦恼，直到凌晨。"
Marcel sigh u "我……在上一所学校没什么朋友，你知道的。"
"又或者，并无任何缘由。"
Marcel sad u "我担心，要是我在巴黎那样的大城市都找不到自己的位置，那么在这么一座小村子里，我就更没指望了。"
Marcel "我不想被冷落。"
Marcel sigh u "我怕自己永远无法融入，一个朋友也交不到。"
Marcel "这很可怕。"
show celine neutral2 w with dissolve
Celine "比克洛蒂娜还可怕？"
Marcel shock u "可怕得多，可怕得多！"
show celine sigh2 w with dissolve
Celine "嗯。好吧，这事听起来{i}的确{/i}很严重。我看得出来，你是个相当容易焦虑的女孩。"
"她如今竟能看穿我了吗？我不禁好奇究竟是什么让她起了疑心。"
show celine sad2 w with dissolve
Celine "你似乎是那种会在脑海里构想出种种最坏情形、然后深陷其中无法自拔的人……"
show celine neutral2 w with dissolve
Celine "但别担心。到头来，我自有办法化解你这层忧虑。"
Marcel huh u "什么……？"
"我抬起头，目光与塞琳相遇：我的湛蓝对上她的深褐。"
"我知道这不过是我的想象，却感觉有什么东西在我们之间流转而过。那是一阵无声的低语，又或许是一道闪念，让我被塞琳吸引，这是任何旁人都未曾给过我的感觉。"
"她理解我。"
"当然，她并非理解{i}全部{/i}的我，但她懂得我的羞怯，那是旧日学校里任何一个同学都不曾做到过的。"
"我不禁想，这会不会是因为她能与我产生共鸣呢？"
show celine frown2 w with dissolve
Celine "我们有些同学无疑会像克洛蒂娜那样来盘问你。她们绝不会让你有片刻安宁。"
Celine "而另一些同学，比如露丝或米拉贝尔，多半会跟你保持距离……"
show celine neutral2 w with dissolve
Celine "但如果你需要的是一个朋友，我想我并不介意扮演这个角色。"
Celine "我们彼此还不太了解，不过时间还充裕。我们会在一起待上一年，所以……{w}你觉得如何？"
Celine "你愿意做我的朋友吗？"
Marcel shock u "哦，当然！我当然愿意！我——"
"我正想开口……却见塞琳带着几分揶揄地微笑起来，我这才意识到自己方才听起来有多恳切。"
Marcel shy u "我是说，嗯……咳咳……"
Marcel ehe u "我……如果你不介意的话，我也愿意做你的朋友。我会深感荣幸。"
show celine smile2 w with dissolve
Celine "荣幸，是吗？哎呀呀。"
"塞琳咯咯地笑了。"
Celine "你还真是能说会道。你简直像个绅士。你要当绅士，个头也绝对是够了！"
Marcel shock u "什——什么？不，我才不是……"
"我的声音渐渐低了下去，被自己的焦虑吞没。"
"塞琳或许向我伸出了友谊的橄榄枝，但她是不会把它递给马塞尔·德·圣雷米的。"
"就我所知，塞琳并不知道有这人存在。"
"她以为我是玛塞尔·雷诺。正因如此，我必须扮演好这个角色。我需要她（也包括我其余的同班同学）相信我是一个女孩。"
"可是，我不禁担心，万一塞琳得知我的真相，会怎么样。她会认为我是个骗子吗？"
"如果真是这样，那我们这份“友谊”恐怕就会化作尘土了。"
show celine frown2 w with dissolve
Celine "玛塞尔？"
"塞琳注视着我，那双褐色的眼睛睁得大大的，满是好奇。"
Celine "你还好吧？"
Marcel "哦——哦，是的！我没事。我只是有点……走神……"
show celine sad2 w with dissolve
Celine "你一定累坏了。你今天忙了一整天，明天多半也会很忙。"
show celine shock2 w with dissolve
Celine "你今晚可得好好补补觉，不然你会发烧的！"
Marcel ehe u "是，夫人。"
"我温顺地答道，这让塞琳笑了起来。"
"我想这是头一回听到她笑。她的笑声也很动听；轻快而清脆，宛如一首在钢琴上弹出的旋律，与她很相配。"
show celine neutral2 w with dissolve
Celine "说起来，被人依靠的感觉确实不错。"
Celine "我自己有两个姐姐，她们总把我当成小孩子，或者一只小宠物。我是家里最小的那个。"
show celine frown2 w with dissolve
Celine "我母亲对我百般宠爱，而我父亲似乎从没把我当回事。"
show celine smile2 w with dissolve
Celine "不过，如今你我之间的情况可不一样了！"
show celine neutral2 w with dissolve
Celine "我在这里待得比你久，所以按理说，该由我来引导你。"
Celine "我一直觉得，要是有个自己的妹妹，让我能好好宠她、疼她，那该多好……"
show celine smile2 w with dissolve
Celine "不过，光是看我们俩的样子，我怀疑没人会相信你比我小。"
Marcel sigh u "这么高，真是抱歉。"
show celine neutral2 w with dissolve
Celine "没关系。你个子或许很高，可你温顺又讲礼。你比克洛蒂娜规矩多了！"
show celine frown2 w with dissolve
Celine "仔细想想，我真的觉得，要是我们能多聊聊，那会很好。"
show celine smile2 w with dissolve
Celine "只是以后别再把我卷进那些粗活了。我这双手宝贵得很，我不会让任何人——哪怕是朋友——毁掉它们。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  9月16日{vspace=1}  失眠") )
scene cg28 with wiperight_slow
play ambience "sfx/night_amb2.ogg" fadein 1.0
play music "bgm/Night.ogg" fadein 1.0
window show dissolve

"那一夜我躺在床上，望着墙壁，在渐浓的昏暗之中，我的双眼几乎失去了视觉。"
"我知道自己该睡了（塞琳也这般劝过我），可我的脑子偏不肯配合。"
"有时候，我不禁怀疑它是不是恨我，才会这样不停地折磨我。"
"我的身体疲惫不堪，可梦乡却迟迟不肯眷顾。"
"我无法停止想起塞琳。"
"起初我以为她难以接近，可细想之后，或许我评判得太过仓促了。她似乎是个真诚的女孩，只是稍显矜持，我很感激她愿意做我的朋友。"
"鉴于我特殊的处境，我并不完全确定自己是否配得上她的友谊，可我也不想将她推开。我怕那样会冒犯她——或者更糟，让她难过。"
"塞琳虽没有明说，但我想她或许也很孤独。"
"我见过她和克洛蒂娜相当自在地拌嘴，但我不会称她们为朋友。她们彼此太过敌对，够不上朋友二字。"
"我认为克洛蒂娜还没有完全接纳塞琳成为她的同窗：单从她那些说塞琳对米延“太好了”的刻薄话来看，就可见一斑。"
"我们其他同学似乎都心照不宣地认为，尽管塞琳在这儿住了一年，她仍是个外人。"
"他们倒没有刻意疏远她，却也不会像对待其他同学那样，对她露出同样轻松友好的笑容。"
"米拉贝尔或许是个例外，但她实在太害羞，又容易结巴，很难与她好好交谈。"
"塞琳力图装作对这一切不为所动的样子，可我不禁怀疑那是不是在故作姿态。"
"在她住于米延的这段日子里，她一直都没有朋友吗？"
"若真是如此，那就能解释她为何（在略微迟疑之后）显得那么热切，要宣称自己是我的新朋友。"
"如果塞琳真心想要我的陪伴，那我就留在她身边。我想与她多相处些时日，也盼着咱们两人能变得更加亲近。"
"尽管我害怕她可能发现真相，可我更害怕的还是孤身一人。"
"我不像塞琳那样坚强，我想自己也承受不了这份被拒绝。"
"我不想被视为一个外人。"
"在我这一生里，哪怕只有一次，我希望能有一个理解我、也能被我理解的朋友——尽管我不禁怀疑这究竟有多大可能。"
"当我自己都不完全明白自己是谁时，我又怎能向塞琳敞开心扉呢？"
"这真是个棘手的问题，它折磨了我整整一夜。"
"到最后，尽管我曾向塞琳保证过，我还是没能睡上多少觉。"

stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene sky g
with clockwipe
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

scene sky with dissolve
play music "bgm/Mysterious.ogg" fadein 1.0
$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  9月17日{vspace=1}  不祥之兆") )
window show dissolve

"夜里我醒了好几次，梦里满是焦虑。"
"清晨来临时，我已记不清这些梦的细节，但仍能想起它们的大致梗概。"
"我想我正与父亲在一起。他带我去了一家咖啡馆，但那并非我与母亲、阿尔贝汀姨妈去过的那家。它要更为气派，满铺着华贵的地毯，悬着闪亮的水晶吊灯。"
"我的梦里交织着一首奏鸣曲柔和而细碎的乐音。"
"那或许是贝多芬的奏鸣曲，可我也并不确定。正如克洛蒂娜乐于指出的那样，我的音乐素养简直糟得惊人。"
"我隐约记得，梦里有个人在弹着那架钢琴。那人留着黑发，梳成一条整洁的辫子，穿着我姨妈学院的制服。"
"那是塞琳。"
"当她看到我穿着男孩的装束、由父亲陪同着时，那双纤细的手从黑白琴键上滑落了下来。她瞪着我，神情骇然，她呼喊道……"
"嗯。我也不太确定她喊了些什么，但想必不是什么好话。"
"但愿这个梦不会成为什么不祥之兆。"
"我穿好衣服，然后端详起床头柜那面带有裂缝的镜子里的自己。"

scene cg29 with wipedown_slow

"因为一夜辗转难眠，我的头发乱蓬蓬的，我也能看到自己眼底浮现的圈圈黑晕。"
"我想这些深得宛如淤青的阴影，甚至都能让克洛蒂娜相形见绌了。"
"我岂止是看起来疲惫，简直是一副贫血的模样。"
Marcel "马塞尔，你简直跟一具尸体差不多。一位淑女就该是这个样子吗？"
"我挑剔地端详着镜中的倒影。它学着我的一举一动，那半垂的眼皮因自我苛责而眯了起来。"
"我叹了口气。"
"我下床还不到十分钟，就已经只想蜷进被窝里睡上一觉了。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  9月17日{vspace=1}  恶名夫人") )
scene sky with wiperight_slow
play ambience "sfx/birds.ogg" fadein 1.0
play music "bgm/Classroom.ogg" fadein 1.0
window show dissolve

"早上的课我很难保持清醒，我只能不停地用笔尖戳自己，好让自己留在清醒的人间。"
"而这些课程本身也丝毫不能让我睁开双眼（在此向阿尔贝汀姨妈致歉）。"
"尽管我姨妈早有警告，我们的数学课却相当简单粗浅。我在心算方面算不上有天赋，可这些练习我早在旧日学校就做过类似的了。"
"课本里——实际上还有黑板上——那些散落的数字，只会让我更加昏昏欲睡。"

play sound "sfx/churchbells.ogg" fadein 1.0

"当远处教堂的钟声响起，宣告着今天头一次课间休息的到来时，一股如释重负的感觉涌遍了我全身。"
"终于能逃离了！"

stop sound fadeout 3.0
stop ambience fadeout 1.0
scene classroom:
    size (1920, 1080) crop (280, 40, 1440, 810)
show al annoyed2:
    xpos 0.50 xanchor 0.5 ypos 0.5 yanchor 0.5
with wipedown_slow

Bru "好了，姑娘们，你们可以下课了——但{i}别{/i}——"
"布吕吉埃夫人与克洛蒂娜的目光相遇。"
show al frown2 with dissolve
Bru "——像一群疯狗似的冲出去。你们要慢慢地、小心地走，做端庄有礼的年轻淑女。"
Bru "我不希望你们给低年级的学生做个坏榜样！"
Claudine u smile "是，夫人。"
"克洛蒂娜回答得倒也亲切，可我不确定她是不是真心的——布吕吉埃夫人似乎也同样存疑。她的眉头皱得更深，愈发凸显出眼角与嘴边的一道道皱纹。"
show al annoyed2 with dissolve
Bru "至于你，米拉贝尔……"
"布吕吉埃夫人锐利地看向米拉贝尔。"
Bru "我看见你打瞌睡了。下次请专心些。这间教室里要是有人需要补习算术，那个人就是你。"
Mirabel shock "是——是的，夫人！非常抱歉！"
show al frown2 with dissolve
Bru "你想道歉随你，可光道歉并不能提高你的成绩。你若真心为你的行为感到抱歉，往后就该更用功。"
Mirabel "是——是的，夫人！我会的！"
show al neutral2 with dissolve
Bru "很好。那么接下来，玛塞尔……"
"布吕吉埃夫人逡巡的目光落在了我身上。我咽了咽口水。"
Marcel shy u "是——是的，夫人……？"
show al annoyed2 with dissolve
Bru "我知道你是新来的学生，一定被这周围的一切弄得不知所措。鉴于你情况特殊，我这次就宽容一些，不过以后请你别再在我的课上打哈欠。那是极不礼貌的。"
Marcel "嗯……"
"我害羞地低下头看着桌面，双颊泛起淡淡的粉红。"
"我本想偷偷隐瞒课堂上不断袭来的睡意，可布吕吉埃夫人还是注意到了。"
"什么都瞒不过她。她长着一双鹰一般的眼睛！"
Marcel sad u "我——我，嗯，非常抱歉，夫人。我昨晚没怎么睡。"
show al sigh2 with dissolve
Bru "那也绝不能成为你行为失当的借口。"
"布吕吉埃夫人抿紧了嘴唇。"
show al annoyed2 with dissolve
Bru "你已经十五岁了。这个年纪，应该足以自己安排作息。别指望我会可怜你。"
show al frown2 with dissolve
Bru "若你再继续惹恼我，我会像对待这里其他女孩一样处罚你！"
Bru "别以为因为你是从巴黎来的，就能得到特殊优待。"
Bru "毋庸置疑，这所学校比你习惯的要小，但我不允许你轻视它，或轻视我的课！"
play sound "sfx/slap.ogg"
with vpunch
"布吕吉埃夫人一掌拍在自己的讲桌上，吓得我猛地一颤。"
"这好歹帮我驱散了些睡意，可当着同学们的面挨骂实在丢人——而且还是被自己的姨妈责备！"
"不过，我也许不该再把她当成我的阿尔贝汀姨妈了。只要我还住在米延，她就始终是布吕吉埃夫人。"
"她是我的老师，我是她的学生，她不能对我表现出任何偏袒。那样对其他女孩不公平。"
"我只希望她不会为了证明些什么，而对我格外严厉，比惩罚她们更苛刻地责罚我……"
show al neutral2 with dissolve
Bru "好了，就这些。你们可以走了。"
"说完这番话，屋里的紧张气氛便缓和了下来。"
# sfx?
"女孩们站起身来，椅子刮擦着地板，争先恐后地朝门口涌去，裙摆沙沙作响，辫子随之蹦跳。"
show al shock2 with dissolve
Bru "姑娘们！姑娘们！"
"布吕吉埃夫人冲着夺门而逃的学生们喊道，声音尖锐而刺耳。"
Bru "我刚才怎么跟你们说的？请{i}规矩些{/i}！{i}不要{/i}在教室里奔跑！"

show image "border" onlayer border
scene classroom:
    subpixel True
    size (1920, 1080) crop (300, 100, 1280, 720)
    linear 20.0 crop (300, 300, 1280, 720)
with wipedown_slow

"我没有随其余人一起起身。我觉得自己实在太虚弱了，更别提有多气馁。"
"就算同学们全都在嘲笑我，我也不会觉得意外。"
"我留下的印象实在算不上好。"
Marcel sigh u "天哪……"
"我深深地叹了口气，这引起了邻座同学的注意。"
"克洛蒂娜咧嘴笑着，朝我瞥了一眼。"

hide image "border" onlayer border
scene classroom:
    size (1920, 1080) crop (0, 40, 1440, 810)
show claudine smile2:
    xpos 0.35 xanchor 0.5 ypos 0.55 yanchor 0.5
with wipeup_slow

Claudine "好了，亲爱的玛塞尔！干吗板着张脸？"
Marcel huh u "克洛蒂娜……"
"我闷闷不乐地看着这位同学，丝毫没有掩饰自己的难堪。"
Marcel "你找我有什么事吗？"
Claudine "也许吧。你干吗这么问？"
Marcel "我还以为教堂的钟声一响，你就会是头一个跑出大门的人呢。"
show claudine smile2 with dissolve
Claudine "哦，你还真没说错！我一向的习惯就是能早些溜走就早些溜走——这教室闷得慌！——不过嘛，唔……"
"克洛蒂娜那了然于心的笑意扩大了。"
Claudine "我今天倒想破个例。"
Marcel frown u "为什么？想捉弄我吗？"
show claudine laugh2 with dissolve
Claudine "那倒也不是没趣的念头，不过我想，你如今已经被训得够惨了。"
Claudine "说真的，才这么点工夫你就能惹得布吕吉埃夫人大发雷霆，可真够厉害的！你到这儿才整整一天呀！"
Marcel sigh u "我并不是{i}存心{/i}要惹她生气。我只是想让自己别睡着。"
show claudine huh2 with dissolve
Claudine "是啊，我看见了。你老是用笔尖戳自己的手，现在瞧瞧你！"
"克洛蒂娜探身越过书桌，把我的手握进她的掌心里。她把我的手翻过来，端详着印在我拇指根部的一个小黑点。"
"它看起来有几分像一颗美人痣，只不过这种痣若被游移的手指轻轻一拭，便会晕成一团。"
show claudine smile2 with dissolve
Claudine "你的手长得很好看，玛塞尔——皮肤也非常好。你真该多上点儿心保养才是！你眼下的眼袋简直惨得没法看！"
Marcel sad u "多谢你的建议，不过……"
"我把手从克洛蒂娜那里抽了回来（她难道不懂得什么叫私人空间吗？），然后贴在胸前护着。"
Marcel frown u "你也好不到哪儿去。你眼下也有黑眼圈呢。"
Claudine "那不一样。我天生就是这样。"
Marcel huh u "真的吗？"
show claudine laugh2 with dissolve
Claudine "真的呀！这可是我的魅力所在！我小时候，我爸爸还管我叫他的小尸体呢！"
Marcel shock u "那……那算是恭维吗？"
Claudine "我想是吧，没错！"
"克洛蒂娜咯咯地笑了起来。"
Claudine "我爸爸的幽默感一向很奇怪！"
Marcel frown u "这想必是家传的……"
"我摇了摇头。"
Marcel "我怕是领会不了你那份雅趣。"
show claudine smile2 with dissolve
Claudine "那没什么！其实我正巴不得这样。我就喜欢当谜一样的人！"
Claudine "要是咱们才说过几句话，你就能把我整个人都看透，那我这个女子也当得太差劲了！咱们总该有些秘密才是！"
show claudine smirk2 with dissolve
Claudine "说到秘密……"
"克洛蒂娜的眼里闪着狡黠的光。"
Claudine "陪我去餐厅好吗？在那儿，你可以把你巴黎的生活、你从前的学校，还有你那些老朋友，都讲给我听！"
show claudine laugh2 with dissolve
Claudine "我真想把你{i}所有{/i}的事都弄个一清二楚！我敢肯定，你那双疲惫的眼睛后头，藏着成堆的秘密呢！"
Marcel shock u "什么？啊，不……"
"一提起「秘密」二字，我便浑身一震。我本就苍白的脸，此刻变得更加惨白。"
Marcel sad u "我真的没那么有意思……"
show claudine smile2 with dissolve
Claudine "好了好了！别这么妄自菲薄！这可得{i}我{/i}说了算！"

play sound "sfx/chair.ogg"
show claudine:
    ease 0.8 ypos 0.50 yanchor 0.5

$ renpy.pause(0.4)

scene classroom
show claudine smile:
    xpos 0.35 xanchor 0.5 ypos 0.5 yanchor 0.5
with dissolve

"克洛蒂娜站起身来，然后挽住我的胳膊，把我一并拉了起来。"
show claudine smile2 with dissolve
Claudine "咱们走吧！机不可失，时不再来！"
Marcel shock u "喂、喂，克洛蒂娜！快停下……！"
show claudine smirk2 with dissolve
Claudine "抱歉啦，我可不会听话。你这么有趣的奖品，我可舍不得错过！"
Marcel "奖……奖品？我、我才不是什么奖品！我不过是个普普通通的姑娘！"
Marcel shy u "而、而且，我记得是你自己说的，女人也该有些秘密。为、凭什么我就得把我所有的秘密都讲给你听？"
show claudine laugh2 with dissolve
Claudine "因为你自己也承认了，你是女孩，不是女人。女孩子又甜又天真，可存不住多少神秘感！"
Claudine "你还是把{i}一切{/i}都告诉我吧，亲爱的玛塞尔！我可不愿见你被那些憋在心里的东西压得喘不过气来！"
show claudine smile2 with dissolve
Claudine "你瞧，我这是在让你在这里更自在些呀。"
show claudine laugh2 with dissolve
Claudine "我可真是个大好人呀！"
"就我个人而言，我倒觉得克洛蒂娜是个厚颜无耻的江湖骗子，而非什么乐善好施的善人。"
"她声称想帮我，可我知道，这不过是她为了满足自己好奇心的托辞罢了。"
"我想，她就算再努力，也不可能把真实意图表现得更露骨了。"
"我实在不想陪她去餐厅。"
"我太累了，实在没精力陪她玩「二十个问题」的游戏——不过，以我对克洛蒂娜的了解，她那二十个问题很快就会变成三十个、四十个、五十个，甚至一百个。"
"我怕她这么连番轰炸下去，会把我编造的那些往事的细节搅得一团糟，到时候她一眼就能看穿我。"
"这可能会非常糟糕。"
"我怎样才能甩掉她，又不惹她生气呢？"
"我感到无助，正犹豫不决，手臂还紧紧被克洛蒂娜挽着，然后……"

play sound "sfx/footsteps3.ogg" fadein 0.5
show celine annoyed:
    xpos 1.10 xanchor 0.5 ypos 0.53 yanchor 0.5
    ease 1.8 xpos 0.75

$ renpy.pause(0.8)

stop sound fadeout 0.5

Celine "克洛蒂娜！你在干什么？"
show claudine smile2 with dissolve
Claudine "哦，塞琳！我没看见你在那儿。"
"克洛蒂娜转过身来，胳膊仍旧挽着我的，微微一笑。"
Claudine "你要不要一起来吃饭？"
show celine sigh with dissolve
Celine "不了，谢谢。"
show claudine shock2 with dissolve
Claudine "什么？你不去？！"
"克洛蒂娜噘起了嘴。"
show claudine annoyed2 with dissolve
Claudine "我知道，瞧你那副拘谨古板、假正经的模样，你准是觉得自己比我们这些人都要高贵——"
show celine shock with dissolve
Celine "喂、喂！我{i}才不是{/i}假正经呢！"
show claudine shock2 with dissolve
Claudine "——不过，哪怕你再是个名门淑女，我也知道你心里肯定也好奇！"
show claudine smile2 with dissolve
Claudine "你不想跟我一起，把玛塞尔的底细掏个明白？她身上也有许多你必定好奇的事呢！"
Claudine "跟我们来吧。别担心，我不会吃人，玛塞尔就更不会了！她可是有两条胳膊的，看见没？你挽一条，我挽一条！"
show claudine laugh2 with dissolve
Claudine "我们三个好朋友可以一起在学校里闲庭漫步。听起来是不是很美？"
show celine frown with dissolve
Celine "在你听来也许很惬意，可我怕玛塞尔未必欣赏你这番好意。"
show claudine smile2 with dissolve
Claudine "哦，她不介意！这不过是闹着玩，对吧，玛塞尔？"
"克洛蒂娜的语气很轻松，可她的手臂却像铁钳一样紧紧箍着我，指甲还掐进了我的掌心。这滋味可不太好受。"
Marcel shy u "我、呃……我自己也说不准……"
show claudine neutral2 with dissolve
Claudine "什么？你不愿意当我的朋友吗？！"
Marcel sad u "我、我可没这么说过。你要是真拿我当朋友，我自然感激不尽，可我真受不了被人那样刨根问底。"
Celine "瞧见了吧？你把玛塞尔弄得局促不安了。别打扰人家。"
show claudine annoyed2 with dissolve
Claudine "为什么？好让你趁虚而入，把她一个人独占了？"
show celine sigh with dissolve
Celine "确实就是这个主意。没错。"
"塞琳以一种十分冷静、就事论事的态度，反驳了克洛蒂娜那句尖刻的话。"
show celine huh with dissolve
Celine "阿梅莉今早替我做了午饭，我带来了。我打算在校园里吃。那里比餐厅清静多了。"
Claudine "哦，对。我几乎忘了。你不是从来都不肯跟我们这些粗人一起吃饭的吗？你呀，就是爱摆架子。"
show celine sigh with dissolve
Celine "而{i}你{/i}才真是不讲理。我们谁都有各自的毛病。"
show celine huh with dissolve
Celine "我正要问玛塞尔，她是否愿意陪我一起在外面用饭。她要是累了，我想安静对她大有裨益。"
Celine "你愿意吗？"
"我的目光在仍紧挽着我手臂的克洛蒂娜与端庄优雅的塞琳之间来回游移。"
"我以前从未遇到过这样的情形。在原先那所学校里，我几乎没什么朋友，所以从来不必为「在两个之间选择与谁相伴」而发愁。"
"如今，却有两位姑娘争着要博取我的关注。"
"这有点尴尬。我谁都不想得罪……但，在经历过多年相对孤独的生活之后，这几乎也算得上一个甜蜜的烦恼了。"
"我以前经历过比这糟糕得多的处境。"
"我的人气比我预想的高得多——不过我知道，克洛蒂娜对我的兴趣并非源自「我这个人」，而是因为我「新来的女孩」这个身份。"
"她把我当成一件稀罕的玩意儿，而不是一个真正的人。"
"既然如此，我想我更愿意和塞琳一起吃饭。"
Marcel ehe u "我、呃……我挺愿意的。谢、谢谢你的邀请，塞琳。"
show celine neutral with dissolve
Celine "别客气。阿梅莉总给我做太多吃的，我一个人总是吃不完。"
show celine sigh with dissolve
Celine "有时候我真不知道她心里把我当成什么！她像是以为我的胃口抵得上一个壮实的伐木工，而我不过是个十五岁的姑娘罢了。"
show celine smile with dissolve
Celine "要不是她做的饭那么可口，我几乎就要恼羞成怒了！"
Claudine "哼。好吧，行。我算是看明白了。"
show claudine annoyed with dissolve
"这番对话让克洛蒂娜很不高兴，她松开了挽着我的胳膊，皱着眉头退开，双手交叉抱在胸前。"
Claudine "你准是觉得，自己金贵得很，不屑跟我们这种乡下姑娘打交道吧！"
Marcel shock u "什么？不、不是的——"
Claudine "{i}拜托。{/i}"
"克洛蒂娜翻了个白眼。"
Claudine "你的道歉就省了吧。我看透你了，玛塞尔。"
Claudine "我起初没把你当成势利眼，可你要是宁愿要塞琳作伴也不愿跟我待在一起，那你八成就是这么一号人。"
Claudine "好罢。随你。你们这些讲究的小姐就丢开我去乐吧。如今我可{i}真真切切{/i}知道自己的位置了。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  9月17日{vspace=1}  二人茶会") )
play music "bgm/Celine.ogg" fadein 1.0
scene yard:
    size (1920, 1080) crop (240, 140, 1440, 810)
show celine neutral2:
    xpos 0.5 xanchor 0.5 ypos 0.55 yanchor 0.5
with wiperight_slow
window show dissolve

Marcel huh u "哇……这{i}确实是{/i}好多吃的呀。"
show celine sigh2 with dissolve
Celine "我知道。我说阿梅莉做得太多，可不是在开玩笑。她总是这样，只是我怎么也想不通缘由。"
Celine "我希望她不会把我当成个贪吃的人……"
show celine neutral2 with dissolve
Celine "总之，这儿的菜不少，你尽管放开吃，别客气。请便吧。"
Marcel smile u "谢、谢谢你。那我就恭敬不如从命了……"
"我小口地咬着一块自制的咸派。我没有盘子可放，所以得小心不把碎屑掉在裙子上。"
"这期间，一阵轻柔的风拂乱了我的头发。"
"塞琳和我盘腿坐在庭院里一棵橡树下。"
"塞琳带来了一条毯子，外加一个柳编野餐篮，我们俩就坐在上面，裙摆在腿边铺展开来。"
"塞琳一边抚平毯子上的褶皱，一边告诉我说，她绝不会做出直接坐在湿润、带露水的草地上这种邋遢不雅的事。"
"我的大多数同学都在餐厅里用餐，庭院本身倒是相对宁静。"
"我能听见树丛间鸟儿微弱的啁啾，还有头顶上树叶的沙沙声。"
"当然，选择在户外吃午餐的学生并不只有塞琳和我。还有少数几个学生自带了食物，而没有在室内用餐：米拉贝尔就是其中之一。"

show image "border2" onlayer border
scene yard
show marie neutral:
    xzoom -1 xpos 0.30 xanchor 0.5
show mirabel neutral:
    xpos 0.70 xanchor 0.5
with wipeleft_slow

"米拉贝尔坐在离塞琳和我几步远的地方，正陪着一位留着一头参差黑发的年轻女孩。"
"那个黑发女孩双手捧着一块肉馅饼，像松鼠一样小口小口地啃着。"
show mirabel smile with dissolve
"米拉贝尔望着她，露出宠溺的微笑，伸手替她拂去下唇上的几粒碎屑。"
Mirabel "哎呀，玛丽-诺埃尔，你可当心点儿！当心把制服弄脏了！"
show marie laugh with dissolve
Marie "没关系，就算是脏了也不要紧。"
"那位想必叫做玛丽-诺埃尔的年轻女孩，用柔软、带着睡意的语调回答。"
Marie "我知道你会帮我收拾的。"
show mirabel shock at bounce
Mirabel "嗯……唔，我可拿不准自己是什么感觉！"
show mirabel sad with dissolve
Mirabel "你真该对自己的整洁多负些责任。你很快就十岁了，我也不能永远这样照看你呀！"
show marie sad with dissolve
Marie "可是我不想你走……"
Mirabel "我也不想离开，可那迟早会来的。我也在慢慢长大呀。"
show marie shout with dissolve
Marie "不要！我不喜欢！我不喜欢，可是……"
Marie "你要是真的一定要走，那你就得更疼我！趁眼下还有机会，你得好好把我宠坏！"
show mirabel smile with dissolve
Mirabel "天哪！原来是这么回事吗？"
Marie "就是这样，就是这样！宠我，宠我！"
show mirabel ehe with dissolve
Mirabel "哎呀，玛丽-诺埃尔……"
"我想玛丽-诺埃尔应该是中级班的学生。她个子很小，看起来顶多七八岁。"
"她和米拉贝尔是亲戚吗？我猜她们也许是姐妹，但长得并不太像。"
"我一边思索着这个谜团，一边吃完了最后一口咸派。塞琳始终静静地看着我，漂亮的脸蛋上挂着一抹浅笑。"

hide image "border2" onlayer border
scene yard:
    size (1920, 1080) crop (240, 140, 1440, 810)
show celine neutral2:
    xpos 0.5 xanchor 0.5 ypos 0.55 yanchor 0.5
with wiperight_slow

Celine "那么，你觉得如何？好吃吗？"
Marcel laugh u "很好吃。简直太好吃了！"
show celine smile2 with dissolve
Celine "谢天谢地。你喜欢就好。"
show celine sad2 with dissolve
Celine "我倒希望这功劳算在我头上……可我实话实说，我并不擅长做菜。"
Marcel huh u "是吗？"
"我好奇地歪了歪头。"
Marcel "我还以为你会呢，看你多心灵手巧。"
show celine neutral2 with dissolve
Celine "你指的是我的琴艺？"
"塞琳一只手托着下巴，若有所思。"
Celine "我想我弹钢琴还算是有些心得，但我还有许多要学的。若我的课不是如此突然被终止，我现在会比如今更出色。"
show celine smile2 with dissolve
Celine "比起瓦雷纳先生来，我可就微不足道了。"
Marcel neutral u "瓦雷纳先生？"
show celine sad2 with dissolve
Celine "他是我的钢琴老师——或者说，{i}曾经是{/i}，直到我搬来这里为止。"
"塞琳叹了口气。"
show celine sigh2 with dissolve
Celine "好吧。先把这事搁下不提……"
show celine shy2 with dissolve
Celine "我在厨房里的本事，还不及我弹琴的一半。说到家务，我可从没受过什么教导。"
Celine "我缝纫穿针还算凑合，也懂些简单的针脚，可一到厨房里我就彻底懵了。"
show celine sigh2 with dissolve
Celine "厨具那么多，名字又都稀奇古怪。我总不知道该从何下手！"
Marcel shock u "什么？真的吗？"
show celine annoyed2 with dissolve
Celine "是的，真的。怎么？你是在说我撒谎吗？"
Marcel shy u "哦，不！我怎么敢那样说。我只是……有点惊讶罢了。"
show celine frown2 with dissolve
Celine "有什么好惊讶的？"
Celine "我的笨拙，没有让你失望吧？"
Marcel shock u "不、不会，当然不会！我只是以为……唔……"
"我原以为塞琳远比我多才多艺，可连我都会下厨。母亲教过我几样简单的菜谱，我们常因闲来无事而一起烤馅饼。"
"那也是我们母女联络感情的一种方式。"
"我并非厨房里的好手。我曾多次把派皮烤焦、让糕点塌陷，不过大多数时候，我做出来的东西至少还能入口。"
"我从没想过竟有塞琳不会而我却会的事，不过也许是我这样想有失公允。"
"正像塞琳所说，烹饪和弹钢琴并不能相提并论。它们是截然不同的两种学问。"
Marcel ehe u "哦，没什么。我只是一时犯傻罢了。"
Marcel smile u "我琢磨着，对一位养尊处优的小姐来说，烹饪可不是什么必备的技艺。那种事自有下人操持。"
"我不知道塞琳家有多富有，但就我所了解的情况来看，他们听起来相当殷实。"
show celine sigh2 with dissolve
Celine "我父亲也是这么想的。他执意不许我踏进厨房。他怕我切着手、烫着自己，不愿我拿手去冒险。"
show celine frown2 with dissolve
Celine "你瞧，我从六岁起就开始弹琴了。"
Marcel shock u "天哪！弹了那么多年吗？难怪你如此出色！"
show celine neutral2 with dissolve
Celine "你眼下不过是在奉承我罢了。"
show celine sigh2 with dissolve
Celine "我想，如今我已不再受制于我父亲，若能学着亲手为自己下厨，或许也不错；不过我不愿妨碍阿梅莉。"
Celine "她是如此可靠，我也就没必要为家务琐事操心了。"
Marcel neutral u "你已提过好几次阿梅莉了，可我还不太清楚她是谁。她是你的姨妈吗？"
show celine smile2 with dissolve
Celine "哦，不是的，阿梅莉与我并无血缘——不过她早已是我家的一员，跟亲人也差不多啦！"
show celine neutral2 with dissolve
Celine "阿梅莉是我的女仆。"
Marcel "真的吗？我竟不知道你还有一位！"
"我原本就有些怀疑，可这下算是板上钉钉了：塞琳家真的{i}必定{/i}很富有。"
show celine sigh2 with dissolve
Celine "哦，也没什么好夸耀的。我身边只有一位女仆服侍。家族里当然还雇了别的女仆，只是她们都留在了奥尔良。随我来米耶讷的，就只有阿梅莉一人。"
show celine sad2 with dissolve
Celine "如今，就只剩我和阿梅莉了。"
"这么说来，塞琳家雇的不止一个女仆：他们雇了许多个。"
"我不禁好奇她父母住在什么样的宅邸里。我在脑海中勾勒出它的模样：一座辽阔连绵的庄园，摆满路易十八时期的家具，挂满金色的吊灯。"
"我和母亲无论如何也算不上穷，但我想塞琳家肯定把我们远远甩在了后头。"
show celine shock2 with dissolve
Celine "哎呀，你看起来好惊讶！玛塞尔，你父母在巴黎难道没雇女仆吗？"
Marcel neutral u "我们家是有位管家，但她并不与我们同住。她究竟做了多少事，我也不太清楚。"
Marcel "我母亲喜欢亲自操持大部分家务。她也没有太多别的事可打发时间。"
show celine frown2 with dissolve
Celine "我母亲就恰恰相反。她整天在奥尔良四处闲逛，拜访某某先生和某某夫人。"
show celine annoyed2 with dissolve
Celine "我们家时常受邀赴午宴、音乐会与舞会。这一切实在乏味透了，那里的人也无聊得要命！他们永远只谈论自己！"
show celine smile2 with dissolve
"塞琳说到这里顿住了，羞涩地笑了笑。"
Celine "不过，我想我现在对你做的也是同样的事。"
show celine sad2 with dissolve
Celine "抱歉，我一人霸占了整场谈话。你一定已经厌烦我了吧。"
Marcel shock u "哦——不，一点也不。我喜欢听你说话，也想多了解你！"
show celine neutral2 with dissolve
Celine "你太客气了。"
"塞琳在毯子上舒展身子，仰起头望着碧蓝的天空，任微风轻抚她的脸颊。"
show celine smile2 with dissolve
Celine "不过，我仍是感激的。能有别人——而不是那个讨厌的克洛蒂娜——偶尔说说话，{i}确实{/i}不错。"
Marcel neutral u "那阿梅莉呢？你与她相处得还好吗？"
show celine frown2 with dissolve
Celine "我不确定那是否算得上恰当的形容……"
Celine "自我记事起，阿梅莉就在我家做工了。她对我十分疼爱，也一直把我照料得很好，但我不会把她当作朋友。你看，她比我年长许多。"
show celine sigh2 with dissolve
Celine "做饭、打扫、洗衣，样样都是她张罗，可她还有空来念叨我！"
show celine neutral2 with dissolve
Celine "她是个相当了不起的女人，只是有点爱多管闲事。"
Marcel huh u "她念叨你？念叨些什么？"
show celine sigh2 with dissolve
Celine "多半是念叨我的胃口。她说我吃得不够，总没完没了地劝我多长点肉！"
show celine frown2 with dissolve
Celine "她也常打探我的私事。她很想知道，为什么我从不邀请任何同学到家里来。这当然不是出于我缺乏兴致。"
show celine sigh2 with dissolve
Celine "我知道克洛蒂娜会求之不得地想要窥伺我的家，要是她办得到的话……"
show celine frown2 with dissolve
Celine "但我宁可别让她那么得意。"
Celine "我的家只属于{i}我{/i}。那是我独享的栖身之所，与世隔绝，我没有义务让任何人踏入。"
show celine annoyed2 with dissolve
Celine "克洛蒂娜只会用她那贪婪的手与轻率的提问来玷污它。"
Marcel neutral u "那么看来，你以前从未邀请过任何人到家中了？"
show celine frown2 with dissolve
Celine "没有。我也不想，可阿梅莉总是为此唠叨个没完。"
show celine sad2 with dissolve
Celine "这宅子里就只有我们两个——我家的其他人仍住在奥尔良——她担心我或许会孤单。"
Marcel "{i}你{/i}会孤单吗？"
show celine neutral2 with dissolve
Celine "眼下不会。"
Celine "我已经很久没有可以倾诉的人了，不过……"
show celine smile2 with dissolve
Celine "我想，我或许能习惯拥有一个朋友。"

stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene sky3 g
with clockwipe
$ renpy.pause(0.5)
show overlay2
show message25 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message25
hide logo2
hide overlay2
with datetrans2

$ renpy.pause(0.3)
$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  9月28日{vspace=1}  渐暗的日子") )
scene sky3 with dissolve
play music "bgm/Mysterious.ogg" fadein 1.0
play ambience "sfx/wind.ogg" fadein 1.0
window show dissolve

"时间一如既往地流逝着。秋天继续向前，带来了凛冽的风，在夜里敲打着我的窗玻璃。"
"树上的叶子变得干枯，开始凋零。每天早晨，当我穿过校园走向教室时，都得踩过散落一地的红、棕、黄三色落叶。"
"在这段时间里，我与塞琳的友谊日渐深厚。"
"我们继续一起共进午餐，她跟我分享了一些她过去在奥尔良生活的点滴。"
"她谈起她的父母（“他们管得太严了！”）、她的姐姐们（“她们总把我当小孩宠！”），还有阿梅莉（“她人真的很好。要是她别那么唠唠叨叨就好了！”）。"
"有时候，她甚至会提起她以前的钢琴老师：那位神秘的瓦雷纳先生……"
"可是，每当塞琳提起这个话题，她便会陷入沉默与沉思，很快也就把这事岔开了。"
"我不知道塞琳和瓦雷纳先生之间发生过什么，但他们两人一定关系密切。听她的话音，她似乎很怀念他。"
"我想试着体谅她，可当我几乎不了解塞琳在奥尔良的过去时，这便很难做到。我从未见过她的父母，也没见过她的姐姐们，更从未见过瓦雷纳先生。"
"我想逗塞琳开心的努力，又因我瞒着她、压在心头那个秘密的分量而越发受挫。"
"正如她把过去的一些事瞒着我、不让我窥探一样，我也必须隐藏我的真实身份。"
"我不是玛塞尔·雷诺。我是马塞尔·德·圣雷米，那位有名的浪子乔治的独子——至少据我所知是独子。"
"然而，我在米延待得越久，就越发现自己渐渐淡忘了这一点。"
"我刚来米延时，曾想自己永远也无法习惯穿裙子、编辫子，或是被人称作「小姐」。对我这个一直把自己当成男孩的人来说，这简直不可想象，但这几周的经历让我改变了看法。"
"人真是出奇地善于适应。刚被抛进陌生的环境时，我们起初会惊慌失措，但规律的生活与熟悉感很快便让我们安定了下来。"
"如今我早晨穿裙子时，甚至不会再有所迟疑。我能毫不笨拙地把头发编成辫子，被人当作女学生称呼时也不会再三寻思。"
"就好像我真的已经变成了玛塞尔·雷诺一样。"
"在过去，我会说这样的转变绝无可能（人的身体哪能如此轻易地改变！），但这件事或许比我原先想的更为复杂微妙。"
"倘若一个人的身份并非由身体决定，而是由他自己的心境决定的呢？"
"倘若我愿意全心全意地成为玛塞尔，也许我真的就能变成她。那样的话，我就不必再为欺骗了塞琳而耿耿于怀。我们之间那道除了我自己谁都察觉不到的隐形屏障，也就能被消除，我也不必再感到那么别扭了。"
"尽管我觉得自己很向往那样，但有一个至关重要的事实始终未曾改变。我并不把自己看作女孩，也不希望别人这样看待我。"
"塞琳愿意让我做她的知心人，这令我受宠若惊，但我更想以我自己的身份来接下这个角色。"
"唯一的问题是，我到底是谁？"
"我也说不准。"
"我不觉得自己像『玛塞尔』，但也从不觉得自己像『马塞尔』。"
"正如姨妈所预言的那样，我在这群女学生当中，比在巴黎那所全男子学校里更能融入，但这并不意味着我自己就是个女孩。"
"时间越久，我对自己这处境就越感到困惑。"
"我和塞琳之间那道屏障依然存在，而我看不出有任何拆除它的办法。"

stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene yard g
with clockwipe
$ renpy.pause(0.5)
show overlay2
show message26 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message26
hide logo2
hide overlay2
with datetrans2

$ renpy.pause(0.3)

$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  10月1日{vspace=1}  完美绅士") )
play ambience "sfx/footsteps2.ogg" fadein 1.0
play music "bgm/Claudine.ogg" fadein 1.0
scene yard with dissolve
window show dissolve

"那是一个清爽的星期四下午，刚过正午，我和全班同学一起正走在前往音乐教室的路上。"
"我穿过庭院，在树丛间穿行。尽管空气已带凉意，红棕色的叶子仍紧附在盘曲的枝头，我不由得为它们的坚韧所打动。"
"大自然的确是一位令人敬畏的女族长。"

stop ambience fadeout 1.0
window hide dissolve
scene black with blinds2
$ renpy.pause(0.8)
scene cg19 with blinds2
window show dissolve

"我们到达音乐教室后，塞琳在钢琴前就座。与此同时，我们其余的女孩排成整齐的两排：高个子在后，矮个子在前。"
"布吕吉埃夫人让我们做一系列热身练习，似乎是要我们把嘴越张越大。"
"接着，等确认我们已经活动开了，她便让塞琳弹几个简单的音阶。这大约花了十来分钟，直到我们唱出一连串的「哆」「来」「咪」之后，这节课才算真正开始。"
"塞琳弹起一首缓慢、柔和的赞美诗，我们这些女孩奉命齐声合唱。"
"至少，本意是这样的，但教室里并非每个女孩都能胜任这一任务。"
"站在前排的米拉贝尔，看上去全然不知所措。"
"她努力模仿同伴的旋律，可她该低的时候声音却高，该高的时候声音又低，唱得一团糟，布吕吉埃小姐很快便叫她停下。"
"我自己也好不到哪儿去。自从第一堂（堪称灾难的）音乐课以来，我的唱功虽有了些许进步，可我还是唱不上去任何高音。"
"我怕若是硬要唱，嗓音会破音。"
"当我们把这几首赞美诗练过几遍之后，布吕吉埃夫人允许我们短暂休息。她说休息时可以交谈，但叮嘱我们压低声音。"
"可对布吕吉埃夫人来说不巧的是，克洛蒂娜压根不懂「节制」二字的意思。校长刚一转身背对我们，克洛蒂娜便立刻开始认真地说起话来。"

scene musicroom
show noemie neutral:
    xpos 0.70 ypos 0.5 xanchor 0.5 yanchor 0.5
show claudine smirk:
    xpos 0.30 ypos 0.5 xanchor 0.5 yanchor 0.5
with wipeleft_slow

Claudine "诺艾米，诺艾米！你绝对猜不到昨天我碰上了什么事！"
show noemie sigh with dissolve
Noémie "我猜我猜不到，不——其实我也并不怎么想知道。"
show claudine shock at bounce
Claudine "哎呀，别那么古板扫兴！这可是正经事！"
show noemie frown with dissolve
Noémie "克洛蒂娜，跟你有关的事{i}从来{/i}就没什么正经的。我看你对“正经”这个词过敏。"
Claudine "大多数情况下，你说得也许没错，可这回我的前程可系于此啊！不，是我的贞洁本身！"
Noémie "你的贞洁？"
"这至少似乎引起了诺艾米的兴趣。她皱起了眉头。"
Noémie "你在说什么啊？"
show claudine annoyed with dissolve
Claudine "哎呀，还不是那个可恶的杜普莱西先生！他竟然又一次向我求婚了！你能相信吗？！"
Noémie "什么？"
"诺艾米的眉头皱得更深了。"
Noémie "那个老家伙还在纠缠你，你上次不是已经把他彻底拒绝了吗？"
Claudine "是啊，就是！他就是不肯接受我的拒绝！"
show claudine neutral with dissolve
Claudine "他是父亲的助手，我每天都得见到他，这已经够尴尬的了。我明白他{i}不能{/i}不常来我家，可我{i}本{/i}指望他能把他对我那份愚蠢而荒谬的感情放下！"
Claudine "我已经拒绝过他一次了。这件事本该就此了结。他要真是个堂堂正正的大人，就该明白这个道理，可是{i}不{/i}！"
show claudine annoyed with dissolve
Claudine "他就像个任性的孩子，没完没了地纠缠这件事！他就是{i}不肯{/i}讲道理！"
show noemie mad with dissolve
Noémie "呃……"
"诺艾米做了个鬼脸。"
Noémie "你父亲或许是位古怪的人物，可我觉得杜普莱西先生更糟。哪个头脑清醒的女学生愿意嫁给一个年龄两倍于自己的男人？"
Claudine "他得是位真正英俊的男子，才能让我回心转意。或者，富可敌国也行。"
show claudine smile with dissolve
Claudine "比方说，若是乔治·德·圣雷米来求婚，我或许会为这份提议心动……"
Marcel shock u "啊……"
"有人提起我父亲的名字，让我猛地抬起头。我原本没料到米延的女学生会知道我父亲，但看来是我错了。他的名声（或者说恶名）想必比我预想的更广为人知。"
show claudine huh with dissolve
Claudine "嗯？"
"我的惊讶没能逃过克洛蒂娜的眼睛。我竭力把面部表情摆得更平静些，但她已经看见了——而且，果不其然，她紧抓不放。"

scene musicroom:
    size (1920, 1080) crop (0, 40, 1440, 810)
show claudine smile2:
    xpos 0.39 xanchor 0.5
with dissolve

Claudine "玛塞尔，你听说过乔治吗？"
Marcel sigh u "嗯，呃……听说过。"
"不幸的是。"
show claudine laugh2 with dissolve
Claudine "这样啊，我本该料到。你{i}毕竟{/i}住过巴黎。"
show claudine smile2 with dissolve
Claudine "你可曾看过他的演出？"
Marcel shy u "嗯——看过一两次。"
show claudine shock2 with dissolve
Claudine "看了两次，是吗？你这幸运儿！我只在舞台上看过他一次，那还是多年前的事了！"
show claudine smile2 with dissolve
Claudine "那你就说说嘛！你觉得乔治怎么样？"
"关于我父亲，我有很多想法，而其中几乎没有一句是赞美之词。"
"我觉得他是个自私、不负责任、毫无担当的男人，利用了我母亲年少时对他的感情，然后又将她抛弃……{w}但这话我不能告诉克洛蒂娜。那样我会把自己的底牌暴露太多。"
Marcel "这个，嗯……他算是……一位有才华的演员吧？我看他那场戏时，他演那个角色或许嫌老了点，不过他扮演的罗密欧倒相当出色。"
show claudine annoyed2 with dissolve
Claudine "哦？"
"克洛蒂娜噘起了嘴，看起来有些失望。"
Claudine "关于这件事，你就只有这么点话可说吗？"
Marcel huh u "我该说些别的什么吗？"
show claudine shock2 with dissolve
Claudine "如果你心里还有一丝热情，那当然就该说点别的！我可不是要你对乔治的演技做什么不偏不倚的分析！"
Marcel frown u "那你{i}到底{/i}想让我怎样？"
show claudine smile2 with dissolve
Claudine "哎呀，你这个傻丫头！"
"克洛蒂娜狡黠地笑了起来。"

stop music fadeout 1.0

Claudine "我想知道你觉他有多迷人！"

play music "bgm/Comedy.ogg" fadein 1.0

Marcel "呃……"
"我担心克洛蒂娜会问起这个，但对她的问题，我实在想不出合适的回答。"
"我该说什么才好？这可是在谈论我的父亲啊！"
"若要客观地看，我想我父亲{i}的确{/i}算得上英俊，属于那种风流不羁的俊俏样。尽管他深陷诸多丑闻，却能长盛不衰地受欢迎这么久，总是有原因的。"
"不过，我不能说自己对他的容貌有多在意，除了偶尔会咒骂他把那过分的身高遗传给了我。"
"我真希望自己能像母亲一样矮一些。那样的话，也许我就不会那么引人注目了。"
show claudine huh2 with dissolve
Claudine "玛塞尔？你怎么一声不吭的？"
"克洛蒂娜凝视着我，目光探究而又执着。"
show claudine neutral2 with dissolve
Claudine "别跟我说你觉得乔治不迷人！我敢肯定，世上没有哪个女人，无论{i}年轻{/i}还是年迈，能抵挡得住他！"
Claudine "就连在这类事上格外一根筋的诺艾米，也承认乔治很英俊！"

scene musicroom
show noemie sigh:
    xpos 0.70 ypos 0.5 xanchor 0.5 yanchor 0.5
show claudine neutral:
    xpos 0.30 ypos 0.5 xanchor 0.5 yanchor 0.5
with dissolve

Noémie "就他的年纪而言，他{i}确实{/i}算英俊，这我承认；可他的年纪也不是一下子就能忘掉的。克洛蒂娜，他已经四十多岁了。"
Claudine "那又怎样？怎么了？"
show noemie shock with dissolve
Noémie "你年纪还小，不该去仰慕这样一个男人吧？他都老得足以当你父亲了！"
show claudine smile with dissolve
Claudine "乔治{i}并没有{/i}比我父亲还老，多谢你提醒。我父亲成婚很晚，他都已经是个老头子了才有了我！"
show noemie frown with dissolve
Noémie "这也改变不了你们两人之间相差二十多岁的事实！"
Noémie "我以为你拒绝杜普莱西先生，是因为他比你年长许多，而他才不过三十岁！乔治又凭什么不一样？"
show claudine laugh with dissolve
Claudine "乔治之所以不同，是因为他不同于杜普莱西先生，他很迷人——而且他还是位演员！想必他一定非常富有！"
Claudine "我承认，近来关于他……那些癖好……的消息，确实让我心里有些不是滋味，可我相信，即便这般不快，也能被他的热吻冲刷得一干二净！"
Marcel sad u "……"
"光是想到我父亲会深情地亲吻某个人，就足以让我反胃，而若把那个面目模糊的「某人」换成我自己的同学，那更是令人作呕。"
"所幸，有这种感受的不止我一个。诺艾米也对克洛蒂娜的直白感到惊骇。"
show noemie mad with dissolve
Noémie "哦，看在上帝份上！你就{i}一点{/i}体统都没有吗？！"
Noémie "怎么，前不久你还嘲笑全班同学，说她们为那个想象中的音乐大师神魂颠倒呢！"
Noémie "我记得你说过，你永远不会蠢到去当某个老男人的床笫之欢吧？"
show claudine smirk with dissolve
Claudine "哎呀，你还不了解我吗，诺艾米。"
"克洛蒂娜吃吃地笑了起来。"
Claudine "为了一个富有而英俊的男人，我乐意抛弃一切顾忌！还有什么比这更值钱的？道德不能当饭吃——{i}也{/i}不能拿来拥抱啊！"
Noémie "呕。"
"诺艾米做出生病的样子。"
show noemie frown with dissolve
Noémie "你尽管随意幻想你中意的人，可别指望我会纵容你。我宁可{i}死{/i}，也不要让个这么老的人用他那双皱巴巴的手来碰我！"
show claudine smile with dissolve
Claudine "我敢肯定乔治的手没那么皱。他可是个文雅的绅士，不是那种粗俗的庄稼汉。"
show claudine laugh with dissolve
Claudine "玛塞尔，你觉得呢？"
Marcel shock u "我——我对这件事没有意见！"
show claudine shock with dissolve
Claudine "你的意思是，你从未想过被乔治那双白皙的手抚摸吗？"
Marcel embarrassed u "没有，我没想过；一次都没有！"
show claudine smirk with dissolve
Claudine "你嘴上这么说，可你的脸红了……"
Marcel shockblush u "哦——只是因为你太荒唐了！这种事不该如此毫无顾忌地谈论！"
show claudine shock with dissolve
Claudine "可我不能跟你们这些亲爱的同窗畅谈我少女的心事，那我{i}还能{/i}跟谁去说？杜普莱西先生吗？"
show claudine annoyed with dissolve
Claudine "我相信他{i}一定{/i}很乐意，可我就是受不了那男人！"
show claudine neutral with dissolve
"克洛蒂娜嘟起了嘴。"
Claudine "我本以为你能体谅我的心情，可巴黎的女孩子想必比我以为的要保守得多！"
show claudine annoyed with dissolve
Claudine "至于你，诺艾米……"
"克洛蒂娜向诺艾米投去一道尖刻的目光。"
Claudine "你{i}自己{/i}的心上人不过是个干活的苦力，你有什么资格抱怨乔治的手！我敢肯定，费利克斯的手比乔治的手远远粗糙得多！"
show noemie shock with dissolve
Noémie "我——我不明白这关费利克斯什么事！我以为我们谈的是你的眼光，不是我的！"
show claudine smile with dissolve
Claudine "那好，谈论你的眼光也没什么意义。我们都清楚你那眼光是怎样的，是不是，姑娘们？"
"克洛蒂娜用胳膊肘捅了捅我们一位同学的身体，那同学咯咯笑了起来。"

show image "border" onlayer border
scene musicroom:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

Cla "哦，是啊！要是他的名字以“F”打头——"
Claa "又以“X”结尾——"
Claaa "那诺艾米准会黏住他不放！"
Class "哈哈哈哈！"
"同学们爆发出一阵哄堂大笑——而这自然招来了布吕吉埃夫人一道锐利的怒视。"

hide image "border" onlayer border
scene musicroom
show al frown:
    xpos 0.70 xanchor 0.5
show claudine smile:
    xpos 0.30 xanchor 0.5
with wipeleft_slow

Bru "姑娘们！我不是叮嘱过你们要守规矩吗！"
show claudine shock at bounce
Claudine "我知道，夫人，我{i}非常{/i}抱歉。"
"克洛蒂娜可爱地眨了眨眼睛，她那深色的睫毛像公主的睫毛般颤动。虽然她是这群闹事者的罪魁祸首，她却竭力装作一副无辜的模样。她可真是没有半点羞耻心。"
Claudine "我并非存心要扰了秩序——真的，我不是故意的！您看，是玛塞尔问了我一个问题，我觉得有义务回答。"
show al annoyed with dissolve
Bru "一个问题？"
"布吕吉埃夫人抿紧了嘴唇。"
Bru "关于什么？"
show claudine smile with dissolve
Claudine "还能是什么，关于咱们学校的合唱团呀！她对我们辉煌的音乐史可感兴趣啦！对不对，玛塞尔？"
Marcel shy u "哦，嗯……"
"我挪了挪身子，感到颇为难堪。"
"克洛蒂娜的话不过是一番精心编排的谎话，可现在她把我也卷进了她的淘气里，我觉得还是应当附和。我可不想与她为敌。"
Marcel neutral u "是——是的，夫人。克洛蒂娜正在跟我说咱们合唱团的事……"
show al neutral with dissolve
Bru "是吗，她倒这么说了？"
"布吕吉埃夫人的眼睛眯了起来。虽然她没有明说，但我看得出，她并不相信我。"
show al annoyed with dissolve
Bru "那么，请问，谈论合唱团又何以让你们笑成那样？音乐有什么好笑的？"
show claudine laugh with dissolve
Claudine "夫人，我刚才是在给玛塞尔绘声绘色地重演勒梅尔小姐私奔那出戏。也许我该收敛些，可您是了解我的。我实在太爱这业余演戏了！"
show al sigh with dissolve
Bru "是啊，我对这点倒是清楚得很……"
"布吕吉埃小姐叹了口气。"
show al annoyed with dissolve
Bru "唉，很抱歉要告诉你这件事，玛塞尔，合唱团已经解散了。没有一位好音乐老师来管住大家，实在没法再办下去。"
show claudine sad with dissolve
Claudine "是的，我知道。这是件令我每天都要扼腕叹息的事。在合唱团唱歌可真是件乐事！"
Cla "我也很想念呢！我们那时玩得可真开心！"
Claa "我们过去常在圣诞节和复活节期间到当地的教堂举办音乐会，对吧？总是特别有趣！"
Claaa "我一直梦想着用我高亢的咏叹调迷住玻璃厂里的某个男人，可还没等到机会，合唱团就解散了！"
show claudine shock with dissolve
Claudine "我知道，我知道。真是太遗憾了！没有了合唱团，总觉得我们学校少了至关重要的一部分！"
show claudine sad with dissolve
Claudine "可怜的玛塞尔却从没能有机会体验一番，这实在{i}太{/i}不公平了！我想她在圣诞庆典上到教堂唱歌一定会很开心的！"
"我可不会乐意做这种事。我唱歌糟透了。我连调都找不准，连水桶里都哼不出个调子，更别说是浴缸了……{w}但我决定保持沉默。"
"沉默，正如我所发现的那样，是应对克洛蒂娜最容易的办法。"
Bru "并非只有你一人希望合唱团能重现昔日的光彩，克洛蒂娜。我也认为，年轻女孩的生命中需要一种健康的音乐滋养。"
Bru "我们的音乐会一直很受欢迎，也给米延的百姓带来了许多欢乐……"
show al sigh with dissolve
Bru "但勒梅尔小姐走了，我也做不了太多。"
show claudine neutral with dissolve
Claudine "您总可以聘请一位新的音乐老师吧，夫人？"

show image "border" onlayer border
scene musicroom:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

Cla "一个年轻英俊的男人，眼神凝重，灵魂饱经沧桑！"
Claa "哦，那太好了！米延的男人根本不够分！"
Claaa "自从特蕾莎把费利克斯抢走以后，我一直失落极了！一位新的音乐老师正是我们需要的！"
Cla "要是好声好气地请求，说不定他会教我怎么弹钢琴呢！"
Claa "哦，没错！他可以握着我的手，在这琴键上游走……"
Claaa "然后在我耳边低语绵绵情话！"
Celine sigh "你们这些女孩子……"
"塞琳皱了皱眉头。"
Celine "你们以为音乐课是什么？可不是让你们调情的借口。"
Cla "那是自然！除非那位音乐老师是{i}你{/i}的话，塞琳！"
Claa "不过，要是你是个男人……"
Claaa "要是你是个严厉、严肃又心思细腻的男人……！"
"同学们之间又爆发出一阵窃笑，而布吕吉埃夫人则叹了口气。"

hide image "border" onlayer border
scene musicroom
show al sigh:
    xpos 0.70 xanchor 0.5
show claudine smile:
    xpos 0.30 xanchor 0.5
with wipeleft_slow

Bru "够了，姑娘们。你们不会得到新的音乐老师，这事就这么定了。"
Bru "好了，你们已经闲站着太久了！"
"布吕吉埃夫人利落地拍了拍手。"
Bru "我想你们该重新开始上课了。塞琳！"
Celine huh "是，夫人？"
Bru "我们接下来唱{i}Love Divine{/i}。你准备好了就开始吧。"
Celine "是，夫人！"
show claudine annoyed with dissolve
"塞琳转回钢琴前，一如既往地尽职尽责。与此同时，克洛蒂娜则低声抱怨。"
Claudine "我不知道你怎么想，玛塞尔，但我今天关于爱情的已经听够了。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
play ambience "sfx/birds.ogg" fadein 1.0
play music "bgm/Classroom.ogg" fadein 1.0
scene sky with wiperight_slow
$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  10月1日{vspace=1}  塞琳的主意") )
window show dissolve

"这一天在缓慢而如梦似幻的氛围中悄然流逝，正如在这田园牧歌式的乡村里经常发生的那样。"
"教堂的钟声终于为今天最后一堂课画上了句号，同学们从椅子上站起身，打着哈欠。"
"得到布吕吉埃夫人的允许后，女孩们一个接一个地走出教室，如流水般源源不断。"
"透过教室窗户照射进来的微弱秋阳，落在她们编成的发辫上。大约六七颗颜色各异的头颅——赤褐、赭红与乌黑——闪着光泽。"
"我看着同学们离去，克洛蒂娜也在其中。我觉得有些疲惫，不愿加入她们热烈的交谈——不过，即便我不累，恐怕也插不进一句话。"
"我的大多数同学（事实上，是其中压倒性的多数）一辈子都住在米延。"
"她们知道村里每个人的名字，知道谁刚刚向谁求了婚，知道谁最近去了巴黎游玩，还有，哦！各种各样的琐事。"
"有时候，当我偷听同学们说话时（我实在忍不住，因为她们实在太吵了），我不禁怀疑她们是否知道这里发生的所有事情。"
"而另一方面，我住到米延来，只不过几个星期而已。"
"我想，我待的时间比我自己预想的要长，可关于米延，仍有许多我尚不了解的地方。"
"我知道这样很傻，但我还是忍不住感到惆怅。"
"我每天都在面对自己格格不入的证据，虽然我正努力融入，可我觉得自己还需要更多时间。不过，我不知道自己还能腾出多少时间来，因为我只会在米延待上一年。"
"我的同学们，会有接纳我的那一天吗？"
"蓦地，我感到了几分迷惘。"
"当同学们脚步声渐渐远去，我站起身来，正打算离开——可就在这时，我又停了下来。"
"原来，我并没有自己以为的那样孤单。"

stop ambience fadeout 1.0
scene classroom:
    size (1920, 1080) crop (250, 40, 1440, 810)
show celine frown2:
    xpos 0.70 xanchor 0.5 ypos 0.55 yanchor 0.5
with wipedown_slow

"塞琳仍坐在我身边，双腿交叠着。她的眼睛半垂着，目光有些涣散，看起来像是正专注地想着什么。"
"她实在太安静了，以致我没有注意到她。我以为她一定已经走了，可显然并非如此。"
"我不知道她在想什么呢……？"
Marcel huh u "塞琳？"
show celine huh2 with dissolve
Celine "哦……玛塞尔。"
show celine frown2 with dissolve
Celine "我没注意到你在这儿。"
Marcel neutral u "我也可以这么说你。你一整天都很安静。"
show celine sigh2 with dissolve
Celine "跟克洛蒂娜比起来，我向来都是安静的。她那张嘴呀，能说个没完没了！"
Marcel laugh u "我觉得跟她比起来，谁都是安静的。"
show celine neutral2 with dissolve
Celine "哈。嗯，你说得没错。"
"克洛蒂娜根本不在场（她和诺艾米跑到别处去了），可她仍然主导着我们的谈话。"
"主导局面似乎确实是克洛蒂娜惯用的行事作风。她说出那么多惊世骇俗的话，让人想不注意她都难。"
show celine sigh2 with dissolve
Celine "好啦，暂且把克洛蒂娜放一边吧。除非有必要，我宁愿不多想她。"
Marcel smile u "为了图个神智清明，这倒不失为一条好规矩。"
show celine neutral2 with dissolve
Celine "嗯，{i}那些{/i}才是值得奉行的至理名言。"
"塞琳微微一笑，尽管笑意很淡，我却也不由自主地回以微笑。"
"也许在班上我确实是那个格格不入的人，原因远不止我作为外来者的身份，可只要和塞琳在一起，我便不那么感到迷惘了。"
"虽然我其他的同学似乎觉得她难以亲近，我却认为她颇为和善。"
show celine huh2 with dissolve
Celine "那我们走吧？"
Marcel smile u "好。"
play sound "sfx/chair.ogg"
"塞琳把一缕黑发拢到耳后，随即站起身来。"

play ambience2 "sfx/footsteps3.ogg" fadein 0.5
show celine huh2:
    ease 0.6 ypos 0.5

$ renpy.pause(0.6)

show celine:
    xzoom -1
with dissolve

$ renpy.pause(0.4)

show celine:
    ease 1.0 xpos 1.10

$ renpy.pause(0.4)

stop ambience2 fadeout 0.5
play sound "sfx/door.ogg"
$ renpy.pause(0.3)
play ambience "sfx/footsteps2.ogg" fadein 0.5

scene yard
show celine frown:
    xzoom -1 xpos -1.10 xanchor 0.5 ypos 0.53 yanchor 0.5
    ease 3.5 xpos 0.5
with wiperight_slow

"我们一起走出教室，迈入校园。"

stop ambience fadeout 1.0

"头顶的天空一片明蓝，却有一丝微风。这阵风拂动树叶，让它们簌簌颤动：斑驳的红与黄交织成一片。"
"几片叶子脱离枝头，在空中飘浮翻飞。我看着它们如蝴蝶般轻盈地掠过，宽阔而平展。"
Marcel smile u "今天天气不错。"
show celine neutral with dissolve
Celine "我同意。"
show celine frown with dissolve
Celine "城里的秋天往往相当阴郁。大约就是这时候，天黑得更早，天空灰蒙蒙的。"
Celine "我住的那条街上没有树，所以我从没见过树叶像这样在地上堆起来。"
show celine sigh with dissolve
Celine "那实在是相当压抑……"
show celine neutral with dissolve
Celine "但这里就明亮多了。"
show celine frown with dissolve
Celine "这是我喜欢这里的原因之一。将来回家的时候，我甚至也许会想念这里。"
Marcel huh u "你不把米延当成自己的家吗？"
show celine sigh with dissolve
Celine "不太算。来这里不是我的选择。我是被送来的——更像被放逐——因为我父亲……"
"塞琳的声音渐渐低了下去，一如她每每触及自己过往时那样。她摇了摇头。"
show celine sad with dissolve
Celine "算了，不提了。"
show celine frown with dissolve
Celine "这听起来或许有些唐突，但其实有一件事我想和你商量。"
Marcel neutral u "什么事？"
Celine "有个想法我已经想了很久，但一直拿不准该不该下定决心去做。"
show celine sigh with dissolve
Celine "如果我决定把这个想法付诸实践，那会是一份相当沉重的责任。我不确定自己有没有足够的时间……"
show celine sad with dissolve
"塞琳皱了皱眉头。"
Celine "不，这不是真的。我在找借口，而且恐怕还都不是什么好借口。"
Celine "我的空闲时间太多了。离家这么远，在这里除了弹钢琴，几乎没什么可做的事。"
Celine "因为无所事事，我每天晚上都独自练琴，可我确实在想，是不是该把精力用到更有意义的事情上。"
show celine frown with dissolve
Celine "我想用我那点微薄的才能去帮助别人。我也希望能让他感到骄傲……"
show celine sad with dissolve
Celine "但我以前从没做过这种事。一想到会失败，就觉得有点害怕。"
Marcel neutral u "嗯？"
"我不解地看着塞琳。"
"我不想在她独白时打断她（她看起来像是在复杂的、矛盾的情绪中挣扎），可我却感到说不出的困惑。"
Marcel "你在说什么啊？"
show celine shock with dissolve
Celine "哦！我没说过吗？"
Marcel ehe u "没有，你没说过。"
show celine ehe with dissolve
Celine "啊……啊哈哈……"
"塞琳腼腆地笑了起来。"
show celine neutral with dissolve
Celine "抱歉。我太沉浸在自己的思绪里了，想必是忘了。我会说得清楚一些。"
show celine huh with dissolve
Celine "我其实是在想学校的合唱团。"
Marcel huh u "合唱团？"
show celine neutral with dissolve
Celine "是的。勒梅尔小姐还在这里任教的时候，我是其中一员。我们班和中年级班的女生大多都加入了。我记得总共有三十名成员。"
Marcel "三十人？"
"我吹了声口哨，心生赞叹。"
Marcel "那几乎是全校学生的一半了！"
show celine huh with dissolve
Celine "这{i}确实{/i}很了不起，对吧？合唱团很受欢迎，不过这也在意料之中。"
Celine "米延是个漂亮的地方，但实在没什么事可做。合唱团让我们这些女孩有事可忙。彼此之间都有一种同袍情谊。"
show celine neutral with dissolve
Celine "刚来这里的时候，我担心自己永远无法融入，但合唱团帮了我。它让我和同学们走得更近了——甚至包括克洛蒂娜！"
show celine frown with dissolve
Celine "当然，并非所有女孩都能参加。有些人要忙着做家务，或者照看弟弟妹妹。"
show celine sigh with dissolve
Celine "还有一些女孩完全是五音不全，就像可怜的米拉贝尔。她们也就远离了合唱团。"
Marcel ehe u "哦，是啊。米拉贝尔的歌声确实还有待提高……"
"尽管问题重重，她仍努力开口歌唱，这确实令人钦佩，但我（私下里）认为她最好还是别费这份力气。"
"我觉得米拉贝尔就算去攀登马特洪峰，恐怕也比找到调子来得更容易。她的嗓音不是太低就是太高，而且怎么也跟不上节拍。"
"就算是我这样没有受过音乐训练的人，也能听出她的声音：苍白、迷失、孤零零的，在所有人的嗓音下方飘忽颤抖。"
"我觉得自己唱得恐怕都比她好，而我连那些高音的一半都唱不上去。"
"至少我能（大致上）踩在节拍上。"
"把米拉贝尔排除出合唱团，大概是勒梅尔小姐一个明智的决定（不，{i}绝对{/i}是明智的决定），但这确实让我心生疑惑。"
Marcel sad u "我希望她没有太觉得自己被冷落……"
show celine sad with dissolve
Celine "她或许有这种感觉，但无论如何她也无法参加学校合唱团；即便她是下一个伊薇特·吉贝尔。"
Celine "她父母在村里开了一家面包店。米拉贝尔帮他们揉面、整形。她太忙了，根本没空唱歌……"
show celine sigh with dissolve
Celine "而且，从她连简单的数学都学不会来看，她也忙得没空复习功课。"
Marcel sigh u "啊……我明白了。"
"我从未听说过米拉贝尔的这些事。"
"事实上，由于她太害羞，我对她几乎一无所知。我想我从未和她好好说过话。每当我们目光相遇，她总是脸红着移开视线。"
Marcel neutral u "那么，我们班上有哪些同学参加过合唱团？"
show celine frown with dissolve
Celine "大部分人。克洛蒂娜当然在列——勒梅尔小姐说她有一副天使般的歌喉！——还有诺艾米，尽管她唱得并不特别好。"
Celine "然后就是茹贝尔双胞胎，还有海伦和伊莎贝尔……"
Marcel huh u "那露丝呢？"
show celine huh with dissolve
Celine "不，她没有参加。"
Marcel "真的吗？可我本以为她唱得很好。"
show celine frown with dissolve
Celine "她确实唱得好，但她不太愿意和别人打交道。勒梅尔小姐试着劝过她，可她拒绝了。"
show celine sigh with dissolve
Celine "她倔强得要命！"
Marcel ehe u "我确实留意到了。"
"露丝是另一位我几乎没说过几句话的同学。不过，她不会像米拉贝尔那样脸红、结巴、舌头打结。"
"我觉得露丝并不是害羞。她也许是别扭，又或者，是毫无兴趣？"
"有几次我尝试（徒劳地）主动攀谈，露丝却径直看穿了我，仿佛我是什么幽灵一般。"
"我曾猜想她是不是觉得自己高高在上，不屑于和我说话，可这或许是个不公平的评判。我不该去评判一个自己几乎不认识的人——不过，如果露丝继续这样冷淡下去，我恐怕永远也别想更了解她了。"
"也许我已经错过了加深我们关系的机会。"
Marcel neutral u "那么，你们合唱团平时做些什么？什么时候排练？"
show celine frown with dissolve
Celine "我们通常在周三和周五放学后的下午排练。"
Celine "勒梅尔小姐负责管理，她是个很随和的人——跟布吕吉埃夫人截然不同——所以她不在意我们闲聊。"
show celine neutral with dissolve
Celine "有时候我们甚至打打牌、掷掷骰子。"
Celine "我们会挤在音乐教室里，尽管地方不大，却非常温馨。"
show celine ehe with dissolve
Celine "我们大概没有像本该那样勤加排练……"
show celine neutral with dissolve
Celine "不过去年圣诞节音乐会筹备期间，我们倒是相当用功。"
show celine smile with dissolve
Celine "我们收起纸牌和骰子，整个十二月每天放学后都练习我们的歌。"
Celine "有时候我们一练就是两个小时，甚至三个小时！"
Marcel shock u "你们一连唱了{i}三{/i}个小时？！"
"我连连续唱上五分钟都极为困难。我无法想象要唱那么久！"
Marcel "你们不累吗？"
show celine neutral with dissolve
Celine "确实有点累，但也很有成就感。"
Celine "我从中获得的乐趣超出了自己的预料。勒梅尔小姐是那样一位和蔼可亲的人，很难不喜欢她。"
show celine smile with dissolve
Celine "我想，到最后我们都这么努力，是因为想让她感到骄傲。她总有办法把人性中最美好的一面激发出来，尽管她从不用威胁或惩罚来吓唬人。"
show celine huh with dissolve
Celine "她比我们大不了多少。我想她二十出头；也许二十二？二十三？"
show celine neutral with dissolve
Celine "从这个意义上说，与其说她是老师，不如说更像一位姐姐……或者也许是一位朋友。"
"塞琳深情地微微一笑。"
show celine smile with dissolve
Celine "在合唱团度过的时光对我来说非常珍贵。我在米延最美好的回忆都是在那里留下的。"
show celine shock with dissolve
Celine "听说勒梅尔小姐私奔了——还是跟一位政客——我大吃一惊！"
Marcel neutral u "我听人说过这些传闻，但不知道确切细节。这个男人到底是谁？"
show celine frown with dissolve
Celine "我想他的名字是……拉夸先生，也许是？他到我们学校来过几次，进行视察。"
show celine huh with dissolve
Celine "他曾是——也许现在还是？——教育部长。布吕吉埃夫人总让我们在他来访之前表现得规规矩矩，因为他想确保我们都开心、健康、守规矩。"
show celine frown with dissolve
Celine "就部长而言，我觉得他年纪不算太大。其实他长得相当英俊，金发碧眼……"
show celine sigh with dissolve
Celine "事实上，我记得克洛蒂娜以前还跟他调过情。"
Marcel ehe u "我可以想象……"
"在听到克洛蒂娜说过的关于我父亲的一切之后，这似乎与她的性格完全吻合。"
"对于一所像这样偏僻乡村学校的女生来说，她也太过放荡了吧。"
"我真想知道，她那些放荡的话都是从哪儿学来的？总该有人教过她吧？"
show celine frown with dissolve
Celine "不过，克洛蒂娜费尽心机却毫无收获。拉夸先生对她并不感兴趣……"
show celine sigh with dissolve
Celine "但他却对勒梅尔小姐颇为倾心。"
show celine frown with dissolve
Celine "我听说这两人暗中交往了相当长的一段时间，一直没被发现。他们互通各种思念缠绵的情书，最终两个人的感情再也无法克制。"
Celine "当拉夸先生最后一次视察结束后离开米延时，勒梅尔小姐也跟着他走了。"
show celine huh with dissolve
Celine "这一切真是太戏剧化了，简直像爱情小说里似的！好几周里人们都在谈论这件事，直到你到来！"
Marcel smile u "我很难责怪他们。我怀疑米延很少发生私奔这种事。"
show celine shock with dissolve
Celine "不，确实几乎从没有过。这事可掀起了轩然大波！"
show celine sigh with dissolve
Celine "如果勒梅尔小姐现在很幸福，我想我替她也高兴。米延地方太小，沉闷又乏味，我不会怪她想离开。"
Celine "要是我也能走，我也会离开的……"
show celine sad with dissolve
Celine "但我希望她能事先给我们一点提示。她走得那么突然，布吕吉埃夫人来不及找一位替代的音乐老师。"
Celine "没有勒梅尔小姐，学校合唱团根本没法维持下去。布吕吉埃夫人把它解散了，从此我们便一直无所适从。"
Celine "如今距我们像过去那样一同歌唱，已经过去了好几个月。我们跟布吕吉埃夫人上的音乐课根本就算不上数，她与勒梅尔小姐实在相去甚远。"
Celine "我告诉自己，虽说可惜，我也只能就此接受了……"
show celine sigh with dissolve
Celine "可我也一直在想，事情是否真的只能如此。"
"塞琳朝院子里扫了一眼。又有几片叶子被微风吹拂着，翻滚而过。"
show celine frown with dissolve
Celine "我的钢琴弹得还算不错。我受过充分的训练。"
show celine huh with dissolve
Celine "我或许算不上是老师，但若我主动站出来，我想我是能带领学校合唱团的。"
show celine frown with dissolve
Celine "我很喜欢与合唱团共度的那些时光，而且听了今天早些时候同学们的谈话，我想他们也一样喜欢。"
show celine huh with dissolve
Celine "我情愿相信，倘若我决定重建学校合唱团，他们是会支持我的。"
show celine frown with dissolve
Celine "我想这么做。我不介意承担这份额外的责任。我想延续勒梅尔小姐的遗志。"
Celine "我想，只要我们俩齐心协力，就一定能够做到。"
show celine neutral with dissolve
Celine "玛塞尔，你觉得呢？"
"塞琳转过身来面向我，唇边漾着一抹微笑。"
Celine "你愿意帮我管理学校的合唱团吗？"
"在此之前，我一直几乎完全赞同地朝塞琳的话点头，可她最后这个问题却让我猝不及防。"
Marcel shock u "什么……？"
"我知道自己的表情称不上最优雅得体，可我实在太过震惊（甚至可以说是惊呆了），以至于这似乎也无所谓了。"
Marcel "为、为什么你需要我帮忙？！"
show celine huh with dissolve
Celine "我倒不是{i}需要{/i}，只是觉得这样会省事些。比起独自苦苦支撑，我更愿意和一位朋友一起打理合唱团。"
show celine shy with dissolve
Celine "我知道这可能看不出来，但我的自信心有些问题。我尽量表现得镇定从容，可内心里，我却总在怀疑自己。光是鼓起勇气说出我这个想法，就花了我好几个月。"
Celine "我害怕失败。我不想显得愚蠢……"
show celine huh with dissolve
Celine "但若你肯陪我一起，我就不会那么害怕了。我们可以共同分担这副担子。"
Celine "你愿意与我共事吗？这对我意义重大，而且我觉得你将会是合唱团的一份宝贵财富。"
Marcel "你、你究竟怎么会这么想？"
show celine at bounce
Celine "这还用得着说吗！你可是从巴黎来的！你一定受过某种正规的音乐教育，不像是其他女孩子那样！"
show celine neutral with dissolve
Celine "我敢肯定你有许多知识可以传授给我们的同学们！你可以帮我教他们。你也知道，我一向不擅长于讲解事情。"
show celine smile with dissolve
Celine "我可以弹钢琴，你可以当老师！那会是如何美妙的合作啊！"
Marcel shy u "这、这听起来确实很美好，理论上说是这样，可……"
Marcel sad u "老实说，就音乐而言，我只是个门外汉。我从未受过任何这方面的正式教育。我甚至连乐谱都看不懂！"
show celine shock with dissolve
Celine "什么？可怎么会这样？"
show celine frown with dissolve
"塞琳的眼睛眯了起来。"
Celine "你{i}明明{/i}在巴黎上过学，难道不是吗？"
Marcel "是上过，但那所学校并不太重视艺术。它更侧重于历史、数学……诸如此类的科目。"
show celine sigh with dissolve
Celine "哎呀，这可真是闻所未闻。"
Celine "要是你连{i}一点{/i}时间都没花在音乐上，那这所学校也真不怎么样！你的教育竟如此贫乏，我都几乎要同情你了！"
Marcel sigh u "我并不是特别喜欢原来的学校，实在不……"
"不过那并非因为这里缺少音乐课。真正让我心力交瘁的，是那无休无止的戏弄与说教。"
show celine frown with dissolve
Celine "啧、啧。这可不行！"
Celine "我原本在你身上寄托了很大的希望。我还一直笃定你会答应的呢！"
Marcel neutral u "相信我，若我有那才能帮到你，我定会答应。可如今的我，实在看不出自己能派上什么用场。"
Marcel "或许你去找克洛蒂娜更好，如果她唱歌真如你所说那般出色……"
show celine annoyed with dissolve
Celine "找克洛蒂娜？我宁愿用缝衣针戳进自己的眼睛！"
Celine "诚然，她并非一无是处，可她对{i}任何事{/i}都从不认真。她不会懂我对音乐的热爱。她浑身上下没有一丝感性、多情的骨头！"
show celine huh with dissolve
Celine "我宁肯、宁肯与你一同去开启这件事。"
Marcel shy u "听你这么说我很高兴，可我只怕会让你失望……"
show celine frown with dissolve
Celine "那很容易补救！"
"塞琳双手叉腰。她忽然显得斗志昂扬：眼中闪烁着坚定的光芒。"
"我不确定自己是否喜欢她那样的神情。它似乎只预示着麻烦。"
Celine "你说过，若你有那个条件就会帮我，难道不是吗？"
Marcel neutral u "我是说过，可——"
show celine huh with dissolve
Celine "那么我们的行动方案就很明确了。我必须先给你创造条件，好让你能用来帮我！"
show celine smile with dissolve
Celine "我会把你需要知道的一切都教给你。我敢肯定，在我的指点下，用不了一个月你就能看懂乐谱——甚至还能弹起钢琴来！"
Marcel shock u "一、一个月？是不是有点太快了？"
show celine frown with dissolve
Celine "哦，玛塞尔。"
"塞琳咂了咂舌。"
Celine "你若老是抱着这种阴暗消沉的态度，那{i}无论{/i}多久的时间都不够用。你得比这更乐观一点儿才行！"
show celine huh with dissolve
Celine "至少我相信你能掌握那些基础——而你就得在十月到十一月之间的某个时候把它们掌握住。"
show celine neutral with dissolve
Celine "这样我们正好能腾出时间来重建学校合唱团，好让我们得以举办一年一度的圣诞音乐会。"
show celine smile with dissolve
Celine "我觉得这主意棒极了！"
Marcel sigh u "也许你是这么想，可我自己拿不准。我看得出你对这件事满腔热忱，可——"
show celine frown with dissolve
Celine "是的，我{i}确实{/i}热忱满腔。"
Celine "我相信我能做到，但仅凭我自己的意志力，或许还不足以支撑下去。你也必须相信这项事业。"
show celine neutral with dissolve
Celine "你是我的朋友，我希望我们一同做成这件事。"
Celine "我刚来到米延时，是合唱团帮了我。如今，我希望它也能帮到你。"
show celine huh with dissolve
Celine "玛塞尔，我这么做既是为了你，也是为了我自己，所以拜托了。你就迁就我一下，好不好？"
Marcel huh u "我……"
"我张开嘴。然后又闭上了。"
show celine frown with dissolve
"塞琳的目光沉静而澄澈，仿佛能将人整个包裹其中，我却无法让自己去迎上它。"
"我不想变得悲观（谁愿意呢？），可我从很小的时候起就被教养得习惯了往最坏处想。"
"我已经习惯了计划落空、事情不尽如人意，这都是拜我那反复无常的父亲所赐；他似乎总是永远无法，至少往往如此，遵守诺言。"
"我几乎觉得，与其怀抱最好希望，不如预料最坏结果。这样一来，当事情出了差错时，便更难感到失望了。"
"我对自己没有太多信心——可塞琳似乎显然有，而我不想辜负她。"
"我珍视与她的相伴，也想成为她的好朋友。"
"我在乎她……"
"于是，伴随着一声轻叹，我最终还是让步了。"
Marcel sigh u "哦，好吧。如果你需要我的帮忙，那我就试试，尽管我不敢保证能成功。"
Marcel smile u "不过，我觉得咱们俩一起把学校合唱团重建起来，倒也挺好的。"
show celine huh with dissolve
Celine "玛塞尔……！"
"塞琳瞪大了眼睛。她凝视着我，睫毛微微颤动……"
show celine smile with dissolve
"随即，一抹比我此前所见过的任何笑容都更为灿烂的微笑，绽放在了她的唇畔。"
"她的笑容那样舒展、那样诚挚，简直光彩照人。"
"我还是有几缕挥之不去的疑虑，但她的笑容让我最沉重的担忧得到了些许缓解。"
"能让塞琳显得如此快乐，我做的想必是对的。"
"我只能祈祷自己不要辜负她。"

stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene sky g
with clockwipe
$ renpy.pause(0.5)
show overlay2
show message27 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message27
hide logo2
hide overlay2
with datetrans2

$ renpy.pause(0.3)

$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  10月2日{vspace=1}  第一堂钢琴课") )
play ambience "sfx/birds.ogg" fadein 1.0
play music "bgm/Celine.ogg" fadein 1.0
scene sky with dissolve
window show dissolve

"第二天如往日一般过去，只有一个明显的例外。"
"当远处教堂的钟声响起，宣告一天的课程结束时，我没有回到我那间逼仄的卧室——那里曾是勒梅尔小姐的住处。"
"取而代之的是，我被一位颇为执拗的塞琳领往了音乐教室。"

stop ambience fadeout 1.0
scene yard
show celine smile:
    xzoom -1 xpos 0.5 xanchor 0.5 ypos 0.53 yanchor 0.5
with wipedown_slow

Celine "玛塞尔，这就是你课程的开端了！"
"在我们穿过校园时，塞琳一路对我絮絮地说着话。"
show celine neutral with dissolve
Celine "我猜想最初会很困难——学一门新学问时总是如此——但我相信你很快就能上手。"
show celine smile with dissolve
Celine "若是以你在课堂上的表现来看，你是个聪明的女孩。我完全相信你能做到！"
Marcel shy u "那要是我做不到呢？"
"我落在塞琳身后，脚步拖沓。我的腿比塞琳的更长，若我愿意，本可以超过她，但我心里太过犹豫，不敢贸然冲到前面去。"
"我以前对音乐一无所知。乐谱对我来说，就如同古希腊文一样难以理解——若非要说，恐怕还更甚。"
"我在以前的学校不得不研读《{i}伊利亚特{/i}》的原文本，还能背诵出其中若干段落，可音乐于我而言，却完全是未知的领域。"
"我怀疑自己那点粗浅的荷马知识在这里派不上多大用场。"
"我实在手足无措。"
Marcel sad u "万一无论你怎么设法教我，我都掌握不了那些基础呢？我真不愿白白浪费你的时间。"
show celine huh with dissolve
Celine "你这么说真贴心，不过不必担心。我对你有信心，所以也请你试着对自己多一点信心。"
Marcel "可万一——"

play sound "sfx/rustle.ogg"
scene yard:
    size (1920, 1080) crop (220, 80, 1440, 810)
show celine frown2:
    xzoom -1 xpos 0.5 xanchor 0.5
with dissolve

Celine "啊，啊，啊。"
"塞琳伸出一根手指，按在我的唇上。"
show celine sad2 with dissolve
Celine "人很容易沉溺于种种假想的情形之中，但那几乎从无益处。"
show celine frown2 with dissolve
Celine "你得学会更积极一些。"
show celine huh2 with dissolve
Celine "况且……"
show celine frown2 with dissolve
Celine "即便你在弹钢琴上遇到困难，我也不会生你的气。"
Celine "你只需尽力而为。只要你能做到这一点，就不会让我失望：我向你保证。"
show celine neutral2 with dissolve
Celine "那么，我们动身吧？一到日落，教室就全都上了锁，我们没多少时间练习。"
Celine "机不可失，时不再来！"
Marcel shy u "好、好的。我会，呃……我会尽力而为。"

play ambience "sfx/footsteps2.ogg" fadein 0.5
show celine:
    ease 2.0 xpos 1.20

$ renpy.pause(1.2)

stop ambience fadeout 0.2
play sound "sfx/door.ogg"

$ renpy.pause(0.5)

play ambience2 "sfx/footsteps3.ogg" fadein 0.5
scene musicroom
show celine frown:
    xzoom -1 xpos -1.10 xanchor 0.5 ypos 0.53 yanchor 0.5
    ease 3.0 xpos 0.50
with wiperight_slow
$ renpy.pause(1.2)
stop ambience2 fadeout 0.5

"我和塞琳走进音乐教室。"
"我之前来过这间屋子好几次，却从未在一天中这么晚的时候进来过。"
"教室里空无一人，也因此更显冷清；只有那架钢琴独自占据着视线。"
"没有同学们来填满这间屋子、彼此兴奋地叽叽喳喳，我周围的一切当真显得十分单调乏味。"

show celine neutral:
    xzoom 1
with dissolve

Celine "走吧，玛塞尔！"

scene musicroom:
    size (1920, 1080) crop (100, 0, 1440, 810)
show celine neutral2:
    xpos 0.50 xanchor 0.5 ypos 0.5 yanchor 0.5
    ease 0.8 ypos 0.55
with dissolve

"塞琳在钢琴前坐了下来。"
Celine "坐到我身边来。我会把一切都讲给你听。"
"塞琳拍了拍琴凳上她身旁的空位。既然没有别的地方可坐，我便依了她。"
"我穿过那间显得比平日更宽敞的屋子，在塞琳身边坐下。"

scene musicroom blur:
    size (1920, 1080) crop (250, 60, 1152, 648)
show celine neutral3:
    ypos 0.55 yanchor 0.5 xpos 0.5 xanchor 0.5
with dissolve

"琴凳并不算大。我想它本不是为两个人准备的。我的身侧紧紧贴着塞琳，我能感觉到她的大腿轻轻抵着我的。"
"我的脸刷地红了。"
"我还不习惯这样的亲密。"
Marcel embarrassed u "我，呃……对不起……"
"我羞赧地想要挪开，可我已无处可去。我的右大腿摇摇晃晃地悬在琴凳边上，险些失去平衡。"
"幸运的是，在我摔倒在地之前，塞琳一把抓住了我。"
show celine shock3 with dissolve
Celine "哦，玛塞尔！"
"塞琳把我拽回琴凳上，使我们的身体再次紧紧相贴，然后啧了一声。"
show celine sad3 with dissolve
Celine "你不必这般躲着我。我又不会传染人，你知道的。"
Marcel shy u "我、我知道。对不起。我、我只是……不想让你不自在……"
show celine sigh3 with dissolve
Celine "你说你担心我，可你看起来比我还要不自在得多。"
show celine frown3 with dissolve
Celine "放轻松些。肩膀老是绷得那么紧，你是什么也弹不出来的！"
Marcel huh u "说真的，我、我都不确定自己到底能不能弹出什么来。"
show celine huh3 with dissolve
Celine "眼下这对你或许是个过高的要求，但你的技艺会随着时间而进步，我敢肯定！"
show celine neutral3 with dissolve
Celine "那么，我们来看看这架钢琴吧。"
play sound "sfx/piano.ogg"
"塞琳打开了钢琴的木质琴盖。它吱呀作响，仿佛一个脾气乖戾的老人在抗议，塞琳叹了口气。"
show celine sigh3 with dissolve
Celine "天哪。这老东西竟发出阵阵可怕的声响！它怕是已经气数将尽了。"
show celine frown3 with dissolve
Celine "我好奇它在这儿待了多久？就算它比这所学校还要老，我也不会觉得意外！简直是一件十足的文物！"
show celine sigh3 with dissolve
Celine "若能让你在稍微不那么任性的琴上开始上课自是最好的……但眼下也只能将就它了。"
Marcel neutral u "就凭{i}我{/i}那蹩脚的琴技，钢琴的好坏恐怕也没什么两样。"
show celine frown3 with dissolve
Celine "恐怕确实没什么两样。你还没到所用乐器真正要紧的那一步。"

window hide dissolve
$ achievement.grant("marcels_first_lesson")
scene cg20 with wiperight_slow
$ renpy.pause(0.8)
window show dissolve

Celine "现在，来看看这些琴键！你留神了吗？"
"塞琳朝那一排排象牙色的琴键比了比：五十二个白键，三十六个黑键。"
Celine "这些都对应着一个音。这些音以字母命名，从 A 一直到 G……"
"塞琳向我讲解琴键布局的细节，而我坐着，连连点头。"
"每隔一会儿，她就会让我弹点什么，以此来证明我已经理解了某个概念。"
Celine "这个键——"
"她朝一个白键示意，那白键正依偎在一枚较小的黑键旁边。"
Celine "——就是 C。所有位于一对平行黑键之前的白键都是 C，只是它们处于不同的八度而已。"
Marcel "八度？那与音高有关吗？"
Celine "没错。你觉得你能用我刚才告诉你的信息，在这架琴上找出所有的 C 吗？"
Marcel "我想可以……"
Celine "那就把它们全都弹给我听。我想看看你是否已经掌握了。"

stop music fadeout 1.0
window hide dissolve
scene black with blinds2
$ renpy.pause(0.8)
play music "bgm/Friendship.ogg" fadein 1.0
scene sky_s with blinds2
window show dissolve

"课程就这样继续了大约半个钟头。"
"我还从未真正弹奏过什么。我仍在努力熟悉这琴盘上琴键的布局，弄清每一个音分别在哪里。"
"琴键如此之多，一时要记住可真不少，可一切都遵循着一种合乎逻辑的规律。"
"黑键以重复的序列排列，两枚一组、三枚一组，借助它们，便能确定其下方那些白键对应的音名。"
"每对成双黑键左侧的那枚白键，永远都是C。其后的白键依次对应D、E、F、G、A、B。然后，又重新回到C。"
"我原本以为学会钢琴是天方夜谭，可塞琳的讲解正帮我一点点理出头绪。"

scene musicroom_s blur:
    size (1920, 1080) crop (250, 60, 1152, 648)
show celine huh3 s:
    ypos 0.55 yanchor 0.5 xpos 0.5 xanchor 0.5
with dissolve

Celine "好了。我想我们正停在一个不错的节点上。"
"塞琳朝窗外瞥了一眼。自我们踏入这间教室以来，大约一个钟头过去了，太阳正开始西沉。"
"琴房里的煤气灯没有点燃，而塞琳并没有获准使用它们。"
"如今夜色已在我们四周沉降，就这样把课继续下去恐怕是不可能了。"
show celine frown3 s with dissolve
Celine "若能继续下去固然好，但没必要让眼睛太过吃力。初学者要记住琴键的位置本来就够难的了，更何况还得在暗处进行！"
Celine "反正这间屋子很快就要上锁了。我可不想让布吕吉埃夫人发现我们在这儿，把我们训斥一顿。"
show celine neutral3 s with dissolve
Celine "我们何不明天就从这里接着继续呢？"
Marcel neutral u "我倒不介意，只是有个小小的难题。"
show celine frown3 s with dissolve
Celine "什么？"
"塞琳皱起了眉头。"
Celine "别告诉我你已经想放弃了？"
Marcel shock u "不、不是的，我不是那个意思！"
"这堂琴课远没有我担心的那样糟糕。我动手弹的不多，但我觉得自己学到了不少东西。"
"至于能否全都记住，那又是另一回事了……"
"但我想，塞琳在一心想教我的匆忙之中，一定忘了某件更要紧的事。"
Marcel neutral u "只是……呃……"
Marcel sigh u "明天是星期六。教室全都关了。"
show celine huh3 s with dissolve
Celine "哦可不是，你说得对。我刚还把这给忘了！"
show celine frown3 s with dissolve
Celine "我们明天不能使用这架钢琴了，可那就太可惜了。你的课才刚开始呀。现在若是停下来可不好。"
show celine neutral3 s with dissolve
Celine "那么，我们何不这样做呢？"
Celine "你可以来我家，用我家的钢琴。它比这老古董要好得多，而且我们应该能用上许久，想用多久都行。"
show celine smile3 s with dissolve
Celine "我可以陪你反复过一遍基础，直到我确信你已经明白了。我很有耐心，等上几个小时也不在话下！"
show celine neutral3 s with dissolve
Celine "你觉得这样可好？"
Marcel shockblush u "这个，呃……"
"我不太确定自己是否喜欢一连几个小时反复练音阶这种事。这一堂课还不到一个钟头，我却已经感到筋疲力尽了。"
"我觉得自己并没有那份心气去承受塞琳的严厉教导——但我{i}确实{/i}想去她的住处。我想看看那里究竟是什么模样，而她居然会想到邀请我，更令我受宠若惊。"
"这是一份她此前从未认为适合赐予这所学校里任何其他女孩的殊荣。"
"这想必意味着，她在某种程度上是关心我的吧？"
"若不是如此，那就是她{i}真的{/i}想让我学会弹钢琴。"
Marcel smile u "那就好吧。"
"犹豫了片刻之后，我对塞琳的问询作了肯定的答复。"
Marcel "明天去见你，我倒不介意。其实我觉得那或许会很有趣。"
Marcel laugh u "请再多教我一些！我会尽力跟上你的！"
show celine smile3 s with dissolve
Celine "好，这可是你自己说的。既然你如此热切，我可就不能对你手下留情了。"
Celine "你是我的得意门生，所以我会把所知道的全都教给你。我相信，假以时日，你会丝毫不逊于巴黎音乐学院的学生！"
Marcel shy u "这、这一点我可没把握……但我会继续努力的。"
"眼下我能做的，就仅止于此了。"
"我从不觉得自己是个有音乐天赋的人，可要是我这番认真的尝试能让塞琳高兴，那我也愿意一试。"
"她的笑容，会让这一切都变得值得。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  10月2日{vspace=1}  长发公主的哀歌") )
scene cg28 with wiperight_slow
play ambience "sfx/night_amb2.ogg" fadein 1.0
play music "bgm/Night.ogg" fadein 1.0
window show dissolve

"那一夜，我躺在床上，直直地望着天花板。屋子被阴影吞没了一半，我听见风擦过窗玻璃发出的沙沙声。"
"我的长发在枕头上铺散开来。有一部分缠绕在我脑后，我一动，它便扯得头皮发疼。"
Marcel "好痛……"
"我疼得皱起了眉头。"
"尽管我的许多女同学都在头发上费尽心思，我却从来不太喜欢留着这样一头长发。它无疑是祸多于福……"
"但这份累赘我已忍受多年。我早已习惯了。"
"如果我能做主，我早就把它剪短了，可母亲执意不允。她向来喜欢为我梳理头发，我想，要是我像从前学校里那些男孩一样把头发剪短，定会伤了她的心。"
"有时候，我会想母亲是不是更想要一个甜美迷人的女儿，而不是一个高挑笨拙的儿子；但我知道，要是我问起，她定会说别犯傻了。"
"母亲总是不断安慰我，说有我，便足以令她幸福。"
"她说我很特别，可有时候，我不禁怀疑。"
"我这过长的头发过去给我带来了不少麻烦，可到了米耶讷，我想它倒成了桩幸事。它让我更容易假装自己是个女孩。"
"只是，我不禁好奇，待到明天早晨，我的伪装是否还能继续奏效。"
"塞琳邀请我去她家。这似乎是我们关系迈出的重要一步。"
"这是个寒冷的夜晚，风从老旧的窗玻璃缝隙间钻进我的房间，但心头那一丝小心翼翼的乐观，让我保持着暖意。"
"我明天就要去见塞琳了。我们会在她家那个私密的地方共度时光，只有我们两个人，到时候会发生什么呢？"
"也许她终于会向我吐露一些她的秘密。"
"我只希望我也能同样对她。"

stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene sky g
with clockwipe
$ renpy.pause(0.5)
show overlay2
show message5 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message5
hide logo2
hide overlay2
with datetrans2

$ renpy.pause(0.3)

$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  10月3日{vspace=1}  手挽着手") )
play ambience "sfx/birds.ogg" fadein 1.0
scene sky with dissolve
window show dissolve

"塞琳约好十一点在村里的面包店外与我会面。"
"尽管才来了一个月，我对米耶讷的路已经认得相当熟了。"
"我的方向感不算好，但村子这么小，店铺又少，走起来倒也不难。"
"那座教堂，有着沉稳的石塔和歪斜的风向标，是一处绝佳的参照物。它是米耶讷当之无愧的最大建筑，高耸于一切之上。"
"正如夜空中恒定不动的北极星一般，也可以用它来辨认自己的方位。"

stop ambience fadeout 1.0
play music "bgm/Friendship.ogg" fadein 1.0
show image "border" onlayer border
scene village:
    subpixel True
    size (1920, 1080) crop (0, 300, 1280, 720)
    linear 25.0 crop (350, 300, 1280, 720)
with wiperight_slow

"我提早了足足半个钟头到达我们约定的会面地点，因前一夜睡眠不足而疲惫，却也小心翼翼地抱着希望。"
"我穿的并不是校服，而是离家前姨母和母亲给我买的那件印花连衣裙。"
"那天早上，我在有限的衣柜里翻找了好一阵子，琢磨着该穿什么。"
"塞琳从未见过我穿那件朴素暗淡的校服以外的样子，而我想给她留下个好印象。"
"既然塞琳出身富裕人家，就算她自己拥有一柜子漂亮合身的连衣裙，我也不会感到意外。"
"我明知不可能与她相比，却总想让自己看起来至少费过一番心思；可是我的裙子没有一件合身得体，件件都显得太过朴素。"
"在把每件衣服都试穿了又放下至少两遍之后，我最终选了来时路上穿的那条裙子。"
"我的头发照例编成了辫子，脚上穿着一双素净实用的深色鞋子。"
"我大概还是老样子。"
"我希望塞琳不会因我这副潦草的模样而嫌弃我，也希望我不会因为这样在她的家里显得太过扎眼。"
"等待之际，我猜想塞琳的家是什么模样。会很大吗？会有多少间房间？她既然建议我到她家练琴，想必她自己一定有一架钢琴吧。"
"也许她有一张童话里公主那般装饰华丽的床，还有镶着攀爬常春藤与忍冬藤蔓的凸窗。"
"厨房里会飘着新烤糕点的香气（多亏了她的女仆），一切都洁净、明亮而通透。"
"我几乎等不及了——所幸，我也并不需要等太久。"
play sound "sfx/churchbells.ogg" fadein 1.0
"附近的教堂钟声发出一阵洪亮而清亮的鸣响。这些钟声标志着学校里所有课程的开始与结束，不过从米耶讷的另一头听去，那声音要安静得多。"
"如今我正站在村子中央，那声音要响得多，也更引人注目。"
"倘若这钟声是准确的，那么现在应该正是十一点。"

stop sound fadeout 1.0
stop music fadeout 1.0

"我向街巷间环顾，很快就看见了塞琳。"

play ambience "sfx/footsteps.ogg" fadein 0.5
hide image "border" onlayer border
play music "bgm/Celine.ogg" fadein 1.0
scene village
show celine c neutral:
    xpos 1.10 xanchor 0.5 ypos 0.53 yanchor 0.5
    ease 2.0 xpos 0.5
with wipeleft_slow

$ renpy.pause(1.2)
stop ambience fadeout 0.5

"她正朝我走来，带着女王般的端庄与优雅（或许是克利奥帕特拉那样的？）。"
"她身上所穿的衣裳，正与我设想的一模一样优雅。她的裙子是棕色的，绣着花朵，外面还套着一件相配的上衣。"
"她的裙子并不特别华丽（荷叶边比我预想的要少），但那面料看起来比村里姑娘们穿的衣裙质地要好得多。"
"塞琳也没有系围裙，而在那些出身劳苦人家的女孩身上，围裙是颇为常见的装束。"
"塞琳与我其余的同学不同，她不必劳作。她没有义务剥豌豆、给鞋子上蜡，或是掸去扶手上的灰。那些，我想，都是她女仆的差事。"
"我好奇米耶讷有多少人家雇得起女仆来打理家务。我怀疑恐怕没多少。"
"也许诺艾米家就有女仆（据我所知，她的父母拥有一间玻璃工坊，雇用了米耶讷的大批男子），但她想必也是仅有的那么几个之一。"
"塞琳的裙子低调朴实，可她仍能脱颖而出。"
"她美得如此动人，我几乎不敢相信她愿意与我扯上任何关系。"
Marcel shy c "塞、塞琳……那个……"
"我怯生生、笨拙地向她挥了挥手。"
Marcel smile c "见到你真好。你来得非常准时。"
show celine c frown with dissolve
Celine "你还指望会有别的结果吗？"
"塞琳挑起了一根眉毛。"
Celine "我从小便接受礼仪教养，深知不该让别人久候。那实在失礼至极；尤其是当{i}我{/i}才是那个约你来此相见的人时。"
show celine c sigh with dissolve
Celine "老实说，看到你比我先到，我挺意外的。"
show celine c sad with dissolve
Celine "但愿你没有等太久吧？"
Marcel ehe c "啊、啊，没有。完全没有。是我不该来得这么早……"
show celine c huh with dissolve
Celine "你提前来了？为什么？你就这么急着想见我？"
Marcel "算是吧，啊哈哈……"
"我将两根食指的指尖对在一起，正像米拉贝尔在被布吕吉埃夫人责骂时惯常做的那样。"
Marcel neutral c "今早我没什么事做，也受不了在房间里干等。我想不如来这里，还能呼吸呼吸新鲜空气。"
show celine c sigh with dissolve
Celine "啊。原来如此。"
show celine c neutral with dissolve
Celine "这么说，你很喜欢户外喽？"
Marcel smile c "我一辈子都住在巴黎，从没真正有机会体会过……但现在到了这里，我觉得这还挺惬意的。"
Marcel "连绵起伏的山丘真是漂亮极了！"
show celine c huh with dissolve
Celine "这一点我倒同意你，只是我自己实在怕冷。我真担心手指会冻僵，到时就弹不了钢琴了！"
Marcel huh c "真有可能吗……？"
show celine c neutral with dissolve
Celine "没有，是我在犯傻。我总为这些事大惊小怪。瓦雷纳先生总说我把音乐看得太重了。"
show celine c smile with dissolve
Celine "不过说到底，我还是个喜欢宅在家里的人。我宁愿待在屋里；最好再有一本书，或是一杯茶。"
show celine c huh with dissolve
Celine "我根本不是过这种自然生活的人……"
show celine c sigh with dissolve
Celine "但既然命运给我发了这样的牌，我只好尽我所能去打好它。"

play sound "sfx/footstep.ogg"
scene village:
    size (1920, 1080) crop (240, 80, 1440, 810)
show celine c huh2:
    xpos 0.5 xanchor 0.5 ypos 0.50 yanchor 0.5
with dissolve

Celine "好了。"
"塞琳伸出了她的一条手臂。"
show celine c neutral2 with dissolve
Celine "我们动身吧？今天要做的事很多，可不是闲聊的时候！"
Marcel shy c "好的。那个……"
"我狐疑地看着塞琳的手臂。"
Marcel neutral c "那是做什么用的？"
Celine "我想我们可以挽着手走。以前在奥尔良，我和朋友们就常常这样走；尤其是在冬天！"
Celine "我实在怕冷得厉害，总得想个法子暖暖身子！"
Marcel "啊、啊，好的……那个……"
Marcel "真的可以吗？"
Celine "当然可以。否则我才不会开口提议呢！"
show celine c huh2 with dissolve
"塞琳端详着我，一只手托着下巴。"
Celine "哎呀呀。你一副这么吃惊的样子，让人还以为我是在问你要不要亲你呢！"
show celine c frown2 with dissolve
Celine "别告诉我你以前从没跟老朋友做过这种事吧？"
Marcel "别、别笑我，不过……"
"我的脸颊染上了红晕，却并非因为天冷。不论塞琳怎么说，这天气都还没冷到那个份上。"
Marcel sigh c "我从来没有朋友可以一起做这种事。就算在以前的学校，我也总是被排斥在外，所以我不太确定朋友之间什么才算正常举止……"
Marcel sad c "我一定显得很傻吧……"
show celine c neutral2 with dissolve
Celine "你并不傻。也许只是有点不开窍？不过我觉得这也不是什么坏事。"
show celine c frown2 with dissolve
Celine "我真不明白为什么你的朋友那样少。巴黎的女孩也许在时尚上挺有品味，但她们识人的眼光实在差劲！"
Celine "你以前的那些同学都相当愚蠢……"
show celine c neutral2 with dissolve
Celine "不过，我倒不介意代她们弥补一二。"

play ambience "sfx/footsteps.ogg" fadein 0.5
window hide dissolve
$ achievement.grant("arm_in_arm")
scene cg21 with dissolve
$ renpy.pause(1.0)
window show dissolve

"塞琳牢牢地挽住我的手臂，宛如一根线穿过针眼。然后，她微微一笑。"
Celine "这样如何？你不介意吧？"
Marcel "啊、啊，不，那个……没、没关系……"
Celine "好！那我们就这样走吧。"
Celine "我来带你回我家。路并不太远。来吧——可千万注意别被自己的脚绊倒哦！"
Marcel "我、我不会的！"
"塞琳独自轻笑，声调柔和而悦耳，而我则跟在她身旁。"
"我能感觉到塞琳的胸膛贴着我的手臂。她那头被微风吹乱的深色头发，轻轻擦过我的肩膀。"
"她离我如此之近，她身上的暖意仿佛融化开来，与我自己的体温交融在一起。"
"我们脚步的声音几乎合成一体，投在地上的影子也相互交融。"
"我心想，若是我凝神细听，是否也能听见她的心跳。"
"我确信自己的心正像一面鼓，狂跳不已。"
"我以前从未与人如此贴近；更不必说是一个与我年纪相仿的姑娘了。"
"……呃，不。这话并不完全准确。克洛蒂娜也曾在几次场合强行挽过我的胳膊，但那只是为了拽着我到处走。这事我并没有多少发言权。"
"与塞琳之间这种新生的亲近感却截然不同。不知怎的，它更柔和，也让人觉得亲昵得多。"
"我不禁疑惑，这莫非真是女子们平日常做的事。倘若真是如此，那我自然是毫无头绪了。"
"我学校里的男孩大多从不这样勾肩搭背地厮混，而那样做的几个，受到的嘲弄跟我一样厉害（甚至更不堪）。"
"我以前的同学似乎把身体的亲近视作一种可耻的软弱：是要遭人唾弃与厌恶的东西。"
"温柔同样被视为专属于“孬种”的东西。男孩们会以别的方式表达情谊：或是锁住脖子的扭抱，或是踢一场足球，又或是在教室后排举行的扳手腕比赛。"
"他们眼中的友情是那样喧闹而粗野，几乎同我天天承受的欺凌一样，处处透着对抗。"
"我并不愿意成为同学们的对头，可要与他们交好，这念头同样令我心惊胆战。"
"我长成这样一个焦虑的人，又有什么可奇怪的呢？"
"我一向不喜欢男子间友情里那些粗野的打闹，而女子间的友情似乎大不相同。"
"我从前不知道，与另一个人挽着手臂走在大街上竟能如此惬意。那令人心安。"
"这样与塞琳在一处，让一件事显得格外分明——我并非孤身一人。"

stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  10月3日{vspace=1}  甜蜜的家") )
play ambience "sfx/birds.ogg" fadein 1.0
play music "bgm/Casual_Day.ogg" fadein 1.0
scene sky with wiperight_slow
window show dissolve

"塞琳的家比我预想的要小，却也丝毫不减其迷人。那是一栋小巧整洁的建筑，离村子中心只需走一小段路，坐落在树林边缘。"
"这房子地势略高，想要抵达，我们得走上坡路。这段跋涉为我的双颊添了些血色，也驱散了最彻骨的寒意。"
"她的家有两层。雪白的碎石抹灰外墙上嵌着四扇整齐的方窗，覆着一片低矮的红瓦屋顶。"
"这房子并不特别豪华，但显然被照料得十分周到。"
"前门上的门环被擦得锃亮，而前院里所有枯败的秋叶也都被清扫一空。"
"比起学校里我那间孤零零又阴郁的房间，这里看上去舒适得多。"
"至少，这才算得上是一个真正的家。"
"尽管它处处整洁，却透着有人居住、被人珍爱的气息。窗内摇曳的灯火足以印证这一点。"
"望着它，说实话，我竟有些想家了。"
"虽然我对巴黎并无太多留恋，我却着实怀念那个可以归去的家。"
Celine c neutral "甜蜜的家啊。至少就目前而言……"
"塞琳笑着摇了摇头。"
Celine "那么，我们进去吧？"
Marcel huh c "好、好的！那个……谢谢你招待我……"
Celine c smile "没什么麻烦的。这房子比我娘家的小得多，但就算是只有我和阿梅莉两个人在里面时，也会觉得空荡荡的。"
Celine c neutral "我想它会很高兴有人作伴吧……"
Celine "我也会一样。"

stop ambience fadeout 1.0
play sound "sfx/door.ogg"
$ renpy.pause(0.5)
play ambience "sfx/footsteps3.ogg" fadein 0.5
scene celine_entrance
show celine c neutral:
    xzoom -1 xpos -1.20 xanchor 0.5 ypos 0.53 yanchor 0.5
    ease 3.2 xpos 0.5
with wipedown_slow
$ renpy.pause(1.2)
stop ambience fadeout 0.5

"塞琳推开前门，然后示意我进去。"
Celine "我带你去客厅。今天大部分时间我们都会待在那里。不过你得先把鞋脱了。"
Celine "阿梅莉对家务可挑剔得很。要是你把泥巴踩得到处都是，弄脏了她漂亮的地毯，她会急得发疯的！"
Marcel huh c "好、好的。当然……"
"我脱下鞋子（其实无需她提醒），把它们与塞琳的鞋并排放好。然后，我跟着她沿走廊走去。"

play ambience "sfx/footsteps3.ogg" fadein 0.5
show celine:
    ease 1.5 xpos 1.1

"塞琳推开走廊尽头的一扇门，领我走了进去。"

play sound "sfx/door.ogg"
scene celine_living
show celine c neutral:
    xzoom -1 xpos -1.0 xanchor 0.5
    ease 3.0 xpos 0.5
with wiperight_slow
$ renpy.pause(0.5)
stop ambience fadeout 0.5

Celine "这里就是客厅了。"
"塞琳带着江湖艺人那副自命不凡的派头宣布道。"
show celine c smile with dissolve
Celine "我们要在这间房里待上不少时间，所以你最好放松些，别拘束。"
Marcel ehe c "不知怎么的，这话听起来像是一种威胁。"
show celine c frown with dissolve
Celine "啧啧！学音乐{i}从来{/i}不是威胁；尤其是在我这么好的一架钢琴上！你该为自己的这份机会感到庆幸才是！"
Marcel "啊、啊，我确实很感激。我、呃，极其感激。谢谢你耐心的教导，塞琳。"
"说罢，我环顾起这新到的环境。"

show image "border" onlayer border
scene celine_living:
    subpixel True
    size (1920, 1080) crop (0, 120, 1280, 720)
    linear 25.0 crop (350, 120, 1280, 720)
with wiperight_slow

"塞琳的起居室与她那处住所的外观一样，处处整洁而雅致。"
"房间本身并不算大，却仍流露着一股富足与良好教养的气度。"
"地毯上缀着繁复的花纹，四壁则是镶木护墙板。"
"屋里有一座壁炉，眼下并未生火，周围摆着几把椅子。这些椅子是路易十七式样的，硬朗的椅背覆着带花纹的奶油色天鹅绒。"
"又一次，我被一股强烈而毫无拘束的乡愁迎面击中。"
"这房间简直同我巴黎寓所里的起居室一模一样。"
"架上的中国花瓶，与当年父亲送给母亲的那份生日礼物颇为相似；弥漫在空气中的气味——肥皂与玫瑰水香水的香气——同样令人熟悉。"
"母亲自诩为一位有品味的女人（尽管她常抱怨，自己挑男人的眼光可不怎么样）。"
"我想，出身富贵的塞琳，也该有着相似的品味。"
"我不禁好奇，是不是所有富人都这样布置家宅。或许这些地毯、这些灯火、这些花瓶，在全法国成百上千——不，成千上万——的宅邸里都能见到……"

hide image "border" onlayer border
scene celine_living
show celine c frown:
    xzoom -1 xpos 0.5 xanchor 0.5
with wipeleft_slow

Celine "玛塞尔？"
"塞琳把脑袋歪向一侧。"
Celine "你还好吧？"
Marcel huh c "哦，对了！我刚刚在想……"
show celine c neutral with dissolve
Celine "在想我的家有多漂亮吗？"
Marcel smile c "确实很漂亮，是的。"
"只是未免太过似曾相识，令我涌起一股强烈的既视感。"
show celine c smile with dissolve
Celine "哎呀，谢谢你——可你还没见识到真正的重头戏呢！看，看！"
"塞琳指向钢琴，眼中闪着说不尽的欢欣。她看起来几乎像一位母亲在夸耀自己孩子的成就。"
show celine c neutral with dissolve
Celine "这架钢琴精美绝伦。它可比学校琴房里的那架华丽得多，你难道不这么觉得吗？"
Marcel neutral c "嗯……"
"我若有所思地端详着那架钢琴。"
"虽然我对乐器知之甚少，但一眼便能看出，它比学校里那架破旧的旧物要气派得多。"
"这架钢琴要新得多，也一直得到远为精心的照料。就我所见，它既无缺损也无凹痕，木质外壳光滑得胜过姑娘们的秀发。"
Marcel huh c "这架钢琴擦得可真亮，我都能在里面看到自己的倒影了！"
show celine c neutral with dissolve
Celine "那你得谢谢阿梅莉。她知道我有多喜爱这架钢琴——我几乎每天都坐在它面前！——所以她对它格外用心。"
Celine "如果物件也有感情，我想桌椅们大概会心生嫉妒吧！"

show celine:
    ease 1.0 xpos 0.68

$ renpy.pause(0.6)

scene celine_living:
    size (1920, 1080) crop (480, 80, 1440, 810)
show celine c neutral2:
    xzoom -1 xpos 0.35 xanchor 0.5
    ease 2.0 xpos 0.5 xanchor 0.5
with wiperight_slow

"塞琳走向钢琴。她用手指轻轻抚过琴身，始终带着若有所思的微笑。"
Celine "这架钢琴对我来说很特别。它伴随我已经有相当一段时间了。"
Celine "当年我还是个小女孩时，就是在这架钢琴上第一次学会弹琴的。"
Marcel shock c "真的吗？可它看起来像崭新的一样！"
show celine c huh2 with dissolve
Celine "那是因为它被照料得很好。事实上，它已经快要十岁高龄了。"
Celine "严格说来，它甚至不算我的钢琴，而是属于我父亲的。"
show celine c frown2 with dissolve
Celine "说起来，他得到这架钢琴的过程还挺有趣。有一天他在一家商店橱窗里见到它，然后就决定了——我想纯粹是一时兴起——他想要它。他觉得这架钢琴会让家里的客厅增色不少。"
Marcel neutral c "他难道没打算用它吗？"
show celine c sigh2 with dissolve
Celine "他不会弹。我父亲不会弹钢琴，我母亲不会，我的两个姐妹也不会。"
Celine "他买下这架钢琴，只是出于审美上的喜好，别无其他理由。对我父亲而言，这架钢琴无非是一件奢侈的摆设。"
Marcel "那一定是一件非常昂贵的摆设……"
show celine c frown2 with dissolve
Celine "哦，确实是，但我父亲非常有钱。他从来不怎么在乎钱，也不在乎是否花得明智。"
Marcel smile c "但到头来它还是派上了些用场。你不是学会弹琴了吗？"
show celine c sad2 with dissolve
Celine "我确实会了……但那并非出于我自己的意愿。至少一开始不是……"
"塞琳的手指继续抚摸着钢琴的木质外壳。她的声音染上一缕追忆的、浸透怀旧的惆怅，接着说下去。"
show celine c frown2 with dissolve
Celine "我父亲买下这架钢琴，是因为他买得起，因为他喜欢。他再没往深处想过别的……"
show celine c huh2 with dissolve
Celine "可后来有一天，他重新考虑了起来。"
show celine c frown2 with dissolve
Celine "他想，既然家里已经有了这架钢琴，那我们不妨用它。让它搁在角落里积灰，实在也没什么意义。"
show celine c sad2 with dissolve
Celine "那便是我开始弹琴的时候。全因我父亲这样要求——正如他对我人生中其他一切也都这般做主一样！"
Celine "他一心想做成什么事，就指望别人一字不差地照办。他向来是个苛刻的人。"
show celine c sigh2 with dissolve
Celine "他是如此严格……"
"塞琳叹了口气。"
show celine c frown2 with dissolve
Celine "起初我并不怎么想学弹琴。我觉得那简直无聊透顶。我在课上一个劲地打哈欠，一点也没专心……"
show celine c neutral2 with dissolve
Celine "但瓦雷纳先生待我极为和善。他的耐心仿佛没有尽头，至少我是这样以为的，而且他从不发脾气。他努力让我明白钢琴的美好，渐渐地，我总算也开始用同样的心意去回应他。"
Celine "若是换了别的老师教我钢琴，我怀疑自己未必能同这件乐器建立起这样的联系……"
show celine c smile2 with dissolve
Celine "可是瓦雷纳先生讲话实在太有感染力了，我忍不住就被他打动了。"
show celine c neutral2 with dissolve
Celine "他对音乐是如此热忱，从他的眼睛里就能看出来。他最爱的莫过于弹奏钢琴，而他也想让我同样爱上它。"
Celine "我变得这般痴迷……我想，恐怕是无可避免的。"
show celine c smile2 with dissolve
Celine "他教会了我如何去爱音乐。"
show celine c huh2 with dissolve
Celine "在我父亲所有的任性念头里，我想钢琴课带给我的好处最大。若不是他十年前一时冲动买下这架钢琴，我也不会成为今天的我。"
show celine c frown2 with dissolve
Celine "一个决定竟能永久地改变一个人的一生，说起来真的有些奇妙……"
"塞琳摇了摇头。"
show celine c huh2 with dissolve
Celine "无论如何，当我被送到这里来时，我就知道自己非得把这架钢琴带到 Myennes 来不可。我实在不忍心把它留在老家的宅邸里，被冷落不弹。"
show celine c frown2 with dissolve
Celine "我父亲起初反对这个主意。他说要把这么一件大东西从奥尔良搬到 Myennes 实在不切实际，但我坚持不让步。在出发前的几个星期里，我们为此一次次争执不下，直到他最终才勉强点了头。"
show celine c sigh2 with dissolve
Celine "这是我有生以来唯一一次能反抗他。"
Celine "从我小时候起，他就一直主宰着我的人生……"
show celine c frown2 with dissolve
Celine "不过至少，我总算保住了这架钢琴。"
show celine c huh2 with dissolve
Celine "这还算值得庆幸。"
play sound "sfx/piano.ogg"
"塞琳掀开琴盖，露出一排琴键：五十二个白键，三十六个黑键。"
"琴键本身与钢琴的木质外壳一样光可鉴人。纤细的黑键宛如煤色，而洁白无瑕的白键则把它们映衬得格外华美。"
"这些琴键未曾被黏腻的手指玷污，又被如此精心地使用，上面几乎看不出任何印记或划痕。"
show celine c neutral2 with dissolve
Celine "好了……我想闲聊就到此为止吧。"
Celine "我们开始上课吧？现在正是最好的时机。"
Marcel huh c "好、好的！"

window hide dissolve
scene cg20_2 with wiperight_slow
$ renpy.pause(0.8)
window show dissolve

"塞琳在琴凳上坐下，我连忙站到她身边。我面朝键盘，咽了口唾沫，手指蜷缩在我印花连衣裙的布料上。"
Celine "那么，我们接着上次讲的地方继续吧。如果你还记得，黑键是按三枚和两枚一组排列的，而白键……"
"塞琳的声音如同海浪般拂过我的全身。"
"她的语气十分平静而有分寸，可我依然能感到掌心在冒汗。"
"我的手指仍蜷曲在膝头，因焦虑而近乎僵直地攥住了一把裙摆。"
"这排琴键过于洁净，我竟有些不敢真的去弹。我不愿自己这双配不上它的手玷污了这件乐器。"
"若是我把它弄坏了，我会愧疚难当。我想塞琳恐怕永远也不会原谅我。"
"这真是要承担一份沉重得可怕的责任。"
Celine "玛塞尔？你还好吗？"
Marcel "啊、啊，是的！我很好！"
Celine "我可不这么认为。"
Celine "我已经让你弹中央C弹了两次了，你却一直没有动手。你盯着琴键的样子，就像它是一条毒蛇！"
Marcel "哦，那个……对、对不起……我又在想别的事了……"
Celine "我希望你是在想音乐的事。要是不专心，是没法磨炼琴技的。"
Celine "好了，中央C在哪里？你能帮我找出来吗？你昨天可还找得到。"
Marcel "昨、昨天情况不一样。我恐怕，那个……"
"我低下头，双颊泛红。"
Marcel "我不想弄坏你的钢琴。"
Celine "啊。原来你担心的是这个？"
"塞琳傲慢的神情缓和了下来。"
Celine "别担心。弹错音符或许会伤了耳朵，更别提伤到我身为老师的自尊，但那是不会损坏钢琴的。"
Celine "要想弄坏它，你得是粗心到了极点才行。"
Marcel "可、可{i}我{/i}就是粗心啊！我笨手笨脚得厉害！"
Celine "你可以嘴上迷糊，但行动上不会。你可不是可怜的米拉贝尔，她总是被自己的脚绊倒。"
Celine "求你，别害怕。有我在呢。我不会让你犯什么大错的。"
Marcel "可万一我真的犯了错呢……？"
Celine "那么，要怪就怪我这个老师当得不称职吧。"
Celine "你是我请来的，所以万一出了什么差池，都由我全权负责——不过我怀疑根本不会出什么差错。"
Celine "好了，中央C！你能找到它吗？"
Marcel "好，呃……我想是这个？"
"我将一根手指按在一个白键上。钢琴随之发出一个饱满的音符；这台木制乐器内部的琴弦，随着我极轻微的触碰而绷紧。"
"这架钢琴比学校那台灵敏得多。琴键不会卡顿，奏出的音色也更加清亮。"
"这么说来，也许弹起来反而更容易。"
Celine "对，没错。做得好。"
Celine "好了，下一个任务。看看你能不能找到这个音……"
"塞琳带着我做几项简单的练习。幸运的是，我还记得昨天课上的不少内容，因此不费什么力气就能找到这些琴键。"
Celine "很好！我想你已经上手了！"
Celine "那么，既然你已经知道白键在哪里了，我们就来说说黑键吧……"
"随着时间推移，我越来越习惯于塞琳的陪伴。她温柔的鼓励抚平了我心中的焦虑，她贴在我身上的体温也让我安心。"
"我依旧是个乐理上的文盲，但我想，只要听从塞琳的指点，我应当学得会。毕竟，没有人是彻底无可救药的。"
"或许我真的做得到。我只需要继续努力。"
"我要先学会所有白键与黑键的位置，然后再学认乐谱，接着——"

stop music fadeout 1.0

scene celine_living:
    size (1920, 1080) crop (480, 80, 1440, 810)
show celine c neutral2:
    xzoom -1 xpos 0.5 xanchor 0.5 ypos 0.55 yanchor 0.5
with wipeleft_slow

W "塞琳！你打算什么时候才告诉我你的客人已经到了，嗯？"

play music "bgm/Comedy.ogg" fadein 1.0

Marcel shock c "哦……！"
"我吓了一跳，手指不协调地撞上琴键。"
"我实在太专注于钢琴，竟没能听见脚步声，也没察觉门被推开。"
"但那道声音，却无论如何也无法忽视。"
"那是一道母亲般的声音，而拥有这道声音的女子，看起来同样温暖、慈祥。"
"她站在门口，双臂在身前交叠。她穿着女仆的朴素装束——一件素净的黑裙，外罩一条白色围裙。"
"她的眼睛温暖而呈棕色，宛如热可可，深陷在脸上。她的眼角与嘴边布满皱纹，双颊的肉也微微下垂。"
"这些皱纹，再加上她花白的头发，让我相信这位女子大约四十出头。"
"她唇边漾起的笑容十分慈祥，周身还散发着一股新切苹果与肉桂的香气。"
"我知道她是谁。她一定是塞琳的女仆。"
"塞琳说她叫什么名字来着……？"
show celine c huh2 with dissolve
Celine "哦，阿梅莉！"

show celine:
    ease 0.6 ypos 0.5

$ renpy.pause(0.3)

scene celine_living
show celine c frown:
    xzoom -1 xpos 0.53 xanchor 0.5 ypos 0.53 yanchor 0.5
    ease 1.4 xpos 0.70
with wipeup_slow

$ renpy.pause(0.8)

show amelie smile:
    xzoom -1 xpos -1.10 xanchor 0.5
    ease 3.0 xpos 0.30

show celine c frown:
    xzoom 1 xpos 0.70

with dissolve

"塞琳从琴凳上起身，一边整理裙摆，一边叹了口气。"
Celine "你来这儿做什么？我还以为你在厨房里烤东西呢！"
Amelie "我是在烤东西，{i}原本{/i}是的，直到被你们这两位弹琴的小姐打断了！怎么？"
"阿梅莉把目光投向我这边。"
Amelie "你难道不打算把我介绍给你的朋友吗，塞琳？"
Marcel neutral c "好，呃……我叫——"
show celine c sigh with dissolve
Celine "哦，阿梅莉！我昨晚不是全告诉你了吗！你难道不记得我说过什么？"
show celine c frown with dissolve
Celine "这位是玛塞尔·雷诺，她和我在一个班。她是九月初来到米延的，来自巴黎。"
show amelie laugh with dissolve
Amelie "玛塞尔小姐，是吗？对，这些我都记得。我的记性还没{i}那么{/i}差劲！"
show celine c sigh with dissolve
Celine "那你为什么还开口要求介绍？你根本就用不着！"
show amelie smile with dissolve
Amelie "我所以开口，小小姐，是因为那样才有礼貌。一个人总得讲究规矩！"
Amelie "听别人谈论一个人，和亲眼见到本人，那可是大不相同的。我也一直盼着见见你的这位小朋友——虽说她恐怕也没那么小，我猜！"
show amelie laugh with dissolve
Amelie "哎呀，我看她简直比圣科尔先生本人还要高呢！"
show celine c frown with dissolve
Celine "你我都清楚，父亲算不上什么叫人敬佩的人物，尽管他偏要装出一副了不起的样子。所以他才会那么爱吹嘘。"
"塞琳嗤了一声。"
show celine c huh with dissolve
Celine "好了。现在你见过玛塞尔了。你总该满意了吧？"
show amelie frown with dissolve
Amelie "哦不，还没呢！我可不能就这样算了！我得让她觉得宾至如归！"
show amelie smile with dissolve
Amelie "您好，小姐？很高兴认识您。要不是这小丫头想把我瞒着，我本该早些结识您的！"
Amelie "我叫阿梅莉·热拉尔，不过你可以叫我阿梅莉。大家都这么叫！"
Marcel smile c "那么，呃……很高兴认识您，阿梅莉……？"
show amelie laugh with dissolve
Amelie "这就对了！多有教养啊！脸蛋也标致！个子这么高，人还这么俊！"
Amelie "哎呀，你简直像位真正的淑女！"
Marcel neutral c "我家颇有些家底……"
"只是最好别提这份家财是靠在舞台上挣来的。当演员算不得体面的行当，而我父亲，更是全巴黎最不体面的男人之一。"
show amelie smile with dissolve
Amelie "是吗？真好啊！"
show amelie sad with dissolve
Amelie "只可惜，这位年轻小姐学校里的大多数女孩怕都是些野丫头！你知道，她们都是邮差、铁匠、农夫的孩子。我家塞琳一直很难融入其中。"
show amelie smile with dissolve
Amelie "我原先担心她会孤零零一个人，现在看来，我最担心的心事总算是放下了！"
Amelie "谢谢你愿意和塞琳小姐做朋友。她可能不会这么说——她一向笨嘴拙舌——但我相信这对她来说意味非凡。"
Amelie "当然，对我这个监护人和陪侍来说，也意味着一切！"
show celine c shockblush with dissolve
Celine "够、够了……！"
"塞琳的脸在阿梅莉滔滔不绝的闲谈中渐渐涨红，如今已泛成一颗熟透的草莓的颜色。"
Celine "一个字也不许再讲了！"
play sound "sfx/slap.ogg"
show celine c annoyed with dissolve
"塞琳眯起眼，眼睑上的一排黑色睫毛宛如一道戏剧性的弧线，然后一脚跺在地上。"
show amelie frown with dissolve
Amelie "行了行了，小姐，这可不够淑女。你父亲可不是把你养成动不动就发脾气、大吵大闹的样子的！"
show celine c frown with dissolve
Celine "我父亲怎么想无关紧要！他现在又不在这儿！"
Celine "他不在，我就是你的主子，你应该听我的！"
show celine c annoyed with dissolve
Celine "我不希望你为了我摆出那副可怜兮兮的感激样子，也不必拿这些恭维话去烦玛塞尔！你说得好像我压根儿没有一个朋友似的！"
Amelie "要是听起来是那样，小姐，那是因为事实就是如此。我一直以为你一个朋友都没有，因为你从没邀请过他们来家里！"
show celine c shy with dissolve
Celine "那是……我只是……我从、从来没想过要请谁来。我没有那个必要。"
show celine c frown with dissolve
Celine "我可不想让哪个同学把脏手指头按在我珍贵的钢琴上！"
show amelie smile with dissolve
Amelie "可是，要是那手指头属于玛塞尔小姐，你就不介意了？"
show celine c huhblush with dissolve
Celine "那不一样。我信任她。她跟别人不同。"
show amelie laugh with dissolve
Amelie "真好！看来你们俩已经走得很近啦！"
show amelie smile with dissolve
Amelie "好了，玛塞尔小姐。希望你不要因为刚才那一闹就看轻了年轻的塞琳小姐。我知道她有时别扭、挑剔、又爱强人所难——"
show celine c annoyed with dissolve
Celine "喂、喂！"
Amelie "——但她骨子里是个非常善良、温柔的女孩。请您千万别忘了这一点。"
Amelie "在涅夫勒——不，在整个法国！——像她这样心思细腻的女孩可没有几个。"
Amelie "请您好好照顾她。"
Marcel shy c "嗯……"
"这渐渐尴尬得像是相亲了。单听阿梅莉的口气，简直让人觉得我是在图谋成为塞琳的终身伴侣，而非她的朋友！"
"这有点让人不安，但我尽力泰然处之。"
Marcel smile c "我会尽力做一个好朋友的。我保证。"
"我优雅地行了个屈膝礼（这似乎是个得体的回应），逗得阿梅莉笑了起来。"
show amelie laugh with dissolve
Amelie "嗯，我想你能尽力，那就够了！"
show amelie smile with dissolve
Amelie "谢谢你打消了我的顾虑，玛塞尔小姐。你看起来是位非常出众、教养良好的年轻淑女。"
Amelie "我想你和塞琳一定会相处得非常融洽！"
show celine c frown with dissolve
Celine "哎呀，多谢你了，不过我想我并没有征求你的意见，阿梅莉。"
"塞琳翻了个白眼。"
show celine c sigh with dissolve
Celine "这正是我不愿意把你介绍给玛塞尔的原因。我不想让你像个警察似的审问我的朋友。"
Celine "你别再管我的闲事了！"
show amelie laugh with dissolve
Amelie "抱歉，小姐，可我实在忍不住！我打听是因为我在乎，你知道的？"
show celine c sad with dissolve
Celine "是的，我知道。你一直对我很好。我……很感激。"
show amelie smile with dissolve
Amelie "这没什么。我不过是尽本分罢了。"
Amelie "小姐，如果我连你的生活都不过问一下，那可真不配当这个管家了！"
Amelie "好了，我就不打扰你们俩了。好好上你们的钢琴课，不过别太苛刻，小姐！你要是把玛塞尔逼得太紧，她说不定会打退堂鼓，不愿再来了！"
show celine c annoyed with dissolve
Celine "这、这话该我来说才对！{i}你{/i}才是那个差点把玛塞尔吓跑的人！"
"阿梅莉并没有反驳这话。相反，她笑了。"
show amelie laugh with dissolve
Amelie "需要我的话，我就在厨房。我拿手的苹果塔再过个把小时就好了。等好了要不要我叫你们一声？"
show celine c neutral with dissolve
Celine "好，有劳了。那就麻烦你了。"
show amelie smile with dissolve
Amelie "那就这样。你们继续吧，小姐们！"

play ambience "sfx/footsteps3.ogg"
show amelie:
    xzoom 1
with dissolve

$ renpy.pause(0.3)

show amelie:
    ease 2.0 xpos -1.10
show celine:
    ease 1.2 xpos 0.5

$ renpy.pause(0.8)

stop music fadeout 0/5
stop ambience fadeout 0.5
play sound "sfx/door.ogg"
hide amelie with dissolve

"阿梅莉转身离开了起居室。她围裙上系着的白色丝带随着每一步轻轻飘动，黑裙的裙摆则如水面般泛起涟漪。"
"门在她身后咔嗒一声关上，随后我便听见她的脚步声沿走廊渐渐远去。"
"此后，便只剩下寂静。"
"等我确定阿梅莉已经走远，我长舒一口气。终于可以放松下来了。"

play music "bgm/Casual_Day.ogg" fadein 1.0

Marcel sigh c "唉……这可真是够可以的了。"
Marcel neutral c "她身子小巧，气场倒是很足。"
show celine c sigh with dissolve
Celine "用‘气场’来形容，倒也是一种说法……"
"塞琳皱起了眉头。"
show celine c frown with dissolve
Celine "我为刚才的事道歉，玛塞尔。阿梅莉确实是好意，可她实在太爱为我操心了。"
Marcel "那么，看来这也不是最近才有的了？"
show celine c sigh with dissolve
Celine "何止！从我小时候起，她就是这样待我的。"
show celine c frown with dissolve
Celine "你要知道，我的母亲从来就不像一位真正的母亲。她总是缺席，不是去赴晚宴，就是去参加派对或舞会。她几乎没有时间留给我。"
show celine c sad with dissolve
Celine "阿梅莉觉得我可怜，就想弥补一下。她便充当起我的代理母亲。她总爱数落我，要我吃掉芦笋，要么就收拾好我的书架。"
show celine c sigh with dissolve
Celine "那时我因此怨恨过她，可我知道那是出于爱。"
show celine c sad with dissolve
Celine "我被送到米延时，她是唯一一个自愿跟我来的仆人。她为了我不知疲倦地操劳，这一点我很感激。"
Celine "我爱她几乎不亚于——也许还胜过——爱我的亲生母亲……"
show celine c frown with dissolve
Celine "可我现在已经十五岁了，到了能自己做主的年纪了。"
Celine "我真希望她能明白这一点！"
Marcel sad c "听起来你们的关系很复杂……不过我想我能体会。"
show celine c huh with dissolve
Celine "你能？"
Marcel sigh c "嗯。我自己的母亲也很疼我。有时我觉得她的关爱让人透不过气，可我知道那是出自真心。"
Marcel "如今我在这儿，在米延，我有点想她了。"
"此刻站在塞琳的起居室里，置身于那些中国花瓶与令人怀旧的玫瑰水香水气味之中，我比从前任何时候都更想念母亲。"
Marcel sad c "我可以给她写信，可那不一样。我想再和她面对面说说话，但目前就是做不到。"
Marcel "她一定很担心我。她的信里满是挂念和问话。她担心我在这儿交不到新朋友。"
Marcel neutral c "我觉得她很像你的阿梅莉。"
Marcel sigh c "那样的人，想不操心都难吧，我想。"
show celine c neutral with dissolve
Celine "我想你说得对。"
"塞琳笑了。"
show celine c smile with dissolve
Celine "谢谢你这么体谅我，也谢谢你不曾评判我。"
show celine c frown with dissolve
Celine "我敢肯定，要是克洛蒂娜看到阿梅莉这么为我操心，她肯定会没完没了地笑话我……"
Marcel smile c  "她多半会那样，没错。"
show celine c sigh with dissolve
Celine "噢，真荒唐！阿梅莉总唠叨我朋友少，可我从没请过任何一个人来家里，一半就得怪她！"
show celine c sad with dissolve
Celine "有时候，我真希望她能给我留一点自己的空间……"
show celine c huh with dissolve
Celine "可我更喜欢有她相伴，胜过独处；我也喜欢和你待在一起，玛塞尔。"
show celine c neutral with dissolve
Celine "好了……"
"塞琳回过头看向钢琴。琴盖仍然敞着，那一排整齐的白键与黑键正等着我们。"
Celine "我们继续上课好吗？"
Marcel shock c "好、好啊！我还有好多东西要学呢！"
Celine "很好。我喜欢你的劲头。我会尽力当个好老师教你的，玛塞尔。"

show celine:
    ease 1.0 xpos 0.68

$ renpy.pause(0.6)

show celine:
    xzoom -1 xpos 0.68
with dissolve

$ renpy.pause(0.3)

scene cg20_2 with wiperight_slow

"塞琳重新在琴凳上坐下，我连忙跟了过去。"
"她为我讲解琴键的排列，我边听边点头。她偶尔让我找出某个特定的音，我便照做。"
"待她确信我已掌握了要领，便接着教我如何弹奏一段简单的旋律。"
"这只是一小串音符——一段来自童谣的、反复循环的简单句子——但当我能够把它复现出来时，我仍感到十分自豪。"
"几天之前，我连两个连贯的音符都串不起来。"
"如今，我已经能弹奏出一些像是真正音乐的东西了。"
"当然，我知道这不过是开始。就目前而言，我连初学者都算不上。我敢说，就连小孩子弹的曲子恐怕也比我复杂，但这终究是进步。"
"一点一点地，我渐渐开始入门了。"
"只要我继续努力，我相信自己一定做得到。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  10月3日{vspace=1}  瓦雷纳先生") )
play music "bgm/Energetic.ogg" fadein 1.0
play ambience "sfx/birds.ogg" fadein 1.0
scene sky with wiperight_slow
window show dissolve

"弹了一个小时的钢琴后，我同塞琳停下来歇口气，尝尝阿梅莉做的苹果派。"
"这苹果派实在美味，甚至胜过我在巴黎任何一家法式糕点铺尝过的。"
"派还带着出炉的温热，酥皮层层起酥，可口至极。至于派里的苹果，则以肉桂慷慨地调味；每一口都仿佛在舌尖化开。"
"这派实在太好吃了，我完全能吃下第二块（乃至第三块）。我想阿梅莉也不会介意。她似乎很高兴我这么喜欢她的派，甚至还想再塞给我一些……"
"但塞琳却不为所动。"
Celine c frown "我请玛塞尔来，可不是让她整天吃派的，阿梅莉。我是要教她弹钢琴的！"
Celine "我们已经耽搁得太久了。我想让她在太阳落山前多少有点进步。"
Celine "好了，把手上的饼屑弄干净，我们接着来。我可不准你把我的钢琴弄脏！"
"尽管塞琳个子不高（我的同学里，除了诺艾米，全都比我矮），说话却如此不容置疑，我连忙照办。"
"我不愿自己与塞琳新建立的友谊，因为一块派就土崩瓦解。"
"我把手洗到发红发疼，然后用毛巾擦干。"
"之后，我回到起居室，和塞琳一起练习。"
"我们又一起练了好几个小时，直到连百折不挠的塞琳也觉得我们需要歇一歇。"
"也许她看出了我有多疲惫，也许她对我生出了一丝怜悯。"
"塞琳或许是个严厉的老师，但她并不残忍。"

stop ambience fadeout 1.0
scene celine_living:
    size (1920, 1080) crop (480, 80, 1440, 810)
show celine c neutral2:
    xzoom -1 xpos 0.5 xanchor 0.5 ypos 0.55 yanchor 0.5
with wipedown_slow

Celine "我想我们暂时已经练得足够好了。要是再继续下去，你的手指会酸的，而且脑子一疲劳，你就会比平时犯更多的错。"
Marcel shy c "是，呃……很抱歉。"
Marcel sigh c "我是很专心的——我发誓我很专心！——可这半个小时里，我的手好像就是不听话。"
show celine c smile2 with dissolve
Celine "没关系。谁都会这样。就连我刚学弹琴时也犯过错。"
Marcel huh c "真、真的……？"
show celine c huh2 with dissolve
Celine "真的，千真万确。你干嘛这么惊讶？"
show celine c frown2 with dissolve
Celine "我和你一样只是个凡人，我也会犯错。"
Marcel "我知道，可是……你看起来不像是会犯错的人。你是那么自信！"
show celine c huh2 with dissolve
Celine "我自信是因为我弹了多年的钢琴。我这份自信是挣来的。而你嘛——"
"塞琳用食指戳了戳我的侧腰。"
Celine "——还没有。你还是个初学者。连业余都算不上。"
show celine c smile2 with dissolve
Celine "离你能达到我严苛的标准，你还差得远呢！"
Marcel shock c "是——是的，夫人！非常抱歉！"
show celine c frown2 with dissolve
Celine "对了，你干嘛这么叫我？我又没结婚，年纪也不比你大。"
Marcel ehe c "我知道。只是……你比我厉害太多，不知怎的，叫你‘夫人’好像挺合适。"
show celine c sigh2 with dissolve
Celine "别，别那么叫。我可不想跟布吕吉埃夫人那类人混为一谈。"
show celine c neutral2 with dissolve
Celine "好了，我们歇一会儿吧。我要是把你逼得太紧，可能会把你压垮，那可绝对不行！"
Marcel shy c "嗯……"
"我并不完全明白塞琳说要把我“磨垮”是什么意思。她是怕我继续犯这种愚蠢的错误，会连仅剩下的一点点自信也丧失殆尽，还是说她指的是我身体的状况？"
"我要是继续弹下去，手指不会真的断掉吧？"
"这想法可真吓人……"
Marcel ehe c "这、这主意不错。我确实觉得有点累了。"
Celine "这很正常。你的脑子正拼命记下这么多新东西，而长时间端坐着不动，对后背和肩膀来说也确实辛苦。"
show celine c huh2 with dissolve
Celine "也许我们该去我的房间。那里既惬意又宽敞。如果你需要的话，我甚至可以让你在我的床上躺一躺。"
Marcel shockblush c "什、什么？呃，唔……"
"面对这个再无耻不过的提议，我的脸颊烧得滚烫。"
"倘若我真是个女孩，我大概连想都不会多想便踏进塞琳的闺房；可事实是，我不是。"
"无论外表如何，我终究是个男孩，所以我实在不该踏入一位小姐的闺房，更别说躺在她的床上！我的良心是永远无法安宁了！"
Marcel shy c "那……真是多谢你的好意，可、可我们不能就待在这儿吗？这间会客厅已经够宽敞了，那边还有几把椅子，我们可以坐下。"
show celine c frown2 with dissolve
Celine "会客厅是不错，没错，可我们要是在这儿逗留，阿梅莉多半会过来打扰我们。"
show celine c sigh2 with dissolve
Celine "以她的性子，她准有一肚子急切的问题想问你。"
show celine c frown2 with dissolve
Celine "你不想被盘问吧？"
Marcel "呃，唔……确实不太想……"
show celine c huh2 with dissolve
Celine "那就来吧。"

play sound "sfx/slap.ogg"

show celine:
    ease 0.6 ypos 0.5

$ renpy.pause(0.3)

scene celine_living
show celine c neutral:
    xzoom -1 xpos 0.5 xanchor 0.5
with wipeup_slow

"塞琳干脆地合上琴盖，发出沉闷的一声，随即站起身来。"
Celine "我带你去看看我的房间在哪儿。"
Marcel huh c "好、好的……"
"我对此仍有几分顾虑，但我觉得自己没法拒绝塞琳。很显然，她已经打定了主意。"
"她的威严，比一位军官还要更盛。"

play ambience "sfx/footsteps3.ogg" fadein 0.5
show celine:
    xzoom 1
with dissolve

$ renpy.pause(0.3)

show celine:
    ease 1.8 xpos 0.0 xanchor 0.5

$ renpy.pause(0.8)

play sound "sfx/door.ogg"
scene celine_entrance
show celine c neutral:
    xpos 1.2 xanchor 0.5
    ease 2.0 xpos 0.5
with wipeleft_slow

"我跟着塞琳走出起居室，然后上了楼。"

show image "border" onlayer border
scene celine_entrance:
    subpixel True
    size (1920, 1080) crop (450, 0, 1280, 720)
    linear 20.0 crop (450, -120, 1280, 720)
with wipeup_slow

"她穿过走廊，推开一扇带着锃亮黄铜门把手的白色房门。"
play sound "sfx/door.ogg"
Celine c smile "你先请。"
"塞琳朝门内示意，随即优雅地行了个屈膝礼。我踩着迟疑而拖沓的步子走了进去，每过一秒都愈发觉得自己像个闯入者。"
"我不该待在这里。"
"走进塞琳的房间，即便得到她的许可，仍让我觉得自己仿佛在辜负她的信任——可我没多少工夫为这事烦恼，因为我很快便被塞琳卧室的室内陈设吸引住了。"

stop ambience fadeout 0.5
hide image "border" onlayer border
scene celine_room
show celine c neutral:
    xzoom -1 xpos -1.0 xanchor 0.5
    ease 3.0 xpos 0.5
with wipe

Marcel shock c "噢，天哪……"
Celine "那么，你觉得怎么样？很漂亮，对吧？"
Marcel smile c "我、我自己实在没什么审美眼光，不过……确实很不错。"

show image "border" onlayer border
scene celine_room:
    subpixel True
    size (1920, 1080) crop (0, 100, 1280, 720)
    linear 20.0 crop (350, 100, 1280, 720)
with wiperight_slow

"塞琳的房间不如起居室那般华丽，却丝毫不减其可爱。事实上，我倒觉得正因如此，它反而更加迷人。"
"她的地板是打磨光洁的木料，但大部分被一张毛茸茸的红色地毯覆盖着。"
"四壁是柔和的粉色，缀着花朵装饰，还有一扇镶着轻薄纱帘的大窗。"
"她的床相当宽敞（那是房间里最大的一件家具），堆满了柔软的枕头和厚实的被褥。"
"整个房间弥漫着一股柔和而清甜的气息，宛如薰衣草。或许是塞琳床上的枕头里填满了它？"
"总而言之，这是一个非常明快、通透的房间，处处都透着品味。"
"这与我在学校里那间用摇摇欲坠的旧床和一面有裂纹的镜子装点起来的凄凉房间，实在大相径庭。"

hide image "border" onlayer border
scene celine_room
show celine c neutral:
    xzoom -1 xpos 0.5 xanchor 0.5
with wipeleft_slow

Celine "当然，我在奥尔良的房间比这儿更漂亮，也更宽敞。"
show celine c sigh with dissolve
Celine "我没办法把家具带到这里来。唯一获准搬来的大件，就是那架钢琴。"
show celine c frown with dissolve
Celine "这张床是新的，那张桌子也是，还有那些抽屉。"
show celine c sad with dissolve
Celine "刚来米延那会儿，我怀疑自己这辈子都不会喜欢上这里。一切都是那么陌生、新鲜，又让人不自在。"
Celine "这间房一点也不像我原来的房间，给人一种不近人情的感觉，仿佛我真不属于这里。"
show celine c huh with dissolve
Celine "不过，如今我在米延已经待了一年多，而这所有的一切……"
"塞琳环顾自己的房间，比划了一下。"
Celine "……终于开始让我有家的感觉了。我已经习惯了这张床、那张桌子，还有这些抽屉。"
show celine c frown with dissolve
Celine "这些普普通通的物件，构成了我日复一日的生活。"
Celine "这张是我睡觉的床，那张是我梳头的桌子，而这些抽屉，则是我放衣服、首饰和各色小玩意儿的地方。"
show celine c neutral with dissolve
Celine "可现在，我又担心自己回奥尔良时会认不出从前那间卧室了。恐怕连我的四柱床和衣橱都会变得相当陌生！"
"塞琳笑了，或许是觉得自己的幻想有点好笑，随即摇了摇头。"
show celine c smile with dissolve
Celine "哎呀，听我这么絮絮叨叨。我说得太多了。若让你觉得无聊，我很抱歉。"
Marcel shock c "啊、啊，不！我不觉得无聊！我喜欢听你讲你的过去，很有意思！"
show celine c frown with dissolve
Celine "有意思？真的吗？"
"塞琳抿紧了嘴唇。"
Celine "你确定不是随口敷衍我？"
Marcel smile c "不、不是的，我没有敷衍！我是认真的！我喜欢听你讲过去的生活，哪怕只是一些片段。那……在某种意义上，让我觉得离你更近了。"
"我无法想象塞琳会把这些私密的念头都跟学校里那些女孩分享。她们多半一辈子都住在米延，怕是难以理解她。"
"她们或许无法感同身受，但是……"
Marcel neutral c "我明白你搬到乡下的感受。对我来说那也很别扭，事实上，现在仍是如此。"
Marcel "我还在努力适应这一切。"
Marcel ehe c "知道一切终究会好起来，真让人安心！"
show celine c smile with dissolve
"塞琳笑出声来。"
Celine "好吧，既然我的抱怨能对你有点积极影响，那我想我这口气也不算白费了。"
show celine c neutral with dissolve
Celine "不过，我真是太不体贴了。我请你来这儿，是为了让你摆脱阿梅莉没完没了的喋喋不休，可我自己却做着几乎一样的事！"
Celine "你不想坐下吗？"

play sound "sfx/fall.ogg"
scene celine_room:
    size (1920, 1080) crop (50, 0, 1440, 810)
show celine c smile2:
    xzoom -1 xpos 0.5 xanchor 0.5 ypos 0.50 yanchor 0.5
    ease 0.8 ypos 0.55
with dissolve

Marcel shy c "我想坐，但是……"
"我狐疑地打量着塞琳的床。"
Marcel "我、我怕会把你的床单弄皱……"
show celine c smile2 with dissolve
Celine "哎呀，这你大可不必担心！我晚些时候自己也能把床铺好——或者让阿梅莉来！"
Marcel neutral c "她不会介意吗？"
Celine "当然不会！那是她分内的事。几条皱巴巴的床单，哪值得小题大做！"
Marcel sigh c "那、那好吧……"

play sound "sfx/fall.ogg"
scene celine_room blur:
    size (1920, 1080) crop (220, 0, 1152, 648)
show celine c neutral3:
    xzoom -1 xpos 0.5 xanchor 0.5 ypos 0.55 yanchor 0.5
with dissolve

"我在塞琳身边坐下，刻意不坐得离她太近。"
"整整一整天，我们的手臂与肩膀不时相碰，这给我的精神带来的负担，丝毫不比塞琳那严苛的钢琴课来得少（甚至还要多）。"
"也许这就是我为何如此心神不宁。"
"突然间，我不知该说些什么。我的脑子比塞琳那架宝贝钢琴上的象牙琴键还要空白。"
"沉默在我们之间蔓延开来。"
"也许塞琳对此安然自处，可我却做不到。"
"独处之时，我颇能享受安闲与静谧；可一旦身边有他人相伴，沉默总让我担心自己是不是做了什么、说了什么，得罪了对方。"
"我开始胡思乱想，结果把自己弄得比原本更加焦躁不安。"
"我得找点话来说，可该说什么才好呢？"
"我带着几分绝望，在塞琳的卧室里四下打量，想寻出一个可以聊起的话题。"
"唔……"

show image "border" onlayer border
scene celine_room:
    subpixel True
    size (1920, 1080) crop (0, 100, 1280, 720)
    linear 20.0 crop (350, 100, 1280, 720)
with wiperight_slow

"我四下张望时，目光与另一个人的相遇了。这房间里还有别人，与塞琳和我同在——当然，并非血肉之躯。"
"她的床头柜上放着一张照片。那是一张黑白快照，上面似乎是个年轻人。他面带微笑，却仍透着严肃，或许那不过是悲伤？"
"他的眼睛很深邃，头发也是深色的，对男人来说算长的了。"
"即便映在黑白照片里，他的肤色也显得比大多数人深，这让我忍不住猜想，他的父母一方（或许是祖辈？）是否来自一个比我们这里更温暖的地方。"
"他的下颌轮廓分明而有力，肩膀宽阔。虽没有参照物难以断言，但他看上去个子偏高。"
"我觉得他不如父亲往来的那些演员朋友那般俊朗，但也绝非难看。"
stop music fadeout 2.0
"我好奇他究竟是谁……"

hide image "border" onlayer border
scene celine_room blur:
    size (1920, 1080) crop (220, 0, 1152, 648)
show celine c frown3:
    xzoom -1 xpos 0.5 xanchor 0.5 ypos 0.55 yanchor 0.5
with wipeleft_slow
play music "bgm/Confession.ogg" fadein 1.0

Celine "嗯？"
"塞琳想必看到了我在盯着看，因为她朝那张照片瞟了一眼。"
Celine "你是在猜想这是谁吗？"
Marcel ehe c "有那么明显吗？"
show celine c sigh3 with dissolve
Celine "你完全没有掩饰。你并不擅长藏住自己的真实心情。"
show celine c huh3 with dissolve
Celine "若是你的学校连礼仪课都不教，那可真够奇怪的！在某些方面，你简直就像个乡下丫头！"
Marcel "哦，呃……对不起。我不是故意惹你不高兴……"
show celine c neutral3 with dissolve
Celine "没关系。我没有不高兴。我本该想到你会好奇的。任谁在房间里发现这样一张照片，都会心生好奇。"
show celine c sigh3 with dissolve
Celine "那么，我这就打消你的疑虑。"
show celine c huh3 with dissolve
Celine "那位男士不是我的未婚夫——谢天谢地，我并没有未婚夫！——也绝非别的什么关系。他是我从前的钢琴老师，瓦雷纳先生。"
Marcel "哦，对了。你以前提起过他。"
"塞琳没有详细谈过瓦雷纳先生，但我明显感觉到她对他怀有好感。"
"看她在卧室里摆着他的照片，我想我那个猜测是对的——可这不奇怪吗？"
"塞琳或许敬重瓦雷纳先生的音乐才华，但单凭这一点，我想还不足以让她那样珍藏着这样一张照片。"
"她为什么会有这张照片，为什么每次提起他时，语气都那样怅然若失？"
"我思忖着……"
show celine c sigh3 with dissolve
Celine "请、请别想太多。我留着这张照片并没有什么真正的理由，它也没有什么特别的意义。它、它只是……对我过往的一点念想，仅此而已——就跟那架钢琴一样。"
Marcel neutral c "你确定就这么简单？"
show celine c huh3 with dissolve
Celine "唔、唔，那我留着这么一张照片，还能有什么别的理由呢？"
Marcel "我说不上来。我只是觉得……"
Marcel smile c "你一定喜欢过他。"
show celine c sigh3 with dissolve
Celine "唔、唔，这么说也没错。这事我也没瞒过人。我很喜欢他。"
show celine c neutral3 with dissolve
Celine "我们关系很亲密，不过这也没什么好奇怪的。从我小时候起，他就教我弹钢琴。"
Celine "我难过的时候，他会逗我开心；我的种种烦恼，他都会一一倾听。他是个极好的倾听者。我想，要当一位钢琴老师，大约少不了这份能耐吧……"
show celine c sigh3 with dissolve
"塞琳叹了口气。"
show celine c frown3 with dissolve
Celine "但我们的关系——不管那曾经是怎样一种关系——如今已经结束了。他还在奥尔良，而我身在米延。我怕是再也见不到他了。"
show celine c sad3 with dissolve
Celine "真是遗憾，可是……"
"塞琳伸出手，拿起瓦雷纳先生的照片，双手捧着，指尖温柔地（几乎是爱怜地）绕着相框。"
show celine c sigh3 with dissolve
Celine "……事情就是这样。"
show celine c sad3 with dissolve
Celine "他不再是我生命的一部分了，但那些共度的时光，将永远活在我心里。我不会忘记。"
show celine c frown3 with dissolve
Celine "事实上……这也正是我想重整学校合唱团的部分原因。"
Marcel huh c "咦……？"
"我皱起眉头。"
Marcel "我还以为你重整合唱团是为了勒梅尔小姐。你不是说过你喜欢她吗？"
show celine c sigh3 with dissolve
Celine "我{i}确实{/i}喜欢过她。她是一位非常善良的女士。我想延续她的遗志……"
show celine c frown3 with dissolve
Celine "可我也想令瓦雷纳先生为我骄傲。"
show celine c huh3 with dissolve
Celine "我敢肯定，倘若他在这儿，他绝不愿看到学校合唱团就此瓦解。他会希望有人挺身而出，担负起这份责任，加以引导。"
show celine c frown3 with dissolve
Celine "遇见瓦雷纳先生时，我还是个年轻的姑娘。那时我意志薄弱，又天真幼稚，担不起什么责任；连自己的人生都做不了主。"
show celine c sigh3 with dissolve
Celine "直到我被放逐到米延，这一切才有所改变。"
"我想，这是塞琳第一次把搬到米耶讷称作「放逐」。"
"那一定说明她并非心甘情愿来到这里。想必是她父亲送她来的，可为什么？"
"然而我没有机会追问。塞琳还没说完。她继续说下去，目光却落在镶框的瓦雷纳先生照片上，我弄不清她是在对我说，还是在对他说。"
show celine c frown3 with dissolve
Celine "如今我有机会了，我想证明自己已经改变。我想凭自己的本事做出一番成就，想做些能让瓦雷纳先生高兴的事。"
Celine "我想，无论如何，他都会感到欣慰吧……"
show celine c sad3 with dissolve
Celine "不过这我也说不准。我已经一年多没见过他了。"
show celine c huh3 with dissolve
Celine "我知道，为了我自己，我该放下过去，可是……"
"塞琳用指尖描摹着瓦雷纳先生的面颊。"
show celine c sad3 with dissolve
Celine "无论我多么努力，都无法说服自己放下。"
show celine c sigh3 with dissolve
Celine "我真的很想念他。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  10月3日{vspace=1}  夜之乐章") )
play music "bgm/Night.ogg" fadein 1.0
play ambience "sfx/footsteps.ogg" fadein 1.0
play ambience2 "sfx/night_amb.ogg" fadein 1.0
show image "border" onlayer border
scene village_n:
    subpixel True
    size (1920, 1080) crop (0, 200, 1280, 720)
    linear 20.0 crop (350, 200, 1280, 720)
with wiperight_slow
window show dissolve

"那天傍晚，日落之后，我离开了塞琳的家。"
"我悠闲地穿过村庄，凉爽的风一路扯动着我裙摆的边缘。"
"时已夜深，沿街的店铺都已打烊。"
"四周十分安静，我是这街上寥寥几人之一。"
"米耶讷人烟稀少，从来就不是什么热闹之地，但今天它比以往任何时候都更显荒凉。"
"我没有见到任何认得的人。没有人驻足向我问好，或道一声晚安，而这正合我意。"
"我没有心情与人打交道。"
"我无法不去回想和塞琳一起度过的这一天。"

stop ambience fadeout 1.0
play ambiencee "sfx/footsteps2.ogg" fadein 1.0
scene yard_n:
    subpixel True
    size (1920, 1080) crop (0, 200, 1280, 720)
    linear 20.0 crop (350, 200, 1280, 720)
with wiperight_slow

"我回到学校时，天空漆黑一片，缀满星星。"
"我走进所有寄宿生下榻的宿舍楼，沿着狭窄的楼梯回到自己的房间。"

stop ambiencee fadeout 1.0
stop ambience2 fadeout 1.0
play ambience "sfx/night_amb2.ogg" fadein 1.0
hide image "border" onlayer border
scene cg28
with wiperight_slow

"一进屋，我换上睡袍，然后扑倒在我那张与塞琳的床大相径庭的窄床上，把自己隔绝在一片寂静之中。"
"我今天过得很好；这事实无法否认。"
"我一连好几个小时都陪在塞琳身边。"
"我们一起弹了钢琴（其实是塞琳在弹。我试图模仿她，至于有没有成功就另当别论了），还尝了阿梅莉做的美味苹果派，也把塞琳的家四处看了一遍。"
"她跟我讲了一点她的往事，讲了她那个专横的父亲，以及她是如何爱上钢琴的……"
"她也跟我讲起了第一个让她领略到音乐之美的男人：瓦雷纳先生。"
"我对瓦雷纳先生仍旧所知甚少，除了据说他为人十分和善之外；但塞琳对他的情意却是显而易见的。"
"我想她甚至可能爱慕着他。"
"倘若她不在乎他，就不会在床头柜上摆着他的一张照片了。"
"塞琳没有她父母或两个姐姐的任何照片，可瓦雷纳先生却不一样。"
"她对他的在乎，难道胜过对自己的家人吗？"
"他们两人并无血缘关系。将他们联结在一起的，只有对音乐共同的热爱——但对塞琳而言，这或许已经足够了。"
"据我了解，她的父亲严厉而专断，母亲在她的生活中几乎缺席。她的两个姐姐我知之甚少，但塞琳说，她们都把她当孩子看待。"
"我想塞琳并不讨厌她的家人，但我也觉得她跟他们算不上亲近。"
"正因如此，阿梅莉才用那样母亲般的亲切对待塞琳。她是在填补塞琳母亲缺席留下的那个空缺。"
"如果阿梅莉是塞琳的代理母亲，那么自小就认识塞琳的瓦雷纳先生又算是什么呢？"
"他会不会，或许，算是个父亲般的人物？"
"这并非不可能——尤其考虑到瓦雷纳先生一定比她年长许多——但我不这么认为。"
"如果塞琳把瓦雷纳先生当作父亲，我想她望着他的照片时，不会那样叹息。"
"我想知道塞琳和她的音乐老师之间到底发生过什么，因为显然，确实发生过什么。一定发生过。"
"不过，我不知道自己有没有资格去探问。"
"发生过的事想必极为私密。我担心，如果我去追问塞琳，她会疏远我。"
"那样的话，我们的友谊就会分崩离析。"
"我向阿梅莉说过，我会尽力照顾塞琳。既然许下这样的承诺，我就不能再去触动她旧日的伤口。"
"若要做她真正的好友，我就要懂得在什么时候缄口不言。"
"这其实与我无关……"
"可是，当我回想起塞琳谈起瓦雷纳先生时的语气，一阵尖锐的痛楚便在胸口骤然升起。我无法将它压回去。"
"我不禁思忖……"
"我该不会，竟然，是在吃醋吧？"

stop ambience fadeout 1.0
stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene sky_s g
with clockwipe
$ renpy.pause(0.5)
show overlay2
show message12 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message12
hide logo2
hide overlay2
with datetrans2

$ renpy.pause(0.3)

$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  11月16日{vspace=1}  行动时刻") )
play music "bgm/Oh Holy Night.mp3" fadein 1.0
scene sky_s with dissolve
window show dissolve

"时光一如往常地流逝。日子变成星期，不知不觉间，一个多月已经过去了。"
"在这段时间里，我全心投入钢琴。每天放学后，我都和塞琳在琴房练习；周末则在塞琳家的客厅里练。"
"随着季节的更替，我在钢琴上的造诣也日益精进。"
"尽管无论如何我都还算不上专业（我在许多方面仍有所欠缺），但我确实进步了。"
"多亏塞琳的指导，我如今能看懂乐谱了，也能演奏一些简单的曲子，手指不再那么慌乱纠缠。"
"我仍会出错，这也在意料之中，但比起十月初已经好太多了。"
"我对自己的成果心怀谨慎的欣喜——看样子，塞琳也是如此。"

scene musicroom_s blur:
    size (1920, 1080) crop (250, 60, 1152, 648)
show celine smile3 s:
    ypos 0.55 yanchor 0.5 xpos 0.5 xanchor 0.5
with wipedown_slow

Celine "干得好，玛塞尔！真是太精彩了！"
Marcel shy u "你、你确定？"

stop music fadeout 1.0

"我让《{i}O Holy Night{/i}》的最后一个音符渐渐归于沉寂，然后转头望向那位坐在钢琴旁、我的老师。"

play music "bgm/Friendship.ogg" fadein 1.0

"在我们最初上课时，每当我出错，塞琳常常不得不打断我，好重新摆正我的双手，或是亲自弹奏那些艰涩的段落来加深我的理解；但最近一周，她出手的次数越来越少了。"
"今天我们练习的最后一个小时里，她一次都没有打断过我。"
"那一定说明我确实进步了。"
"关于自己的长进，我已有充分的证据，可即便如此，我仍难以全然相信。"
Marcel "你不觉得我弹得有些过于迟疑了吗？"
Marcel "我知道自己也犯了几个错……"
show celine neutral3 s with dissolve
Celine "你确实还有进步的空间，这点不假，但我想大多数人根本注意不到这些错误。"
Marcel sad u "不过，{i}我{/i}却注意到了。"
show celine huh3 s with dissolve
Celine "我知道你注意到了。若是你察觉不到，我反倒要担心了！不过，你能够认清自己的不足，我认为这反而是件好事。"
show celine smile3 s with dissolve
Celine "人无完人。我们要从错误中汲取教训，而不是为它们低落消沉。唯有如此，我们才能进步！"
show celine neutral3 s with dissolve
Celine "你之所以会注意到这些错误，是因为你清楚这首曲子本该弹成怎样。旁人可不会这么苛求。"
Marcel huh u "这可不好说。{i}O Holy Night{/i}是一首家喻户晓的圣歌……"
show celine huh3 s with dissolve
Celine "不管熟不熟悉，大多数人聆听时远没有你想象的那般用心。只有你完全停下来不弹，别人才会看出你出了错。"
show celine smile3 s with dissolve
Celine "只要你继续弹下去，并装出一副笃定的样子，旁人便绝不会察觉！"
Celine "你得学会如何戴上这副面具。任何表演，有一半都是虚伪做作！"
Marcel "任何表演，嗯……"
"我想起父亲似乎也说过类似的话，那是我问他怎能一字不差地记住所有台词的时候。"

window hide dissolve
scene black with circleirisin
window show dissolve

Dad "{i}马塞尔，像你这般一丝不苟的孩子，听到这话怕是要吃惊——可我并不是什么绝无纰漏的人！{/i}"
Dad "{i}我不过是个凡人，和常人一样也会犯错。然而，让我与众不同的，是我随机应变的本事！{/i}"
Dad "{i}嘿，就在昨晚，我还把罗密欧的台词念错了好几句，可我会因此停下吗？不，我没有！{/i}"
Dad "{i}我依旧是满怀自信地演了下去，我相信剧院里没人察觉出任何不对劲：即便是那些自诩为莎翁信徒的人也不例外！{/i}"
"当时我以为，父亲只是又摆出他一贯放任不羁的态度；可现在塞琳印证了他的话，他那番话便有了新的分量。"
"或许，咬牙坚持确实有它的道理。正如人们所说的，戏还得继续演下去。"
"尽管如此……"

window hide dissolve
scene musicroom_s blur:
    size (1920, 1080) crop (250, 60, 1152, 648)
show celine smile3 s:
    ypos 0.55 yanchor 0.5 xpos 0.5 xanchor 0.5
with circleirisout
window show dissolve

Marcel frown u "这么说来，岂不是显得所有演员都是江湖骗子？"
show celine huh3 s with dissolve
Celine "或许其中确实有几分道理，嗯……"
show celine neutral3 s with dissolve
Celine "但你不该用这么非黑即白的方式去思考。别一门心思追求完美，否则你只会僵住。那样你谁都讨不了好，更别提令自己开心了。"
Celine "你只需要像现在这样，尽心尽力就好。"
show celine huh3 s with dissolve
Celine "事实上……"

scene musicroom_s
show celine neutral s:
    xpos 0.5 xanchor 0.55 ypos 0.56 yanchor 0.5
    ease 0.6 ypos 0.53
with wipeup_slow

"塞琳从琴凳上站起身，伸了个懒腰，双臂像舞者一般舒展。"
Celine "……我想，我们或许已经准备好重整学校合唱团了。"
Marcel shock u "您真的这么觉得吗？"
show celine frown s with dissolve
Celine "我们必须尽快开始考虑这件事了。"
Celine "很快就要到十二月了。圣诞音乐会总是在24日举行。"
show celine sigh s with dissolve
Celine "如果我们想把这变成现实，就得从现在开始恢复排练。否则，我们会赶不上的。"
show celine frown s with dissolve
Celine "你可以弹钢琴，我就试着来指挥。我会带着姑娘们做热身，也会尽量在出了岔子时指出来。"
show celine sad s with dissolve
Celine "我想我没办法一边弹琴一边教人……"
show celine smile s with dissolve
Celine "但有你在身边，应当能帮我大忙。有你的支持，我相信自己一定能在音乐会前把一切筹备妥当！"
Marcel sad u "你能这么信任我的技艺，我很高兴，但是……"
"我回头望向那架钢琴。"
"那黑白琴键，曾经显得那样高深莫测、不近人情，在这过去的一个月里，竟几乎开始像老朋友一般熟悉了……"
"可是，即便我现在能弹奏一些简单的曲子，我仍不确定这够不够。"
Marcel sigh u "可我还是个新手。若是让我当你的伴奏，我怕会拖累你。"
Marcel "我想我需要更多时间。"
show celine frown s with dissolve
Celine "这一点我不与你争辩，因为确属实情。你{i}确实{/i}需要更多时间，可我们没有那么多时间可以挥霍。"
show celine sigh s with dissolve
Celine "这场圣诞音乐会对我很重要。我想让勒梅尔小姐为我骄傲——也想让瓦雷纳先生同样为我骄傲。"
show celine huh s with dissolve
Celine "在我教同学们的时候，你可以趁机学着怎样把钢琴弹得更好。我们还有一个月的时间。你会进步的。"
Marcel shy u "那要是没有进步呢……？"
show celine smile s with dissolve
Celine "别这么操心！从过去的经历也能看出，你是个学得很快的人。我确信不会有问题。"
show celine huh s with dissolve
Celine "我会带着同学们一遍又一遍地练那同样的十首圣歌。你只需弹这些就够了，别的都不用碰。"
show celine neutral s with dissolve
Celine "光是这般反复练习，就足以把它们牢记在你心里。很快，你连乐谱都不必借助了。"
show celine smile s with dissolve
Celine "我们会练得又久又刻苦，直到你闭上眼睛都能弹奏这些曲子！"
"我自己也不是那么有把握，但塞琳看起来那样坚定，我不愿挫了她的兴致。"
"我与她，在这过去的一个月里已走了很远。我答应去上她的课，是为了帮她实现梦想。若此刻在压力下垮掉，我就实在不配做她的朋友了。"
"我对这一切仍心怀犹豫（我总是回避尝试新事物），但只要这能让塞琳快乐，我就能忍受。"
"我必须如此。"
Marcel neutral u "哦，那好吧。既然实在别无选择，那我就……当你的伴奏吧。"
Marcel "我不敢保证自己不会出任何差错——"
"那是不言而喻的事。"
Marcel smile u "——但我会试试的。"
show celine neutral s with dissolve
Celine "那也就是我所能要求的全部了。谢谢你，玛塞尔。"
show celine huh s with dissolve
Celine "好了，我站在这里畅谈未来的计划固然很好，但如果没有先得到布吕吉埃夫人的许可，这一切都只是空谈。"
Celine "没有她的同意，我们就无法重组合唱团，所以我们必须和她谈一谈。"
Marcel huh u "现在？"
show celine frown s with dissolve
Celine "{i}是的{/i}，就是现在。{i}必须{/i}是现在。"
Celine "我们的时间不多了。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  11月16日{vspace=1}  深情的恳求") )
show image "border" onlayer border
play music "bgm/Casual_day.ogg" fadein 1.0
scene office_s:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow
window show dissolve

"在米耶讷度过的这两个月里，我一次都没有去过布吕吉埃夫人的办公室。"
"克洛蒂娜已经去过多回了，可我远没有她那么顽劣。我上课专心听讲，也尽量不去招惹我姨母生气。"
"因此，她办公室的内部于我而言是个谜——可我很快发现，那里与我想象的大相径庭。"
"我以前学校的校长办公室是个很大的房间——我想，比它实际需要的还要大——里面摆着一张气派的红木书桌和高背椅。"
"地上铺着豪华的红色地毯，宛如高档酒店里的陈设，墙上则挂满了镶框的文凭与奖状。"
"在旧学校时，我进过校长办公室好多回。我总是惹上麻烦——当然，并非出自我的本意。"
"我仍记得自己如何在那个办公室里垂着头等待校长裁决，而那裁决总是把我描绘成自己种种苦难的罪魁祸首。"
Headmaster "{i}这全都是你的错，圣雷米。{/i}"
"校长总会这样说，同时在那张冷峻的书桌后审视着我。"
Headmaster "{i}如果别的男孩取笑你，那是因为你没有试着融入他们。你那些古怪的举止，让你自己成了靶子。{/i}"
Headmaster "{i}我实在不能责怪我的学生们去挑逗你。事实上，我认为这对你或许有些好处。让我们希望，随着时间推移，这会教会你如何更好地融入体面的社会！{/i}"
"我并不觉得被踢小腿、被推下楼梯是什么「礼貌」之举，但校长在这件事上的立场始终坚定不移。"
"欺辱我的同学从未受过责罚。我总被认定是过错一方。"
"从前去旧校长办公室总要以这样那样的倒霉收场，这让我对踏进布吕吉埃夫人办公室这件事更加心生抗拒。"
"所幸，她的办公室没有旧校长那般的排场与浮华。"
"她的办公室狭小而朴素。墙上没有任何文凭，也没有玻璃柜里陈列的奖杯。"
"靠墙摆着几座书架，塞满了翻旧了的书籍，窗台上点缀着几盆盆栽。就装饰而言，大致也就如此了。"
"布吕吉埃夫人本人正坐在书桌后。她正埋头翻阅一本厚厚的硬面账簿，但当我和塞琳走进来时，她停了下来。"

hide image "border" onlayer border
scene office_s
show celine frown s:
    xzoom -1 xpos 0.30 xanchor 0.5 ypos 0.53 yanchor 0.5
show al shock s:
    xpos 0.70 xanchor 0.5
with wipeleft_slow

Bru "天哪！我没料到会在这里见到你们俩——还来得这么迟！"
show al annoyed s with dissolve
Bru "你们为什么不敲门？你们应该知道，未经女士明确许可就闯进她的房间是多么失礼。"
show celine sigh s with dissolve
Celine "我们敲过门了，可您没有应声。"
show al frown s with dissolve
Bru "那就更说明你们应该等着——或者，干脆离开更好！"
show al sigh s with dissolve
Bru "我知道你们这些女孩不懂得我为维持这所学校所做的一切——你们又怎么会懂呢？你们不过是孩子！——可我现在实在是忙得很。"
show al annoyed s with dissolve
Bru "我没有时间，也没有耐心去理会你们的要求，无论那是什么。"
show al sigh s with dissolve
Bru "好了，出去！去去去！"
"布吕吉埃夫人朝我这个方向不耐烦地挥了挥手。"
"我拘谨地退到一旁，双手在身前交叠着。"
"布吕吉埃夫人还没吩咐我给网球拍换线，我只能把这当作一个好消息，可她见到我们时看上去并不太高兴。"
"我不想烦扰她，更不想让她与我为敌。我宁可把她当作盟友。"
Marcel shy u "或-或许我们该走了，塞琳。我们可以改天再说……"
show celine frown s with dissolve
Celine "不，我{i}绝不{/i}离开，我也绝不会把这件事拖到改天。我不能。这事太重要了！"
show al frown s with dissolve
Bru "哦？"
"布吕吉埃夫人皱起眉头。"
Bru "这实在太不像你了，塞琳。你一向都是那么乖巧。"
show al annoyed s with dissolve
Bru "我本以为这种胡闹会来自克洛蒂娜，可你？这实在有违你的性情。你确定自己感觉还好吗？"
show celine sigh s with dissolve
Celine "我很好，谢谢您。"
show al sigh s with dissolve
Bru "那好！既然你像你说的那样好，那你必定明白，我不容许任何不服从。"
show al annoyed s with dissolve
Bru "我是你们的校长，塞琳，你必须以配得上我的年龄与职位的敬意来称呼我！"
Bru "现在，马上离开。你也是，玛塞尔。我不希望你卷入任何不愉快的事。你的母亲会失望的。"
"这一招可真是够下作的。"
"我知道我姨母定期给母亲写信，信里满是关于我近况的汇报，以及我一切安好的安慰。"
"我不愿去想，若母亲知道我惹了麻烦，会说些什么。"
"我不想让她难过……可我也不想让塞琳难过。"
show al neutral s with dissolve
Bru "怎么？你们这些女孩没听见我方才说的话吗？我更希望清静一些。"
show celine annoyed s with dissolve
Celine "可-可您根本不知道我们想要的是什么！"
show al annoyed s with dissolve
Bru "你们可以明天再告诉我。我的办公室还会在这里，我也一样。就我所知，世界末日还没降临——除非你们俩最近受到了上帝及其天上使者的拜访？"
show celine huh s with dissolve
Celine "没有，我们没有……"
show al sigh s with dissolve
Bru "那么，我真想不出你们要说的话能有什么要紧。"
show celine annoyed s with dissolve
Celine "可-可这{i}确实{/i}很重要！这不只是关于我！这关系到学校的合唱团！"
show al annoyed s with dissolve
Bru "哦……？"
"听到这话，布吕吉埃夫人坐得更直了一些。她的目光先落在我身上，随即转向塞琳。"
show al sigh s with dissolve
Bru "你在说什么？你比谁都清楚，学校的合唱团已经无法运转了。"
Bru "我们失去了音乐女教师，而我眼下既没有时间，也没有经费去另觅人选。没有她，合唱团便无法继续。它能维持至今，全靠勒梅尔小姐。"
show celine huh s with dissolve
Celine "您也许会这么想，但您忘了点什么！勒梅尔小姐并不是学校里唯一有音乐背景的人！"
show celine frown s with dissolve
Celine "我也会弹钢琴！我不介意代替她！"
show al neutral s with dissolve
Bru "啊。原来是为了这个。"
Bru "你是说，让我们重组学校合唱团，由你接替勒梅尔小姐的位置？"
show celine frown s with dissolve
Celine "大意正是如此，是的。我想我能做到。您一定也同意吧。若您不同意，就不会让我在音乐课上为同学们伴奏了！"
Celine "合唱团是我们校史中重要的一部分。它已经存在了许多年，至少我是这么听说的。"
Celine "它在勒梅尔小姐来到这所学校之前就已存在，所以我不明白为什么她的离去就该让它终结。"
show celine annoyed s with dissolve
Celine "它可以改由学生们来经营。那样，它的传承就能延续下去！我想这会让大家都高兴！"
show al sigh s with dissolve
Bru "唔……"
"布吕吉埃夫人有片刻没有回答。她只是抱起双臂，皱起眉头。"
"我想，在她开口之前，我就已经知道她的裁决会是怎样了。"
"情况看来不妙。"
show al neutral s with dissolve
Bru "我想，至少我得称赞你的热情。"
Bru "你确实是个有才华的钢琴手。我自己对音乐所知不多——我年纪够大了，也承认自己的不足！——但在我看来，你显然有着丰富的才艺。"
show al sigh s with dissolve
Bru "若由你来挑大梁，重组学校合唱团也许并非不可能……"
show al annoyed s with dissolve
Bru "但对于你的这个计划，我仍心存疑虑。"
show celine shock s with dissolve
Celine "什么？可为什么？！"
show al neutral s with dissolve
Bru "把如此沉重的责任压在一个女孩肩上，实在太多了。我怕这也会耗费你大量的时间。"
Bru "我不希望你因为忙于管理学校合唱团，而使学业被搁置一旁。"
show al sigh s with dissolve
Bru "你正处于学业的最后一年。这对你来说是个非常关键的时期。我绝不能让你考试不及格！"
Celine "我不会考砸的！合唱团和我的考试，我{i}都{/i}能兼顾！"
show al annoyed s with dissolve
Bru "你现在这么说，但我自认是个公正的识人者，我了解你的为人。你太追求完美，绝不会半途而废、草草了事。"
Bru "你要么全身心地投入合唱团，学业因此受损；要么在两件事上都倾注太多精力，最终把自己累垮。"
show al sigh s with dissolve
Bru "这两种结局都不算理想。"
show al neutral s with dissolve
Bru "你必须明白自己的处境，塞琳。你的成绩是全校最顶尖的。你是我们的一笔财富。我输不起让你考试失败，否则那将有损于这所学校的名声。"
show al annoyed s with dissolve
Bru "督学会来嗅探风声，经费甚至可能被削减——而为了什么呢？就为了让你放任自己年少的心血来潮？"
show al frown s with dissolve
Bru "很抱歉，但我必须拒绝。合唱团不会重组。"
show celine sad s with dissolve
Celine "什-什么？可是，这不公平……！"
show al annoyed s with dissolve
Bru "生活本就不公平。好了，这就是你想说的全部了吗？"
Celine "我……我只是……"
"塞琳垂下了头。她的脸色苍白，双手无力地垂在身侧。"
"她方才还那样气势汹汹地闯进布吕吉埃夫人的办公室，如今却像败下阵来一般。"
"一股同情如泉水般在我心底涌起。"
"我比任何人都明白这对她有多么重要。她一直为学校合唱团的缘故而辛勤付出。我不愿她的努力此刻被轻易抹杀。"
"我并不是个很勇敢的人，也不喜欢冲突；尤其是与家人的冲突。要牵起塞琳的手，领她走出布吕吉埃夫人的办公室，对我来说轻而易举。"
"我本可以与她一同为我们的失败而黯然神伤，然后我们的校园生活照常继续……"
"但那并非塞琳所愿。"
"我也不认为那是我想要的。"
"我付出了这么多练习，可不是为了让我们的请求被无视！"
Marcel shock u "布-布吕吉埃夫人，请您听我说！还没说完！"
show al shock s with dissolve
Bru "您这话是什么意思？"
"布吕吉埃夫人眨了眨眼。"
show al neutral s with dissolve
Bru "对这件事，你有什么要说的吗，玛塞尔？"
Marcel neutral u "是的，我有。您看……"
Marcel frown u "塞琳并不是这学校里唯一会弹钢琴的人。"
Marcel "她辅导我已经一个多月了。我远不如她，但我知道的也够多，勉强能磕磕绊绊地弹几首赞美诗。"
Marcel neutral u "我明白要塞琳同时担任伴奏和指挥是很难的，所以我想或许我可以帮帮她。"
Marcel "我们俩商量过这件事，我已经答应要助她一臂之力。"
Marcel huh u "塞琳不会成为合唱团唯一的负责人。我们可以分担工作，我可以支持她。那样事情会轻松得多！"
show al sigh s with dissolve
Bru "嗯……"
"沉默再度笼罩。布吕吉埃夫人困惑地在我们两人之间来回打量。"
show al neutral s with dissolve
Bru "你确定吗？"
Marcel shock u "是的，我确定！"
show al annoyed s with dissolve
Bru "真的吗？我得说，这实在出人意料。我从来不知道你对音乐有任何好感，也不知道你会演奏乐器！"
Bru "你是出于自愿才这么说的，对吧？"
Marcel "当-当然是自愿的！我想帮塞琳，因为我是她的朋友！"
show al frown s with dissolve
Bru "我倒是有些好奇……"
"布吕吉埃夫人皱起了眉头。"
Bru "这话出自你之口，实在很反常。"
show al annoyed s with dissolve
Bru "从与你母亲的交谈中，我知道你不是那种爱出风头的人。"
Marcel sad u "也许我不是……但我也不能一辈子都活在阴影里。如果我总是退缩不前，就永远也做不成任何事！"
Marcel sigh u "我承认，起初我对这件事有些犹豫……"
Marcel smile u "但在与塞琳相处之后，我明白了弹钢琴是件很有趣的事。"
Marcel neutral u "我这么说并不全是为了塞琳。这也是为了我自己。"
Marcel huh u "我这辈子头一次，想要在某件事上竭尽全力！我想看看自己能做些什么……我想做成一件能让自己引以为傲的事！"
Marcel "您能给我这个机会吗？"
show al sigh s with dissolve
Bru "天哪……"
"布吕吉埃夫人摇了摇头。"
Bru "我从没听过你这样热切地说话！"
show al neutral s with dissolve
Bru "我想我必须为先前那些怀疑表示歉意。我能看出你对这件事很认真……{w}但我还不会就此让步。"
show al smile s with dissolve
Bru "不如弹一首你们一直在排练的曲子给我听听？"
Bru "如果你能毫无差错地弹完一首赞美诗，那我就考虑你的提议。"
show celine shock s at bounce
Celine "哦，夫人！您要给我们一个机会吗？"
show al neutral s with dissolve
Bru "听了这么多之后，我认为若不给你们一个机会，反倒是我的失职。"
Marcel shy u "可您刚才听起来那么严厉。我还担心永远无法说服您……"
show al sigh s with dissolve
Bru "我若显得严厉，那是因为我心情不好。埋头算上一个小时的账目，即便最温和的人也会如此。"
show al smile s with dissolve
Bru "现在，我气已经消了些，有件事我希望你们俩知道。"
show al neutral s with dissolve
Bru "无论你们怎么看我，我都不想扼杀学生们的志向。如果重组合唱团真像你们说的那么重要——"
show celine huh s at bounce
Celine "哦，这对我{i}确实{/i}很重要！{i}非常{/i}重要！"
Bru "——那么你们就该能展示一下你们新学的本领。"
show al smile s with dissolve
"布吕吉埃夫人浅浅一笑。"
Bru "我得说，我很期待。请别让我失望。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  11月16日{vspace=1}  夕阳奏鸣曲") )
scene cg22 with wiperight_slow
play music "bgm/Oh Holy Night.mp3" fadein 1.0
$ renpy.pause(0.8)
window show dissolve

Bru "好了，玛塞尔。你准备好了吗？"
Marcel "我，呃……我想是准备好了……"
"我坐在学校琴房那架破旧的钢琴前，目光聚焦在黑白琴键上。"
"从与塞琳的课上学到，钢琴有五十二个白键和三十六个黑键。有些钢琴多一些，有些少一些，但八十八键是一架标准钢琴最常见的键数。"
"黑键以两个、再三个为一组排列。你可以借助黑键那纤瘦窄小的位置，来辨认各个白键。"
"凡是成双的黑键，其正左侧一定就是C。然后音阶依次递进为D、E、F、G、A、B，再回到C。"
"我知道这键盘上所有音符的位置，也知道如何将它们与乐谱上的记号一一对应。"
"只要我懂得这些，应该就没问题。我做得到。"
"我从未在听众面前弹奏过。这是第一次，除了塞琳以外的人将要听我演奏。"
"我有些紧张，但我努力按捺住不安。"
"我在布吕吉埃夫人的办公室里发表了那样慷慨激昂的一番话，若此刻半途而废，可就太丢人了。"
"我闭上双眼，深深吸了一口气。双手悬在琴键上方。"
"曾经，这一排排黑白琴键看起来简直难以逾越。我心想，像我这样笨拙的人，要从冰冷无情的象牙中引出乐音，是绝无可能的。"
"如今我知道自己错了。世上并无所谓「不可能」。只要我下定决心，连我也能有所成就。"
"我睁开双眼……然后，我开始弹奏。"
"我决定演奏那首脍炙人口的圣诞圣歌《{i}圣善夜{/i}》。这正是我先前排练的那支曲子，后来被塞琳提前结束了课程。"
"我弹奏的这版是供初学者使用的简化版。速度相对缓慢，也不需要什么花哨的指法。"
"根据乐谱，它以E音开始，然后转到G，再转到A……"
"这些音符是八分音符，所以只须按住半拍。还有稍长的四分音符，以及更长的二分音符……"
"曲子我已弹到一半。我不得不专注于乐谱，以免出错，可我仍旧忍不住想要低头看向琴键。"
"我担心，若不时刻保持警觉，我便会出错。"
"我痛苦地意识到，布吕吉埃夫人的目光正灼灼地刺向我的后背。她一定在评判我。"
"她或许对音乐一窍不通，但这首歌广为人知。我们在音乐课上唱过好几次。若我弹错几个音符，她定能察觉！"
"琴房里很是凉爽，但我的掌心却沁出了汗。"
"我觉得那个键或许按得久了一点，而且——哦！那个音符本该是B，不是C！我弹错了！"
"我心中有一部分想要停下来重新开始，但那只会让我的错误比现在更加明显。"
"正如塞琳所说，大多数人的听力远没有想象中那么敏锐。只要不让信心动摇，掩盖失误其实很容易。"
"我从未有过多少自信，但我仍会尽力而为。如今，这支曲子我几乎要弹完了。"
"我奏完了曲子的最后几个音符。《{i}圣善夜{/i}》的余音渐渐消散。随即，我将双手从琴键上移开。"

stop music fadeout 3.0

"我喘着粗气。掌心滑腻腻地满是汗水，双肩也在颤抖。"
"我不过弹了短短几分钟，甚至可能连几分钟都不到，却已感到筋疲力尽。简直是跑完了一场马拉松。"
"我从不知道音乐竟能如此强烈。"
"我一直对塞琳的技艺心生敬畏，但我想如今对她又多了一份崭新的敬佩。她竟能在全班面前弹奏那么多比这复杂得多的曲子，实在了不起！"
"她真的很了不起。"
"每当我拿自己与塞琳相比，就忍不住感到沮丧，尽管我知道这很愚蠢。我们总得从某个起点出发。"
"我只希望我已经做得足够证明自己。"

play music "bgm/Friendship.ogg" fadein 1.0
scene musicroom_s:
    size (1920, 1080) crop (240, 40, 1440, 810)
show al neutral2 s:
    xpos 0.5 xanchor 0.5 ypos 0.5 yanchor 0.5
with wipeup_slow

Marcel shy u "那么，呃……您觉得怎么样……？"
"我害羞地瞥了姨妈一眼。"
"我不敢听她的评价。我比任何人都更清楚地知道，自己的演奏并不完美。我犯了好几个错误，还抖得像一片风中的落叶。"
"我的琴艺仍有不足。"
"即便布吕吉埃夫人对我的努力不予认可，我也丝毫不会意外。若不是那样做实在太过自我否定，大概连我也会轻视自己，但令我宽慰的是……"
show al smile2 s with dissolve
Bru "天哪。"
"姨妈看上去一点也不失望。"
"事实上，她脸上反而挂着微笑。"
show al neutral2 s with dissolve
Bru "你说你一直在练习时，我还心存怀疑，但现在我明白我不该质疑你。你弹得棒极了！"
Marcel "哦-哦，不，呃……真的没什么。我有点紧张，出了几个错。这并非您要求的那种毫无瑕疵的演奏。我-我很抱歉……"
show al shock2 s with dissolve
Bru "你出错了吗？我都没察觉！"
show al smile2 s with dissolve
Bru "现在，你为什么要道歉？别低着头。我认为你做得很好。"
Marcel shock u "真-真的吗？"
Bru "真的！你实在很有才华！"
"姨妈向我露出宽慰的微笑。"
Bru "如果你的母亲在这里，我相信她会为你骄傲！并非每个家庭都能夸口说自家有一位有音乐才华的女儿！"
Marcel "您-您过奖了。我们都知道塞琳比我强得多。"

scene musicroom_s
show celine frown s:
    xzoom -1 xpos 0.30 xanchor 0.5
show al neutral s:
    xpos 0.70 xanchor 0.5
with wipeleft_slow

Celine "也许我是比你强，但那是意料之中的。我从小女孩起就开始弹钢琴了。你才学了一个多月，要是比我还强，那才奇怪呢！"
"我想塞琳说得没错。她并非天生就擅长弹琴。没有人天生就会。她的技艺是多年磨砺出来的，从很小的年纪便已开始。"
"以我现在的样子，根本无法与她相比——尽管我想，这从一开始就谈不上什么较量。"
show celine huh s with dissolve
Celine "请不要拿自己和我比。你应该专注于你自己的旅程，看看你已经走了多远。"
show celine smile s with dissolve
Celine "我觉得你做得很好！"
show al smile s with dissolve
Bru "我同意。"
Bru "现在我明白你们俩对这件事有多认真了。你们都付出了许多努力。"
show al sigh s with dissolve
Bru "我不敢说我完全懂得学校合唱团的吸引力何在……"
show al smile s with dissolve
Bru "但如果它对你们如此重要，那么即便这请求来得突然，不顺从你们的请求也是我的失职。"
Marcel shock u "诶-诶？ "
"我震慑地望着布吕吉埃夫人。"
"姨妈就像我的母亲。她们都很固执。我没想到她会这么痛快地松口。"
"尽管我在她办公室里说了那番大胆的话，我却早已做好了被拒绝的准备，因此面对这个结果，我一时有些难以接受。"
"这感觉太不真实。"
Marcel huh u "这-这真的可以吗？您真的让我们重组学校合唱团吗？"
show al neutral s with dissolve
Bru "是的，的确如此。塞琳可以负责，你可以做她的助手。只要你们仔细分配好各自的职责，这应当完全是可以应付的。"
show al annoyed s with dissolve
Bru "眼下我先信任你们……"
show al frown s with dissolve
Bru "但是，如果你们的课堂表现下滑，我会毫不犹豫地再次解散合唱团。我以前这么做过，若我认为必要，我还会再这么做一次。"
Bru "我明白音乐是慰藉灵魂的良药，但它不会、也永远不会比学业上的造诣更为重要。"
show celine huh s at bounce
Celine "哦，布吕吉埃夫人！非常感谢您——说真的，您实在不必为我操心！"
Celine "我会兼顾好自己的学业，也会时刻留心学校合唱团的孩子们！"
show celine smile s with dissolve
Celine "我会全力以赴，我相信玛塞尔也会的！"
Marcel huh u "哦——哦，好。我会，嗯……我会努力试试的！"
"近来我似乎老是这样说。"
"为了塞琳，我开始练习音乐，还不得不去说服布吕吉埃夫人。如今，我要协助塞琳管理学校的合唱团。"
"我不得不应付一大堆琐事，但远没有我原先预想的那样介意。"
"事实上，这几乎称得上是一种乐趣。"
"过去，一旦事情不顺，我便索性放弃。我心想，无论怎样努力去交朋友或融入其中都毫无意义。我知道同学们永远不会接纳我，无论我做什么。这一点他们表现得再明白不过。"
"我疲惫不堪，实在没有心力再去为那些鄙视我的人付出任何努力。"
"可如今不一样了。"
"我非常在乎塞琳，希望她能实现自己的目标。为了做到这一点，我必须以前所未有的劲头去努力。"
"无论发生什么，我都会全力以赴。"

stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene sky3 g
with clockwipe
$ renpy.pause(0.5)
show overlay2
show message28 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message28
hide logo2
hide overlay2
with datetrans2

$ renpy.pause(0.3)

$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  11月17日{vspace=1}  塞琳的宣告") )
play ambience "sfx/wind.ogg" fadein 1.0
scene sky3 with dissolve
window show dissolve

"次日清晨寒气逼人。我费了极大的意志力才从床上爬起来，用来洗脸的水冷得刺骨，比冰还要凉。"
"我以冻得麻木、笨拙不灵的手指穿衣。裙子的纽扣总跟我作对，屡屡从指腹下滑脱。把袜子往腿上拉同样费劲，我险些站不稳。"
"而打理头发，则是一项浩大得简直堪比赫拉克勒斯十二功绩的壮举。"
"我的手指麻木得厉害，编辫子费了好一番工夫。辫子在我手中散开了好几次，我只好把一切梳开，从头再来。"
"在那面裂开的镜子前，我花了至少十五分钟的专注功夫，才勉强把头发摆弄出个大致像样的发型，可即便如此，我对结果仍不满意。"
"我的辫子歪歪扭扭。一边比另一边更粗，松脱的发丝已经开始从发绳间散落出来。"
"我看起来并不怎么像个淑女，但眼下也只能如此将就了。"
"我绝不能上课迟到：偏偏今天不行，今天最不能迟到。"
"我匆匆走出房间，然后拖着步子下楼，来到餐厅。"

play music "bgm/Classroom.ogg" fadein 1.0
stop ambience fadeout 1.0
play sound "sfx/door.ogg"
scene diningroom
show luce neutral:
    xpos 0.5 xanchor 0.5 ypos 0.55 yanchor 0.5
with wipedown_slow

"我原本担心迟到，结果却是到得最晚的那一个。"
"这严寒的天气想必击垮了我其他的同学，因为到场的只有寥寥几位女生：其中便有露丝。"
"露丝心不在焉地拨弄着早餐。一只手把小块面包送向嘴边，另一只手则攥着一本皱巴巴的平装书。"
"她在读什么？能让她如此入迷，想必是本好书。"

scene diningroom:
    size (1920, 1080) crop (240, 40, 1440, 810)
show luce neutral2:
    xpos 0.5 xanchor 0.5 ypos 0.55 yanchor 0.5
with dissolve

"我好奇地朝封面探过头去。上面写着什么呢……？"
Marcel neutral u "马拉美？"
"我一定是不小心说出了声，因为露丝放下了书。她的目光与我对上，那双浅淡的眼睛里满是挑衅的意味。"
show luce frown2 with dissolve
Luce "没错。有什么问题吗？"
Marcel shock u "哦——哦，没有！我只是好奇而已……"
show luce sigh2 with dissolve
Luce "那就别好奇。好奇害死猫。"
Marcel ehe u "我——我希望这话不是威胁……"
"露丝是个安静的姑娘。她上课从不举手回答问题，也只在别人同她说话时才开口。"
"我完全不知道她脑子里在想些什么。说不定她当真在盘算着要杀掉我（以及其余同学），而我也毫不知情。"
Luce "……"
"她目不转睛地盯着我看了好一会儿。我不禁猜想，她是否正以千百种不同的方式在心里诅咒我去死。"
"这样纤弱的姑娘，却着实令人不安。"
"最终，我不得不移开目光。手指紧紧攥住盛食物的餐盘，垂下眼帘望向地面。"
Marcel sad u "对不起，如果我打扰到你了，我可以坐到别处去……"
"又不是没有空位。"

show image "border" onlayer border
scene diningroom
with wipeleft_slow

"我转过身，正准备离开，却被露丝的声音唤住。"
Luce neutral "不，没关系。"
Marcel shock u "是——是吗？"
Luce "嗯，我不介意，你可以和我坐在一起。"

hide image "border" onlayer border
scene diningroom:
    size (1920, 1080) crop (240, 40, 1440, 810)
show luce frown2:
    xpos 0.5 xanchor 0.5 ypos 0.55 yanchor 0.5
with wiperight_slow

"我四下张望，目光再度与露丝相遇。她皱着眉头，一只手肘撑在木质桌面上。"
Luce "今天天气糟透了。有个人说说话，或许能让我不去在意这份寒冷。"
Marcel ehe u "看来你手里的书也没能帮上多少忙？"
show luce neutral2 with dissolve
Luce "确实没帮上什么。我喜欢马拉美，但他的诗都写得太过伤感了。"
Marcel neutral u "我可以想象……"
"我在以前的学校多少研读过一些马拉美的作品，却始终难以与他的文字亲近。没有灵魂的男人与濒死的天使，读多了总难免叫人腻味。"
"我在露丝身旁坐下，放下餐盘，小心翼翼，以免打翻早餐。"
"今天的食物算是寻常餐点：一只黄油面包卷，外加一碗麦片粥。那面包卷又小又寒酸，粥也不多，但至少是热的。"
"运气好的话，它应当能压住我的寒颤。"
Marcel sigh u "这里的冬天总是这么冷吗？"
show luce sigh2 with dissolve
Luce "总是。"
show luce neutral2 with dissolve
Luce "有时候还会下雪。"
"我见过雪，可巴黎不常下雪。偶尔飘落在街道上的几片雪花，也会很快被清扫得干干净净；闹市街道在积雪堆积之前便已撒上了盐。"
"不过，我听说乡下情形恰恰相反。那儿冷得整片湖泊都结了冰，男孩女孩们可以去溜冰、滑雪橇。"
"这一切听来都那么田园牧歌。不知我是否也有机会亲身体验一番？"
show luce sigh2 with dissolve
Luce "天哪……我真要冻出病来了。"
"露丝呼出一口气。天冷得让她的气息凝成了有形之物，宛如雪茄的青烟。"
show luce huh2 with dissolve
Luce "不过你看起来倒是兴致勃勃的。"
Marcel neutral u "我吗？"
show luce neutral2 with dissolve
Luce "嗯。我看见你进门时，脚步轻快得很。"
Luce "是遇上什么好事了吗？"
Marcel ehe u "啊哈哈哈……"
"我没想到自己竟表现得如此显而易见。"
Marcel smile u "算是吧，也可以这么说。"
show luce frown2 with dissolve
Luce "那是什么缘故？该不会是你的生日吧？"
Marcel neutral u "还早呢，要到三月。"
show luce huh2 with dissolve
Luce "那么，是收到你父母的信了吗？"
Marcel sigh u "不完全是。我母亲本来就常常给我写信，至于我的父亲……唉，他从来都不太关心我的事。"
show luce sigh2 with dissolve
Luce "啊，我明白了。那么看来，你父亲是个混蛋。"
Marcel ehe u "也差不多是这样了。我母亲心情不好的时候，还会用更难听的话骂他……"
"「那个混蛋」是她用来称呼我父亲的许多绰号中最常用的一个。不过，我可不能把这话转述给露丝听——尤其是在餐厅里。我不愿让任何人听见。年轻姑娘不该说脏话。"
"在我们交谈之际，又有几名学生拖沓着走了进来。我想我至少能数出二十个脑袋。看来还有几位女生尚未到齐。"
show luce neutral2 with dissolve
Luce "天哪，真有意思。"
Luce "我无论如何也想不到，像你这样的人居然会有一个邪恶的父亲。你看上去教养良好、性情温和，与那种人实在沾不上边。"
show luce sigh2 with dissolve
Luce "看来外表是会骗人的。"
"哦，露丝对此毫不知情。"
show luce frown2 with dissolve
Luce "那么，告诉我吧：你为什么这么兴奋？我可懒得再玩猜谜游戏了。"
Marcel smile u "你很快就会知道了。这件事关系到我们全班——不，是关系到全校！"
show luce neutral2 with dissolve
Luce "全校，是吗？那可真有意思。我倒好奇会发生什么事。"
play sound "sfx/churchbells.ogg" fadein 1.0
"幸运的是，露丝不必再好奇太久。远处的教堂钟声终于响起，宣告着清晨课程的开始。"
"我们站起身，动身前往教室。班上还有两三位女生跟在我们身后，其中便有埃莱娜和朱贝尔双胞胎。"

stop sound fadeout 1.0

play ambience "sfx/footsteps3.ogg" fadein 0.5
scene diningroom
show luce neutral:
    xpos 0.5 xanchor 0.5 ypos 0.55 yanchor 0.5
    ease 0.6 ypos 0.5
with dissolve

$ renpy.pause(0.4)

show luce:
    ease 1.8 xpos 1.05

$ renpy.pause(1.2)

play ambience2 "sfx/footsteps2.ogg" fadein 0.5
stop ambience fadeout 0.5

scene yard_r
show luce neutral r:
    xpos 0.01 xanchor 0.5
    ease 4.5 xpos 1.0
with wiperight_slow

$ renpy.pause(2.0)

stop ambience2 fadeout 0.5
play ambience "sfx/footsteps3.ogg" fadein 0.5
scene classroom_r
show luce neutral:
    xpos -0.10 xanchor 0.5 ypos 0.5 yanchor 0.5
    ease 1.8 xpos 0.30
with wiperight_slow

$ renpy.pause(0.5)
stop music fadeout 1.0
stop ambience fadeout 1.0

"我们走进教室，各自落座。"

play music "bgm/Celine.ogg" fadein 1.0

show luce:
    ease 0.5 ypos 0.53
"时间流逝，又有几位女生陆续走进来；她们不住在校内，而是住在附近的村庄里。"

show image "border" onlayer border
scene classroom_r:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 25.0 crop (350, 50, 1280, 720)
with wiperight_slow

"诺艾米第一个到，紧接着是克洛蒂娜。塞琳随后也来了，再后面是米拉贝尔。"
"还有几位女生缺席。我猜想一定是天气的缘故。我们少了三个人。"
"真可惜。我本希望这项通知能在全班面前宣布，不过想来她们很快就会知道的。"
play sound "sfx/door.ogg"
"终于，布吕吉埃夫人亲自走了进来。她果断地「砰」一声关上门，然后拍了拍手。"

hide image "border" onlayer border
scene classroom_r:
    size (1920, 1080) crop (240, 40, 1440, 810)
show al neutral at center
with wipeleft_slow

Bru "好了，姑娘们，安静一下。又一个光辉灿烂的求学之日正等着我们！"
Claudine u smile "光辉灿烂？哪里算得上！"
Claudine "夫人，如果您觉得外面的天空称得上这个词，那我看您真该去瞧瞧眼睛了！"
"几个女生因克洛蒂娜的冒失而窃窃轻笑，但并无任何喧哗的私语，也没有人怂恿她。我想所有人都冷得没了去胡闹的兴致。"
show al frown with dissolve
Bru "好了，克洛蒂娜小姐，少说这种话，除非你想站到外面去挨这份冻？"
Claudine u annoyed "想都别想！这间教室是够冷的，可外面还要糟糕得多！我怕那风会把我头发的蓬松劲儿全给吹没了！"
Bru "你若再敢顶撞我，年轻的小姐，那你的头发可就成最小的事了。比起外面的风霜，我能更厉害地收拾你。我说明白了吗？"
Claudine "是，夫人……"
show al sigh with dissolve
Bru "很好。我相信今天上午不会再听到你发表任何异议了。"
show al neutral with dissolve
Bru "好了，我来点名。巴尼耶？"
Cla "是，夫人。"
Bru "贝尔纳？"
Claa "到，夫人。"
Bru "卡庞蒂耶？"
Claaa "是，夫人。"
"于是，清晨便如往常一般过去。布吕吉埃夫人记录下我们三位缺席的学生，随后朝全班扫视一圈。"
show al annoyed with dissolve
Bru "好了，在我们正式开始上课之前，有一件事你们必须知道。这件事关系到你们所有姑娘——也包括你，克洛蒂娜！请坐直了——所以你们最好用心听。"
"同学们一齐在椅子上挪动身子，露丝也在其中。她向我投来好奇的一瞥，随即又把头转向布吕吉埃夫人。"
show al neutral with dissolve
Bru "这是一项相当重要的通知……"
show al smile with dissolve
Bru "不过，考虑再三之后，我觉得不该由我来宣布。毕竟，这一切并不是我安排的。"
Bru "我想，不如由塞琳和玛塞尔来主持这件事更好。你们俩能到讲台前面来吗？"
Marcel shock u "咦……？"
"我从没料到布吕吉埃夫人会让我向同学们讲话。"
"我连一对一的谈话都不擅长，何况是一对二十一人。我究竟该怎么保持镇定呢？"
"光是想到这一点，便足以让我的脸涨得通红，而同学们好奇的窃窃私语更是雪上加霜。"

show image "border" onlayer border
scene classroom_r:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 35.0 crop (350, 50, 1280, 720)
with wiperight_slow

Cla "这是怎么回事？塞琳做错什么了吗？"
Noémie smile "她？她绝不会做错事！她可太像一位完美的公主了！"
Cla "那她为什么会被叫到讲台前面去？这种事平时可不会发生！"
Claa "那布吕吉埃夫人找玛塞尔又有什么事？她总是那么安静！"
Claaa "布吕吉埃夫人说这项通知关系到我们所有人……"
Cla "你们觉得会不会和音乐老师有关？"
Claa "哦！说得有理！也许我们会来一位新的音乐女教师，或者一位新的音乐男教师！"
Noémie frown "那为什么塞琳和玛塞尔会被叫到讲台前面去？她们对音乐能懂多少呢？"
Cla "塞琳从小就弹钢琴。也许是她帮布吕吉埃夫人挑选新老师吧？"
Claa "谁都知道布吕吉埃夫人五音不全！"
Noémie "那玛塞尔呢？"
Claaa "她来自巴黎，也许她有人脉。说不定那位音乐老师是她从前学校的熟人呢！"
Claa "哦，我真希望我们能来一位新音乐老师！我渴望遇见一位体贴的成熟男士！米延这座小城里这样的人太少了！"
Claaa "这一带的男人本来就不够多！"
Cla "克洛蒂娜，你对这些事怎么看？"
Claudine u smile "我吗？这个嘛……"
"克洛蒂娜那双猫儿般的眼睛闪烁着光芒。"
Claudine "我想我们只能拭目以待了。"
Claudine "不得不说，我对这些事还挺好奇的。这谜团可真让人兴奋！简直让上学都变得值得了！"
"同学们开始咯咯发笑。她们的猜想越来越离奇，各自在脑海中勾勒出那位完美的音乐老师。"
"他会有深色的头发和棕色的眼睛（或者是蓝色；朱贝尔双胞胎对此意见不一），还有修长优雅的手指。"
"他会礼貌而善良，或许还带几分矜持，但骨子里却炽热深情。"
"我自己也觉得这一切听来有些不真实，好得过了头。"
"若她们是想找个英俊的新音乐老师来奉承讨好，那她们定会大失所望。"

hide image "border" onlayer border
scene classroom_r:
    size (1920, 1080) crop (350, 40, 1440, 810)
show celine neutral2:
    xpos 0.70 xanchor 0.5 ypos 0.55 yanchor 0.5
with wipeleft_slow

Celine "准备好了吗，玛塞尔？"
"塞琳看着我，脸上挂着一抹自信的微笑。"
Celine "你想来告诉大家，还是由我来？"
Marcel smile u  "哦——哦，不……嗯……我们可以一起说。"
Marcel "我本该当你的助手。要是把所有责任都推给你，那可不公平。"
show celine smile2 with dissolve
Celine "说得好！那我们就到讲台前面去吧。"

play sound "sfx/chair.ogg"
show celine:
    ease 0.8 ypos 0.5

$ renpy.pause(0.4)

scene classroom_r
show celine frown:
    xpos 0.70 xanchor 0.5 ypos 0.53 yanchor 0.5
    ease 1.2 xpos 0.5
with dissolve

"我站起身来，椅子发出一声抗议般的刺耳声响。"
"走向教室前方时，我清楚地意识到自己的双腿颤抖得多么厉害。我没有绊倒，简直是个奇迹。"
"我从来都不是什么协调灵活的人。"
Celine "好了，各位，安静一下。"
show celine sigh with dissolve
Celine "我知道你们都迫不及待地想要一位能调戏的男音乐老师，但那根本不可能。你们应该早就知道，布吕吉埃夫人不许男人在这里教书。"
"房间里响起一片失望的声浪，为首的是朱贝尔双胞胎中的一个。"
Cla "这不公平！"
show celine huh with dissolve
Celine "恐怕生活本身就是不公平的。"
Claudine u smile "呵，果然不出我所料。"
Claudine "那么，你们想告诉我们的是什么呢？但愿值得花我们这点时间！"
show celine neutral with dissolve
Celine "绝对值得。我相信你们每个人都会喜欢这个好消息。"
Celine "过去这一个月，玛塞尔和我一直在努力，对吧？"
Marcel shy u "是——是的。嗯……"
"我低头看着自己的脚。比起迎上同学们好奇的目光，这样要容易得多。"
"在巴黎时，我班上有四十多名学生。与之相比，米耶纳这间破旧狭小的教室算不得什么——可全班同学齐刷刷投来的目光，仍然令人紧张得透不过气来。"
Marcel neutral u "我刚来这里时，对音乐几乎一窍不通。我从未受过任何正规的训练。我是个无可救药的初学者，但塞琳没有放弃我。"
Marcel smile u "这一个月来，她一直在私下给我上课……"
Claudine "私下授课，是吗？真够伤风败俗的！"
"同学们听了这话都笑了起来，米拉贝尔也在其中，不过我想她并不明白克洛蒂娜究竟在暗指什么。她只是在学别人的样。"
"与此同时，塞琳叹了口气。"
show celine annoyed with dissolve
Celine "这没什么可伤风败俗的。是你读多了你父亲那些不正经的书。"
Claudine "罪证确凿，我认了！"
Claudine "那么，你们那点小课程又怎样？那跟我们其他人有什么关系？"
Marcel neutral u "那——那个，嗯……在这过去的一月里，我——我算是掌握了……嗯，谈不上掌握，只是学了点钢琴的基础。"
Marcel "我现在能弹几首简单的圣歌了，包括{i}圣善夜{/i}。"
Marcel shy u "我知道这没什么好夸耀的——我还有很大的进步空间！——不过塞琳和我商量了一下，嗯……"
Marcel "她告诉我勒迈尔小姐的合唱团对学校有多么重要……于是，在同布吕吉埃夫人商量之后，我们达成了共识。"
Claudine "关于……？"
show celine neutral with dissolve
Celine "学校合唱团。"
show celine huh with dissolve
Celine "我们要重新办起合唱团，这一次由玛塞尔和我来负责。我将担任你们的指导兼指挥，玛塞尔则负责弹奏钢琴。"
show celine neutral with dissolve
Celine "和从前一样，高年级和中级班的任何学生都可以参加。我们将在每周三和周五放学后，在音乐教室排练。"
Celine "我们的第一次排练将在明天下午进行。有兴趣参加的同学，请今晚告诉你们的父母。"
Celine "我的目标，是让我们的合唱团按照惯例，在圣诞夜去教堂献唱。"
show celine huh with dissolve
Celine "我知道我们时间不多，但我相信我们能行。我下定决心，要让学校的合唱团办得成功。"

show image "border" onlayer border
scene classroom_r:
    subpixel True
    size (1920, 1080) crop (0, 50, 1280, 720)
    linear 35.0 crop (350, 50, 1280, 720)
with wiperight_slow

"此话一出，教室里又漾起一阵好奇的窃窃私语。"
Cla "学校合唱团？"
Claa "真的要重新办起来了吗？！"
Claaa "我还以为勒迈尔小姐走后，它就永远停办了呢！"
Claa "这是好消息！解散的时候我还难过呢！"
Cla "我也是！我最喜欢在圣诞音乐会上表演了！"
Claudine u neutral "我跟你们一样喜欢合唱团，但我是因为勒迈尔小姐主持才喜欢的。不论你多努力，塞琳，由你来都不会是同一回事。"
Claudine "你确定自己有当老师的本事吗？"

hide image "border" onlayer border
scene classroom_r
show celine huh:
    xpos 0.5 ypos 0.54 yanchor 0.5 xanchor 0.5
with wipeleft_slow

Celine "也许我没有。我知道自己年纪轻，经验还不及勒迈尔小姐的一半。"
show celine sigh with dissolve
Celine "想取代她，确实是我太过自负了……"
show celine neutral with dissolve
Celine "但即便我无法像她那样，我仍会努力让我们的合唱团办得成功。"
Marcel ehe u "我——我也是。我会和大家一起学习，我想那会很有趣。"
Marcel smile u "如果你们愿意，能加入的话我会很高兴。要是能多交几个朋友就太好了，我也很想和你们大家共度时光。"
"我长长地吸了一口气。身体感觉轻飘飘的，仿佛随时都会被一阵微风吹走。"
"演说进行的某个时刻，我一定抬起了头，尽管我完全没有自觉的记忆。"
"我不再看着自己的鞋子，转而凝视着同学们的脸，而他们也都在回望着我。"
"我的手指攥住裙子上朴素的黑色布料，然后重重地叹了口气。"
"塞琳和我已经尽了全力。现在，我们只能静观其变。"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  11月17日{vspace=1}  补课时间") )
play music "bgm/Oh Holy Night.mp3" fadein 1.0
scene sky_s with wiperight_slow
window show dissolve

"那天下午晚些时候，我和塞琳一同前往音乐教室。这将是合唱团正式开始之前，我们最后一堂单独相处的课。"
"此刻房间里静极了，静得我连风儿的低语都听不见。"
"然而等到明天，这间教室就会充满其余同学兴奋的叽喳声了——或者，至少我希望如此。"
"总有可能，同学们怀疑我和塞琳的本事，一个都不来参加我们的第一次排练。"
"这个念头令人难受。我觉得它比想到要在众人面前演奏还要让人焦虑。"
"我忍不住为这些事忧心忡忡。心思没法集中在钢琴上，演奏也因此大受影响。"
"昨天我还算顺利地弹完了{i}圣善夜{/i}，可如今却频频出错。我把副歌部分弹得一团糟，几乎听不出是那首曲子，塞琳不得不打断我。"

stop music fadeout 2.0
scene musicroom_s blur:
    size (1920, 1080) crop (250, 60, 1152, 648)
show celine annoyed3 s:
    ypos 0.55 yanchor 0.5 xpos 0.5 xanchor 0.5
with wipedown_slow

Celine "停，停，停！完全不是这样！"
show celine frown3 s with dissolve
Celine "你到底怎么回事，玛塞尔？"

play music "bgm/Friendship.ogg" fadein 1.0

Marcel shy u "我，嗯……我——我很抱歉……"
"我让手指从琴键上滑落。羞愧之下，我把手搁在膝上，这样它们便再也无法糟蹋阿道夫·亚当那首广受喜爱的曲子了。"
Marcel "我脑子里装了很多事。"
show celine sigh3 s with dissolve
Celine "你的心思似乎总是这么重呢，没错！"
show celine frown3 s with dissolve
Celine "听着，无论是弹钢琴，还是弹别的什么乐器，都必须把全部的心神倾注其上。你若任由思绪游荡，就永远成不了一名真正的乐师。"
Celine "分心的事，等你把手指从琴键上移开再去理会也不迟。在那之前，你最好专心致志！"
Marcel sigh u "我知道。对不起。只是……"
Marcel sad u "你真的觉得同学们会愿意加入合唱团吗？"
show celine huh3 s with dissolve
Celine "我不觉得她们会不乐意。"
Celine "合唱团还在时一直很受欢迎。解散的时候，许多同学都很难过，克洛蒂娜就是其中之一！"
show celine neutral3 s with dissolve
Celine "同学们会来的。我确信。"
Marcel "可是，据我所知，它之所以受欢迎，是因为当时由勒梅尔小姐主持。"
Marcel "她们会对一个由我们两个来主持的合唱团有兴趣吗？"
Marcel "你本身便是位有才华的乐师，而我还是个初学者。别人怎么会相信我呢？"
show celine huh3 s with dissolve
Celine "你若对自己没有信心，她们自然也不会。你只需要相信就好。"
Marcel huh u "可是——"
show celine frown3 s with dissolve
Celine "现在已经没有时间讲那些「但是」了。你不能总是盯着最坏的结局看。"
Marcel sigh u "我知道不该这样。我明白担忧无济于事，可我还是放心不下。我想这是天生的吧……"
"我轻叹一声。"
Marcel "我只是……不想让你受伤。仅此而已。"
Marcel neutral u "我知道你为此付出了许多心血。我希望看到它开花结果。若是不成功，那就太叫人沮丧了。"
show celine huh3 s with dissolve
Celine "若是不成功，我就去恳求同学们，直到她们让步同意加入为止——但也只有在万不得已的时候。"
show celine neutral3 s with dissolve
Celine "你或许对自己毫无信心，可{i}我{/i}有。我一个人的信心，就足以支撑我们两个。"
Celine "我的决心坚定不移。同学们至少也该明白这一点。"
Celine "我不是勒梅尔小姐，但她们可以信任我。我不会让她们失望的！"
"我呆呆地望着塞琳，惊得说不出话来。她这番小小的演说，真让我不得不佩服。"
"我不确定她的话是专为我说的，还是她也在为自己打气，但不管她的用意如何，这番话都起了作用。"
"我依然担忧（我什么事都担心），但她的坚定已平息了我最深的忧虑。"
"我这是在做什么，为一个我无法掌控的未来而焦虑？我真是傻。"
Marcel smile u "……是啊。你说得对。你一向坚定，坚定得惊人！正因如此，我才答应帮你。"
Marcel "我……也希望你能成功。我愿意做这件事，不光是为了你，也是为了我自己。"
Marcel "我不想拖你的后腿，所以我会努力让自己更有信心。"
Marcel laugh u "我有把握，到了明天下午，这间屋里就会挤满人！"
show celine smile3 s with dissolve
Celine "是的，一定会。这还用说吗。"
show celine huh3 s with dissolve
Celine "所以我们才要善用眼下这段时光。你必须加倍、再加倍地练习。我可不想你在众人面前表演时吓得僵住！"
Marcel shy u "这、这……确实是个很中肯的顾虑，是啊。"
Marcel sigh u "抱歉，我浪费了时间。"
show celine neutral3 s with dissolve
Celine "没关系。"
Celine "我们做得到的。我知道我们做得到。若是一开始就认定这是一场徒劳，我根本不会踏上这条路。"
show celine smile3 s with dissolve
Celine "那么，就让我们一起全力以赴，好吗？"
Celine "这会很辛苦，但我相信也一定会很有成就感。"
Celine "我们会非常开心的！"

stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene sky g
with clockwipe
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

$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  11月18日{vspace=1}  新的校合唱团") )
$ renpy.pause(0.3)
play ambience "sfx/birds.ogg" fadein 1.0
scene sky with dissolve
window show dissolve

"我试着保持乐观，但这比我想象的更难。于是，我一个晚上多半在为第一次合唱排练担心，随之而来的大半个早晨也是如此。"
"我向来不擅长往好处想。"
"住在巴黎时，我的生活几乎完全没有阳光。我真正的盟友只有母亲，而她也无法让我免受同学和老师的欺负（平心而论，她确实试着这么做了）。"
"每一天都是令人痛苦的煎熬。我学会了做最坏的打算，因为抱最好的希望到头来只会以失望收场。"
"我已深谙悲观这门艺术，但这不是过日子的方式。"
"我倒想试着相信有美好的结局。"
"我告诉自己一切都会好起来的。我一遍又一遍地对自己这么说——而当一天中的最后一堂课结束时，我遇到了一个令人愉快的惊喜。"
"与我的担忧相反，音乐教室并非空无一人。不算我和塞琳，那里有十五名学生，其中就有露丝和克洛蒂娜。"

stop ambience fadeout 1.0
play music "bgm/Claudine.ogg" fadein 1.0
scene musicroom:
    size (1920, 1080) crop (240, 40, 1440, 810)
show claudine smile2 at center
with wipedown_slow

Claudine "哎呀，这可真是个温馨的聚会呢，不是吗？"
show claudine smirk2 with dissolve
Claudine "可你不觉得人似乎有点少了吗？我记得当年勒梅尔小姐主持合唱团的时候，起码有三十名团员！如今人数连一半都不到了！"
"克洛蒂娜用轻快、抑扬顿挫的口吻说出她的观察，可我照样皱起了眉。"
"那听来几乎像是一种攻击，又或许是一种嘲弄。"
"克洛蒂娜来这里难道就只是为了找麻烦吗？"
"我摆弄着裙子的布料，再度焦虑起来。我不希望这个新合唱团总被拿来与勒梅尔小姐的合唱团相比。那对塞琳不公平。"
"她已尽了最大努力。克洛蒂娜没有评判的资格！"
"塞琳似乎也这么想，因为她毫不迟疑地让克洛蒂娜收敛起来。"

scene musicroom
show claudine smile:
    xpos 0.30 xanchor 0.5 ypos 0.5 yanchor 0.5
show celine frown:
    xpos 0.70 xanchor 0.5 ypos 0.53 yanchor 0.5
with dissolve

Celine "合唱团是几个月前才解散的。如今已经有十五名成员，这值得骄傲。这不是个小数。"
Claudine "我想也是吧，没有。"
show claudine laugh with dissolve
Claudine "我看到了好多熟悉的面孔！茹贝尔家的两位都在这儿，还有亲爱的海伦也在！"
show claudine smirk with dissolve
Claudine "真遗憾诺艾米不肯赏光光临。我是邀过她的，可她说她还有更要紧的事要忙，没空来迎合你这样一个爱慕虚荣的城里姑娘的心血来潮！"
show celine sigh with dissolve
Celine "她真是这么说的？"
"塞琳叹了口气。"
Celine "她可真是客气得紧。"
show claudine neutral with dissolve
Claudine "诺艾米一向说话直来直去。她不是个特别有礼数的人。"
show celine frown
show claudine laugh
with dissolve
Claudine "要知道，她可是在米耶讷土生土长的，所以根本不懂得什么叫风雅、什么叫分寸，偏还喜欢摆出一副淑女的派头！"
Claudine "她父母或许很有钱，可教养是买不来的！"
Claudine "她跟你完全不一样，塞琳！"
"克洛蒂娜咯咯地笑了，另外几个女孩也跟着笑了起来。"
show claudine neutral with dissolve
Claudine "那么，还有谁在这儿呢？我没看到什么生面孔，不过……"
show claudine smirk with dissolve
Claudine "哎呀！"
"克洛蒂娜的目光落在露丝身上，笑意加深。"

show luce frown:
    xzoom -1 xpos 1.10 xanchor 0.5 ypos 0.5 yanchor 0.5
    ease 2.0 xpos 0.86

Claudine "真没想到会在这儿见到{i}你{/i}，亲爱的露丝！你以前对那个老合唱团可是从没表现出半点兴趣！我还不知道你在音乐上也有两下子？"
Luce "我会唱一点。"
show claudine laugh with dissolve
Claudine "我想肯定只有{i}一点{/i}点吧！你这么娇小，说话又轻声细语的，恐怕也发不出多大的声响！"
"同学们又咯咯笑了起来。"
show claudine smile with dissolve
Claudine "那你怎么决定来这儿了？是回心转意了吗？"
show luce huh with dissolve
Luce "没什么特别的理由。我只是觉得也许会有意思。"
show claudine neutral with dissolve
Claudine "可你对勒梅尔小姐的合唱团可从来没这么想过！"
show luce neutral with dissolve
Luce "那是另一回事。她每周给我们上三次音乐课。那对我已经足够了。"
Luce "不过，我还没听过玛塞尔弹钢琴。我想知道那是什么样子。就这样而已。"
show claudine laugh2 with dissolve
Claudine "哦——我明白了！"
"克洛蒂娜用手肘捅了捅我的侧腰。"
Claudine "看来你有了一位爱慕者呢，玛塞尔！"
show claudine smirk2 with dissolve
Claudine "你到底做了什么，把小小的露丝迷成这样？是凑在她耳边说着甜言蜜语，还是向她许下了海誓山盟？"
Marcel shockblush u "当、当然不是！我，我绝没做过那样的事！"
"我试着把克洛蒂娜挡开，却收效甚微。她照样捉弄我，对我的窘迫视而不见（又或许正因为如此）。"
show claudine smile2 with dissolve
Claudine "别这样嘛，何必这么害羞！你一定做了什么打动露丝芳心的事！她平时除了那些旧书，可是谁都不放在心上的！"
Claudine "你到底有什么特别之处，嗯？"
Marcel "我、我没什么特别的！我什么都没做，我——"
Marcel "啊……！"

play sound "sfx/slap.ogg"
show claudine smile
with vpunch

"我往后退了一步，差点被钢琴凳绊倒。塞琳不得不伸手把我扶稳，这让同学们又窃笑起来。"
"这可真{i}是{/i}太难为情了。简直让我后悔当初谁都不来才好！"
show celine annoyed with dissolve
Celine "好了，闹够了吧。"
Celine "如果你是来这里取笑我们的，那就不必费心了。我是要认真对待这个合唱团的。若是你做不到，那请便吧！"
show claudine shock at bounce
Claudine "这么说，我这么快就被赶出去了？可我才来五分钟呀！"
show celine frown with dissolve
Celine "而这五分钟里，你就已经给自己留下了相当糟糕的印象。"
show claudine smirk with dissolve
Claudine "天哪！你说话简直就像布吕吉埃夫人！再这样皱下去，你会长出皱纹的，到那时就没男人肯娶你了！"
show celine embarrassed with dissolve
Celine "这、这根本是两码事！现在担心这些还太早了！我更愿意把心思放在音乐上！"
Claudine "哎呀，你多虔诚啊！简直就像个小修女。真是令人佩服——不过同时也有点让人失望。"
show claudine sad with dissolve
Claudine "这个崭新的合唱团，看起来似乎没什么乐趣。勒梅尔小姐可从来没这么严厉过！"
show celine annoyed with dissolve
Celine "还有，想来你还没注意到，我并不是勒梅尔小姐。别指望我会像她那样容忍你的胡闹。我没有那份耐心。"
show claudine neutral with dissolve
Claudine "哎呀，我真命苦啊！"
"克洛蒂娜撅起了嘴。"
Claudine "塞琳，我可是一路专程赶来的，你这样可不是谢人的态度！我还想方设法要诺艾米陪我来，只是没能如愿，你也看到了。"
show claudine sad with dissolve
Claudine "我觉得自己受了欺负！我真有点想转身就走了……"
show claudine smile with dissolve
Claudine "不过，正如小露丝所说，我{i}确实{/i}想听听玛塞尔弹钢琴。"
Claudine "也许我会留下来听一两首歌。要是合我心意，我也许会屈尊多待一会儿。你觉得如何？"
show celine frown with dissolve
Celine "你随时都可以走。只是别闹出太大动静来。"
show luce frown with dissolve
Luce "你对她要求太高了。克洛蒂娜是不可能{i}不{/i}闹出动静来的。"
show claudine laugh with dissolve
Claudine "小露丝说得对，恐怕正是如此！要我安安静静的，那是办不到的！我生来就是要引人注目的……"
show claudine smile with dissolve
Claudine "不过，就算是我，也看得出自己做得过分了。我不想惹你哭，塞琳，所以我会安分守己——至少眼前是这样！"
show celine sigh with dissolve
Celine "谢谢你。"
"塞琳深深地叹了口气。"
show celine frown with dissolve
Celine "那么，我们先做一系列的发声练习。请各位姑娘各就各位，好吗？"
"合唱团的十五名临时成员没有太多异议，都听从了塞琳的安排。就连克洛蒂娜也照做了，而且没有翻白眼。"
"这一定是个奇迹！"
show celine neutral with dissolve
Celine "那么，玛塞尔，你愿意为我们弹几个和弦吗？我希望大家都跟着一起唱。"
Marcel huh u "好、好的！当然！"
"我在钢琴前坐下。与此同时，塞琳站到房间前方，活像一位真正的指挥家。她举起双手，然后说道……"

stop music fadeout 1.0

Celine "开始吧！数到三！"

play music "bgm/Oh Holy Night.mp3" fadein 1.0
scene sky with wipeup_slow

"于是，这支新学校合唱团的第一次排练正式开始了。"
"塞琳带领同学们做了大约十分钟的暖身练习，接着开始排练圣诞赞美诗。这些都是耳熟能详的流行歌曲，似乎没有人觉得有困难。"
"我想这些一定就是学生们跟勒梅尔小姐唱过的那些歌。这倒也解释了为何他们的元音和辅音都显得那么纯熟。"
"尽管这堂课因克洛蒂娜的挑衅而开局不顺，但每个人似乎都在认真对待。"
"当塞琳要求女孩们重复某些段落，或指出她们的错误时，会有几声不满的嘟囔，但没有人在气恼中放弃。"
"就连克洛蒂娜也留了下来，尽管她早前扬言要甩手走人。"
"事实证明，塞琳是一位相当不错的指挥。她懂音乐，足以领着女孩们齐声开唱，而她在要求唱得轻柔或响亮时的手势也清晰易懂。"
"她的指导一丝不苟，却不盛气凌人。"
"她的热忱在她的一言一行中都表露无遗，以至于我想就连克洛蒂娜也必定对她生出几分（不情愿的）敬意。"
"塞琳做得棒极了。"
"至于我自己呢…… {w}唉。"
"至于我自己的表现，还是少说为妙。"
"我从未在这么多人面前弹过钢琴。事实上，直到昨天下午，我除了塞琳之外从没在别人面前弹过。"
"我浑身僵硬，因紧张而焦虑，手指也似乎不愿与我配合。"
"课程一开始我就犯了许多愚蠢的错误。我把好几首歌彻底弹砸了，害得合唱团不知所措，连塞琳的指挥都无法引导他们。"
"每当这种情况发生时，我就在半途停下弹奏并道歉。这换来塞琳责备的一瞪，可合唱团的其他女孩似乎觉得好笑胜过恼火。"

stop music fadeout 1.0
scene musicroom
show claudine smirk:
    xpos 0.5 xanchor 0.5
with wipedown_slow
play music "bgm/Claudine.ogg" fadein 1.0

Claudine "哎呀，{i}那{/i}可真是对{i}圣善夜{/i}的一次别出心裁的演绎！"
"当我把那支被我弹得一团糟的曲子勉强引向一个凄惨、蹒跚的收尾时，克洛蒂娜发出了窃笑。"
Claudine "我可不知道还能唱成这样！反正我们跟勒梅尔小姐一起唱的时候，绝对不是这样的！"
Claudine "巴黎就是那样唱这首歌的吗？还是你想给它加上自己的一番现代演绎？"
show claudine laugh with dissolve
Claudine "要是如此，我可真得为你喝彩！那可真是相当前卫，只是略显凌乱了些！"
Marcel shy u "不、不是的，呃……我没有那样的本事去改编别人的作品。要是硬去试，只会把它弄糟。"
Marcel "我再来一次吧……"

show claudine:
    ease 0.8 xpos 0.30
show celine sigh:
    xpos 1.10 xanchor 0.5 ypos 0.53 yanchor 0.5
    ease 1.4 xpos 0.70

Celine "好，你就再试一次——下次可要更用心些，玛塞尔！"
show claudine smile with dissolve
Claudine "哎呀，请别这么责备玛塞尔！她已经尽力了，虽说她的尽力也确实还有待加强！"
"我再次开始弹奏，脸上一直火烧火燎的。"
"我庆幸自己可以背对着其他同学。他们看不到我的双颊有多烫，我也不必看到他们那副看好戏的表情。"
"因为没在看着他们，我几乎可以想象这房间空无一人——而这正是我所做的。"
"不让他们灼灼的目光穿透我的后背，弹起来要容易得多。"
"我相信我一定能做到；不，我{i}一定{/i}要做到。"
"我要全力以赴；不只是为了我自己，也是为了塞琳。"
"我不希望她的辛苦白费。"

stop music fadeout 1.0
window hide dissolve
scene black with blinds2
$ renpy.pause(0.3)
$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  11月18日{vspace=1}  旗开得胜") )
scene cg22 with blinds2
play music "bgm/Friendship.ogg" fadein 1.0
window show dissolve

"时间悄然流逝，而随着时间流逝，我的琴声也变得愈发自信。"
"我仍会出错，但这些错误远比排练头半个小时里犯的要少得多、轻得多。"
"等到整整一个小时过去，太阳开始西沉，我几乎为自己感到骄傲。我撑了过来，而它并没有我想象中那般艰难。"
"我没能跟许多同学说上话（我忙着在琴键上紧张得冒汗），可我感到自己与他们建立了一点情谊，而我从前从没有过这样的机会。"
"我玩得比预想中更开心，而我知道开心的人不止我一个。"
"等到其余同学都离开后，克洛蒂娜留在音乐室里，然后说道……"

scene musicroom_s
show claudine smile s:
    xpos 0.30 xanchor 0.5
show celine frown s:
    xpos 0.70 xanchor 0.5 ypos 0.54 yanchor 0.5
with wipedown_slow

Claudine "你让我吃了一惊，塞琳。我本没打算待整整一个钟头，可这一小时实在很有趣！"
show celine huh s with dissolve
Celine "您真的这么觉得吗？"
"塞琳满腹狐疑地看着克洛蒂娜。"
show celine frown s with dissolve
Celine "难得你会这样称赞人。"
Celine "这不是什么玩笑的伏笔吧？"
show claudine laugh s with dissolve
Claudine "不是，不是！才不是！你这副愤世嫉俗的样子真叫我伤心！"
show celine sigh s with dissolve
Celine "就算我愤世嫉俗，你也得原谅我——因为你做过的事，早已足够让我如此了……"
show claudine smile s with dissolve
Claudine "好了，好了，我承认。我知道自己有时是个坏女孩，也爱看布吕吉埃夫人难堪，但我现在是真心实意的。"
Claudine "我很喜欢唱歌。合唱团解散后过了那么久，我几乎都快忘了自己原来这么喜欢它！"
Claudine "要是我能，我倒想在家里多唱唱，可我爸爸总忙着工作，我不愿打扰他。"
show claudine laugh s with dissolve
Claudine "这个合唱团是我对音乐这份心意的唯一出口了！"
show claudine smile s with dissolve
Claudine "我承认，听说你打算重组合唱团时，我是心存疑虑的。我以为没有勒梅尔小姐就不会有趣，可现在我知道自己下结论下得太草率了。"
Claudine "我看得出你很努力——你也是，玛塞尔！"
show claudine laugh s with dissolve
Claudine "你的琴技还有待提高，但至少你能勉强应付一些简单的歌曲。这总归是件好事！"
show claudine smile s with dissolve
Claudine "既然你们这么用心，我也许会受感染，跟着一起下功夫。"
Claudine "我也想参加圣诞音乐会演出！"
Marcel shock u "我、我们也想！这正是我们的目标！所以我才会努力学钢琴。我很乐意为你在音乐会上伴奏！"
Marcel "我知道自己还有许多要学，但我会一直练下去；我保证！"
show claudine laugh s with dissolve
Claudine "这才像话！"
show claudine smile s with dissolve
Claudine "放学后能这样聚在一起，多好啊，对不对？我们都是朋友，所以应该好好相处。你同意我的话吗，塞琳？"
show celine huh s with dissolve
Celine "这、这个，那……我也不是特别想跟你做朋友。你既招人烦又自以为是，还总不知道什么时候该闭嘴……"
show claudine laugh s with dissolve
Claudine "我知道！我是不是很讨人喜欢？"
Claudine "真奇怪，比杜普莱西先生更俊朗的男人，怎么到现在还没向我求婚呢！"
show celine neutral s with dissolve
Celine "不过我想，你也不是一无是处。我知道你爱唱反调，可有些时候，你还是挺肯下苦功的。"
show celine huh s with dissolve
Celine "你无疑是全校最出色的歌手之一。若你肯留下来，合唱团会大受裨益。"
show celine huhblush s with dissolve
Celine "既、既然如此，我……觉得……若是我们能多相处些时间……那会很好……也许……"
show claudine smile s with dissolve
Claudine "这么说，你{i}确实{/i}想和我做朋友？"
"克洛蒂娜得意洋洋地咧开嘴笑了。"
Claudine "我就知道！你这傻姑娘，何不直说，非要这样含含糊糊、拐弯抹角？"
show claudine smirk s with dissolve
Claudine "身为一位优雅的淑女，你也真是够束手无策的……{w}不过别担心。我就喜欢帮助那些无依无靠的人！"
show claudine laugh s with dissolve
Claudine "要让合唱团在音乐会之前达到水准，确实是个挑战，但我准备好试一试了！大家一起努力吧！"

show claudine:
    ease 1.2 xpos -1.10
show celine:
    ease 0.8 xpos 0.5

$ renpy.pause(0.8)
play sound "sfx/door.ogg"
hide claudine with dissolve

"于是，克洛蒂娜便带着一个轻盈的笑声离去了。她随手关上了那间破旧老音乐教室的门，留下塞琳和我独处。"
Marcel neutral u "那么……"

scene musicroom_s:
    size (1920, 1080) crop (240, 40, 1440, 810)
show celine huh2 at center
with dissolve

"我看着塞琳。"
Marcel huh u "你感觉怎么样？"
show celine sigh2 s with dissolve
Celine "有点累，不过我觉得进行得相当不错，只除了几个小纰漏。"
show celine neutral2 s with dissolve
Celine "我真的很开心！"
Celine "你呢？"
Marcel shy u "是有点紧张……不过我想我也挺开心的。嗯……"
Marcel sigh u "对不起，犯了那么多错……"
show celine annoyed2 s with dissolve
Celine "你本就该如此！头几首歌你确实唱得一塌糊涂！"
Celine "为了把课程拉回正轨，我可是费了好大的力气！我生怕克洛蒂娜开始起哄，那样周围的秩序就要全乱套了！"
Marcel shy u "我、我知道……我、我下次会更加小心的……"
show celine neutral2 s with dissolve
Celine "……好吧，没关系。我知道你已经尽力了。"
"塞琳的神情变得柔和。"
Celine "总的说来，我认为你做得还算不错。"
Marcel huh u "真-真的吗？"
show celine smile2 s with dissolve
Celine "{i}真的{/i}，确实如此！至少在课的后半段，当你回过神来之后，你表现得相当好。"
show celine huh2 s with dissolve
Celine "下次，你开始演奏之前试着深呼吸几次。那或许能帮你平复紧张的心情！"
Marcel shy u "我很紧张这件事，表现得有那么明显吗？"
Celine "很明显，相当明显。我从你的演奏里听得出来。起初颤抖又刺耳，不过最后终于平稳下来了。"
Marcel sigh u "呃……"
"我皱起了眉。"
Marcel shy u "你觉得别的女孩注意到我的笨拙了吗？"
show celine sigh2 s with dissolve
Celine "要是她们没注意到，我反倒会更惊讶。她们都有眼睛，你知道吧——还有耳朵！"
Celine "尤其是克洛蒂娜，她非常敏锐。她一定察觉到哪里不对劲了。我原本担心她会拿这件事取笑你，不过她并没有像平时那样咄咄逼人。"
Marcel frown u "她似乎更专注于取笑你，而不是我。"
show celine frown2 s with dissolve
Celine "她一直就是这样。她喜欢拿别人开玩笑。我想她对我开这样的玩笑比对谁都多，是因为她知道我能受得住。"
Celine "我不会像这儿的一些姑娘那样，一被取笑就哭鼻子。别人怎么对我，我也怎么回敬——尤其是在涉及音乐的时候。"
show celine neutral2 s with dissolve
Celine "也许看不出来，不过我其实相当坚韧。"
Marcel smile u "我很清楚。呃，其实……挺令人敬佩的……"
show celine huh2 s with dissolve
Celine "只有“挺”吗？"
Marcel shock u "我、我是说，非常！你简直令人敬佩极了！"
show celine smile2 s with dissolve
Celine "哎呀，多谢夸奖！"
"塞琳笑了起来。"
show celine neutral2 s with dissolve
Celine "而且你不必担心那个坏心眼的克洛蒂娜。要是她敢取笑你，我会替你说话的，虽然我怀疑不至于到那一步。她{i}的确{/i}保证过会规规矩矩的。"
Marcel neutral u "你相信她吗？"
Celine "半信半疑吧。她虽说有种种毛病，却也不至于全然不知廉耻。她确实还有几分荣誉感，尽管那已经扭曲了。"
show celine smile2 s with dissolve
Celine "那么……既然你这么努力，我该给你一些奖励才是。"
Marcel shockblush u "啊、啊，不用……！"

scene musicroom_s
show celine smile s:
    xpos 0.5 xanchor 0.5 ypos 0.53 yanchor 0.5
with dissolve

"我往后退了一步，又差点被钢琴凳绊倒（又一次）。这一次，我无需塞琳帮忙就自己站稳了，可我感到格外地恍惚。"
"我怎么这么笨手笨脚？"
"我想我应该庆幸自己练琴时没从凳子上摔下来。要是真摔了，那可就丢人丢大了。"
Marcel shy u "你、呃……你不用给我什么。我觉得我不配。"
show celine huh s with dissolve
Celine "胡说什么！你帮了我，就该得到某种回报。不然我会过意不去的。"
Marcel shock u "可、可我们是朋友啊。你不需要为我做到这个地步——尤其是在我犯了那么多错之后！"
Marcel "真要我说，我觉得我该被责骂，而不是被奖励！"
show celine frown s with dissolve
Celine "你{i}想{/i}挨骂吗？"
Marcel "当、当然不想，可是——"
show celine sigh s with dissolve
Celine "那就别再犯傻了。至少让我为你做点好事吧——别担心，我没打算送你太贵重的东西。不会有什么钻石胸针或宝石的！"
show celine shy s with dissolve
Celine "我想的是……嗯……"
"塞琳的声音渐渐低了下去。"
"她垂下头，眼睛半阖着，用鞋尖在木地板上蹭来蹭去。"
Celine "你想去我家坐坐吗？我觉得我们若能一起放松放松会很好，而今天正是阿梅莉做点心的日子。我知道你有多喜欢她做的苹果派！"
Celine "你不会想错过这个机会的吧？"
"塞琳试着让语气听起来自信，可我听得出她的动摇。她突然间显得格外地不自信。"
"她是担心我会拒绝她的邀请吗？"
"或许这所谓的“奖励”与其说是塞琳想谢我，不如说是想确保我们不至于就此分道扬镳。"
"若她想与我共度更多的时光，那她一定很珍视我们的友谊。"
"我连自己都不一定愿意陪着，而{i}我{/i}终究是我，可塞琳，无论出于什么原因，似乎都乐于有我在旁。"
"我不知道为什么，但我想这些细节也并不重要。被人需要的感觉真好。"
show celine sigh s with dissolve
Celine "嗯……抱歉。当我没说过。"
"塞琳转过身去，双臂交叠。"
Celine "你不想来就不用来。我不想勉强你。"
Celine "就算你已经烦我了，我也不会觉得意外。我们在一起的时间确实很多！我可不想死缠着你……"
Marcel huh u "噢，不会！没关系的！我很感谢你的邀请！"
show celine huh s with dissolve
Celine "你愿意……？"
Marcel "是的，我愿意！"
Marcel smile u "你该知道，我绝不会错过品尝阿梅莉手艺的机会！我可没那么没出息！"
Marcel laugh u "我很乐意跟你回家！"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.8)
$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  11月18日{vspace=1}  塞琳的告白") )
play ambience "sfx/footsteps.ogg" fadein 1.0
play music "bgm/Night.ogg" fadein 1.0
scene sky_s with wiperight_slow
window show dissolve

"塞琳和我挽着手臂，一起穿过村庄。"
"店主们正忙着打烊。我看到系着围裙的男人们翻转招牌、放下百叶窗。"
"这标示着又一个工作日结束的喧闹，竟出奇地让人放松。每个人都慢悠悠地，仿佛身在梦中。"
"面包的香气从镇上的面包房飘散出来。一块招牌在风中吱呀作响，一只流浪猫悄无声息地踏过鹅卵石路面。"
"天气很冷，塞琳依偎着我取暖。她的发丝搔着我的脸颊，而我们长长的影子在地面交融在一起。"
"我们以从容不迫的步伐走着，心满意足地任凭世界在我们身边流转。"
"最后几片秋叶从我脚边滚过。我踩上一片，它发出嘎吱声，随即瘪了下去。"

window hide dissolve
scene black with blinds2
$ renpy.pause(0.3)
play ambience2 "sfx/night_amb.ogg" fadein 1.0
scene sky_n with blinds2
window show dissolve

"当塞琳和我终于抵达目的地时，天色已暗了下来；星星早已探出头来。"
play sound "sfx/door.ogg"
"塞琳握住门把手拧了拧。门吱呀一声打开，她把我迎进屋里。"
"塞琳简短地跟阿梅莉说了说合唱排练的事。她比平时更兴致勃勃，令阿梅莉很是高兴，双眼神采飞扬。"

stop ambience fadeout 1.0
stop ambience2 fadeout 1.0
scene celine_entrance_n
show celine neutral:
    xzoom -1 xpos 0.30 xanchor 0.5 ypos 0.53 yanchor 0.5
show amelie smile:
    xpos 0.70 xanchor 0.5
with wipedown_slow

Amelie "天哪！听起来您玩得可真开心啊，年轻的小姐！"
show celine smile with dissolve
Celine "确实相当有趣。即便和克洛蒂娜针锋相对，虽然叫人恼火，却也算得上是一段愉快的经历。"
show celine huh with dissolve
Celine "那自然比待在屋里无所事事要好得多。"
show amelie sad at bounce
Amelie "无所事事？噢，小姐，您可真让我伤心！"
Amelie "您随时都能跟我玩皮克牌，知道吧！咱们上一局已经是很久以前的事了！"
show celine sigh with dissolve
Celine "那是因为你总出老千。你把老K都藏进袖子里了。"
Amelie "出老千，小姐？我绝不会！我可是品行无可指摘的淑女！"
show celine frown with dissolve
Celine "你爱怎么辩解都行，可我知道真相。一碰到这种无聊的纸牌游戏，你就把体面全丢到九霄云外了！"
show amelie frown with dissolve
Amelie "啧啧！"
"阿梅莉啧了啧舌。"
Amelie "皮克牌可不无聊，小姐！那可是骑士和贵族们玩的游戏！"
show celine annoyed with dissolve
Celine "那就更有理由该正正经经地玩了！你该知道我受不了耍诈的人！"
show amelie frown with dissolve
Amelie "我哪算得上！您把我形容得好像个墨菲斯托费勒斯似的！我或许只是出牌时有点发挥创意——"
show celine sigh with dissolve
Celine "你的意思是说简直是在骗人。"
Amelie "——但那能让场面热闹些嘛！我这么做只是为了逗您笑，小姐！"
show celine frown with dissolve
Celine "因为你的那些把戏一连输上十次，可让我笑不出来……"
show celine sigh with dissolve
Celine "不过这不重要。"
show celine neutral with dissolve
Celine "我要和玛塞尔一起回我房间。你趁机做一个你的苹果派好吗？玛塞尔非常喜欢。"
show amelie smile with dissolve
Amelie "啊！原来您爱吃甜食，是不是？"
"阿梅莉以一种温暖、慈母般的姿态对我微笑，让我想起了自己的母亲。"
Amelie "好极啦。我这就动手。用不了太久。我刚刚正好在擀面皮呢！"
Amelie "您要不要也跟我们一起吃晚饭？我们今晚吃牛舌哦！"
Marcel shy u "噢，不用了，没关系的。我不想打扰……"
show amelie laugh with dissolve
Amelie "一点都不打扰！塞琳小姐吃起东西来像只小鸟一样啄来啄去，盘子里总剩下零零碎碎的。肯定足够您吃的！"
Amelie "我很乐意给塞琳的同学做饭，只要您不像她那么挑嘴就行！"
show amelie smile with dissolve
Amelie "您喜欢牛舌，对吧？"
Marcel neutral u "我、我不是不喜欢……"
Amelie "太好啦！那我这就回厨房去。"
show amelie laugh with dissolve
Amelie "晚饭大约一个小时后就好。做好了我会叫你们这些小姐的！"

play ambience "sfx/footsteps3.ogg" fadein 0.5

show amelie:
    xzoom -1
with dissolve

$ renpy.pause(0.3)

show amelie:
    ease 1.8 xpos 1.20
show celine:
    ease 1.2 xpos 0.5

$ renpy.pause(0.6)

stop ambience fadeout 0.5

"阿梅莉退回到厨房，一路上哼着曲子。"
show celine sigh with dissolve
"塞琳望着她离去的背影，然后叹了口气。"
Celine "走吧。我有些话想跟你说——私下说。"
Marcel huh u "私下……？"
"听上去很严重。我不晓得会是什么事。"

play ambience "sfx/footsteps3.ogg" fadein 0.5
show celine:
    ease 1.8 xpos 1.10

$ renpy.pause(0.8)

show image "border" onlayer border
scene celine_entrance_n:
    subpixel True
    size (1920, 1080) crop (450, 0, 1280, 720)
    linear 20.0 crop (450, -120, 1280, 720)
with wipeup_slow

"塞琳领着我上了楼。我们走进她的卧室，她在身后关上了门。随后，她在床沿坐了下来。"

play sound "sfx/door.ogg"
hide image "border" onlayer border
scene celine_room_n2
show celine neutral:
    xzoom -1 xpos -1.0 xanchor 0.5
    ease 4.0 xpos 0.5
with wiperight_slow
stop ambience fadeout 3.0

"至于我，却不完全确定该坐哪里。我环顾房间半晌，一时有些茫然，直到塞琳用手拍了拍床。"
Celine "怎么？你在等什么？过来呀；来嘛。"
Marcel shock u "好、好的！当然……"

play sound "sfx/fall.ogg"
scene celine_room_n2:
    size (1920, 1080) crop (50, 0, 1440, 810)
show celine neutral2:
    xzoom -1 xpos 0.5 xanchor 0.5 ypos 0.50 yanchor 0.5
    ease 0.8 ypos 0.55
with dissolve

"我快步走到塞琳身边，脸上微微泛红。和塞琳在一起时，我似乎经常这样脸红；尤其是当我们独处的时候。"
"我在她床边坐下，一条腿叠在另一条腿上。我只有第一次拜访她家时进过她的房间，如今置身于一个女孩的私密天地，实在有些局促。"
"倘若她知道我其实是个男孩，我敢肯定她绝不会这么快就邀我来到如此私密的地方——更不会让我坐到她的床上。"
"我清楚地意识到这一切是多么不合时宜。也许正因为如此，我才无法放松下来。"
show celine sad2 with dissolve
Celine "玛塞尔……"
"塞琳的声音打破了笼罩在我们之间的沉默，那沉默浓重得像积雪一般。"
"她从睫毛下打量着我。双手交握搁在膝上，面色苍白，几乎像是褪了色一般。"
"她看起来不像平时的自己。先前的好心情已荡然无存。"
Marcel sad u "有什么事吗？"
show celine sigh2 with dissolve
Celine "没什么事。至少不该有事。我度过了美妙的一天，多亏了你，可是……我一直在想……"
show celine sad2 with dissolve
Celine "我们……是朋友，对吧？"
Marcel huh u "我希望如此！"
show celine smile2 with dissolve
Celine "你答得可真热情啊……"
"塞琳笑了。"
show celine neutral2 with dissolve
Celine "不过我很感激。我很感激你。"
show celine huh2 with dissolve
Celine "一开始，我提出和你做朋友，是因为我可怜你。我不希望你像我当初刚来米延时那样孤零零的。"
Celine "当时我没怎么多想……"
show celine neutral2 with dissolve
Celine "但在过去的这两个月里，我越来越看重你了。"
show celine smile2 with dissolve
Celine "你已证明自己是个非常好的朋友。你能毫无怨言地忍受我所有的任性念头，真是难以置信！"
show celine neutral2 with dissolve
Celine "你应我的请求学了钢琴，甚至还帮我向布吕吉埃夫人提议组建学校合唱团的事。"
show celine huh2 with dissolve
Celine "说实话，这让我有点愧疚——你为我做了那么多，而我当初却只是出于同情才提出和你做朋友！"
show celine sad2 with dissolve
Celine "这也让我担心自己没像你那样认真对待我们之间的关系。我不希望你觉得自己被利用了。"
Marcel shock u "我完全不这么觉得！"
show celine sigh2 with dissolve
Celine "可是，要不是我一直缠着你，你根本不会去学钢琴。"
Marcel smile u "这倒是真的，可我觉得这并非坏事。"
Marcel "起初我也有过疑虑，但如今我已开始享受弹琴的乐趣。我以前从不懂得欣赏音乐，是你真正让我开了眼界！"
Marcel "一连练习上好几个钟头确实辛苦，没错，可每当我回想自己是从哪里起步、如今又到了哪里时，我便觉得这一切都值得。"
Marcel neutral u "我这么做并不只是为了你。眼下，我是因为自己想学才这么做的。看着自己的琴艺日渐精进，让我很快乐……"
Marcel huh u "而和你待在一起，也让我很快乐！"
show celine huh2 with dissolve
Celine "噢，玛塞尔……你真是太贴心了。你真是个心地善良的姑娘，只是有点天真！"
show celine neutral2 with dissolve
Celine "你最好小心点，别跟什么无赖混在一起。世上有许多男人，巴不得用甜言蜜语把像你这样的姑娘引入歧途，然后反过来伤透你的心！"
Marcel sigh u "这一点我很清楚，相信我。"
"我的父亲正是这样一个人。母亲当年还是个年轻愚昧的姑娘时爱上了他，他便利用了这一点。"
"他占有了她，然后抛弃了她。"
"我的父亲是个出了名的浪子，但他不过是众多同类中的一个。我怀疑他甚至算不上其中最糟糕的，因为他仍与我保持着联系——尽管十分疏淡。那些像我父亲一样睡过无数女人的男人，恐怕连这点都不会去费心。"
Marcel neutral u "但我怀疑世上会有男人想追求我。我又高又笨拙。"
show celine smile2 with dissolve
Celine "你也许很高，可你有一张漂亮的脸蛋！举止也很优雅。我要是男孩子，说不定就会喜欢上你！"
Marcel shy u "你、你在取笑我……"
show celine neutral2 with dissolve
Celine "唔，也许是吧。我又不是男孩子，所以要是的话，我也不太确定自己会怎么看待你！"
Marcel frown u "不，我{i}知道{/i}你在取笑我。我们或许是朋友，可你对我的感情再深也深不过朋友这个界限了。"
Marcel huh u "你不是爱着瓦雷纳先生吗？"
"塞琳从未明说过，但我相当确信这就是真相。倘若她不爱他，就不会在他卧室里放着他的照片。"
"即使是现在，我仍能看到她床头柜上那张照片。瓦雷纳先生那双深邃而多情的眼睛，仿佛几乎要穿透到我心里。"
"我心中忽然涌起一股冲动，想拿起那张照片把它转过去，让它面朝墙壁，可那样做未免太小气了。我想塞琳也不会喜欢这样的举动。"
show celine embarrassed2 with dissolve
Celine "什、什么？"
"现在轮到塞琳脸红了。她凝视着我，双颊染成了绯红。"
Celine "谁、谁告诉你的？！是不是阿梅莉在我背后说长道短？！"
Marcel neutral u "没人告诉我。是你说过那么多关于他的话之后，我自己推断出来的。"
Marcel "那么，我说得对吗？"
show celine sigh2 with dissolve
Celine "你、呃……我想，你并非完全猜错了。"
show celine shy2 with dissolve
Celine "这有点难为情，不过……事实上，这{i}正是{/i}我想跟你谈的事。"
Celine "我以前从未跟任何人详细谈过我的过去。同学们当然问起过，可我总搪塞过去。我实在不愿多想它。"
show celine sigh2 with dissolve
Celine "那并不是个快乐的故事。事实上，它相当难堪。我后悔发生的一切，要是时光能够倒流，我愿……"
show celine sad2 with dissolve
Celine "但现在，已经太迟了。"
show celine huh2 with dissolve
Celine "当初我来到米耶讷时，就告诉自己要把过去抛在脑后。我不愿让过去纠缠着我。"
Celine "我知道自己无法真正快乐，但我以为，只要试着往前走，或许还能得到一丝安宁……"
show celine sigh2 with dissolve
Celine "但那是不可能的。"
show celine sad2 with dissolve
Celine "过去不是你能从身上割舍的东西。无论你愿不愿意，它都如影随形，你越想忘掉它，它在你心头压得就越重。"
Celine "我在学校里从不提起它，可它仍整日折磨着我——夜晚也一样。最难以忍受的，是当我躺在床榻上，想要入睡的时候。"
Celine "无视它并不能让它消失，也不能让我更快乐。它只会让我感到更加孤单。"
show celine sigh2 with dissolve
Celine "因为心头压着这件事，我一直很难和同学们建立起任何情谊。"
show celine sad2 with dissolve
Celine "我内心的一部分仍然不愿谈起那件事，可把它一直当作秘密，实在叫人疲惫不堪！"
Celine "我觉得米耶讷这里，没有任何人能够真正体谅我——连你也不例外！"
Celine "我想找个可以倾诉的人，也不希望这个秘密把我们两人推得越来越远。那太叫人难过了……"
show celine huh2 with dissolve
Celine "所以，我告诉你。我把一切都告诉你。"

stop music fadeout 1.0

Marcel huh u "塞琳……"

play music "bgm/Sad.ogg" fadein 1.0
scene celine_room_n2 blur:
    size (1920, 1080) crop (220, 0, 1152, 648)
show celine sad3:
    xzoom -1 xpos 0.5 xanchor 0.5 ypos 0.55 yanchor 0.5
with dissolve

"我伸出手，握住塞琳的手。她的肌肤白得如同瓷器，而且正在颤抖。"
"我并不确切知道她过去究竟发生了什么，但我能感觉到那必定是动荡不安的，甚至称得上是创伤。"
"她受了很多苦。这正是她被放逐到米延的原因。"
"她一直试图摆脱过去的重负，可事实证明这根本不可能。"
"过去太过执拗，怎么也摆脱不掉。"
"虽然我想知道究竟是什么事把塞琳带到了米延，可如果她不愿意，我也不想强迫她向我倾吐心声。那样或许能满足我的好奇心，却丝毫不会让她好受。"
"作为我的朋友，塞琳的安危比我满足自己的好奇更为重要。"
Marcel neutral u "你没必要把你所有的秘密都告诉我。就算不说这些，我们一样可以做朋友。"
Marcel sigh u "毕竟，我也对你藏着一些秘密。"
show celine huh3 with dissolve
Celine "唔，你当然有。别说得好像这是什么了不起的发现似的！每个人都有自己不愿启齿的事，不过我的秘密，可是相当严重。"
show celine sad3 with dissolve
Celine "这关乎我的一生。关乎我对音乐的爱……"
show celine sigh3 with dissolve
Celine "也关乎我对瓦雷纳先生的爱。"
"原来我猜对了。塞琳确实爱他——或者说，至少曾经爱过。"
"当初第一次听见她提起他时，我就已经隐隐有此猜测，可如今证实了，仍不免令我震惊。"
"我的胃不安地紧缩起来。我想，那一定是嫉妒。"
"这对我自己对塞琳的感情又意味着什么呢？"
"我称呼她为朋友，可我或许喜欢她，喜欢得远不止于此……"
"不过我绝不会告诉她。现在绝不是合适的时机。"
"只要我还打扮成女孩、表现得像个女孩，我想就永远不会有合适的（或为社会所接受的）时机。"
show celine sad3 with dissolve
Celine "你说得没错，玛塞尔。我{i}确实{/i}爱过瓦雷纳先生。我想我现在仍然爱着他，尽管距离上一次和他说话，已经过去一年多。"
show celine huh3 with dissolve
Celine "我年少时，他……就是我的整个世界。我从小就认识他，对他的信任胜过任何男人；甚至胜过我的父亲。"
"塞琳从床头柜上拿起瓦雷纳先生的照片。她端详着他的面容，手指环绕着相框。"
"我也打量着瓦雷纳先生的脸。这是一张颇为讨巧的照片，他的头侧转成侧面轮廓。"
"他的头发或许稍长了些（我其实也谈不上有资格说他），衣着打扮也不算入时。他的衣服看起来又旧又皱。"
"他看起来不像个富裕的人，却确实像个善良的人。"
show celine shy3 with dissolve
Celine "他一直对我那么好。他是那样一位绅士——而且我也觉得他很英俊。"
show celine sigh3 with dissolve
Celine "我想，从某种意义上说，我一直都爱着他……但随着年岁渐长，我的感情越来越强烈。"
show celine shy3 with dissolve
Celine "我十三岁那年，才确确实实地明白，我爱他已不只是把他当作音乐老师。我深深地爱着他，也希望他能回应我的心意。"
Celine "我总是期盼着我们的课。那是整个星期里最明亮的时刻。只要我们在一起，一切似乎都无关紧要了：父亲的殷切期望也好，母亲的缺席也好，姐姐们无休止的宠溺也好，都不再重要。"
Celine "他让我觉得自己很重要。"
Celine "当我们的手指轻轻相触，我觉得自己的心跳都要停止了。在他身边，我老是脸红，尤其在他称赞我的时候；但他很有分寸，只是假装没有察觉。"
Celine "他从不会让我难堪。"
Celine "他是那样完美……"
show celine sigh3 with dissolve
Celine "可这其中有一个问题。"
"塞琳把照片放到一旁，一边怅惘地叹了口气。"
show celine frown3 with dissolve
Celine "我有一个未婚夫。"
Marcel huh u "未、未婚夫？"
"我震惊地瞪着塞琳。"
"我早就对塞琳对瓦雷纳先生的感情半信半疑，所以那也算不上太意外。可我从没料到竟会是这样的事。"
Marcel frown u "我想，你以前从没提起过这件事吧……"
show celine sigh3 with dissolve
Celine "没有，确实没有。我不愿去想那件事。"
show celine frown3 with dissolve
Celine "无论如何，他已经不是我的未婚夫了，谢天谢地！我对他没有丝毫兴趣。"
Celine "这门亲事是我父亲替我决定的。他没有征求我的同意，正如他一贯所做的那样。他从不肯来问问我——连这样关系到我未来幸福的大事，也从不和我商量！"
show celine annoyed3 with dissolve
Celine "他真是太不体贴了……"
"塞琳的手指在膝上攥成了拳头。"
show celine sad3 with dissolve
Celine "我是在十三岁生日后不久，才得知这门安排的。父亲把我叫进他的书房，说有事要和我商量。"
Celine "一切都来得太突然。我很惊讶。我不知道他想从我这里得到什么，但我想，总不会是什么太要紧的事。"
Celine "若真是要紧事，他事先总会和我商量一下的。"
Celine "我当时就是这么告诉自己的……"
show celine sigh3 with dissolve
Celine "但我错了。"
show celine huh3 with dissolve
Celine "父亲当场就挑明了我未婚夫的事，事先没有半点征兆。你可以想象，我当时有多震惊！"
show celine frown3 with dissolve
Celine "父亲说他替我觅得了一门完美的亲事。要与我成婚的，是一位糖厂老板的儿子——贝尔热拉克先生。他不过比我大十五岁——{i}不过!{/i}——而父亲认为我们会是相配的一对！"
Celine "我永远不会忘记父亲告诉我这件事时的表情。他显得那样自得，仿佛真的安排了一桩无比美妙的好事。"
Celine "我真心觉得，他以为我会跪在他面前，感激涕零地大哭一场！"
show celine sigh3 with dissolve
Celine "而我自己实在太惊讶了，好一会儿才回过神来回答他。"
show celine frown3 with dissolve
Celine "等我缓过神来，确认这并非某种残忍的玩笑之后，我反驳了他。"
Celine "我告诉父亲，无论他以为我们会是何等般配的一对，我对这门婚事都有些顾虑，而我也不想嫁给一个从未谋面的人。"
Celine "自然，这让父亲很不快。他说我太孩子气，叫我该放眼长远，想想自己的将来，而不该只顾眼前的快乐。"
Celine "他说，这位贝尔热拉克先生很有钱——说到底，你看，图的就是钱——而且他往后也能长久地照顾我。"
Celine "他还说，这桩婚事对我们家族也有好处；他说我若放弃这个机会，就太愚蠢了，毕竟他费了那么多功夫才谈成。"
Celine "父亲表现得像是施恩于我，但我并不信那一套。"
show celine shock3 with dissolve
Celine "若他当真在乎我的感受，就该先和我商量这事！毕竟，赌上的是我的将来，而不是他的！"
"塞琳停顿了一下。她深吸一口气，竭力维持着镇定。"
show celine sad3 with dissolve
"她看起来既愤怒又疲惫，两者兼而有之……"
"但她的故事还没有讲完。"
"催促她让我几乎感到愧疚，可好一会儿过去了，塞琳仍未继续讲她的故事。"
"我想知道她究竟发生了什么。我想这或许能让我更好地理解她，也许还会拉近我们之间的距离。"
"但愿塞琳能原谅我的冒昧，我轻声开了口……"
Marcel neutral u "那，后来呢？"
show celine sigh3 with dissolve
Celine "噢，一场好大的风波！我不想嫁，可父亲想，而他又向来不习惯不顺自己的意。无论我怎么恳求，他都拒不改口。"
show celine frown3 with dissolve
Celine "他说我不该对他嗤之以鼻；至少该先见见他。他似乎笃定，见过之后我就会改变主意！"
show celine annoyed3 with dissolve
Celine "嗯，我确实见了贝尔热拉克先生，而父亲在那一点上倒是说对了。我对他{i}的确{/i}改变了看法。"
Celine "起初，我出于原则而厌恶他。见过他之后，我{i}憎恨{/i}他了。"
show celine frown3 with dissolve
Celine "他是个糟糕透顶的男人：自负又傲慢。他对我讲了许多恭维话，可那些话全都空洞无物，就像他以前拿来哄骗那些比我更蠢、更肤浅的女人的说辞！"
show celine sad3 with dissolve
Celine "我越是见贝尔热拉克先生，就越是痛苦。我嫁给他的意愿，甚至比不上愿意让人在我头上钻个洞，可父亲仍然执意不肯让步。"
Celine "已经定下，我十五岁生日后不久就要成婚，可我们才交往了六个月，如果那也算交往的话！"
Celine "一切都发生得太快了。我开始为自己的将来感到恐惧。我不想在还在上学的时候，就嫁给一个自己不喜欢的人！"
Celine "我开始表现得十分抑郁，瓦雷纳先生不可能察觉不到。我们一向很亲近，我态度的转变让他很担心。"
show celine huh3 with dissolve
Celine "他问我出了什么事，我便把一切都向他吐露了。我说我不想嫁给贝尔热拉克先生，我宁可死，也不愿在上帝的见证下对他许下誓言！"
show celine sad3 with dissolve
Celine "自然，这让他大惊失色。他答应替我向父亲进言，看看能否挽回这个局面。"
Celine "他真是好意……"
show celine sigh3 with dissolve
Celine "可如今回想起来，我觉得这个举动或许是{i}太过{/i}体贴了。"
show celine sad3 with dissolve
Celine "可想而知，瓦雷纳先生与我父亲的交涉失败了。父亲三言两语就打发了区区一位音乐教师的意见——他甚至威胁要辞退瓦雷纳先生，以惩戒他的放肆！"
show celine annoyed3 with dissolve
Celine "放肆！"
"塞琳气冲冲地重复道，眼里噙着辛酸的泪水。"
Celine "好像关心我也会变成放肆似的！"
show celine frown3 with dissolve
Celine "瓦雷纳先生与我并无血缘关系，可他对我的感受，却比我自己的父亲还要体贴得多！"
"塞琳的指甲深深掐进掌心里，我担心她会留下痕迹。"
"我从没见过她这副模样。她气得浑身发抖，而眼里则闪着泪光。"
show celine sad3 with dissolve
Celine "见父亲心意已决，瓦雷纳先生又试着去恳求贝尔热拉克先生。他登门拜访——他究竟是怎样说动仆人放他进去的，我就不清楚了——试图与他谈一谈。"
Celine "这些听闻都是二手消息——这场谈话，我本人并不在场——不过，据我所知，瓦雷纳先生尽了最大努力去说服贝尔热拉克先生回心转意。"
Celine "瓦雷纳先生说，他是我家的世交，还说我曾向他吐露过，对这场迫在眉睫的婚事感到很不快。"
Celine "他问贝尔热拉克先生，是否愿意考虑取消这门婚事，因为他实在非常担心我。"
show celine neutral3 with dissolve
Celine "这是一桩非常高贵的义举……"
show celine sad3 with dissolve
Celine "可这同时也是非常愚蠢的。"
show celine sigh3 with dissolve
Celine "你可以想象，贝尔热拉克先生并不乐意接受这样的冒犯；尤其是对方不过是区区一位音乐教师。"
Celine "贝尔热拉克先生的暴躁脾气是出了名的。瓦雷纳先生几乎还没把话说完，他就扑了上来。"
show celine frown3 with dissolve
Celine "他……那个人……不，那头畜生……"
"塞琳紧紧闭上双眼。几滴滚烫的泪水从眼角滑落，缓缓地沿着她泛红的脸颊淌下。"
show celine annoyed3 with dissolve
Celine "他像一头野兽那样，扑打了瓦雷纳先生！"
Celine "他以为瓦雷纳先生和我关系非同寻常。他实在想不出，瓦雷纳先生还有什么别的原因要取消我们的婚事——好像男人若非与女人有私情，就不会去关心她们似的！"
Celine "我从未与瓦雷纳先生有过情爱关系，尽管我确实爱过他。他极为看重自己作为教师的职责，绝不敢做出任何越轨之事！"
Celine "瓦雷纳先生没有做错任何事！他之所以想保护我，是因为没有人愿意为我出头，而他竟因此遭到殴打！"
Celine "那头怪物竟打了我最亲近的朋友！他打断了他两根肋骨，若不是他及时清醒过来，恐怕还会打断更多！"
show celine sad3 with dissolve
Celine "瓦雷纳先生伤得很重，不得不被送进医院！"
show celine sigh3 with dissolve
Celine "当我得知发生的一切，我感到无比难受。"
Celine "我知道，瓦雷纳先生之所以去找贝尔热拉克先生，全都是因为我。是因为他担心我，不忍心看我如此痛苦。"
show celine shock3 with dissolve
Celine "要-要是当初我什么都没说……如果我守口如瓶，假装一切都好……这一切就都不会发生了！"
Celine "这……都是我的错……"
show celine sad3 with dissolve
Celine "瓦雷纳先生差点因为我而死！"
Celine "我比什么都更爱他，却害他受了伤！我不知道自己还能不能原谅自己！"
"塞琳的泪水真正涌了出来。她用手捂住脸，断断续续地哽咽着，肩膀不住抖动。"
"她看起来、听起来都彻底被击垮了。"
"我在教室里认识的那个冷静自持的塞琳已经消失不见。如今，她显露出本来的模样：不过是个年纪尚轻、无力抵抗年长男人阴谋的少女，而那些男人本应更有分寸。"
"她竟要为一桩明明白白绝非她过错的事，背负如此沉重的内疚，这实在说不通。"
"她从一开头就坦率地表明了心迹。她很清楚地表示自己不想嫁给贝尔热拉克先生，可她的父亲仍执意坚持。"
"他没有理会女儿心中的忧虑，结果酿成了一场灾祸。"
"一个无辜的男人受了重伤，而塞琳的名声也遭到了质疑。"
"这实在不公平。"
Marcel sad u "塞琳……哦，塞琳，我很抱歉。我-我没想到你承受了这么多……"
show celine sigh3 with dissolve
Celine "对-对，唔……我-我不想让你知道。我不想让任何人知道……"
"塞琳吸了吸鼻子。她用胳膊背擦了擦眼睛，然后让双手垂落到膝上。"
"她的脸颊被泪水浸湿，肩膀仍在微微发抖，但她没有再试图遮掩自己的脸。"
"她的悲伤里透着一种毫不道歉的倔强。她的眼睛周围或许像野兔一样泛着粉红，但她的决心尚未消退。"
show celine sad3 with dissolve
Celine "我不愿同学们因那件事而评判我，也不想让他们把这事当成一出蹩脚的戏来谈。"
show celine shock3 with dissolve
Celine "我的人生不是一则故事，可以由人随手翻看，再随手丢弃。局外人或许觉得它有趣——甚至好笑！——可我却不得不与它共处，去承受它！"
show celine sad3 with dissolve
Celine "即便到了现在，它仍然让我痛心。时间并未让这一切变得更容易承受。"
Celine "我真希望瓦雷纳先生没有伤得那么重；不是为了我……"
show celine smirk3 with dissolve
Celine "不过，我想这一切总还带来了一点好处——尽管是以一种迂回曲折的方式。"
"塞琳苦笑了一下。"
Celine "贝尔热拉克先生一口咬定我和瓦雷纳先生有过肌肤之亲。他让奥尔良的每一个人——应该说，每一个有头有脸的人——都知道，我是个企图蒙骗他的无耻荡妇。"
Celine "他解除了婚约。从那以后，我再也没见过他。"
show celine sigh3 with dissolve
Celine "对我而言，这反倒让我大大松了口气……但你可以想象，我的父亲却气得暴跳如雷。"
show celine frown3 with dissolve
Celine "没了富有的贝尔热拉克家族撑腰，我想他有几桩生意就此泡了汤。"
Celine "他为此事感到恼怒，更恼怒的是我的名声，乃至我们家族的声名也遭到了诋毁。"
Celine "当然，他并不生贝尔热拉克先生的气，尽管散布这些不堪传闻的正是他。所有的罪责都落到了我头上，还有可怜的瓦雷纳先生。"
show celine annoyed3 with dissolve
Celine "父亲说我自私；说我不为他人着想。他说我的过错不仅让自身蒙羞，更连累了我们整个家族。"
Celine "他说我该为自己感到羞耻。"
show celine sigh3 with dissolve
Celine "我也懒得去申辩。我知道那毫无意义。父亲从来没有听过我的话；这辈子一直如此。"
show celine frown3 with dissolve
Celine "经过一番争执，父亲最终决定让我离开奥尔良。这份耻辱他实在难以承受，而他以为，只要把我送走，那些闲言碎语或许就会更快平息下去。"
Celine "于是我便来到了米耶讷。"
show celine sad3 with dissolve
Celine "我是在蒙羞之下被送到这里的，只有一名女仆陪着我。自此以后，我就一直住在这里。"
show celine frown3 with dissolve
Celine "来到这里时，我曾立誓，不对任何同学亲近。我不愿任何人知道发生了什么。那样实在太痛苦了。"
Celine "我试着和所有人都保持着距离……"
show celine sigh3 with dissolve
Celine "可当我听说学校有合唱团时，我觉得自己必须加入。我一直热爱音乐，而它让我觉得离瓦雷纳先生更近了些，尽管我已有很久没见到他了。"
show celine shy3 with dissolve
Celine "我给他写过信，可我没有勇气寄出去。我害怕他会说什么。"
Celine "他一定知道，他所有的不幸都该由我来负责。"
Celine "我想，若是他像父亲那样与我反目，我怕是承受不住。"
show celine sigh3 with dissolve
Celine "这个念头想来真叫人害怕。"
show celine shy3 with dissolve
Celine "我很想念他。我想感谢他所做的一切。正因为有他，所以直到如今我才没有嫁给贝尔热拉克先生。"
Celine "是他把我从一辈子的苦难中拯救了出来……"
show celine embarrassed3 with dissolve
Celine "但我几乎愿意忍受这一切，只要我能确切地知道他并不恨我！"
"泪水再次在塞琳眼中凝聚。它们顺着她的脸颊滑落，宛如窗玻璃上的雨滴。"
"她看起来如此悲伤、湿漉、凌乱，我心中涌起一股对她的怜惜。"
"我一直都很喜欢塞琳，但我现在似乎更喜欢她了。"
"从某种意义上说，她的烦恼与我的并无太大不同。我是因为一场类似的丑闻才被迫离开家，只不过那桩丑闻牵涉的是我的父亲，而不是我本人。"
"对于被骚扰或侮辱，我并不陌生，但我想我从未像塞琳那样受过这样的苦。"
"她承受了许多，却仍在努力把生活过得充实。她继续勤勉地用功，表面上是想让瓦雷纳先生引以为傲……{w} 但我认为，她这样做更多的是为了她自己。"
"她想给自己一个可以期盼、可以憧憬的东西，我觉得这实在了不起。"
Marcel neutral u "塞琳……我相信他并不恨你……"
show celine shy3 with dissolve
Celine "可——可你怎么知道？！你从未见过他！"
Marcel "也许没有……但你把他描述得如此生动，几乎让我觉得我见过他一样。"
Marcel "如果瓦雷纳先生真如你所说的那样善良，我不认为他会因为那个可恶男人的所作所为而恨你。那不是你的错。"
Marcel huh u "你自己就是个善良的人。我知道你绝不会希望任何人遭遇不幸。"
show celine shock3 with dissolve
Celine "那——那不是真的。我诅咒贝尔热拉克先生遭受许多不幸——更别提我自己的父亲了！"
Marcel frown u "我不怪你对他们心存不满。他们活该。"
Marcel neutral u "他们亏待了你……但此刻他们并不在这里。{i}我{/i}在这里，我会支持你。我很在乎你。"

window hide dissolve
$ achievement.grant("painful_memories")
scene cg23 with wiperight_slow
$ renpy.pause(1.0)
window show dissolve

"我朝塞琳挪近了些。然后，我张开双臂环抱住她，把她拥入怀中。"
"塞琳没有推开我。相反，她把头枕在我的胸口，任睫毛垂落合上。"
"她的呼吸仍因哭泣而急促，但我想她听起来已比先前放松了些。"
"她的泪水把我的裙前襟濡湿了一片，但我没有试着挪动她。那样做简直是不可饶恕的冷酷。"
"我的校服比起塞琳的幸福，实在是微不足道。"
"我想让她展露笑颜，于是尽管自己的心也隐隐作痛，我仍尽力安慰她。"
Marcel "我在乎你……而且我相信瓦雷纳先生也一样。他一定在乎你，否则他不会那样为你竭尽全力。"
Marcel "我无法确定他是否以你爱他的那种方式爱着你，但他一定在某种意义上是爱你的。否则他不会那样维护你。"
Marcel "你对他来说很珍贵……"
Marcel "而且我确信他绝不会、永远不会恨你。"

stop music fadeout 1.0
window hide dissolve
scene black with blinds2
$ renpy.pause(0.8)
play music "bgm/Confession.ogg" fadein 1.0
scene sky_n with blinds2
window show dissolve

"在她含泪倾诉之后，我尽可能地安慰塞琳。我帮她擦干眼泪，又用手指替她梳理缠结的发丝。"
"到了阿梅莉唤我们用晚餐时，塞琳看起来已与平日相差无几。她的眼角仍比平时稍稍泛红，但她已恢复了大部分镇定。"
"我同塞琳和阿梅莉一同用晚餐。阿梅莉的牛舌十分鲜嫩，她配上了蒜香黄油煮的新土豆和芦笋。"
"我不太喜欢芦笋，但拒绝未免失礼。我把每一根青绿的茎都嚼了下去；那股特有的味道被蒜香黄油略微掩去了些。"
"晚餐后是甜点，那是何等美味的甜点啊！阿梅莉的苹果派与上次吃到的一样可口，甚至可以说犹有过之。"
"我吃光了每一粒碎屑，然后和塞琳在客厅里玩了几局皮克牌。打牌期间我们几乎没怎么交谈，而我也输掉了每一局。"
"不久，我开始觉得疲惫，塞琳提议我或许该回家了。"
"我向她保证，今后会比以往任何时候都更认真地练习钢琴，这似乎让她高兴起来。随后，我便告辞离去。"

play ambience2 "sfx/footsteps3.ogg" fadein 0.5
scene celine_entrance_n
show amelie neutral:
    xpos 1.10 xanchor 0.5
    ease 2.5 xpos 0.5
with wipedown_slow

$ renpy.pause(1.0)
stop ambience2 fadeout 0.5

"塞琳留在客厅里，而阿梅莉则送我走到前门。"
"一路上她以那种管家妇般的关切唠叨着我，这让我想起自己的母亲。"
show amelie sad with dissolve
Amelie "您确定您真的没问题吗，玛塞尔小姐？外面已经很黑了，而且天冷得要命！"
Amelie "我真怕您迷路，或者撞上什么不三不四的人！"
Marcel smile u "我确定我不会有事的。我已在米延住了几个月，如今对这一带已经熟悉了。"
"我的方向感很差，可米延实在太小，除非刻意为之，否则很难在它的街巷间迷路。"
Marcel "我想我也不会被人找麻烦。米延看起来就是个美好又宁静的村庄。"
show amelie neutral with dissolve
Amelie "确实如此。它不太像奥尔良——更不像巴黎！——但我还是忍不住担心。请原谅这个老太婆的胡思乱想吧！"
Marcel "一点也不傻。我很高兴您这么关心我；真的！"
show amelie laugh with dissolve
Amelie "哈！您肯定是第一个这么说的人。塞琳小姐不喜欢我对她嘘寒问暖。她会为此很恼火。"
show amelie smile with dissolve
Amelie "‘天哪，阿梅莉！难道非要我一次次提醒你，我不是小孩子了吗？你让我难堪了！’"
"阿梅莉摆出一副与她那位年轻女主人如出一辙的嗔怪语气。那真是相似得令人称奇，我不由自主地笑出来，阿梅莉也跟着笑了。"
Amelie "好了，好了！我们别站在这里咯咯笑了，不然会惊动那位小姐的。她会想知道出了什么事，然后就会闹起别扭来！"
Marcel ehe u "我可以想象那副光景……"
"我愧疚地笑了笑。"
Marcel "她不喜欢被人取笑。"
Marcel neutral u "我们班上有个女孩，克洛蒂娜，总爱取笑她。我想她这么做是因为塞琳常常会有反应，尽管塞琳似乎自认为不可攻破。"
Amelie "她一直是这个样子，我可怜的小姐。她把心事都写在脸上。她努力想摆出淑女的派头，愿上帝保佑她，可她还有太多东西要学。"
show amelie sad with dissolve
Amelie "我实在忍不住替她担心。她讨厌承认自己的弱点，而且她又是那么倔强——不过我也怪不得她。"
Amelie "经历了奥尔良那桩糟心事之后，她一直很难信任别人。我们刚来米延的时候，我还担心她一个朋友都交不到。她真是个孤零零的小可怜。"
show amelie smile with dissolve
Amelie "您可以想象，当她带您回家时我有多宽慰。您一定是她在这里交到的第一个真正的朋友！"
Marcel huh u "她并不是完全没有朋友。她和我们班上大多数同学都相处得不错。他们似乎都敬重她，克洛蒂娜除外。"
Marcel smile u "至少，似乎没有人讨厌她。"
show amelie neutral with dissolve
Amelie "她确实很擅长讨人喜欢，可她并不愿意向人敞开心扉。我想她是害怕受伤。"
show amelie smile with dissolve
Amelie "她竟然会邀请您来这里，这本身就证明了她有多在乎您。"
Amelie "无论那位小姐是否表露出来，您的友谊对她一定非常重要。"
Marcel "她告诉过我了，是的。她对我一直很好。"
"塞琳天性或许冷淡疏离，但她已向我倾吐了许多。"
"她把她对瓦雷纳先生的感情、她与父亲的关系，以及她那段与前未婚夫的惨淡往事，统统告诉了我。"
"她对我坦诚相待，远胜过我对她。"
"我多希望也能把自己的秘密告诉她……"
"我叹了口气；阿梅莉似乎把这当作是我对塞琳的担忧，因为她笑了。"
"她向我走近一步，压低了声音，像是分享什么机密似的说……"
show amelie smile2 with dissolve
Amelie "您是个非常善良的女孩，玛塞尔。我很高兴塞琳能交到像您这样的朋友。"
Amelie "我希望您能继续留在她身边。正如人们所说，没有人是一座孤岛，她也需要一个同龄的伙伴。"
Marcel smile u "您不必担心这个。我会陪着她，也会尽力照顾她。我保证。"
"我从不轻易许诺，但这个承诺应该很容易兑现。"
"到了这个地步，我想即便我想疏远塞琳，也已经做不到了。"
"我实在太过在乎她了。"

stop music fadeout 1.0
window hide dissolve
scene black with clockwipe
$ renpy.pause(0.3)
scene sky_n g
with clockwipe
$ renpy.pause(0.5)
show overlay2
show message30 at message
show logo2
with datetrans

$ renpy.pause(4.0)

hide message30
hide logo2
hide overlay2
with datetrans2

$ renpy.pause(0.3)

$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  12月24日{vspace=1}  圣善之夜") )
scene sky_n with dissolve
play ambience "sfx/night_amb.ogg" fadein 3.0
window show dissolve

"十一月匆匆走到了尽头，十二月紧随其后。"
"我要做的事情太多，几乎一刻也闲不下来。放学后，我不是和塞琳一起练钢琴，就是为校合唱队弹琴。"
"我肩上担着不少重任，但我无法为此责怪塞琳。若我拼命工作能抵得上两个人的份，那她必定抵得上四个人的份。"
"合唱队须由她来带领。指导姑娘们、化解那些小口角、在大家的热情消退时鼓励每一个人，这些重担都落在她的肩上。"
"她得背下我们要演唱的每一首圣歌的女高音和女低音声部，以便更好地指导合唱队的每一位成员。"
"当某个姑娘唱不上去高音，或在和弦转换时卡住，塞琳总会在一旁帮助她们。"
"我看到过她在当天练习结束后还进行一对一的辅导，并在别人都走了之后，独自在音乐室里待上几个小时，为她的乐谱批注。"
"她要应付的也不只是合唱队。她还得当我的老师，而且她依旧像以前一样严格，甚至有过之而无不及。"
"时间开始变得紧迫，但即便我出错，塞琳也从不发脾气。"
"她温和而亲切，当我手指一时弹不顺某个乐段时，她会亲自为我示范。"
"我能感到自己每天都在进步，尽管由于不间断的练习，我的指尖又红又疼。"
"只要集中精神，我就能毫不出错地弹奏出圣诞音乐会上我们要演出的绝大部分圣歌。这些曲子我已弹过太多遍，甚至能不看琴键就弹出来。"
"有塞琳坚定不移的支持，我几乎开始觉得自己无所不能。"
"塞琳把醒着的每一刻都用在了校合唱队上，致力于我们圣诞音乐会的成功……"
"就这样，在一阵忙乱之中，十二月二十四日的夜晚终于来临。"
"期待已久的圣诞音乐会终于到了，塞琳所有的心血都将在此开花结果。"
"我还没能完全驱散心头萦绕的不安，但我懒得去把这些模糊、尚未成形的疑虑说出口。"
"塞琳已经告诉过我很多次，我应该试着往好处想。"
"今晚弹琴时我或许会犯一些错，但那又有什么关系呢？即便是专业的音乐家也会出错。"
"专业与业余的区别，就在于即使犯了错，也能继续坚持弹下去。"
"我不愿让自我怀疑战胜自己；至少在圣诞音乐会这个夜晚不能。"
"我下定决心要全力以赴。"

stop ambience fadeout 1.0
play music "bgm/Oh Holy Night.mp3" fadein 1.0
window hide dissolve
scene cg22_2 with wipedown_slow
$ renpy.pause(0.8)
window show dissolve

"我办得到的。我知道我办得到。"
"塞琳过去几个月对我的悉心指导，绝不会付诸东流。"
"我要全力以赴。"
"至少，当我坐在村中教堂里那架破旧的老钢琴前时，我是这样告诉自己的。"
"音乐会尚未开始，人们仍陆续步入教堂，但我已经就位。"
"与此同时，学校合唱团的其他成员正整齐地分坐成两排，坐在最前排的长椅上。"
"音乐会将在十分钟后开始。牧师将先向听众致辞，随后我就得把手指放上这些黑白琴键。"
"我将用我的琴声填满这座宽敞而高挑的房间。"
"会有数十乃至上百的人听我演奏。"
"在这教堂空旷的寂静里，连最细微的声响都会激起回音，我的任何失误都无从掩饰。我将暴露无遗。"
"这个念头令人害怕，但我知道塞琳不会离开我太远。"
"有她在身旁，我应该能做到。"
Marcel "{size=-5}会没事的。会没事的。会没事的。{/size}"
"我低声嘟囔着这句咒语般的话，手指深深掐进大腿。"
"我照旧穿着朴素的校服。头发编得整整齐齐，塞琳甚至帮我化了一点妆，来掩盖我灰白的脸色。"
"我看上去和平时没什么两样。"
"经过一番关于制服的争论（其间克洛蒂娜颇为大胆地提议，让我们打扮成歌舞厅舞女的模样），最终决定，我们就穿着平素的日常校服出现在米延的乡亲面前。"

window hide dissolve
scene white with slow_dissolve
scene musicroom g
show celine frown g:
    xpos 0.70 xanchor 0.5 ypos 0.53 yanchor 0.5
show claudine annoyed g:
    xpos 0.30 xanchor 0.5 ypos 0.5 yanchor 0.5
with dissolve
window show dissolve

Celine "我们是要代表我们的学校。穿别的衣服未免太荒唐。"
"这是塞琳在我们某次排练时说的。"
"克洛蒂娜，如所预料的那样，对此表示反对。"
Claudine "什么？但那太无聊了！那样我们根本不会给人留下印象！"
Claudine "我们的校服是黑色的，而教堂在夜里又那么单调灰暗！我们会和背景融为一体！观众根本不会知道我们在那儿！"
"尽管克洛蒂娜连声抱怨，塞琳仍能保持镇定，并以一种淡然的口吻回敬道……"
Celine "那我们就得唱得比以往任何时候都响亮，让歌声充满整座教堂。这样，就没有人会怀疑我们真的在场了。"
show claudine shock g at bounce
Claudine "可是——"
show celine sigh g with dissolve
Celine "此事没有商量。这是我的{i}决定{/i}，且已是{i}最终{/i}的。"
show celine frown g with dissolve
Celine "勒梅尔小姐主管合唱团的时候，我们也是穿着校服演出。我不希望今晚的音乐会有任何不同。"
Celine "我们应该显得整洁、利落、得体；而不是像那些风尘女子！"
show claudine annoyed g with dissolve
Claudine "哎呀，塞琳，你太无趣了！你该学着活得自在一点！"
"克洛蒂娜争辩不休，但她的论据被干脆利落地驳了回去，这让我松了一口气。"

window hide dissolve
scene white with slow_dissolve
scene cg22_2 with dissolve
window show dissolve

"穿着端庄的校服坐在钢琴前，这已经让我足够难为情了。我实在无法想象，要是还要我为这一场合盛装打扮，那该有多么局促不安。"
"我甚至没有什么特别华贵的裙子。"
"尽管我男扮女装已有数月，可对女装我实在知之甚少。若是要我穿校服以外的任何衣服，我想我一定会方寸大乱。"
"其实，我已经开始心慌意乱了。"
"更多的人正陆续走进教堂。我能听见他们彼此低声交谈；每个声响都被教堂高耸的拱顶放大。"
"我能听见笑声、咳嗽声，还有某个我猜想是婴儿的啼哭声。"
"塞琳告诫我不要去看台下的听众。她说那只会让我更加紧张。她这话当然说得极对，可我仍旧忍不住抬起了头。"
"究竟来了多少人？"

show image "border" onlayer border
scene church:
    subpixel True
    size (1920, 1080) crop (0, 230, 1280, 720)
    linear 40.0 crop (400, 230, 1280, 720)
with wiperight_slow

"我粗略地扫视了一圈教堂，看来靠前的大部分长椅都已坐满了人。"
"在木质长椅后面，一颗颗脑袋露出，宛如业余花园里疏密不齐的花朵；他们彼此转过身交谈时，全都前后晃动着。"
"其中一些男人像是刚从田里回来的农夫。他们肤色黝黑，穿着马裤。"
"而那些女士，则来自各行各业。有几位打扮成优雅的贵妇，穿着晚礼服，戴着精致的帽子；但大多数似乎是前述农夫的妻子；她们梳着辫子，穿着廉价的棉布或亚麻布裙。"
"还有几位白发苍苍、满脸皱纹的老翁老妪，需要旁人搀扶才能坐下。这些人拄着拐杖或手杖，随后把手杖靠在身前的那排长椅上。"
"其中有位妇人看起来格外苍老枯槁，我真怕她在我们演出中途会化为一缕尘土。"
"除了年迈的，还有年幼的。"
"还有一群未满十岁的孩子，有的看起来兴奋不已，有的则在长椅上扭来扭去，缠着母亲；想必早已觉得无聊了。"
"还有几个还无法自行坐立的小婴儿，需要被母亲抱在怀里。"
"我认出了几张面孔（我想那是肉铺的伙计，而那个看上去像是菜贩），但我并不知道他们中大多数人的名字。"
"不过，我还是能认出阿梅莉。塞琳那位忠心的女仆正坐在最前排的一张长椅上，身旁是一个看起来有些眼熟的男人。"
"那男人肤色异常黝黑，目光锐利，面容英俊。"
"我不禁纳闷，究竟在哪里见过他呢？"
"我认不出这位神秘男子，却能轻易认出布吕吉埃夫人，还有杜布瓦小姐。"
"几位不屑加入合唱团的同学也到场了，米拉贝尔和诺艾米就在其中。她们和家人坐在一起，穿着便装。"
"米拉贝尔的父亲是个高大壮实的男人，脖子粗壮，前臂隆起。相比之下，她的母亲则逊色得多；与这位魁梧的丈夫一比，她简直是个纤弱的小女子。"
"看来米拉贝尔还有个弟弟。他有着和米拉贝尔一样的棕色头发和眼睛，脸上满是雀斑。"
"他依偎着姐姐，而她则微笑着握住他的手。"
"我想这里大概有八十……九十……或许一百人吧？"
"这数字不算庞大，但米延也不是什么大村子。"
"教堂还远未坐满，但也不算空无一人。只有最靠后的几排长椅完全空着，而就在我注视的当口，人们仍在陆续进来。"

hide image "border" onlayer border
scene cg22_2
with wipeleft_slow

"要在这么多陌生人面前演奏，这个念头实在让人别扭……"
"但这同时也令人心生谦卑。"
"我相信塞琳会对这样的到场人数感到欣慰。"
"她筹备这一切的时间非常仓促，可一切都安排得妥妥当当。现在说这话或许还太早，但我觉得这场音乐会必将大获成功。"
"我或许算不上一个自信的人，但我终究是演员的儿子。父亲的血液在我血管里流淌。我总该能装出一副自信的样子吧，哪怕只有一个钟头——可又有谁知道呢？"
"若我继续这样装作自信，或许有一天，我真的能将它化为现实。"
"正当我思忖着这些时，最后几个磨蹭的人才悄悄溜进教堂落座。"
# i should probably get another door sfx
play sound "sfx/door2.ogg"
"教堂那两扇宽大的木门终于合拢。伴着一声响亮而利落的闷响，声音在整座建筑中回荡。"
"会众安静下来，所有目光都投向教堂前端。"
"神父——一位眼神慈祥温和的长者——走上讲坛。他望着台下的会众，随即这样开口说道。"

scene church with wiperight_slow

Priest "我深感荣幸，在此圣婴降生的祥瑞之夜，向各位女士、各位先生，致以由衷的欢迎。"
Priest "看到我们的社群在这样一个夜晚团结一心，共度欢乐的庆祝与谦卑的祈祷，令我倍感欣慰。"
Priest "今晚，你们将有幸聆听本地女子唱诗班的动人青春之声。他们将为大家演唱八首曲目，这些曲子是他们为我们在整个冬天里精心打磨而成的。"
Priest "诸位都知道，米延的圣诞音乐会算得上是一项传统。我们在过去二十五年里一直坚持举办，从未中断，但今年却有些不同。"
Priest "在这所学校音乐女教师出了意外的……可以这么说，缺席之后——"
"听到这话，教堂里响起几声压抑的低语，男女们相互交换着鬼祟的眼神。"
"显而易见，农夫、工人和小店主们都很清楚勒梅尔小姐的境况。这想必早已成了人们议论的话题，不仅在校墙之内，也传遍了整座村庄。"
Priest "——校合唱团便被解散了。我担心今年不会有音乐会了，因为没有音乐，又何谈音乐会呢？"
Priest "然而，幸运的是，奇迹发生了。本地学校的学生们团结起来，借此把合唱团从灰烬中重新缔造出来。"
Priest "这支合唱团与你们去年复活节听到的那支颇有不同，尽管成员大体上仍是同样的天赋之辈。"
Priest "过去的合唱团由一位音乐女教师主持，而如今这支合唱团完全由学生们自己管理。"
Priest "高年级的女孩们夏季即将迎来考试。从学业上说，她们有太多事情要做，然而出于一片好心，她们仍决定投身音乐，奉献给我们的社群。"
Priest "她们确实是堪称楷模的年轻淑女，我希望诸位都能从她们的忘我精神中有所感悟。"
Priest "就我个人而言，我想祝愿她们在未来的努力中一切顺利……"
Priest "但现在，就让我们安坐于此，尽情享受他们辛勤劳动的成果吧。"
Priest "在他们演唱圣歌之间，会穿插圣经诵读和集体祈祷。如果诸位愿意以歌声赞美上帝，也将在几首众所周知的圣歌时被邀请一起吟唱。"
Priest "我希望诸位能在主的智慧与唱诗班的歌声中获得慰藉，从而带着满足的心离开这座圣殿。"
"神父走下祭坛，在其中一张长椅上坐下。随后，随着他一点头，塞琳站起身来。"

play ambience "sfx/footsteps.ogg" fadein 0.5
show celine neutral:
    xpos 1.10 xanchor 0.5 ypos 0.53 yanchor 0.5
    ease 2.0 xpos 0.5

$ renpy.pause(1.0)
stop ambience fadeout 0.5

"她朝教堂前端走去，那条素净黑裙的裙摆在她腿边飘动。"
"其余的同学跟在她身后，排成一列纵队。她们在祭坛前站成两排：最高者在后，最矮者在前。"
"塞琳面向听众，露出微笑，随后开始了她自己的欢迎致辞。"
Celine "非常感谢您，布卢安神父，谢谢您热情的介绍。您如此客气，我都要感到脸红了！"
"听到这话，教堂里漾起几声轻笑。"
show celine huh with dissolve
Celine "在布卢安神父讲完之后，我不确定自己还有什么可说的，所以我尽量说得简短些。"
show celine frown with dissolve
Celine "确实，在勒梅尔小姐离开之后，校合唱团被解散了相当长一段时间。能否重组一度成迷；这个事实让我深感遗憾。"
show celine sigh with dissolve
Celine "我本人并非米延人。我出生在奥尔良，在这里住了不过一年多。"
Celine "当我初到米延时，我感到非常不自在。我正值学业的倒数第二年，却被猛然抛入一个陌生的新环境。我怀念从前的同学，怀念从前的朋友。"
show celine sad with dissolve
Celine "对我来说那是一段艰难的日子。"
show celine huh with dissolve
Celine "勒梅尔小姐看出我处境艰难，于是向我伸出了援手。她邀请我加入校合唱团。"
show celine frown with dissolve
Celine "起初我有些迟疑。我担心自己无法融入，我很害怕，但勒梅尔小姐说服了我，我还是加入了合唱团。"
show celine neutral with dissolve
Celine "如今，我非常庆幸自己当时那样做了。"
Celine "我在合唱团短暂的时光里交到了朋友，而勒梅尔小姐更是以无人能及的方式让我感到被接纳。"
Celine "去年我参加了圣诞音乐会，复活节音乐会也是如此。我过得非常愉快，对那段时光怀有许多珍贵的回忆。"
show celine sad with dissolve
Celine "当我听说勒梅尔小姐已经离开，合唱团也随之解散时，没有谁比我更心碎。"
Celine "尽管我心烦意乱，却觉得自己也无可奈何。没有音乐女教师，重组合唱团是不可能的。当时我是这么想的，可很快我便开始思忖。"
Celine "也许到底还是有可能的，只要我能找到另一个女孩来帮我。"
show celine neutral with dissolve
Celine "我找了一位来自巴黎的新同学帮忙，就是玛塞尔·雷诺。唔……"
show celine smile with dissolve
"塞琳羞怯地笑了笑。"
Celine "我说‘请她帮忙’，不过‘死缠烂打’或许才是更准确的说法。"
"教堂里又漾起几声轻笑。"
show celine neutral with dissolve
Celine "我问她是否愿意协助我重组校合唱团的计划，她最终接受了我的提议。"
show celine huh with dissolve
Celine "唉，等待我们的可是一项艰巨的任务。我自幼便学习钢琴，而玛塞尔完全没有音乐基础。我不得不从零开始教她弹钢琴。"
Celine "在十月初，她对音乐还一窍不通……"
show celine neutral with dissolve
Celine "但在过去两个月里，我和她——连同这支新合唱团的诸位成员——都付出了一番努力，好让米延的人们能一起欢度圣诞节。"
show celine huh with dissolve
Celine "我只希望我们的演出能令诸位满意，尽管它或许略显业余。"
show celine neutral with dissolve
Celine "我永远无法取代勒梅尔小姐，我也不想取代她。她曾是——而且我相信如今依然是——一位极有才华的女性，但我希望我们自己的才艺也足以令诸位满意。"
Celine "今晚的第一首歌将是那首著名的圣歌，《{i}O Holy Night{/i}》。如果听众中恰有人会唱，请随意与我们一起歌唱。"
show celine huh with dissolve
Celine "好了……"
"塞琳瞥了我一眼。"
show celine frown with dissolve
Celine "我们这就开始吧。"
"于是，我们便开始了。"

scene cg22_2 with wipeleft_slow

"我稍作停顿，手指悬停在琴键上方。"
"随即，我开始弹奏。"

stop music fadeout 1.0
window hide dissolve
scene black with blinds2
$ renpy.pause(0.3)
$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  12月24日{vspace=1}  音乐会之后") )
play music "bgm/Night.ogg" fadein 1.0
scene sky_n with blinds2
window show dissolve

"令我大大松了一口气的是，这场圣诞音乐会进行得十分顺利。"
"正如所料，我出了一些差错，但我尽量不让自己为其所扰。我刻意不去理会那些失误而继续弹奏，而令我宽慰的是，它们也并非多么严重。"
"我确实进步了。"
"我弹奏时，齐聚于此的学校合唱团成员随之歌唱。她们甜美的嗓音与我的伴奏交融，浑然一体。"
"尽管我们合唱团只有十五名成员（不算我和塞琳），她们的歌声却足以充盈整座教堂。"
"她们的吐字清晰利落，经塞琳不倦的教导打磨而成，那乐音悠悠飘荡在空中，宛如飘落的雪花。"
"在唱那些更脍炙人口的赞美诗时，听众中的一些人也站起身来，与合唱团一同歌唱。男人们浑厚低沉的嗓音与合唱团较高的音域相映成趣，只是其中还夹杂着一丝粗粝。"
"我们以两首为一组进行演出。每唱完两首，神父（我想塞琳是称他为布卢安神父）便会站起身来，用他那洪亮的声音念上几段《圣经》。"
"随后，我们一同默默地祈祷，低着头，闭着眼。"
"一个小时后，音乐会落幕；在唱完{i}在牛与灰驴之间{/i}之后，我感到一种莫大的宁静。"
"音乐会前的那些天，我惶恐至极；但尽管心存疑虑，我仍是庆幸自己坚持了下来。"
"我在米延住得并不算久，但这是我头一次如此真切地感到自己融入了当地的乡里。"
"我在米延为自己挣得了一席之地。这里如今是我的新家，我很庆幸自己来到了这里。"
"我骤然搬来此地的缘由确实并不光彩，但无论如何，我还是找到了一些足以称之为自己的幸福碎片。"

stop music fadeout 1.0

scene church
show luce neutral:
    xpos 0.30 xanchor 0.5 ypos 0.5 yanchor 0.5
with wipedown_slow

play music "bgm/Classroom.ogg" fadein 1.0

Luce "……你做得很好。"
Marcel shock u "哦！"
"我合上钢琴，站起身，双颊泛红。"
"我太过沉浸在自己的情绪里，直到露丝站到我身旁，我才注意到她。"
"如今越过她的肩头望去，我能看到合唱团的其他成员已经开始散开。有的同学聚在一起闲聊，有的则走开去寻找自己的家人或校友。"
"曾一度笼罩这座教堂的宁静，如今已荡然无存。"
"整座建筑里再度充满了上百位村民欢快的交谈与随意的闲话。"
"歌唱的时刻已经过去，但我希望我们的心仍能彼此相连。"
"……如今，这话听起来未免太过感性了。"
"若是露丝知晓我此刻的心绪，我敢说她准会嘲笑我！"
show luce frown with dissolve
Luce "你没事吧，玛塞尔？你相当安静呢。"
show claudine smile:
    xzoom -1 xpos 1.20 xanchor 0.5 ypos 0.5 yanchor 0.5
    ease 1.8 xpos 0.70
Claudine "玛塞尔总是安安静静的！"
"克洛蒂娜蹦跳着来到我身边，咧嘴笑着，她常是这样。"
show claudine laugh with dissolve
Claudine "她一点都不像我以前见过的任何一个巴黎人！我姑妈萨比娜能把她当早饭吃掉！"
Marcel neutral u "您姑妈……？"
show luce sigh with dissolve
Luce "她住在巴黎。几年前的一个夏天，克洛蒂娜去她那里小住了一阵。她还为此喋喋不休呢。"
Luce "照她谈起姑妈时的那种口气，你会以为她那位圣人似的姑妈是基督再世呢。"
show claudine shock at bounce
Claudine "喂，露丝！在这神圣之夜的前夕，我们可不要妄称主的名！"
"克洛蒂娜戳了戳露丝的脸颊，露丝皱起了眉。"
show luce frown with dissolve
Luce "我想怎么说就怎么说。你又不是布吕吉埃夫人。"
show claudine smile with dissolve
Claudine "那真是谢天谢地！至少我还有幽默感！"
show luce sigh with dissolve
Luce "{i}现在{/i}又是谁在妄称主的名呢？"
"露丝撅起了嘴，可克洛蒂娜并不理会她，反倒一把搂住我的肩膀。"
show claudine laugh2 with dissolve
Claudine "不管怎么说，玛塞尔，你表现得棒极了！"
show claudine smile2 with dissolve
Claudine "你确实在这里那里犯了几个小错，但你的表演进步神速！"
Claudine "塞琳可要当心了！如果你照着这样的势头继续进步，说不定你会取代她，成为我们学校的音乐才女！"
Marcel shy u "哦——哦，我可不敢那么肯定……"
show claudine laugh2 with dissolve
Claudine "你太谦虚了！如果不是因为你，我们根本办不成这场音乐会！"
Claudine "清唱固然不错，但总归会让人觉得乏味！人们喜欢听点钢琴伴奏。它能活跃气氛——而这其实正合时宜，毕竟我们是在庆祝圣婴耶稣的降生！"
Marcel ehe u "嗯——嗯，呃……我很高兴我能不辱使命？"
show claudine smile2 with dissolve
Claudine "正是如此！你真成了整场演出的明星！"
"克洛蒂娜飞快地在我颊上亲了一下，让我羞红了脸，随即又退了开去。"
show claudine smile with dissolve
Claudine "好啦！我很想留下来好好夸夸你——你脸红的样子实在太可爱了，玛塞尔——但我好像看到我爸爸在那边了……"
show claudine annoyed with dissolve
Claudine "哦，还有杜普莱西先生，真是倒霉。"
"克洛蒂娜做了个鬼脸。"
show claudine huh with dissolve
Claudine "我谈不上多喜欢他，不过我想我还是去打个招呼为好。"
show luce smile with dissolve
Luce "杜普莱西先生？"
"露丝的唇角微微勾起，漾出一丝浅笑。"
Luce "就是那个向你求婚的可怜男人吗？"
show claudine sad with dissolve
Claudine "是啊，他求过。而且还不止一次。他已经揪着这件事说上好几个月了。"
show claudine neutral with dissolve
Claudine "你是怎么听说的，小露丝？我不记得跟你谈过这件事啊。"
show luce sigh with dissolve
Luce "我实在忍不住听见了。你跟诺艾米抱怨这件事时声音可大了。"
show claudine shock with dissolve
Claudine "作为一朵正值青春的花朵，我完全有权抱怨！我可不想被神圣的婚姻捆绑给那样一个老头子，真是{i}多谢{/i}了！"
show luce frown with dissolve
Luce "那要是他英俊呢？"
show claudine annoyed with dissolve
Claudine "{i}那{/i}就完全是另一回事了，可事实是他并不英俊。我也不妨告诉你，他并不富有，所以他给不了我任何东西。"
Claudine "唉，要是他不是我爸爸的助手就好了！那样的话，我就不必这么频繁地忍受他陪着我了！"
Claudine "要是他压根儿没来这场音乐会就好了……"
show claudine smile with dissolve
Claudine "不过，身为主角的我可不能让我的听众干等！告辞！"
"克洛蒂娜给我抛了个飞吻，随后蹦蹦跳跳地跑去迎接她的父亲和他那位助手。"

play sound "sfx/footsteps.ogg" fadein 0.5
show claudine:
    xzoom 1
with dissolve

$ renpy.pause(0.3)

show claudine:
    ease 1.8 xpos 1.20

$ renpy.pause(1.0)

show image "border2" onlayer border
scene church
show claudine smile:
    xpos -1.15 xanchor 0.5 ypos 0.5 yanchor 0.5
    ease 2.0 xpos 0.30
with wiperight_slow
stop sound fadeout 0.5

Claudine "爸爸，爸爸！您能来我太高兴了！我瞧您总算舍得把脑袋从那些伤风败俗的书里抬起来一回了！"
Laroche "那当然。我无论如何也不会错过圣诞音乐会，我亲爱的克洛蒂娜！你知道我最爱看你唱歌了！"
show claudine laugh with dissolve
Claudine "哦，爸爸！您真是太贴心了！"
show claudine annoyed with dissolve
Claudine "我希望您刚才也在听，杜普莱西先生！要是我听说您光顾着盯着我看，压根没留意我美妙的歌声，我可是会非常、非常生气的！"
Du "什么？"
"杜普莱西先生用手帕擦拭着发红的额头，双眼却愧疚地左右游移。"
Du "我、我……我怎会。我毕竟是位绅士，知道不该让您这样一位美丽的小姐感到难堪。"
show claudine neutral with dissolve
Claudine "唔……"
"克洛蒂娜抿了抿嘴唇。"
show claudine laugh with dissolve
Claudine "好了，不管怎样！见到您我真是太高兴了，爸爸！您已经太久没离开那间灰扑扑的旧书房了！"
show claudine smile with dissolve
Claudine "我们该一起挽着手走回家，就像我还是个小女孩时那样……"
show claudine shock with dissolve
Claudine "不过得先去跟亲爱的特茜打个招呼！我看见她在那儿了，费利克斯也在！"
show claudine smile with dissolve
Claudine "特茜！嘿，特茜！"
"克洛蒂娜隔着教堂大声呼喊，那架势无论就场合还是就气氛而言，似乎都不大合适。"
"幸运的是，并没有人为这事责骂她（尽管杜普莱西先生的脸确实红了）。"
"大家都在叽叽喳喳地说个不停，我想这点小事也就无伤大雅了。"

play sound "sfx/footsteps.ogg" fadein 0.5
show felix smile:
    xpos 1.20 xanchor 0.5 ypos 0.5 yanchor 0.5
    ease 2.0 xpos 0.85
show tessie smile:
    xpos 1.20 xanchor 0.5 ypos 0.5 yanchor 0.5
    ease 1.8 xpos 0.69
$ renpy.pause(0.5)
stop sound fadeout 0.5

Thérèse "哦，克洛蒂娜！我亲爱的克洛蒂娜！"
"克洛蒂娜的朋友朝她走来。那是个漂亮的年轻姑娘，年纪与我们相仿，长着一头红棕色的头发。"
"我在学校里从未见过她。要么她比我们高一届，已经通过了考试；要么就是她因身外之事而中途退学了。"
Thérèse "你唱得太精彩了！我真是太喜欢听你唱歌了！"
show tessie sigh with dissolve
Thérèse "说实话，我挺难过的，因为没法上去跟你一起唱。我以前最爱在学校合唱团里唱歌了！"
Claudine "我也想你，特茜。没了你作伴，学校里总觉得不是滋味，不过你不在这段日子，我可{i}一直{/i}拿诺艾米磨爪子来着。你也知道，她可厌恶我了。"
show tessie sad with dissolve
Thérèse "哎呀。你们俩还那么势同水火吗？"
show claudine smirk with dissolve
Claudine "我也没办法！是她自找的，谁让她总摆出那副傲慢自大、高人一等的做派！"
show felix laugh with dissolve
Fel "好了，好了！"
"特蕾莎的同伴（我想克洛蒂娜是称他为费利克斯吧？）笑了。"
Fel "这样说诺艾米小姐可不好！我还以为你们三个本该是朋友呢！"
"我看着克洛蒂娜与特蕾莎、费利克斯相谈甚欢、争得热火朝天。如今她背对着我，我实在听不清他们在说些什么。"
"数十人三五成群地站着，彼此聊着天。其中一些人群正陆续走出教堂，但他们挪动得极为缓慢。"
"我猜想，他们是不愿冒然走进那寒冷、狂风呼啸的夜色之中。"
"这里面暖和得多，也舒适得多。"
"不过，也确实吵得很。"
hide image "border2" onlayer border
scene church
show luce frown:
    xpos 0.30 xanchor 0.5 ypos 0.5 yanchor 0.5
with wipeleft_slow

Marcel neutral u "克洛蒂娜的朋友挺多的，不是吗？"
show luce sigh with dissolve
Luce "……算是吧。"
show luce frown with dissolve
Luce "我自己也弄不懂她有什么吸引力。她那么聒噪。"
Marcel ehe u "也许正因为她性子闹，大家才喜欢她吧？她挺容易相处的。"
Luce "她对着人{i}大发议论{/i}的天赋极高，可{i}与人交谈{/i}这门功夫，她却尚未掌握。"

stop music fadeout 3.0

Marcel "也许你说得有道理……"

show image "border" onlayer border
scene church:
    subpixel True
    size (1920, 1080) crop (0, 40, 1280, 720)
    linear 25.0 crop (400, 40, 1280, 720)
with wiperight_slow

"我扫视着人群，寻找塞琳的身影。自从音乐会结束、布卢安神父作了闭幕致辞之后，我就再也没见到她的踪影。"
"我想称赞她所付出的全部辛苦，可我连她在哪里都不知道，又怎么称赞呢？"
"我把头转来转去，左右张望，然后……"

play music "bgm/Friendship.ogg" fadein 1.0

Marcel shock u "哦！"
"终于，我看到了她。"
Marcel huh u "塞琳！打扰一下，塞琳……！"
"我朝她走去，却又顿住了脚步。"
"她并非孤身一人。"
"她正与某人交谈。那人比她高出不少，她得仰起头，才能迎上对方的目光。"
"塞琳的眼眸闪烁着，亮得我从未见过；她的笑容温暖得足以融化哪怕是最坚硬的心。"
"她看起来那么幸福，整个人都熠熠生辉——而她那满满的欢喜，全朝着她的同伴而去。"
"正是我先前见过、坐在阿梅莉身边的那位先生。他的年纪难以断定（或许三十出头？），但看上去并不显老。"
"他的肤色是深沉黝黑的那种，头发长到能拂过下颌。他肩背宽阔，下巴轮廓分明，一双眼睛是丰润的棕色。"
"他正是茹贝尔家那对双胞胎会为之倾倒的那类男人；性感又深情，简直到了骨子里。"
"我原以为他面熟，却直到此刻看见他和塞琳在一起，才认出他是谁。"
"我见过这个男人，只是并非真人。他栖身于塞琳的闺房之中；那张装框的肖像就立在她床头柜边、灯盏旁。"
"是瓦雷纳先生。"
"他怎么会出现在这里？我还以为他应该在奥尔良呢！塞琳说他自从搬走之后就没见过他。我不知道他们是否有书信往来，但想来是没有的。"
"那么，他又是怎么听说这场音乐会的？"
"是谁告诉他的？"

hide image "border" onlayer border
scene church
show amelie smile:
    xzoom -1 xpos 0.30 xanchor 0.5
with wipeleft_slow

Amelie "玛塞尔！又见到你真好，亲爱的。你干得太出色了！"
Marcel shock u "啊、哦……"
"我用力把目光从塞琳和她那位英俊的钢琴老师身上移开，转而看向阿梅莉。这位好心肠的管家在人群中认出了我，因为她正站在我身边。"
"我朝她微笑（至少，我尽力去笑），回应着她的好意。"
Marcel smile u "见到你我也很高兴，阿梅莉。谢谢你的夸奖。只是我不太确定自己配得上这份称赞。"
Marcel ehe u "我犯下的错误，远比应有的为多。"
show amelie laugh with dissolve
Amelie "就算有，我也没注意到！"
Amelie "你的钢琴不如那位年轻小姐那般精湛，但依然迷人！"
Amelie "跟着你的伴奏唱歌，我可开心了！我本就爱唱，可塞琳说我的歌声太不着调，已经禁止我在宅子里唱了！"
Amelie "我想是我对高雅艺术的糟蹋惹恼了她。"
"阿梅莉轻声笑了起来。"
show amelie smile with dissolve
Amelie "我觉得你弹得棒极了，不过请别只听我一家之言。我们何不去问问专业人士呢？"

play ambience "sfx/footsteps.ogg" fadein 0.5
show amelie:
    ease 1.0 xpos 0.80

$ renpy.pause(0.8)

show amelie:
    xzoom 1 xpos 0.80 xanchor 0.5
show celine neutral:
    xzoom -1 xpos -1.0 xanchor 0.5 ypos 0.53 yanchor 0.5
    ease 2.8 xpos 0.35
show marius neutral:
    xpos -1.10 xanchor 0.5
    ease 3.0 xpos 0.18
with dissolve

$ renpy.pause(1.6)
stop ambience fadeout 0.5

"阿梅莉领着我朝塞琳和瓦雷纳先生走去。而我却落在后面，脚步迟钝而沉重。"
"我实在不太想去问候塞琳的心上人，可我又有得选吗？"
"拒绝只会显得失礼，而我也没有回避瓦雷纳先生的理由。我甚至根本不认识他。"
"据塞琳所说，他是个彬彬有礼、举止得体的绅士——可为什么我待在他身旁，就浑身不自在呢？"
show celine smile with dissolve
Amelie "塞琳小姐，我已把玛塞尔从人群里带出来了。你有什么话想对她说吗？"
show celine huh with dissolve
Celine "玛塞尔！"
show celine:
    ease 0.8 xpos 0.5
"塞琳从瓦雷纳先生身边走开，随后带着微笑朝我走来。"
show celine smile2 with dissolve
"她以一种敷衍的拥抱环住我（即便我们分开时，我也能闻到她的香水味），然后在我两颊各落下一个轻快的吻。"
Celine "哦，玛塞尔！谢谢你的鼎力相助！没有你，我根本办不成这件事！"
Celine "音乐会办得很成功，你觉得呢？我度过了非常愉快的时光，全都多亏了你——快看！"

show celine neutral:
    xzoom 1
with dissolve

"塞琳从我身旁退开，朝瓦雷纳先生打了个手势。他面对这番举动，显得有些局促。"
Celine "你当然应该认识这位！我跟你说过不少关于他的事！"
show marius smile with dissolve
Va "是吗？天哪！真是荣幸！"
"瓦雷纳先生笑了。他的笑声醇厚而温暖，一如他的嗓音，我甚至发觉自己听着听着便红了脸。"
"难怪他能攫住塞琳的心。若我本人也是个女子，或许也会为他倾心吧。"
Va "小姐，我希望你只跟朋友们说了我的好话。我可不想有关于我那些，呃……风流韵事的传闻……传遍整个法国。"
Celine "是朋友，单数。我只告诉过玛塞尔关于你的事，因为我太信任她了——何况，你大可不必担心。"
Celine "你是个善良的人。你没什么可羞愧的；至少，{i}我{/i}不这么认为。"
show marius sigh with dissolve
Va "恐怕令尊不会这么想。若是他知道我到这儿来看你，怕是会火冒三丈。"
show amelie laugh with dissolve
Amelie "哦，圣柯尔先生对什么都不太赞成。我才不会把他放在心上。他远在奥尔良呢！"
Amelie "我们可以把这件事瞒下来，只在我们之间。他永远也不会知道！"
show marius neutral with dissolve
Va "那或许是最好的办法，尽管我一向不擅长保守秘密。"
show marius sad with dissolve
Va "我仍不太确定，我到这里来是否妥当……"
show marius smile with dissolve
Va "但当你写信给我时，热拉尔夫人，我就知道我不能不来。"
Va "我已经很久没见过你和塞琳小姐了。我一直很想知道你们俩近况如何。"
"啊。我想这大概就解释了瓦雷纳先生何以会来到米耶纳。知晓塞琳一切往来的阿梅莉，想必给他写了封信，告知这场即将举行的音乐会。"
"我不清楚她是如何打听到瓦雷纳先生的住址的（或许她去问过塞琳在奥尔良宅邸里的女仆们？），不过我想具体的细节倒也不打紧。"
"阿梅莉写了信，瓦雷纳先生收到了，于是他决定来赴这场音乐会。"
"说穿了，就是这么简单。"
show marius sad with dissolve
Va "你还好吗，塞琳？我一直非常担心。你当初离开奥尔良的情形，实在算不上顺遂……"
Celine "我还好，先生；真的，我还好。"
show celine huh with dissolve
Celine "我承认，刚安顿下来时确实有些难处，可、可这几个月真是乐趣多多。"
show celine neutral with dissolve
Celine "我每天都练习音乐，就跟在你身边时一样，而且我还交了玛塞尔这样一位好朋友。"
Celine "她陪着我，让我不再孤单。"
Celine "多亏了她的帮助，我才能办成今晚的圣诞音乐会。没有她，我可真不知如何是好。"
show celine smile with dissolve
Celine "我十分在乎她……能遇见她，我真的很高兴！"
Marcel shockblush u "塞、塞琳……"
"我的脸颊开始发烫。"
"我早知道塞琳在乎我，可听她如此直白地说出来，还是叫人难为情。"
"不过，我倒并不为此感到不快。事实上恰恰相反。"
"我只希望我的心别再这样狂跳个不停。"
Marcel ehe u "我……也很高兴你遇见了我。"
Marcel "为今晚的音乐会做准备，我有很多乐趣。那是件苦差事，却很有意义。我但愿自己能发挥出更好的水准……"
show marius smile with dissolve
Va "是玛塞尔小姐吗？很抱歉我迟迟没有自我介绍。我一整天都在赶路，担心自己有些不在状态，不过这当然不能成为失礼的借口！"
Va "很高兴认识您。"
"瓦雷纳先生对我微微一笑。"
Va "塞琳已经跟我说了不少你的事——而且，你也知道，就在不到十分钟前，我还有幸聆听你的演奏呢！"
Marcel shockblush u "荣幸？哦，不不……"
"一想到我那业余的琴音，不仅被米耶纳的村民们听了去，还被一位拥有二十多年教龄的钢琴老师听到，我就简直羞惭欲死。"
"倘若人真能羞愤而亡，我想此刻我就会倒在瓦雷纳先生的脚边了。"
Marcel shy u "我、我这琴艺一定很糟糕。很抱歉让您忍受了我那业余的演奏。但愿不算太糟糕吧？"
show marius neutral with dissolve
Va "道歉？为什么要道歉？考虑到你排练的时间那么少，我认为你表现得很好！"
show amelie smile with dissolve
Amelie "看吧？"
"阿梅莉骄傲地挺起了胸膛。"
Amelie "我早跟你说过什么来着，玛塞尔？你比你想象的要好！你得更有自信才行！"
show marius smile with dissolve
Va "自信确实是关键。多一点自信会大大有助于提升你的琴艺，然而鉴于你练习的时间如此之少，还能弹得这样，实在令人赞叹。"
Va "任何水平的钢琴演奏，我都喜欢听。每个人都会把自己的个性融入演奏之中。我们都有想要表达的东西，正因如此，每一段音乐都是独一无二的。"
Va "没有任何两场演奏会是完全相同的……哦，就拿{i}《圣善夜》{/i}来说吧，即便用的是同一份乐谱。"
Va "这正是音乐之所以如此美妙的原因——至少在我看来是如此！"
Marcel "美、美妙？我并不……"
"我的脸烧得越来越红。"
show celine smile2 with dissolve
"与此同时，塞琳笑着挽住了我的手臂。"
Celine "求您了，先生，别再说了！我看可怜的玛塞尔怕是吃不消这么多夸奖！您要是再这么待她，可真会把她夸死的！"
show marius shock with dissolve
Va "夸死她？"
"瓦雷纳先生瞪大了眼睛。"
Va "哎呀，我绝没有那个意思！我可不是为了夺走你最好的朋友才来米耶讷的！"
show marius neutral with dissolve
Va "关于你的琴艺，玛塞尔小姐，我这就暂且闭嘴……"
show marius smile with dissolve
Va "但我想谢谢你，你对塞琳这么好。"
Va "自从她离开奥尔良，我就一直为她担心。她一生中承受了太多，我只希望她能幸福。"
Va "把她送到这样一个远离故乡和朋友的偏僻小村，我本不确定她能否寻得幸福……"
Va "但看到我的担忧是多余的，我也就放心了。"
Va "这世间，好的朋友并不易寻。你们俩之间的情谊很特别。我只盼它能长久地延续下去。"
show celine neutral2 with dissolve
Celine "我相信会的。"
show celine smile2 with dissolve
Celine "为了这场音乐会，我可没少折腾玛塞尔，而她至今没厌烦我。我觉得，这对将来来说是个好兆头！"
Marcel shock u "当、当然不会厌烦你！绝不可能！"
show celine neutral2 with dissolve
Celine "那就这样说定了！我们往后会做好长好长的朋友——所以你看，瓦雷纳先生，你也不必再为我操心了！"
Celine "我确实想念你，这是真的……但我不再孤单了。再也不了。"
show celine smile with dissolve
Celine "我好久好久没有这么快乐过了！"

stop music fadeout 1.0
window hide dissolve
scene black with wiperight_slow
$ renpy.pause(0.3)
$ save_name = (__("{u}塞琳篇{/u}{vspace=1}  12月24日{vspace=1}  我所求唯有你") )
play music "bgm/Night.ogg" fadein 1.0
scene sky_n with wiperight_slow
window show dissolve

"那晚我没有回学校。塞琳反倒邀我去了她家，好让我们能多待在一起。"

window hide dissolve
scene white with dissolve
$ renpy.pause(0.3)
scene church g:
    size (1920, 1080) crop (240, 40, 1440, 810)
show celine neutral2 g:
    xpos 0.5 xanchor 0.5 ypos 0.53 yanchor 0.5
with slow_dissolve
window show dissolve

Celine "我们的音乐会大获成功，全都因为有你相助。你待我真好，玛塞尔……"
Celine "而我也不想我们这么快就说再见。"
Celine "阿梅莉昨天又烤了苹果派，还剩一些。我把最后那一块留给你，我知道你多爱吃。"
Celine "那就算给你的奖赏——而且，我也许你睡我的床哦！"
show celine smile2 g with dissolve
Celine "我的房间总该比你睡的那间暖和些吧？"
"这是塞琳说的，而她同我说这话时神情如此真挚，叫我根本没法回绝她的邀请。"

window hide dissolve
scene white with slow_dissolve
$ renpy.pause(0.3)
scene sky_n with dissolve
window show dissolve

"我回到塞琳那简陋的住处，手臂与她相挽。到了那里，阿梅莉端来最后一块苹果派，外加一杯加了牛奶的茶。"
"派本身已经凉了，因它在食橱里搁了一整夜；饼皮酥脆可口，香料苹果依旧美味。"
"吃完了东西，阿梅莉又为我和塞琳放好了洗澡水。"
"我在浴盆里享受了至少半个钟头，任一日的疲惫从肩头滑落。"
"洗过、擦干之后（因为头发实在太长，擦干总要多费些时候），我披上了阿梅莉为我备好的睡裙。"
"这条裙子，我猜是塞琳的。裙摆有些短，在小腿上方几厘米处就打住了，不过我想倒也无妨。"
"这屋里没有男人会来偷看我——除了我自己之外，我想。"
"我不必担心塞琳的想法。自我们初次相见以来，她对我一直体贴而周到。"
"几个月前，我初次在教室里见到她时，从未想过我们会变得如此亲近。我一度害怕自己永远交不到朋友，如今看来是我错了。"
"塞琳和我之间，已结下一段牢不可破的情谊。我们一起经历了许多：那苦不堪言的钢琴练习化作合唱排练，随后又有了那场成功的（若容我自己夸口的话）圣诞音乐会。"
"感觉我们算是做成了一番了不起的事，而我们的情谊也因之愈发深厚。"
"塞琳如此信任我，甚至让我用她的浴盆洗澡，穿她的睡裙，还睡在她的床上。"
"从某种意义上说，我们简直像一对姐妹——可那真是我想要的吗？"
"虽然我替塞琳能与她昔日的钢琴老师重逢而高兴，可当我开口说话时，心里确实有什么东西紧紧揪了一下。"
"如今我已确信无疑，那必定是嫉妒。"
"而说到塞琳昔日那位钢琴老师……"

scene celine_room_n blur:
    size (1920, 1080) crop (0, 60, 1152, 648)
show celine n sad3 n:
    xpos 0.50 xanchor 0.5
with wipedown_slow

# marcelle needs an alt nightgown sprite
Marcel neutral n2 "塞琳……"
"我们俩正并排躺在塞琳的床上，被子拉上来盖住我们。塞琳在我之后洗了澡，头发还湿着；她那一头深色的发绺（难得地披散着）自由地卷曲在脸旁。"
"她的睡裙是加了奶的咖啡的颜色，上面点缀着恰到好处的荷叶边与缎带。"
"即便在黑暗中，她也显得异常动人；月光透过她半掩的窗帘滑入，照出她侧脸的轮廓。"
"阴影在塞琳眼窝的凹陷处汇集成潭。她的虹膜比以往任何时候都更深邃、更神秘。"
"我们靠得如此之近，我能感觉到她香甜的气息拂过我的脸颊。只要我愿意，就能伸手探进被子里去牵她的手……"
"可我没有。"
"我们一起弹钢琴时，我们的手指或许曾无数次擦过彼此，但我认为现在去牵她的手并不合适。"
"我想那太过唐突了。"
"我知道塞琳珍惜我的陪伴（她必定如此，才肯让我睡在她床上），可她对我，是否有那样的情意呢？"
"我不知道。"
"她从未像看她那位昔日钢琴导师那样看过我。"
show celine n huh3 n with dissolve
Celine "玛塞尔？"
"塞琳慵懒地眨了眨眼。我想她一定是快睡着了，因为她的嗓音里带着沉沉袭来的睡意。"
"我不怪她疲倦。在音乐会筹备的那段日子里，我们着实练得苦极了。"
"如今音乐会结束了，塞琳的气力似乎也终于开始见底。"
"我大概该让她好好歇歇。"
"若我是个贴心的朋友，就该搁下这个话题。我会说一声“算了”，然后向她道晚安——可就算我这么做，我也怀疑自己能否睡得着。"
"我有太多话想对她说。"
"我再也无法把自己的心事藏在心里了。"
Marcel "我知道夜深了，很抱歉打扰你，但我想知道……"
Marcel huh n2 "音乐会结束后，瓦雷纳先生上哪儿去了？"
show celine n frown3 n with dissolve
Celine "嗯？"
"塞琳在黑暗中朝我眨着眼。我想她一定是困了，因为她花了好一会儿才消化这个问题。"
"她答话则更久，其间睫毛一直撩人地颤动着。"
show celine n sigh3 n with dissolve
Celine "他当然是回家了。"
Marcel frown n2 "回家？你说的是奥尔良吗？"
show celine n huh3 n with dissolve
Celine "是这样。"
Marcel huh n2 "什么？可奥尔良离这儿太远了……"
"我对法国的地理知识谈不上多好，但那些最大的城市在哪，我大体还是知道的。米耶纳离奥尔良颇有一段距离，不过倒还没有巴黎那么远。"
Marcel "何况天色已晚。他要是能留下来过夜，岂不更好？"
show celine n frown3 n with dissolve
Celine "那你倒说说，他该住哪儿？米耶讷可没有旅馆。"
Marcel "这倒也是，我想……"
Marcel frown n2 "可他也不算外人。我在教堂见到他时，还以为你会想尽可能多跟他待在一起呢。"
Marcel "你为什么不让他留下来？"
Marcel "他一路上千辛万苦赶来米耶讷，结果几个时辰后又匆匆折返家中，未免太可惜了。"
show celine n huh3 n with dissolve
Celine "噢，天哪……"
"我那一番情真意切的剖白，想必帮塞琳驱散了最沉的困乏，因为此刻她看上去比先前清醒多了。"
show celine n frown3 n with dissolve
"她眉头微蹙，开口说道……"
Celine "我真没料到你会这么关心瓦雷纳先生，玛塞尔！哎呀，你们俩可是素不相识！你们才说过几句话呢！"
Celine "你可真是个好心的姑娘！"
Marcel neutral n2 "我、我打听他，不是因为{i}我{/i}关心他；我问是因为我知道{i}你{/i}关心他。"
Marcel "你想他了，对吧？"
show celine n sigh3 n with dissolve
Celine "……是的，我想他了。我很想他。"
Marcel huh n2 "那你为什么邀请{i}我{/i}去你家，却不请他？"
Marcel "你随时都见得到我。我们住同一个村子，又上同一所学校。我真的没什么特别之处。"
Marcel "可你是爱着瓦雷纳先生的。你亲口向我承认过。"
Marcel "你说过，他是你生命中最重要的人之一。"
Marcel frown n2 "我不明白你怎么能就这样放他走了。"
show celine n frown3 n with dissolve
Celine "哦，玛塞尔。"
"塞琳咂了咂舌。"
Celine "你是个贴心的姑娘，我知道你是好意，可你在这些事情上实在太天真了！"
Marcel neutral n2 "那我大概是够天真的，因为我实在弄不懂你为什么要这么做。"
Marcel "塞琳，你{i}真的{/i}对今夜这样的结局感到满意吗？"
show celine n sigh3 n with dissolve
Celine "我……还好。"
"塞琳叹了口气，那声气让我不由得揣度，这“没事”究竟有几分真。"
"今夜，她与她那般痴恋的男人重逢了。然而，不到一个钟头之后，他又一次离她而去。"
"塞琳始终没机会向他表白心意。据我所知，没有泪水，没有拥抱，更遑论亲吻。"
"塞琳与瓦雷纳先生的重逢是场纯洁无瑕的会面，不讲究任何仪式。"
"塞琳一直尽力装作不受这一切影响，可我怀疑她的微笑并不足以表明她真实的感受。"
"她难道不难过吗？"
"我知道换作是在她的处境，我定会难过。"
Marcel sad n2 "你确定你没事吗？"
show celine n frown3 n with dissolve
Celine "我确定。"
Marcel neutral n2 "那你难道连请他回你家住一晚的念头，都没起过？"
Marcel "他又不是非得睡在你同一张床上。你不是有间客房吗？"
show celine n sad3 n with dissolve
Celine "有是有。其实，我确实考虑过——我怎么可能会不想呢？——但是……"
"塞琳顿了顿，目光先瞥向左边，又落向右边。"
"虽然我看不进塞琳的脑瓜，但我知道她一定在掂量着自己的话；思忖着接下来该说什么。"
"这一夜是凯旋与欢庆之夜，却也充满意外。还有悲伤。"
show celine n huh3 n with dissolve
Celine "可到头来，我知道那是不可能的。"
Celine "我和阿梅莉商量过这件事，我们俩一致认为那样做不妥当。"
Marcel huh n2 "让你从前的音乐老师住一晚，怎么就不妥当了？我不明白。"
show celine n neutral3 n with dissolve
Celine "哦，真的吗？"
"塞琳淡淡地笑了笑。"
Celine "换作任何别的女人，都能一眼看明白。我想就连米拉贝尔——她虽然迷迷糊糊——也该懂我的意思。"
Celine "你说出这种话来，真让我怀疑你到底是不是个女人……"
show celine n sigh3 n with dissolve
Celine "不过没关系。如果这个道理对你来说太复杂，那我就勉为其难地解释给你听。"
"塞琳深吸一口气，被褥之下的胸口随之起伏，随后才继续开口。"
show celine n frown3 n with dissolve
Celine "要是让人知道我留了一个英俊的青年男子在我家过夜，人们定会议论纷纷——相信我，他们{i}一定会{/i}知道的。"
Celine "米耶纳是个小村庄，人人都认识彼此。他们也晓得别人都在干些什么勾当。"
Celine "在这样的地方，想守住秘密是不可能的。"
Celine "我不想冒险毁掉自己的名声；更何况我来这里，就是为了躲开那些在奥尔良流传的、关于我的恶毒谎言。"
show celine n shock3 n with dissolve
Celine "哎，我甚至可能被人当成轻浮的荡妇！"
show celine n sad3 n with dissolve
Celine "而且，无论如何，瓦雷纳先生都必须离开。他没法留下来。"
Marcel neutral n2 "为什么？"
Celine "我并不是他唯一牵挂的人。我们之间的关系确实亲密，可我们终究不是一家人。"
Celine "也许他把我当成某种意义上的朋友，可他在奥尔良有位已定下婚约的未婚妻，正等着他回去。"
show celine n sigh3 n with dissolve
Celine "我怀疑，如果她知道自己的未婚夫曾在从前学生的家里过夜，她不会高兴——{i}更何况{/i}这个从前学生还是大名鼎鼎的塞琳·圣科尔！"
Celine "关于我们的流言在街上早已沸沸扬扬，实在不必再火上浇油了！"
Marcel shock n2 "什么……？我不知道他有未婚妻！"
show celine n frown3 n with dissolve
Celine "我今晚之前也不知道。这着实是个意外。"
Celine "你知道，我不是那种在男人已经被别人占有时还会对他想入非非的女孩子。我可远没有诺艾米那么不知廉耻。"
Marcel "我、我从没说过你是！"
show celine n neutral3 n with dissolve
Celine "我知道。我只是逗你玩。你的脸那样泛红的时候，看着可真好看！"
Marcel sigh n2 "我、我自己倒不觉得有那么好看……"
"我叹了口气。"
Marcel neutral n2 "那么，瓦雷纳先生是什么时候认识这位女士的？我猜这是最近才发生的事。"
show celine n huh3 n with dissolve
Celine "我想是的。"
Celine "据我所知，瓦雷纳先生是在我搬到米耶纳之后不久认识她的。"
Celine "她是他入院时那家医院的护士之一——就是他与贝尔热拉克先生发生那场争执之后住的院。"
Celine "她为他包扎伤口，两人便这样建立起某种情谊。"
Celine "他们几乎天天见面，时常交谈，等到双方都还没回过神来的时候，就已经坠入了爱河。"
Celine "交往一年后，瓦雷纳先生就求了婚，她自然是喜出望外，一口答应。"
Celine "婚礼定在明年夏天。那会是一场小型婚礼，只有几位至亲出席，但瓦雷纳先生非常兴奋。"
"塞琳以一种背熟了般的、机械的口吻说出这段话来。她看起来如此心不在焉，简直像是在课堂上念一段福楼拜的课文……"
"可这，同样只是一场戏。"
show celine n sad3 n with dissolve
"当她停下来时，我能看见她眉间的褶皱。"
"她得先颤抖着吸进一口气，攥着被角的手指也微微抽动，才能最终继续说下去。"
Celine "当他谈起她、谈起与她共同的未来时，他的脸像个小男孩一样焕发光彩。他看起来完完全全地入了迷。"
show celine n sigh3 n with dissolve
Celine "嗯……对他来说，这是好事。我很高兴他这么幸福。我相信他会成为一个很棒的丈夫。"
Marcel sad n2 "哦，塞琳……"
"塞琳脸上那痛苦的神情在我心里拨动了一根弦，正如一根绷紧的钢琴弦定会鸣响出一个音符。"
"说句不客气的大实话，我其实盼过会发生些这样的事。"
"当我最初得知塞琳爱着（而且确实是仍爱着）她那位昔日的钢琴老师时，我被嫉妒攫得心头作呕。"
"我曾以一种自己幼稚的方式，以为她那份情意是归我所有、且只归我一人所有的。我不喜欢与人分享我的第一位朋友——连与一段记忆共享也不愿意——可是……"
"如今我明白瓦雷纳先生不会、也绝不会回应塞琳的心意，我不禁替她感到难过。"
"塞琳很擅长把自己的心思藏着掖着，这常常叫人难以洞悉她的真实情绪，可此刻她的伤痛却已明显得令人心疼。"
Marcel "那一定是个不小的打击。我希望你别太难过……"
show celine n frown3 n with dissolve
Celine "我{i}确实{/i}很难过。我想否认也否认不了，尽管我已经试着去否认了。我知道，现在这一切显得很傻，可我原以为瓦雷纳先生和我之间有着某种特别的东西。"
show celine n sad3 n with dissolve
Celine "即便是在被放逐到米耶纳之后，我仍然天天想他。他从没有离开过我的脑海。"
Celine "我之所以在学校合唱团唱歌，是因为我对他的那份余情未了。我曾想让他为我感到骄傲。我曾希望，若我们再度相遇，他会明白我是为了他才这么拼命，明白他对我而言有多重要。"
Celine "我曾做梦……"
"塞琳摇了摇头。"
show celine n sigh3 n with dissolve
Celine "可我现在明白了，我那些梦全都幼稚得很。"
show celine n sad3 n with dissolve
Celine "我曾以为他也许会爱我，就像我爱他那样，可与他相比，我还是个年轻姑娘。他几乎比我大二十岁！"
Celine "是的，他待我很好，可我不认为他待我好是因为爱我。他对我好，是因为他怜悯我——怜悯我有一个那么严厉的父亲——他想让我开心起来。"
Celine "我把他的疼爱错当成了浪漫的爱情。他从没做过任何事来助长我这些妄想。这一切都只是我一厢情愿。"
Celine "我太渴望他回应我的感情了，以至于用我自己爱的滤镜去曲解一切。尽管我口口声声说在乎他，我想我从来都没有真正看清过他。"
Celine "我真蠢……"
show celine n neutral3 n with dissolve
Celine "可如今，我的眼睛终于睁开了。"
Celine "被拒绝{i}确实{/i}很痛，但我想这或许是最好的结果。既然我知道瓦雷纳先生已有未婚妻，我也就能不再奢望他会回应我的感情了。"
Celine "我生命中的那一章，到此彻底翻篇了。"
"塞琳朝我笑了。她的笑容在嘴角处显得很虚弱，我能看见水珠正缀在她的睫毛上。"
"她正努力坚强，可哪怕是她自己的意志，也抚慰不了那颗碎裂之心的疼痛。"
"瓦雷纳先生是塞琳的初恋。自六岁那年懵懂初开地遇见他起，她便崇拜着他。"
"她对钢琴老师的这份情愫随着岁月滋长；每过一年都在她心底扩张，直到她几乎无法遏止。"
"如今，这一切轰然崩塌了。"
"塞琳说服自己，相信瓦雷纳先生爱着她，正如她爱着他一样，因为这样相信会让她幸福——但那，正如她此刻所发现的，不过是一场缥缈的白日梦。"
show celine n huh3 n with dissolve
Celine "我很庆幸自己知道了。真的，我很庆幸。一直那样执迷地活在自己的幻想世界里，实在是很不健康的。"
show celine n sad3 n with dissolve
Celine "事情本该如此，可是……"
"塞琳的强撑勇气动摇了。她的眼里又泛起更多的泪水，开始顺着脸颊滑落。"
"她屏住一口气。她喘息着，仿佛快要死去，然后哭喊出声……"
show celine n shock3 n with dissolve
Celine "我一直在这样劝自己，可它还是痛！我胸口疼得厉害，我都不知道该怎么办才好！"
show celine n sad3 n with dissolve
Celine "我现在拿自己怎么办才好？我还能去爱谁呢？"
Celine "会有人{i}终究{/i}爱上我吗？"
Celine "我觉得自己真是个傻瓜！"
Marcel sad n2 "塞、塞琳，求求你……别哭成这样。我会陪在你身边的。"

stop music fadeout 1.0

window hide dissolve
play music "bgm/Confession.ogg" fadein 1.0
scene cg24 with wiperight_slow
$ renpy.pause(1.0)
window show dissolve

"怀着安慰塞琳的心念，我发觉自己跨过了我们之间的那段距离。我不再顾虑应当保持距离，而是环住她的背，把她揽入怀中，贴近自己。"
"让我宽慰的是，塞琳没有试图挣脱。她反倒朝我瘫倒过来，自己的手臂也环上了我的腰。"
"她紧紧地缠着我，就像一个溺水之人死死抓住一块浮木。"
"我们靠得如此之近，双腿在被下交缠。透过睡裙的布料，我能感到塞琳肌肤的温暖。而她披散的发卷那般柔软，正拂过我的脸颊。"
"塞琳仍在抽泣，可我觉得她看起来很美。"
Celine "玛、玛塞尔……哦，玛塞尔……"
"塞琳沮丧地抽噎着，随后用断断续续、近乎恳求的语调说道……"
Celine "我、我很抱歉。我这样子一定很难看吧！"
Marcel "没事的。我觉得你看着就很完美。"
Celine "你、你骗人。"
Celine "要、要是再这样下去，我都会把你睡衣的前襟哭湿了！"
Marcel "没事的。反正那也不是我的睡衣。是你送给我的。"
Celine "我、我知道，可你正穿着它呢……哦！我不想让它沾满眼泪，还有我自己的鼻涕。那会{i}尴尬{/i}得要命。"
Celine "说实话，这{i}一切{/i}都太尴尬了。我、我简直像个被宠坏的孩子！"
Celine "瓦雷纳先生对我不感兴趣，这有什么好奇怪的？他、他是个真正的成年人了。跟他相比，我不过是个婴儿！"
Celine "玛塞尔，我常常说你天真，可至少你足够聪明，不会去追求一个比你年长二十岁的男人！"
Marcel "没事的。塞琳，我不会评判你。你想哭多久就哭多久。不管你把这件睡衣的前襟哭得有多湿，我依然会在乎你。"
Celine "啊……"
"塞琳凝视着我。她因哭泣而泛红的双颊，涨成了更深的粉色。"
Celine "你这样说的时候，你、你听起来简直像一位英俊的王子……"
Marcel "那样不好吗？"
Celine "我、那……很奇怪……"
Celine "我的心本来就够脆弱了。你、你要是再在我耳边说这些甜言蜜语，我说不定会晕过去！"
Marcel "我觉得不会有那种危险。你太坚强了，不会的。"
Celine "我不坚强。我很软弱；软弱得无可救药。"
Marcel "你也许这么觉得，但我可不这么想。"
Marcel "我知道你现在很难受，但我相信你一定能挺过去。你是个坚强的人，从不会在逆境面前屈服。"
Marcel "你骄傲而高贵……{w}而且我觉得你很美。"
Celine "玛、玛塞尔……"
"塞琳眨了眨眼。"
"她深色的睫毛因泪水而黏成一簇簇。当她眨眼时，更多的咸涩泪珠自她的睫毛上被抖落下来。"
"她看上去简直悲痛欲绝，可我仍旧敬慕她。"
"我{i}爱慕{/i}她。"
Celine "这个问题也许听起来很奇怪，可是……你喜欢我吗？"
Marcel "我很喜欢你。你是我最好的朋友。"
Celine "不、不，我……我不是那个意思。我是想问，就像……嗯……"
"塞琳深吸一口气。"
Celine "你……对我……是不是像我当初喜欢瓦雷纳先生那样？"
Marcel "诶、诶？"
"我盯着塞琳，完全摸不着头脑。"
"我没想到她会提出这样一个问题……{w} 但也许，以我们这般亲近，这也在所难免。"
"我不太了解女人之间的友谊，但直觉告诉我，这种亲密程度并不寻常。"
"我一心想要安慰塞琳，想必让我的心事表露得太明显了。"
Marcel "有那么……明显吗？"
Celine "是的，很明显。说实话，我已经疑惑好一阵子了。练琴时每每我们的手相触，你总会脸红着躲开。这让我想起当年的自己，想起我和瓦雷纳先生在一起的时候……"
Celine "我们在一起时，我也就是那样的感受。"
Celine "我的心会开始怦怦直跳，随后嘴巴发干。我总是飞快地躲开他，希望他不会察觉，可事后回想起来，那一定是非常明显的。"
Celine "我很不擅长掩饰自己的感情——你也是一样。"
Celine "我想你一定喜欢我。这就是你一直为了我如此拼命付出的缘故。"
Celine "你……爱上我了，对不对？"
Marcel "……嗯，没错。"
"我凝视着塞琳澄澈的眼睛。我担心会从她炭黑的瞳孔里看到某种坚硬的、钢铁般的东西（也许是拒绝？），但令我欣慰的是，她的神情很温柔。"
"她没有听我开口，就已窥破了我心意的真相，但她至今没有尝试把我推开。"
"这种默许的认可，给了我继续说下去的勇气。"
"现在或许不是向塞琳坦白的最佳时机，但我想让她知道我的感受。"
"我想让她知道关于我的真相。"
Marcel "起初我自己也拿不准自己的感情。我以前从没对别人有过这种感觉，所以才犹豫不定。这对我来说很陌生，但我{i}的确{/i}爱你，塞琳。"
Marcel "我很爱你，我受不了看你流泪。"
Marcel "如果你愿意，我想陪在你身边，好替你拭去眼泪。你不介意吧？"
Celine "不、不介意。这、这其实让我挺受宠若惊的。"
"塞琳虚弱地笑了笑。"
Celine "我已经习惯了去爱别人，可还不习惯被人爱着。"
Celine "我也有过未婚夫，可我不觉得他爱我。他爱的只是我父母那笔钱的指望。"
Celine "不过你不一样。你是那样真挚。"
Celine "这几个月你那么拼命。你学着弹钢琴，只为满足我那些自私的任性念头，还帮我重振了学校的合唱团。"
Celine "你听我倾诉了所有鸡毛蒜皮的抱怨，哪怕到了现在，你也还在尽力哄我开心。"
Celine "你、你……是一个比我无私得多的情人。"
Celine "你那么温柔体贴，我都不知道自己是否真的配得上你这份感情。"
Celine "这么久以来，我一直在想着我自己，而你却在想着我。"
Celine "我不知道自己是否配得上你的这份体贴。"
Marcel "哦，别这么说。我也不是什么圣人。"
"我虚弱地笑了笑。"
Marcel "的确，我常常在想你，但那在我并非什么无私之举。我会想着你，是因为我别无选择，只能如此。"
Marcel "你已经偷走了我的心。"
Celine "可、可你知道我喜欢瓦雷纳先生。我跟你说过的。你、你怎么能在知道这一点的情况下，还继续和我待在一起？"
Celine "你不会嫉妒吗？"
Marcel "是的，我确实嫉妒过，但那并没有影响我对你的感情。"
Marcel "我本来怀疑我们俩的关系是否能成，无论你是不是喜欢别人。我从来都没真正打算告诉过你我的感受。"
Marcel "那也改变不了什么……"
Celine "是这样。"
"塞琳叹了口气，下唇微微颤抖。"
Celine "我们都是女人。社会不会接纳这样的结合。"
Celine "我很喜欢你，玛塞尔，但大多数人会觉得你对我的这份感情很奇怪。"
Celine "当然，我绝不会因此评判你。我太喜欢你了，绝不会因你自己的感情而责怪你。我比任何人都清楚，我们无法控制自己会爱上谁。人生就是这样。"
Celine "不过，恐怕别人不会这么宽容。"
Celine "如果我们真的彼此相恋，又被发现了，我们会遭人耻笑。"
Celine "我知道你绝不愿意让我承受那份羞辱……{w}我也绝不愿意让你承受。"
Celine "我不想伤害你。"
"塞琳说这话时是那般真挚，令我的心隐隐作痛。"
"虽然我怀疑她不会像我爱她那样爱我，但她显然在乎我。一定是这样，否则她不会如此包容。"
"她不想让我受伤，可她那些善意的安慰，却建立在一个根本的误会之上。"
"她仍然不知道真相。"
"一想到要坦白，我就害怕——毕竟我把身份隐瞒了这么久——但我知道，如今我再也无法保持缄默。"
"塞琳是我最好的朋友。她跟我说了很多关于她自己的事，我也想回报这份信任。"
"我也希望她了解关于我的一切——包括我真正的名字，以及我为何来到米延。"
Marcel "塞琳，听着。有件事我得告诉你。"
Celine "哦？"
"塞琳看着我，好奇地眨了眨眼。"
Celine "怎么了，玛塞尔？"
Marcel "这也许让你一时难以接受——相信我，对我自己而言也同样难以接受！——可是……"
"我深吸一口气，硬起心肠，然后把那些我希望数月之前就能告诉塞琳的话说了出来。"
Marcel "我其实并不是个女孩，我的名字也不是玛塞尔·雷诺。我是马塞尔·德·圣雷米。"
"当然，那只是我坦白的开端。一旦这些话从口中涌出，我便发现自己已经停不下来了。"
"我把自己的事一五一十地告诉了塞琳，连最微小的细节也不例外。"
"我告诉她我那位风流成性、声名狼藉的父亲乔治，他与母亲有过一段旋风般的恋情，却在母亲怀上我之后抛弃了她。"
"我告诉她我在上一所学校的短暂寄读，以及同学们如何因我父亲的恶名与我自身的阴柔相貌，日复一日地嘲笑、欺辱我。"
"我告诉她我父亲最近的丑闻，以及《吉尔·布拉斯》上所有关于此事的报道，还有母亲的担忧——如果我回到学校，会被愤怒的暴民处以私刑。"
Marcel "那时候，是我的姨母介入了。她是这所学校的校长，她主动提出收留我。"
Marcel "于是我们定下，在最后一个学年里，我将以女孩的身份生活，并自称玛塞尔·雷诺。"
Marcel "我从没有想过要欺骗你，或欺骗我任何一位同学，可我实在别无选择。"
Marcel "我的姨母和我的母亲为了庇护我，共同策划了这个计划。我不愿辜负她们的心血。那样做会显得我自私，尽管我确实为之感到愧疚。"
Marcel "塞琳，当你答应做我朋友时，我真的很高兴。那时我害怕极了，怕自己无论作为男孩{i}还是{/i}女孩，都无法融入。"
Marcel "我曾担心自己在哪里都找不到归属，但你让我明白，事实并非如此。"
Marcel "正是因为你温柔善良，我才能变得更自信。你给了我尝试新事物的勇气。和你一起弹钢琴，我真是太快乐了！"
Marcel "我真的爱你，也很抱歉一直瞒着你。希望你不要因此看轻我。"
"我低声诉说，为自己怯懦而羞愧。这些话在舌尖苦涩难当，仿佛毒药。"
"我仍有点害怕塞琳会转而敌视我——但她没有。"
"她对这个真相显得很惊讶（这也难怪），但她的神情并非厌恶。相反，她看上去好奇，就像坦尼尔笔下那个充满好奇的爱丽丝。"
Celine "哦……"
"塞琳眨了眨眼。"
"她的睫毛仍被残留的泪水打湿，但大半的悲伤已经消散。"
"她不再哭了。"
Celine "这确实……一时难以接受，我必须承认。我从没想过你竟藏着一段如此波澜起伏的过往！"
Celine "哎呀，这简直像冒险小说里的情节！"
Celine "你说你是个男孩？"
Marcel "没错。就像我说过的，我的父亲是乔治·德·圣雷米。我是他的儿子，马塞尔。"
Celine "马塞尔，而不是玛塞尔？"
Marcel "不，不是玛塞尔。她从未存在过。她是我的姨母和母亲为了护住我的身份而编造出来的人。她只是一层伪装。"
Celine "真的吗？你嘴上这么说，可是……"
"塞琳皱起眉头。"
Celine "即便你如你所说是个男孩，我也无法换一种眼光来看你。"
Celine "这确实叫人震惊，可我不认为这会改变你真正的本质。你待我的那份善意，也不会因此减弱半分。"
Celine "这几个月来，你一直在努力帮我，对吧？我看得出来，你是真心想让我开心。"
Marcel "是、是的，没错！我比什么都要更想让你开心！"
Celine "那么，我就看不出你我之间有什么理由要改变。"
Celine "倘若你当初是以男孩的身份自我介绍，我们的关系自然是另一番光景。我会与你保持距离，也不会邀你到我家来。不过，如今再去设想这些已经太迟了。"
Celine "事实终究是，我{i}确实{/i}邀你进了我家，而我们{i}也{/i}已经亲密了起来。"
Celine "你依旧是我的朋友——也是我生命中很重要的一部分。"
Celine "我喜欢的就是你本来的模样，我仍然喜欢你。"
Celine "我想这份心意不会改变。我的心可没那么善变！"
Marcel "真、真的……？"
"我屏住呼吸，瞪大眼睛盯着塞琳。"
"我们的身体仍交缠在她的被褥之下。双腿互相缠绕，我能感觉到塞琳的气息拂过我的脸颊。"
"我们正如以往那般贴近；若说没有，那便更甚。"
Marcel "所、所以，你不恨我？"
Celine "不恨。我为何要恨？"
Celine "我不恨你。你为我做了那么多，我怎么可能恨你。"
Celine "我若恨你，岂不是辜负你为钻研钢琴付出的不懈努力……又辜负你为我拭去眼泪的心意。"
Marcel "谢天谢地……哦，谢天谢地……"
"我长长地呼出一口气。紧张从我身上消散，我终于觉得自己可以放松下来了。"
"我熬过了人生中最凶险的一场风暴，而且毫发无损地走了出来。"
"如今塞琳已经知道了真相，我也没什么需要瞒着她的了。我们之间将再无秘密。"
"我希望我们能尽可能地亲近，即使塞琳没有（或无法）以爱回报我，我也永远会陪伴在她身边。我想让她幸福的心愿，丝毫没有改变。"
Marcel "谢、谢谢你，塞琳。谢谢你。我……我之前担心极了，可是你……唔……"
"我吸了吸鼻子。"
"现在，轮到我哭了。我能感到水汽在睫毛上凝结成珠，尽管我竭力想要眨眼将它们驱散。"
"我这一生，从未感到自己如此赤裸地展露。"
Marcel "你真的是……太温柔了……"
Celine "我并不觉得自己有多温柔。我当然是很会趁人之危的——利用了你对我的感情——不过请你别哭！再这样下去，咱们俩都要被淹死了！"
Marcel "我、我、我忍不住嘛！我从没交过你这样的朋友……或、或者说，我压根一个朋友都没有过！"
Marcel "这是我过去只敢在梦里憧憬的事。真真切切就像一场奇迹！"
Celine "我身上哪有什么奇迹。我只是个蠢女孩，执拗地守着荒唐而不切实际的梦，直到被它刺伤。"
Celine "你不该这样抬举我。我受不起。"
Marcel "我也受不起你的温柔，毕竟我对你说了那么多谎！"
Celine "你没有说谎。你一向诚实坦率，只是你自己不这么觉得。说到底，马塞尔和玛塞尔本来就是同一个人。"
"塞琳替我拭去眼角几滴零落的泪水。她的指节轻触我的脸颊，令我不禁一颤。"
Celine "我喜欢你，马塞尔。你是我的朋友，我说过的话绝不反悔。"
Celine "就算知道你是男孩，我也不会因此少在乎你几分——不过，要是让阿梅莉知道了，恐怕她不会乐意见到你睡在我的床上！"
"塞琳笑了，我也跟着她笑了起来。一声轻笑从我唇间逸出，尽管虚弱而疲倦。"
"突然间，我感到精疲力竭。"
"这一夜确实令人疲惫。我和塞琳都吐露了彼此最黑暗的秘密，我们俩也着实哭了不少。"
"我们各自承受着自己的苦难，却依然留在彼此身边。"
"我知道我会陪伴在塞琳身边，正如她此刻陪伴着我。"
"这就是真正的友谊。"
Celine "你为了我付出了那么多，马塞尔，而你{i}确实{/i}是个温柔的人。"
Celine "我喜欢你，却不清楚自己是否爱你。至少，我不会像当初爱瓦雷纳先生那样爱你。"
Celine "我把自己整个身心都献给了他。我无时无刻不在念着他，直到这股思念将我吞噬。我想我大约是有点发疯了。"
Celine "那样的爱——不，是痴迷——实在太磨人。如今它总算过去了，我不确定自己还能不能再把心交出去。"
Celine "我想，我恐怕得先花些时日让自己缓过来……"
Celine "但此后会怎样，又有谁知道呢？我还年轻，无法预料将来。日子久了，我的心情也说不定会变。"
Celine "也许到那时候，我便准备好再度坠入爱河了。"
Celine "眼下我不能许下任何承诺，但也许有一天，我能够回应你的这份情意。"
Celine "请先给我一点时间就好。"
Marcel "没关系。"
"我朝塞琳微笑，手臂仍环在她的腰间。"
Marcel "你有的是时间慢慢考虑。离夏天结束还有好几个月呢。"
Marcel "我想我能等。在那之前，我不会做任何危及我们友情的事。我太在乎你了，不会那样做。"
Celine "谢谢你肯理解我。我就知道你会的。"
Celine "等到学年结束，你就要回巴黎去了，我也会回奥尔良。我们恐怕不能再像这样待在一起了……"
Celine "但这不会是我们这段情谊的终点。这一点我很有把握。"
Celine "无论我们之间发生什么……我都会一直关心着你。"

window hide dissolve
scene cg25 with dissolve
$ renpy.pause(0.8)
window show dissolve

"于是，就在这句承诺还停留在她唇边之时，塞琳俯身靠近。"
"我能感觉到她的呼吸落在我脸颊上。那气息清凉而温柔，吹拂起几根拂过脸庞的散落发丝。"
"她的睫毛垂落合拢，我的也一并闭上。"
"随即，伴着一记轻柔的叹息，我感到她的唇贴上了我的唇。"
"那是一个非常轻柔、纯洁的吻，只持续了不过一瞬。它羞涩而带着试探，算不上多么缱绻，但无论如何，它终究是一个吻。"
"那不是真爱之吻。倘若在童话里，一位公主只得到这样蜻蜓点水般的一啄，我怀疑她能否苏醒，但这并不意味着这个吻毫无意义。"
"这是塞琳对我依旧怀有感情的证明。"
"她无法像爱瓦雷纳先生那样爱我，我也并不奢望她如此。她仍沉浸在震惊之中，心里一定很痛。"
"然而，随着时间流逝，她的心会愈合。到那时，也许便腾得出容纳我的空间。"
"我不知道那一天是否会到来，但我不会像塞琳曾经那样，用无望的期待折磨自己。"
"我会尽情享受与她相伴的时光——我相信，我们在一起定能创造出许多美好的回忆。"

$ achievement.grant("celine")
$ persistent.end = "on"
stop music fadeout 1.0
stop ambience2 fadeout 1.0
window hide dissolve
scene black with slow_dissolve

jump celine_credits

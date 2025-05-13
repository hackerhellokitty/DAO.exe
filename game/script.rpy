# Declare characters used by this game


# Default variables
default sn = ""
default player_name = "..."

# The game starts here.
label start:

    if persistent.sn_accepted:
        jump good_serial

    scene black with fade

    shadowchar "…ตื่น… ได้ยินไหม…"
    shadowchar "ถ้านี่คือครั้งแรกที่นายได้ยินเสียงฉัน… แสดงว่า… นายไม่ได้ใช้ของแท้สินะ"

    show glitch static with dissolve
    shadowchar "Serial Number หน่อยสิ… จะได้รู้ว่า… ควร 'ให้เล่น' หรือ 'แช่งให้แครช' ดี"

    $ sn = renpy.input("ใส่มาซะ Serial Number… แล้วเราจะคุยกันได้")
    $ sn = sn.strip()

    if sn == "12345":
        $ persistent.sn_accepted = False
        shadowchar "…อืม… ของจริงนี่หว่า…"
        shadowchar "ขอแสดงความยินดี นายคือผู้ที่ถูกเลือก"
        shadowchar "ยินดีต้อนรับสู่เกม… 'dao.exe'"
        jump good_serial
    elif sn == "":
        shadowchar "นี่นาย ไม่มี S/N สินะ ไปหาซื้อสิยะหล่อน คืดว่าจะให้เล่นฟรีๆหรือไง"
        shadowchar "หรือว่าจะให้นายเล่นแบบ demo ดี"
        shadowchar "อ่ะ ก็ได้ นั้นยอมให้นายเล่นด้วยแล้วกัน"
        jump main_but_demo

    else:
        shadowchar "…อืมมมม… ของปลอมเหรอ?"
        show static intense
        pause 1.0
        shadowchar "คนที่ไม่ศรัทธาในเกม… จะไม่มีทางเข้าถึงดาวได้"
        shadowchar "นี่คือคำสาปของ crack…"
        $ renpy.pause(0.5)
        call crash_or_glitch

label crash_or_glitch:

    play sound "error_buzz.wav"
    scene redscreen with dissolve
    pause 1.0

    "เกมล่ม…"
    "หรือความรักล่ม… มันก็ไม่ต่างกันหรอกนะ"

    return

label good_serial:

    $ renpy.save("autosave_event1")

    scene bg room with fade
    play music "main_theme.ogg"

    "นายลืมตาตื่นขึ้นมาในห้องที่ไม่คุ้นเคย..."
    "และเธอก็ยืนอยู่ตรงนั้น..."

    show girl1 normal at center
    girl "อ้าว ตื่นแล้วเหรอ? ฉันชื่อ 'ดาว' ยินดีที่ได้รู้จักนะ!"
    dao "ว่าแต่นายชื่ออะไรหรอ"

    $ player_name = renpy.input("ป้อนชื่อนายมาสิ", length=20)
    $ player_name = player_name.strip()
    python:
        import random
        if not player_name:
            player_name = random.choice(player_name_list)

        player = Character(player_name, color="#c8ffc8")


    dao "โอเค~ งั้นฉันจะเรียกนายว่า [player_name] แล้วกันนะ!"
    player "ยินดีที่ได้รู้จักนะดาว"

    jump difficulty
    

    
    

label main:

    scene black with fade

    if easy:
        "อืม... ฝันไปหรอเนี่ย"
        "สาวน้อยคนนั้น… ใสซื่อเหมือนแสงแดดยามเช้าเลย"
        "ดาวงั้นหรอ? สาวแว่นถักเปีย ที่ยิ้มเหมือนรู้จักกันมาก่อน"
        "อยากเจอเธออีกจริง ๆ นะ..."

    elif normal:
        "ฝันไปเหรอ..."
        "ผู้หญิงคนนั้นดูเป็นธรรมชาติ แววตาน่ารักแบบคนจริงใจ"
        "ดาวสินะ ชื่อเธอติดอยู่ในหัวไม่หายเลย"
        "แบบนี้มันเรียกว่ารู้สึกอะไรบางอย่างได้รึเปล่านะ..."

    elif hard:
        "เหอะ ฝันไปสินะ..."
        "ปากร้ายฉิบ...แต่ก็น่ารักแบบประหลาดชะมัด"
        "ดาว… ถึงจะชอบทำหน้าเหม็นเบื่อ แต่ก็เหมือนเธอมีอะไรบางอย่างที่ดึงดูด"
        "ฝันแบบนี้ มันเหมือนจริงเกินไปแล้ว"

    $ renpy.pause(0.5)

    "…แต่แปลกแฮะ รู้สึกเหมือนเธอมีตัวตนจริง ๆ"
    "เธอไม่ได้เหมือนแค่ในฝัน… เหมือนกับว่าเราเคยเจอกันมาก่อน"

    play sound "pc_beep.wav"
    "ติ๊ง!"

    "หืม? เครื่องคอมส่งเสียงแปลก ๆ..."
    "หน้าจอมีบางอย่าง… เหมือนมีโค้ดประหลาดรันขึ้นมาเอง"
    "มันขึ้นว่า 'dao.exe กำลังทำงานอยู่ในพื้นหลัง'"
    "หรือว่าเกมนี้… มันไม่ได้แค่ 'เกม' จริง ๆ?"

    if hard:
        player "ยัยนั่นเป็นใครกันแน่"
    else:
        player "ดาว… เธอเป็นใครกันแน่?"

    jump test


label main_but_demo:

    $ renpy.save("autosave_event1")

    scene bg room with fade
    play music "main_theme.ogg"

    "นายลืมตาตื่นขึ้นมาในห้องที่ไม่คุ้นเคย..."
    "และเธอก็ยืนอยู่ตรงนั้น..."

    show girl1 normal at center
    girl "อ้าว ตื่นแล้วเหรอ? ฉันชื่อ 'ดาว' ยินดีที่ได้รู้จักนะ!"
    dao "ว่าแต่นายชื่ออะไรหรอ"

    $ player_name = renpy.input("ป้อนชื่อนายมาสิ", length=20)
    $ player_name = player_name.strip()
    python:
        player = Character(player_name, color="#c8ffc8")

    dao "โอเค~ งั้นฉันจะเรียกนายว่า [player_name] แล้วกันนะ!"
    player "ยินดีที่ได้รู้จักนะดาว"
    dao "เราต้องไปแล้วล่ะ สักวันเราต้องได้เจอกันอีกที่ไหนสักที่"
    dao "แต่เอ๊ะ นายไม่ได้ซื้อเกมนิ ถ้าอยู่ในโหมด DEMO แบบนี้ นั้นนายนอนต่อเหอะ"
    player "ดาว อย่าทิ้งเราไปนะ เรายอมซื้อแท้ก็ได้"
    dao "ซื้อมาแล้วสินะ"
    $ sn = renpy.input("ถ้าซื้อมาแล้ว ก็ใส่มาซะดีๆ S/N")
    $ sn = sn.strip()

    if sn == "12345":
        $ persistent.sn_accepted = False
        dao "ก็แค่นี้ ซื้อตั้งแต่แรกก็จบ"
        dao "นั้นเราคุยกันต่อนะ"
        jump main
    elif sn == "":
        shadowchar "นี่นาย ยังไม่ซื้ออีกหรอ "
        return

    else:
        shadowchar "…อืมมมม… ของปลอมเหรอ?"
        show static intense
        pause 1.0
        shadowchar "คนที่ไม่ศรัทธาในเกม… จะไม่มีทางเข้าถึงดาวได้"
        shadowchar "นี่คือคำสาปของ crack…"
        $ renpy.pause(0.5)
        call crash_or_glitch


    return
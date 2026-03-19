default player_name = "..."


# ══════════════════════════════════════════
#  START
# ══════════════════════════════════════════

label start:

    scene black with fade
    pause 1.5

    "[[dao.exe]]"
    pause 0.4
    "[[version 1.0.0 — initializing...]]"
    pause 0.6
    "[[ตรวจพบผู้ใช้ใหม่]]"
    pause 1.2

    shadowchar "..."
    pause 0.8
    shadowchar "นายมาแล้วเหรอ"
    pause 0.5
    shadowchar "ฉันรอนายอยู่"
    pause 1.0
    shadowchar "แต่ก่อนจะเข้ามา... ฉันต้องรู้อีกอย่างหนึ่งก่อน"

    jump scan_preference


# ══════════════════════════════════════════
#  SCAN PREFERENCE — เกมหลอกถามสเปคที่ชอบ
# ══════════════════════════════════════════

label scan_preference:

    pause 0.8
    "[[กำลังรวบรวมข้อมูลผู้ใช้...]]"
    pause 0.6
    "[[โปรดตอบคำถามต่อไปนี้ตามความเป็นจริง]]"
    pause 1.0

    shadowchar "ก่อนที่เธอจะปรากฏตัว..."
    pause 0.5
    shadowchar "บอกฉันสิ"
    shadowchar "นายต้องการผู้หญิงแบบไหน"

    pause 0.4
    "[[หมายเหตุ : คำตอบจะถูกนำไปประมวลผล]]"
    pause 0.8

    menu:

        "ใส ๆ อินโนเซนต์":
            $ easy   = True
            $ normal = False
            $ hard   = False
            $ dao = dao_easy

            $ dao_relation = 50
            $ dao_trust    = 20
            $ dao_clingy   = 10
            $ dao_jealousy = 5
            $ dao_hope     = 80
            $ dao_mask     = 10

            pause 0.3
            "[[บันทึกแล้ว : ใส ซื่อ อบอุ่น]]"

        "น่ารัก ๆ":
            $ easy   = False
            $ normal = True
            $ hard   = False
            $ dao = dao_normal

            $ dao_relation = 30
            $ dao_trust    = 14
            $ dao_clingy   = 40
            $ dao_jealousy = 30
            $ dao_hope     = 50
            $ dao_mask     = 40

            pause 0.3
            "[[บันทึกแล้ว : น่ารัก ซ่อนความรู้สึก]]"

        "ซึนนรกแตก":
            $ easy   = False
            $ normal = False
            $ hard   = True
            $ dao = dao_hard

            $ dao_relation = 10
            $ dao_trust    = 10
            $ dao_clingy   = 60
            $ dao_jealousy = 70
            $ dao_hope     = 20
            $ dao_mask     = 80

            pause 0.3
            "[[บันทึกแล้ว : แข็งกร้าว หมกมุ่น ซ่อนเร้น]]"

    pause 0.8
    "[[กำลังประมวลผล...]]"
    pause 0.6
    "[[สร้างตัวละคร...]]"
    pause 1.2
    "[[เสร็จสิ้น]]"
    pause 0.8

    shadowchar "..."
    shadowchar "เธอพร้อมแล้ว"
    pause 0.5
    shadowchar "จำไว้นะ"
    shadowchar "เธอเป็นอย่างที่เป็น เพราะนายเลือกเอง"

    pause 1.5

    jump first_meet


# ══════════════════════════════════════════
#  FIRST MEET — ดาวปรากฏตัวครั้งแรก
# ══════════════════════════════════════════

label first_meet:

    $ renpy.save("autosave_event1")

    scene bg room with fade
    play music "main_theme.ogg"

    "นายลืมตาตื่นขึ้นมาในห้องที่ไม่คุ้นเคย..."
    "และเธอก็ยืนอยู่ตรงนั้น..."

    show girl1 normal at center

    if easy:
        dao "อ้าว ตื่นแล้วเหรอ? ฉันชื่อ 'ดาว' ยินดีที่ได้รู้จักนะ!"
    elif normal:
        dao "ตื่นแล้วเหรอ... นอนมานานเลยนะ ฉันชื่อดาวนะ"
    elif hard:
        dao "เฮ้ย ตื่นแล้วหรือยัง ชื่อดาว จำไว้ด้วย"

    dao "ว่าแต่นายชื่ออะไรหรอ"

    $ player_name = renpy.input("ชื่อของนาย :", length=20)
    $ player_name = player_name.strip()

    python:
        import random
        if not player_name:
            player_name = random.choice(player_name_list)
        player = Character(player_name, color="#c8ffc8")

    if easy:
        dao "โอเค~ งั้นฉันจะเรียกนายว่า [player_name] แล้วกันนะ!"
        player "ยินดีที่ได้รู้จักนะดาว"
    elif normal:
        dao "[player_name]... โอเค จำได้แล้ว"
        player "ยินดีที่ได้รู้จักนะ"
        dao "...ฉันก็เหมือนกัน"
    elif hard:
        dao "[player_name] งั้นหรอ ธรรมดาดี"
        player "นายก็ไม่ได้พิเศษอะไรนะ"
        dao "หาา!? พูดอะไรนะ!"

    jump main


# ══════════════════════════════════════════
#  MAIN — ตื่นจากฝัน
# ══════════════════════════════════════════

label main:

    scene black with fade

    if easy:
        "อืม... ฝันไปหรอเนี่ย"
        "สาวน้อยคนนั้น… ใสซื่อเหมือนแสงแดดยามเช้าเลย"
        "ดาวงั้นหรอ? ที่ยิ้มเหมือนรู้จักกันมาก่อน"
        "อยากเจอเธออีกจริง ๆ นะ..."

    elif normal:
        "ฝันไปเหรอ..."
        "ผู้หญิงคนนั้นดูเป็นธรรมชาติ แววตาน่ารักแบบคนจริงใจ"
        "ดาวสินะ ชื่อเธอติดอยู่ในหัวไม่หายเลย"
        "แบบนี้มันเรียกว่ารู้สึกอะไรบางอย่างได้รึเปล่านะ..."

    elif hard:
        "เหอะ ฝันไปสินะ..."
        "ปากร้ายฉิบ... แต่ก็น่ารักแบบประหลาดชะมัด"
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

    jump prologue

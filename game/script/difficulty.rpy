label difficulty:

    $ renpy.pause(0.5)
    dao "ว่าแต่นายล่ะ ขอบผู้หญิงแบบไหนหรอ ?"
    dao "อยากรู้จัง"

    menu:

        "ใส ๆ อินโนเซนต์":
            $ easy   = True
            $ normal = False
            $ hard   = False

            # สลับ character object
            $ dao = dao_easy

            # Stats — เปิดใจสูง ไม่หมกมุ่น เชื่อง่าย
            $ dao_relation = 50
            $ dao_trust    = 20
            $ dao_clingy   = 10
            $ dao_jealousy = 5
            $ dao_hope     = 80
            $ dao_mask     = 10

            dao "เอ๋~ งั้นฉันจะพยายามเป็นผู้หญิงแบบนั้นให้นะ!"

        "น่ารัก ๆ":
            $ easy   = False
            $ normal = True
            $ hard   = False

            $ dao = dao_normal

            # Stats — ระวังตัวกลาง ๆ แอบหึง ซ่อนความรู้สึก
            $ dao_relation = 30
            $ dao_trust    = 14
            $ dao_clingy   = 40
            $ dao_jealousy = 30
            $ dao_hope     = 50
            $ dao_mask     = 40

            dao "อื้ม! ฉันก็พอจะน่ารักอยู่บ้างล่ะนะ~"

        "ซึนนรกแตก":
            $ easy   = False
            $ normal = False
            $ hard   = True

            $ dao = dao_hard

            # Stats — ไม่ไว้ใจ หมกมุ่นสูง หน้ากากหนา ความหวังน้อย
            $ dao_relation = 10
            $ dao_trust    = 10
            $ dao_clingy   = 60
            $ dao_jealousy = 70
            $ dao_hope     = 20
            $ dao_mask     = 80

            dao "หาา!? บ้าเหรอ ใครจะอยากเป็นแบบนั้นกันล่ะ!!! (หน้าแดง)"

    $ renpy.pause(0.5)

    if hard:
        dao "หวังว่าจะไม่เจอกับนายเป็นครั้งที่สองอีกนะ"
    else:
        dao "เราต้องไปแล้วล่ะ สักวันเราต้องได้เจอกันอีกที่ไหนสักที่"

    jump main

label difficulty:
$ renpy.pause(0.5)
dao "ว่าแต่นายล่ะ ขอบผู้หญิงแบบไหนหรอ ?"
dao "อยากรู้จัง"

menu:
    "ใส ๆ อินโนเซนต์":
            $ dao_relation = 50
            $ dao_clingy = 10
            $ dao_trust = 20
            $ easy = True
            $ normal = False
            $ hard = False
            dao "เอ๋~ งั้นฉันจะพยายามเป็นผู้หญิงแบบนั้นให้นะ!"
    "น่ารัก ๆ":
            $ dao_relation = 30
            $ dao_clingy = 40
            $ dao_trust = 14
            $ easy = False
            $ normal = True
            $ hard = False
            dao "อื้ม! ฉันก็พอจะน่ารักอยู่บ้างล่ะนะ~"
    "ซึนนรกแตก":
            $ dao_relation = 10
            $ dao_clingy = 60
            $ dao_trust = 10
            $ easy = False
            $ normal = False
            $ hard = True
            dao "หาา!? บ้าเหรอ ใครจะอยากเป็นแบบนั้นกันล่ะ!!! (หน้าแดง)"
$ renpy.pause(0.5)

if hard :
    dao "หวังว่าจะไม่เจอกับนายเป็นครั้งที่สองอีกนะ"
else:
    dao "เราต้องไปแล้วล่ะ สักวันเราต้องได้เจอกันอีกที่ไหนสักที่"
"Dev Debug"
"ความสัมพันธ์: [dao_relation]"
"ความไว้วางใจ: [dao_trust]"
"ความงี่เง่า: [dao_clingy]"

jump main 
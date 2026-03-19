label chapter2:

    # ── ตรวจสอบและสร้าง fon.chr ───────────────
    python:
        import os
        fon_path = os.path.join(renpy.config.gamedir, "fon.chr")

        if not persistent.fon_chr_created:
            f = open(fon_path, "w", encoding="utf-8")
            f.write("fon\n[character file]\n[memory intact]\n[do not delete]")
            f.close()
            persistent.fon_chr_created = True
            persistent.fon_loop_count  = 0

        store.fon_exists = os.path.exists(fon_path)

    # ไม่มีไฟล์ = ผู้เล่นลบออกแล้ว
    if not fon_exists:
        jump ch2_resolved

    # มีไฟล์ → นับลูปและเข้าฉากซ้ำ
    $ persistent.fon_loop_count = getattr(persistent, "fon_loop_count", 0) + 1


    # ── GLITCH INTRO (ลูปที่ 2 ขึ้นไป) ──────────

    if persistent.fon_loop_count == 2:
        scene black with dissolve
        pause 0.3
        "..."
        "รอ"
        "เราเคยผ่านตรงนี้มาแล้วไหม"

    elif persistent.fon_loop_count == 3:
        scene black with dissolve
        show glitch static with dissolve
        pause 0.5
        shadowchar "..."
        shadowchar "ทำไมนายยังอยู่ที่นี่"

    elif persistent.fon_loop_count >= 4:
        scene black with dissolve
        show static intense
        pause 0.8
        shadowchar "[[fon.chr ยังคงอยู่]]"
        pause 0.5
        shadowchar "ลบมันซะ"
        pause 1.0


    # ── บ่ายวันเสาร์ ──────────────────────────

    scene black with fade
    pause 0.5
    "สองวันต่อมา"

    scene bg room with fade
    play music "main_theme.ogg"

    "ดาวบอกว่าจะมาช่วยทำความสะอาดห้อง"
    "ฉันไม่ได้ขอให้เธอมา"
    "แต่เธอก็มาอยู่ดี"

    show girl1 normal at center

    if easy:
        dao "ห้องนายรกมากเลยนะ ดาวช่วยจัดให้นะ~"
    elif normal:
        dao "...ห้องนายรกจริง ๆ เลยนะ"
    elif hard:
        dao "ห้องอะไรรกขนาดนี้ ก็ดีที่ฉันมา ไม่งั้นคงเน่าอยู่คนเดียว"

    pause 1.0


    # ── เจอจดหมาย ────────────────────────────

    "เสียงกระดาษกรอบแกรบดังขึ้นจากมุมห้อง"
    pause 0.6
    dao "..."
    pause 1.0
    "เธอหยิบซองสีขาวขึ้นมา"
    "ลายมือกลม ๆ ที่คุ้นเคย แต่นานมากแล้วที่ไม่ได้เห็น"
    pause 0.5

    "[[fon.chr — พบไฟล์]]"
    pause 0.3
    "[[วันที่แก้ไขล่าสุด : 1 ปี 47 วันที่แล้ว]]"
    pause 1.0

    dao "...ฝน"
    pause 0.8

    if easy:
        dao "นายยังเก็บจดหมายของเธออยู่เหรอ"
        "เธอพูดเบา ๆ เหมือนถามตัวเอง"
    elif normal:
        dao "นายยังเก็บของเธออยู่"
    elif hard:
        dao "อ้อ ของฝน"
        "เธอวางซองลงช้า ๆ แล้วยืนมองมือตัวเอง"


    # ── JEALOUSY LOOP ─────────────────────────

    if easy:
        dao "นายคิดถึงเธออยู่ไหม ไม่ตัดสินนะ แค่อยากรู้"
    elif normal:
        dao "นายยังติดต่อกับเธออยู่ไหม"
    elif hard:
        dao "ก็ไม่แปลกหรอก คนเก่ายังไงก็ลืมยาก ใช่ไหม"

    menu:
        "เปล่า ลืมไปนานแล้ว":
            pass
        "ก็แค่จดหมายเก่า":
            pass

    pause 0.6

    if easy:
        dao "แต่นายเคยรักเธอใช่ไหม"
        dao "แค่อยากรู้น่ะ"
    elif normal:
        dao "นายเคยรักเธอมากไหม"
    elif hard:
        dao "นายยังรักเธออยู่ไหม"
        "เธอถามตรง ไม่มีเสียงสั่น"

    menu:
        "เคย แต่มันผ่านไปแล้ว":
            pass
        "ไม่รู้จะตอบยังไง":
            pass

    pause 0.8

    if easy:
        dao "ดาวแค่กลัวว่านายจะยังคิดถึงเธออยู่"
        dao "แล้วสักวันนายจะหันหลังให้ดาว"
    elif normal:
        dao "นายยังคิดถึงเธออยู่ไหม"
        dao "ตอบตรง ๆ ได้เลย"
    elif hard:
        dao "ยังไม่ลืมฝนใช่ไหม"
        "เธอถามอีกครั้ง เหมือนวนกลับมาที่คำถามเดิม"

    menu:
        "ลืมแล้ว":
            pass
        "หยุดถามได้แล้ว":
            pass

    pause 1.0


    # ── ปิดฉากแล้ววนกลับ ─────────────────────

    scene black with dissolve
    pause 0.8

    if persistent.fon_loop_count == 1:
        "เธอทำความสะอาดห้องจนเสร็จ ไม่พูดถึงฝนอีก"
        "ฉันก็ไม่พูดถึงเหมือนกัน"
        "แต่มันยังค้างอยู่ในอากาศ"

    elif persistent.fon_loop_count == 2:
        "เธอทำความสะอาดห้องจนเสร็จ ไม่พูดถึงฝนอีก"
        "..."
        "เดี๋ยว"
        "เราเคยผ่านตรงนี้มาแล้วใช่ไหม"

    elif persistent.fon_loop_count == 3:
        show glitch static with dissolve
        pause 0.5
        "เธอทำความสะอาดห้อง—"
        pause 0.3
        show static intense
        pause 0.3
        scene black with dissolve
        shadowchar "มีบางอย่างผิดปกติ"

    else:
        show static intense
        pause 1.0
        scene black with dissolve
        shadowchar "[[fon.chr ยังคงอยู่]]"
        pause 0.5
        shadowchar "ตราบใดที่ไฟล์นั้นยังอยู่"
        shadowchar "เธอก็จะยังจำอยู่"
        pause 0.5
        shadowchar "และวันนี้ก็จะวนซ้ำไปเรื่อย ๆ"

    pause 1.5

    jump chapter2


# ══════════════════════════════════════════
#  CH2 RESOLVED — ผู้เล่นลบ fon.chr แล้ว
# ══════════════════════════════════════════

label ch2_resolved:

    scene black with fade
    pause 1.0

    "[[fon.chr — ไม่พบไฟล์]]"
    pause 0.8

    shadowchar "..."
    pause 0.5
    shadowchar "นายลบมันทิ้งแล้ว"
    pause 0.8
    shadowchar "เธอจะยังจำได้ไหมนะ ว่าเมื่อวานเกิดอะไรขึ้น"
    pause 1.5

    scene bg room with fade
    play music "main_theme.ogg"

    "บ่ายวันเสาร์"
    "ดาวมาช่วยทำความสะอาดห้อง"

    show girl1 normal at center

    if easy:
        dao "ห้องนายรกมากเลยนะ~"
    elif normal:
        dao "...ห้องนายรกเลยนะ"
    elif hard:
        dao "ก็ดีที่ฉันมา ไม่งั้นจะอยู่กับความรกได้ยังไง"

    pause 1.0

    "เธอทำความสะอาดไปสักพัก"
    "มุมที่เมื่อวานเจอซองจดหมาย..."
    "ตอนนี้ว่างเปล่า"

    dao "..."
    pause 0.5

    if easy:
        dao "นายทำอะไรกับของในมุมนั้นเหรอ"
        dao "มีอะไรอยู่ที่นั่นเมื่อกี้เหมือนกันนะ"
    elif normal:
        dao "ตรงนั้น..."
        dao "เมื่อกี้มีอะไรอยู่ไหม"
    elif hard:
        dao "เฮ้"
        dao "เมื่อกี้ฉันหยิบอะไรขึ้นมาไหม"

    player "เปล่า ไม่มีอะไร"
    pause 0.5
    dao "..."
    dao "อ้อ"

    "เธอพยักหน้า แล้วก็จัดของต่อ"
    "เหมือนเธอลืมไปแล้ว"

    pause 1.0

    player "ดาว"
    dao "อะไร"
    player "เราพยายามจะลืมคนเก่าให้ได้"

    pause 1.2

    dao "..."

    if easy:
        "เธอหันมาช้า ๆ"
        dao "นายไม่ต้องพยายามขนาดนั้นก็ได้นะ"
        dao "ดาวรู้ว่านายเป็นยังไง"
        "เธอยิ้ม ครั้งนี้มันเหมือนในฝัน"
        $ dao_trust    += 20
        $ dao_relation += 15
        $ dao_hope     += 20
        $ dao_clingy   -= 10

    elif normal:
        "เธอไม่หัน แต่มือที่เช็ดโต๊ะหยุดลง"
        dao "รู้อยู่แล้ว"
        pause 0.5
        dao "แค่บางทีก็อยากได้ยิน"
        $ dao_trust    += 15
        $ dao_relation += 10
        $ dao_hope     += 15
        $ dao_mask     -= 10

    elif hard:
        "เธอไม่หัน"
        pause 1.0
        dao "ใช้เวลานานนะ"
        pause 0.5
        "แต่ไหล่เธอดูเบาลงกว่าเมื่อกี้"
        $ dao_trust    += 12
        $ dao_relation += 8
        $ dao_hope     += 10
        $ dao_mask     -= 20

    pause 1.5
    scene black with dissolve

    shadowchar "[[fon.chr — ไม่พบไฟล์]]"
    pause 0.8
    shadowchar "บางอย่างที่ลบออกไปแล้ว..."
    shadowchar "ไม่ได้แปลว่ามันไม่เคยมีอยู่"
    pause 0.5
    shadowchar "แต่อย่างน้อย..."
    shadowchar "วันนี้ก็ไม่ต้องวนซ้ำแล้ว"

    pause 2.0

    jump chapter3

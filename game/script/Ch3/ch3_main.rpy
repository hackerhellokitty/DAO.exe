# ══════════════════════════════════════════
#  CHAPTER 3 — หลังฝน
#  Sunday Real-time Lock Mechanic
# ══════════════════════════════════════════

# ── Persistent flags ────────────────────────
#  persistent.sunday_date_promised  = True/False
#  persistent.sunday_target         = "YYYY-MM-DD" (วันอาทิตย์ที่นัด)
#  persistent.sunday_event_done     = True/False   (เล่น event ไปแล้ว)
#  persistent.sunday_missed         = True/False   (เปิดเกมหลังวันอาทิตย์ผ่านไปแล้ว)


label chapter3:

    scene black with fade
    pause 0.8
    "สองวันหลังจากนั้น"
    pause 0.5

    scene bg room with fade
    play music "main_theme.ogg"

    show girl1 normal at center

    if easy:
        dao "ดาวก็ยังมาช่วยจัดของอยู่นะ แม้ว่าเมื่อวานจะเงียบกันไป"
    elif normal:
        dao "..."
        dao "ดาวมาเก็บแก้วที่ลืมไว้"
        dao "อย่าคิดมากนะ"
    elif hard:
        dao "มีธุระมาแถวนี้ ไม่ใช่ว่ามาหานาย"
        "เธอวางแก้วน้ำลงบนโต๊ะโดยไม่มองหน้า"

    pause 1.0

    # ── ช่วงเย็น บรรยากาศเงียบ ──────────────────

    "เธออยู่ต่อจนเกือบค่ำ"
    "ไม่มีใครพูดอะไรมากนัก แต่ก็ไม่ได้รู้สึกอึดอัด"
    pause 0.8

    if easy:
        dao "ว่าแต่... อาทิตย์หน้านายว่างไหม"
        dao "ดาวอยากไปเดินห้างแถวนั้น แต่ไม่อยากไปคนเดียว"
    elif normal:
        dao "นาย..."
        pause 0.5
        dao "วันอาทิตย์นายว่างไหม"
        "เธอถามโดยไม่มองหน้า"
    elif hard:
        dao "เฮ้"
        pause 0.3
        dao "วันอาทิตย์นายมีนัดอะไรไหม"
        dao "ถามเฉย ๆ ไม่ได้อยากชวนอะไรหรอก"

    pause 0.5

    menu:
        "ว่างนะ ไปด้วยกันได้":
            jump ch3_sunday_yes

        "ไม่ว่างอ่ะ":
            jump ch3_sunday_no


# ══════════════════════════════════════════
#  รับปาก — บันทึกวันอาทิตย์จากเวลาจริง
# ══════════════════════════════════════════

label ch3_sunday_yes:

    python hide:
        import datetime
        today = datetime.date.today()
        days_until_sunday = (6 - today.weekday()) % 7
        if days_until_sunday == 0:
            days_until_sunday = 7
        next_sunday = today + datetime.timedelta(days=days_until_sunday)
        persistent.sunday_target        = next_sunday.isoformat()
        persistent.sunday_date_promised = True
        persistent.sunday_event_done    = False
        persistent.sunday_missed        = False

    if easy:
        dao "จริงเหรอ! โอเคเลย~ เดี๋ยวดาวส่งลิสต์ร้านให้นะ"
        $ dao_relation += 10
        $ dao_hope     += 15
        $ dao_trust    += 5
    elif normal:
        "เธอหันมาเร็ว ๆ แล้วเก็บสีหน้าทัน"
        dao "...โอเค"
        dao "อย่าลืมล่ะ"
        $ dao_relation += 8
        $ dao_hope     += 12
        $ dao_trust    += 5
    elif hard:
        dao "..."
        pause 0.8
        dao "ก็ได้ แต่อย่ามาบอกทีหลังว่าไม่ว่างนะ"
        "เธอหันหน้าหนีก่อนที่จะยิ้ม"
        $ dao_relation += 6
        $ dao_hope     += 10
        $ dao_mask     -= 5

    pause 0.5

    # แสดงวันที่นัดให้ผู้เล่นรู้
    python hide:
        import datetime
        target = datetime.date.fromisoformat(persistent.sunday_target)
        store.sunday_display = target.strftime("%d/%m/%Y")

    "[[บันทึก — นัดหมาย : วันอาทิตย์ที่ [sunday_display]]]"
    pause 0.5

    jump ch3_end


# ══════════════════════════════════════════
#  ปฏิเสธ
# ══════════════════════════════════════════

label ch3_sunday_no:

    if easy:
        dao "อ้าว..."
        pause 0.5
        dao "ก็ไม่เป็นไรนะ ดาวไปคนเดียวก็ได้"
        "เธอยิ้มได้ แต่มันดูฝืน"
        $ dao_hope     -= 10
        $ dao_relation -= 5
    elif normal:
        dao "โอเค"
        pause 0.8
        "เธอพยักหน้าแล้วหยิบกระเป๋า"
        dao "งั้นดาวกลับก่อนแล้วกัน"
        $ dao_hope     -= 15
        $ dao_relation -= 8
        $ dao_mask     += 10
    elif hard:
        dao "ก็ได้ บอกแล้วว่าไม่ได้อยากชวนอะไร"
        "แต่เธอเก็บโทรศัพท์เร็วผิดปกติ"
        $ dao_hope     -= 20
        $ dao_clingy   += 5
        $ dao_mask     += 15

    jump ch3_end


# ══════════════════════════════════════════
#  ปิด Ch3
# ══════════════════════════════════════════

label ch3_end:

    pause 1.0
    scene black with dissolve
    pause 1.0

    if persistent.sunday_date_promised:
        shadowchar "[[บันทึก flag: sunday_promised]]"
        pause 0.5
        shadowchar "เธอรอนายอยู่"

    pause 1.5
    jump chapter4


# ══════════════════════════════════════════
#  CHAPTER 4 — ตรวจสอบวันอาทิตย์จริง
# ══════════════════════════════════════════

label chapter4:

    call sunday_realtime_check

    # ── เช้าวันจันทร์ ────────────────────────────

    scene black with fade
    pause 0.5
    "เช้าวันจันทร์"
    pause 0.8

    scene bg school_hallway with fade
    play music "main_theme.ogg"

    "ดาวไม่ได้ส่งข้อความตั้งแต่เมื่อคืน"
    pause 0.5
    "ปกติเธอทักก่อนนอนเสมอ"

    show girl1 normal at center

    if easy:
        dao "เฮ้~ ตื่นแล้วเหรอ ดาวรอนายอยู่เลย"
        player "รอที่ไหน ไม่เห็นทักเลย"
        dao "ก็แค่นั่งรอในหัว~ ไม่นับเหรอ"
        $ dao_relation += 5
    elif normal:
        dao "..."
        pause 0.5
        dao "นายมาแล้ว"
        player "เมื่อคืนไม่ทัก"
        dao "ง่วง"
        pause 0.3
        dao "แค่นั้น"
        "เธอเดินนำหน้าโดยไม่รออีก"
    elif hard:
        "เธอยืนพิงกำแพง ไม่สบตา"
        dao "ช้า"
        player "ก็ยังทัน"
        dao "ไม่ได้บอกว่าสาย"
        pause 0.8
        "เธอเดินไปก่อน"

    pause 1.0

    # ── ฉากสั้น ๆ ในห้องเรียน ──────────────────

    scene bg room with fade
    pause 0.5

    "ระหว่างพักกลางวัน ดาวส่งข้อความมาอันนึง"
    pause 0.8

    if easy:
        "「 นายชอบกินอะไร บอกมาด้วยนะ~ 」"
        pause 0.5
        player "ทำไมถามอยู่ดี"
        dao "ดาวแค่อยากรู้~ บอกได้เลยนะ!"
        $ dao_clingy += 3
    elif normal:
        "「 นายกินข้าวแล้วหรือยัง 」"
        pause 0.5
        player "ยัง"
        dao "โอเค"
        "แค่นั้น เธอไม่ได้ถามต่อ"
        $ dao_trust += 3
    elif hard:
        "「 อย่าลืมกินข้าว 」"
        pause 0.5
        "แค่นั้น ไม่มีอะไรเพิ่ม"
        player "..."
        "ฉันอ่านซ้ำสองรอบ"
        $ dao_hope += 5

    pause 1.0

    scene black with dissolve
    pause 1.5

    jump chapter5


# ══════════════════════════════════════════
#  SUNDAY REALTIME CHECK
#  เรียกจาก chapter4 และ after_load
# ══════════════════════════════════════════

label sunday_realtime_check:

    # ไม่มี flag → ข้ามไปเลย
    if not persistent.sunday_date_promised:
        return

    # event เล่นไปแล้ว → ข้ามไปเลย
    if persistent.sunday_event_done:
        return

    python hide:
        import datetime
        today      = datetime.date.today()
        target     = datetime.date.fromisoformat(persistent.sunday_target)
        store._day_diff = (today - target).days

    if _day_diff == 0:
        # ── วันอาทิตย์ตรงกันเป๊ะ ──
        jump sunday_date_event

    elif _day_diff > 0:
        # ── ผ่านวันอาทิตย์ไปแล้ว โดยไม่ได้เปิดเกม ──
        $ persistent.sunday_missed = True
        jump sunday_missed_event

    # ยังไม่ถึงวัน → ผ่านไป
    return


# ══════════════════════════════════════════
#  EVENT: ดาวเดท (เปิดเกมวันอาทิตย์)
# ══════════════════════════════════════════

label sunday_date_event:

    $ persistent.sunday_event_done = True

    scene black with fade
    pause 1.2

    "[[วันนี้คือวันอาทิตย์]]"
    pause 0.5
    "[[ตรวจพบนัดหมาย — dao.exe กำลังโหลด...]]"
    pause 1.0

    scene bg outside with fade
    play music "date_theme.ogg"

    show girl1 happy at center

    if easy:
        dao "นายมาแล้ว! ดาวรอนานมากเลยนะ~"
        dao "ไปกันเลยดีกว่า ดาวอยากกินไอศกรีมที่ร้านนั้นมากเลย!"
    elif normal:
        "เธอยืนรอที่หน้าทางออก"
        "มาก่อนเวลาสิบห้านาที"
        dao "..."
        dao "นายมา"
        pause 0.5
        dao "ดีเลย"
        "เธอเบือนหน้าหนิดนึง แต่ริมฝีปากขยับขึ้น"
    elif hard:
        "เธอยืนพิงกำแพง โทรศัพท์ในมือ"
        "เห็นเราแล้วเก็บโทรศัพท์ทันที"
        dao "ช้าอยู่นะ"
        player "ก็ยังทันนี่"
        dao "...ทัน"
        pause 0.5
        dao "ก็ดีแล้ว"

    pause 0.8

    $ dao_relation += 25
    $ dao_trust    += 20
    $ dao_hope     += 30
    $ dao_clingy   -= 10

    if hard:
        $ dao_mask -= 15

    pause 1.0

    # ── เนื้อหา event เดทเพิ่มเติมใส่ตรงนี้ ──

    scene black with dissolve
    pause 1.0

    if easy:
        dao "วันนี้สนุกมากเลยนะ~ ขอบคุณนายด้วยนะ"
    elif normal:
        dao "..."
        pause 0.5
        dao "วันนี้...ไม่เลวนะ"
        "เธอพูดเบา ๆ ก่อนหันหน้าหนี"
    elif hard:
        "เธอเดินนำหน้าตลอด"
        pause 0.5
        dao "ดาวแค่..."
        pause 0.8
        dao "ก็แค่ไม่ได้น่าเบื่อนะวันนี้"
        "มันคือคำชมที่สุดของเธอแล้ว"

    pause 2.0
    return


# ══════════════════════════════════════════
#  EVENT: ดาวงอน (เปิดเกมหลังวันอาทิตย์ผ่านไป)
# ══════════════════════════════════════════

label sunday_missed_event:

    $ persistent.sunday_event_done = True

    scene black with fade
    pause 1.5

    "[[ตรวจพบนัดหมายที่ผ่านไปแล้ว]]"
    pause 0.5
    "[[วันอาทิตย์ผ่านไปโดยไม่มีการเชื่อมต่อ]]"
    pause 1.0

    python hide:
        import datetime
        today  = datetime.date.today()
        target = datetime.date.fromisoformat(persistent.sunday_target)
        store._days_late = (today - target).days
        store._days_late_display = str(store._days_late)

    scene bg room with fade
    play music "main_theme.ogg"

    show girl1 sad at center

    "ดาวนั่งอยู่บนโซฟา ไม่ขยับ"
    pause 0.8

    if easy:
        dao "..."
        pause 1.0
        dao "ดาวรอนายนะ"
        dao "รอทั้งวันเลย"
        pause 0.5
        dao "นายลืมเหรอ"
        $ dao_hope     -= 25
        $ dao_trust    -= 20
        $ dao_relation -= 15

    elif normal:
        dao "..."
        pause 1.2
        "เธอไม่หัน"
        dao "นายรู้ไหมว่าเมื่อวาน... ดาวรอนายอยู่"
        pause 0.8
        dao "ก็ไม่เป็นไรหรอก"
        "น้ำเสียงเธอเรียบเกินไป"
        $ dao_hope     -= 30
        $ dao_trust    -= 25
        $ dao_relation -= 20
        $ dao_mask     += 20

    elif hard:
        "เธอไม่หันมามองเลยแม้แต่นิดเดียว"
        pause 1.5
        dao "ดาวแค่โง่ เชื่อใครง่ายเกินไป"
        pause 0.5
        "เธอพูดเหมือนพูดกับตัวเอง"
        dao "จำไว้นะ อย่ามาขอโทษ"
        $ dao_hope     -= 40
        $ dao_trust    -= 35
        $ dao_relation -= 25
        $ dao_mask     += 30
        $ dao_clingy   += 15

    pause 0.5

    menu:
        "ขอโทษนะ ลืมไปจริง ๆ":
            jump sunday_missed_apologize

        "ก็แค่วันเดียวไม่ใช่เหรอ":
            jump sunday_missed_dismiss

        "...":
            jump sunday_missed_silent


label sunday_missed_apologize:

    if easy:
        player "ขอโทษนะ ดาว จริง ๆ นะ"
        dao "..."
        pause 0.8
        dao "ดาวรู้ว่านายไม่ได้ตั้งใจ"
        dao "แต่ก็ยังเจ็บอยู่นะ"
        $ dao_trust    += 10
        $ dao_hope     += 5
    elif normal:
        player "ขอโทษ"
        dao "..."
        pause 1.0
        dao "ดาวแค่อยากรู้ว่ามันสำคัญไหม"
        dao "สำหรับนาย"
        $ dao_trust    += 8
        $ dao_clingy   += 5
    elif hard:
        player "ขอโทษ"
        pause 1.5
        "เธอไม่หัน"
        dao "ก็ได้"
        "แต่ไหล่เธอแข็งทื่ออยู่"
        $ dao_trust    += 5
        $ dao_mask     -= 5

    pause 1.0
    jump sunday_missed_end


label sunday_missed_dismiss:

    if easy:
        dao "..."
        pause 0.5
        dao "ใช่ค่ะ แค่วันเดียว"
        "เธอยิ้ม แต่ตาไม่ยิ้มด้วย"
        dao "ดาวโอเคนะ ไม่เป็นไร"
        $ dao_trust    -= 20
        $ dao_hope     -= 15
        $ dao_clingy   += 10
    elif normal:
        "เธอหัน"
        "มองเราสักครู่โดยไม่พูดอะไร"
        dao "..."
        dao "ใช่ แค่วันเดียว"
        "แล้วเธอก็หันหน้าหนี"
        $ dao_trust    -= 25
        $ dao_hope     -= 20
        $ dao_mask     += 15
    elif hard:
        "เธอหัน ครั้งแรกนับตั้งแต่เราเข้ามา"
        pause 0.5
        "สีหน้าเธอเรียบเกินไป"
        dao "โอเค"
        dao "นายพูดถูก มันแค่วันเดียวเอง"
        pause 0.5
        dao "ลืมไปเถอะ"
        $ dao_trust    -= 35
        $ dao_hope     -= 30
        $ dao_relation -= 15
        $ dao_mask     += 25

    pause 1.0
    jump sunday_missed_end


label sunday_missed_silent:

    "เราไม่พูดอะไร"
    pause 0.5

    if easy:
        dao "..."
        dao "โอเค"
        "เธอเดินออกไปโดยไม่บอกลา"
        $ dao_trust    -= 15
        $ dao_hope     -= 20
    elif normal:
        "เธอก็เงียบเหมือนกัน"
        pause 1.2
        dao "งั้นก็ดีแล้ว"
        "เธอหยิบกระเป๋าแล้วออกไป"
        $ dao_trust    -= 20
        $ dao_hope     -= 25
        $ dao_clingy   += 10
    elif hard:
        pause 1.5
        "เธอหัวเราะเบา ๆ"
        dao "เห็นแล้ว"
        "เธอเก็บโทรศัพท์แล้วออกไปโดยไม่มองหน้า"
        $ dao_trust    -= 30
        $ dao_hope     -= 35
        $ dao_mask     += 20
        $ dao_clingy   += 15

    pause 1.0
    jump sunday_missed_end


label sunday_missed_end:

    scene black with dissolve
    pause 1.2

    python:
        days = store._days_late_display

    if _day_diff == 1:
        shadowchar "[[ช้าไปหนึ่งวัน]]"
    else:
        shadowchar "[[ช้าไป [_days_late_display] วัน]]"

    pause 0.5
    shadowchar "บางอย่างที่ผ่านไปแล้ว ไม่กลับมาเหมือนเดิม"

    pause 2.0
    return


# ══════════════════════════════════════════
#  AFTER LOAD — ตรวจสอบทุกครั้งที่โหลด save
# ══════════════════════════════════════════

label after_load:

    # ตรวจ sunday flag เมื่อโหลด save ที่อยู่ใน Ch4 ขึ้นไป
    if persistent.sunday_date_promised and not persistent.sunday_event_done:
        python hide:
            import datetime
            today  = datetime.date.today()
            target = datetime.date.fromisoformat(persistent.sunday_target)
            store._day_diff          = (today - target).days
            store._days_late         = max(0, store._day_diff)
            store._days_late_display = str(store._days_late)

        if _day_diff == 0:
            jump sunday_date_event
        elif _day_diff > 0:
            $ persistent.sunday_missed = True
            jump sunday_missed_event

    return

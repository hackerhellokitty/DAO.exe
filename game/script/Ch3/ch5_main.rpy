# ══════════════════════════════════════════
#  CHAPTER 5 — วันเกิด
#  Birthday Real-time Check + Age Gate
# ══════════════════════════════════════════

# ── Persistent flags ────────────────────────
#  persistent.player_birth_day    = int (1–31)
#  persistent.player_birth_month  = int (1–12)
#  persistent.player_birth_year   = int (เช่น 2001)
#  persistent.player_age          = int (อายุปัจจุบัน)
#  persistent.player_is_adult     = True/False (>= 18)
#  persistent.birthday_event_done = True/False


label chapter5:

    scene black with fade
    pause 0.8
    "สักพักต่อมา"
    pause 0.5

    scene bg room with fade
    play music "main_theme.ogg"

    show girl1 normal at center

    if easy:
        dao "เฮ้~ นายเกิดวันไหนอ่ะ?"
        dao "ดาวแค่อยากรู้น่ะ ไม่ได้มีอะไรหรอก"
    elif normal:
        dao "ว่าแต่..."
        dao "นายเกิดวันไหน"
        dao "แค่อยากรู้"
    elif hard:
        dao "นายเกิดวันไหนอ่ะ"
        dao "ถามเฉย ๆ"
        "เธอพูดราวกับว่าไม่สนใจ แต่หูเธอตั้งรอ"

    pause 0.5

    # ── รับ input วันเกิด ───────────────────────

    python hide:
        import datetime
        import calendar

        # ── วัน ──────────────────────────────
        while True:
            raw_day = renpy.input("วัน (1–31) :", length=2, default="").strip()
            try:
                bd = int(raw_day)
                if 1 <= bd <= 31:
                    break
            except:
                pass

        # ── เดือน ──────────────────────────────
        while True:
            raw_mon = renpy.input("เดือน (1–12) :", length=2, default="").strip()
            try:
                bm = int(raw_mon)
                if 1 <= bm <= 12:
                    break
            except:
                pass

        # ── ปี ──────────────────────────────
        while True:
            raw_yr = renpy.input("ปี (ค.ศ.) :", length=4, default="").strip()
            try:
                by = int(raw_yr)
                if 1900 <= by <= datetime.date.today().year:
                    break
            except:
                pass

        # ── คำนวณอายุ ──────────────────────────
        today = datetime.date.today()

        try:
            birth_date = datetime.date(by, bm, bd)
        except ValueError:
            last_day = calendar.monthrange(by, bm)[1]
            birth_date = datetime.date(by, bm, min(bd, last_day))

        age = today.year - birth_date.year - (
            (today.month, today.day) < (birth_date.month, birth_date.day)
        )
        age = max(0, age)

        persistent.player_birth_day   = birth_date.day
        persistent.player_birth_month = birth_date.month
        persistent.player_birth_year  = birth_date.year
        persistent.player_age         = age
        persistent.player_is_adult    = (age >= 18)

        store.player_age    = age
        store._is_birthday  = (
            today.month == birth_date.month and
            today.day   == birth_date.day
        )

    # ── Dao ตอบรับ ───────────────────────────

    if easy:
        dao "โอ้~ [player_age] ปีแล้วเหรอ จำไว้แล้วนะ!"
    elif normal:
        dao "..."
        dao "[player_age] ปี"
        dao "จำไว้แล้วนะ"
    elif hard:
        dao "แค่นั้นเองเหรอ"
        dao "ก็โอเค"
        "เธอพยักหน้าเล็กน้อย"

    pause 0.5

    # ── ถ้าวันนี้คือวันเกิดพอดี ────────────────

    if _is_birthday:
        jump ch5_birthday_today

    jump ch5_continue


# ══════════════════════════════════════════
#  วันนี้คือวันเกิด
# ══════════════════════════════════════════

label ch5_birthday_today:

    $ persistent.birthday_event_done = True

    scene black with dissolve
    pause 0.8
    "[[ตรวจพบ — วันนี้คือวันเกิดของผู้ใช้]]"
    pause 1.0

    scene bg room with fade
    play music "date_theme.ogg"

    show girl1 happy at center

    if easy:
        dao "เดี๋ยวนะ..."
        pause 0.5
        dao "วันนี้วันเกิดนายด้วย!?"
        dao "ทำไมไม่บอก! ดาวจะได้เตรียมของให้!"
        $ dao_relation += 15
        $ dao_hope     += 20
        $ dao_trust    += 10
    elif normal:
        dao "..."
        pause 1.0
        dao "วันนี้วันเกิดนายใช่ไหม"
        pause 0.5
        dao "ดาวไม่รู้เลย"
        "เธอเงียบสักครู่"
        dao "สุขสันต์วันเกิดนะ"
        dao "พูดแค่นี้ก็แค่นั้น"
        $ dao_relation += 12
        $ dao_hope     += 15
        $ dao_trust    += 8
    elif hard:
        "เธอหยุดพิมพ์โทรศัพท์"
        pause 0.5
        dao "..."
        dao "นายไม่บอกเลยนะว่าวันนี้วันเกิด"
        pause 0.8
        dao "สุขสันต์วันเกิด"
        dao "บอกไปงั้น"
        "แต่เธอวางโทรศัพท์ลงแล้วนั่งใกล้กว่าเดิม"
        $ dao_relation += 10
        $ dao_hope     += 12
        $ dao_mask     -= 10

    pause 2.0
    jump ch5_continue


# ══════════════════════════════════════════
#  ต่อ Ch5 → Ch6
# ══════════════════════════════════════════

label ch5_continue:

    pause 1.0
    scene black with dissolve
    pause 1.5

    jump chapter6

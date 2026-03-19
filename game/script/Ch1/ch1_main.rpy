label chapter1:

    # ── เช้าวันต่อมา ─────────────────────────

    scene black with fade
    "07:50"

    if easy:
        player "สาวในฝันคนนั้น… น่าจะเป็นสาวรุ่นเดียวกับเราสินะ"
        player "แว่น ถักเปีย ยิ้มง่าย..."
        player "แปลก ทำไมยังจำหน้าได้อยู่เลย"
    elif normal:
        player "ฝันแบบนั้น... มันชัดเกินไปนะ"
        player "ดาว... ชื่อมันติดอยู่ในหัว"
        player "คนแบบนั้นมีจริงไหมวะ"
    elif hard:
        player "เฮ้อ... ฝันอะไรงี้"
        player "ปากร้ายชะมัด แต่ทำไมยังนึกถึงอยู่เลย"
        player "บ้าแล้ว"

    pause 0.8

    # ── เจอดาว ───────────────────────────────

    scene bg school_hallway with fade

    if easy:
        "ระหว่างทางไปห้องเรียน เราเจอเธอที่หน้าห้อง"
        "ดาวยืนมองโทรศัพท์อยู่ สีหน้าไม่ค่อยดี"
        dao "..."
    elif normal:
        "เจอดาวที่บันได เธอเดินผ่านไปเฉย ๆ โดยไม่มอง"
        "เหมือนไม่ได้เห็นเรา... หรือเปล่า?"
        dao "..."
    elif hard:
        "เจอดาวที่บันได"
        "เธอหันมาเห็นเรา แล้วหันหน้าหนีทันที"
        dao "..."

    pause 0.5

    if easy:
        player "ดาว? เป็นอะไรหรือเปล่า?"
        dao "เปล่า... ไม่เป็นไรหรอก"
        dao "แค่..."
        dao "นายไม่ได้ตอบข้อความเลย"
    elif normal:
        player "ดาว"
        dao "..."
        player "เฮ้ ได้ยินไหม"
        dao "ได้ยิน"
        dao "แค่ไม่รู้จะพูดอะไร"
    elif hard:
        player "เฮ้ ทำไมเดินหนี"
        dao "ไม่ได้หนี"
        dao "แค่ไม่อยากคุยด้วย"
        player "เกิดอะไรขึ้นวะ"
        dao "ไม่มีอะไร ก็แค่นายไม่ตอบข้อความ มันเป็นเรื่องใหญ่เหรอ"

    pause 0.5

    # ── จุดระเบิด ────────────────────────────

    if easy:
        dao "ดาวส่งไปห้าทุ่ม... คิดว่าอย่างน้อยก็น่าจะเห็น"
        dao "ก็ไม่เป็นไรค่ะ"
        "เธอยิ้ม แต่มันไม่เหมือนยิ้มในฝันเลย"
    elif normal:
        dao "ส่งข้อความไปสามทุ่ม"
        dao "นายอ่านแล้วด้วย"
        dao "แต่ก็..."
        "เธอหันหน้าไปทางหน้าต่าง"
        dao "ก็ไม่เป็นไรหรอก"
    elif hard:
        dao "ลืมไปเลยก็ได้นะ ไม่ได้สำคัญอะไร"
        dao "แค่รู้ว่าจากนี้ไปอย่ามาถามว่าฉันเป็นอะไร"
        "เธอพูดเร็ว เหมือนท่องมาแล้ว"

    pause 0.6

    # ── TIMED CHOICE ─────────────────────────
    # timeout ขึ้นกับ dao_clingy — ยิ่งหมกมุ่นมาก ยิ่งรอนายน้อย

    if dao_clingy > 55:
        $ limit = 5
    elif dao_clingy <= 20:
        $ limit = 15
    else:
        $ limit = 10

    "..."

    call screen timed_menu(
        items=[
            ("ขอโทษนะ ไม่ได้ตั้งใจ",   "apologize"),
            ("ก็แค่ข้อความ เรื่องใหญ่อะไร", "deflect"),
            ("เมื่อคืนหลับไปก่อน",          "excuse"),
        ],
        timeout=limit,
        default="silent"
    )

    $ ch1_result = _return

    # ── ผลลัพธ์ ──────────────────────────────

    if ch1_result == "apologize":

        if easy:
            dao "..."
            dao "นายพูดตรง ๆ แบบนี้... ทำดาวรู้สึกผิดเองเลยนะ"
            $ dao_trust    += 10
            $ dao_relation += 10
            $ dao_hope     += 5
        elif normal:
            dao "..."
            "เธอหันมามอง สักพักจึงพูด"
            dao "โอเค... เชื่อนาย"
            dao "แต่ครั้งหน้าตอบด้วยนะ"
            $ dao_trust    += 8
            $ dao_relation += 5
        elif hard:
            dao "ขอโทษก็แค่คำพูด"
            "เธอพูดสั้น แต่หูแดงนิดนึง"
            $ dao_trust    += 5
            $ dao_relation += 3
            $ dao_mask     -= 5

    elif ch1_result == "deflect":

        if easy:
            dao "..."
            dao "อ... โอเค"
            "เธอยิ้มน้อยลงกว่าเดิม"
            $ dao_trust    -= 5
            $ dao_relation -= 5
            $ dao_hope     -= 10
        elif normal:
            dao "ใช่ แค่ข้อความ"
            dao "ลืมไปก็ได้"
            "เธอเดินเลยไปก่อน"
            $ dao_trust    -= 10
            $ dao_relation -= 8
            $ dao_clingy   += 5
        elif hard:
            dao "เออ ก็ใช่ แค่ข้อความ"
            dao "งั้นก็ไม่ต้องพูดถึงอีกแล้วกัน"
            $ dao_trust    -= 15
            $ dao_relation -= 10
            $ dao_clingy   += 10

    elif ch1_result == "excuse":

        if easy:
            dao "จริงเหรอ?"
            "เธอมองหน้าเราสักครู่"
            dao "งั้น... โอเคนะ"
            $ dao_trust    += 3
            $ dao_relation += 3
        elif normal:
            dao "..."
            dao "ก็ได้"
            "อ่านน้ำเสียงไม่ออกว่าเชื่อหรือเปล่า"
            $ dao_trust    += 1
            $ dao_relation -= 2
        elif hard:
            dao "หลับ งั้นหรอ"
            dao "โอเค เชื่อ"
            "เธอพูดแห้ง ๆ แล้วเดินเลยไป"
            $ dao_trust    -= 5
            $ dao_relation -= 5
            $ dao_mask     += 5

    else:  # silent / timeout

        "..."
        "คำพูดมันอยู่ในหัว แต่ปากไม่ยอมเปิด"

        if easy:
            dao "...นายไม่พูดอะไรเลย"
            "เธอหัวเราะเบา ๆ แต่มันว่างเปล่า"
            $ dao_hope     -= 15
            $ dao_trust    -= 10
            $ dao_relation -= 10
        elif normal:
            "เธอรอสักครู่ แล้วพยักหน้า"
            dao "โอเค... เข้าใจแล้ว"
            $ dao_hope     -= 20
            $ dao_trust    -= 15
            $ dao_relation -= 15
            $ dao_clingy   += 10
        elif hard:
            dao "เงียบงั้นหรอ"
            dao "ก็ดี ฉันก็ไม่ได้อยากฟังอยู่แล้ว"
            "เธอเดินเลยไปโดยไม่หันมาอีก"
            $ dao_hope     -= 25
            $ dao_trust    -= 20
            $ dao_relation -= 20
            $ dao_clingy   += 15

    pause 0.8

    # ── ปิดฉาก ───────────────────────────────

    scene black with dissolve

    "วันนั้นเราไม่ได้คุยกันอีกเลย"

    if dao_hope <= HOPE_LOW:
        "มีบางอย่างที่รู้สึกว่า... อาจจะสายเกินไปแล้ว"
    else:
        "แต่ยังไงก็ตาม เธอยังอยู่ที่นี่"
        "และนายก็ยังอยู่ที่นี่"

    jump chapter2

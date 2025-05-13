label test:
    if dao_clingy > 55:
        $ limit = 5
    elif dao_clingy <= 50:
        $ limit = 10
    else:
        $ limit = 15

    "ดาว" "ทำไมไม่สนใจดาวเลย..."

    call screen timed_menu(
        items=[
            ("ขอโทษนะ", "apologize"),
            ("เงียบ", "silent"),
            ("แล้วไง ใครสน", "rude"),
        ],
        timeout=limit,
        default="silent"
    )
    $ timer_result = _return

    if timer_result == "apologize":
        "ดาว" "อย่างน้อยนายก็รู้ตัว..."
        $ dao_trust += 10
        $ dao_relation +=10
        jump after_argument

    elif timer_result == "rude":
        "ดาว" "งั้นไม่ต้องมาคุยกันอีก!"
        $ dao_trust -= 30
        $ dao_relation -=10
        jump after_argument

    else:  # silent or timeout
        "ดาว" "...เงียบสินะ"
        $ dao_trust -= 10
        $ dao_relation -=20
        jump after_argument

label after_argument:

dao "ขอโทษนะ พอดี คนสร้างดาวอยากทดสอบนายน่ะ"
"Debug ความงี่เง่า: [dao_clingy]"
"Debug ความสัมพันธ์: [dao_relation]"
return
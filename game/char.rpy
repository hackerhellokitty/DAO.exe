init:
    default easy   = False
    default normal = False
    default hard   = False


# ──────────────────────────────────────────
#  ตัวละคร
# ──────────────────────────────────────────

define shadowchar = Character("???",  color="#AAAAFF")
define me         = Character("")
define girl       = Character("Girl", color="#AAAAFF")

# ดาว — สีเปลี่ยนตาม mode (set ใน difficulty.rpy)
define dao_easy   = Character("ดาว", color="#FFB3C6")   # ชมพูอบอุ่น — ใส ๆ อินโนเซนต์
define dao_normal = Character("ดาว", color="#A8C8E8")   # ฟ้าเย็น   — น่ารัก ซ่อนความรู้สึก
define dao_hard   = Character("ดาว", color="#E88080")   # แดงหม่น   — ซึน ปากร้าย

# alias ที่ใช้ใน script (จะถูก set หลัง difficulty เลือก)
default dao = dao_normal


# ──────────────────────────────────────────
#  Stats ดาว
#  ทุกค่าอยู่ในช่วง 0–100
#  ค่าเริ่มต้นจะถูก override ใน difficulty.rpy
# ──────────────────────────────────────────

# ความสัมพันธ์โดยรวม
# สูง  → เธอเปิดใจ พูดคุยง่าย
# ต่ำ  → เธอระวังตัว เงียบ ห่างเหิน
default dao_relation = 0

# ความไว้วางใจ
# สูง  → เล่าเรื่องส่วนตัว ยอมให้เข้าใกล้
# ต่ำ  → ปิดกั้น ไม่ยอมรับความช่วยเหลือ
default dao_trust    = 0

# ความหมกมุ่น / ตามล้าน
# สูง  → timer choice สั้น หึง บ่อย สังเกตทุกอย่าง
# ต่ำ  → มั่นคงในตัวเอง ไม่ตื่นตระหนก
default dao_clingy   = 0

# ความหึง (ต่างจาก clingy — นี่คือ reactive ต่อ trigger เฉพาะ)
# สูง  → ระเบิดเมื่อเห็นผู้เล่นสนใจคนอื่น
# ต่ำ  → วางเฉย หรือซ่อนได้
default dao_jealousy = 0

# ความหวัง (ในความสัมพันธ์)
# สูง  → เธอยังพยายาม ยังรอ
# ต่ำ  → เริ่มถอย → ถ้าลด 0 อาจ trigger bad ending
default dao_hope     = 0

# หน้ากาก (Hard mode เป็นหลัก)
# สูง  → ซ่อนความรู้สึกเก่ง ผู้เล่นอ่านไม่ออก
# ต่ำ  → เริ่มแตก เริ่มพูดสิ่งที่รู้สึกจริง ๆ
default dao_mask     = 0


# ──────────────────────────────────────────
#  Threshold — ใช้ใน if/elif เพื่อกำหนด reaction
# ──────────────────────────────────────────

define TRUST_CLOSE    = 60    # ไว้ใจพอจะเล่าเรื่องส่วนตัว
define TRUST_BROKEN   = 20    # ความไว้ใจพัง — เธอเริ่มปิดตัว

define CLINGY_HIGH    = 55    # หมกมุ่นหนัก — timer สั้น, react ไว
define CLINGY_EXTREME = 80    # วิกฤต — เริ่มทำสิ่งที่ไม่สมเหตุสมผล

define HOPE_LOW       = 25    # ความหวังเริ่มหมด — dialogue เปลี่ยน tone
define HOPE_DEAD      = 10    # ถ้าต่ำกว่านี้ → เส้นทาง bad ending เปิด

define MASK_CRACKED   = 30    # หน้ากากเริ่มแตก — ดาว hard เริ่มพูดตรง

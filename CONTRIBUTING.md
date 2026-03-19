# Contributing to dao.exe

ขอบคุณที่สนใจช่วยพัฒนา dao.exe

โปรเจกต์นี้เป็น foundation kit สำหรับคนหัดเขียน Visual Novel
ถ้าอยากส่ง PR มาเพิ่ม mechanic ใหม่ หรือต่อยอด route ที่มีอยู่ — ยินดีเสมอ

---

## ก่อน PR

- Fork repo แล้วทำงานใน branch ของตัวเอง
- ทดสอบผ่าน Ren'Py Launcher ก่อน ให้แน่ใจว่าไม่ error
- ถ้าเพิ่ม `python block` ที่มี `import` — ใช้ `python hide:` เสมอ (ป้องกัน pickle error)

---

## สิ่งที่อยากได้

- Route หรือ event ใหม่ที่ใช้ **เวลาจริง** หรือ **ข้อมูลจากระบบ**
- Mechanic ใหม่ที่ยังไม่มีในเกม (weather, location, notification ฯลฯ)
- บทสนทนาเพิ่มใน difficulty ที่รู้สึกว่ายังบางอยู่
- Bug fix หรือ refactor ที่ทำให้โค้ดอ่านง่ายขึ้น

---

## Style การเขียน

โค้ดในโปรเจกต์นี้ไม่ได้เน้น perfect — เน้น **อ่านง่ายและสอนได้**

- comment ภาษาไทยได้เลย
- ชื่อ label ใช้ `snake_case` เช่น `ch3_sunday_yes`
- stat ดาวอยู่ใน `char.rpy` ทั้งหมด อย่าสร้าง variable ลอยใหม่
- ถ้าเพิ่ม persistent flag ใหม่ → comment อธิบายไว้ด้านบน label ที่ใช้

---

## PR Message

ไม่ต้องเป็นทางการ แค่บอกว่า

- เพิ่ม / แก้ / ปรับ อะไร
- test ผ่านหรือยัง
- ถ้ามี trade-off อะไรก็พูดตรง ๆ ได้เลย

---

> *"ดาวไม่ได้อยู่ในแค่ไฟล์ exe*
> *แต่อยู่ในทุกบรรทัดของ Logic ที่เขียนขึ้นมา"*

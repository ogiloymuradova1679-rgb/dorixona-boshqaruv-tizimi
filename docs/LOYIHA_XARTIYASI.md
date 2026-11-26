# Loyiha xartiyasi

## 1. Pasport

| Maydon | Qiymat |
|---|---|
| Loyiha nomi | DoriMed — dorixona boshqaruv tizimi |
| Loyiha kodi | DOR-2026 |
| Buyurtmachi | Urganch davlat universiteti, «Loyihalarni boshqarish» fani |
| Ijrochi | Murodova O'g'iloy Qahramon qizi, KIDT, 236-guruh |
| Qabul qiluvchi | Xusainov Shixnazar |
| Boshlanish | 05.10.2026 |
| Yakun | 13.12.2026 |
| Platforma | Web ilova |
| Byudjet | 0 so'm to'g'ridan-to'g'ri xarajat; 120 soat mehnat |
| Asosiy natija | GitHub Pages'dagi ishlaydigan demo va 7 ta laboratoriya hujjati |

## 2. Muammo va imkoniyat

Kichik dorixonalarda qoldiq va yaroqlilik muddati ko'pincha daftar yoki alohida Excel fayllarida yuritiladi. Natijada:

- bir xil dori uchun bir nechta yozuv paydo bo'ladi;
- qoldiq haqiqiy holatga mos kelmaydi;
- yaroqlilik muddati o'tgan dori o'z vaqtida aniqlanmaydi;
- hisobot tayyorlash uzoq vaqt oladi.

Bir faylli web ilova bu jarayonni soddalashtirishi mumkin: uni o'rnatish oson, internet shart emas va ma'lumotlar brauzerda saqlanadi. Loyiha aynan shu ehtiyojni tekshirish uchun mo'ljallangan.

## 3. Loyiha maqsadi

Dorilar, ishlab chiqaruvchilar, kirim-chiqim va hisobotlarni yagona interfeysda boshqarish imkonini beruvchi, GitHub Pages orqali ochiladigan ishlaydigan web prototipini yaratish.

### Muvaffaqiyat mezonlari

1. Barcha asosiy ombor amallari brauzerda bajariladi.
2. Qoldiq kirim va chiqimda avtomatik o'zgaradi.
3. Muddati o'tgan dori chiqimi bloklanadi.
4. Boshqaruv paneli 4 ta asosiy KPI va 2 ta diagrammani ko'rsatadi.
5. Hisobot CSV va chop etish shaklida olinadi.
6. Demo GitHub Pages'da ochiladi.
7. CI muvaffaqiyatli yakunlanadi.
8. 7 ta laboratoriya hujjati 10–20 bet oralig'ida topshiriladi.

## 4. Qamrov

**Kiradi:** boshqaruv paneli, dorilar registri, ishlab chiqaruvchilar, kirim-chiqim, qoldiq, muddat nazorati, hisobot, CSV, JSON zaxira, mobil moslashuv, GitHub Pages, CI.

**Kirmaydi:** to'lov, kassa, retsept imzosi, server autentifikatsiyasi, bulutli baza, davlat tizimlari integratsiyasi, shtrix-kod skaneri.

## 5. Mahsulot va natijalar

| Natija | Tavsif | Topshirish |
|---|---|---|
| D1 | `index.html` — to'liq ishlaydigan ilova | 8-hafta |
| D2 | Texnik topshiriq | 2-hafta |
| D3 | GitHub repozitoriyasi va README | 1-hafta |
| D4 | User story va sprint reja | 3-hafta |
| D5 | Gantt diagrammasi va risk registri | 5-hafta |
| D6 | CI pipeline va code review dalillari | 6-hafta |
| D7 | 7 ta laboratoriya hujjati | 9-hafta |
| D8 | Yakuniy demo va himoya | 10-hafta |

## 6. Bosqichlar

| Bosqich | Asosiy ish | Natija | Sana |
|---|---|---|---|
| I. Tashabbus | Muammo tahlili, xartiya, repo | D3 | 05–11.10 |
| II. Talablar | User story, acceptance criteria, prioritet | D4 | 12–18.10 |
| III. Dizayn | Interfeys eskizi, ma'lumotlar modeli | prototip | 21.09–04.10 |
| IV. Ishlab chiqish | Dorilar, hamkorlar, kirim-chiqim | D1 beta | 19.10–13.11 |
| V. Tahlil | Hisobot, diagrammalar, CSV | D1 | 02–13.11 |
| VI. Sifat | CI, code review, testlar | D6 | 02–24.11 |
| VII. Hujjat | 7 ta laboratoriya ishi | D7 | 02.11–06.12 |
| VIII. Topshirish | Demo, himoya | D8 | 07–13.12 |

## 7. Resurslar

- **Inson resursi:** 1 nafar talaba (loyiha menejeri, analitik, dasturchi, tester va hujjatchi rollarida).
- **Texnika:** shaxsiy kompyuter, brauzer, Git, Python, LibreOffice.
- **Xizmatlar:** GitHub Free, GitHub Actions, GitHub Pages.
- **Vaqt:** haftasiga 10–14 soat, jami taxminan 120 soat.
- **Moliyaviy xarajat:** 0 so'm (bepul xizmatlar).

## 8. Manfaatdor tomonlar

| Tomon | Ta'siri | Qiziqishi |
|---|---|---|
| Talaba | Yuqori | Loyihani muvaffaqiyatli topshirish |
| O'qituvchi / qabul qiluvchi | Yuqori | Talablar va hujjatlar sifati |
| Universitet | O'rta | O'quv natijasi |
| Kelgusi foydalanuvchi (dorixona) | O'rta | Qulay va ishonchli vosita |
| GitHub platformasi | Past | Xizmat ko'rsatish |

## 9. Asosiy risklar

| Risk | Ta'sir | Reja |
|---|---|---|
| Vaqt yetishmasligi | Yuqori | MVP qamrovini muzlatish, past prioritetlarni keyinga qoldirish |
| LocalStorage yo'qolishi | Yuqori | JSON zaxira, demo tiklash |
| Brauzerlar farqi | O'rta | Chrome, Firefox va mobil testlar |
| Bitta fayl hajmining o'sishi | O'rta | Kodni bo'limlarga ajratish, CI hajm tekshiruvi |
| GitHub Pages nosozligi | O'rta | Lokal ishga tushirish yo'riqnomasi |
| Autentifikatsiya yo'qligi | O'rta | Demo cheklovi sifatida hujjatlashtirish |

To'liq risk registri L4 hujjatida keltiriladi.

## 10. Qabul qilish

Loyiha quyidagi holatda qabul qilinadi:

- demo havolasi ishlaydi;
- asosiy foydalanish stsenariylari bajariladi;
- CI yashil holatda;
- 7 ta DOCX va texnik topshiriq mavjud;
- GitHub repozitoriyasida kod va hujjatlar ochiq.

**Imzolar:**

| Rol | F.I.Sh. | Imzo | Sana |
|---|---|---|---|
| Ijrochi | Murodova O'g'iloy Qahramon qizi |  |  |
| Qabul qiluvchi | Xusainov Shixnazar |  |  |

**Repozitoriy:** <https://github.com/ogiloymuradova1679-rgb/dorixona-boshqaruv-tizimi>

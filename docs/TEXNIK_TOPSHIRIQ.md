# DORIXONA BOSHQARUV TIZIMI
## Texnik topshiriq

| Maydon | Qiymat |
|---|---|
| Loyiha nomi | DoriMed — dorixona boshqaruv tizimi |
| Hujjat versiyasi | 1.0 |
| Hujjat sanasi | 26.11.2026 |
| Buyurtmachi | Urganch davlat universiteti, «Loyihalarni boshqarish» fani |
| Ijrochi | Murodova O'g'iloy Qahramon qizi |
| Qabul qiluvchi | Xusainov Shixnazar |
| Platforma | Web ilova (bitta HTML fayl) |
| Joylashtirish | GitHub Pages |
| Holati | Amalga oshirilgan demo |

---

## 1. Loyihaning maqsadi

Dorixona faoliyatida dori vositalarining qoldig'i, narxi, partiyasi va yaroqlilik muddatini qog'oz daftar yoki alohida Excel fayllari orqali yuritish ma'lumotlarning takrorlanishiga, qoldiqning hisobdan chiqib ketishiga va muddati o'tgan dorining sotilishiga olib kelishi mumkin.

Loyihaning maqsadi — dorixona ombori uchun oddiy, tez o'zlashtiriladigan va server talab qilmaydigan boshqaruv tizimini yaratish. Tizim quyidagi amaliy muammolarni hal qilishi kerak:

1. dori kartochkalarini yagona registrda saqlash;
2. ishlab chiqaruvchi va yetkazib beruvchi ma'lumotlarini bog'lash;
3. har bir kirim va chiqimni qayd etish hamda qoldiqni avtomatik hisoblash;
4. yaroqlilik muddati yaqinlashgan va muddati o'tgan dorilarni ajratib ko'rsatish;
5. minimal qoldiqdan pastga tushgan dorilar bo'yicha ogohlantirish berish;
6. ombor qiymati va potensial tushumni hisoblash;
7. ma'lumotlarni zaxiralash va qayta tiklash;
8. natijani GitHub Pages orqali ko'rsatish.

Loyiha o'quv loyihasi bo'lgani uchun maqsad — real dorixona uchun to'liq ERP emas, balki asosiy ombor jarayonlarini qamrab oluvchi ishlaydigan MVP prototipini yaratish.

## 2. Qamrov

### 2.1. Qamrovga kiradi

- boshqaruv paneli (KPI kartochkalari, diagrammalar, ogohlantirishlar);
- dori vositalari registri va kartochkalarini boshqarish;
- ishlab chiqaruvchilar registri;
- kirim va chiqim operatsiyalari;
- qoldiqni avtomatik yangilash;
- yaroqlilik muddati nazorati;
- minimal qoldiq nazorati;
- qidiruv, filtrlash va saralash;
- ombor hisoboti, CSV eksport va chop etish;
- JSON zaxira nusxasi;
- demo ma'lumotlarini tiklash;
- mobil moslashuv;
- GitHub Pages demo va CI tekshiruvi.

### 2.2. Qamrovga kirmaydi

- real to'lov tizimi va kassa apparati integratsiyasi;
- onlayn dorixona va yetkazib berish moduli;
- retseptlarni raqamli imzolash;
- foydalanuvchi rollari va server tomonidagi autentifikatsiya;
- bulutli ma'lumotlar bazasi;
- soliq va buxgalteriya hisobotlari;
- davlat tibbiyot axborot tizimlari bilan integratsiya;
- shtrix-kod skaneri va printer bilan apparat integratsiyasi.

Bu cheklovlar demo versiyaning texnik topshiriq doirasida ongli ravishda qabul qilingan. Kelgusi versiyalarda ular alohida bosqichlarda qo'shilishi mumkin.

## 3. Foydalanuvchilar

| Rol | Tavsif | Demo versiyadagi huquqlar |
|---|---|---|
| Administrator | Ombor va dori kartochkalarini yuritadi | Barcha bo'limlarga to'liq kirish |
| Dorixona mudiri | Qoldiq va hisobotlarni nazorat qiladi | Ko'rish, hisobot, eksport |
| Sotuvchi / farmatsevt | Kirim-chiqimni qayd etadi | Dori qidirish, kirim-chiqim |
| O'quvchi / mehmon | Demo sahifasini ko'radi | Demo ma'lumotlarini ko'rish |

Demo versiyada autentifikatsiya o'chirilgan: barcha foydalanuvchilar administrator sifatida ishlaydi. Bu qaror o'quv ko'rgazmasi uchun qulaylik yaratadi, lekin ishlab chiqarish muhitida rolga asoslangan ruxsatlar majburiy bo'lishi kerak.

## 4. Asosiy foydalanish stsenariylari

### UC-01. Yangi dori qo'shish

**Aktyor:** administrator.  
**Shart:** ishlab chiqaruvchi bazada mavjud.  
**Asosiy oqim:** administrator «Yangi dori» tugmasini bosadi, nom, kategoriya, ishlab chiqaruvchi, partiya, yaroqlilik muddati, tannarx, sotuv narxi, qoldiq va minimal qoldiqni kiritadi. Tizim majburiy maydonlarni tekshiradi va kartochkani saqlaydi.  
**Natija:** dori jadvalda paydo bo'ladi; KPI va kategoriya diagrammasi yangilanadi.

### UC-02. Kirim qayd etish

**Aktyor:** administrator yoki sotuvchi.  
**Shart:** dori mavjud.  
**Asosiy oqim:** «Kirim-chiqim» bo'limida «Kirim» tanlanadi, dori va miqdor kiritiladi. Tizim birlik narxini dorining tannarxidan oladi, summani hisoblaydi va qoldiqni oshiradi.  
**Natija:** harakatlar tarixida yangi yozuv paydo bo'ladi; qoldiq yangilanadi.

### UC-03. Chiqim qayd etish

**Aktyor:** administrator yoki sotuvchi.  
**Shart:** dori qoldig'i yetarli va muddati o'tmagan.  
**Asosiy oqim:** «Chiqim» tanlanadi, dori va miqdor kiritiladi. Tizim qoldiqni tekshiradi, summani sotuv narxida hisoblaydi va qoldiqni kamaytiradi.  
**Muqobil oqim:** qoldiq yetarli bo'lmasa yoki dori muddati o'tgan bo'lsa, operatsiya bloklanadi va xabar beriladi.  
**Natija:** qoldiq yangilanadi, harakat tarixi saqlanadi.

### UC-04. Yaroqlilik muddatini nazorat qilish

**Asosiy oqim:** tizim har bir dori uchun bugungi sana va yaroqlilik sanasi orasidagi kunlar sonini hisoblaydi. 60 kundan kam qolgan dorilar «Muddati yaqin», o'tganlar «Muddati o'tgan» deb belgilanadi. Boshqaruv panelida va dorilar jadvalida ko'rsatiladi.

### UC-05. Hisobot olish

**Asosiy oqim:** «Hisobotlar» bo'limida tannarx, sotuv qiymati, potensial foyda va muddati o'tgan zaxira hisoblanadi. Kategoriyalar bo'yicha jadval, muddat taqsimoti va eng qimmat zaxiralar ko'rsatiladi. Administrator CSV yuklab olishi yoki hisobotni chop etishi mumkin.

### UC-06. Zaxira nusxasini tiklash

**Asosiy oqim:** administrator avval olingan JSON faylni tanlaydi. Tizim fayl strukturasini tekshiradi, tasdiqlash oynasini ko'rsatadi va ma'lumotlarni yuklaydi.  
**Muqobil oqim:** fayl formati noto'g'ri bo'lsa, xato xabari beriladi.

## 5. Funktsional talablar

| ID | Talab | Prioritet | Qabul mezonlari |
|---|---|---|---|
| FR-01 | Dori vositalari ro'yxatini ko'rsatish | Yuqori | Jadvalda barcha dorilar, qoldiq va holat ko'rinadi |
| FR-02 | Dori qo'shish | Yuqori | Majburiy maydonlar tekshiriladi, yangi yozuv saqlanadi |
| FR-03 | Dorini tahrirlash | Yuqori | O'zgarishlar jadval va KPI'da aks etadi |
| FR-04 | Dorini o'chirish | O'rta | Tasdiqlashdan keyin kartochka o'chadi, tarix saqlanadi |
| FR-05 | Ishlab chiqaruvchilarni boshqarish | Yuqori | Qo'shish, tahrirlash, bog'langan dori bo'lsa o'chirishni bloklash |
| FR-06 | Kirim operatsiyasi | Yuqori | Qoldiq miqdorga ortadi, tarix yoziladi |
| FR-07 | Chiqim operatsiyasi | Yuqori | Qoldiq yetarliligi tekshiriladi, qoldiq kamayadi |
| FR-08 | Muddati o'tgan dorini bloklash | Yuqori | Chiqimda xato xabari chiqadi, qoldiq o'zgarmaydi |
| FR-09 | Qidiruv | Yuqori | Nom, partiya, ishlab chiqaruvchi va javon bo'yicha ishlaydi |
| FR-10 | Filtrlash | O'rta | Kategoriya va holat bo'yicha ro'yxat o'zgaradi |
| FR-11 | KPI kartochkalari | Yuqori | Dori soni, ombor qiymati, kam qoldiq, muddat ko'rsatiladi |
| FR-12 | Diagrammalar | O'rta | 7 kunlik kirim-chiqim va kategoriya ulushi ko'rinadi |
| FR-13 | Ogohlantirishlar | Yuqori | Kam qoldiq, tugagan, muddati yaqin dorilar chiqadi |
| FR-14 | Hisobot | Yuqori | Tannarx, sotuv qiymati, foyda va muddat taqsimoti hisoblanadi |
| FR-15 | CSV eksport | O'rta | Yuklab olingan fayl UTF-8 va nuqta-vergul bilan ajratilgan |
| FR-16 | Chop etish | O'rta | Faqat faol hisobot sahifasi oq-qora A4 ko'rinishida chiqadi |
| FR-17 | JSON zaxira | O'rta | Barcha ma'lumotlar bitta faylga yuklanadi |
| FR-18 | JSON tiklash | O'rta | Struktura tekshiriladi va ma'lumotlar yuklanadi |
| FR-19 | Demo ma'lumotlarini tiklash | Past | 20 ta dori, 13 ta hamkor va 20 ta harakat qayta yuklanadi |
| FR-20 | Mobil moslashuv | Yuqori | 390 px kenglikda asosiy funksiyalar ishlaydi |

## 6. Nofunksional talablar

| ID | Talab | Mezon |
|---|---|---|
| NFR-01 | Ishlash tezligi | 20–100 ta dori bilan sahifa 1 soniyadan tez ochiladi |
| NFR-02 | Offline ishlash | Tashqi CDN va API bo'lmaganda ham ishlaydi |
| NFR-03 | Yagona fayl | Asosiy ilova `index.html` ichida, alohida runtime fayllarsiz |
| NFR-04 | Moslashuv | 390, 768, 1024 va 1440 px kengliklarda tekshirilgan |
| NFR-05 | Brauzerlar | Chrome, Firefox, Edge va Safari'ning zamonaviy versiyalari |
| NFR-06 | Xavfsizlik | Kiritilgan matn HTML sifatida bajarilmaydi (escaping) |
| NFR-07 | Ma'lumot yaxlitligi | Qoldiq manfiy bo'lmaydi, chiqim qoldiqdan oshmaydi |
| NFR-08 | Saqlash ishonchliligi | `localStorage` xatosi foydalanuvchiga xabar qilinadi |
| NFR-09 | Kod sifati | Bitta HTML faylda CI orqali struktura va JS sintaksisi tekshiriladi |
| NFR-10 | Hujjatlashtirish | README, texnik topshiriq va 7 ta laboratoriya ishi mavjud |

## 7. Ma'lumotlar modeli

### 7.1. `medicines`

| Maydon | Tur | Izoh |
|---|---|---|
| `id` | string | Unikal identifikator |
| `name` | string | Dori nomi va dozasi |
| `category` | string | Farmakologik kategoriya |
| `manufacturerId` | string | `manufacturers.id` ga havola |
| `batch` | string | Partiya raqami |
| `expiry` | date | Yaroqlilik muddati, `YYYY-MM-DD` |
| `purchasePrice` | number | Tannarx, so'm |
| `price` | number | Sotuv narxi, so'm |
| `stock` | number | Joriy qoldiq |
| `minStock` | number | Minimal qoldiq chegarasi |
| `unit` | string | O'lchov birligi |
| `shelf` | string | Javon yoki saqlash joyi |
| `description` | string | Qo'shimcha tavsif |

### 7.2. `manufacturers`

`id`, `name`, `country`, `phone`, `email`, `note` maydonlari saqlanadi.

### 7.3. `transactions`

| Maydon | Tur | Izoh |
|---|---|---|
| `id` | string | Harakat identifikatori |
| `type` | `in` / `out` | Kirim yoki chiqim |
| `medicineId` | string | Dori identifikatori |
| `medicineName` | string | Voqea paytidagi nom (tarix uchun) |
| `qty` | number | Miqdor |
| `unit` | string | Birlik |
| `unitPrice` | number | Voqea paytidagi birlik narx |
| `total` | number | Umumiy summa |
| `date` | date | Operatsiya sanasi |
| `note` | string | Izoh |
| `createdAt` | datetime | Yozuv yaratilgan vaqt |

### 7.4. Holat qoidasi

```text
agar expiry < bugun                   -> "Muddati o'tgan"
agar stock <= 0                       -> "Tugagan"
agar expiry - bugun <= 60 kun         -> "Muddati yaqin"
agar stock <= minStock                -> "Kam qoldiq"
aks holda                             -> "Yaroqli"
```

Ushbu tartib muhim: muddati o'tgan dori qoldiq holatidan qat'i nazar birinchi navbatda xavfli deb belgilanadi.

## 8. Interfeys talablari

1. Asosiy navigatsiya chap tomonda, mobil qurilmada yig'iladigan menyu ko'rinishida bo'lishi.
2. Har bir sahifa sarlavhasi, qisqa tavsifi va asosiy amal tugmasi bilan boshlanishi.
3. Jadvalda dori nomi, partiyasi, ishlab chiqaruvchisi, kategoriyasi, muddati, narxi, qoldig'i va holati ko'rinishi.
4. Xavfli holatlar qizil, ogohlantirishlar sariq, normal holat yashil rangda ajratilishi.
5. Formalar modal oynada ochilishi va xato holatida sababni ko'rsatishi.
6. Katta jadvallar gorizontal aylanishi, sahifa esa mobilda buzilmasligi.
7. Rang kontrasti WCAG 2.1 AA darajasiga yaqin bo'lishi.

## 9. Texnik arxitektura

Ilova klassik uch qatlamli ko'rinishning brauzer ichidagi soddalashtirilgan variantidan foydalanadi:

```text
Foydalanuvchi
    │
    ▼
HTML interfeys (sahifalar, formalar, modallar)
    │
    ▼
JavaScript mantiq (holat, hisob-kitob, validatsiya)
    │
    ├── Canvas diagrammalar
    ├── CSV / JSON / Print
    └── localStorage
```

Tashqi API yo'q. Bu yondashuvning afzalligi — joylashtirish qulayligi va offline ishlash; kamchiligi — ma'lumotlar faqat bitta brauzerda qolishi va ko'p foydalanuvchi uchun mos emasligi.

## 10. Sifat mezonlari va testlar

| Test | Kutilgan natija |
|---|---|
| T-01 yangi dori qo'shish | Jadvalda yangi qator, KPI yangilangan |
| T-02 noto'g'ri narx kiritish | Forma saqlanmaydi, xato ko'rsatiladi |
| T-03 qoldiqdan ko'p chiqim | Operatsiya bloklanadi |
| T-04 muddati o'tgan dorini chiqim qilish | Operatsiya bloklanadi |
| T-05 dori o'chirish | Tasdiqlashdan keyin ro'yxatdan chiqadi |
| T-06 ishlab chiqaruvchini o'chirish | Bog'langan dori bo'lsa bloklanadi |
| T-07 qidiruv | Mos yozuvlar ko'rsatiladi |
| T-08 CSV eksport | UTF-8 fayl yuklab olinadi |
| T-09 zaxira va tiklash | Barcha massivlar tiklanadi |
| T-10 mobil menyu | Menyu ochiladi va sahifa almashadi |

Testlar qo'lda brauzerda va Playwright yordamida avtomatlashtirilgan stsenariylar orqali bajarilgan. CI'da esa HTML tuzilmasi va JavaScript sintaksisi tekshiriladi.

## 11. Yetkazib berish rejasi

| Bosqich | Natija | Davr |
|---|---|---|
| Tahlil | Texnik topshiriq, user story'lar | 1–2-hafta |
| Loyihalash | Interfeys eskizi, ma'lumotlar modeli | 3-hafta |
| Ishlab chiqish | Dorilar, hamkorlar, kirim-chiqim | 3–6-hafta |
| Hisobot va sifat | Diagrammalar, hisobot, CI | 5–7-hafta |
| Sinov | Funksional va mobil testlar | 6–9-hafta |
| Topshirish | Hujjatlar, demo, himoya | 9–10-hafta |

## 12. Qabul qilish mezonlari

Loyiha quyidagi shartlar bajarilganda qabul qilingan hisoblanadi:

- `index.html` tashqi fayllarsiz ochiladi va demo ma'lumotlarini yuklaydi;
- dori qo'shish, tahrirlash va o'chirish ishlaydi;
- kirim qoldiqni oshiradi, chiqim qoldiqni kamaytiradi;
- muddati o'tgan dori chiqim qilinmaydi;
- kam qoldiq va muddat ogohlantirishlari ko'rinadi;
- hisobot va CSV eksport ishlaydi;
- JSON zaxira va tiklash ishlaydi;
- mobil ko'rinishda asosiy amallar bajariladi;
- GitHub Pages manzilida demo ochiladi;
- GitHub Actions CI muvaffaqiyatli yakunlanadi;
- 7 ta laboratoriya hujjati va loyiha kodi repozitoriyada mavjud.

## 13. Cheklovlar va kelgusi ishlar

Demo versiyaning asosiy cheklovi — server va autentifikatsiya yo'qligi. Kelgusi versiyada quyidagilar rejalashtirilgan:

1. foydalanuvchi rollari va JWT autentifikatsiya;
2. PostgreSQL yoki SQLite asosidagi server API;
3. dorixona filiallari o'rtasida sinxronizatsiya;
4. shtrix-kod skaneri;
5. talabni prognozlash (MLOps);
6. audit jurnali va o'zgarishlar tarixi;
7. ko'p tilli interfeys;
8. real vaqt rejimida bildirishnomalar.

---

**Ilova:** [DoriMed demo](https://ogiloymuradova1679-rgb.github.io/dorixona-boshqaruv-tizimi/)  
**Repozitoriy:** [github.com/ogiloymuradova1679-rgb/dorixona-boshqaruv-tizimi](https://github.com/ogiloymuradova1679-rgb/dorixona-boshqaruv-tizimi)

# DoriMed arxitekturasi

## 1. Umumiy ko'rinish

DoriMed — brauzerda mustaqil ishlaydigan bir sahifali ilova (SPA). Asosiy fayl `index.html` ichida HTML tuzilmasi, CSS uslublari va JavaScript mantig'i birlashtirilgan. Ilova tashqi serverga murojaat qilmaydi, shuning uchun GitHub Pages, lokal fayl yoki oddiy statik server orqali bir xil ishlaydi.

```text
┌──────────────────────────────────────────────┐
│                 Brauzer                      │
│                                              │
│  ┌──────────────┐   ┌────────────────────┐   │
│  │  HTML/CSS    │   │  JavaScript modul  │   │
│  │  interfeys   │◄──│  holat va mantiq   │   │
│  └──────────────┘   └─────────┬──────────┘   │
│                               │              │
│       ┌───────────────────────┼──────────┐   │
│       ▼                       ▼          ▼   │
│  ┌─────────┐          ┌────────────┐  ┌──────┐│
│  │ Canvas  │          │ localStorage│ │ CSV  ││
│  │ charts  │          │  (JSON)    │ │ JSON ││
│  └─────────┘          └────────────┘  └──────┘│
└──────────────────────────────────────────────┘
```

## 2. Qatlamlar

### 2.1. Taqdimot qatlami

- yon menyu va yuqori panel;
- oltita sahifa: boshqaruv paneli, dorilar, ishlab chiqaruvchilar, kirim-chiqim, hisobotlar, sozlamalar;
- modal formalar;
- toast bildirishnomalari;
- moslashuvchan CSS Grid va Flexbox.

### 2.2. Mantiq qatlami

JavaScript IIFE ichida quyidagi mas'uliyatlar ajratilgan:

| Funksiya guruhi | Vazifa |
|---|---|
| `loadDB`, `saveDB` | ma'lumotlarni yuklash va saqlash |
| `renderDashboard` | KPI, so'nggi harakatlar, ogohlantirishlar |
| `renderMedicineTable` | qidiruv va filtr natijalarini jadvalga chiqarish |
| `renderTransactions` | kirim-chiqim tarixi va shakl holati |
| `renderReports` | moliyaviy va muddat hisobotlari |
| `statusOf` | dori holatini aniqlash |
| `addTransaction` | qoldiq va audit yozuvini yangilash |
| `openModal` | umumiy modal oynani boshqarish |
| `drawFlowChart`, `drawCategoryChart` | Canvas diagrammalar |
| `exportReportCSV`, `downloadBackup` | fayl eksporti |

### 2.3. Saqlash qatlami

Barcha ma'lumotlar bitta JSON obyekt sifatida `localStorage`'da `dorimed_db_v1` kaliti ostida saqlanadi:

```json
{
  "version": 1,
  "manufacturers": [],
  "medicines": [],
  "transactions": [],
  "updatedAt": "2026-11-26T10:30:00.000Z"
}
```

Bu yondashuv kichik demo uchun yetarli. Katta hajmdagi ma'lumotlarda brauzer xotirasi cheklovi (odatda 5–10 MB) hisobga olinishi kerak. Shuning uchun JSON zaxira nusxasi nazarda tutilgan.

## 3. Ma'lumot oqimi

### 3.1. Dori qo'shish

```text
Forma → validatsiya → db.medicines.push() → saveDB()
      → renderAll() → KPI, jadval va diagramma yangilanadi
```

### 3.2. Chiqim operatsiyasi

```text
Dori tanlash → muddat tekshiruvi → qoldiq tekshiruvi
            → stock = stock - qty
            → transactions.push()
            → saveDB() → UI yangilanishi
```

Muddati o'tgan dori yoki qoldiqdan ortiq miqdor uchun funksiya erta qaytadi; qoldiq va tarix o'zgarmaydi.

## 4. Holat hisoblash qoidasi

```js
function statusOf(medicine) {
  const days = daysLeft(medicine);
  if (days < 0) return 'expired';
  if (medicine.stock <= 0) return 'out';
  if (days <= 60) return 'expiring';
  if (medicine.stock <= medicine.minStock) return 'low';
  return 'ok';
}
```

Ustuvorlik tartibi muhim: muddati o'tgan dori birinchi o'rinda turadi, chunki uni sotish xavfli.

## 5. Xavfsizlik

- foydalanuvchi kiritgan matn HTML'ga chiqarishdan oldin `escapeHtml()` bilan tozalanadi;
- `innerHTML` faqat tizim shablonlari bilan ishlatiladi;
- tashqi skriptlar yuklanmaydi;
- `eval` va `document.write` ishlatilmaydi;
- ma'lumotlar serverga yuborilmaydi;
- JSON importida struktura tekshiriladi.

Cheklov: demo uchun autentifikatsiya va rolga asoslangan ruxsatlar yo'q. Ishlab chiqarish versiyasida API, sessiya, parol xeshi va audit talab qilinadi.

## 6. CI/CD

GitHub Actions har bir push va Pull Request'da:

1. `scripts/check_app.py` orqali HTML strukturasini tekshiradi;
2. inline JavaScript'ni ajratib oladi va `node --check` bilan sintaksisini tekshiradi;
3. `index.html`ni artefakt sifatida saqlaydi.

GitHub Pages `main` branch'ining ildizidan statik faylni chiqaradi. Alohida build bosqichi yo'q — bu bir faylli ilovaning asosiy afzalligi.

## 7. Kengaytirish yo'nalishlari

1. `data` qatlamini API bilan almashtirish va `localStorage`ni kesh sifatida qoldirish.
2. Dorilar va harakatlar uchun serverni tomonlama validatsiya.
3. Foydalanuvchi rollari: administrator, mudir, sotuvchi.
4. PostgreSQL sxemasi va migratsiyalar.
5. Shtrix-kod skaneri.
6. Talabni prognozlash uchun MLOps pipeline.
7. Telegram bot orqali muddat ogohlantirishlari.

## 8. Repository havolalari

- Repozitoriy: <https://github.com/ogiloymuradova1679-rgb/dorixona-boshqaruv-tizimi>
- CI: <https://github.com/ogiloymuradova1679-rgb/dorixona-boshqaruv-tizimi/actions>
- Demo: <https://ogiloymuradova1679-rgb.github.io/dorixona-boshqaruv-tizimi/>

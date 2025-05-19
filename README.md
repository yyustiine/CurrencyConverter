# CurrencyConverter

>[!TIP]
>Kods ir paredzēts izpildei ar **Python** un **HTML**, izmantojot **Flask** tīmekļa ietvaru.

> [!NOTE]
> Nepieciešams ielādēt šādas bibliotēkas un rīkus:
>
> 📦flask
> 
> 🌐requests
> 
> 📊matplotlib
> 
> Ielādēt var ar komandu: `pip install -r requirements.txt`

---

## Projekta Autori 👤
- Luthiena Džemre Akčinara, 3. grupa | 241RDB111
- Justīne Pavārniece, 15. grupa | 241RDC039

## Projekta Pamatmērķi un Uzdevumi 🎯

Šī projekta mērķis ir izveidot tīmekļa lietotni, kas ļauj lietotājam:

1. 🔢 **Veikt valūtu konvertēšanu:** Izmantojot API, lietotājs var konvertēt jebkuru summu starp populārākajām valūtām.
2. 🌍 **Apskatīt 10 populārāko valūtu kursus pasaulē:** Balstoties uz izvēlēto galveno valūtu, tiek parādīts aktuālais kurss pret pārējām.
3. 📈 **Redzēt vēsturisko kursa izmaiņu grafiku:** Tiek ģenerēts grafiks ar izvēlētās valūtas attiecību pret USD pēdējā gada laikā.

---

## Uzdevumu padziļinātais skaidrojums 🧩
🔁`Valūtu kursu konversija`: Lietotājs ievada summu un izvēlas sākotnējo un mērķa valūtu. Izmantojot Flask izsauc FreeCurrencyAPI, tiek iegūts aktuālais kurss, aprēķināts rezultāts un izvadīts lietotājam.
🌐`Populārāko valūtu saraksts`: Lietotājs var apskatīt 10 populārākās pasaules valūtas pēc izvēlētās galvenās valūtas, un sistēma atgriež aktuālos kursus pret pārējām top 10 valūtām, izņemot pašu galveno valūtu. Informācija tiek attēlota sarakstā.
📊`Kursa izmaiņu grafiks`: Ar matplotlib palīdzību tiek uzzīmēts vēsturisks valūtas kurss pret USD, pamēnešiem viena gada laika periodā. Grafiks tiek automātiski saglabāts kā attēls `static/chart.png`. Grafiks tiek attēlots zem top 10 konversijas rezultātiem.

---

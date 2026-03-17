# IT Helpdesk Analizi

Bu proje, IT destek  taleplerini analiz etmek ve SLA (Service Level Agreement) ihlallerini incelemek amacıyla Python ve Power BI kullanılarak geliştirilmiştir.

## 🎯 Projenin Amacı
- IT destek taleplerinin analiz edilmesi
- SLA ihlallerinin (breach) tespit edilmesi
- Ticket (talep) yoğunluğunun incelenmesi
- Verilerin görselleştirilmesi

## ⚙️ Yapılan İşlemler

### 1. Veri Oluşturma
- Python kullanılarak örnek IT helpdesk verisi üretildi
- Farklı kategoriler: Hardware, Software, Network, Security
- Öncelik seviyeleri: Low, Medium, High

### 2. Veri Temizleme
- Eksik ve hatalı veriler düzenlendi
- Analize uygun hale getirildi

### 3. Veri Analizi
- Toplam ticket sayısı hesaplandı
- SLA breach (ihlal) sayısı bulundu
- SLA breach rate (%) hesaplandı
- Aylara göre trend analizi yapıldı

### 4. Power BI Dashboard
Dashboard içerisinde:
- Toplam ticket sayısı
- SLA breach sayısı
- SLA breach oranı (%)
- Aylık trend grafiği
- Kategori ve önceliğe göre filtreleme

## 📁 Proje Dosyaları
- `analysis.py` → Veri analizi işlemleri
- `generate_dataset.py` → Veri oluşturma scripti
- `it_tickets.csv` → Ham veri
- `it_tickets_cleaned.csv` → Temizlenmiş veri
- `it_helpdesk_analysis.pbix` → Power BI dashboard

## 🛠️ Kullanılan Teknolojiler
- Python
- Pandas
- Power BI

## 📊 Sonuç
Bu proje ile IT destek süreçlerinde SLA performansı analiz edilmiş ve veriler görselleştirilerek daha anlaşılır hale getirilmiştir.

# 🎵 Windows için Android Ses Kontrolü

**🌍 Türkçe | [English](README.md)**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)
[![ADB](https://img.shields.io/badge/Requires-ADB-green.svg)](https://developer.android.com/studio/command-line/adb)

> 🚀 **Android cihazınızın ses seviyesini Windows Ses Karıştırıcısından doğrudan kontrol edin!**

Windows PC'nizi Android cihazınızın ses sistemi için uzaktan kumandaya dönüştürün. Bu yenilikçi uygulama, Windows Ses Karıştırıcısı ile Android cihazınız arasında kusursuz entegrasyon sağlayarak telefonunuza dokunmadan ses seviyesi ve sessiz ayarlarını yapmanıza olanak tanır.

## ✨ Özellikler

- 🎛️ **Windows Ses Karıştırıcısı Entegrasyonu** - Android ses seviyesini Windows'un yerel arayüzünden kontrol edin
- 🔊 **Gerçek Zamanlı Ses Senkronizasyonu** - Sıfır gecikme ile anlık ses değişiklikleri
- 🔇 **Sessiz/Sesli Desteği** - Windows'tan tam sessiz kontrolü
- 📱 **Çoklu Cihaz Desteği** - Bağlı Android cihazları otomatik olarak algılar
- 🛡️ **Güçlü Hata Yönetimi** - Bağlantı sorunlarının zarif bir şekilde ele alınması
- 🔄 **Otomatik Yeniden Bağlanma** - Geçici bağlantı kesintilerinden akıllı kurtarma
- 💾 **Bellek Verimli** - Minimum sistem kaynak kullanımı
- 🎯 **Hassas Kontrol** - Tam aralık ses kontrolü (%0-100)

## 🎯 Nasıl Çalışır

1. **🔌 Cihaz Bağlantısı**: ADB aracılığıyla Android cihazınıza bağlanır (USB Hata Ayıklama)
2. **🎵 Ses Kaydı**: Windows Ses Karıştırıcısında sanal bir ses oturumu oluşturur
3. **🔄 Gerçek Zamanlı Senkronizasyon**: Windows ses değişikliklerini izler ve Android'e uygular
4. **📊 Akıllı Eşleme**: Windows ses aralığını Android'in yerel aralığına akıllıca eşler

## 📋 Gereksinimler

### Sistem Gereksinimleri

- 🖥️ **İşletim Sistemi**: Windows 10/11
- 🐍 **Python**: 3.7 veya üzeri
- 📱 **Android Cihaz**: USB Hata Ayıklama etkinleştirilmiş Android 5.0+

### Gerekli Araçlar

- **Android SDK Platform Tools** (ADB için)
- **Python Kütüphaneleri**: `pycaw` (otomatik olarak yüklenir)

## 🚀 Hızlı Başlangıç

### 1. 📥 Kurulum

```bash
# Repoyu klonlayın
git clone https://github.com/y4kupkaya/android-volume-controller.git
cd android-volume-controller

# Python bağımlılıklarını yükleyin
pip install pycaw
```

### 2. 🔧 Android Cihaz Kurulumu

1. **Geliştirici Seçeneklerini Etkinleştirin**:
   - `Ayarlar` → `Telefon Hakkında` bölümüne gidin
   - `Yapı Numarası`na 7 kez dokunun

2. **USB Hata Ayıklamayı Etkinleştirin**:
   - `Ayarlar` → `Geliştirici Seçenekleri` bölümüne gidin
   - `USB Hata Ayıklama`yı etkinleştirin

3. **Cihazı Bağlayın**:
   - USB kablosu ile bağlayın
   - İstendiğinde USB hata ayıklamaya izin verin

### 3. 🛠️ ADB Kurulumu (Android Debug Bridge)

**Seçenek A: Android Studio (Önerilen)**

```bash
# Android Studio'yu indirin ve SDK Platform Tools'u kurun
# PATH'e ekleyin: C:\Users\KullaniciAdi\AppData\Local\Android\Sdk\platform-tools
```

**Seçenek B: Bağımsız ADB**

```bash
# Google'dan platform-tools'u indirin
# Çıkarın ve Windows PATH'ine ekleyin
```

**Kurulumu Doğrulayın**:

```bash
adb devices
# Bağlı cihazınızı göstermeli
```

### 4. ▶️ Uygulamayı Çalıştırın

```bash
python android_volume_controller.py
```

### 5. 🎛️ Ses Kontrolü

1. **Windows Ses Karıştırıcısını Açın**:
   - Sistem tepsisindeki hoparlör simgesine sağ tıklayın
   - "Ses karıştırıcısını aç"ı seçin

2. **Python Uygulamasını Bulun**:
   - Ses karıştırıcısında "Python"u arayın

3. **Android'inizi Kontrol Edin**:
   - 🔊 Android ses seviyesini değiştirmek için kaydırıcıyı ayarlayın
   - 🔇 Android cihazı sessize almak/açmak için sessiz düğmesine tıklayın

## 🎮 Kullanım Örnekleri

### Temel Ses Kontrolü

```python
# Uygulama başlatıldıktan sonra otomatik olarak çalışır
# Android cihazınızı kontrol etmek için sadece Windows Ses Karıştırıcısını kullanın
```

### Uygulamayı Çalıştırma

```bash
# Ses kontrolcüsünü başlat
python android_volume_controller.py
```

## 🔧 Yapılandırma

Uygulama çoğu ayarı otomatik olarak algılar ve yapılandırır, ancak şunları özelleştirebilirsiniz:

- **Ses Aralığı Eşlemesi**: Cihazınızın ses aralığına otomatik olarak uyum sağlar
- **Bağlantı Zaman Aşımı**: Bağlantı sorunları için akıllı yeniden deneme mekanizması
- **Ses Kalitesi**: Minimum gecikme için optimize edilmiş

## 📱 Desteklenen Cihazlar

✅ **Test Edilmiş ve Uyumlu**:

- Samsung Galaxy serisi
- Google Pixel serisi
- OnePlus cihazları
- Xiaomi/MIUI cihazları
- Çoğu Android 5.0+ cihaz

⚠️ **Bilinen Sınırlamalar**:

- Bazı özel ROM'lar ek izinler gerektirebilir
- Ağır şekilde değiştirilmiş ses sistemlerine sahip cihazlar manuel yapılandırma gerektirebilir

## 🐛 Sorun Giderme

### Yaygın Sorunlar

**🔴 "Android cihaz bulunamadı"**

```bash
# Cihaz bağlantısını kontrol edin
adb devices

# USB hata ayıklamanın etkin olduğundan emin olun
# Farklı USB kablosu/portu deneyin
```

**🔴 "ADB bulunamadı"**

```bash
# Android SDK Platform Tools'u kurun
# ADB'yi Windows PATH'ine ekleyin
# Komut istemini yeniden başlatın
```

**🔴 "Ses oturumu bulunamadı"**

- Windows'un ses oturumunu kaydetmesi için birkaç saniye bekleyin
- Windows Ses Karıştırıcısını manuel olarak kontrol edin
- Uygulamayı yeniden başlatın

**🔴 "İzin reddedildi"**

- Android cihazda USB hata ayıklamayı yeniden yetkilendirin
- USB bağlantı modunu kontrol edin ("Dosya Aktarımı" veya "PTP" olmalı)

### Hata Ayıklama Modu

```bash
# Ayrıntılı günlükleme ile çalıştır
python android_volume_controller.py --debug
```

## 🛡️ Güvenlik ve Gizlilik

- 🔒 **Sadece Yerel Bağlantı**: Tüm iletişim USB aracılığıyla yerel olarak gerçekleşir
- 🚫 **İnternet Gerekmez**: İnternet üzerinden veri iletimi yoktur
- 🔐 **Minimum İzinler**: Sadece USB hata ayıklama erişimi gerektirir
- 📊 **Veri Toplama Yok**: Kullanıcı verisi toplanmaz veya saklanmaz

## 🤝 Katkıda Bulunma

Katkılarınızı memnuniyetle karşılıyoruz! Nasıl yardımcı olabileceğiniz:

1. 🍴 **Repoyu Fork Edin**
2. 🌟 **Özellik Dalı Oluşturun** (`git checkout -b feature/harika-ozellik`)
3. 💻 **Değişikliklerinizi Yapın**
4. 🧪 **Kapsamlı Test Edin**
5. 📝 **Değişiklikleri Commit Edin** (`git commit -m 'Harika özellik ekle'`)
6. 🚀 **Dalı Push Edin** (`git push origin feature/harika-ozellik`)
7. 🎯 **Pull Request Açın**

### Geliştirme Kurulumu

```bash
# Geliştirme için klonlayın
git clone https://github.com/y4kupkaya/android-volume-controller.git
cd android-volume-controller

# Geliştirme bağımlılıklarını yükleyin
pip install -r requirements-dev.txt

# Testleri çalıştırın
python -m pytest tests/
```

## 📄 Lisans

Bu proje **GNU General Public License v3.0** altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

```
Copyright (C) 2025 Yakup Kaya (y4kupkaya@github)

Bu program özgür yazılımdır: Free Software Foundation tarafından yayınlanan
GNU Genel Kamu Lisansı'nın 3. sürümü veya (tercihinize bağlı olarak)
daha sonraki herhangi bir sürümü şartları altında yeniden dağıtabilir
ve/veya değiştirebilirsiniz.
```

## 👨‍💻 Yazar

**Yakup Kaya**

- 🌐 Website: [yakupkaya.me](https://yakupkaya.me)
- 📧 GitHub: [@y4kupkaya](https://github.com/y4kupkaya)
- 💼 LinkedIn: [Benimle bağlantı kurun](https://linkedin.com/in/y4kupkaya)

## 🙏 Teşekkürler

- 📚 **pycaw kütüphanesi** - Windows ses sistemi entegrasyonu
- 🤖 **Android Debug Bridge** - Android cihaz iletişimi
- 🎵 **Windows Audio Session API** - Ses karıştırıcısı entegrasyonu
- 🌟 **Açık Kaynak Topluluğu** - İlham ve destek

## 🔮 Yol Haritası

- [ ] 🎚️ **Bireysel Uygulama Kontrolü** - Android'de belirli uygulama seslerini kontrol etme
- [ ] 🔊 **Ses Profili Yönetimi** - Özel ses profillerini kaydetme ve yükleme
- [ ] 📡 **Kablosuz Destek** - WiFi ağı üzerinden kontrol
- [ ] 🎯 **GUI Arayüzü** - Kullanıcı dostu grafik arayüzü
- [ ] 📱 **iOS Desteği** - iOS cihazlarına destek genişletme
- [ ] 🔄 **Çift Yönlü Senkronizasyon** - Android değişikliklerini Windows'a geri senkronize etme

## ⭐ Yıldız Geçmişi

Bu projeyi faydalı buluyorsanız, lütfen yıldız vermeyi düşünün! ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=y4kupkaya/android-volume-controller&type=Date)](https://star-history.com/#y4kupkaya/android-volume-controller&Date)

---

<div align="center">

**❤️ ile [Yakup Kaya](https://yakupkaya.me) tarafından yapıldı**

</div>
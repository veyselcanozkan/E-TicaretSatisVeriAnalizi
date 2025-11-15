#  E-Ticaret Satış Veri Analizi

Bu proje, bir e-ticaret sitesine ait (kurgusal veya gerçek) bir satış veri setini analiz ederek şirketin satış performansını, popüler ürünlerini ve bölgesel dağılımını anlamayı amaçlamaktadır.

Bu analizle birlikte yönetime "hangi ürünlere odaklanmalı" ve "hangi şehirlerde pazarlama artırılmalı" gibi konularda içgörüler sunulması hedeflenmektedir.

---

##  Kullanılan Kütüphaneler

Proje, veri analizi ve görselleştirme için aşağıdaki temel Python kütüphanelerini kullanmaktadır:

* **Pandas:** Veri yükleme, temizleme ve hazırlık işlemleri için.
* **Numpy:** Keşifsel veri analizi (EDA) sırasında sayısal hesaplamalar için.
* **Matplotlib:** Analiz sonuçlarını görselleştirmek için.

---

##  Proje Aşamaları

Proje dört ana aşamadan oluşmaktadır:

1.  **Veri Yükleme ve Hazırlık:** Veri setinin Pandas DataFrame'e yüklenmesi, eksik verilerin (varsa) ele alınması ve veri tiplerinin düzeltilmesi.
2.  **Keşifsel Veri Analizi (EDA):** Veri setinin temel istatistiklerinin çıkarılması, en çok satan ürünlerin, en çok satış yapılan şehirlerin ve zaman içindeki satış trendlerinin incelenmesi.
3.  **Veri Görselleştirme:** EDA sırasında elde edilen bulguların Matplotlib kütüphanesi kullanılarak grafiklere (çubuk grafikler, çizgi grafikler vb.) dökülmesi.
4.  **Raporlama:** Elde edilen içgörülerin ve sonuçların özetlenmesi.

---

##  Veri Seti

Bu analizde kullanılan veri seti Kaggle'dan temin edilmiştir. Aşağıdaki bağlantıdan erişebilirsiniz:

* [Kaggle: E-Commerce Sales Dataset](https://www.kaggle.com/datasets/berkayalan/ecommerce-sales-dataset)

---

##  Kurulum ve Çalıştırma

1.  Bu depoyu klonlayın:
    ```bash
    git clone [https://github.com/veyselcanozkan/E-TicaretSatisVeriAnalizi.git](https://github.com/veyselcanozkan/E-TicaretSatisVeriAnalizi.git)
    cd E-TicaretSatisVeriAnalizi
    ```

2.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

3.  Analizi içeren `.ipynb` (Jupyter Notebook) veya `.py` (Python) dosyasını çalıştırın.

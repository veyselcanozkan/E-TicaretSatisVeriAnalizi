import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


basket_df = pd.read_csv("basket.csv")
customer_df = pd.read_csv("customer.csv")

print(" Basket Detayları (İlk 5 Satır):")
print(basket_df.head(), "\n")

print(" Müşteri Detayları (İlk 5 Satır):")
print(customer_df.head(), "\n")

print("Basket veri boyutu:", basket_df.shape)
print("Customer veri boyutu:", customer_df.shape)
print("\n") 

print("=== Basket Details Genel Bilgiler ===")
print(basket_df.info(), "\n")

print("=== Customer Details Genel Bilgiler ===")
print(customer_df.info(), "\n")

print("=== Eksik Değerler ===")
print("Basket:", basket_df.isnull().sum())
print("Customer:", customer_df.isnull().sum(), "\n")

print("=== Basket Detayları İstatistikleri ===")
print(basket_df.describe(include='all'), "\n")

print("=== Customer Detayları İstatistikleri ===")
print(customer_df.describe(include='all'), "\n") 

print("Eşsiz müşteri sayısı:", customer_df['customer_id'].nunique())
if 'product_id' in basket_df.columns:
    print("Eşsiz ürün sayısı:", basket_df['product_id'].nunique())
else:
    print("product_id sütunu yok")


top_products = basket_df.groupby('product_id')['basket_count'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
top_products.plot(kind='bar', color='skyblue')
plt.title("En Çok Satan 10 Ürün")
plt.xlabel("Product ID")
plt.ylabel("Toplam Satış Adedi")
plt.xticks(rotation=45)
plt.show()


logical_age_df = customer_df[
    (customer_df['customer_age'] >= 10) & 
    (customer_df['customer_age'] <= 100)
]

outlier_count = len(customer_df) - len(logical_age_df)
print(f"\nYaş dağılımı grafiği için {outlier_count} adet mantıksız yaş kaydı (10 dışı veya 100+) filtrelendi.")

plt.figure(figsize=(10,6))

plt.hist(logical_age_df['customer_age'], bins=15, color='salmon', edgecolor='black')
plt.title("Müşteri Yaş Dağılımı (Mantıklı Aralık: 10-100 Yaş)")
plt.xlabel("Yaş")
plt.ylabel("Müşteri Sayısı")
plt.show()

sex_counts = customer_df['sex'].value_counts()

plt.figure(figsize=(6,6))
sex_counts.plot(kind='pie', autopct='%1.1f%%', colors=['lightblue','pink'])
plt.title("Müşteri Cinsiyet Dağılımı")
plt.ylabel("") 
plt.show()

if 'basket_date' in basket_df.columns:
    basket_df['basket_date'] = pd.to_datetime(basket_df['basket_date'])
    daily_sales = basket_df.groupby('basket_date')['basket_count'].sum()

    plt.figure(figsize=(12,6))
    daily_sales.plot(kind='line', color='green')
    plt.title("Günlük Satış Dağılımı")
    plt.xlabel("Tarih")
    plt.ylabel("Satış Adedi")
    plt.show()

print("\n=== RAPOR ===\n")

total_sales = basket_df['basket_count'].sum()
print(f"Toplam Satış Adedi: {total_sales}")

top5_products = basket_df.groupby('product_id')['basket_count'].sum().sort_values(ascending=False).head(5)
print("\nEn Çok Satan 5 Ürün:")
print(top5_products)

print("\nMüşteri Yaş Dağılımı (Ham Veri - Özet):")
print(customer_df['customer_age'].describe())


if 'logical_age_df' in locals():
    print("\nMüşteri Yaş Dağılımı (Mantıklı Aralık 10-100 Yaş - Özet):")
    print(logical_age_df['customer_age'].describe())

sex_counts = customer_df['sex'].value_counts()
print("\nMüşteri Cinsiyet Dağılımı:")
print(sex_counts)

if 'basket_date' in basket_df.columns:
    daily_sales = basket_df.groupby('basket_date')['basket_count'].sum()
    print("\nSon 5 Günlük Satış Trendleri:")
    print(daily_sales.tail())

summary_df = pd.DataFrame({
    'Top 5 Ürün': top5_products.index,
    'Top 5 Ürün Satış Adedi': top5_products.values
})

try:
    summary_df.to_excel("rapor.xlsx", index=False)
    print("\nRapor Excel dosyasına kaydedildi: rapor.xlsx")
except Exception as e:
    print(f"\nExcel dosyası kaydedilirken hata oluştu: {e}")
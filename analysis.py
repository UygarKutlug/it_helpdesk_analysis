import pandas as pd


df = pd.read_csv("it_tickets.csv")

print("Ortalama Çözüm Süresi:")
print(df["Resolution_Hours"].mean())

print("\nÖncelik Dağılımı:")
print(df["Priority"].value_counts())


df["SLA_Breach"] = df["Resolution_Hours"] > df["SLA_Hours"]


breach_count = df["SLA_Breach"].sum()


breach_rate = breach_count / len(df) * 100

print("\nToplam SLA İhlali:")
print(breach_count)

print("\nSLA İhlal Oranı (%):")
print(round(breach_rate, 2))


team_breach = df.groupby("Assigned_Team")["SLA_Breach"].mean() * 100

print("\nEkip Bazlı SLA İhlal Oranı (%):")
print(round(team_breach, 2))



priority_breach = df.groupby("Priority")["SLA_Breach"].mean() * 100

print("\nPriority Bazlı SLA İhlal Oranı (%):")
print(round(priority_breach, 2))



category_breach = df.groupby("Category")["SLA_Breach"].mean() * 100

print("\nCategory Bazlı SLA İhlal Oranı (%):")
print(round(category_breach, 2))



df.to_csv("it_tickets_cleaned.csv", index=False)

print("\nTemiz veri export edildi!")

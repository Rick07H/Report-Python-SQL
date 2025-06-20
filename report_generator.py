#Realiza as importações das bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
from conncetDB import get_engine

#Abre e armazena o arquivo com a query em uma variável
with open("kpi_query.sql", "r") as file:
    query = file.read()

#Utiliza a conexão sql para acessar o banco e rodar a query
engine = get_engine()
df = pd.read_sql(query, engine)

#Monta um excel com os dados extraídos
df.to_excel("Outputs/report.xlsx", index=False)

plt.figure(figsize=(10, 6))

#Monta um gráfico que verifica os dados por turno
for turno in df["Turno"].unique():
    sub = df[df["Turno"] == turno]
    plt.bar(sub["Lote"] + f" ({turno})", sub["Total_Produzido"], label=f"Turno: {turno}")

#Montagem do Layout fo gráfico
plt.title("Produção por Lote e Turno")
plt.xlabel("Lote")
plt.ylabel("Total_Produzido")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.legend()

#Salva o gráfico em um arquivo .png
plt.savefig("outputs/chart.png")
plt.close()

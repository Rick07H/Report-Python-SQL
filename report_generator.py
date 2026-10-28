from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from connect_db import get_engine

OUTPUT_DIR = Path("Outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

# Read the query from its own file so it can be edited without touching Python
query = Path("kpi_query.sql").read_text(encoding="utf-8")

# Run the query against the database
engine = get_engine()
df = pd.read_sql(query, engine)

# Export the result to Excel
df.to_excel(OUTPUT_DIR / "report.xlsx", index=False)

# One group of bars per shift (Turno), one bar per batch (Lote)
plt.figure(figsize=(10, 6))
for turno in df["Turno"].unique():
    sub = df[df["Turno"] == turno]
    plt.bar(sub["Lote"] + f" ({turno})", sub["Total_Produzido"], label=f"Shift: {turno}")

plt.title("Production by Batch and Shift")
plt.xlabel("Batch")
plt.ylabel("Total produced")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.legend()

plt.savefig(OUTPUT_DIR / "chart.png")
plt.close()

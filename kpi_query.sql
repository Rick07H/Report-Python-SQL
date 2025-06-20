SELECT
	Lote
	,Turno
	,ROUND(SUM(CAST(Produzido AS FLOAT)), 1) AS Total_Produzido
	,ROUND(AVG(CAST(Eficiencia AS FLOAT)), 1) AS MediaEficiencia

FROM ProducaoSimulada

GROUP BY 
	Lote
	,Turno

ORDER BY Lote ,Turno ASC
-- Creates the sample table used by kpi_query.sql and fills it with fake data.
-- Run it once in an empty database (for example ReportDemo).
IF OBJECT_ID('dbo.ProducaoSimulada') IS NOT NULL DROP TABLE dbo.ProducaoSimulada;

CREATE TABLE dbo.ProducaoSimulada (
    Id         INT IDENTITY(1,1) PRIMARY KEY,
    Lote       VARCHAR(10)  NOT NULL,  -- batch
    Turno      VARCHAR(10)  NOT NULL,  -- shift
    Produzido  INT          NOT NULL,  -- units produced
    Eficiencia DECIMAL(5,2) NOT NULL   -- efficiency, in percent
);

-- 4 batches x 3 shifts x 5 readings, with random values
INSERT INTO dbo.ProducaoSimulada (Lote, Turno, Produzido, Eficiencia)
SELECT
    l.Lote,
    t.Turno,
    400 + ABS(CHECKSUM(NEWID())) % 300,
    80 + (ABS(CHECKSUM(NEWID())) % 1500) / 100.0
FROM (VALUES ('L001'), ('L002'), ('L003'), ('L004')) AS l(Lote)
CROSS JOIN (VALUES ('Morning'), ('Afternoon'), ('Night')) AS t(Turno)
CROSS JOIN (VALUES (1), (2), (3), (4), (5)) AS n(n);

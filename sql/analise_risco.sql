USE banco_risco;

SELECT 
    loan_intent AS motivo_emprestimo,
    person_home_ownership AS tipo_moradia,
    CASE 
        WHEN person_age < 25 THEN '18-24 anos'
        WHEN person_age <= 35 THEN '25-35 anos'
        WHEN person_age <= 50 THEN '36-50 anos'
        ELSE 'Mais de 50 anos'
    END AS faixa_etaria,
    COUNT(*) AS total_pedidos,
    ROUND(AVG(loan_status) * 100, 2) AS taxa_inadimplencia_porcento,
    ROUND(SUM(CASE WHEN loan_status = 1 THEN loan_amnt ELSE 0 END), 2) AS valor_total_inadimplente,
    ROUND(AVG(loan_amnt), 2) AS ticket_medio_emprestimo
FROM credit_risk_dataset
WHERE person_age <= 80
GROUP BY loan_intent, person_home_ownership, faixa_etaria
ORDER BY valor_total_inadimplente DESC;

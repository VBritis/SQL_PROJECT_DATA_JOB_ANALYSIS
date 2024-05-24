/*
SELECT '2023-02-19':: DATE,
       '123':: INTEGER,
       'true':: BOOLEAN,
        '3.14':: FLOAT;
*/

/*SELECT
    job_title_short,
    salary_year_avg,
    CASE
        WHEN salary_year_avg > 100000.0 THEN 'High'
        WHEN salary_year_avg BETWEEN 70000.0 AND 100000.0 THEN 'Standart'
        WHEN salary_year_avg BETWEEN 0 AND 70000.0 THEN 'Low'
        ELSE 'Null'
    END AS "Salary conditions"
FROM    
    job_postings_fact

WHERE
    job_title_short = 'Data Analyst' AND salary_year_avg IS NOT NULL
ORDER BY
    salary_year_avg DESC
*/


-- SubQuery
/*
SELECT *
FROM(
    SELECT*
    FROM job_postings_fact
    WHERE EXTRACT(MONTH FROM job_posted_date) = 1
)AS january_jobs;
*/



-- CTE, Common Table Expressions
/*
WITH january_jobs AS(
    SELECT *   
    FROM job_postings_fact
    WHERE EXTRACT(MONTH FROM job_posted_date) = 1
)
SELECT *
FROM january_jobs*/





/*
SELECT 
    company_id,
    name AS company_name
FROM 
    company_dim
WHERE company_id IN (
    SELECT 
            company_id
    FROM    
            job_postings_fact
    WHERE
            job_no_degree_mention = true
    ORDER BY
            company_id
)*/






/* IMPORTANTE ! ! ! ! ! ! ! ! ! ! ! ! ! !
! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! 
! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !




--Cria uma consulta temporária para ser utilizada mais a frente

WITH company_job_count AS ( -- Atribuição do nome da consulta temporária
    SELECT
        company_id, --Indentificador KEY para fazer o left join
        COUNT(*) AS total_jobs --Contador de empregos disponiveis, nomeado para ser chamado mais a frente
    FROM
        job_postings_fact
    GROUP BY
        company_id
)

SELECT
    company_dim.name AS company_name, -- . pois foi feito um join
    company_job_count.total_jobs -- chamada da consulta feita lá atrás para efetuar a contagem de empregos por nome de empresa
FROM
    company_dim
LEFT JOIN company_job_count ON company_job_count.company_id = company_dim.company_id -- Utiliza a KEY como dito encima para fazer um LeftJoin
ORDER BY
    total_jobs DESC
*/


/*
WITH remote_job_skills AS(
    SELECT
        skill_id,
        COUNT(*) AS skill_count
    FROM
        skills_job_dim AS skills_job 
    INNER JOIN job_postings_fact AS job_postings ON job_postings.job_id = skills_job.job_id
    WHERE
        job_postings.job_work_from_home = True AND
        job_postings.job_title_short = 'Data Scientist'
    GROUP BY 
        skill_id
)

SELECT 
    skills.skill_id,
    skills AS skill_name,
    skill_count
FROM remote_job_skills
INNER JOIN skills_dim AS skills ON skills.skill_id = remote_job_skills.skill_id 
ORDER BY 
    skill_count DESC
LIMIT 5
*/


--Union
/*
SELECT * FROM(
SELECT*
FROM jan_jobsi
UNION  
SELECT*
FROM feb_jobsi
UNION
SELECT*  
FROM march_jobs) AS first_quarter
*/
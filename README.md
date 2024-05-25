# Introduction
    🌌 This project focuses on analyzing job market data using SQL to uncover trends, identify top-paying jobs, and understand skill demands focus in data scientist rules! The SQL scripts provided facilitate detailed analysis to extract valuable insights from job market data.

    🔎 SQL queries? Check them out here: [sql_project folder](/project_sql/)
    📊 Graphics? Check out here: [graphics folder](/visualization/)

# Background
   🌠 The job market dataset includes various attributes such as job titles, companies, locations, salaries, and job descriptions. The primary objective is to use SQL to clean, process, and analyze this data to understand job trends and salary distributions.

# Tools I Used
-  **SQL**: For querying and analyzing data.
- **PostgreSQL**: As the database management system.
- **GIT and GITHUB**: For upload and create a repositor.
- **Excel**: For initial data exploration and preprocessing.
    
    
    
# The Analysis
The project_sql directory contains the following SQL scripts:

### 1_top_paying_jobs.sql: Identifies the top-paying jobs.

This script reveals which job titles offer the highest average salaries. For example, "Staff Data Scientist/Quant Researcher" and "Staff Data Scientist - Business Analytics" at Selby Jennings offer the highest average annual salaries, indicating that specialized data science roles in quantitative research and business analytics are highly lucrative.


```sql
SELECT 
    job_id,
    job_title,
    job_location,
    job_schedule_type,
    salary_year_avg,
    job_posted_date,
    name AS company_name
FROM  job_postings_fact
LEFT JOIN company_dim ON job_postings_fact.company_id = company_dim.company_id
WHERE
    job_location = 'Anywhere' AND
    job_title_short = 'Data Scientist' AND
    salary_year_avg IS NOT NULL
ORDER BY 
    salary_year_avg DESC
LIMIT 10;
```
Here the breakdown of the top data scientists jobs in 2023:

- **Specialization Matters** - Roles like "Staff Data Scientist/Quant Researcher" and "Head of Battery Data Science" indicate a focus on specific domains or industries. This specialization often commands higher salaries due to the expertise required and the value they bring to the organization.

- **Leadership Positions** - Roles such as "Head of Data Science" and "Director Level - Product Management - Data Science" show that leadership positions in data science can lead to higher compensation. These roles often involve not just technical skills but also strategic decision-making and team management responsibilities.

- **Company Size and Reputation** - Companies like Walmart, Reddit, and Demandbase are well-known and likely have substantial resources to invest in data science. Positions in such companies may offer higher salaries compared to smaller or less established companies.

![Top Paying Roles](assets\1_query.png)
*Bar graph visualizing the top 10 data jobs*


### 2_top_paying_job_skills.sql: Analyzes skills associated with top-paying jobs.

 By identifying skills linked to the highest-paying jobs, this analysis helps professionals focus on acquiring the most financially rewarding skills. Skills relevant to high-paying roles such as those at Selby Jennings and Algo Capital Group are particularly valuable.

```sql
WITH top_paying_jobs AS(
SELECT 
    job_id,
    job_title,
    job_location,
    job_schedule_type,
    salary_year_avg,
    job_posted_date,
    name AS company_name
FROM  job_postings_fact
LEFT JOIN company_dim ON job_postings_fact.company_id = company_dim.company_id
WHERE
    job_location = 'Anywhere' AND
    job_title_short = 'Data Scientist' AND
    salary_year_avg IS NOT NULL
ORDER BY 
    salary_year_avg DESC
LIMIT 10
)

SELECT 
    top_paying_jobs.*,
    skills
FROM top_paying_jobs
INNER JOIN skills_job_dim ON top_paying_jobs.job_id = skills_job_dim.job_id
INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
ORDER BY
    salary_year_avg DESC
```





### 3_top_demanded_skills.sql: Finds the most demanded skills in the job market.

 This analysis highlights which skills are in the highest demand, guiding job seekers to develop these skills. For instance, skills in data science and analytics are highly demanded across various roles.

### 4_top_paying_skills.sql: Identifies top-paying skills.

 This script uncovers which skills command the highest salaries, allowing professionals to invest in skills that provide the best return on investment. Data science and analytics skills associated with high-paying jobs are particularly noteworthy.

### 5_optimal_skills.sql: Determines the optimal skills that balance demand and pay.

 This analysis identifies skills that are both highly demanded and well-compensated, providing a strategic focus for career development. Skills relevant to roles such as "Director of Data Science & Analytics" at Reddit and "Head of Data Science" at Demandbase are both in demand and well-paid.

# Conclusions
This project highlights the power of SQL in data analysis, offering valuable insights into job market trends and salary distributions. The SQL scripts provided can be reused and adapted for similar data analysis tasks.

# Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests with improvements or additional analyses.

# License
This project is licensed under the MIT License. See the LICENSE file for details.
# Introduction
🌌 This project focuses on analyzing job market data using SQL to uncover trends, identify top-paying data jobs in 2023, and understand skill demands focus in data scientist rules! The SQL scripts provided facilitate detailed analysis to extract valuable insights from job market data.

🔎 SQL queries? Check them out here: [queries folder](/project_sql/)

📊 Graphics? Check out here: [graphics folder](/visualization/)

# Background
🌠 The job market dataset includes various attributes such as job titles, companies, locations, salaries, and job descriptions. The primary objective is to use SQL to clean, process, and analyze this data to understand job trends and salary distributions.

# Tools I Used
-  **SQL**: For querying and analyzing data.
- **PostgreSQL**: As the database management system.
- **GIT and GITHUB**: For upload and create a repositor.
- **Python with Pandas and Matplotlib**: 
**Pandas**: This is essential for data manipulation and analysis, especially for handling large datasets, cleaning, and transforming data.
**Matplotlib**: Ideal for creating static, animated, and interactive visualizations in Python. It will help you create detailed charts and graphs to better present your analysis.
   
    
    
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

![Top Paying Roles](/assets/query.png)
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

Here the breakdown of the top data scientists job skills in 2023:

- **Proficiency in Programming Languages** - There is a strong demand for skills in languages such as SQL, Python, Java, and others like Pandas, Numpy, and Scikit-learn. This suggests that employers value candidates capable of efficiently manipulating and analyzing data in an automated manner.

- **Competencies in Platforms and Tools** - In addition to programming languages, skills in cloud computing platforms such as AWS, Azure, and GCP are also highly valued. This reflects the increasing adoption of cloud infrastructure for processing and analyzing data at scale.

- **Specialization in Specific Domains** - Some positions require specific knowledge, such as the Director of Data Science with skills in Pandas and Numpy, indicating a need for professionals specialized in data analysis within a particular context, such as data science applied to specific products or services. This highlights the importance of specialization in certain domains for more advanced and well-paying positions.

![Top Paying Skills](/assets/2_query.png)
*Bar graph visualizing the top 30 skills*
### 3_top_demanded_skills.sql: Finds the most demanded skills in the job market.

 This analysis highlights which skills are in the highest demand, guiding job seekers to develop these skills. For instance, skills in data science and analytics are highly demanded across various roles.



``` sql
SELECT skills,
    COUNT(skills_job_dim.job_id) AS demand_count
FROM job_postings_fact
INNER JOIN skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
WHERE
    job_title_short = 'Data Scientist' AND
    job_work_from_home = TRUE
GROUP BY
    skills
ORDER BY
    demand_count DESC
LIMIT 5
```

Here the breakdown of the top demanded skills for data scientists in 2023:


- **Python Dominance**: Python stands out as the most in-demand skill for data scientists, with a significantly higher demand count compared to other skills. Its versatility, ease of use, and extensive libraries for data analysis, machine learning, and visualization contribute to its popularity.

- **SQL Proficiency**: SQL (Structured Query Language) remains a crucial skill for data scientists, with a substantial demand count. Proficiency in SQL is essential for managing and querying databases, which are often a primary source of data for data science projects.

- **Emerging Technologies**: Skills like AWS (Amazon Web Services) indicate a growing demand for cloud computing expertise among data scientists. As more organizations adopt cloud-based solutions for data storage, processing, and deployment, familiarity with platforms like AWS becomes increasingly valuable for data scientists.

These insights highlight the importance of a diverse skill set for data scientists, encompassing programming languages, data querying and manipulation, and knowledge of emerging technologies like cloud computing.

![Top 5 demanded skills](/assets/3_query.png)
*Bar graph visualizing the top 5 demanded skills*


### 4_top_paying_skills.sql: Identifies top-paying skills.

 This script uncovers which skills command the highest salaries, allowing professionals to invest in skills that provide the best return on investment. Data science and analytics skills associated with high-paying jobs are particularly noteworthy.


```sql
SELECT skills,
    ROUND(AVG(salary_year_avg),0) AS avg_salary
FROM job_postings_fact
INNER JOIN skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
WHERE
    job_title_short = 'Data Scientist' AND
    salary_year_avg IS NOT NULL AND
    job_work_from_home = TRUE
GROUP BY
    skills
ORDER BY
    avg_salary DESC
LIMIT 25
```


Here the breakdown of the top paying skills for data scientists in 2023:

- **High Salary Premium for Specialized Skills**: Skills like GDPR and Golang command the highest average salaries among data scientists, with average salaries of $217,738 and $208,750 respectively. This indicates a high demand for these specialized skills, likely due to their importance in data privacy (GDPR) and efficient back-end programming (Golang).

- **Emerging Technologies and Tools**: Skills such as Neo4j, MicroStrategy, and DynamoDB also offer high average salaries (around $170,000). This suggests that expertise in emerging and specialized technologies, especially those related to database management and business intelligence, are highly valued in the market.

- **Diverse Skill Set Demand**: The wide range of skills listed, from traditional programming languages like C ($164,865) and PHP ($168,125) to more niche tools like OpenCV ($172,500) and Tidyverse ($165,513), highlights the diverse skill set required for modern data scientists. It underscores the importance of versatility and the ability to work with different tools and technologies in the field.


![Top paying skills](/assets/4_query.png)
*Bar graph visualizing the top paying skills fro Data Scientist in 2023*


### 5_optimal_skills.sql: Determines the optimal skills that balance demand and pay.

 This analysis identifies skills that are both highly demanded and well-compensated, providing a strategic focus for career development. Skills relevant to roles such as "Director of Data Science & Analytics" at Reddit and "Head of Data Science" at Demandbase are both in demand and well-paid.




```sql
WITH skills_demand AS(
    SELECT
        skills_dim.skill_id, 
        skills_dim.skills,
        COUNT(skills_job_dim.job_id) AS demand_count
    FROM job_postings_fact
    INNER JOIN skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
    INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
    WHERE
        job_title_short = 'Data Scientist' AND
        job_work_from_home = TRUE AND
        salary_year_avg IS NOT NULL 
    GROUP BY
        skills_dim.skill_id
), avg_salary_skills AS(
    SELECT
        skills_job_dim.skill_id, 
        ROUND(AVG(salary_year_avg),0) AS avg_salary
    FROM job_postings_fact
    INNER JOIN skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
    INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
    WHERE
        job_title_short = 'Data Scientist' AND
        salary_year_avg IS NOT NULL AND
        job_work_from_home = TRUE
    GROUP BY
        skills_job_dim.skill_id
)

SELECT
    skills_demand.skill_id,
    skills_demand.skills,
    demand_count,
    avg_salary
FROM 
    skills_demand
INNER JOIN avg_salary_skills ON skills_demand.skill_id = avg_salary_skills.skill_id
ORDER BY
     avg_salary DESC,
    demand_count DESC
LIMIT 25
```


- **High Salary Doesn't Always Correlate with High Demand**:
Skills like GDPR and Golang are among the highest paying with average salaries of $217,738 and $208,750 respectively, but their demand counts are relatively low, with GDPR at 4 and Golang at 2. This suggests that while these skills are highly valued monetarily, they are not as widely required in the job market.

- **Broadly Required Skills with Moderate Salaries**:
Skills such as "C" and "Go" have high demand counts of 48 and 57 respectively, with average salaries of $164,865 and $164,691. This indicates that these skills are broadly required across various job roles, even though they do not command the highest salaries. Employers may be willing to pay moderately high salaries due to the widespread necessity of these skills.

- **Niche Skills with High Salaries**:
Several niche skills, such as "Atlassian" and "Microstrategy", have moderate demand counts (5 and 6 respectively) but command relatively high average salaries ($189,700 and $171,147). This indicates that while these skills are not in high demand, they are specialized enough to warrant higher pay when they are needed.





# Conclusions
This SQL-based data job analysis project successfully demonstrates the power of SQL in uncovering valuable insights from job market data. By analyzing trends, top-paying jobs, and in-demand skills, the project highlights key areas for career development in data science. The findings emphasize the importance of specific programming languages, cloud computing skills, and specialized domains in achieving high salaries and demand. This project serves as a robust framework for similar analyses, providing reusable SQL scripts for detailed job market investigations. Contributions and further enhancements are encouraged under the MIT License.
# Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests with improvements or additional analyses.

# License
MIT License


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
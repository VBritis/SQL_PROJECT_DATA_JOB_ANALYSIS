import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np




data = [
  { "salary_year_avg": "550000.0", "skills": "sql" },
  { "salary_year_avg": "550000.0", "skills": "python" },
  { "salary_year_avg": "525000.0", "skills": "sql" },
  { "salary_year_avg": "375000.0", "skills": "sql" },
  { "salary_year_avg": "375000.0", "skills": "python" },
  { "salary_year_avg": "375000.0", "skills": "java" },
  { "salary_year_avg": "375000.0", "skills": "cassandra" },
  { "salary_year_avg": "375000.0", "skills": "spark" },
  { "salary_year_avg": "375000.0", "skills": "hadoop" },
  { "salary_year_avg": "375000.0", "skills": "tableau" },
  { "salary_year_avg": "320000.0", "skills": "azure" },
  { "salary_year_avg": "320000.0", "skills": "aws" },
  { "salary_year_avg": "320000.0", "skills": "tensorflow" },
  { "salary_year_avg": "320000.0", "skills": "keras" },
  { "salary_year_avg": "320000.0", "skills": "pytorch" },
  { "salary_year_avg": "320000.0", "skills": "scikit-learn" },
  { "salary_year_avg": "320000.0", "skills": "datarobot" },
  { "salary_year_avg": "300000.0", "skills": "scala" },
  { "salary_year_avg": "300000.0", "skills": "java" },
  { "salary_year_avg": "300000.0", "skills": "spark" },
  { "salary_year_avg": "300000.0", "skills": "tensorflow" },
  { "salary_year_avg": "300000.0", "skills": "pytorch" },
  { "salary_year_avg": "300000.0", "skills": "kubernetes" },
  { "salary_year_avg": "300000.0", "skills": "python" },
  { "salary_year_avg": "300000.0", "skills": "aws" },
  { "salary_year_avg": "300000.0", "skills": "gcp" },
  { "salary_year_avg": "300000.0", "skills": "python" },
  { "salary_year_avg": "300000.0", "skills": "pandas" },
  { "salary_year_avg": "300000.0", "skills": "numpy" }
]

skills = [x["skills"] for x in data]
salaries = [float(x["salary_year_avg"]) for x in data]

plt.figure(figsize=(10,6))
plt.barh(skills, salaries, color='skyblue')
plt.xlabel('Avg Anual Salary  ($)')
plt.ylabel('Skills')
plt.title('Top 30 paying data jobs skills in 2023')
plt.gca().invert_yaxis() 
plt.tight_layout()

plt.show()
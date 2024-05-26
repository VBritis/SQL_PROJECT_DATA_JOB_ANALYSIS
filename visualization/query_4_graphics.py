import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt




data = [
  {
    "skills": "gdpr",
    "avg_salary": "217738"
  },
  {
    "skills": "golang",
    "avg_salary": "208750"
  },
  {
    "skills": "atlassian",
    "avg_salary": "189700"
  },
  {
    "skills": "selenium",
    "avg_salary": "180000"
  },
  {
    "skills": "opencv",
    "avg_salary": "172500"
  },
  {
    "skills": "neo4j",
    "avg_salary": "171655"
  },
  {
    "skills": "microstrategy",
    "avg_salary": "171147"
  },
  {
    "skills": "dynamodb",
    "avg_salary": "169670"
  },
  {
    "skills": "php",
    "avg_salary": "168125"
  },
  {
    "skills": "tidyverse",
    "avg_salary": "165513"
  },
  {
    "skills": "solidity",
    "avg_salary": "165000"
  },
  {
    "skills": "c",
    "avg_salary": "164865"
  },
  {
    "skills": "go",
    "avg_salary": "164691"
  },
  {
    "skills": "datarobot",
    "avg_salary": "164500"
  },
  {
    "skills": "qlik",
    "avg_salary": "164485"
  },
  {
    "skills": "redis",
    "avg_salary": "162500"
  },
  {
    "skills": "watson",
    "avg_salary": "161710"
  },
  {
    "skills": "rust",
    "avg_salary": "161250"
  },
  {
    "skills": "elixir",
    "avg_salary": "161250"
  },
  {
    "skills": "cassandra",
    "avg_salary": "160850"
  },
  {
    "skills": "looker",
    "avg_salary": "158715"
  },
  {
    "skills": "slack",
    "avg_salary": "158333"
  },
  {
    "skills": "terminal",
    "avg_salary": "157500"
  },
  {
    "skills": "airflow",
    "avg_salary": "157414"
  },
  {
    "skills": "julia",
    "avg_salary": "157244"
  }
]


skills = [x['skills']for x in data]
salaries = [float(x['avg_salary'])for x in data]

plt.figure(figsize=(10,6))
plt.barh(skills,salaries,color='skyblue')
plt.xlabel('Avg Salary')
plt.ylabel('Skills')
plt.title('Top paying skills for Data Scientist')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

data = [
  {
    "skills": "python",
    "demand_count": "10390"
  },
  {
    "skills": "sql",
    "demand_count": "7488"
  },
  {
    "skills": "r",
    "demand_count": "4674"
  },
  {
    "skills": "aws",
    "demand_count": "2593"
  },
  {
    "skills": "tableau",
    "demand_count": "2458"
  }
]

skills = [x['skills']for x in data]
demand = [float(x['demand_count'])for x in data]


plt.figure(figsize=(10,6))
plt.barh(skills,demand, color='skyblue')
plt.xlabel('Demand Count')
plt.ylabel('Skills')
plt.title('Top demanded skills')
plt.gca().invert_yaxis() 
plt.tight_layout()
plt.show()
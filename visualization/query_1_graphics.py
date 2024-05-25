import matplotlib.pyplot as plt

# Dados dos 10 empregos mais bem pagos
data = [
    {"job_title": "Staff Data Scientist/Quant Researcher", "salary_year_avg": 550000.0},
    {"job_title": "Staff Data Scientist - Business Analytics", "salary_year_avg": 525000.0},
    {"job_title": "Data Scientist", "salary_year_avg": 375000.0},
    {"job_title": "Head of Data Science", "salary_year_avg": 351500.0},
    {"job_title": "Head of Data Science", "salary_year_avg": 324000.0},
    {"job_title": "Director Level - Product Management - Data Science", "salary_year_avg": 320000.0},
    {"job_title": "Director of Data Science & Analytics", "salary_year_avg": 313000.0},
    {"job_title": "Distinguished Data Scientist", "salary_year_avg": 300000.0},
    {"job_title": "Head of Battery Data Science", "salary_year_avg": 300000.0},
    {"job_title": "Principal Data Scientist", "salary_year_avg": 300000.0}
]

# Extrair os títulos dos trabalhos e salários médios
job_titles = [job["job_title"] for job in data]
salaries = [job["salary_year_avg"] for job in data]

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))
plt.barh(job_titles, salaries, color='skyblue')
plt.xlabel('Avg Anual Salary ($)')
plt.ylabel('Job Names')
plt.title('Top 10 paying data jobs in 2023')
plt.gca().invert_yaxis()  # Inverter a ordem dos trabalhos para mostrar o mais bem pago no topo
plt.tight_layout()

# Exibe o gráfico
plt.show()

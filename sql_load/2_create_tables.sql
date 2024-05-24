-- Create company_dim table with primary key
INSERT INTO company_dim (company_id, name, link, link_google, thumbnail)
VALUES (
    company_id:integer INSERT INTO job_applied (
        job_id,
        application_sent_date,
        custom_resume,
        resume_file_name,
        cover_letter_sent,
        cover_letter_file_name,
        status,
        contact_name
      )
    VALUES (
        job_id:integer INSERT INTO job_postings_fact (
            job_id,
            company_id,
            job_title_short,
            job_title,
            job_location,
            job_via,
            job_schedule_type,
            job_work_from_home,
            search_location,
            job_posted_date,
            job_no_degree_mention,
            job_health_insurance,
            job_country,
            salary_rate,
            salary_year_avg,
            salary_hour_avg
          )
        VALUES (
            job_id:integer,
            company_id:integer,
            'job_title_short:character varying',
            'job_title:text',
            'job_location:text',
            'job_via:text',
            'job_schedule_type:text',
            job_work_from_home:boolean,
            'search_location:text',
            'job_posted_date:timestamp without time zone',
            job_no_degree_mention:boolean,
            job_health_insurance:boolean,
            'job_country:text',
            'salary_rate:text',
            salary_year_avg:numeric,
            salary_hour_avg:numeric
          );,
        'application_sent_date:date',
        custom_resume:boolean,
        'resume_file_name:character varying',
        cover_letter_sent:boolean,
        'cover_letter_file_name:character varying',
        'status:character varying',
        'contact_name:text'
      );,
    'name:text',
    'link:text',
    'link_google:text',
    'thumbnail:text'
  );
  
  
  
  CREATE TABLE public.company_dim
(
    company_id INT PRIMARY KEY,
    name TEXT,
    link TEXT,
    link_google TEXT,
    thumbnail TEXT
);

-- Create skills_dim table with primary key
CREATE TABLE public.skills_dim
(
    skill_id INT PRIMARY KEY,
    skills TEXT,
    type TEXT
);

-- Create job_postings_fact table with primary key
CREATE TABLE public.job_postings_fact
(
    job_id INT PRIMARY KEY,
    company_id INT,
    job_title_short VARCHAR(255),
    job_title TEXT,
    job_location TEXT,
    job_via TEXT,
    job_schedule_type TEXT,
    job_work_from_home BOOLEAN,
    search_location TEXT,
    job_posted_date TIMESTAMP,
    job_no_degree_mention BOOLEAN,
    job_health_insurance BOOLEAN,
    job_country TEXT,
    salary_rate TEXT,
    salary_year_avg NUMERIC,
    salary_hour_avg NUMERIC,
    FOREIGN KEY (company_id) REFERENCES public.company_dim (company_id)
);

-- Create skills_job_dim table with a composite primary key and foreign keys
CREATE TABLE public.skills_job_dim
(
    job_id INT,
    skill_id INT,
    PRIMARY KEY (job_id, skill_id),
    FOREIGN KEY (job_id) REFERENCES public.job_postings_fact (job_id),
    FOREIGN KEY (skill_id) REFERENCES public.skills_dim (skill_id)
);

-- Set ownership of the tables to the postgres user
ALTER TABLE public.company_dim OWNER to postgres;
ALTER TABLE public.skills_dim OWNER to postgres;
ALTER TABLE public.job_postings_fact OWNER to postgres;
ALTER TABLE public.skills_job_dim OWNER to postgres;

-- Create indexes on foreign key columns for better performance
CREATE INDEX idx_company_id ON public.job_postings_fact (company_id);
CREATE INDEX idx_skill_id ON public.skills_job_dim (skill_id);
CREATE INDEX idx_job_id ON public.skills_job_dim (job_id);
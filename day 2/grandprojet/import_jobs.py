

import csv
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grandprojet.settings') 
django.setup()

from jobs.models import JobRecord, Contract, Candidate, Industry

csv_path = 'salaries.csv'  

created = 0
skipped = 0

default_industry, _ = Industry.objects.get_or_create(name="General")

with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        exists = JobRecord.objects.filter(
            job_title=row['job_title'],
            work_year=row['work_year'],
            employee_residence=row['employee_residence']
        ).exists()
        if exists:
            skipped += 1
            continue


        contract, _ = Contract.objects.get_or_create(
            type_code=row['employment_type'],
            defaults={'description': row['employment_type']}
        )


        candidate_name = f"{row['job_title']}@{row['company_location']}"
        candidate, _ = Candidate.objects.get_or_create(
            name=candidate_name,
            defaults={
                'email': f"{candidate_name.replace(' ', '_').lower()}@example.com",
                'location': row['employee_residence']
            }
        )


        JobRecord.objects.create(
            work_year=int(row['work_year']),
            experience_level=row['experience_level'],
            employment_type=contract,
            job_title=row['job_title'],
            salary=int(row['salary']),
            salary_currency=row['salary_currency'],
            salary_in_usd=int(row['salary_in_usd']),
            employee_residence=row['employee_residence'],
            remote_ratio=int(row['remote_ratio']),
            company_location=row['company_location'],
            company_size=row['company_size'],
            candidate=candidate,
            industry=default_industry
        )

        created += 1

print(f"✅ Done: {created} job records created, {skipped} skipped (already existed).")

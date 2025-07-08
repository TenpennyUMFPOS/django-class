import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grandprojet.settings')
django.setup()


from jobs.models import JobRecord
from django.db.models import Avg, Count

output = []


output.append(" Top 5 Highest Paying Job Titles (by avg USD salary):")
top_jobs = (
    JobRecord.objects
    .values('job_title')
    .annotate(avg_salary=Avg('salary_in_usd'))
    .order_by('-avg_salary')[:5]
)
for job in top_jobs:
    output.append(f"  {job['job_title']}: ${int(job['avg_salary']):,}")


output.append("\n Average Salary by Experience Level:")
avg_by_exp = (
    JobRecord.objects
    .values('experience_level')
    .annotate(avg_salary=Avg('salary_in_usd'))
    .order_by('experience_level')
)
for row in avg_by_exp:
    output.append(f"  {row['experience_level']}: ${int(row['avg_salary']):,}")

output.append("\n Number of Jobs by Company Location:")
jobs_by_loc = (
    JobRecord.objects
    .values('company_location')
    .annotate(total=Count('id'))
    .order_by('-total')
)
for row in jobs_by_loc:
    output.append(f"  {row['company_location']}: {row['total']} jobs")


total_jobs = JobRecord.objects.count()
remote_jobs = JobRecord.objects.filter(remote_ratio=100).count()
ratio = (remote_jobs / total_jobs * 100) if total_jobs else 0
output.append(f"\n Ratio of Fully Remote Jobs: {remote_jobs}/{total_jobs} ({ratio:.2f}%)")


with open("job_report.txt", "w", encoding="utf-8") as f:
    for line in output:
        print(line)
        f.write(line + "\n")

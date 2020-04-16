import bs4
import requests
import csv


url  = "https://jobs.bdjobs.com/jobdetails.asp?id=869296&fcatId=8&ln=1"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')


containers = soup.findAll("div", {"class": "container job-details1"})


file = open('Record19.csv', 'w')
################################################################################################################
writer = csv.writer(file)
writer.writerow(['JOB TITLE','COMPANY NAME','VACANCY','JOB RESPONSIBILITIES', 'JOB CONTEXT', 'EMPLOYMENT STATUS', 'EXPERIENCE','GENDER','AGE','JOB LOCATION','EDUCATIONAL REQUIREMENTS','ADDITIONAL REQUIREMENTS','SALARY','COMPENSATION & AND OTHER BENEFITS','PUBLISHED ON','APPLICATION DEADLINE'])




for item in containers:
    Job_Title = item.find("div", {"class": "col-sm-9 col-sm-pull-9"})
    job_titie = Job_Title.h4.text

    Company_Name = item.find("div", {"class": "col-sm-9 col-sm-pull-9"})
    company_name = Company_Name.h2.text

    Vacancy = item.find("div", {"class": "vac"})
    vac = Vacancy.p.text

    Employment_Status = item.find("div", {"class": "job_nat"})
    employment_status= Employment_Status.p.text

    Job_Responsibilities = item.find_all("div", {"class": "job_des"})
    job = Job_Responsibilities[1].ul.text
    
    #job_context = " "
    job_context = Job_Responsibilities[0].ul.text
    

    Educational_Requirements = item.find("div", {"class": "edu_req"})
    edu_req = Educational_Requirements.ul.text


    add_req = " "

    Compensation = item.find("div", {"class": "oth_ben"})
    comp="khan"
    if Compensation:
        comp = Compensation.ul.text

    else:
        comp = ""




    Job_Summary = soup.find("div", {"class": "panel-body"})
    h4_tags = Job_Summary.find_all('h4')


    Published_On = h4_tags[0].text
    pub_on = Published_On.replace("Published on:", "")

    #exp=""
    experience = h4_tags[3].text
    exp = experience.replace("Experience:", "")
##########################################################

    #gen = ""
    Gender = h4_tags[4].text
    gen = Gender.replace("Gender:", "")

    #ag = ""
    Age = h4_tags[5].text
    ag = Age.replace("Age:", "")

########################################################################################

    Job_Location = h4_tags[6].text
    joblctn = Job_Location.replace("Job Location:", "")

    sal = ""
    #Salary = h4_tags[7].text
    #sal = Salary.replace("Salary:", "")

    Application_Deadline = h4_tags[7].text
    app_dead = Application_Deadline.replace("Application Deadline:", "")


    writer.writerow([ job_titie, company_name, vac,job, job_context, employment_status, exp, gen, ag, joblctn, edu_req, add_req, sal, comp, pub_on, app_dead])


file.close()

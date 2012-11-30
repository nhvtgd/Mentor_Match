import os
os.environ["DJANGO_SETTINGS_MODULE"]="settings"
os.chdir("/home/trannguyen/MentorMatch")

from MentorMatchApp.models import CustomUser, Interest, Campus, Building
from password_generator import password_gen
from password_generator import username_gen
import string, random
##export DJANGO_SETTINGS_MODULE =${HOME}:/MentorMatch/settings.py
##import os
##os.environ['DJANGO_SETTINGS_MODULE'] = "myproject.settings"

skills = ['Ajax' ,'ASP' , 'ASP.NET' ,'BASIC', 'C', 'C++', 'C#', 'ColdFusion' , 'CSS', 'Flash', 'HTML', 'Java', 'Javascript', 'MySQL', 'Perl', 'PHP', 'Python', 'Ruby', 'Visual Basic','XHTML', 'XML'] 

building = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

campus= ['Corporate South', 'Research & Development (RDC)', 'OAB', 'Corporate HeadQuarter', 'TRAIL']

list_of_mentee = ['Sherie Ovitt','Reena Scheider','Clarinda Christo','Kasha Seyler','Nguyet Carignan','Cristi Paro','Romaine Rawley','Corine Slonaker','Sherise Ferdinand','Palmira Rowell']

list_of_mentor = ['Tran Nguyen','Mark Coztanzo', 'Michael', 'Melissa Piontek', 'Unknown']

list_of_password = [password_gen() for i in range(len(list_of_mentee)+len(list_of_mentor))]

list_of_username = [username_gen() for i in range(len(list_of_mentee)+len(list_of_mentor))]

boolean = [True,False]
for i in range(10):
    p = CustomUser( name = random.choice(list_of_mentee),
                password = random.choice(list_of_password),
                username = random.choice(list_of_username),
                mentee = random.choice(boolean),mentor = random.choice(boolean),
                interests = Interest.objects.create(interest_name = random.choice(skills)),
                campus = Campus.objects.create(campus_name = random.choice(campus)),
                building = Building.objects.create(building_name = random.choice(building)),
                numMentees = random.randint(0,2),
                numMentors = random.randint(0,2))
    p.save()


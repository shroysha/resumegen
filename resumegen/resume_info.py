from collections import UserDict

contact_info = dict(name="Shawn Shroyer",
                    email="shroysha@gmail.com",
                    phone="(240) 310-8658",
                    website="https://www.shroysha.dev")


class Certification(UserDict):

    def __init__(self, name, acronym, start_date):
        super().__init__(name=name, acronym=acronym, start_date=start_date)


class WorkExperience(UserDict):

    def __init__(self, position, company, location, start_date, end_date, duties):
        super().__init__(position=position, company=company, location=location, start_date=start_date,
                         end_date=end_date, duties=duties)


class Education(UserDict):

    def __init__(self, description, year, gpa, degree_type, major, minor, notes):
        super().__init__(description=description, year=year, gpa=gpa, degree_type=degree_type, major=major, minor=minor,
                         notes=notes)


certifications = [Certification("Certified Associate in Python Programming", "PCAP", 2019),
                  Certification("GIAC Security Essentials Certification", "GSEC", 2015),
                  Certification("Cisco Certified Network Associate in Routing and Switching", "CCNA", 2015),
                  Certification("Axelos Information Technology Infrastructure Library v3", "ITIL", 2015)]

work_experiences = [WorkExperience("Application Developer", "Independent", "Hagerstown, MD", "10/2016", "Present", [
    "Used IntelliJ to implement Gradle, MVC, Spring Boot, JUnit, and Lombok into my personal coding portfolio",
    "Created a Python modulo 29 number theory module in attempt to solve the 2015 Cicada 3301 puzzle",
    "Created a VR app using C#, Unity, PHP, MySQL, and OAuth2, which displays user-created geographical content, "
    "using the devices’ location, gyroscopic angle, and compass data"]),
                    WorkExperience("IT Support Specialist Level 3", "The Pennsylvania State University",
                                   "State College, PA", "01/2016", "10/2016", [
                                       "Moved to State College (post-graduation) and supported the Eberly College of "
                                       "Science’s Astronomy, Math, and Physics departments Linux research servers and "
                                       "their classroom and office Windows / Mac desktops",
                                       "Installed, packaged, and resolved issues with Anaconda, GCC, R Server, "
                                       "MATLAB, Maple, Mathematica, ArcGIS, and any other scientific software "
                                       "requested from researchers (some compiled from source)",
                                       "Lead and managed departments’ projects and assisted other departments as "
                                       "needed (primarily with Mac and Linux)",
                                       "Developed Bash, Python, and PowerShell scripts to automate daily tasks in "
                                       "SSH, SharePoint, and Active Directory"]),
                    WorkExperience("NOC Technician", "TE Connectivity", "Shirley, NY", "09/2015", "10/2015", [
                        "Participated in a two week contract to assist the physical setup of a WAN NOC at an AT&T "
                        "facility"]),
                    WorkExperience("Service Desk Technician", "National Institute of Standards and Technology (NIST)",
                                   "Gaithersburg, MD", "06/2014", "09/2015", [
                                       "Worked full-time at a highly structured helpdesk providing user support to "
                                       "Gaithersburg and Boulder, while in college"]),
                    WorkExperience("Student Technician Supervisor", "The Pennsylvania State University",
                                   "Mont Alto, PA", "01/2013", "06/2014",
                                   ["Received promotion (from Student Technician) on 01/2014"])]

educations = [Education("Graduate of The Pennsylvania State University", 2015, 3.59, "B.S.",
                        "Information Sciences and Technology (Integration of Applications focus)",
                        "Security and Risk Analysis (Network Security focus)", ["Dean’s List in all semesters"])]

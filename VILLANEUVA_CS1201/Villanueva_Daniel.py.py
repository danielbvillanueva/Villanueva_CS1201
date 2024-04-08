#Job Search Site Simulation

jobs_library = {
    "Accounting": [
        {
            "title": "Senior Accountant",
            "location": "Philippines, Manila",
            "salary_range": "$60,000 - $80,000 per year",
            "company": "ABC Accounting Firm"
        },
        {
            "title": "Financial Analyst",
            "location": "Philippines, Marikina",
            "salary_range": "$55,000 - $70,000 per year",
            "company": "XYZ Financial Services"
        },
        {
            "title": "Tax Specialist",
            "location": "Philippines, Quezon City",
            "salary_range": "$70,000 - $90,000 per year",
            "company": "LMN Tax Consultants"
        }
    ],
    "Management/Support": [
        {
            "title": "Administrative Assistant",
            "location": "Philippines, Batangas",
            "salary_range": "$40,000 - $50,000 per year",
            "company": "DEF Corporation"
        },
        {
            "title": "Human Resources Coordinator",
            "location": "Philippines, Cavite",
            "salary_range": "$45,000 - $55,000 per year",
            "company": "GHI Solutions"
        },
        {
            "title": "Operations Manager",
            "location": "Philippines, Taguig City",
            "salary_range": "$70,000 - $90,000 per year",
            "company": "JKL Enterprises"
        }
    ],
    "Sales": [
        {
            "title": "Sales Representative",
            "location": "Philippines, Manila",
            "salary_range": "$50,000 - $70,000 per year + Commission",
            "company": "MNO Sales Agency"
        },
        {
            "title": "Account Manager",
            "location": "Philippines, Baguio City",
            "salary_range": "$60,000 - $80,000 per year + Commission",
            "company": "PQR Solutions"
        },
        {
            "title": "Business Development Executive",
            "location": "Philippines, Cebu City",
            "salary_range": "$80,000 - $100,000 per year + Commission",
            "company": "STU Enterprises"
        }
    ],
    "Science/Technology": [
        {
            "title": "Software Engineer",
            "location": "Philippines, Manila",
            "salary_range": "$90,000 - $120,000 per year",
            "company": "VWX Tech Solutions"
        },
        {
            "title": "Data Scientist",
            "location": "Philippines, Davao City",
            "salary_range": "$100,000 - $130,000 per year",
            "company": "YZA Analytics"
        },
        {
            "title": "Research Scientist",
            "location": "Philippines, Pasig City",
            "salary_range": "$80,000 - $110,000 per year",
            "company": "ZAB Research Institute"
        }
    ]
}
employer_jobs_library = {}
ads_library = []
user_accounts = {}
employer_accounts = {}

def main_user():
    print("\n____________________________________________")
    print("Welcome! Find Online Jobs & Hire Top Talents")
    print("[1] Register")
    print("[2] Sign-in")
    print("[3] Employer")
    print("[4] Exit")
    print("_____________________________________________")
    
    while True:
        try:
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                register()
            elif choice == 2:
                sign_in()
            elif choice == 3:
                main_employer()
            elif choice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid Input. Please try again!")
        except ValueError:
            print("Invalid Input. Please enter a valid choice (1, 2, 3, or 4).")
                 
def register():
    username = input("Create your username: ")
    while True:
        if not username:
            print("Username cannot be empty!")
            username = input("Create your username: ")
            continue
        if username in user_accounts:
            print("Username already exists. Please try another name!")
            username = input("Create your username: ")
            continue
        break
    
    while True:
        password = input("Create your password (Must be at least 8 characters): ")
        if len(password) < 8:
            print("Password must be at least 8 characters!")
        else:
            user_accounts[username] = {'password': password}
            print("Sign-up Successful")
            main_user()
            break

def sign_in():
    print("Sign-in!")
    while True:
        username = input("Please enter your username: ") 
        if not username:
            print("Username cannot be empty!")
            continue
        password = input("Please enter your password: ")
        if user_accounts.get(username) and user_accounts[username]['password'] == password:
            print("Sign-in Successful")
            user_menu(username)
        else:
            print("Invalid username or password")
            break

def user_menu(username, profile = None):    
    print("\n________________________")
    print("Greetings User!")
    print("[1] Job Search")
    print("[2] Edit Profile")
    print("[3] Check Profile")
    print("[4] Career Advice")
    print("[5] Simulated Interview")
    print("[6] Resume Builder")
    print("[7] Exit")
    print("________________________")
    
    while True:
        try:
            choice = int(input("Please Enter your choice: "))
            if choice == 1:
                job_search()
            elif choice == 2:
                profile = edit_profile(profile)
            elif choice == 3:
                check_profile(profile)
            elif choice == 4:
                career_advice()
            elif choice == 5:
                simulated_interview()
            elif choice == 6:
                resume_builder()
            elif choice == 7:
                main_user()
            else:
                print("Invalid Input. Please choose again!")
            user_menu(username, profile)
        except ValueError:
            print("Invalid Input. Please enter a valid choice (1-7).")

def job_search():
    print("\n__________________________________")
    print("Let's Start your Job Hunt!")
    print("[1] Job Classification")
    print("[2] Popular/Hot Jobs")
    print("[3] Salary Range Selection")
    print("[4] Go back")
    print("__________________________________")

    while True:
        try:
            choice = int(input("Please Enter your Choice: "))
            if choice == 1:
                job_classification()
            elif choice == 2:
                job_trend()
            elif choice == 3:
                salary_range()
            elif choice == 4:
                user_menu(username)
            else:
                print("Invalid Input!")
        except ValueError:
            print("Invalid Input. Please enter a valid choice (1-4).")
            
def job_classification():
    print("\n__________________________________")
    print("Let's Start your Job Hunt!")
    print("Job Classification:")
    print("[1] Accounting")
    print("[2] Management/Support")
    print("[3] Sales")
    print("[4] Science/Technology")
    print("[5] Go back")
    print("__________________________________")
    choice = int(input("Please Enter your Choice: "))
    
    if choice == 5:
        job_search()
    
    elif 1 <= choice <= len(jobs_library):
        selected_class = list(jobs_library.keys())[choice - 1]
        print("\n")
        print(f"{selected_class} Jobs")
           
        for job in jobs_library[selected_class]:
            print(f"{job['title']}:")
            print(f"   Location: {job['location']}")
            print(f"   Salary Range: {job['salary_range']}")
            print(f"   Company: {job['company']}")  
            print("\n")
            
    print("[0] Go back to Job Classification")
    while True:
        go_back = input("Press 0 to go back: ")
        if go_back == '0':
            job_classification()
        else:
            print("Invalid input. Please enter '0' to go back to Job Classification.")

def job_trend():
    popular_jobs = [
        jobs_library["Accounting"][0], 
        jobs_library["Management/Support"][2], 
        jobs_library["Sales"][2],  
        jobs_library["Science/Technology"][1],  
        jobs_library["Science/Technology"][0]  
    ]
    
    print("\n__________________________________")
    print("Popular Jobs")
    print("__________________________________")
    for job in popular_jobs:
        print(f"Title: {job['title']}")
        print(f"Location: {job['location']}")
        print(f"Salary Range: {job['salary_range']}")
        print(f"Company: {job['company']}")
        print("\n")
    
    print("[0] Go back to Job Menu")
    while True:
        go_back = input("Press 0 to go back: ")
        if go_back == '0':
            job_search()
        else:
            print("Invalid input. Please enter '0' to go back.")

def salary_range():
    while True:
        job_salary_range = input("Please enter the range of the salary you're looking for (e.g., $50,000 - $70,000): ")
        matching_jobs = []

        for jobs in jobs_library.values():
            for job in jobs:
                job_salary = job["salary_range"]
                job_salary = [s.strip("$, per year").replace(",", "") for s in job_salary.split("-")]
                try:
                    job_salary = [int(s) for s in job_salary]
                    if job_salary[0] <= int(job_salary_range.split('-')[0].strip("$, ").replace(",", "")) <= job_salary[1]:
                        matching_jobs.append(job)
                except ValueError:
                    continue

        if matching_jobs:
            print("\n_______________________________________")
            print("Jobs within the specified salary range:")
            print("_______________________________________")
            for job in matching_jobs:
                print(f"Title: {job['title']}")
                print(f"Location: {job['location']}")
                print(f"Salary Range: {job['salary_range']}")
                print(f"Company: {job['company']}")
                print("\n")
        
           
            choice = input("Enter '0' to go back to job search menu: ")
            if choice == '0':
                job_search()
                break  
        else:
            print("No available jobs for the specified salary range.")
            break
    
def edit_profile(profile=None):
    print("\nWelcome to your Profile!")

    fields = ['First Name', 'Last Name', 'Address', 'Email Address', 'Phone Number (+63)']
    profile = {} if profile is None else profile  

    print("\nPlease fill out the following profile information:")
    for field in fields:
        if field in profile:
            print(f"- {field}: {profile[field]}")
            print(f"Would you like to change {field}? [y/n]")
            choice = input()
            if choice.lower() == 'y':
                if field == 'Phone Number (+63)':
                    while True:
                        phone_number = input(f"{field}: ")
                        if phone_number.isdigit() and len(phone_number) == 11:
                            profile[field] = phone_number
                            break
                        else:
                            print("Please enter a valid 11-digit phone number consisting only of digits.")
                else:
                    profile[field] = input(f"{field}: ")
        else:
            if field == 'Phone Number (+63)': 
                while True:
                    phone_number = input(f"{field}: ")
                    if phone_number.isdigit() and len(phone_number) == 11:
                        profile[field] = phone_number
                        break
                    else:
                        print("Please enter a valid 11-digit phone number consisting only of digits.")
            else:
                profile[field] = input(f"{field}: ")

    return profile
       
def check_profile(profile=None):
    if not profile:
        print("Profile is empty. Please fill it out first.")
        choice = input("Enter '0' to go back to the main menu or '1' to fill out your profile: ")
        
        if choice == '0':
            return
        elif choice == '1':
            profile = edit_profile() 
            check_profile(profile) 
        else:
            print("Invalid input. Please choose again.")
            check_profile(profile) 
    else:
        print("\nCompleted Profile:")
        for key, value in profile.items():
            print(f"{key}: {value}")
        print("\n[0] Go Back")
        choice = input("Enter '0' to go back to the main menu: ")
        
        if choice != '0':
            print("Invalid input. Please choose again.")
            check_profile(profile)
             
username = "Sample User"      
     
def career_advice():
    print("\n______________________________________________________")
    print("Career Compass: Navigating Your Professional Journey")
    print("Select Free Career Advises")
    print("[1] Mastering the art of negotiation")
    print("[2] Effective networking strategies")
    print("[3] Hard skills for workplace")
    print("[4] Best way to describe yourself")
    print("[5] Go back")
    print("______________________________________________________")
    
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("\nMastering the art of negotiation:")
                print("--Preparation is key. Know your goals, alternatives, and the other party's perspective.")
                print("--Listen actively to understand the other party's needs and concerns.")
                print("--Aim for win-win solutions where both parties feel satisfied.")
                print("--Be confident but flexible. Know when to compromise and when to stand firm.")
                print("\n[0] Go back")
                choice = int(input("Press 0 to go back!: "))
                if choice == 0:
                    career_advice()
            elif choice == 2:
                print("\nEffective networking strategies:")
                print("--Build genuine connections by showing interest in others and offering value.")
                print("--Utilize online platforms like LinkedIn to expand your professional network.")
                print("--Attend industry events, seminars, and workshops to meet new people.")
                print("--Follow up with contacts regularly to maintain relationships and stay top-of-mind.")
                print("\n[0] Go back")
                choice = int(input("Press 0 to go back!: "))
                if choice == 0:
                    career_advice()
            elif choice == 3:
                print("\nHard skills for workplace:")
                print("--Technical Skills  --Project Management")
                print("--Digital Literacy  --Analytical Skills")
                print("--Communication Skills  --Industry-specific Skills")
                print("\n[0] Go back")
                choice = int(input("Press 0 to go back!: "))
                if choice == 0:
                    career_advice()
            elif choice == 4:
                print("\nBest way to describe yourself:")
                print("--'I am passionate about my work; This conveys enthusiasm and dedication to the tasks at hand.'")
                print("--'I am ambitious and driven; Demonstrates a strong desire to achieve goals and excel in one's endeavors.'")
                print("--'I'm a natural leader; Indicates confidence in taking initiative and guiding others towards success.'")
                print("\n[0] Go back")
                choice = int(input("Press 0 to go back!: "))
                if choice == 0:
                    career_advice()
            elif choice == 5:
                user_menu(username)
            else:
                print("Invalid Input. Please Try Again!")
        except ValueError:
            print("Invalid Input. Please enter a valid choice (1-5).")

def simulated_interview():
    print("\nWelcome to the Simulated Interview!")
    print("Please answer the following questions as you would in a real interview:")
    
    questions = [
        "Tell me about yourself.",
        "What are your strengths?",
        "What are your weaknesses?",
        "Can you describe a challenging situation you faced and how you overcame it?",
        "Where do you see yourself in 5 years?",
    ]

    for i, question in enumerate(questions):
        print("\nQuestion", i + 1, ":", question)
        answer = input("Your answer: ")
        
        while True:
            print("\n[1] Continue to the next question")
            print("[2] Go back to the user menu")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                break  
            elif choice == '2':
                user_menu(username)
            else:
                print("Invalid choice. Please try again.")

    print("\nEnd of the simulated interview. Good luck!")

def resume_builder():
    print("\nWelcome to the Resume Builder!")
    print("Let's start building your resume.")
    
    resume = {}

    print("\nPlease enter your information:")
    resume['Name'] = input("| Name: ")
    resume['Email'] = input("| Email: ")
    
    while True:
        phone = input("| Phone (+63): ")
        if phone.isdigit() and len(phone) == 11:
            resume['Phone'] = phone
            break
        else:
            print("Invalid phone number. Please enter a 11 digits number.")
            
    resume['Address'] = input("| Address: ")
    resume['Objective'] = input("| Objective: ")
    resume['Education'] = input("| Education: ")
    resume['Experience'] = input("| Experience: ")
    resume['Skills'] = input("| Skills: ")
    
    print("\nYour resume has been created successfully!")
    print("Here's your resume:")
    print("\n____________________________")
    
    for key, value in resume.items():
        print("| " + key + ": ", value)
    print("____________________________")
    
    while True:
        print("\n[0] Go back to user menu")
        choice = input("Press 0 to go back: ")
        
        if choice == '0':
            user_menu(username)
        else:
            print("Invalid choice. Please try again.")
        
def main_employer():
    print("\n___________________________________________")
    print("Hire the right people for your business")
    print("[1] Register")
    print("[2] Sign-in")
    print("[3] Go Back!")
    print("___________________________________________")
    
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                employer_register()
            elif choice == 2:
                employer_sign_in()
            elif choice == 3:
                main_user()
            else:
                print("Invalid Input. Please try again!")
                main_employer()
        except ValueError:
            print("Invalid Input. Please enter a valid choice (1-3).")

def employer_register():
    employer_username = input("\nCreate your username: ")
    while True:
        if not employer_username:
            print("Username cannot be empty!")
            employer_username = input("Create your employer username: ")
            continue
        if employer_username in employer_accounts:
            print("Username already exists. Please try another name!")
            employer_username = input("Create your employer username: ")
            continue
        break
    
    while True:
        employer_password = input("Create your password (Must be at least 8 characters): ")
        if len(employer_password) < 8:
            print("Password must be at least 8 characters!")
        else:
            employer_accounts[employer_username] = {'password': employer_password}
            print("Employer Sign-up Successful")
            main_employer() 
            break

def employer_sign_in():
    print("\nEmployer Sign-in!")
    while True:
        employer_username = input("Please enter your employer username: ") 
        if not employer_username:
            print("Username cannot be empty!")
            continue
        employer_password = input("Please enter your employer password: ")
        if employer_accounts.get(employer_username) and employer_accounts[employer_username]['password'] == employer_password:
            print("Employer Sign-in Successful")
            employer_menu()
        else:
            print("Invalid username or password")
            break

def employer_menu():
    print("\n_________________________")
    print("Start your Business!")
    print("[1] Edit Business")
    print("[2] Create Ads")
    print("[3] Dashboard")
    print("[4] Go back")
    print("_________________________")
    
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                edit_business()
            elif choice == 2:
                create_ads()
            elif choice == 3:
                dashboard()
            elif choice == 4:
                main_user()
            else:
                print("Invalid Input. Please try again!")
        except ValueError:
            print("Invalid Input. Please enter a valid choice (1-4).")
            
def edit_business():
    print("\n_________________________________________")
    print("Edit Business")
    company_name = input("Enter your company name: ")
    description = input("Enter business description: ")
    while True:
        job_title = input("Enter job title: ")
        job_location = input("Enter job location: ")
        salary_range = input("Enter salary range: ")
        employer_jobs_library[job_title] = {'company_name': company_name, 'location': job_location, 'salary_range': salary_range}
        while True:
            add_more = input("\nDo you want to add another job? (yes/no): ")
            if add_more.lower() == 'yes':
                break
            elif add_more.lower() == 'no':
                print("Business information updated successfully!")
                break
            else:
                print("Invalid Input. Please enter 'yes' or 'no'!")
        if add_more.lower() == 'no':
            break
    input("Press Enter to go back to the Employer Menu...")
    employer_menu()

def create_ads():
    print("\nCreate Ads")
    ad_content = input("Write your ad content: ")
    target_audience = input("Specify target audience: ")
    ads_library.append({'content': ad_content, 'audience': target_audience})
    print("Ad created successfully!")
    choice = input("\nDo you want to create another ad? (yes/no): ")
    if choice.lower() == 'yes':
        create_ads()
    else:
        input("Press Enter to go back to the Employer Menu...")
        employer_menu()

def dashboard():
    print("\nDashboard")
    print("[1] Check Business")
    print("[2] Posted Ads")
    print("[0] Go back to Employer Menu")
    
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                check_business()
            elif choice == 2:
                posted_ads()
            elif choice == 0:
                employer_menu()
            else:
                print("Invalid choice!")
                input("Press Enter to go back to the Dashboard...")
                employer_menu()
        except ValueError:
            print("Invalid Input. Please enter a valid choice (0-2).")

def check_business():
    print("\nBusiness Details")
    company_name = input("Enter your company name: ")
    print("Business Name:", company_name)
    
    company_exists = False
    
    for job_title, job_details in employer_jobs_library.items():
        if job_details['company_name'] == company_name:
            print("Title:", job_title)
            print("Location:", job_details['location'])
            print("Salary Range:", job_details['salary_range'])
            print("-----------------------------")
            company_exists = True

    if not company_exists:
        print("Company name doesn't exist. Please check the name or create one!")
        input("Press Enter to go back to the Employer Menu...")
        check_business()
        return
    
    input("Press Enter to go back to the Employer Menu...")
    employer_menu()

def posted_ads():
    print("\nPosted Ads")
    if len(ads_library) == 0:
        print("No posted ads available currently.")
    else:
        for i, ad in enumerate(ads_library, 1):
            print(f"Ad {i}:")
            print("Content:", ad['content'])
            print("Target Audience:", ad['audience'])
            print("-----------------------------")
    choice = input("Do you want to create another ad? (yes/no): ")
    if choice.lower() == 'yes':
        create_ads()
    else:
        input("Press Enter to go back to the Employer Menu...")
        employer_menu()
        
main_user()


    
   




                        
                    

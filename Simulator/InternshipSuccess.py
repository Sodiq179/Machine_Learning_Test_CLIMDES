import random
import uuid
import pandas as pd

class InternshipSuccessDataSimulator:
    """
        A class for simulating internship success data.

        Parameters
        ----------
        number_of_interns: int
            The total number of interns to simulate.
        success_prop: float
            The proportion of interns who are successful.

        Attributes
        ----------
        interns_data: List[dict]
            A list of dictionaries containing the simulated internship success data. Each dictionary contains the following keys:
                * id: A unique identifier for each intern.
                * gender: The gender of the intern.
                * age: The age of the intern.
                * company_name: The name of the company where the intern is applying.
                * intern_role: The role the intern is applying for.
                * internship_duration: The duration of the internship.
                * academic_gpa: The intern's academic GPA.
                * number_of_internships_completed: The number of internships the intern has completed.
                * number_of_certification: The number of certifications the intern has.
                * intern_technical_skills: A list of the intern's technical skills.
                * programming_level: The intern's programming level (Beginner or Intermediate).
                * technical_skills_required: A list of the technical skills required for the intern role.
                * soft_skills: A list of the intern's soft skills.
                * technical_interview_score: The intern's technical interview score.
                * education: The intern's education level (Student or Graduate).
                * department: The intern's department.
                * internship_success: A boolean indicating whether the intern is successful.

        Methods
        -------
        generate_data() -> pd.DataFrame
            Generates the simulated internship success data and returns it as a Pandas DataFrame.

        Usage
        ------
        ```python
        simulator = InternshipSuccessDataSimulator(number_of_interns=100, success_prop=0.4)
        df = simulator.generate_data()

        print(df.head())
"""
    def __init__(self, number_of_interns: int, success_prop: float):
        self.number_of_interns = number_of_interns
        self.success_prop = success_prop
        self.interns_data = []

    def generate_data(self):
        for i in range(self.number_of_interns):
            intern = {}
            intern["id"] = uuid.uuid4()
            intern["gender"] = random.choice(["male", "female"])
            intern["age"] = random.randint(21, 25)
            intern["company_name"] = "CLIMDES"
            intern["intern_role"] = random.choice(["Machine Learning", "Frontend", "Backend"])
            intern["internship_duration"] = random.choice([3, 6, 12])
            intern["academic_gpa"] = round(random.uniform(2, 3), 2)
            intern["number_of_internships_completed"] = random.randint(0, 2)
            intern["number_of_certification"] = random.randint(0, 2)
            intern["intern_technical_skills"] = random.sample(["Excel", "Pandas", "Python", "HTML","SQL", "PowerPoint"], 3) if intern["intern_role"] == "Machine Learning" else random.sample(["Excel", "R", "CSS", "JavaScript","Python","SQL"], 3) if intern["intern_role"] == "Frontend" else random.sample(["CSS", "Java", "SQL","C","C++"], 3)
            intern["programming_level"] = random.choice(["Beginner", "Intermediate"])
            intern["technical_skills_required"] = ["Python", "SQL", "Machine Learning"] if intern["intern_role"] == "Machine Learning" else ["HTML", "CSS", "JavaScript"] if intern["intern_role"] == "Frontend" else ["Python", "Java", "SQL"]
            intern["technical_interview_score"] = random.randint(150, 197)
            intern["education"] = random.choice(["student", "graduate"])
            intern["department"] = random.choice(["Statistics", "Computer Science", "Engineering", "Mathematics"])

            # Set internship success based on success_prop
            if random.random() < self.success_prop:
                intern["internship_success"] = True
                intern["academic_gpa"] = round(random.uniform(3.5, 4), 2)
                intern["programming_level"] = "Intermediate"
                intern["technical_interview_score"] = random.randint(220, 250)
                intern["number_of_internships_completed"] = random.randint(1, 5)
                intern["number_of_certification"] = random.randint(3, 10)
                intern["intern_technical_skills"] = random.sample(["Python", "SQL", "Machine Learning", "HTML","CSS"], 3) if intern["intern_role"] == "Machine Learning" else random.sample(["HTML", "CSS", "JavaScript","Python","SQL"], 3) if intern["intern_role"] == "Frontend" else random.sample(["Python", "Java", "SQL","C","C++"], 3)

            else:
                intern["internship_success"] = False

            self.interns_data.append(intern)

        return pd.DataFrame(self.interns_data)
    

simulator = InternshipSuccessDataSimulator(number_of_interns=2500, success_prop=0.4)
df = simulator.generate_data()



#### Save the Dataset
df.to_csv("InternshipDataset.csv")

print("Successful")
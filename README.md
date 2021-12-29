# <p align="left">**Smart Recruitment System**</p>
Finding the best candidate for a specific job from a recruitment process within the shortest time is a challenge for a company nowadays. Nowadays, there are too many applicants, and it takes too much time and effort to get suitable candidates for a company’s job. The Human Resources team needs more workforce to scrutinize the resumes or CVs of candidates. 

The project aims to develop a more flexible, realistic and expert resume ranker system that ranks the resumes effectively and efficiently and gives the best candidate or candidates. This is a simple Django-based resume ranker website where recruiter users post jobs, candidate-users apply for the job, fill in the required data, and upload resumes. The system ranks the resumes based on the document similarity of the job description and the resumes using the KNN model. It saves human efforts, time, and cost.

# System Architecture
![](ProjectPic/Recruitment_System_Architecture.png)
- **Register/Login:** A user should be an authentic user to post a job or apply for a job.
- **View Job:** A user can browse or search for the job.
- **Apply Job:** An authentic users can apply for a job.  <!-- - **Participate assessment:** -->
- **Upload Resume:** An interested candidate user has to upload their resumes to apply for the desired vacancy.
- **Parsing:** The system parses the candidate resumes and generates the document similarity score of the candidates resumes according to the job description.
- **Ranking:** The system ranks the resumes based on the document similarity scores.

# Ranking Model
![](https://github.com/parvez86/Smart-Recruitment-System/blob/main/ProjectPic/Recruitment_System_Model_%20Architecture.png)
- **Data Preprocessing:** Data cleaning, word stemming, and verb lemmatization etc.
- **Basic Requirements:** Check different requirements like CGPA, gender and working experience etc.
- **Requirement Extraction:** 
    - TF-IDF: It calculates a score for each keyword that signifies its importance to the document or resumes.
       ```
       TF(‘keyword’) = number of appeared (‘keyword’)/Total number of (‘keyword’)  
       ```
       ``` 
       IDF(‘keyword’) = log(total number of resumes / total number of the resume with term ‘keywords’)
       It sets IDF log value = 1 for the required resume and 0 for the unwanted.
       ```
- **Generate Document Similarity Score:** Using the KNN (K-Nearest Neighbour) model and the TF-IDF weight of the resumes, the system generates a document similarity score (KNN-score) of each resumes according to the job description.
- **Ranking:** Based on the KNN-scores, the system ranks the resumes and shortlists them.

<!-- # Project Features

| Home Page   | Job List| Single Job Details  |
|:---------------:  |:-----------:|:-------:|
|![home_page]|![job_list]|![single_job]  |


| Apply Job   | Shortlisted Candidates  |SignUp Page|
|:-------------------:|:-----------------------:|:------------:|
|![apply_job]|![ranking]|![signup_page]|


[home_page]: https://github.com/parvez86/Smart-Recruitment-System/blob/main/ProjectPic/homepage.png
[job_list]: https://github.com/parvez86/Smart-Recruitment-System/blob/main/ProjectPic/joblisting_page.png
[single_job]: https://github.com/parvez86/Smart-Recruitment-System/blob/main/ProjectPic/single_job_details.png
[apply_job]: https://github.com/parvez86/Smart-Recruitment-System/blob/main/ProjectPic/apply_job_page.png
[ranking]: https://github.com/parvez86/Smart-Recruitment-System/blob/main/ProjectPic/rank_page.png
[signup_page]:  https://github.com/parvez86/Smart-Recruitment-System/blob/main/ProjectPic/signup_page.png -->

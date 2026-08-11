# Overview

The goal of this assignment is to give you a final opportunity to apply key software engineering practices covered throughout the semester, including project management, teamwork, version control, design, coding best practices, object-oriented principles, and quality assurance. 

# Instructions

You and your team of up to 3 members have the freedom to choose what to implement for this project, provided you meet the requirements outlined in this section. The first requirement is that the software must be a web application, with the backend written in Python and supporting user creation and authentication. Additionally, you are required to use Scrum as your development methodology, completing at least three sprints during the project. Meetings should be documented with notes saved in the **scrum** folder, using the provided template ([scrum/sprint_template.md]). Proper documentation of Scrum meetings—such as planning, daily scrums, reviews, and retrospectives—helps track progress, identify issues, and maintain transparency throughout the project.

The project should be organized in a separate GitHub public repository that you will create under the [colorado-online](https://github.com/colorado-online) organization. Add all team members and the instructor as collaborators to ensure proper access and collaboration. The project's repository should maintain two long-lived branches: 

* **main**: for the stable release and
* **dev**: for ongoing development. 

To preserve code quality, the **main** branch must be protected and require a code review before any pull request is approved. This workflow promotes stability, accountability, and best practices in version control.

```
Share the URL of your project's GitHub repository here.
```

The repository should have, at a minimum, the following structure:

```
README.md
Dockerfile
docker-compose.yml (only if using a multi-layer architecture)
requirements.txt
src/
tests/
uml/
scrum/
htmlcov/
```

Feel free to add other folders and files as needed. 

Use the provided [README_TEMPLATE.md](README_TEMPLATE.md) as the basis for the repository’s **README.md** file.

All source code must include a consistent header comment with a brief description and the author(s). It should comply with the PEP 8 style standard and will be reviewed for best practices, including proper commenting, meaningful naming, clean formatting, effective function decomposition, adherence to object-oriented principles, robust error handling, and other quality guidelines.

Provide at least one **white-box** test and one **black-box** test, neither related to user creation or authentication. **White-box** testing focuses on the internal logic and structure of the code, while **black-box** testing validates functionality from the user’s perspective without considering the internal implementation. Additionally, generate a **test coverage** report under **htmlcov** using Python’s coverage tool to show how much of the code is exercised by your tests.

The final product must be deployed using Docker containerization technology and include all project dependencies frozen in a **requirements.txt** file. Optionally, you should provide database persistence using a database other than SQLite and follow at least a three-layer software architecture. In that case, deployment must be done with **Docker Compose**, using a minimum of two containers to ensure modularity and scalability.

A final progress report must be created. We suggest using the provided burndown template. A generated image from the burndown chart should be displayed in the GitHub repository's README. 

# Self and Team Evaluation 

Please reflect on both your own contributions and those of your teammates using the descriptions provided for each dimension. You may refer back to these descriptions as you consider each person's role in the project.

* Meaningful Contributions: Consider how often and significantly the person contributed to the project. This includes writing code, testing, researching, documenting, or helping solve problems.
* Value of Contributions: Value goes beyond technical input. It includes contributions in organization, communication, conflict resolution, and other areas that support team success.
* Collaboration: Collaboration ranges from baseline participation-such as responding when asked-to proactive support like initiating discussions and resolving misunderstandings. Collaboration: can range from basic participation—such as responding when asked—to proactive engagement, like initiating discussions and helping resolve misunderstandings.
* Initiative and Responsibility: Initiative means stepping up without needing to be asked. Responsibility includes owning tasks, meeting deadlines, and following through on commitments.
* Communication and Dependability: This includes keeping teammates informed, communicating challenges, and reliably completing assigned tasks.
* Presence and Availability: Reflect on how consistently the person was present and reachable—attending meetings, responding to messages, and participating in team activities. Note that some team members may contribute meaningfully but be less available than expected.
* Trust Building: Trust is essential for team success because it creates the foundation for effective collaboration, communication, and accountability. When team members trust each other, they feel safe sharing ideas, asking questions, and giving honest feedback—without fear of judgment or retaliation.
* Conflict Resolution: Conflict resolution is the process of addressing and resolving disagreements in a constructive and respectful way. It helps team members find common ground, maintain collaboration, and move forward productively.
* Decision-Making: Decision-making is the process of choosing the best course of action among available options to achieve a goal. It provides direction and keeps the team moving forward.

```
Your Name: <Last_First_Name>
```

Rate your collaboration using: 
* 1 (strongly disagree)
* 2 (disagree)
* 3 (neutral)
* 4 (agree) or 
* 5 (strongly agree)

```
[  ] I made meaningful contributions to the project.
[  ] My contributions were valuable to the team’s success.
[  ] I supported collaboration within the team.
[  ] I took initiative and responsibility for my work.
[  ] I communicated effectively and was dependable.
[  ] I was present and available to the team as expected.
[  ] I fostered trust by being reliable, transparent, and respectful in all interactions.
[  ] I helped resolve disagreements constructively, promoting understanding and collaboration.
[  ] I contributed to or led decision-making processes with clarity, fairness, and consideration of team input.
```

```
Teamate's Name: <Last_First_Name>
```

Rate their collaboration using: 
* 1 (strongly disagree)
* 2 (disagree)
* 3 (neutral)
* 4 (agree) or 
* 5 (strongly agree)

```
[  ] The team member made meaningful contributions to the project.
[  ] The team member  contributions were valuable to the team’s success.
[  ] The team member supported collaboration within the team.
[  ] The team member took initiative and responsibility for my work.
[  ] The team member communicated effectively and was dependable.
[  ] The team member was present and available to the team as expected.
[  ] The team member fostered trust by being reliable, transparent, and respectful in all interactions.
[  ] The team member helped resolve disagreements constructively, promoting understanding and collaboration.
[  ] The team member contributed to or led decision-making processes with clarity, fairness, and consideration of team input.
```

```
Teammate's Name: <Last_First_Name>
```

Rate their collaboration using: 
* 1 (strongly disagree)
* 2 (disagree)
* 3 (neutral)
* 4 (agree) or 
* 5 (strongly agree)

```
[  ] The team member made meaningful contributions to the project.
[  ] The team member  contributions were valuable to the team’s success.
[  ] The team member supported collaboration within the team.
[  ] The team member took initiative and responsibility for my work.
[  ] The team member communicated effectively and was dependable.
[  ] The team member was present and available to the team as expected.
[  ] The team member fostered trust by being reliable, transparent, and respectful in all interactions.
[  ] The team member helped resolve disagreements constructively, promoting understanding and collaboration.
[  ] The team member contributed to or led decision-making processes with clarity, fairness, and consideration of team input.
```


# Rubric

✅ Documentation (35 points)

+5 Project README: Mission statement
+5 Project README: Use case diagram
+5 Project README: Sequence diagram
+10 Project README: User stories (~6 × 1.5)
+5 Project README: Class diagram for model classes
+5 Project README: Test coverage report using Python’s coverage

✅ Repository & Process (30 points)

+5 GitHub repository organization, branches, and main branch protection
+10 Scrum notes
+15 Team/self evaluation

✅ Implementation & Quality (25 points)

+10 Implementation (~5 × 2)
+5 Code inspection: PEP8 compliance
+5 Code inspection: Comments, naming, functions, formatting, OOP best practices, error handling
+5 Project deployment

✅ Testing (10 points)

+10 Testing requirements

Total: 100 points

✅ Bonus (5 points)

+5 Deployment using Docker Compose and multi-layer architecture

❌ Penalties

-10 User creation not available/working
-10 User authentication not available/working
-5 For each user story not completed (up to 25 points deduction)
-5 Main branch does not have consistent commits
-5 Dev branch does not have consistent commits
-5 No burndown chart was created
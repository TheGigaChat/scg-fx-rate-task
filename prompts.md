# Prompts Log

## Template
Use this template for each new prompt:

```md
## Prompt <N>
- Date: YYYY-MM-DD
- Timezone: Europe/Kiev
- Context: Short note about what was happening
- User Prompt:
  <paste full prompt>
- Notes (optional):
  <quick tags or follow-up decisions>
```
## Prompt 1
- Date: 2026-02-28
- Timezone: Europe/Kiev
- Context: Project understanding and planning request.
- User Prompt:
  I will give you the context and then create a new plan.md file where you will create a detailed plan for this project.

  I see a small task in the description of the SEB bank application. I send you a work description together to the task, so you can better understand what is important for the bank. As I understand I have a task where I need to connect to the endpoint with the API (or download the zip) and then exchange the currency by using the ECB protoloc/rule. As I understand this is a simple Python program without a large structure or any frontend. Explain me what to do there and then make a plan with general steps (not too detailed). I assess it and if I will have any questions, we expand the plan.

  [Job description and assignment details were included in full in chat.]

## Prompt 2
- Date: 2026-02-28
- Timezone: Europe/Kiev
- Context: Add project behavior rules.
- User Prompt:
  Also create the agents.md file that will have the preferences/constrains of how to work in this project. At first write to use the built-in vscode command, so I will be able to see that changes on the code that you do. Then you need to write a clean, structured code with attention to edge cases, but not fancy. It should be easy to read for the second year student.

## Prompt 3
- Date: 2026-02-28
- Timezone: Europe/Kiev
- Context: Extend project behavior rules.
- User Prompt:
  Also add to the rule that every time when you make a change with the code in the end of the promp suggest me a clean commit name.

## Prompt 4
- Date: 2026-02-28
- Timezone: Europe/Kiev
- Context: Prompt logging and module layout request.
- User Prompt:
  Also I need to log my prompts. Make a prompts.md file where you need to create a simple template for storing my prompts and then store all the prompts from this chat.

  I downloaded zip files to the data folder. Now you can clearly see todays data and the historical data.

  Let's make file structure (small module layout). Suggest me the structure. If I would like it, implement it.

## Prompt 1 Appendix (Full Details)
- Date: 2026-02-28
- Timezone: Europe/Kiev
- User Prompt (full additional context):
  Youth LAB - Software Developer Intern in FX and Derivatives team | SEB, Tallinn

  Tallinn, Harjumaa, Estonia � 2 weeks ago � 34 applicants

  Promoted by hirer � No response insights available yet


  �1,050/month - �1,300/month

  Hybrid

  Internship
  Easy Apply

  Save
  See how you compare to 34 applicants

  Access exclusive applicant insights, see jobs where you have the highest chance of hearing back, and more.

  Try Premium for �0

  People you can reach out to

  School alumni from Tallinn University of Technology


  Show all
  About the job
  Are you looking for a way to gain practical skills and experience in the field of finance?

  Your career should be as unique as you are. As a leading employer in the banking sector, we promote the development and career of our employees. By working with us, you will acquire new skills and it does not matter what your experience is so far.

  Youth LAB is a paid international internship program at SEB Bank. You will dedicate ten weeks of time working on real and meaningful business projects, including hackathon where you will also discover new ways of collaborative and innovative work between other international students. You will get a personal mentor who will support you throughout the internship. How great is that?

  FX and Derivatives team in Savings and Investments tribe is looking for a person to contribute to software developments.

  Your Responsibilities Will Include

  Contribute to larger Java/Spring Boot and Angular projects;
  Creating end to end tests based on prepared test case descriptions with Playwright in TypeScript;
  Writing unit tests;
  Preparing documentation.

  To Thrive In This Role, We Believe You

  Are an IT student in Higher educational institution;
  Are interested in the software development and like to focus on details;
  Have excellent communication and teamwork abilities;
  Are fluent in Estonian and English;
  Are outgoing & positive team player with can-do attitude;
  Are able to manage your time & prioritize.

   What we offer?

  Agile and modern ways of working;
  Paid summer internship;
  A flat hierarchy and openness to share ideas, opinions and points of views;
  Extensive training and learning opportunities;
  Innovative company at the forefront of technology;
  Possibility to work part time remotely.

  Do you want to be a part of SEB?

  Welcome to join our inspiring culture and dedicated team distributed all across the Baltic states and beyond.

  Since we select candidates continuously, feel free to send in your application today, but no later than March 1st.

  Learn more about SEB culture and Youth LAB summer internship program: www.seb.ee/en/internship.

  Before tax deduction, the final offer will depend on the experience and competencies of the selected candidate. Overall remuneration package consists of the salary together with other benefits.

  NB! To better understand your technical capabilities and how you could stand out from other candidates, we invite you to complete a short homework assignment.

  Overview

  The solution can be implemented in Python or a Jupyter Notebook. NB! If you choose to implement the solution in a Jupyter Notebook, ensure that all code cells are executed in order, and that the notebook can be run from start to finish without errors.

  Use Python 3.12 or later and a strongly typed coding style (explicit variable types, function return types, etc.). Follow Pythonic conventions and best practices. You may use any suitable Python packages, but avoid obscure or lesser-known libraries. If external packages are used, freeze the dependencies in a requirements.txt file using pip freeze > requirements.txt, or list them in a new README file.

  NB! If you use any help from AI tools (e.g., ChatGPT), please mention it in a separate README file in your submission and include links to the chats or chat logs used. If no AI tools were used, please state that as well.

  Task

  Create a simple ETL process: extract the Euro foreign exchange reference rates from the ECB, transform the data, and load the cleaned data into a separate HTML or Markdown file in table format. More information about ECB foreign exchange reference rates can be found here: https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html

   (Extract)
   Extract and read ECB rates from ECB APIs: o Daily rates: https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip o Historical rates: https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip
   (Transform)
   Load daily and historical exchange rates
   Select only USD, SEK, GBP, and JPY
   Calculate the historical mean rates for the four selected currencies based on historical data
   (Load)

  Create an HTML or Markdown table with the following columns:

  Currency Code
   Rate
   Mean Historical Rate

  Save the table to a file named exchange_rates.html or exchange_rates.md in the project root folder.

  Submission

  Save your code in a public GitHub repository (or a similar platform) and include the link in your job application.

## Prompt 5
- Date: 2026-02-28
- Timezone: Europe/Kiev
- Context: Package naming clarification.
- User Prompt:
  A question about the folder fx_etl/. Is it our app folder? Can we call it app or this is not correct?

## Prompt 6
- Date: 2026-02-28
- Timezone: Europe/Kiev
- Context: App package scaffold request.
- User Prompt:
  Geterate this project structure but use app folder/package.

## Prompt 7
- Date: 2026-02-28
- Timezone: Europe/Kiev
- Context: Add mandatory prompt-logging rule.
- User Prompt:
  write to the agents rule, that after any prompt that I do you must log it.

## Prompt 8
- Date: 2026-02-28
- Timezone: Europe/Kiev
- Context: Gitignore expansion request.
- User Prompt:
  Do I need to expand the .gitignore file for this project? Can you do it.

## Prompt 9
- Date: 2026-02-28
- Timezone: Europe/Kiev
- Context: Recovery request after accidental rollback.
- User Prompt:
  I accidentally made a rollback for 3 files. Can you find them and restore.

## Prompt 10
- Date: 2026-02-28
- Timezone: Europe/Kiev
- Context: Memory bank documentation request.
- User Prompt:
  Can you write the description of the project on which we are working right now to the readme_ai.md file. This is a memory bank, so update it after any change. Also write in into the ai rules.

## Prompt 11
- Date: 2026-02-28
- Timezone: Europe/Kiev
- Context: Implement first transform step for daily rates.
- User Prompt:
  Read the readme_ai.md file to understand on what we are working. Also read the agents.md file to understand the rules.

  Let's do this small step: Parse daily rates and capture latest values for `USD`, `SEK`, `GBP`, `JPY`.

## Prompt 12
- Date: 2026-02-28
- Timezone: Europe/Kiev
- Context: Implement historical transform step.
- User Prompt:
  Lets continue with the next step:
  - Parse historical rates and collect full time-series values for those currencies.

## Prompt 13
- Date: 2026-02-28
- Timezone: Europe/Kiev
- Context: Implement historical mean and formatting step.
- User Prompt:
  Nice, I like it. Let's continue with this step:
  - Compute mean historical rate per selected currency.
  - Apply consistent numeric formatting/rounding for output.

## Prompt 14
- Date: 2026-02-28
- Timezone: Europe/Kiev
- Context: Improve console table readability with consistent column widths.
- User Prompt:
  Now when I run the main, I see the columns with the different width. Can you make the width consistent so it will be easy to understand which value and to which column is attached.

## Prompt 15
- Date: 2026-02-28
- Timezone: Europe/Kiev
- Context: Implement load step to write final output file.
- User Prompt:
  Let's complete the step number 4 about the load.

## Prompt 16
- Date: 2026-02-28
- Timezone: Europe/Kiev
- Context: Clarify whether generated output should be committed or ignored.
- User Prompt:
  Do I need to push the output table to the git or is it better to add it to the .gitignore?

## Prompt 17
- Date: 2026-02-28
- Timezone: Europe/Kiev
- Context: Complete final validation and polish steps from plan.
- User Prompt:
  Complete the final steps of the plan.md

## Prompt 18
- Date: 2026-02-28
- Timezone: Europe/Kiev
- Context: Switch extract implementation to ECB ZIP API with in-memory processing and remove local data files.
- User Prompt:
  Now use all the rules for the ai as before. Update the plan.md to include the extract step from the zip API endpoint: https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip and https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip. Then we need to extract it in memory and then parse immediately, save only the final output. Also delete the data folder with the manually downloaded files.

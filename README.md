<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">PHISHKILL</h1></p>
<p align="center">
	<em>Shield Your Inbox, Block the Bait!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/sandeepsalwan1/AnimalCare?style=flat&logo=opensourceinitiative&logoColor=white&label=License&color=0080ff" alt="MIT License">
	<img src="https://img.shields.io/github/last-commit/sandeepsalwan1/PhishKill?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/sandeepsalwan1/PhishKill?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/sandeepsalwan1/PhishKill?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

PhishKill is an innovative tool designed to enhance email security by detecting and assessing phishing risks. Utilizing advanced AI technology, it analyzes email content for potential threats, providing users with a risk assessment and practical advice on handling suspicious emails. Ideal for individuals and organizations aiming to bolster their cybersecurity measures, PhishKill offers a user-friendly interface and robust protection against email-based threats.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes a web-based interface hosted on Heroku for real-time interaction and feedback.</li><li>Centralized configuration via `tst` for secure API key management.</li><li>Core processing handled by `EmailPhishingScript/Main.py` using the OpenAI GPT-3.5-turbo model.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Modular design with separate scripts for different functionalities within `EmailPhishingScript`.</li><li>Use of Python for backend processing and Flask for web application framework.</li><li>Consistent use of external libraries specified in `requirements.txt` files.</li></ul> |
| 📄 | **Documentation** | <ul><li>Documentation includes install, usage, and test commands primarily managed through `pip`.</li><li>Language distribution indicates primary use of `.txt` and `.py` files.</li><li>Documentation spread across various text files and inline comments in scripts.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integration with OpenAI's API for email content analysis.</li><li>Deployment on Heroku cloud platform via `Procfile`.</li><li>Utilizes Flask for web application management and routing.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Codebase includes distinct components for handling email analysis, user interface, and API interactions.</li><li>Separate `requirements.txt` for main project and `EmailPhishingScript` directory.</li><li>Template-based approach for user interface in `templates/index.html`.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes a specific script `EmailPhishingScript/test.py` for testing API connectivity and functionality.</li><li>Testing primarily focuses on integration with OpenAI services.</li><li>Use of Python's built-in testing capabilities.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Performance optimizations likely focused on API response handling and data processing.</li><li>Asynchronous operations supported by libraries like `aiohttp` and `anyio`.</li><li>Efficient handling of text and email data formats for quick analysis.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Uses `argon2-cffi` for potentially managing secure authentication processes.</li><li>Secure API key storage and management via `tst` file.</li><li>Security assessments for emails include checking links and attachments for phishing threats.</li></ul> |

---

## 📁 Project Structure

```sh
└── PhishKill/
    ├── EmailPhishingScript
    │   ├── Mail1.txt
    │   ├── Mail2.txt
    │   ├── Main.py
    │   ├── Procfile
    │   ├── app.py
    │   ├── requirements.txt
    │   ├── responseToMail1.txt
    │   ├── responseToMail2.txt
    │   ├── results.txt
    │   ├── templates
    │   └── test.py
    ├── LICENSE
    ├── README.md
    ├── WebsiteLink
    ├── requirements.txt
    └── tst
```


### 📂 Project Index
<details open>
	<summary><b><code>PHISHKILL/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/sandeepsalwan1/PhishKill/blob/master/WebsiteLink'>WebsiteLink</a></b></td>
				<td>- Provides a critical component of the project's web infrastructure by hosting the main interface on Heroku<br>- The link directs users to the primary access point where they can interact with the application's features, facilitating user engagement and functionality testing in a live environment<br>- This setup is essential for real-time user feedback and iterative development.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/sandeepsalwan1/PhishKill/blob/master/tst'>tst</a></b></td>
				<td>- Stores the API key for the OpenAI service, essential for authenticating and enabling API requests across the application<br>- It serves as a centralized configuration point, ensuring secure and efficient access to OpenAI functionalities required for the project's operations, such as generating text or processing data inputs<br>- This setup supports maintainability and scalability within the codebase architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/sandeepsalwan1/PhishKill/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>- The `requirements.txt` file serves a crucial role within the overall architecture of the codebase by specifying the exact versions of external libraries and dependencies required for the project<br>- This file ensures that the environment for the project is consistent and predictable, mitigating issues that may arise from version discrepancies among different development setups<br>- It lists various Python libraries along with their specific versions, including frameworks for asynchronous operations (`aiohttp`, `anyio`), security components (`argon2-cffi`), and other utilities that support the project's functionality<br>- By maintaining this file, the project upholds a stable development, testing, and production environment, facilitating seamless collaboration and deployment processes across different systems and platforms.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- EmailPhishingScript Submodule -->
		<summary><b>EmailPhishingScript</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/sandeepsalwan1/PhishKill/blob/master/EmailPhishingScript/Main.py'>Main.py</a></b></td>
				<td>- Main.py serves as the core component of an email phishing detection system, utilizing OpenAI's GPT-3.5-turbo model<br>- It processes user-inputted email content, evaluates the likelihood of phishing, and records the AI-generated risk assessment and indicators to a results file for review.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/sandeepsalwan1/PhishKill/blob/master/EmailPhishingScript/results.txt'>results.txt</a></b></td>
				<td>- Analyzes and assesses the risk level of emails for phishing threats<br>- The script evaluates the content, subject, language, and tone of emails, along with checking for suspicious links or attachments<br>- It provides a risk probability and advises on caution, enhancing email security within the system.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/sandeepsalwan1/PhishKill/blob/master/EmailPhishingScript/responseToMail1.txt'>responseToMail1.txt</a></b></td>
				<td>- Analyzes potential phishing threats in emails by evaluating risk factors such as urgent language, claims of unusual activity, requests for identity verification, and suspicious links<br>- The analysis concludes with a high likelihood of phishing, aiding in the identification and prevention of email-based security threats within the system.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/sandeepsalwan1/PhishKill/blob/master/EmailPhishingScript/Mail1.txt'>Mail1.txt</a></b></td>
				<td>- Mail1.txt serves as a phishing simulation template within the EmailPhishingScript project, designed to educate users on recognizing fraudulent emails<br>- It mimics a security alert from a bank, instructing recipients to verify their account through a deceptive link, thereby highlighting common tactics used by cybercriminals to compromise personal information.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/sandeepsalwan1/PhishKill/blob/master/EmailPhishingScript/app.py'>app.py</a></b></td>
				<td>- EmailPhishingScript/app.py serves as the core interface for a web application that assesses email content to determine phishing risks<br>- Utilizing the OpenAI API, it processes user-submitted emails, evaluates potential phishing indicators, and outputs risk assessments<br>- The application also records responses for further analysis.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/sandeepsalwan1/PhishKill/blob/master/EmailPhishingScript/responseToMail2.txt'>responseToMail2.txt</a></b></td>
				<td>- EmailPhishingScript/responseToMail2.txt evaluates the security risk of a work-related email, assigning a low risk percentage<br>- It assesses the email's content, tone, sender's credentials, and absence of suspicious requests, concluding minimal phishing indicators<br>- Users are advised to verify sender details and exercise caution with links and attachments.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/sandeepsalwan1/PhishKill/blob/master/EmailPhishingScript/Procfile'>Procfile</a></b></td>
				<td>- Specifies the command that a Heroku-based application should execute to start the server, using Python to run the script named app.py<br>- This setup is crucial for deploying the web application component of the EmailPhishingScript project, ensuring it is accessible and operational on the Heroku cloud platform.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/sandeepsalwan1/PhishKill/blob/master/EmailPhishingScript/requirements.txt'>requirements.txt</a></b></td>
				<td>- Requirements.txt in the EmailPhishingScript directory specifies dependencies essential for the project's operation<br>- It includes Flask for web application framework, python-dotenv for environment variable management, and openai for integrating AI functionalities<br>- These dependencies ensure the software's compatibility and functionality within the broader codebase architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/sandeepsalwan1/PhishKill/blob/master/EmailPhishingScript/test.py'>test.py</a></b></td>
				<td>- EmailPhishingScript/test.py serves as a diagnostic tool within the broader codebase, verifying the operational status of the local development environment<br>- It utilizes the OpenAI API to execute a simple test interaction, ensuring that the API key is correctly sourced from the environment and that the OpenAI client is properly configured and responsive.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/sandeepsalwan1/PhishKill/blob/master/EmailPhishingScript/Mail2.txt'>Mail2.txt</a></b></td>
				<td>- EmailPhishingScript/Mail2.txt serves as a simulated phishing email within the security training module<br>- It mimics a typical workplace communication about an upcoming meeting, complete with details like date, time, and location, crafted to test employee vigilance against phishing attempts in a controlled environment.</td>
			</tr>
			</table>
			<details>
				<summary><b>templates</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/sandeepsalwan1/PhishKill/blob/master/EmailPhishingScript/templates/index.html'>index.html</a></b></td>
						<td>- Serves as the primary user interface for the Phish Kill application, providing a web-based platform where users can input and analyze email content for spam indicators<br>- It features navigation, spam checking functionality, and sections detailing the app's features, about us information, and contact form.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with PhishKill, ensure your runtime environment meets the following requirements:

- **Programming Language:** Error detecting primary_language: {'txt': 7, 'py': 3, 'html': 1}
- **Package Manager:** Pip


### ⚙️ Installation

Install PhishKill using one of the following methods:

**Build from source:**

1. Clone the PhishKill repository:
```sh
❯ git clone https://github.com/sandeepsalwan1/PhishKill
```

2. Navigate to the project directory:
```sh
❯ cd PhishKill
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-INSTALL-COMMAND-HERE'
```




### 🤖 Usage
Run PhishKill using the following command:
**Using `pip`** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-RUN-COMMAND-HERE'
```


### 🧪 Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-TEST-COMMAND-HERE'
```


---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/sandeepsalwan1/PhishKill/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/sandeepsalwan1/PhishKill/issues)**: Submit bugs found or log feature requests for the `PhishKill` project.
- **💡 [Submit Pull Requests](https://github.com/sandeepsalwan1/PhishKill/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/sandeepsalwan1/PhishKill
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/sandeepsalwan1/PhishKill/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=sandeepsalwan1/PhishKill">
   </a>
</p>
</details>

---

## 🎗 License

This project is released under the [MIT License](https://opensource.org/licenses/MIT/). For more details, please refer to the [LICENSE](./LICENSE) file. 

---

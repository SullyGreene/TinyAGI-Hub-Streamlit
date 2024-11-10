# 🤖 TinyAGI Hub Streamlit

Welcome to **TinyAGI Hub Streamlit** — a streamlined interface built with 🦄 Streamlit for managing and exploring the components of **TinyAGI Hub**. This app allows users to manage 🤖 agents, 🧩 plugins, 🛠️ tools, 📦 modules, and ⚙️ services that form the TinyAGI system. It also supports easy integration of new components, enabling quick customization and expansion. With its modular design, TinyAGI Hub Streamlit allows users to efficiently adapt and enhance their AGI systems for flexible development.

TinyAGI Hub Streamlit offers a robust platform for implementing AGI solutions. Whether you are a 🧑‍🔬 researcher, 💻 developer, or enthusiast, it provides powerful 🛠️ tools for experimentation, configuration, and deployment of AGI components. The user-friendly interface minimizes technical overhead, enabling users to focus on 🚀 innovation rather than setup tasks.

## 🌟 Features

- **Component Management**: TinyAGI Hub Streamlit allows users to ➕ add, ➖ remove, or ✏️ modify 🤖 agents, 🧩 plugins, 🛠️ tools, 📦 modules, and ⚙️ services directly through an intuitive Streamlit interface. This makes it simple to manage the diverse components that comprise the AGI system, offering a centralized point of control for all elements involved.

- **Hub Integration**: Users can easily 🌀 clone or 🔄 update components from the TinyAGI Hub Git repository, integrating them seamlessly into their current system configuration. This feature enables ongoing improvements and ensures that the system is always equipped with the latest 🛠️ tools, 🤖 agents, and ⚙️ services available in the TinyAGI ecosystem. By facilitating easy updates, AGI Hub integration fosters a collaborative and dynamic environment where new ideas and improvements can be readily adopted.

- **Task Execution**: Users can create and ▶️ execute pre-configured tasks that utilize the various components available in the system. This allows for efficient task management and 🤖 automation within the AGI environment. With pre-defined configurations, users can quickly deploy complex tasks, automate recurring workflows, and achieve a high level of operational efficiency. Task execution capabilities are particularly useful for those who need to run specific AGI experiments or recurring processes as part of their research or application.

- **Configuration Builder**: The ⚙️ Configuration Builder allows users to efficiently create or ✏️ modify configuration files that control TinyAGI's functionality. This feature provides a structured and easy-to-use approach to defining the system's behavior, making it accessible for both beginners and advanced users. Through its intuitive interface, users can adjust system parameters, modify task settings, and fine-tune other aspects of the AGI system, ensuring that it meets their unique requirements. The Configuration Builder enhances system usability by offering a straightforward way to customize AGI operations, providing flexibility for diverse use cases.

## 🛅 Installation

To run **TinyAGI Hub Streamlit** locally, please follow the instructions below:

### Prerequisites
- 🐍 **Python 3.8+**: Python is required to run the app. Ensure that your Python version is up-to-date.
- 🌀 **Git**: Git is required to clone the repository. It helps manage the codebase and ensures you have the latest updates.
- 📦 **pip (Python package manager)**: pip is necessary for installing the required Python packages from the `requirements.txt` file.

### 📂 Clone the Repository
To get started with TinyAGI Hub Streamlit, clone the repository using 🌀 Git:
```bash
$ git clone https://github.com/SullyGreene/TinyAGI-Hub-Streamlit.git
$ cd TinyAGI-Hub-Streamlit
```
This will download the latest version of the TinyAGI Hub Streamlit codebase and navigate to the project's root directory.

### 📦 Install Dependencies
Install the required Python packages using 📦 pip:
```bash
$ pip install -r requirements.txt
```
This command will install all necessary packages and dependencies required to run the app effectively.

### ⚙️ Virtual Environment Setup

Setting up a virtual environment is recommended to keep dependencies isolated from other Python projects. Use the provided startup script for your operating system to create and activate the virtual environment, install dependencies, and launch the Streamlit app.

1. **🪟 Windows**: Execute `start_app.bat`
   - This script creates a virtual environment (`tinyagi-env`), activates it, installs dependencies from `requirements.txt`, and launches the Streamlit app.
   - Double-click `start_app.bat` or run it from the command line:
     ```cmd
     start_app.bat
     ```

2. **🐧 Linux**: Execute `start_app.sh`
   - This script sets up the virtual environment, activates it, installs dependencies, and launches the app.
   - Make the script executable and run it:
     ```bash
     chmod +x start_app.sh
     ./start_app.sh
     ```

3. **🍏 macOS**: Execute `start_app.command`
   - Similar to the Linux setup, this script initializes and activates the virtual environment, installs dependencies, and starts the app.
   - Make the script executable and run it:
     ```bash
     chmod +x start_app.command
     ./start_app.command
     ```

After executing the appropriate script, open your 🌐 browser at `http://localhost:8501` to access the app. The interface will provide access to all TinyAGI features, allowing you to explore the various components and configurations available.

### ⚙️ Set Up Environment Variables
Environment variables are used to configure various settings of the app. To set up environment variables, rename `.env.example` to `.env` and configure them as needed:

```
LOG_LEVEL=INFO
```
The environment file allows you to define the log level, ensuring that you receive the appropriate amount of information about system operations.

## 🚀 Usage

The **TinyAGI Hub Streamlit** app provides an intuitive interface comprising several core sections that facilitate effective management of AGI components and configurations:

### 🔧 Component Management
- **Manage Agents**: The agent management section allows users to ➕ add, ✏️ modify, or ➖ remove 🤖 agents utilized within the TinyAGI system. Agents are core components of the AGI architecture and are responsible for executing specific tasks or processes. Managing these agents efficiently is crucial to tailoring the AGI system to meet particular needs or perform specific actions.

- **Manage Plugins**: 🧩 Plugins are auxiliary components that extend the capabilities of TinyAGI. Users can ➕ add or ➖ remove plugins through this interface, thereby enhancing or reducing functionality as required. This modular approach enables users to customize the AGI environment based on their evolving needs, providing enhanced flexibility and scalability.

- **Manage Tools**: 🛠️ Tools are external utilities that can be integrated into the TinyAGI system to provide additional capabilities. The **Manage Tools** section allows users to ➕ add, ➖ remove, or ⚙️ configure these utilities, enabling the system to leverage external resources effectively. This feature ensures that users can incorporate specialized tools as part of their AGI solutions without complex integration procedures.

- **Manage Modules**: 📦 Modules represent larger, self-contained components that add significant functionality to the TinyAGI system. Users can integrate additional modules to enhance their AGI's capabilities. The modular nature of the system supports rapid prototyping, experimentation, and seamless addition of new features.

- **Manage Services**: ⚙️ Services refer to background processes that operate continuously to support AGI tasks. The **Manage Services** section allows users to ▶️ start, ⏹️ stop, or ⚙️ configure these services, providing control over the system's underlying processes. Proper management of services ensures optimal performance and system reliability.

### ⚙️ Configurations & Execution
- **📊 Dashboard**: The Dashboard offers a comprehensive overview of TinyAGI Hub activities, including the system's operational status and recent activities. It serves as a monitoring tool that provides insights into ongoing processes, allowing users to keep track of their AGI environment's health and activity.

- **🛠️ Configuration Builder**: The ⚙️ Configuration Builder provides a user-friendly interface for creating or ✏️ editing configuration files. These files determine the behavior of the AGI system, and the builder simplifies the process of defining system parameters, task settings, and more. This feature is vital for users who need to tailor the system to specific requirements without manually editing configuration files.

- **🚀 Task Execution**: Users can define tasks within the system configuration and execute them via the **Task Execution** section. This allows for automated, efficient task management within the AGI environment. Tasks may involve multiple components and require precise coordination, which is facilitated by the streamlined execution interface.

- **🔗 Hub Integration**: The **Hub Integration** section enables users to explore new 🤖 agents, 🧩 plugins, 🛠️ tools, 📦 modules, and ⚙️ services available from the TinyAGI Hub. Users can then import these directly into their configuration, ensuring that they have access to the latest advancements and updates within the TinyAGI ecosystem.

## 🤝 Contributing
Contributions are highly valued, as they are essential for continuous improvement and evolution of TinyAGI Hub Streamlit. If you wish to enhance this project, please 🍴 fork the repository, make your changes, and submit a 🔄 pull request. You can also report 🐞 issues or discuss ideas by submitting an issue through GitHub. We welcome any form of contribution, including improving the 📜 documentation, fixing 🐛 bugs, adding new ✨ features, providing feedback on current functionality, 🧪 testing, and suggesting new feature ideas.

### 🔄 Contribution Steps
1. **🍴 Fork the repository**: Forking allows you to create a personal copy of the repository where you can make your changes.
2. **🛠️ Create a new branch**: Create a dedicated branch for your feature or bug fix (`git checkout -b feature-branch`). This ensures that your changes are isolated from the main codebase.
3. **✏️ Make your changes**: Implement the improvements, whether they are new features, bug fixes, or updates to the documentation.
4. **✅ Commit your changes**: Once you have completed the changes, commit them with a meaningful message (`git commit -m 'Add new feature'`). This helps maintain a clear project history.
5. **⬆️ Push to the branch**: Push your changes to your GitHub repository (`git push origin feature-branch`).
6. **📬 Open a Pull Request**: Submit a pull request to the main repository, and the project maintainers will review your changes.

## ⚠️ License
This project is licensed under the ⚖️ Apache License, Version 2.0. The Apache License is a permissive license that allows for significant flexibility while maintaining proper attribution. See the [📜 LICENSE](LICENSE) file for additional details regarding permissions and limitations.

## 🤞 Acknowledgements
- **[Streamlit](https://streamlit.io/)**: The user-friendly and interactive UI framework provided by Streamlit plays a crucial role in enabling the ease of use of TinyAGI Hub Streamlit. Streamlit’s ability to create sophisticated interfaces without requiring extensive front-end development greatly enhances the accessibility of the AGI system.
- **[TinyAGI Hub](https://github.com/SullyGreene/TinyAGI-Hub)**: The modular AGI components available through the TinyAGI Hub form the core building blocks of this system, providing a solid foundation for users to create and extend AGI functionality in a meaningful way.

## 🛠️ Troubleshooting
- **🔗 Hub Integration Components Not Visible**: If the **Hub Integration** components are not appearing, verify that the repository has been successfully cloned and that the necessary directories are in place.
- **⚙️ Environment File Issues**: Ensure that the `.env` file is properly configured for logging and other settings. Missing or misconfigured environment variables can lead to unexpected behavior.
- **📦 Dependency Issues**: If you encounter issues with missing packages or dependencies, ensure that all required Python packages are installed by running `pip install -r requirements.txt`.
- **🚫 Permission Denied on macOS/Linux**: If you receive a "Permission Denied" error when trying to execute scripts, ensure the script has executable permissions (`chmod +x script_name.sh`).

## 🛠️ Contact
For any inquiries or support, feel free to reach out via the repository's [📨 Issues page](https://github.com/SullyGreene/TinyAGI-Hub-Streamlit/issues). We encourage you to use the Issues page not only for reporting bugs but also for suggesting enhancements and providing feedback that can improve the project. Community collaboration is key to advancing TinyAGI Hub Streamlit.

Happy building with **TinyAGI Hub Streamlit**! 🚀


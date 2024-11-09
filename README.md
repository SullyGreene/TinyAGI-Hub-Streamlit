# 🤖 TinyAGI Hub Streamlit

Welcome to **TinyAGI Hub Streamlit** — a user-friendly interface built with 🦄 Streamlit to manage and explore the dynamic and modular components of the **TinyAGI Hub**. With this app, you can seamlessly manage 🤖 agents, 🧩 plugins, 🛠️ tools, 📦 modules, and ⚙️ services that make up TinyAGI. You can also integrate new components from the TinyAGI Hub, making it easier than ever to customize and expand your AGI system.

## 🌟 Features

- **🔧 Manage Components**: ➕ Add, ➖ remove, or ✏️ modify 🤖 Agents, 🧩 Plugins, 🛠️ Tools, 📦 Modules, and ⚙️ Services directly through the Streamlit interface.
- **🔗 Hub Integration**: 🌀 Clone or 🔄 update components from the TinyAGI Hub Git repository, and integrate them into your current configuration.
- **🚀 Task Execution**: 📝 Create and ▶️ execute pre-configured tasks with the components you've configured.
- **🛠️ Configuration Builder**: 🛠 Easily create or modify configuration files to control TinyAGI's behavior.

## 📥 Installation

To run **TinyAGI Hub Streamlit** locally, follow these steps:

### Prerequisites
- 🐍 Python 3.8+
- 🌀 Git
- 📦 pip (Python package manager)

### 📂 Clone the Repository
```bash
$ git clone https://github.com/SullyGreene/TinyAGI-Hub-Streamlit.git
$ cd TinyAGI-Hub-Streamlit
```

### 📦 Install Dependencies
Install all required Python packages:
```bash
$ pip install -r requirements.txt
```

### ⚙️ Set Up Environment Variables
Rename `.env.example` to `.env` and configure your environment variables as needed:

```
LOG_LEVEL=INFO
```

### ▶️ Run the Streamlit App
Use the following command to run the Streamlit app:
```bash
$ streamlit run app.py
```

After executing the above command, you can open your 🌐 browser at `http://localhost:8501` to use the application.

## 🚀 Usage

The **TinyAGI Hub Streamlit** app provides an intuitive interface with several key sections:

### 🔧 Manage Components
- **🧠 Manage Agents**: ➕ Add, ✏️ modify, or ➖ remove 🤖 Agents used in the TinyAGI system.
- **🔌 Manage Plugins**: Manage 🧩 Plugins that extend TinyAGI's capabilities.
- **🛠️ Manage Tools**: ➕ Add or ➖ remove 🛠️ external utilities used by TinyAGI.
- **📦 Manage Modules**: Integrate additional 📦 modules for added functionality.
- **⚙️ Manage Services**: ▶️ Start, ⏹️ stop, or ⚙️ configure background services for TinyAGI.

### ⚙️ Configurations & Execution
- **📊 Dashboard**: Overview of TinyAGI Hub activities, 🖥 system status, and recent activity.
- **🛠️ Configuration Builder**: 🛠 Easily create or edit configuration files to control system behavior.
- **🚀 Task Execution**: ▶️ Execute tasks predefined in your configuration.
- **🔗 Hub Integration**: 🌀 Explore new 🤖 Agents, 🧩 Plugins, 🛠️ Tools, 📦 Modules, and ⚙️ Services from the TinyAGI Hub. 📥 Import them directly into your configuration.

## 🧑‍💻 Contributing
Contributions are 💖 welcome! If you'd like to improve this project, please 🍴 fork the repository and create a 🔀 pull request. You can also 📝 submit an issue to discuss ideas or report 🐛 bugs.

### 🚀 Contribution Steps
1. 🍴 Fork the repository.
2. 🏗️ Create a new branch (`git checkout -b feature-branch`).
3. ✏️ Make your changes.
4. ✅ Commit your changes (`git commit -m 'Add new feature'`).
5. ⬆️ Push to the branch (`git push origin feature-branch`).
6. 📬 Open a Pull Request.

## ⚠️ License
This project is licensed under the ⚖️ Apache License, Version 2.0. See the [📜 LICENSE](LICENSE) file for more details.

## 🤝 Acknowledgements
- **[Streamlit](https://streamlit.io/)** for making the 🖼️ UI fast and intuitive.
- **[TinyAGI Hub](https://github.com/SullyGreene/TinyAGI-Hub)** for providing modular 🤖 AGI components to integrate and manage.

## 🛠️ Troubleshooting
- If the **🔗 Hub Integration** components are not visible, make sure the repository is successfully cloned and the directory exists.
- 🔍 Check that the `.env` file is properly configured for logging.

## 📫 Contact
For any inquiries or support, feel free to reach out via the repository's [📨 Issues page](https://github.com/SullyGreene/TinyAGI-Hub-Streamlit/issues).

Happy building with **TinyAGI Hub Streamlit**! 🚀


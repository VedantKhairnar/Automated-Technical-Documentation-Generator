Automated Technical Documentation Generator
===========================================

Overview
--------

The **Automated Technical Documentation Generator** is a Python-based tool designed to parse Swagger documentation and generate structured, clear API documentation. The tool enhances the generated documentation using various AI services, making it more concise and user-friendly. It also extracts test cases from Python test files to provide a comprehensive overview of API behavior.

Features
--------

-   **Parse Swagger Files**: Load and parse Swagger JSON files to extract metadata and API paths.
-   **Generate Documentation**: Automatically create formatted API documentation in Markdown format.
-   **Extract Test Information**: Analyze Python test files to summarize test functions and their expected behaviors.
-   **Enhance Documentation**: Utilize AI services (OpenAI, Gemini, Fynd Copilot) to refine the generated documentation.
-   **Environment Variable Support**: Load API keys and other configurations from a `.env` file for secure management.

Requirements
------------

-   Python 3.6 or later
-   Required Python packages:
    -   `requests`
    -   `json`
    -   `openai`
    -   `ast`
    -   `logging`
    -   `python-dotenv`
    -   `google.generativeai`

You can install the required packages using:


```bash
pip install -r requirements.txt
```

Setup
-----

1.  Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  Create a `.env` file in the root directory of the project and add your API keys:

    ```
    OPENAI_API_KEY=your_openai_api_key
    GEMINI_API_KEY=your_gemini_api_key
    FYND_API_KEY=your_fynd_api_key
    ```

3.  Ensure you have defined the Swagger JSON file and Python test files in the main.


Contributing
------------

Contributions are welcome! If you have suggestions for improvements or want to report a bug, please open an issue or submit a pull request.

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Make your changes and commit them (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/YourFeature`).
5.  Open a pull request.

Contact
-------

For questions or feedback, feel free to create an issue in the GitHub repository.

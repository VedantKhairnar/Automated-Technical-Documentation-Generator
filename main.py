import requests, json, os, openai, ast, logging
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

###------ Data Parsing -----
def parse_swagger_metadata(swagger_data):
    """
    Extracts metadata from the Swagger documentation.

    Args:
        swagger_data (dict): The Swagger data as a dictionary.

    Returns:
        dict: A dictionary containing extracted metadata, including title, version, 
              description, termsOfService, contact, and license information.
    """

    info = swagger_data.get('info', {})
    metadata = {
        'title': info.get('title', 'No title provided'),
        'version': info.get('version', 'No version provided'),
        'description': info.get('description', 'No description provided'),
        'termsOfService': info.get('termsOfService', 'No terms provided'),
        'contact': info.get('contact', {}),
        'license': info.get('license', {})
    }
    return metadata

def parse_parameters(params, swagger_data):
    """
    Extracts parameter details from the Swagger data, resolving any references.

    Args:
        params (list): A list of parameter objects to be parsed.
        swagger_data (dict): The entire Swagger data as a dictionary, used to resolve references.

    Returns:
        list: A list of dictionaries, each containing the following information for a parameter:
            - name (str): The name of the parameter.
            - in (str): The location of the parameter (e.g., 'query', 'header', 'path', etc.).
            - description (str): A description of the parameter, or 'No description' if not provided.
            - required (bool): Whether the parameter is required (default is False).
            - type (str): The data type of the parameter (default is 'N/A' if not provided).
            - format (str): The format of the parameter (default is 'N/A' if not provided).
    """

    parsed_params = []
    for param in params:
        if '$ref' in param:
            param = resolve_ref(param['$ref'], swagger_data)

        param_details = {
            'name': param.get('name'),
            'in': param.get('in'),
            'description': param.get('description', 'No description'),
            'required': param.get('required', False),
            'type': param.get('type', 'N/A'),
            'format': param.get('format', 'N/A')
        }
        parsed_params.append(param_details)
    
    return parsed_params


def resolve_ref(ref, swagger_data):
    """
    Resolves a reference in the Swagger document to get the actual parameter or schema details.

    Args:
        ref (str): The reference string to resolve.
        swagger_data (dict): The parsed Swagger data.

    Returns:
        dict: The resolved parameter or schema details.
    """

    if ref.startswith('#/'):
        keys = ref[2:].split('/')
        for key in keys:
            swagger_data = swagger_data.get(key, {})
        return swagger_data
    else:
        # Handle external references (implement as needed)
        return {}

def parse_swagger(swagger_file):
    """
    Parses the Swagger file and extracts relevant information.

    Args:
        swagger_file (str): The path to the Swagger file.

    Returns:
        tuple: A tuple containing metadata (dict) and parsed paths (dict).
    """

    with open(swagger_file, 'r') as f:
        swagger_data = json.load(f)

    # Extract metadata
    metadata = parse_swagger_metadata(swagger_data)

    # Parse paths
    paths = swagger_data.get('paths', {})
    parsed_paths = {}
    for path, methods in paths.items():
        parsed_methods = {}
        for method, details in methods.items():
            parsed_params = []
            if 'parameters' in details:
                parsed_params = parse_parameters(details['parameters'], swagger_data)

            parsed_methods[method] = {
                'description': details.get('description', 'No description'),
                'parameters': parsed_params,
                'responses': details.get('responses', {})
            }
        parsed_paths[path] = parsed_methods

    return metadata, parsed_paths

###------ Generate Intermediate Documentation -----
def generate_documentation(metadata, paths):
    """
    Generates documentation from the parsed data.

    Args:
        metadata (dict): The metadata containing title, version, and description.
        paths (dict): The parsed paths and their corresponding methods.

    Returns:
        str: A formatted string representing the generated documentation.
    """

    documentation = f"# {metadata['title']} (v{metadata['version']})\n\n"
    documentation += f"{metadata['description']}\n\n"

    for path, methods in paths.items():
        documentation += f"## Path: {path}\n"
        for method, details in methods.items():
            documentation += f"### Method: {method.upper()}\n"
            documentation += f"Description: {details['description']}\n"
            documentation += "Parameters:\n"
            for param in details['parameters']:
                documentation += f"- {param['name']} ({param['in']}): {param['description']} (Required: {param['required']}, Type: {param['type']}, Format: {param['format']})\n"
            documentation += "Responses:\n"
            for status, response in details['responses'].items():
                documentation += f"- {status}: {response.get('description', 'No description')}\n"
            documentation += "\n"
    export_documentation(documentation,"intermediate.md")
    return documentation


###------ Test_api File analysis code -----

def extract_test_info(test_file):
    """
    Extracts test function names, descriptions (from docstrings), and expected outcomes
    (assertions or print statements) from a Python test file.

    Args:
        test_file (str): The path to the Python file containing the test functions (e.g., 'test_api.py').

    Returns:
        list: A list of dictionaries, where each dictionary contains the following information for a test function:
            - name (str): The name of the test function (should start with 'test_').
            - description (str): The docstring of the test function, or 'No description provided' if no docstring exists.
            - expected_output (list): A list of expected outcomes, including assertions or print statements. If no assertions or print statements are present, it defaults to 'No explicit output provided'.
    """

    with open(test_file, 'r') as file:
        file_content = file.read()

    # Parse the file content into an abstract syntax tree (AST)
    tree = ast.parse(file_content)
    test_summaries = []

    # Traverse the AST nodes
    for node in ast.walk(tree):
        # Look for function definitions
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test_"):
            test_name = node.name
            docstring = ast.get_docstring(node) or "No description provided."

            # Extract assertions or any print statements for expected output
            expected_output = []
            for sub_node in ast.walk(node):
                if isinstance(sub_node, ast.Assert):
                    expected_output.append(ast.dump(sub_node.test))
                elif isinstance(sub_node, ast.Call) and isinstance(sub_node.func, ast.Name) and sub_node.func.id == 'print':
                    # Capture print statement output for demonstration purposes
                    expected_output.append(ast.dump(sub_node))

            # Combine test details into a summary
            summary = {
                'name': test_name,
                'description': docstring,
                'expected_output': expected_output if expected_output else ["No explicit output provided."]
            }
            test_summaries.append(summary)

    return test_summaries

def generate_test_summary_prompt(test_summaries):
    """
    Generates a formatted string summarizing the test functions and their expected behavior.

    Args:
        test_summaries (list): A list of dictionaries containing details about each test function.
                               Each dictionary should include the test's name, description, and expected output.

    Returns:
        str: A formatted string summarizing the test functions, including their names, descriptions, and expected outputs.
    """

    prompt_summary = "\n### Unit Test Summary:\n\n"
    
    for test in test_summaries:
        prompt_summary += f"- **{test['name']}**: {test['description']}\n"
        prompt_summary += f"  - Expected output: {', '.join(test['expected_output'])}\n\n"
    return prompt_summary.strip()

def enhance_prompt_with_tests(test_file, original_prompt):
    """
    Enhances the generated documentation by summarizing test cases.

    Args:
        test_file (str): The path to the test file.
        documentation (str): The existing documentation string to enhance.

    Returns:
        str: The enhanced documentation including test summaries.
    """

    test_summaries = extract_test_info(test_file)
    test_summary_prompt = generate_test_summary_prompt(test_summaries)

    # Append the test summary to the original prompt
    enhanced_prompt = f"{original_prompt}\n\n{test_summary_prompt}"

    return enhanced_prompt


###------ Improvise Documentation with GenAI -----

def openai_ai_component(prompt, documentation): ## Not tested
    """
    Processes the documentation through the OpenAI API for improvements.

    Args:
        documentation (str): The documentation string to process.
        model (str): The OpenAI model to use for processing.

    Returns:
        str: The improved documentation generated by the AI model.
    """

    try:
        api_key = os.getenv('OPENAI_API_KEY')
        
        if not api_key:
            print("API key not found. Please set the 'OPENAI_API_KEY' environment variable.")
            return documentation
        openai.api_key = api_key

        response = openai.Completion.create(
                model="gpt-3.5-turbo", 
                prompt=prompt,
                max_tokens=1500,        # Adjust based on your needs
                temperature=0.7,        # Control creativity
                n=1,                    # Number of responses to return
                stop=None             
            )

        # Extract the content from the API response
        improved_documentation = response['choices'][0]['message']['content']
    
        return improved_documentation.strip()  # Return the cleaned output
    except:
        logging.error("Error occured while running the OpenAI. Return default documentation")
        return documentation

def gemini_ai_component(prompt, documentation):
    """
    Processes the documentation through the Gemini API for improvements.

    Args:
        documentation (str): The documentation string to process.

    Returns:
        str: The improved documentation generated by the Gemini API.
    """

    try:
        api_key = os.getenv('GEMINI_API_KEY')
        
        if not api_key:
            print("API key not found. Please set the 'GEMINI_API_KEY' environment variable.")
            return documentation
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        improved_documentation = response.text
        return improved_documentation.strip()  # Return the cleaned output
    except Exception as e:
        logging.error(f"Error occurred while running the Gemini API: {e}. Returning default documentation.")
        return documentation

def fynd_copilot_component(prompt, documentation): 
    """
    Processes the documentation through the Fynd Copilot API for enhancements.

    Args:
        documentation (str): The documentation string to process.

    Returns:
        str: The enhanced documentation generated by the Fynd Copilot API.
    """

    api_key = os.getenv("FYND_API_KEY") 

    if not api_key:
        return "API key is not set. Please check your .env file."
    # Call Fynd Copilot API
    try:
        url = "https://api.fynd.com/copilot" 
        headers = {
            "Authorization": "Bearer {FYND_API_KEY}", 
            "Content-Type": "application/json"
        }
        data = {
            "prompt": prompt,
            "max_tokens": 1500  # Adjust based on your needs
        }
        response = {'data':{'text':prompt}}
        # response = requests.post(url, json=data, headers=headers)

        improved_documentation = response.get('data', {}).get('text', 'No improvement provided.')
        return improved_documentation.strip()  # Return cleaned response

    except Exception as e:
        logging.error(f"An error occurred while calling the Fynd Copilot API: {str(e)}")
        return documentation

def ai_component(documentation, ai):
    """
    Integrates AI processing for enhancing API documentation based on the user's choice of AI.

    Args:
        documentation (str): The existing API documentation to be improved.
        ai (str): The AI service to be used for processing, such as 'OpenAI', 'Fynd', or 'Gemini'.

    Returns:
        str: The improved API documentation or an error message if an invalid AI service is selected.
    """

    prompt = (
        """Please review and enhance the following API documentation with a focus on clarity, conciseness, and structure. Ensure the documentation includes the following elements:

        1.  **Purpose Explanation**: Begin with a brief overview of the module or feature, explaining its purpose and key functionalities. Keep this detailed.

        2.  **Functionality Summary**: Summarize what the module or feature does based on unit tests, including any important behaviors or edge cases that should be highlighted.

        3.  **Onboarding Guide**: Provide clear and concise explanations and guidance tailored for developers who are onboarding onto the project. Include any essential information or tips that can help them effectively understand and utilize the API.
        
        4.  **Key API Endpoints**: For each API endpoint, provide:

            -   The endpoint path and HTTP method.
            -   A brief description of its functionality.
            -   A list of parameters, specifying:
                -   The name, type, required status, and description of each parameter.
            -   Possible responses with status codes and brief explanations.
        5. **Information around status codes: 
        6. Provide a proper ending note.
        Make sure the final output is structured in a coherent and organized manne, to facilitate readability and integration into the existing documentation."""
        f"{documentation}\n\n" + "\n\nPlease provide the entire improved documentation in markdown format, from start to end in a single markdown."
    )

    if ai.lower() == 'openai':
        logging.info("Processing documentation using OpenAI...")
        return openai_ai_component(prompt, documentation)

    elif ai.lower() == 'gemini':
        logging.info("Processing documentation using Gemini AI...")
        return gemini_ai_component(prompt, documentation)

    elif ai.lower() == 'fynd':
        logging.info("Processing documentation using Fynd Copilot...")
        return fynd_copilot_component(prompt, documentation)

    else:
        logging.error(f"Unsupported AI service: {ai}")
        return documentation

###------ Documentation Export -----

def export_documentation(documentation, filename):
    """
    Exports the final documentation to a specified markdown file.

    Args:
        documentation (str): The documentation string to export.
        file_path (str): The file path where the documentation will be saved.
    """

    with open(filename, 'w') as f:
        f.write(documentation)

if __name__ == "__main__":
    # Define file paths for the Swagger and test files
    swagger_file = "swagger.json"
    test_file = "test_api.py"
    output_file = "documentation.md"
    # Parse Swagger file and generate initial documentation
    metadata, paths = parse_swagger(swagger_file)
    logging.info("Swagger File Parsed")
    documentation = generate_documentation(metadata, paths)
    logging.info("Base Documentation Generated")
    # Enhance documentation with test summaries
    documentation_with_tests = enhance_prompt_with_tests(test_file, documentation)
    logging.info("Updated Documentation with Test Summaries")
    # Process the documentation through the AI component for improvements
    final_documentation = ai_component(documentation_with_tests, ai='gemini') # Gemini Tested
    logging.info("Improvised Documentation using GenAI")
    # Export the final documentation to a markdown file
    export_documentation(final_documentation, 'documentation.md')
    logging.info("Documentation Exported")
    # Print the final documentation to console
    # print(final_documentation)
    logging.info("Documentation stored in %s", output_file)

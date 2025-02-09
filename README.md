# Langflow Translation Component

A flow and a custom component to translate text to a certain language in Langflow.

With this repository, you can create a easy-to-use, reusable translation component for Langflow. You will set up at least two things: A flow that contains various components needed for the translation, as well as a custom component that will request the flow via it's local API, setting the text to be translated and the target language.

> Input text is limited to ~900 characters.

The current version is 0.4. 

## Files

### Flow

- **File:** `* Flow`
- **Description:** This flow creates a translation of a given text into a specified language. It uses the Model component `Ollama` and the model `7shi/mistral-small:22b-instruct-2409-iq3_M`. These are required but can be replaced with another Model component or model if desired.

### Component

- **File:** `* Component`
- **Description:** This is the code for a custom component that interacts with the local API of the flow. It allows you to specify the input text and the output language. You will have to update the local endpoint URL to the flow as well as the id of the Output Language component; both configurable at the top of the code. The output of the component is a `Message`.

### Test

- **File:** `* Test`
- **Description:** This Langflow serves as a reference implementation, utilizing the custom component to test and demonstrate its functionality.

## Usage

### Requirements

Hard

- Langflow version 1.0 or higher

Soft

- Local installation of "Ollama"
- Running LLM "7shi/mistral-small:22b-instruct-2409-iq3_M" 
  (or an alternative model like "aya 23" or "llama 3")

### Setup

1. Set up the Flow
   * Ensure you have Langflow version 1.0 or higher installed.
   * Import the `* Flow` file to your Langflow projects.
   * Replace the Model component and-or the model as needed.
2. Create the Component
   * Create a custom component using the code from the `* Component` file somewhere.
   * Update the local endpoint URL in the `* Component` file to point to your flow's API.
   * Update the id of the Output Language component to address in your local flow.
   * Save the component.
3. Set up the Test (optional)
   * Import the `* Test` file to your Langflow projects.
   * Choose a language to translate to in the `Translation *` component.
   * Enter text to translate in the Playground.

## Appendix

### Notes

See something similar discussed [here](https://www.youtube.com/watch?v=g_1gNmWARqY).

### License

This project is licensed under the MIT License.

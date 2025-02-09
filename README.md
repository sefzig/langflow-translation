# Langflow Translation Component

A Flow and a Custom Component to translate text to a certain language in Langflow.

With this repository, you can create a easy-to-use, reusable translation component for Langflow. You will set up at least two things: A `Flow` that contains various components needed for the translation, as well as a custom `Component` that will request the Flow via it's local API, setting the text to be translated and the target language.

> Input text is limited to ~900 characters.

The current version is 0.3. 

## Files

### Flow

- **File:** `* Flow`
- **Description:** This Flow creates a translation of a given text into a specified language. It uses the Model component "Ollama" and the model "mistral small 22b". These are required but can be replaced with another Model component or model if desired.

### Component

- **File:** `* Component`
- **Description:** This is the code for a custom `Component` that interacts with the local API of the Flow. It allows you to specify the input text and the output language. You will have to update the local endpoint URL to the Flow. The output of the `Component` is a `Message`.

### Test

- **File:** `* Test`
- **Description:** This Langflow serves as a reference implementation, utilizing the custom `Component` to test and demonstrate its functionality.

## Usage

### Requirements

Hard

- Langflow version 1.0 or higher

Soft

- Local installation of "Ollama"
- Running LLM "mistral small 22b" (or an alternative model)

### Setup

1. Set up the Flow
   * Ensure you have Langflow version 1.0 or higher installed.
   * Import the `* Flow` file to your Langflow projects.
   * Replace the Model component and-or the model as needed.
2. Create the Component
   * Create a custom `Component` using the code from the `* Component` file somewhere.
   * Update the local endpoint URL in the `* Component` file to point to your Flow's API.
   * Save the `Component`.
3. Set up the Test (optional)
   * Import the `* Test` file to your Langflow projects.
   * Choose a language to translate to in the `Translation *` component.
   * Enter text to translate in the Playground.

## License

This project is licensed under the MIT License.

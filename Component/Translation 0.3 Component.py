# Helper: Translation 0.3

from langflow.custom import Component
from langflow.io import MessageTextInput, DropdownInput, Output
from langflow.schema.message import Message
import requests
import json
import numpy as np

class CustomComponent(Component):
    display_name = "Translation 0.3"
    description = "Translate the Input Text to the specified Output Language."
    documentation: str = "http://docs.langflow.org/components/custom"
    icon = "languages"
    name = "Translation03"
    HelperUrl = "http://127.0.0.1:7860/api/v1/run/da2c087a-b26c-460d-9e8a-1e095c394058?stream=false"

    inputs = [
        MessageTextInput(
            name="InputText",
            display_name="Input Text",
            value='Hola mundo',
            info="The string to translate"
        ),
        DropdownInput(
            name="OutputLanguage",
            display_name="Output Language",
            options=["English", "German", "Mandarin", "Spanish"],
            value="English",
            info="The language to translate to",
        ),
    ]

    outputs = [
        Output(display_name="Response", name="output", method="build_output"),
    ]

    def reduce_dimensions(self,vector, target_dim=1024):
        if len(vector) == target_dim:
            return vector
        elif len(vector) > target_dim:
            return vector[:target_dim]
        else:
            return vector + [0] * (target_dim - len(vector))
        
    def build_output(self) -> Message:
        url = self.HelperUrl
        method = "POST"
        body = '{ "input_value": "' + self.InputText + '", "input_type": "chat", "output_type": "chat", "tweaks": { "TextInput-Svbb0": { "input_value": "' + self.OutputLanguage + '" } } }'
        
        try:
            
            json_body = json.loads(body)
            
            response = requests.request(
                method=method,
                url=url,
                json=json_body,
                headers={
                    "Content-Type": "application/json"
                }
            )
            
            response.raise_for_status()
            content = response.json()
            translation = content["outputs"][0]["outputs"][0]["results"]["message"]["data"]["text"]
            output_str = translation
            
        except json.JSONDecodeError:
            output_str = "Invalid JSON body: " + body
        except requests.RequestException as e:
            output_str = "error" + str(e)

        data = Message(text=output_str)
        self.status = data
        return data
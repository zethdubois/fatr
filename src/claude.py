# src/claude.py

import ipywidgets as widgets
from IPython.display import display
import anthropic
import os

api_key = os.getenv('ANTHROPIC_API_KEY')
client = anthropic.Anthropic(api_key=api_key)

# Function to check the API key and run different logic
def verify_api_key():
    global api_key  # Reference the global variable if you plan to modify it inside this function
    if api_key is None:
        print("API key is not set. Make sure you have env vars setup before running jupyter")
        # Place your alternative logic here
        # For example, asking for the API key via input or widgets
        # api_key = input("Please enter your API key: ")  # Be cautious using input for sensitive data
    else:
        print("API key is set. Proceeding with normal operation.")
        print("Provide instructions in conversational text, and a LaTeX template for the analysis output")
        # Normal operation logic here

def condition_claude():
    verify_api_key()
    output = widgets.Output()

    
    def on_submit_button_clicked(b):
        with output:
            output.clear_output()
            # Assuming `summarize_results` function and `aov_dict` are defined elsewhere
            summary_text = summarize_results(aov_dict, marginal_means)
            
            # Use the dropdown's value directly to specify the model
            model = dropdown.value
            
            # Proceed with your anthropic API call, inserting the `summary_text` into the 'text' field
            # Note: Make sure you have the `anthropic` library and your API key configured as needed
            api_key = os.getenv('ANTHROPIC_API_KEY')
            client = anthropic.Anthropic(api_key=api_key)
            
            # Example call (adjust according to the actual anthropic API client usage)
            response = client.some_api_call_function(model=model, text=summary_text)
            
            # Display the response or any other output you wish to show
            print("API Response:", response)


    template_textarea = widgets.Textarea(
        placeholder='Enter LaTeX template...',
        description='Template:',
        layout={'width': '100%', 'height': '300px'}
    )

    instructions_textarea = widgets.Textarea(
        placeholder='Enter written instructions...',
        description='Instructions:',
        layout={'width': '100%', 'height': '300px'}
    )

    # Dropdown widget for selection
    dropdown = widgets.Dropdown(
    options=[
        ('Claude Instant', 'claude-instant-1.2'), 
        ('Claude 2.1', 'claude-2.1'), 
        ('Claude 3 Opus', 'claude-3-opus-20240229')
    ],
        value='claude-instant-1.2',  # Default value
        description='Model:',
        disabled=False,
    )

    submit_button = widgets.Button(
        description='Submit',
        button_style='success',
        tooltip='Click to submit'
    )
    
    # Arrange the text areas horizontally
    text_area_box = widgets.HBox([instructions_textarea,template_textarea])
    
    # Arrange the dropdown and submit button horizontally
    controls_box = widgets.HBox([dropdown, submit_button])
    
    # Stack the text areas and controls vertically
    final_layout = widgets.VBox([text_area_box, controls_box])
    
    # Display the final layout
    display(final_layout)

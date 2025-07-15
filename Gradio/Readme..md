Gradio
│
├── Interface (gr.Interface)
│   ├── fn: function to wrap
│   ├── inputs: UI components for inputs (Textbox, Slider, Image, etc.)
│   ├── outputs: UI components for outputs
│   └── live: for real-time (streaming) apps
│
├── Components
│   ├── Textbox, Image, Slider, Dropdown, Checkbox, etc.
│   └── Can be combined in lists for multi-input/output
│
├── Launching
│   ├── .launch() — starts the UI
│   └── share=True — creates a public link
│
├── Advanced
│   ├── Blocks — for custom layouts and control
│   ├── Events — button clicks, change triggers
│   ├── State — session-based memory
│   └── Themes — styling the UI

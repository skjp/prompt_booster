# Prompt Booster - SPOUT Addon

A SPOUT addon module that enhances and improves text prompts to make them more comprehensive, precise, and effective.

## 🌟 Features

- **Comprehensive Prompt Analysis**: Examines core intent and identifies gaps in clarity
- **Strategic Enhancement**: Adds context, specifications, and requirements
- **Quality Assurance**: Ensures clarity, precision, and completeness
- **Multiple Spoutlet Support**: Includes default and experimental enhancement strategies
- **GUI and CLI Integration**: Supports both graphical and command-line interfaces

## 🚀 Installation

### Prerequisites
- SPOUT framework installed
- Python 3.x
- AutoHotkey v2 (for GUI features on Windows)

### Setup

1. Create the addon directory:
```bash
cd spout_workspace/spout/addons
mkdir prompt_booster
```

2 Clone the addon repository:
```bash
cd prompt_booster
git clone https://github.com/skjp/prompt_booster.git .
```

3. Register the addon:
- Run `spout/shared/IncludesGenerator.ahk` to update SPOUT's addon registry
- Or restart SPOUT using the QuickStart script

## 🛠️ Usage

### Command Line Interface
```bash
# Basic prompt enhancement
spout prompt_booster "Write a story about a dragon"
# Process clipboard content
spout prompt_booster
```

### GUI Interface (Windows)
The addon integrates with SPOUT's base GUI system, providing:
- Text input/output fields
- Progress tracking
- Spoutlet selection dropdown
- Copy/paste functionality
- Sound effect feedback

Access via:
- Hotkey example console command `Capslock + F1`
- SPOUT context menu
- Direct script execution

## 🔧 Configuration

### Spoutlet Templates
The addon includes one enhancement strategy prompt template:

- **Default**: Comprehensive prompt improvement with detailed requirements
- 
Customize templates in `prompt_booster_plugins/[spoutlet]/prompt.txt`

### Execution Settings
Adjust in `config.json`:
- Token limits
- Temperature
- Top-p sampling
- Presence/frequency penalties

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Add your custom spoutlet template in `prompt_booster_plugins/`
4. Update tests in `tests/test_cases.json`
5. Submit a Pull Request

## 📝 Technical Details

### Integration
The addon uses SPOUT's `BaseGui.ahk` shared library for:
- Window management
- Progress tracking
- Clipboard handling
- Theme support
- Event handling

### Script Components
- `cli_info.py`: Defines CLI interface and help documentation
- `script.ahk`: Implements GUI integration and hotkey support
- `prompt.txt`: Contains enhancement strategy templates
- `config.json`: Spoutlet-specific settings

## 🌱 Origins

Prompt Booster began as a tool to improve AI prompt engineering workflows, helping users create more effective and comprehensive prompts for various AI applications. It also serves as the first example addon for the SPOUT framework. 

## 📚 Documentation

For more detailed information:
- [SPOUT Module Standard Documentation](https://spout.dev/basics/modules)
- [Addon Development Guide](https://spout.dev/essentials/addons)
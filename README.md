# ChatSense - WhatsApp Chat Analyzer and Behavior Predictor

## Overview

This machine learning model aims to provide a simple but powerful tool for analyzing WhatsApp chat data. By utilizing  some machine learning techniques, it not only provides insights into chat but in future i will make it to predict behaviors and moods based on the conversation history.

## Features

- **Chat Analysis**: Visualizes various aspects of WhatsApp chats, including message frequency and word usage.
- **Mood Prediction**: Uses machine learning to predict the mood or behavior of participants based on chat history.
- **Customizable Visualization**: Offers a range of visualization options using Matplotlib, Seaborn, and WordCloud.
- **Data Preprocessing**: Extracts URLs, emojis, and cleans text using regular expressions.
- **Easy Integration**: Can be integrated into existing projects or used as a standalone tool.

## Requirements

- Python 3.x
- Dependencies:
  - `matplotlib`
  - `pandas`
  - `seaborn`
  - `urlextract`
  - `emoji`
  - `wordcloud`

## Usage

1. **Install Dependencies**: Ensure Python 3.x is installed. Then, install the required packages:
   ```bash
   pip install matplotlib pandas seaborn urlextract emoji wordcloud
   ```

2. **Prepare Data**: Export your WhatsApp chat history as a text file and place it in the `data_chats` folder. Update the `file` variable in `app.py` (line 7) with the relative path to your chat file.

3. **Run the Analyzer**: Execute the script to analyze your WhatsApp chat data:
   ```bash
   python app.py
   ```

4. **Explore Results**: Review the generated visualizations and insights. Customize them as needed.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/new-feature`.
3. Make your changes.
4. Commit your changes: `git commit -am 'Add new feature'`.
5. Push to the branch: `git push origin feature/new-feature`.
6. Create a Pull Request.

## Contact

For inquiries or feedback, please contact [Satyam Kumar](mailto:isatyamks@gmail.com) or connect on GitHub or LinkedIn.
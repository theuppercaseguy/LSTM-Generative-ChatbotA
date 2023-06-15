# Text Generation with LSTM Neural Network

This repository contains code for training an LSTM neural network to generate text. The model is trained on a dataset of tweets related to Lionel Messi and performs text generation based on the input provided.

## Code Overview

The code is written in Python and consists of the following main components:

1. Data Preprocessing: The dataset is preprocessed using various techniques, including removing links, special characters, and emojis, and tokenizing the text.

2. Tokenization: The text is tokenized into sequences of words. The unique tokens are identified, and a mapping is created to assign an index to each token.

3. Training of LSTM NN: An LSTM neural network is created and trained on the tokenized data. The model architecture includes bidirectional LSTM layers, dropout layers, dense layers, and activation layers.

4. Text Generation: The trained model is used to generate text based on the given input. The next word predictions are made using the model, and a specified number of possible words are selected.

5. Voice Module: The code includes a voice module that utilizes the SpeechRecognition and pyttsx3 libraries to enable text-to-speech functionality. The user can speak the input, which is then processed and used for text generation.

## Usage

To use the code, follow these steps:

1. Install the required libraries by running `pip install -r requirements.txt`.

2. Download the dataset files mentioned in the code comments. Some files might be large and not included in the repository.

3. Run the code in a Python environment, ensuring that all the dependencies are properly installed.

4. You can modify the code to experiment with different input phrases, text lengths, and creativity levels for text generation.

5. If you want to use the voice module, ensure that your system has a working microphone and speaker. The code will prompt you to speak the input, and the generated text will be spoken back to you.

## Further Improvements

The code provided serves as a starting point for text generation tasks using LSTM neural networks. Here are some possible areas for improvement:

- Experiment with different model architectures and hyperparameters to achieve better performance and generate more coherent text.

- Explore using different datasets to train the model on a broader range of text sources.

- Incorporate techniques like attention mechanisms or transformer architectures to enhance the model's ability to capture long-range dependencies.

- Optimize the code for efficiency and speed, especially during the data preprocessing and tokenization steps.

- Enhance the voice module to handle a wider range of input scenarios and provide a more interactive user experience.

Please note that the code provided here is a simplified version for demonstration purposes, and further refinement and customization might be required for specific use cases.

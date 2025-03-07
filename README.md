# Chatbot-For-Original-Taste
# Chatbot System

## Overview
This is a chatbot system designed to extract relevant information from users based on their queries. The chatbot processes natural language input, retrieves key details, and provides structured responses.

## Features
- **Few-Shots**: Few shots examples in order to enhance the selection
- **Memory**: Retains conversation history to enhance user interactions.
- **Item Availability Verification**: Checks whether an item is in stock.
- **Total Estimation**: Calculates the estimated total cost of selected items.
- **Order Reinstate**: Allows users to reinstate previous orders.
- **ReAct Framework**: Identifies whether the customer has completed their order.
- **Payment System Integration**: Uses LangGraph to process payments securely.
- **Tailored Info Marketing**: Provides personalized marketing recommendations.

## Installation
### Prerequisites
- Users must bring their own API key from LLM providers (OpenAI).
- Python 3.10+
- Poetry (for dependency management)

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```
3. Run the chatbot:
   ```bash
   poetry run python main.py
   ```

## Usage
- Start the chatbot and interact via the command line or web interface.
- Provide relevant input, and the chatbot will extract information accordingly.

## Future Enhancements
Planned features include:
- **Integration with LINE** for seamless messaging support.
- **Voice Command Support** to enable hands-free interactions.
- **Multi-Language Support** for better accessibility.
- **Cloud Deployment** for improved scalability and performance.

## Contributing
Feel free to open issues and submit pull requests to improve this chatbot system.

## License
This project is licensed under the MIT License.


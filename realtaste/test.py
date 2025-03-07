def convert_data_to_message(reference_examples):
    """
    Converts each Data object to a LangGraph-compatible message.

    Args:
        reference_examples (list): List of examples, where each example is a dictionary containing "tool_calls".

    Returns:
        list: List of LangGraph-compatible messages.
    """
    data_obj = []

    for example in reference_examples:
        # Debugging print statements
        print(type(example["tool_calls"]))  # To check the type of example["tool_calls"]
        print(example["tool_calls"])  # To see the actual value of example["tool_calls"]

        # Ensure example["tool_calls"] is a list and has at least one element
        if isinstance(example["tool_calls"], list) and len(example["tool_calls"]) > 0:
            data_obj.append(data_to_message(example["tool_calls"][0]))
        else:
            print("Warning: 'tool_calls' is either not a list or is empty for this example.")

    return data_obj

# Usage example
# reference_examples = [...]  # Your list of reference examples
# result = convert_data_to_message(reference_examples)
# print(result)

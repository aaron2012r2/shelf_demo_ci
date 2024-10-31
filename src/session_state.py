import streamlit as st


def initialize_session_state() -> None:
    """
    Initializes the session state for storing chat messages if not already present.
    """
    if "messages" not in st.session_state:
        st.session_state.messages = []


def add_llm_response_to_chat_history(llm_response: str, source_inforamtion: str) -> None:
    """
    Adds the response from a language model (LLM) and the associated source information to the chat history.

    Args:
        llm_response (str): The response generated by the language model.
        source_inforamtion (str): The source information associated with the response.
    """
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": f"{llm_response}\n" + source_inforamtion,
        }
    )


def clear_chat_history() -> None:
    """
    Clear chat history.
    """
    st.session_state.messages = []


def display_chat_messages_from_history() -> None:
    """
    Displays chat messages from history on app rerun.
    """
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

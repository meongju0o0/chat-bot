import streamlit as st
from langchain_core.messages import ChatMessage

class ChatWeb:
    def __init__(self, page_title="Gazzi Chatbot", page_icon=":books:"):
        self._page_title = page_title
        self._page_icon = page_icon
    
    def print_messages(self):
        if "messages" in st.session_state and len(st.session_state["messages"]) > 0:
            for chat_message in st.session_state["messages"]:
                st.chat_message(chat_message.role).write(chat_message.content)
    
    def run(self):
        st.set_page_config(
            page_title=self._page_title,
            page_icon=self._page_icon
        )
        st.title(self._page_title)

        # Ensure session state has "messages"
        if "messages" not in st.session_state:
            st.session_state["messages"] = []
        
        self.print_messages()

        # Handle user input
        if user_input := st.chat_input("질문을 입력해 주세요."):
            # Add user's message to session state
            user_message = ChatMessage(role="user", content=user_input)
            st.session_state["messages"].append(user_message)
            st.chat_message("user").write(user_input)
        
            # Generate assistant's response
            with st.chat_message("assistant"):
                msg_assistant = f"당신이 입력한 내용: {user_input}"
                st.write(msg_assistant)
                assistant_message = ChatMessage(role="assistant", content=msg_assistant)
                st.session_state["messages"].append(assistant_message)

if __name__ == '__main__':
    web = ChatWeb()
    web.run()

import os
from langchain_google_vertexai.model_garden import ChatAnthropicVertex
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig

import chainlit as cl

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "service_account.json"

"""
@cl.set_chat_profiles
async def chat_profile():
    return [
        cl.ChatProfile(
            name="Gemini",
            markdown_description="The underlying LLM model is **Gemini Pro**.",
            icon="https://picsum.photos/200",
        ),
        cl.ChatProfile(
            name="Claude-3 Sonnet",
            markdown_description="The underlying LLM model is **Claude-3 Sonnet**.",
            icon="https://picsum.photos/250",
        ),
    ]
"""

@cl.on_chat_start
async def on_chat_start():
    #model = ChatOpenAI(streaming=True)
    model = ChatAnthropicVertex(
        model_name="claude-3-sonnet@20240229",
        project='vtxclass',
        location="asia-southeast1"
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You're a very knowledgeable historian who provides accurate and eloquent answers to historical questions.",
            ),
            ("human", "{question}"),
        ]
    )
    runnable = prompt | model | StrOutputParser()
    cl.user_session.set("runnable", runnable)


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  # type: Runnable

    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()

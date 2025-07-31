import os
from dotenv import load_dotenv
# from langchain_ollama import ChatOllama
from langchain.chat_models import init_chat_model
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import(
    create_react_agent,
    AgentExecutor,
)
from langchain import hub #pre-made prompts made by langchain community.
# from Tools.tools import get_prof_url
from Tools.tools import get_prof_url

load_dotenv()


def lookup(name: str) -> str:
    llm = init_chat_model(
        model="gemini-2.5-flash",
        model_provider="google_genai"
    )

    template = """given the full name {name_of_person} I want you to get me a link to their Linkedin profile page.
                        Your answer should contain only URL."""
    
    prompt_template = PromptTemplate(template= template, input_variables=["name_of_person"])
    tools_for_agent = [Tool(
        name= "Crawl Google 4 Linkedin Profile page",
        func = get_prof_url,
        description="useful for when you need to get the Linkedin Page URL"
    )]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose= True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format(name_of_person=name)}
    )

    linkedin_prof_url = result["output"]
    return linkedin_prof_url

if __name__ == "__main__":
    linkedin_url = lookup(name="Mahin Dhoke")
    print(linkedin_url)
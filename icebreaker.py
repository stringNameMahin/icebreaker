import os
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
# from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain.chains import LLMChain
from thirdparties.linkedin import scrape_linkedin_profile

if __name__== "__main__":
    load_dotenv()

    print("Hello LangChain")

    summary_template = """give the LinkedIn information {information} about a person I want you to create: 
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    # llm = ChatOpenAI(temperature=0.0, model="gpt-3.5-turbo")
    llm = ChatOllama(model="Llama3")

    chain = summary_prompt_template | llm
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url = "https://www.linkedin.com/in/eden-marco/"
    )
    res = chain.invoke(input={"information": linkedin_data})

    print(res.content) #Remove the .content for a more AI like output, .content just converts it to simple text like you would have if one used an LLM like chatgpt or gemini.
import os
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain
from thirdparties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from langchain.chat_models import init_chat_model
from output_parser import Summary_parser, Summary

def icebreak_with(name: str) -> tuple[Summary, str]:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_url = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)
    
    summary_template = """give the LinkedIn information {information} about a person I want you to create: 
    1. A short summary
    2. two interesting facts about them
    \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template,
                                             partial_variables={"format_instructions": Summary_parser.get_format_instructions()} #partial vars is used specifically for using output parsing template, a premade schema.
                                             )
    

    llm = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")

    #chain = summary_prompt_template | llm
    chain = summary_prompt_template | llm | Summary_parser

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url = linkedin_username
    )
    res:Summary = chain.invoke(input={"information": linkedin_data})

    return res, linkedin_data.get("photoUrl")
    
    #print(res.content) #Remove the .content for a more AI like output, .content just converts it to simple text like you would have if one used an LLM like chatgpt or gemini.


if __name__== "__main__":
    load_dotenv()
    print("Ice Breaker")
    # inp = input("Enter a name to be searched: ")
    inp = input("Enter a name to be searched: ")
    # print(f"DEBUG: inp = '{inp}'")

    icebreak_with(name=inp)
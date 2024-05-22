from agency_swarm import Agency
from SeniorProofreaderAgent import SeniorProofreaderAgent
from SeniorCopywriterAgent import SeniorCopywriterAgent
from SeniorCEOAgent import SeniorCEOAgent

senior_ceo = SeniorCEOAgent()
senior_copywriter = SeniorCopywriterAgent()
senior_proof_reader = SeniorProofreaderAgent()

agency = Agency([senior_ceo, 
                 [senior_ceo, senior_copywriter, senior_proof_reader]],
                shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                max_prompt_tokens=25000,  # default tokens in conversation for all agents
                temperature=0.3,  # default temperature for all agents
                )

if __name__ == '__main__':
    agency.demo_gradio()
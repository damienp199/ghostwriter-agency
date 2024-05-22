from flask import Flask, request, jsonify
import os

from agency_swarm import Agency
from YouTubeGhostwriterAgency.SeniorProofreaderAgent import SeniorProofreaderAgent
from YouTubeGhostwriterAgency.SeniorCopywriterAgent import SeniorCopywriterAgent
from YouTubeGhostwriterAgency.SeniorCEOAgent import SeniorCEOAgent

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Heroku!"

@app.route('/agency', methods=['POST'])
def agency():

    # get the prompt from the request
    data = request.get_json()
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided!'}), 400
    
    # create the agency
    senior_ceo = SeniorCEOAgent()
    senior_copywriter = SeniorCopywriterAgent()
    senior_proof_reader = SeniorProofreaderAgent()

    agency = Agency([senior_ceo, 
                    [senior_ceo, senior_copywriter, senior_proof_reader]],
                    shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                    max_prompt_tokens=25000,  # default tokens in conversation for all agents
                    temperature=0.3,  # default temperature for all agents
                    )

    #agency.demo_gradio()

    result = agency.get_completion(prompt)
    
    return jsonify({'result': result})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
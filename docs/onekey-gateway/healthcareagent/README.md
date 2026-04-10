# AI Agent for Healthcare: HeathcareAgent Pypi Package for Common Agentic APIs and Awesome Healthcare AI Agent Projects

This is the official github repo of pypi package HeathcareAgent. This repo is intended to provide common APIs interface to help develop Healthcare related AI Agents.

***IMPORTANT LEGAL DISCLAIMER***

HeathcareAgent is not affiliated, endorsed, or vetted by Heathcare Agents or Institutions. It's an open-source tool that uses finance APIs.

In healthcare industry, many professionals can benefit from AI technology especially the AI Agent and LLM (ChatGPT style chatbot). 
Here are some key professionals whose workflow and productivity can be improved by AI Agents technology. They can be released from heavy burden of paper work, writing reports, making general advice and consulting, etc. 

- Health coaches/nutritionists: Health coaches and nutritionists are nutrition professionals who offer advice on diet and health.  A health professional, healthcare professional, or healthcare worker is a provider of health care treatment and advice based on formal training and experience. 
- Surgeon: Many different types of surgeons, and they all go through extensive training before they are allowed to practice independently. Surgeons might specialize in orthopedics, neurology, cardiothoracic, or abdominal surgeries. While surgeons are highly paid, they have a big responsibility to keep their patients safe and make sure the entire operating room staff is performing well. 
- Nurses
- Dentists
- Pharmacist
- Radiographer/Optician and other professionals.
- Surgical Tech


### AI Agent for Healthcare Types and Awesome Projects

| Application  | AI Agent| Description   |
|  ----  | ----  | ----  |
|  Clinical Decision Support  | [IBM Watson Health](https://www.ibm.com/industries/healthcare) |  Helps analyze medical literature and patient data to provide evidence-based treatment recommendations. | 
|  Clinical Decision Support  | [Infermedica](https://infermedica.com/) |  Provides diagnostic support and triage for healthcare professionals. | 
|  Clinical Decision Support  | [Buoy Health](https://www.buoyhealth.com/) |  A chatbot for symptom checking and guiding users to appropriate care. | 
|  Virtual Health Assistants  | [Ada Health](https://ada.com/) |  Symptom checker and health assessment app with AI-driven insights. | 
|  Virtual Health Assistants  | [Babylon Health](https://en.wikipedia.org/wiki/Babylon_Health) |  Provides symptom checks, virtual consultations, and health monitoring tools. | 
|  Virtual Health Assistants  | [Sensely](https://apps.apple.com/us/app/sensely/id871632284) |  A virtual assistant for managing chronic conditions and improving patient engagement. | 
|  Patient Management  | [HealthTap](https://www.healthtap.com/telehealth/) |  Offers virtual doctor consultations and AI-based symptom checking. | 
|  Patient Management  | [Ginger](https://my.ginger.com/) |  Mental health AI for providing chat-based therapy and support. | 
|  Medical Imaging and Diagnostics  | [Aidoc](https://www.aidoc.com/) |  AI-powered imaging analysis for detecting anomalies in radiology scans. | 
|  Medical Imaging and Diagnostics  | [Zebra Medical Vision](https://www.zebra.cn/cn/zh/solutions.html) |  Automates the analysis of medical imaging data for early detection of diseases. | 
|  Medical Imaging and Diagnostics  | [Arterys](https://www.arterys.com/) |  Uses AI for advanced imaging in cardiology, oncology, and other specialties. | 
|  Drug Discovery and Development  | [Atomwise](https://www.atomwise.com/) |  AI-driven platform for discovering potential drug compounds. | 
|  Drug Discovery and Development  | [BenevolentAI](https://www.benevolent.com/) |  Combines AI and biomedical data to accelerate drug discovery. | 
|  Drug Discovery and Development  | [DeepMind (AlphaFold)](https://deepmind.google/technologies/alphafold/) |  Revolutionizes protein folding predictions for pharmaceutical research. | 
|  Mental Health and Therapy  |  [Woebot](https://woebothealth.com/) |  A chatbot offering cognitive behavioral therapy (CBT) for anxiety and depression. | 
|  Mental Health and Therapy  |  [Replika](https://replika.com/) |  Acts as a conversational agent for emotional support and companionship. | 
|  Mental Health and Therapy  |  [Wysa](https://www.wysa.com/) |  AI for mental health assistance, focusing on stress and emotional well-being. | 
|  Personalized Medicine  |  [23andMe AI](https://therapeutics.23andme.com/our-platform/) |  Uses genetic data to provide personalized health insights and risk assessments. | 
|  Personalized Medicine  |  [Tempus](https://www.tempus.com/) |  Employs AI to personalize cancer treatments based on genetic and molecular data. | 
|  Chronic Disease Management  |  [Livongo](https://www.livongo.com/) |  Combines AI with connected devices for managing diabetes, hypertension, and weight loss. | 
|  Chronic Disease Management  |  [Omada Health](https://www.omadahealth.com/) |  AI-based coaching for chronic disease prevention and management. | 
|  Elderly Care and Accessibility |  [EllieQ by Intuition Robotics](https://elliq.com/) |  AI companion for reducing loneliness and enhancing quality of life in seniors. | 
|  Elderly Care and Accessibility |  [Paro Robot](https://www.parorobots.com/) | Therapeutic AI robot designed for dementia and Alzheimer’s patients. | 
|  Workflow Optimization |  [DeepScribe](https://www.deepscribe.ai/) | AI-powered medical scribe to automate clinical documentation. | 
|  Workflow Optimization |  [Nuance Dragon Medical](https://www.nuance.com/healthcare/dragon-ai-clinical-solutions.html) | Speech recognition AI for documenting patient encounters. |
|  Healthcare Administration |  [Healthcare Admin Agents](https://github.com/ajhcs/healthcare-agents) | 51 open-source AI agents with MHA-level expertise across 10 divisions including revenue cycle, compliance, quality, clinical ops, payer relations, health IT, and pharmacy. Features real regulatory citations (42 CFR, CMS) and works with Claude Code, Codex CLI, and Gemini CLI. | 


### AI Agent for Healthcare Common APIs

|  API NAME  | SOURCE | WEBSITE |DESCRIPTION  |
|  ----  | ----  | ----  | ---- |
|  food_calories_usda  | USDA | https://fdc.nal.usda.gov/ |U.S. Department of Agriculture Food Search for Ingredients and Calories |
| Supplement Drug Interaction Safety | Truthstack Co | https://api.truthstack.co/api/interactions/check | Truthstack Co |



![USDA Food Ingredients and Energies](https://raw.githubusercontent.com/AI-Hub-Admin/HealthcareAgent/refs/heads/main/doc/usda_demo.jpg?raw=true)


### Install
```
pip install HealthcareAgent
```

### Run Case

```

import HealthcareAgent as ha

def run_fetch_health_food_calories():

    ## group 1:
    print ("DEBUG: ### Food Nutritions for Brand Starbucks")
    result_dict = ha.api(api_name="food_calories_usda", query="Starbucks", topk=10)
    item_list = result_dict["item_list"]
    item_dict = result_dict["item_dict"]
    item_list_pretty = result_dict["item_list_pretty"]
    print ("DEBUG: ## Return Item List")
    print (item_list)
    print ("DEBUG: ## Return Item Dict")    
    print (item_dict)
    print ("DEBUG: ## Return Item Print Pretty")        
    [print (line) for line in item_list_pretty]


    ## group 2:
    print ("DEBUG: ### Food Nutritions for Peet's Coffee")
    result_dict = ha.api(api_name="food_calories_usda", query="peet", topk=10)
    item_list = result_dict["item_list"]
    item_dict = result_dict["item_dict"]
    item_list_pretty = result_dict["item_list_pretty"]
    print ("DEBUG: ## Return Item List")
    print (item_list)
    print ("DEBUG: ## Return Item Dict")    
    print (item_dict)
    print ("DEBUG: ## Return Item Print Pretty")        
    [print (line) for line in item_list_pretty]


def main():
    run_fetch_health_food_calories()

if __name__ == '__main__':
    main()

```

**Use Case 1: Nutritionist AI Agent Find Food Calories of Starbucks Coffee**


```


1. CHILLED COFFEE DRINK
$$starbucks CHILLED COFFEE DRINK(#image)$$
Every 100g:
Energy71.0KCALFiber, total dietary0.0G
Calcium, Ca85.0MG
Iron, Fe0.09MG
Vitamin A, IU0.0IU
Vitamin C, total ascorbic acid0.0MG
Protein2.19G
Total lipid (fat)1.09G
Carbohydrate, by difference12.9G
Total Sugars11.2G
Sodium, Na36.0MG
Cholesterol5.0MG
Fatty acids, total trans0.0G
Fatty acids, total saturated0.73G


2. CLASSIC HOT COCOA MIX, CLASSIC
$$starbucks CLASSIC HOT COCOA MIX, CLASSIC(#image)$$
Every 100g:
Energy357KCALProtein7.14G
Total lipid (fat)8.93G
Carbohydrate, by difference78.6G
Total Sugars60.7G
Fiber, total dietary10.7G
Calcium, Ca57.0MG
Iron, Fe14.3MG
Potassium, K986MG
Sodium, Na0.0MG
Vitamin D (D2 + D3), International Units0.0IU
Sugars, added57.1G
Cholesterol0.0MG
Fatty acids, total trans0.0G
Fatty acids, total saturated5.36G


3. COFFEE & PROTEIN BEVERAGE
$$starbucks COFFEE & PROTEIN BEVERAGE(#image)$$
Every 100g:
Energy61.0KCALCalcium, Ca91.0MG
Iron, Fe0.11MG
Vitamin A, IU0.0IU
Vitamin C, total ascorbic acid0.0MG
Protein6.06G
Total lipid (fat)0.76G
Carbohydrate, by difference10.3G
Total Sugars6.36G
Fiber, total dietary0.6G
Sodium, Na36.0MG
Cholesterol3.0MG
Fatty acids, total trans0.0G
Fatty acids, total saturated0.45G


4. COLD BREW PREMIUM COFFEE DRINK WITH CREAM
$$starbucks COLD BREW PREMIUM COFFEE DRINK WITH CREAM(#image)$$
Every 100g:
Energy46.0KCALFiber, total dietary0.0G
Calcium, Ca46.0MG
Iron, Fe0.11MG
Vitamin A, IU0.0IU
Vitamin C, total ascorbic acid0.0MG
Protein1.54G
Total lipid (fat)1.38G
Carbohydrate, by difference7.38G
Total Sugars6.46G
Sodium, Na52.0MG
Cholesterol5.0MG
Fatty acids, total trans0.0G
Fatty acids, total saturated0.77G


5. ENERGY COFFEE BEVERAGE
$$starbucks ENERGY COFFEE BEVERAGE(#image)$$
Every 100g:
Energy45.0KCALCalcium, Ca90.0MG
Iron, Fe0.08MG
Vitamin A, IU90.0IU
Vitamin D (D2 + D3), International Units18.0IU
Vitamin C, total ascorbic acid6.8MG
Riboflavin0.767MG
Niacin9.03MG
Vitamin B-60.903MG
Protein2.26G
Total lipid (fat)0.68G
Carbohydrate, by difference7.67G
Total Sugars6.55G
Fiber, total dietary0.2G
Potassium, K237MG
Sodium, Na38.0MG
Cholesterol3.0MG
Fatty acids, total trans0.0G
Fatty acids, total saturated0.34G


6. ESPRESSO BEVERAGE
$$starbucks ESPRESSO BEVERAGE(#image)$$
Every 100g:
Energy60.0KCALCalcium, Ca72.0MG
Iron, Fe0.17MG
Vitamin A, IU24.0IU
Vitamin C, total ascorbic acid0.0MG
Protein2.42G
Total lipid (fat)1.09G
Carbohydrate, by difference9.9G
Total Sugars9.18G
Fiber, total dietary0.2G
Sodium, Na68.0MG
Cholesterol4.0MG
Fatty acids, total trans0.0G
Fatty acids, total saturated0.72G


7. ESPRESSO BEVERAGE, SMOKED BUTTERSCOTCH LATTE
$$starbucks ESPRESSO BEVERAGE, SMOKED BUTTERSCOTCH LATTE(#image)$$
Every 100g:
Energy53.0KCALFiber, total dietary0.0G
Calcium, Ca60.0MG
Iron, Fe0.0MG
Vitamin A, IU24.0IU
Vitamin C, total ascorbic acid0.0MG
Protein1.93G
Total lipid (fat)1.09G
Carbohydrate, by difference8.7G
Total Sugars8.21G
Sodium, Na27.0MG
Cholesterol4.0MG
Fatty acids, total trans0.0G
Fatty acids, total saturated0.72G


8. FRAPPUCCINO CHILLED COFFEE DRINK
$$starbucks FRAPPUCCINO CHILLED COFFEE DRINK(#image)$$
Every 100g:
Energy73.0KCALCalcium, Ca73.0MG
Iron, Fe0.18MG
Vitamin A, IU0.0IU
Vitamin C, total ascorbic acid0.0MG
Protein2.43G
Total lipid (fat)1.09G
Carbohydrate, by difference13.1G
Total Sugars11.4G
Fiber, total dietary0.2G
Sodium, Na34.0MG
Cholesterol5.0MG
Fatty acids, total trans0.0G
Fatty acids, total saturated0.73G


9. ICED COFFEE
$$starbucks ICED COFFEE(#image)$$
Every 100g:
Energy33.0KCALFiber, total dietary0.0G
Calcium, Ca18.0MG
Iron, Fe0.0MG
Vitamin A, IU30.0IU
Vitamin C, total ascorbic acid0.0MG
Fatty acids, total saturated0.0G
Protein0.3G
Total lipid (fat)0.15G
Carbohydrate, by difference6.97G
Total Sugars6.36G
Sodium, Na6.0MG
Cholesterol2.0MG
Fatty acids, total trans0.0G


10. JUICE BLEND DRINK FROM CONCENTRATE
$$starbucks JUICE BLEND DRINK FROM CONCENTRATE(#image)$$
Every 100g:
Energy25.0KCALTotal lipid (fat)0.0G
Fiber, total dietary0.0G
Calcium, Ca6.0MG
Iron, Fe0.0MG
Vitamin A, IU0.0IU
Vitamin C, total ascorbic acid16.9MG
Niacin2.25MG
Pantothenic acid1.27MG
Vitamin B-60.254MG
Cholesterol0.0MG
Fatty acids, total saturated0.0G
Protein0.0G
Carbohydrate, by difference6.2G
Total Sugars5.35G
Sodium, Na13.0MG
Fatty acids, total trans0.0G


```


### Related Blogs
[AI Agent Frameworks Benchmarks Types Examples and Marketplace Review A Comprehensive List](http://www.deepnlp.org/blog/ai-agent-review-benchmarks-and-environment-a-comprehensive-list) <br>
[Introduction to multimodal generative models](http://www.deepnlp.org/blog/introduction-to-multimodal-generative-models) <br>
[Generative AI Search Engine Optimization](http://www.deepnlp.org/blog/generative-ai-search-engine-optimization-how-to-improve-your-content) <br>
[AI Image Generator User Reviews](http://www.deepnlp.org/store/image-generator) <br>
[AI Video Generator User Reviews](http://www.deepnlp.org/store/video-generator) <br>
[AI Chatbot & Assistant Reviews](http://www.deepnlp.org/store/chatbot-assistant) <br>
[AI Store-Best AI Tools User Reviews](http://www.deepnlp.org/store/pub/) <br>
[AI Store Use Cases-Best AI Tools Cases User Reviews](http://www.deepnlp.org/store) <br>

### Agents Related Pipeline Workflow and Document
#### Search AI Agent & Robotics
[AI Agent Marketplace and Search](http://www.deepnlp.org/search/agent) <br>
[Robot Search](http://www.deepnlp.org/search/robot) <br>
[Equation and Academic search](http://www.deepnlp.org/search/equation) <br>
[AI & Robot Comprehensive Search](http://www.deepnlp.org/search) <br>
[AI & Robot Question](http://www.deepnlp.org/question) <br>
[AI & Robot Community](http://www.deepnlp.org/community) <br>
[AI Agent Marketplace Blog](http://www.deepnlp.org/blog/ai-agent-marketplace-and-search-portal-reviews-2025) <br>

#### AI Agent
[Microsoft AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-microsoft-ai-agent) <br>
[Claude AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-claude-ai-agent) <br>
[OpenAI AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-openai-ai-agent) <br>
[AgentGPT AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-agentgpt) <br>
[Saleforce AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-salesforce-ai-agent) <br>
[Google AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-google-ai-agent) <br>
[AI Agent Builder Reviews](http://www.deepnlp.org/store/ai-agent/ai-agent-builder) <br>
[AI Agent Board Visualization](https://ai-hub-admin.github.io/agentboard) <br>
[AI Agent Board](https://ai-hub-admin.github.io/agentboard) <br>
[AI Agent Pro Master](https://agentpromaster.github.io/ai-agent) <br>
[RAG Visualizer Agent](https://aiforce1024.github.io/rag_tutorial) <br>
[Chat Visualizer Agent](https://llmpro70b.github.io/Chat-Visualizer) <br>

### AI Services Reviews and Ratings <br>
##### Chatbot
[OpenAI o1 Reviews](http://www.deepnlp.org/store/pub/pub-openai-o1) <br>
[ChatGPT User Reviews](http://www.deepnlp.org/store/pub/pub-chatgpt-openai) <br>
[Gemini User Reviews](http://www.deepnlp.org/store/pub/pub-gemini-google) <br>
[Perplexity User Reviews](http://www.deepnlp.org/store/pub/pub-perplexity) <br>
[Claude User Reviews](http://www.deepnlp.org/store/pub/pub-claude-anthropic) <br>
[Qwen AI Reviews](http://www.deepnlp.org/store/pub/pub-qwen-alibaba) <br>
[Doubao Reviews](http://www.deepnlp.org/store/pub/pub-doubao-douyin) <br>
[ChatGPT Strawberry](http://www.deepnlp.org/store/pub/pub-chatgpt-strawberry) <br>
[Zhipu AI Reviews](http://www.deepnlp.org/store/pub/pub-zhipu-ai) <br>
##### AI Image Generation
[Midjourney User Reviews](http://www.deepnlp.org/store/pub/pub-midjourney) <br>
[Stable Diffusion User Reviews](http://www.deepnlp.org/store/pub/pub-stable-diffusion) <br>
[Runway User Reviews](http://www.deepnlp.org/store/pub/pub-runway) <br>
[GPT-5 Forecast](http://www.deepnlp.org/store/pub/pub-gpt-5) <br>
[Flux AI Reviews](http://www.deepnlp.org/store/pub/pub-flux-1-black-forest-lab) <br>
[Canva User Reviews](http://www.deepnlp.org/store/pub/pub-canva) <br>
##### AI Video Generation
[Luma AI](http://www.deepnlp.org/store/pub/pub-luma-ai) <br>
[Pika AI Reviews](http://www.deepnlp.org/store/pub/pub-pika) <br>
[Runway AI Reviews](http://www.deepnlp.org/store/pub/pub-runway) <br>
[Kling AI Reviews](http://www.deepnlp.org/store/pub/pub-kling-kwai) <br>
[Dreamina AI Reviews](http://www.deepnlp.org/store/pub/pub-dreamina-douyin) <br>
##### AI Education
[Coursera Reviews](http://www.deepnlp.org/store/pub/pub-coursera) <br>
[Udacity Reviews](http://www.deepnlp.org/store/pub/pub-udacity) <br>
[Grammarly Reviews](http://www.deepnlp.org/store/pub/pub-grammarly) <br>
##### Robotics
[Tesla Cybercab Robotaxi](http://www.deepnlp.org/store/pub/pub-tesla-cybercab) <br>
[Tesla Optimus](http://www.deepnlp.org/store/pub/pub-tesla-optimus) <br>
[Figure AI](http://www.deepnlp.org/store/pub/pub-figure-ai) <br>
[Unitree Robotics Reviews](http://www.deepnlp.org/store/pub/pub-unitree-robotics) <br>
[Waymo User Reviews](http://www.deepnlp.org/store/pub/pub-waymo-google) <br>
[ANYbotics Reviews](http://www.deepnlp.org/store/pub/pub-anybotics) <br>
[Boston Dynamics](http://www.deepnlp.org/store/pub/pub-boston-dynamic) <br>
## Reasoning
[OpenAI o1 Reviews](http://www.deepnlp.org/store/pub/pub-openai-o1) <br>
[OpenAI o3 Reviews](http://www.deepnlp.org/store/pub/pub-openai-o3) <br>
##### AI Tools
[DeepNLP AI Tools](http://www.deepnlp.org/store/pub/pub-deepnlp-ai) <br>
##### AI Widgets
[Apple Glasses](http://www.deepnlp.org/store/pub/pub-apple-glasses) <br>
[Meta Glasses](http://www.deepnlp.org/store/pub/pub-meta-glasses) <br>
[Apple AR VR Headset](http://www.deepnlp.org/store/pub/pub-apple-ar-vr-headset) <br>
[Google Glass](http://www.deepnlp.org/store/pub/pub-google-glass) <br>
[Meta VR Headset](http://www.deepnlp.org/store/pub/pub-meta-vr-headset) <br>
[Google AR VR Headsets](http://www.deepnlp.org/store/pub/pub-google-ar-vr-headset) <br>
##### Social
[Character AI](http://www.deepnlp.org/store/pub/pub-character-ai) <br>
##### Self-Driving
[BYD Seal](http://www.deepnlp.org/store/pub/pub-byd-seal) <br>
[Tesla Model 3](http://www.deepnlp.org/store/pub/pub-tesla-model-3) <br>
[BMW i4](http://www.deepnlp.org/store/pub/pub-bmw-i4) <br>
[Baidu Apollo Reviews](http://www.deepnlp.org/store/pub/pub-baidu-apollo) <br>
[Hyundai IONIQ 6](http://www.deepnlp.org/store/pub/pub-hyundai-ioniq-6) <br>



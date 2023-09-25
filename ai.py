import openai
import os
def call_ai(Query):

    api_key = os.environ.get('OPENAI_API_KEY')
            # Initialize the OpenAI API client
    openai.api_key  = api_key
  
    prompt = Query
            # Generate a response using the OpenAI GPT-3.5 Turbo model
    response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "user", "content": prompt}],
                max_tokens=300, # Adjust the length of the generated response
                stop=None, 
                temperature= 0.5 # You can specify a stop word to end the response if needed
            )

            # Extract and print the generated answer
    answer = response.choices[0]["message"]["content"]
    return answer
    # return """Hey ChatGpt You Are A genius Dotor. You have a 10 years of experience in medical science field. 
    #         your job is to solve patient queries regarding what he can feel about his body and being a doctor 
    #          you have to suggest him with best advices and prescribtion and also suggest the query realated body 
    #          test and also please be sure that your answer is formated like a sugguestion not a proper solution format
    #          and also give a disclaimer that i am a ai not a doctor :
    #          and The user query is """